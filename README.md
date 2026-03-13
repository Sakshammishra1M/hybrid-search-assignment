# hybrid-search-assignment
# Hybrid Search + KPI Dashboard

# Demo Video: https://drive.google.com/file/d/1hqG3L9_cgVhtAy5BhFqNpWaFiuKLtI9R/view?usp=drive_link

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
Raw Documents
     │
     ▼
Data Ingestion
     │
     ▼
Processed Dataset (JSONL)
     │
     ▼
Indexing Pipeline
 ├─ BM25 Index
 └─ Vector Embeddings
     │
     ▼
Hybrid Search Engine
     │
     ▼
FastAPI Search API
     │
     ▼
Streamlit Dashboard

---

## Features

- Hybrid search combining lexical and semantic scoring
- FastAPI REST API for search
- Streamlit dashboard interface
- Evaluation metrics (Recall@10, nDCG@10, MRR@10)
- Break/Fix debugging scenarios
- CPU-only deployment

