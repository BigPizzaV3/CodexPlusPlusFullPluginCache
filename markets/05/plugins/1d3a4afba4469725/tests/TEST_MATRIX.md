# Local regression test matrix

Run these commands from the plugin root.

## Automated regression suite

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_*.py'
```

The suite verifies:

- formula-like workbook and CSV values remain literal text while genuine negative numbers remain numeric;
- the bundled LEDES fixture reconciles to 23 rows and $124,774.50;
- malformed, incomplete, reordered, unterminated, and nonnumeric LEDES inputs are rejected or skipped;
- every referenced positive-test fixture exists;
- every golden workbook uses the five-tab contract; and
- every golden report identifies its data as synthetic.

## Package validation

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool tests/evals.json >/dev/null
python3 -m json.tool tests/submission-test-cases.json >/dev/null
python3 /Users/peterprice/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/spend-management-analysis
python3 /Users/peterprice/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

## Workbook QA

Open the five `.xlsx` files under `tests/expected/` and confirm Summary, Action Plan, Findings, AI Leverage, and Normalized Data are present and readable. The Summary tab must show the synthetic-data notice. AI Leverage must either contain task-supported opportunities with safeguards or explicitly record that it was not assessed.
