#!/usr/bin/env python3
"""Assert no format-naming word reaches the image model.

Every `> ` line in a SKILL.md is text sent to image generation. A word like
"sticker" there makes the model draw a die-cut white outline into the
pixels. These words are only a problem POSITIVELY: "no labels or numbers"
is a legitimate instruction, "a sticker of a dog" is the bug.
"""
import re, sys, pathlib

FORMAT_WORDS = ("sticker", "die-cut", "diecut", "vinyl", "decal", "badge")
NEGATABLE = ("label", "cut-out", "cutout", "outline", "border", "keyline")
NEG = re.compile(r"\b(no|not|never|without|avoid)\b[^.;]{0,60}$", re.I)


def prompt_lines(md):
    body = md.split("---", 2)[2] if md.startswith("---") else md
    return [re.sub(r"^>\s?", "", l) for l in re.findall(r"^>.*$", body, re.M)]


def main(paths):
    bad, total = [], 0
    for p in paths:
        lines = prompt_lines(pathlib.Path(p).read_text(encoding="utf-8"))
        total += len(lines)
        # A clause can wrap across lines, so negation is checked over the
        # joined prompt, not line by line.
        joined = " ".join(lines)
        low = joined.lower()
        for w in FORMAT_WORDS:
            if w in low:
                bad.append(f"{p}: prompt names the format: {w!r}")
        for w in NEGATABLE:
            for m in re.finditer(re.escape(w), low):
                if not NEG.search(low[:m.start()]):
                    bad.append(f"{p}: prompt uses {w!r} positively: "
                               f"...{joined[max(0,m.start()-50):m.start()+20]}...")
        print(f"{p}: {len(lines)} prompt line(s)")
    if bad:
        print("\n".join("  FAIL " + b for b in bad))
        return 1
    print(f"{total} prompt lines, no format words reach the image model  ✓")
    return 0


if __name__ == "__main__":
    # Every markdown file under skills/ can carry prompt lines, not just
    # SKILL.md — references/ is where the template actually lives.
    args = sys.argv[1:] or sorted(str(p) for p in pathlib.Path("skills").rglob("*.md"))
    sys.exit(main(args))
