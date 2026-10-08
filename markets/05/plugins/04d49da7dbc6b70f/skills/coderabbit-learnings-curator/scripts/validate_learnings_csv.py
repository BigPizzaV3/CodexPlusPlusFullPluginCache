import argparse
import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = [
    "Learning",
    "Repository",
    "File",
    "Pull Request",
    "URL",
    "Created By",
    "Usage",
    "Last Used",
    "Created At",
    "Updated At",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument(
        "--removed-sources",
        action="append",
        default=[],
        help="Comma-separated source id group that must be absent from Pull Request.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    csv_path = Path(args.csv_path)

    with csv_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    errors: list[str] = []
    if fieldnames != REQUIRED_COLUMNS:
        errors.append(f"unexpected columns: {fieldnames}")

    for index, row in enumerate(rows, 1):
        if not row.get("Learning", "").strip():
            errors.append(f"row {index}: blank Learning")
        if not row.get("Repository", "").strip():
            errors.append(f"row {index}: blank Repository")
        if not row.get("Usage", "").strip():
            errors.append(f"row {index}: blank Usage")

    seen: dict[str, int] = {}
    for index, row in enumerate(rows, 1):
        learning = " ".join(row.get("Learning", "").split())
        if learning in seen:
            errors.append(f"row {index}: duplicate Learning also appears at row {seen[learning]}")
        else:
            seen[learning] = index

    pull_request_values = {row.get("Pull Request", "") for row in rows}
    for removed in args.removed_sources:
        if removed in pull_request_values:
            errors.append(f"removed source group still present: {removed}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"valid csv: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
