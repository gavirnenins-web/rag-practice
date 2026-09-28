from pathlib import Path
import re


def tokenize(text):
    return set(re.findall(r"[a-zA-Z]+", text.lower()))


def retrieve(query, documents, top_k=2):
    query_words = tokenize(query)
    scored = []

    for document in documents:
        score = len(query_words & tokenize(document))
        scored.append((score, document))

    return sorted(scored, key=lambda item: item[0], reverse=True)[:top_k]


documents = Path("documents.txt").read_text().splitlines()
query = "Tokyo railway and temple"

for score, document in retrieve(query, documents):
    print(f"score={score}: {document}")
