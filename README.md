# hybrid-search-assignment
# Hybrid Search + KPI Dashboard

## Overview
Hybrid search system combining BM25 and semantic embeddings.

## Architecture
Explain pipeline.

## Installation
pip install -r requirements.txt

## Run system
python -m backend.app.ingest
python -m backend.app.index
python -m uvicorn backend.app.api:app --reload
python -m streamlit run frontend/app.py

## Evaluation
python -m backend.app.eval

## Tests
pytest
