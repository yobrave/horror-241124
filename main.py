"""tsh6: two-sentence archivist. File the pair; the second sentence decides."""
import json
import os
import sys
from pathlib import Path

SHELF = 400


def sentences(raw: str):
    parts = [p for p in raw.strip().replace("? ", "?\n").replace(". ", ".\n").replace("! ", "!\n").split("\n") if p]
    return parts


def main():
    raw = Path(__file__).resolve().parent.joinpath("entry.txt").read_text(encoding="utf-8")
    bare = raw.strip()
    parts = sentences(bare)
    checkup = {
        "archivist": "tsh6-pair-r6",
        "sentences_seen": len(parts),
        "chars": len(bare),
        "shelf": SHELF,
        "files": 1 <= len(bare) <= SHELF and bare != "" and not bare.isspace(),
    }
    if checkup["files"]:
        drawer = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        drawer.mkdir(parents=True, exist_ok=True)
        (drawer / "entry.txt").write_bytes(bare.encode("utf-8"))
    print("VERDICT", json.dumps(checkup))
    return 0 if checkup["files"] else 1


if __name__ == "__main__":
    sys.exit(main())
