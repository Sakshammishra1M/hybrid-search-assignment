import json
import argparse
import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
import os


def load_docs(path):

    docs = []

    with open(path) as f:
        for line in f:
            docs.append(json.loads(line))

    return docs


def build_index(docs):

    tokenized = [d["text"].lower().split() for d in docs]

    bm25 = BM25Okapi(tokenized)

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode([d["text"] for d in docs])

    os.makedirs("data/index", exist_ok=True)

    np.save("data/index/tokenized.npy", np.array(tokenized, dtype=object), allow_pickle=True)
    np.save("data/index/embeddings.npy", embeddings)

    with open("data/index/docs.json", "w") as f:
        json.dump(docs, f)

    print("Index built successfully")


def main(input_path):

    docs = load_docs(input_path)

    build_index(docs)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)

    args = parser.parse_args()

    main(args.input)