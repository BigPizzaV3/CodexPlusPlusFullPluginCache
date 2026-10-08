# Changelog

## 2.5.9

### Research-quality improvements
- Added a dedicated historical market/regime module with systematic 1M, 3M, 6M, YTD, and 1Y comparisons when decision-relevant.
- Added common-window and young-fund rules so partial histories are not compared as if equivalent.
- Added benchmark-relative performance and a momentum-dependency test to reduce recency bias.
- Strengthened Market Strategist separation of durable leadership, event repricing, mean reversion, and extended momentum.
- Strengthened Geopolitical Risk Analyst with explicit causal transmission mapping, “already priced” assessment, comparable historical analogues, and counterexamples.
- Added commodity/futures data hygiene for spot vs front-month vs continuous-contract series and roll effects.
- Added `scripts/return_context.py` for reproducible relative-return and preceding-3M calculations.

### Efficiency improvements
- Reworked the evidence packet into triggered modules rather than requiring every dataset on every query.
- Quick Scan now avoids broad macro/history research unless it can change the conclusion.
- Full ETF/sector comparisons reuse one multi-horizon history packet across the panel.
- Historical event studies are escalation-only, not a default geopolitical research step.

### Instruction cleanup
- Consolidated repeated panel-output rules into the report template.
- Consolidated role responsibilities and horizon weights into `judges.md`.
- Fixed the prior tension between “display weights before scores” and Decision View by setting weights internally before voting and exposing them in Audit View.
- Reduced duplicated workflow language while preserving hard non-tailoring and compliance boundaries.
