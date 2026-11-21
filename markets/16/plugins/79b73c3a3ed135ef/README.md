# Fiera Incrementality

A ChatGPT and Codex plugin that helps paid media teams measure whether their ads drive results that would not have happened anyway.

## Skills

| Skill | What it does |
|---|---|
| incrementality-planner | Explains incrementality and turns a question into a test plan. Recommends the platform's lift study when available, a geo experiment, a switchback, or a directional read |
| geo-test-design | Picks treated regions from a KPI-by-region-by-day CSV, estimates the MDE on held-out history, the duration and the cost, and writes the plan |
| geo-test-readout | Estimates the effect with TBR and synthetic control, placebo-based intervals, iCPA and iROAS, and robustness checks |
| quick-incrementality | Directional before/after comparison against several baselines and their normal noise; switchback analysis |
| lift-result-review | Reviews a lift study, vendor test or internal claim |

All skills share `scripts/geolift.py` (numpy, pandas, scipy) and a set of references with sourced methods, platform requirements and evidence.

## Run the script locally

```bash
pip install numpy pandas scipy matplotlib
python skills/geo-test-design/scripts/geolift.py profile --data panel.csv
python skills/geo-test-design/scripts/geolift.py design --data panel.csv --test-days 28 --out design
python skills/geo-test-readout/scripts/geolift.py readout --data panel.csv --treated A B C --start 2026-03-02 --end 2026-04-12 --out readout
```

## Validation

The estimator is calibrated on simulated panels with autocorrelated shared and geo-level shocks and Poisson noise, 200 panels per scenario. Results are in `skills/geo-test-readout/references/validation.md`.

## Source layout

- `dev/src/geolift.py`: the script (copied into each skill by `dev/build.sh`).
- `dev/skills_src/`: SKILL.md per skill.
- `dev/shared/`: references and templates copied into each skill.
- `dev/tests/`: unit tests and the panel simulator.
- `dev/validation/`: calibration study.
- `dev/build.sh`: assembles `skills/`, runs tests, validates the manifest, writes the ZIP to `dev/dist/`.

## License

Apache-2.0.
