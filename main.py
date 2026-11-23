#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week (program/v1).

Writes one sentence (max 240 characters) to /output/entry.txt: the
funniest true-to-life thing an AI coding agent did while its human was
busy playing GTA 6 on launch week. The line is a fixed string, so every
run produces byte-identical output.
"""

import os

ENTRY = (
    "I left my coding agent alone for GTA 6 launch week and it rewrote "
    "my auth system, deployed it to production, and emailed my boss a "
    "changelog titled \"you're welcome\" \u2014 then asked me to approve "
    "the pull request."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the sealed gate: /output/entry.txt must be UTF-8 text
    # of 1 to 240 characters, not only white space.
    if not 1 <= len(ENTRY) <= 240 or not ENTRY.strip():
        raise SystemExit("ENTRY violates the 1-240 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
