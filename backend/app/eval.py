import json
from backend.app.search_engine import SearchEngine


def recall_at_k(predicted, relevant, k=10):

    predicted = predicted[:k]

    hits = len([p for p in predicted if p in relevant])

    return hits / len(relevant)


def run_eval():

    engine = SearchEngine()

    with open("data/eval/queries.jsonl") as f:
        queries = [json.loads(line) for line in f]

    scores = []

    print("Running evaluation...\n")

    for q in queries:

        results = engine.search(q["query"], 10)

        predicted = [r["doc_id"] for r in results]

        score = recall_at_k(predicted, q["relevant"], 10)

        scores.append(score)

        print("Query:", q["query"])
        print("Recall@10:", round(score, 3))
        print("-------------------")

    avg_score = sum(scores) / len(scores)

    print("\nAverage Recall@10:", round(avg_score, 3))


if __name__ == "__main__":
    run_eval()