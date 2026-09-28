from pathlib import Path

CHUNK_SIZE = 120
text = Path("travel_guide.txt").read_text().strip()

chunks = [text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]

for number, chunk in enumerate(chunks, start=1):
    print(f"\n--- CHUNK {number} ---")
    print(chunk)
