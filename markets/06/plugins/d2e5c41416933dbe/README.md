# Aivana Outcome Operations

Combine supplied KPI signals, revenue findings, evidence, and proposed actions into one reviewable operating brief.

Publisher: [Aivana GmbH](https://www.aivana-gmbh.ai). Language: English (United States).

```powershell
python scripts/run.py --input examples/input.json --output output/result.json
python -m unittest discover -s tests -v
```

Input accepts `goal`, `evidence`, optional `kpis`, `revenue_findings`, `constraints`, and `actions`. The output contains a status, signals, steps, evidence references, risks, guardrails, approval flags, and a reversible preview. All references must point to supplied evidence IDs.

Limits: no external connectors, action execution, currency conversion, causal ROI proof, or completion assertion. This is a local planning bundle; its component engines remain available separately.
