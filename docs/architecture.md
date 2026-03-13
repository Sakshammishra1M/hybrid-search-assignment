# System Architecture

This project implements a Hybrid Search + KPI Dashboard system.

## Components

1. Data Ingestion
Raw documents from data/raw are loaded and converted into JSONL format.

Fields in dataset:
- doc_id
- title
- text
- source
- created_at

The ingestion pipeline normalizes whitespace and removes empty lines.

Command used:
python -m backend.app.ingest --input data/raw --out data/processed


2. Indexing

Two indexes are created:

BM25 index:
Built using rank-bm25 for lexical search.

Vector index:
Built using sentence-transformers embeddings.

Embedding model:
all-MiniLM-L6-v2

Artifacts stored in:
data/index/


3. Hybrid Search Engine

Search combines lexical and semantic scores.

Formula used:

hybrid_score = alpha * bm25_score + (1 - alpha) * vector_score

Normalization:
Min-max normalization.


4. FastAPI Backend

Provides API endpoints:

GET /health
Returns system health status.

POST /search
Returns ranked search results with score breakdown.


5. Streamlit Dashboard

Provides UI for:

- Query search
- Result display
- Hybrid score visualization