"""Two-sentence horror entry: tally the sentences, then shelve with the gate output."""
import json
import os
import pathlib
import re

STORY = "entry.txt"
PAGE_CAP = 400


def tally(text: str) -> dict:
    body = text.strip()
    ends = re.findall(r"[.!?]", body)
    page = {
        "words": len(body.split()),
        "full_stops": len(ends),
        "two_sentences": len(ends) == 2,
        "page_fits": 0 < len(body) <= PAGE_CAP and len(body.encode("utf-8")) < PAGE_CAP + 2,
    }
    page["shelved_ok"] = page["page_fits"] and page["two_sentences"]
    return page


def shelve() -> int:
    spine = pathlib.Path(__file__).resolve().parent / STORY
    raw = spine.read_text(encoding="utf-8")
    page = tally(raw)
    cellar = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or spine.parent / "cellar")
    cellar.mkdir(parents=True, exist_ok=True)
    (cellar / STORY).write_bytes(raw.encode("utf-8"))
    print(json.dumps({"story": "house-note", "page": page, "cellar": str(cellar)}))
    return 0 if page["shelved_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(shelve())
