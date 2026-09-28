from pathlib import Path
import re


def words(text):
    return set(re.findall(r"[a-zA-Z]+", text.lower()))


def retrieve(query, chunks, top_k=1):
    query_words = words(query)
    ranked = []
    for chunk in chunks:
        score = len(query_words & words(chunk))
        ranked.append((score, chunk))
    return sorted(ranked, reverse=True)[:top_k]


def generate_answer(query, context):
    if not context:
        return "I could not find relevant information in the knowledge base."
    return f"Based on the retrieved travel information: {context[0]}"


chunks = Path("knowledge.txt").read_text().splitlines()
query = "What transportation can I use in Tokyo?"
retrieved = retrieve(query, chunks)
context = [chunk for _, chunk in retrieved]

print("Query:", query)
print("Context:", context)
print("Answer:", generate_answer(query, context))
