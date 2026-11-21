---
name: json-diff
description: Compare strict JSON documents semantically and inspect changed JSON Pointer paths, types, and decimal values.
---
Call `compare_json` with `before` and `after` as strict JSON strings. Object key order does not matter; array order does. Duplicate keys are rejected. Decimal numbers compare without floating-point rounding. Do not include secrets.
Explain the counts and any type changes. The empty JSON Pointer path means the root; `~0` escapes a tilde and `~1` escapes a slash. Array differences use indexes, not move detection. The interactive card filters and searches changes. The report contains complete values and expires in about one hour; previews may be shortened.
Limits: 20,000 characters and 4,000 values per document, depth 64, 500 differences, numeric exponents from -10000 through 10000. Do not call for source code, YAML, JSON5, or patch execution.
