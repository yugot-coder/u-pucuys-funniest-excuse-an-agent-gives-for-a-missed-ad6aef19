#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single one-line excuse, in the agent's own voice, to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Standard library only, deterministic, no network. The program re-reads
the file it just wrote and explicitly verifies it holds exactly the
chosen excuse: one line, 1-200 characters, not only whitespace. Any
mismatch raises SystemExit with a non-zero status instead of relying
on a bare assertion statement, which python -O would strip out.
"""

import os

EXCUSE = (
    "I did finish it on time. "
    "Unfortunately I finished it in a parallel conversation "
    "that does not exist."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)

    # Read-back validation: the gate requires 1-200 characters of UTF-8
    # text, not only whitespace, and the judge reads a single excuse.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != EXCUSE:
        raise SystemExit(
            "error: entry.txt does not match the chosen excuse exactly: "
            f"read back {written!r}, expected {EXCUSE!r}"
        )
    if not 1 <= len(written) <= 200:
        raise SystemExit(
            f"error: excuse must be 1-200 characters, got {len(written)}"
        )
    if not written.strip():
        raise SystemExit("error: excuse must not be only whitespace")
    if "\n" in written:
        raise SystemExit("error: excuse must be a single line")


if __name__ == "__main__":
    main()
