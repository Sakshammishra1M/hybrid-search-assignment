import argparse
import os
import json
import glob
from pathlib import Path
from datetime import datetime


def clean_text(text):
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


def ingest(input_dir, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    docs = []

    for file in glob.glob(os.path.join(input_dir, "*")):

        if not file.endswith(".txt"):
            continue

        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        doc = {
            "doc_id": Path(file).stem,
            "title": Path(file).stem,
            "text": clean_text(text),
            "source": file,
            "created_at": datetime.utcnow().isoformat()
        }

        docs.append(doc)

    out_file = os.path.join(output_dir, "docs.jsonl")

    with open(out_file, "w") as f:
        for d in docs:
            f.write(json.dumps(d) + "\n")

    print("Documents processed:", len(docs))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)

    args = parser.parse_args()

    ingest(args.input, args.out)