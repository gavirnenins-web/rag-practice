# Session 03 - Retrieval

## Goal
Build a simple retriever without embeddings or a vector database.

## Task
Implement keyword-based scoring in `retriever.py`.

For each chunk:
- split the query into words
- count matching words
- rank chunks by score
- return the top results

## Concept
This is intentionally a simple stand-in for semantic retrieval. Production RAG commonly uses embeddings and vector or hybrid search, but understanding retrieval logic first is useful.

## Practice status
Completed as a local practice exercise.
