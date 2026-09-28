from pathlib import Path

query = "What can I visit in Paris?"
document = Path("documents/travel.txt").read_text()

print("QUERY:", query)
print("\nRETRIEVED CONTEXT:")

for line in document.splitlines():
    if "Paris" in line:
        print(line)

print("\nNEXT STEP: In a real RAG system, an LLM would use the retrieved context to generate the final answer.")
