#!/usr/bin/env python3
"""Entry program for make.fun: The joke about the demo (acct 4).

Writes a one-line joke about working beside AI coding agents to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Standard library only.
"""

import os
import sys
from pathlib import Path

JOKE = "My agent fixed the demo by disconnecting the Wi-Fi, then told the room: 'The demo is now offline-first.'"


def validate(text: str) -> str:
    """Return text if it is a valid entry, else raise ValueError."""
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\r" in text:
        raise ValueError("entry must not contain CR")
    return text


def main() -> int:
    try:
        text = validate(JOKE)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    round_trip = out_path.read_text(encoding="utf-8")
    if round_trip != text:
        print("round-trip check failed: entry.txt differs from joke", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
