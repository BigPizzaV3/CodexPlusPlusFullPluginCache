#!/usr/bin/env python3
"""Simple case-insensitive search in the bundled workshop notes/transcript."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "skills" / "ask-farouk-creative-thinking" / "references"

def search(query: str, source: Path, context: int = 1):
    lines = source.read_text(encoding="utf-8").splitlines()
    matched = [i for i, line in enumerate(lines) if query.casefold() in line.casefold()]
    for idx in matched:
        lo, hi = max(0, idx - context), min(len(lines), idx + context + 1)
        print(f"\n{source.name}:{idx + 1}")
        for pos in range(lo, hi):
            print(f"{pos + 1}: {lines[pos]}")
    return len(matched)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Arabic or English phrase")
    parser.add_argument("--notes", action="store_true", help="search condensed notes")
    parser.add_argument("--context", type=int, default=1, help="lines of context")
    args = parser.parse_args()
    src = ROOT / ("lecture-notes.md" if args.notes or not (ROOT / "transcript.md").exists() else "transcript.md")
    hits = search(args.query, src, context=max(0, min(5, args.context)))
    print(f"\n{hits} matches found")
