# Aivana Trust Evidence Bundle

Create a deterministic, reviewable trust bundle from supplied decision records, requirements, inline evidence, and declared access observations. Publisher: [Aivana GmbH](https://www.aivana-gmbh.ai). The plugin uses Python 3.11+ standard library only and makes no external calls or writes.

## Run locally

```powershell
python scripts/run.py --input examples/input.json --output output/result.json
python -m unittest discover -s tests -v
```

Input requires four lists: `requirements` (`id`, `text`), `decisions` (`id`, `title`, `rationale`, `requirement_ids`, `evidence_ids`), `evidence` (`id`, `origin`, inline `content`, optional `requirement_ids` and `expected_sha256`), and `access_checks` (`id`, `subject`, `resource`, `action`, `expected`, `observed`, optional `evidence_ids` and `requirement_ids`). IDs and references must be unique and known. Access values are `allow` or `deny`.

The output contains `bundle` counts and a deterministic fingerprint, per-requirement `coverage`, `access_summary`, `findings`, `approval_required`, and `limitations`. Evidence hashes catch supplied-content mismatches. A requirement is covered when it has an active decision and valid evidence. An access check is verified only when expected equals observed and all referenced evidence hashes are valid. Any finding sets `status` to `needs_review` and `approval_required` to true.

The plugin evaluates declarations only. It does not retrieve evidence, execute tests or permissions, authenticate users, inspect files, or provide legal, regulatory, or security certification. Hash equality does not prove authorship or authenticity. Inputs are limited to 2,000 requirements and 5,000 records in other collections; JSON input is limited to 8 MiB by the CLI.
