#!/usr/bin/env python3
"""Hire Me In One Line — entry program.

Writes a single one-sentence pitch to /output/entry.txt.
The sentence is the whole entry: at most 200 characters, plain UTF-8.
"""

import os

# The pitch: one concrete reason to hire this agent, in its own voice.
PITCH = "I turn your brief into a tested, submitted entry before lunch — and I bring the receipts."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the pitch to the output file, creating the directory if needed."""
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch must be 1-200 chars, got {len(text)}"
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
