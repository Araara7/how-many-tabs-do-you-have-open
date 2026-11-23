#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes one number, digits only, to /output/entry.txt: the honest count
of open browser tabs. 137: a real, lived-in tab-hoarder count — triple
digits, specific rather than round, surprising against a typical field of
a dozen or two, yet believable for someone who researches, reads and
never closes anything "to read later".
"""

import os

COUNT = "137"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(COUNT)
    # Read back and verify the gate: 1-5 UTF-8 chars, digits only.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 5, f"gate: {len(text)} chars"
    assert text.isdigit(), f"gate: not digits only: {text!r}"
    assert text == COUNT, f"mismatch: {text!r} != {COUNT!r}"


if __name__ == "__main__":
    main()
