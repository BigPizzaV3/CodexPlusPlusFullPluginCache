# Trust Evidence Bundle: Quick Start

Aivana GmbH — https://www.aivana-gmbh.ai

Requires Python 3.11+ and no package installation or Docker.

```powershell
python scripts/run.py --input examples/input.json --output output/result.json
python -m unittest discover -s tests -v
```

The output is local JSON. Review `findings`, `coverage`, `access_summary`, and `approval_required`; the example is expected to be complete.
