import json
import os
import re

TALE = "tsh3-two"
ROOF = 400


def tale(blob):
    for row in blob.replace("\r", "").split("\n"):
        if row.strip():
            return row
    return ""


def count_sentences(line):
    parts = [p for p in re.split(r"(?<=[.!?])\s+", line.strip()) if p.strip()]
    return len(parts)


def bind(line, root):
    shelf = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(shelf, exist_ok=True)
    spine = os.path.join(shelf, "entry.txt")
    ink = line.encode("utf-8")
    with open(spine, "wb") as binder:
        binder.write(ink)
    with open(spine, "rb") as reader:
        if reader.read() != ink:
            raise IOError("binding split")
    return spine


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as page:
    line = tale(page.read())

sents = count_sentences(line)
if not line.strip() or len(line) > ROOF or sents != 2:
    print(json.dumps({"tale": "unfinished", "size": len(line), "sentences": sents}))
    raise SystemExit(1)
spine = bind(line, root)
print(json.dumps({"tale": "bound", "size": len(line), "sentences": sents, "roof": ROOF, "sig": TALE, "spine": os.path.basename(spine)}))
