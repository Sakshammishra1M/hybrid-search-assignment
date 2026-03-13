import json
import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SearchEngine:

    def __init__(self):

        with open("data/index/docs.json") as f:
            self.docs = json.load(f)

        tokenized = np.load("data/index/tokenized.npy", allow_pickle=True)

        self.bm25 = BM25Okapi(tokenized)

        self.embeddings = np.load("data/index/embeddings.npy")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def normalize(self, scores):

        scores = np.array(scores)

        return (scores - scores.min()) / (scores.max() - scores.min() + 1e-9)

    def search(self, query, top_k=10, alpha=0.5):

        tokens = query.lower().split()

        bm25_scores = self.bm25.get_scores(tokens)

        query_vec = self.model.encode([query])

        vector_scores = cosine_similarity(query_vec, self.embeddings)[0]

        bm25_norm = self.normalize(bm25_scores)
        vector_norm = self.normalize(vector_scores)

        hybrid = alpha * bm25_norm + (1 - alpha) * vector_norm

        ranked = np.argsort(hybrid)[::-1][:top_k]

        results = []

        for i in ranked:

            d = self.docs[i]

            results.append({
                "doc_id": d["doc_id"],
                "title": d["title"],
                "bm25_score": float(bm25_scores[i]),
                "vector_score": float(vector_scores[i]),
                "hybrid_score": float(hybrid[i])
            })

        return results