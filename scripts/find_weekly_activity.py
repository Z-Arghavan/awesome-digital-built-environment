#!/usr/bin/env python3
"""
Find GitHub repositories, across every category of this awesome list, that
were created or pushed to within the last 7 days, and open (or update) a
weekly digest issue with them.

Reuses the same category/query lists as find_ifc_repos.py and
find_new_digital_built_environment_repos.py, just narrowed to recent
activity via GitHub's `pushed:>=` search qualifier. Meant to run every
Monday, see .github/workflows/weekly-activity.yml.
"""

from datetime import date, timedelta

from discovery_lib import run
from find_ifc_repos import CATEGORY_QUERIES as IFC_QUERIES
from find_new_digital_built_environment_repos import CATEGORY_QUERIES as DBE_QUERIES

SINCE = (date.today() - timedelta(days=7)).isoformat()

ALL_QUERIES = {**IFC_QUERIES, **DBE_QUERIES}
CATEGORY_QUERIES = {
    category: [f"{q} pushed:>={SINCE}" for q in queries]
    for category, queries in ALL_QUERIES.items()
}

ISSUE_TITLE = "Repos created or updated in the past week"
LABEL = "weekly-activity"

if __name__ == "__main__":
    run(CATEGORY_QUERIES, ISSUE_TITLE, LABEL)
