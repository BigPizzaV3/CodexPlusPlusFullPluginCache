"""Offline text checks only; no network, storage, provider action or readiness claim.

Run with host-local Python and JSON on stdin:
{"value":"draft text","max_length":200,"required":false,"constraints_inspected":true}
Output never echoes the draft. Inspect actual format/options/consent requirements
separately. A passing text check is not full-form validation or permission to send.
"""

import json
import sys


def check_text(
    value: str,
    max_length: int | None = None,
    *,
    required: bool = False,
    constraints_inspected: bool = False,
    textarea: bool = True,
) -> dict:
    if not isinstance(value, str):
        raise ValueError("A text value is required")
    if max_length is not None and (
        not isinstance(max_length, int)
        or isinstance(max_length, bool)
        or max_length < 0
    ):
        raise ValueError("Use a nonnegative observed limit or null")
    if not all(
        isinstance(flag, bool) for flag in (required, constraints_inspected, textarea)
    ):
        raise ValueError("Flags must be boolean")
    measured = value.replace("\r\n", "\n").replace("\r", "\n") if textarea else value
    units = len(measured.encode("utf-16-le", errors="surrogatepass")) // 2
    present = not required or bool(value.strip())
    fits = (max_length is None or units <= max_length) and present
    return {
        "length_utf16": units,
        "observed_max_length": max_length if constraints_inspected else None,
        "required_value_present": present if constraints_inspected else None,
        "fits_inspected_text_constraints": fits if constraints_inspected else None,
        "scope": "Text length/required value only; not full-form validation, readiness or transmission permission",
    }


def main() -> int:
    try:
        result = check_text(**json.load(sys.stdin))
    except (ValueError, TypeError):
        print(json.dumps({"error": "Invalid offline text-check input"}))
        return 2
    print(json.dumps(result))
    return 1 if result["fits_inspected_text_constraints"] is False else 0


if __name__ == "__main__":
    raise SystemExit(main())
