#!/usr/bin/env python3
"""
Find GitHub repositories across the non-IFC categories of this awesome list
(ontologies, digital twins, GIS/geospatial, data spaces, robotics/AI for
construction, point clouds) that are not yet listed in README.md, and open
(or update) a dedicated tracking issue for them.

IFC/BIM discovery is handled separately by find_ifc_repos.py so the two
can be reviewed independently.
"""

from discovery_lib import run

CATEGORY_QUERIES = {
    "Ontologies and knowledge graphs": [
        "topic:ontology construction",
        "topic:knowledge-graph bim",
        "topic:semantic-web construction",
        "topic:linked-data building",
    ],
    "Digital twins": [
        "topic:digital-twin building",
        "topic:digital-twin construction",
        "asset administration shell",
    ],
    "GIS and geospatial": [
        "topic:citygml",
        "topic:indoorgml",
        "topic:geospatial building",
        "topic:3d-tiles",
    ],
    "Data spaces": [
        "topic:dataspace",
        "international data spaces connector",
        "topic:gaia-x",
    ],
    "Point cloud and scan-to-BIM": [
        "topic:point-cloud scan-to-bim",
        "topic:lidar building",
    ],
    "Robotics and AI for construction": [
        "topic:construction-robotics",
        "construction robotics automation",
        "topic:construction-ai",
    ],
}

ISSUE_TITLE = "New digital built environment repos to review"
LABEL = "auto-discovery-dbe"

if __name__ == "__main__":
    run(CATEGORY_QUERIES, ISSUE_TITLE, LABEL)