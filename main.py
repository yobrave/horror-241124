"""Two sentences that should not sit next to each other."""
import os

SENTENCES = [
    "Every night at nine, my house locks its doors and dims the "
    "lights without being asked.",
    "Tonight it left a note: 'Sweet dreams — homeowner not detected.'",
]
DOOR = "tsh2"
NINE = "21:00"
NOTE_LEFT = "yes"

story = " ".join(SENTENCES)
base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
os.makedirs(base, exist_ok=True)
p = os.path.join(base, "entry.txt")
with open(p, "w", encoding="utf-8", newline="\n") as f:
    f.write(story + "\n")
with open(p, encoding="utf-8") as f:
    back = f.read().strip()
assert back == story, "the house rewrote it"
print(DOOR, NINE, len(back), "chars, lights dimmed")
print("note left:", NOTE_LEFT, "signed by nobody")
