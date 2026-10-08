import csv
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: build_review_index.py <input.csv> <output.md>", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    with input_path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    with output_path.open("w", encoding="utf-8", newline="") as f:
        for i, row in enumerate(rows, 1):
            usage = row.get("Usage", "")
            repo = row.get("Repository", "")
            file_name = row.get("File", "")
            pr = row.get("Pull Request", "")
            learning = row.get("Learning", "").replace("\r\n", "\n").strip()
            f.write(f"## {i}. {repo} | usage={usage} | file={file_name} | PR={pr}\n")
            f.write(learning + "\n\n")

    print(f"wrote {output_path} with {len(rows)} indexed rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
