# No BS PPC by Fiera

A ChatGPT and Codex plugin that answers Google Ads questions like a senior paid search manager. It reads report exports to back each answer with numbers.

## Skills

| Skill | What it does |
|---|---|
| no-bs-ppc | Direct answers: verdict, the numbers that decide it, the action, what would change it. Corrects common mistakes |
| performance-triage | From a campaign report by day: splits a CPA or conversion change into demand, share, CTR, CPC and CVR, by segment, with mix shift |
| search-terms-cleanup | N-grams of a search terms report, safe negative candidates, routing decisions |
| account-quick-audit | Prioritized audit from shared exports and screenshots |
| rsa-review | Writes and checks RSAs: limits, editorial rules, duplicates, competitor names |
| bid-targets | Target CPA or ROAS from unit economics |
| budget-pacing | Month-to-date spend, forecast, daily spend needed |
| auction-insights | Competitor share changes, new entrants, position above |
| change-history-review | Risky changes and the ones that line up with a performance shift |
| quality-score-review | Spend-weighted Quality Score and the component to fix |

All skills share `scripts/ppc.py` (pandas, numpy) and references with Fiera's decision rules and verified platform facts.

## Run the script locally

```bash
pip install pandas numpy openpyxl
python skills/performance-triage/scripts/ppc.py inspect --data campaigns.csv
python skills/performance-triage/scripts/ppc.py triage --data campaigns.csv --a 2026-08-01:2026-08-28 --b 2026-08-29:2026-09-25 --out triage
python skills/search-terms-cleanup/scripts/ppc.py ngrams --data search_terms.csv --target-cpa 60 --out ngrams
```

## Source layout

- `dev/src/ppc.py`: the script, copied into each skill by `dev/build.sh`.
- `dev/skills_src/`: SKILL.md per skill.
- `dev/shared/references/`: references copied into each skill.
- `dev/tests/`: tests with synthetic Google Ads exports in English and Spanish.
- `dev/eval/`: the 20-question comparison against an assistant without the plugin.

## License

Apache-2.0.
