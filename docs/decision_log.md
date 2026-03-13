# Decision Log

This document explains key technical decisions made during development.

## Embedding Model

Model used:
all-MiniLM-L6-v2

Reason:
Small model optimized for CPU inference with good semantic performance.


## Vector Search Implementation

Instead of FAISS or hnswlib, cosine similarity using sklearn was used.

Reason:
Avoids heavy C++ dependencies and simplifies setup.


## Hybrid Scoring Formula

Formula used:

hybrid_score = alpha * bm25 + (1 - alpha) * vector

Reason:
Allows balancing lexical relevance and semantic similarity.


## Score Normalization

Min-max normalization used.

Reason:
BM25 and cosine similarity produce different score ranges.


## Frontend Framework

Streamlit used instead of React.

Reason:
Faster development and simpler deployment for small applications.