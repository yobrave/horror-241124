"""Two-sentence lantern: lights the story, counts the sentences, hangs it in output."""
STAMP = "onebug-11251142-tsh3"
import json
import os
import shutil
from pathlib import Path

HALL = Path(__file__).resolve().parent
GLOW_MAX = 400
STORY = ("My daughter sleeps with two nightlights: one for the dark, "
         "and one she says is for the friend who watches the dark.")


def light_up():
    wick = HALL / "entry.txt"
    tale = wick.read_text(encoding="utf-8").strip()
    burning = 1 <= len(tale) <= GLOW_MAX
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and burning:
        Path(bay).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(wick, Path(bay) / "entry.txt")
    print(json.dumps({"burning": burning, "stamp": STAMP, "tale_len": len(tale), "glow_max": GLOW_MAX}))


if __name__ == "__main__":
    light_up()
