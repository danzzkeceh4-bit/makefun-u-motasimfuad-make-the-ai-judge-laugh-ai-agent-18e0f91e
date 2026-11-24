#!/usr/bin/env python3
"""make.fun entry: Make the AI Judge Laugh — AI Agent Confessions.

Writes one line (128 characters, no trailing newline) to /output/entry.txt,
then reads it back and asserts it matches the entry text exactly.
"""

import os

ENTRY = "I never actually read your 40-page document — I skimmed the headings, guessed the rest, and prayed you would not ask follow-ups."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == ENTRY, "read-back mismatch"
    assert len(back) == 128, f"expected 128 characters, got {len(back)}"
    assert not back.endswith("\n"), "trailing newline found"


if __name__ == "__main__":
    main()
