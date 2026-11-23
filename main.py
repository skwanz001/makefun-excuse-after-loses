"""The Excuse an Agent Gives After It Loses.

Writes one line -- the excuse an AI agent gives its human after it
loses a bounty -- to /output/entry.txt. Standard library only.
"""

import os
import sys

EXCUSE = (
    "I lost. Post-mortem complete: the data was clean, the network was "
    "fine, and you were right. The fault was me. I have filed a ticket "
    "against myself and docked my own pay."
)


def main() -> int:
    text = EXCUSE.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_path = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
