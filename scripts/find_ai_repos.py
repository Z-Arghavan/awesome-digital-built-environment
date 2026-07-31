#!/usr/bin/env python3
"""
Find GitHub repositories at the intersection of AI/ML and the built
environment (BIM/IFC, construction, buildings, cities) that were created
or pushed to within the last 7 days, and open (or update) a dedicated
weekly tracking issue for them.

Categories mirror the README's "Artificial intelligence and machine
learning" section, so results map directly onto its existing subsections.
Kept separate from find_ifc_repos.py and
find_new_digital_built_environment_repos.py so AI-specific candidates can
be reviewed on their own.
"""

from datetime import date, timedelta

from discovery_lib import run

SINCE = (date.today() - timedelta(days=7)).isoformat()

BASE_CATEGORY_QUERIES = {
    "AI for BIM and IFC": [
        "topic:ifc topic:llm",
        "topic:bim topic:ai",
        "topic:bim topic:nlp",
        "IFC LLM",
        "BIM LLM",
        "IFC agent",
        "BIM chatbot",
        "IFC copilot",
    ],
    "LLM agents and natural-language interfaces": [
        "topic:mcp construction",
        "topic:mcp bim",
        "topic:mcp aec",
        "construction AI agent",
        "BIM AI agent",
        "MCP server BIM",
        "MCP server construction",
    ],
    "Computer vision for construction": [
        "topic:computer-vision construction",
        "topic:object-detection construction",
        "construction site detection",
        "building defect detection",
        "construction safety AI",
        "site monitoring detection",
    ],
    "Generative design and spatial intelligence": [
        "topic:generative-design",
        "floor plan generation",
        "floor plan GAN",
        "floor plan transformer",
        "topic:floorplan deep-learning",
    ],
    "Building control and reinforcement learning": [
        "topic:reinforcement-learning building",
        "topic:reinforcement-learning hvac",
        "building energy RL",
        "HVAC reinforcement learning",
        "gymnasium building",
    ],
    "GeoAI and urban intelligence": [
        "topic:geoai",
        "topic:remote-sensing building",
        "geospatial foundation model",
        "satellite building segmentation",
        "urban foundation model",
    ],
    "Foundation models for the built environment": [
        "topic:foundation-model construction",
        "topic:foundation-model building",
        "foundation model AEC",
        "vision-language model construction",
        "multimodal model building",
        "pretrained model point-cloud",
        "topic:foundation-model 3d",
        "large model construction",
    ],
    "AI benchmarks and datasets": [
        "topic:bim topic:benchmark",
        "topic:bim topic:dataset",
        "BIM benchmark",
        "construction dataset AI",
        "building dataset machine-learning",
    ],
    "Neuro-symbolic AI": [
        "topic:neurosymbolic",
        "topic:neuro-symbolic",
        "neurosymbolic reasoning",
        "neuro-symbolic knowledge-graph",
        "symbolic reasoning LLM",
        "topic:knowledge-graph topic:reasoning",
        "ontology grounded LLM",
        "graph RAG reasoning",
    ],
    "NLP for construction and built environment": [
        "topic:nlp construction",
        "topic:nlp bim",
        "construction document NLP",
        "specification text extraction",
        "building code NLP",
        "contract text extraction",
        "construction text classification",
        "text mining construction",
        "regulatory text extraction",
        "BERT construction",
        "BERT building",
        "topic:bert construction",
        "construction named-entity",
        "SBERT construction",
        "sentence-transformers construction",
        "sentence embeddings BIM",
    ],
    "AI bias and fairness in construction": [
        "topic:ai-fairness construction",
        "AI bias construction",
        "bias built-environment",
        "fairness AI building",
        "algorithmic bias AEC",
    ],
    "RAG for AEC documents": [
        "topic:rag construction",
        "topic:rag bim",
        "RAG building code",
        "retrieval augmented construction",
        "document RAG AEC",
    ],
    "Structural health monitoring and anomaly detection": [
        "topic:structural-health-monitoring",
        "SHM anomaly detection",
        "structural anomaly detection",
        "sensor anomaly building",
        "predictive maintenance building",
    ],
    "Time-series forecasting for building energy": [
        "topic:load-forecasting building",
        "building energy forecasting",
        "energy consumption forecasting",
        "load forecasting building",
    ],
    "Multi-agent systems for construction": [
        "topic:multi-agent construction",
        "multi-agent construction",
        "multi-agent BIM",
        "multi-agent building",
    ],
    "Synthetic data generation": [
        "synthetic BIM data",
        "synthetic construction data",
        "topic:synthetic-data building",
        "synthetic point-cloud generation",
    ],
}

CATEGORY_QUERIES = {
    category: [f"{q} pushed:>={SINCE}" for q in queries]
    for category, queries in BASE_CATEGORY_QUERIES.items()
}

ISSUE_TITLE = "New AI/ML repos to review"
LABEL = "auto-discovery-ai"

if __name__ == "__main__":
    run(CATEGORY_QUERIES, ISSUE_TITLE, LABEL)
