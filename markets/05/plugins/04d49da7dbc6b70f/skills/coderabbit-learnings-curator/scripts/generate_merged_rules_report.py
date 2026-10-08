import csv
import re
import sys
from pathlib import Path


def load_originals(review_index: Path) -> dict[str, tuple[str, str]]:
    text = review_index.read_text(encoding="utf-8")
    parts = re.split(r"(?m)^## (\d+)\. ", text)
    originals: dict[str, tuple[str, str]] = {}
    for i in range(1, len(parts), 2):
        number = parts[i]
        body = parts[i + 1]
        header, _, learning = body.partition("\n")
        originals[number] = (header.strip(), learning.strip())
    return originals


def source_ids(row: dict[str, str]) -> list[str]:
    value = row.get("Pull Request", "")
    return [part.strip() for part in value.split(",") if part.strip().isdigit()]


def main() -> int:
    if len(sys.argv) != 4:
        print(
            "usage: generate_merged_rules_report.py <curated.csv> <review-index.md> <output.md>",
            file=sys.stderr,
        )
        return 2

    curated_path = Path(sys.argv[1])
    review_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    with curated_path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    originals = load_originals(review_path)
    merged = [(source_ids(row), row) for row in rows if len(source_ids(row)) > 1]

    lines: list[str] = ["# Merged Learnings Review", "", f"Merged draft rules: {len(merged)}", ""]
    for index, (ids, row) in enumerate(merged, 1):
        lines.extend(
            [
                f"## {index}. {row.get('Repository', '')} | {row.get('File', '')}",
                "",
                "### Original rules merged",
                "",
            ]
        )
        for rule_id in ids:
            header, learning = originals.get(rule_id, ("missing", ""))
            one_line = " ".join(learning.split())
            if len(one_line) > 500:
                one_line = one_line[:497] + "..."
            lines.append(f"- **#{rule_id}** ({header}): {one_line}")
        lines.extend(["", "### Merged rule", "", row.get("Learning", ""), ""])

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {output_path} with {len(merged)} merged rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
