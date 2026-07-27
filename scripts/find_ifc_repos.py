#!/usr/bin/env python3
"""
Find GitHub repositories related to IFC / BIM that are not yet listed in
README.md, and open (or update) a dedicated tracking issue for them.

Kept separate from find_new_digital_built_environment_repos.py so IFC/BIM
candidates can be reviewed on their own schedule, independently of the
broader categories.
"""

from discovery_lib import run

CATEGORY_QUERIES = {
    "BIM / IFC tools": [
        "topic:ifc",
        "topic:openbim",
        "topic:bim",
        "topic:ifcopenshell",
        "topic:buildingsmart",
        "IFC BIM in:description,name",
    ],
}

ISSUE_TITLE = "New IFC/BIM repos to review"
LABEL = "auto-discovery-ifc"

if __name__ == "__main__":
    run(CATEGORY_QUERIES, ISSUE_TITLE, LABEL)
