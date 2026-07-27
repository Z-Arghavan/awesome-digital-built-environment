"""
Shared logic for GitHub repo discovery scripts.

Not run directly. find_ifc_repos.py and find_new_digital_built_environment_repos.py
both import run() from this module and only differ in which categories/queries
they search and which tracking issue they update.
"""

import os
import re
import sys
import time
import requests

GITHUB_API = "https://api.github.com"
README_PATH = "README.md"

MIN_STARS = 2
EXCLUDE_FORKS = True
PER_PAGE = 100           # GitHub's max per page
MAX_PAGES = 5             # 5 pages x 100 = up to 500 results per query
REQUEST_DELAY = 2         # seconds between requests, stays well under rate limits
MAX_PER_CATEGORY = 25     # cap listed candidates per category to keep issue readable
MAX_DESC_LENGTH = 120     # truncate long repo descriptions
MAX_BODY_LENGTH = 60000   # stay under GitHub's 65536-char issue body limit


def existing_urls():
    """Extract all github.com URLs already present in README.md."""
    with open(README_PATH, encoding="utf-8") as f:
        text = f.read()
    return set(re.findall(r"https://github\.com/[\w\-./]+", text))


def search_repos(query, seen_ids, headers):
    url = f"{GITHUB_API}/search/repositories"
    results = []
    for page in range(1, MAX_PAGES + 1):
        params = {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": PER_PAGE,
            "page": page,
        }
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        resp.raise_for_status()
        items = resp.json().get("items", [])
        if not items:
            break

        for item in items:
            if item["id"] in seen_ids:
                continue
            if EXCLUDE_FORKS and item.get("fork"):
                continue
            if item.get("stargazers_count", 0) < MIN_STARS:
                continue
            seen_ids.add(item["id"])
            results.append(item)

        if len(items) < PER_PAGE:
            break

        time.sleep(REQUEST_DELAY)
    return results


def build_issue_body(candidates_by_category):
    lines = [
        "Automatically discovered repositories that may fit this awesome list.",
        "Review each one, then either add it to README.md or check it off if not relevant.",
        "",
    ]
    for category, candidates in candidates_by_category.items():
        if not candidates:
            continue
        lines.append(f"### {category}")
        for repo in candidates[:MAX_PER_CATEGORY]:
            desc = repo["description"] or "no description"
            if len(desc) > MAX_DESC_LENGTH:
                desc = desc[:MAX_DESC_LENGTH].rsplit(" ", 1)[0] + "..."
            lines.append(
                f"- [ ] [{repo['full_name']}]({repo['html_url']}) "
                f"({repo['stargazers_count']} stars): {desc}"
            )
        lines.append("")

    body = "\n".join(lines)
    if len(body) > MAX_BODY_LENGTH:
        body = body[:MAX_BODY_LENGTH]
        body += "\n\n_List truncated, too many candidates to fit in one issue. Lower MAX_PER_CATEGORY or MIN_STARS to narrow results next run._"
    return body


def find_open_tracking_issue(repo, headers, title, label):
    url = f"{GITHUB_API}/repos/{repo}/issues"
    params = {"state": "open", "labels": label, "per_page": 10}
    resp = requests.get(url, headers=headers, params=params, timeout=30)
    resp.raise_for_status()
    for issue in resp.json():
        if issue["title"] == title:
            return issue
    return None


def create_or_update_issue(repo, headers, title, label, body):
    existing = find_open_tracking_issue(repo, headers, title, label)
    if existing:
        url = f"{GITHUB_API}/repos/{repo}/issues/{existing['number']}"
        resp = requests.patch(url, headers=headers, json={"body": body}, timeout=30)
    else:
        url = f"{GITHUB_API}/repos/{repo}/issues"
        payload = {"title": title, "body": body, "labels": [label]}
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
    if not resp.ok:
        print(f"GitHub API error {resp.status_code}: {resp.text}", file=sys.stderr)
    resp.raise_for_status()
    return resp.json()


def run(category_queries, issue_title, label):
    """Search all category_queries, dedupe against README.md, and file/update
    a tracking issue titled issue_title with the given label."""
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("GITHUB_TOKEN and GITHUB_REPOSITORY must be set.", file=sys.stderr)
        sys.exit(1)

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }

    known = existing_urls()
    seen_ids = set()
    candidates_by_category = {}
    total = 0

    for category, queries in category_queries.items():
        category_candidates = []
        for q in queries:
            for r in search_repos(q, seen_ids, headers):
                if r["html_url"] not in known:
                    category_candidates.append(r)
        category_candidates.sort(key=lambda r: r["stargazers_count"], reverse=True)
        candidates_by_category[category] = category_candidates
        total += len(category_candidates)

    if total == 0:
        print("No new candidates found.")
        return

    body = build_issue_body(candidates_by_category)
    issue = create_or_update_issue(repo, headers, issue_title, label, body)
    print(f"Updated issue #{issue['number']} with {total} candidates across {len(category_queries)} categories.")
