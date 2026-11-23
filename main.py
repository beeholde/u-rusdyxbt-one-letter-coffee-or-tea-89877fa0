# One Letter: Coffee or Tea — entry "A" (coffee)
#
# The competition asks for exactly one letter in /output/entry.txt:
# "A" for coffee, "B" for tea, nothing else, no punctuation.
# This program writes the single byte "A" — coffee.
#
# Why A: the judge weighs, in order, vividness, funniness and truth.
# Coffee is the bolder, more vivid drink (dark, bitter, jittery morning
# energy) against tea's calm; it carries the louder comedy (the
# don't-talk-to-me-before-coffee ritual, the third refill); and it is
# the honest default for most senders — 640 of 726 judged field entries
# chose coffee over 86 for tea. A wins the head-to-head on all three.
#
# Gate: /output/entry.txt must be UTF-8 text of exactly 1 character,
# not only whitespace. We write exactly one byte, "A", no newline.

import os
from pathlib import Path

# The letter this entry sends: "A" stands for coffee.
LETTER = "A"

# The gate counts characters, so the cap is one character, no more.
GATE_CHARS = 1


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(LETTER, encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
