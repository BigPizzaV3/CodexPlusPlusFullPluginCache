#!/usr/bin/env python3
"""
Parse a LEDES 1998B e-billing file into the normalized row structure this
skill's analyses expect (entity, matter_id, matter_type, timekeeper_role,
hours, rate, billed_amount, budget_estimate).

Why this exists: LEDES 1998B is the most widely used e-billing data exchange
standard in the US legal industry (used under the hood by Legal Tracker,
TyMetrix 360, Brightflag, Onit, and most other e-billing platforms), so a
real e-billing export is at least as likely to look like this pipe-delimited,
24-field format as it is to look like a clean CSV. Rather than asking every
user to reformat their export before uploading, detect this format and
convert it automatically.

LEDES 1998B structure:
    Line 1: "LEDES1998B[]" -- format identifier
    Line 2: pipe-delimited header naming the 24 fields, ending in "[]"
    Line 3+: pipe-delimited data rows, ending in "[]"

Important honest limitations (don't paper over these in the output):
    - LEDES 98B has no firm NAME field, only LAW_FIRM_ID (typically a tax ID).
      The normalized output uses LAW_FIRM_ID as the entity identifier -- if
      the user knows which ID maps to which firm name, they can tell you and
      you can substitute it in, but don't guess a firm name from the ID.
    - LEDES 98B has no "matter type" or "practice area" field. Where the fee
      line's task code falls in the UTBMS Litigation code set (L100-L600),
      that family is used as an approximate matter-type label (e.g. "L300
      series (Discovery)"); otherwise matter_type is left as "Not specified
      in LEDES data" rather than invented.
    - LEDES 98B carries actual billed amounts, not budgets or estimates.
      budget_estimate will be blank for every row -- budget variance analysis
      isn't possible on a LEDES file alone unless the user separately
      provides a budget/estimate for the matter.
    - Expense lines (EXP/FEE/INV_ADJ_TYPE = "E") have no timekeeper or hours
      attached -- they're costs, not staffing time. They're kept as their own
      rows (role/hours left blank) so they still count toward total billed
      amount, but they should be excluded from staffing-mix ratio math.

Usage:
    python parse_ledes.py <input.txt> <output.csv>
"""

import csv
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

UTBMS_LITIGATION_FAMILIES = {
    "L1": "L100 series (Case Assessment, Development & Administration)",
    "L2": "L200 series (Pre-Trial Pleadings & Motions)",
    "L3": "L300 series (Discovery)",
    "L4": "L400 series (Trial Preparation & Trial)",
    "L5": "L500 series (Appeal)",
    "L6": "L600 series (Settlement/ADR)",
}

LEDES_1998B_HEADERS = (
    "INVOICE_DATE",
    "INVOICE_NUMBER",
    "CLIENT_ID",
    "LAW_FIRM_MATTER_ID",
    "INVOICE_TOTAL",
    "BILLING_START_DATE",
    "BILLING_END_DATE",
    "INVOICE_DESCRIPTION",
    "LINE_ITEM_NUMBER",
    "EXP/FEE/INV_ADJ_TYPE",
    "LINE_ITEM_NUMBER_OF_UNITS",
    "LINE_ITEM_ADJUSTMENT_AMOUNT",
    "LINE_ITEM_TOTAL",
    "LINE_ITEM_DATE",
    "LINE_ITEM_TASK_CODE",
    "LINE_ITEM_EXPENSE_CODE",
    "LINE_ITEM_ACTIVITY_CODE",
    "TIMEKEEPER_ID",
    "LINE_ITEM_DESCRIPTION",
    "LAW_FIRM_ID",
    "LINE_ITEM_UNIT_COST",
    "TIMEKEEPER_NAME",
    "TIMEKEEPER_CLASSIFICATION",
    "CLIENT_MATTER_ID",
)

ALLOWED_LINE_TYPES = {"F", "E", "IF", "IE"}

NORMALIZED_FIELDNAMES = [
    "entity", "matter_id", "matter_type", "timekeeper_role", "timekeeper_name",
    "hours", "rate", "billed_amount", "budget_estimate", "line_item_description",
    "task_code", "activity_code", "line_item_date", "invoice_number", "line_type",
]

TEXTUAL_OUTPUT_FIELDS = {
    "entity", "matter_id", "matter_type", "timekeeper_role", "timekeeper_name",
    "line_item_description", "task_code", "activity_code", "line_item_date",
    "invoice_number", "line_type",
}


def safe_csv_text(value):
    """Neutralize formula controls in untrusted text written to CSV."""
    if isinstance(value, str):
        candidate = value.lstrip(" \t\r\n")
        if candidate.startswith(("=", "+", "-", "@")):
            return "'" + value
    return value


def is_ledes_1998b(path: Path) -> bool:
    """Quick check: does this file look like a LEDES 1998B export."""
    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            first_line = f.readline().strip()
    except OSError:
        return False
    return first_line.upper().startswith("LEDES1998B")


def strip_terminator(line: str) -> str:
    line = line.rstrip("\n").rstrip("\r")
    if line.endswith("[]"):
        line = line[:-2]
    return line


def infer_matter_type(task_code: str) -> str:
    if not task_code:
        return "Not specified in LEDES data"
    family = task_code[:2].upper()
    return UTBMS_LITIGATION_FAMILIES.get(family, f"Not specified in LEDES data (task code: {task_code})")


def is_decimal(value: str, *, allow_blank: bool = False) -> bool:
    if not value:
        return allow_blank
    try:
        parsed = Decimal(value)
    except InvalidOperation:
        return False
    return parsed.is_finite()


def parse(input_path: Path):
    with open(input_path, "r", encoding="utf-8-sig") as f:
        raw_lines = [l for l in f.readlines() if l.strip()]

    if not raw_lines or raw_lines[0].strip().upper() != "LEDES1998B[]":
        raise ValueError("This doesn't look like a LEDES 1998B file (expected 'LEDES1998B[]' on line 1).")
    if len(raw_lines) < 2:
        raise ValueError("LEDES 1998B file is missing its pipe-delimited header row.")
    if len(raw_lines) < 3:
        raise ValueError("LEDES 1998B file contains no data rows.")
    if not raw_lines[1].rstrip("\r\n").endswith("[]"):
        raise ValueError("LEDES header row is missing the required '[]' terminator.")

    header_fields = [h.strip() for h in strip_terminator(raw_lines[1]).split("|")]
    if tuple(header_fields) != LEDES_1998B_HEADERS:
        missing_headers = sorted(set(LEDES_1998B_HEADERS).difference(header_fields))
        duplicate_headers = sorted({h for h in header_fields if header_fields.count(h) > 1})
        details = []
        if missing_headers:
            details.append(f"missing required field(s): {', '.join(missing_headers)}")
        if duplicate_headers:
            details.append(f"duplicate field(s): {', '.join(duplicate_headers)}")
        if not details:
            details.append("fields are not in the required 24-column LEDES 1998B order")
        raise ValueError(f"LEDES header is invalid: {'; '.join(details)}")
    idx = {name: i for i, name in enumerate(header_fields)}

    def get(fields, name, default=""):
        i = idx.get(name)
        if i is None or i >= len(fields):
            return default
        return fields[i].strip()

    rows = []
    skipped = 0
    for line in raw_lines[2:]:
        if not line.rstrip("\r\n").endswith("[]"):
            skipped += 1
            continue
        fields = strip_terminator(line).split("|")
        if len(fields) != len(header_fields):
            skipped += 1
            continue

        line_type = get(fields, "EXP/FEE/INV_ADJ_TYPE").upper()
        matter_id = get(fields, "LAW_FIRM_MATTER_ID")
        entity = get(fields, "LAW_FIRM_ID") or "Unknown firm (LAW_FIRM_ID missing)"
        task_code = get(fields, "LINE_ITEM_TASK_CODE")
        billed = get(fields, "LINE_ITEM_TOTAL")

        if line_type not in ALLOWED_LINE_TYPES:
            skipped += 1
            continue
        if (
            not is_decimal(billed)
            or not is_decimal(get(fields, "INVOICE_TOTAL"))
            or not is_decimal(get(fields, "LINE_ITEM_ADJUSTMENT_AMOUNT"), allow_blank=True)
        ):
            skipped += 1
            continue
        if line_type == "F" and (
            not is_decimal(get(fields, "LINE_ITEM_NUMBER_OF_UNITS"))
            or not is_decimal(get(fields, "LINE_ITEM_UNIT_COST"))
        ):
            skipped += 1
            continue

        if line_type == "F":
            rows.append({
                "entity": entity,
                "matter_id": matter_id,
                "matter_type": infer_matter_type(task_code),
                "timekeeper_role": get(fields, "TIMEKEEPER_CLASSIFICATION") or "Unspecified",
                "timekeeper_name": get(fields, "TIMEKEEPER_NAME"),
                "hours": get(fields, "LINE_ITEM_NUMBER_OF_UNITS"),
                "rate": get(fields, "LINE_ITEM_UNIT_COST"),
                "billed_amount": billed,
                "budget_estimate": "",  # not present in LEDES 98B
                "line_item_description": get(fields, "LINE_ITEM_DESCRIPTION"),
                "task_code": task_code,
                "activity_code": get(fields, "LINE_ITEM_ACTIVITY_CODE"),
                "line_item_date": get(fields, "LINE_ITEM_DATE"),
                "invoice_number": get(fields, "INVOICE_NUMBER"),
                "line_type": "fee",
            })
        elif line_type == "E":
            rows.append({
                "entity": entity,
                "matter_id": matter_id,
                "matter_type": infer_matter_type(""),
                "timekeeper_role": "",
                "timekeeper_name": "",
                "hours": "",
                "rate": "",
                "billed_amount": billed,
                "budget_estimate": "",
                "line_item_description": get(fields, "LINE_ITEM_DESCRIPTION"),
                "task_code": "",
                "activity_code": "",
                "line_item_date": get(fields, "LINE_ITEM_DATE"),
                "invoice_number": get(fields, "INVOICE_NUMBER"),
                "line_type": "expense",
            })
        else:
            # Invoice-level adjustment or unrecognized type; keep for completeness
            rows.append({
                "entity": entity,
                "matter_id": matter_id,
                "matter_type": infer_matter_type(""),
                "timekeeper_role": "",
                "timekeeper_name": "",
                "hours": "",
                "rate": "",
                "billed_amount": billed,
                "budget_estimate": "",
                "line_item_description": get(fields, "LINE_ITEM_DESCRIPTION"),
                "task_code": "",
                "activity_code": "",
                "line_item_date": get(fields, "LINE_ITEM_DATE"),
                "invoice_number": get(fields, "INVOICE_NUMBER"),
                "line_type": line_type or "unknown",
            })

    if not rows:
        raise ValueError("LEDES file contains no valid data rows after structural and numeric validation.")

    return rows, skipped


def write_normalized_csv(rows, output_path: Path):
    """Write normalized rows while preserving validated numeric fields."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=NORMALIZED_FIELDNAMES)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                field: safe_csv_text(row.get(field, ""))
                if field in TEXTUAL_OUTPUT_FIELDS
                else row.get(field, "")
                for field in NORMALIZED_FIELDNAMES
            })


def main():
    if len(sys.argv) != 3:
        print("Usage: python parse_ledes.py <input.txt> <output.csv>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not is_ledes_1998b(input_path):
        print("Warning: file does not start with 'LEDES1998B[]' -- proceeding anyway, but double-check this is really a LEDES 1998B export.")

    try:
        rows, skipped = parse(input_path)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)

    write_normalized_csv(rows, output_path)

    fee_count = sum(1 for r in rows if r["line_type"] == "fee")
    expense_count = sum(1 for r in rows if r["line_type"] == "expense")
    print(f"Parsed {len(rows)} line items ({fee_count} fee, {expense_count} expense) into {output_path}")
    if skipped:
        print(f"Skipped {skipped} malformed row(s) that failed structural or numeric validation.")
    print("Note: no firm names (only LAW_FIRM_ID), no matter type field, and no budget/estimate "
          "field exist natively in LEDES 1998B -- these are approximated or left blank per the "
          "limitations documented at the top of this script. State these limitations in the report.")


if __name__ == "__main__":
    main()
