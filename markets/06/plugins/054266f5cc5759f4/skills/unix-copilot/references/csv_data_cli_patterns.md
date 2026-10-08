# CSV and CLI Data Patterns

## Purpose

Use this file for CSV, TSV, delimited data, encoding, BI preparation, and command-line analytics.

# 1. CSV is not “split on comma”

General CSV can contain:
- quoted delimiters;
- embedded quotes;
- embedded newlines;
- different line terminators;
- different delimiters/dialects.

A line-oriented command may be wrong even when it works on simple samples.

# 2. When `awk`/`cut` is acceptable

Use simple delimiter tools only when assumptions are explicit, for example:

> Assumes fields never contain quoted commas, embedded newlines, or escaped delimiters.

For simple TSV without embedded tabs/newlines, line tools may be appropriate.

# 3. CSV-aware options

Prefer one of:
- Python `csv`;
- Miller (`mlr`);
- csvkit;
- DuckDB;
- another parser with clear CSV support.

Choose based on what is already installed and the size/task.

# 4. Python `csv`

Use `newline=''` when opening CSV files because Python’s CSV parser handles newline conventions itself and embedded quoted newlines correctly.

Example:

```python
import csv

with open("input.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ...
```

Specify delimiter/quote behavior when the file is not standard comma-separated CSV.

# 5. Headers

Validate:
- duplicate names;
- blank names;
- unexpected whitespace;
- inconsistent order;
- encoding/BOM.

Do not normalize names destructively without recording the mapping.

# 6. Ragged rows

Validate field count only after accounting for quoting rules.

A naive:

```bash
awk -F, 'NF != expected'
```

is not reliable for general quoted CSV.

Use a CSV parser when quoted/multiline fields are possible.

# 7. Encoding

`file` or MIME inspection is a clue, not proof of encoding.

For conversion with `iconv`, specify the known/verified source encoding:

```bash
iconv -f WINDOWS-1252 -t UTF-8 input.csv > output.csv
```

`-c` discards invalid input sequences and can lose data.

Do not call:

```bash
iconv -f UTF-8 -t UTF-8 -c
```

an encoding conversion; it is filtering invalid UTF-8 bytes.

# 8. BOM

A UTF-8 BOM can affect the first header name.

Use a CSV-aware parser or explicit BOM-aware decoding when needed.

Do not assume every `sed` escape syntax is portable.

# 9. BI preparation

For analytics/Power BI ingestion:

1. preserve raw input;
2. inspect encoding/delimiter/header;
3. validate rows;
4. define duplicate rule;
5. preserve identifier strings;
6. standardize dates only when semantics are known;
7. write new output;
8. reconcile rows/rejects.

Do not silently:
- drop leading zeros;
- change decimal separators;
- infer locale-specific dates;
- convert blanks to zero;
- merge duplicate records.

# 10. Validation

Useful checks:
- input/output row count;
- rejected-row count;
- column count/schema;
- duplicate key count;
- null/blank count;
- checksum for unchanged files;
- sample diff.

Treat the parser’s definition of a record as authoritative when fields can contain embedded newlines.
