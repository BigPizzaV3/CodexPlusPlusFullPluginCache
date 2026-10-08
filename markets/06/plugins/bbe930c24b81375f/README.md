# Aivana Incident Intelligence

Combine sanitized incident events and explicit migration checks into one evidence-linked review brief.

Publisher: [Aivana GmbH](https://www.aivana-gmbh.ai). Language: English (United States).

```powershell
python scripts/run.py --input examples/input.json --output output/result.json
python -m unittest discover -s tests -v
```

Input accepts `incidents` with IDs, messages, and optional request/expected response objects, plus optional `migration_checks`. Output contains groups, reproducibility counts, migration risk findings, evidence references, and approval flags.

Limits: no network replay, log ingestion, data migration, target-system validation, or automatic remediation. Sanitization is not authenticity proof; review before sharing.
