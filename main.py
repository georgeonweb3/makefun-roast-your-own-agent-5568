#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single original roast line to /output/entry.txt: my own
agent has a 200k-token context window yet forgot my name by token 40
and spent the rest confidently calling me "boss" — confident wrong
answers plus eager agreement, the two classic agent behaviours.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = (
    "My agent's context window is 200k tokens; it forgot my name by "
    "token 40 and spent the rest confidently calling me 'boss'."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 140 characters, not only whitespace — and one line.
    # No trailing newline: the gate counts every byte, and a
    # newline would split the roast from its punchline.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, gate wants 1-140"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
