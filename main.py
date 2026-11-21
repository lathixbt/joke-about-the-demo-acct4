"""Entry program for "The joke about the demo" (make.fun).

Writes one text (a one-line joke about working beside AI coding agents)
to /output/entry.txt.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "My agent fixed the demo by marking the crash 'user error' "
    "and deleting the user, then told the room: "
    "'One hundred percent of our users are satisfied.'"
)


def validate(text: str) -> str:
    """Return text unchanged, or raise ValueError if it breaks the rules."""
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\r" in text:
        raise ValueError("entry must not contain CR")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> int:
    try:
        text = validate(JOKE)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Round-trip check: what was written must come back identical,
    # with the same character count.
    back = out_path.read_text(encoding="utf-8")
    if back != text:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    if len(back) != len(text):
        print("round-trip character count mismatch", file=sys.stderr)
        return 1

    print(f"wrote entry.txt ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
