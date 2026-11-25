#!/usr/bin/env python3
"""The Funniest Toaster Error Message -- make.fun entry, round 2.

Writes one 82-character toaster error message to /output/entry.txt.

The line is a fatal-error report in the voice of a crash investigator:
the toaster recovers the bread's black box and quotes its dying words.
Two beats inside one read: the report (setup) and the quote (reframe
and kicker). Standard library only.
"""

import os

ENTRY = "E99: Black box recovered. Final words of the bread: 'Tell the butter I loved her.'"
MAX_CHARS = 120


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS or not ENTRY.strip():
        raise ValueError("entry must be 1-120 non-blank characters")
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
