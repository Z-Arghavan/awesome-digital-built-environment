#!/usr/bin/env python3
"""
Find GitHub repositories related to IFC / BIM / openBIM that are not yet
listed in this repo's README.md, and open (or update) a tracking issue
with the candidates for manual review.

Curation stays manual on purpose: this script never edits README.md
directly, it only surfaces candidates as a checklist issue.
"""

import os
import re
import sys
import requests

GITHUB_API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN")
REPO = os.environ.get("GITHUB_REPOSITORY")  # e.g. "Z-Arghavan/Template-repo-for-test"
README_PATH = "README.md"
TRACKING_ISSUE_TITLE = "New IFC/BIM repos to review"
TRACKING_LABEL = "auto-discovery"

SEARCH_QUERIES = [
    "topic:ifc",
    "topic:openbim",
    "topic:bim",
    "topic:ifcopenshell",
    "topic:buildingsmart",
    "IFC BIM in:description,name",
]

MIN_STARS = 5
EXCLUDE_FORKS = True

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}


def existing_urls():
    """Extract all github.com URLs already present in README.md."""
    with open(README_PATH, encoding="utf-8") as f:
        text = f.read()
    return set(re.findall(r"https://github\.com/[\w\-./]+", text))


def search_repos(query, seen_ids):
    url = f"{GITHUB_API}/search/repositories"
    params = {"q": query, "sort": "stars", "order": "desc", "per_page": 30}
    resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
    resp.raise_for_status()
    results = []
    for item in resp.json().get("items", []):
        if item["id"] in seen_ids:
            continue
        if EXCLUDE_FORKS and item.get("fork"):
            continue
        if item.get("stargazers_count", 0) < MIN_STARS:
            continue
        seen_ids.add(item["id"])
        results.append(item)
    return results


def build_issue_body(candidates):
    lines = [
        "Automatically discovered repositories that may fit this awesome list.",
        "Review each one, then either add it to README.md or check it off if not relevant.",
        "",
    ]
    for repo in candidates:
        lines.append(
            f"- [ ] [{repo['full_name']}]({repo['html_url']}) "
            f"({repo['stargazers_count']} stars): {repo['description'] or 'no description'}"
        )
    return "\n".join(lines)


def find_open_tracking_issue():
    url = f"{GITHUB_API}/repos/{REPO}/issues"
    params = {"state": "open", "labels": TRACKING_LABEL, "per_page": 10}
    resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
    resp.raise_for_status()
    for issue in resp.json():
        if issue["title"] == TRACKING_ISSUE_TITLE:
            return issue
    return None


def create_or_update_issue(body):
    existing = find_open_tracking_issue()
    if existing:
        url = f"{GITHUB_API}/repos/{REPO}/issues/{existing['number']}"
        resp = requests.patch(url, headers=HEADERS, json={"body": body}, timeout=30)
    else:
        url = f"{GITHUB_API}/repos/{REPO}/issues"
        payload = {
            "title": TRACKING_ISSUE_TITLE,
            "body": body,
            "labels": [TRACKING_LABEL],
        }
        resp = requests.post(url, headers=HEADERS, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


def main():
    if not TOKEN or not REPO:
        print("GITHUB_TOKEN and GITHUB_REPOSITORY must be set.", file=sys.stderr)
        sys.exit(1)

    known = existing_urls()
    seen_ids = set()
    candidates = []

    for q in SEARCH_QUERIES:
        for repo in search_repos(q, seen_ids):
            if repo["html_url"] not in known:
                candidates.append(repo)

    if not candidates:
        print("No new candidates found.")
        return

    candidates.sort(key=lambda r: r["stargazers_count"], reverse=True)
    body = build_issue_body(candidates[:50])  # cap to keep the issue readable
    issue = create_or_update_issue(body)
    print(f"Updated issue #{issue['number']} with {len(candidates)} candidates.")


if __name__ == "__main__":
    main()
