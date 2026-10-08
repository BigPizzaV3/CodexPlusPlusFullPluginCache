# Equity Council

A Codex plugin for deep research into publicly traded companies in an industry. It writes a plan, executes specialist investigations, builds valuations, challenges the leading thesis, checks sources and calculations, and produces an ordered research report.

**Default focus: 5–10 years of compounding, with a seven-year central model.** The starting universe is U.S.-listed common equities and ADRs. Both can be changed in any request.

## Start here

After installing/enabling the plugin, start a new Codex task and use:

> Use $equity-council to analyze the semiconductor equipment industry. Prioritize quality over speed. Write the research plan and procedure first, then execute it. Rank the five strongest opportunities for 5–10 year compounding. Explain expected returns, downside, source quality, market-implied expectations, and the assumptions that would change the winner.

Or simply:

> Use $equity-council for the water infrastructure industry.

The director supplies explicit defaults, publishes its plan and continues researching. If the industry is missing, it asks for the industry. A full run needs live research access for current conclusions; an offline run produces conditional analysis and identifies missing evidence.

## Eleven skills and their expert roles

| Skill | Responsibility |
|---|---|
| `equity-council` | Research director, planning, coordination and final ranking |
| `equity-universe` | Industry economics, value chain, candidate discovery and exclusions |
| `equity-business` | Competitive advantage, customer economics and reinvestment runway |
| `equity-financials` | Forensic accounting, cash conversion, capital structure and dilution |
| `equity-stewardship` | Management incentives, governance and capital allocation |
| `equity-risk` | Financing, macroeconomic, regulatory and technology risks |
| `equity-catalysts` | Expectations, milestones and mechanisms for value realization |
| `equity-valuation` | Reverse valuation, cash-flow models and shareholder scenarios |
| `equity-red-team` | Strongest countercase, thesis-breaking evidence and rank reversals |
| `equity-audit` | Independent source, calculation and ranking verification |
| `equity-update` | New evidence, changed rankings and forecast accountability |

These are real skill instructions with distinct assignments and deliverables. When Codex provides subagents, the director delegates independent work in waves within available capacity. When it does not, it performs the lenses sequentially and says so. The plugin cannot enable missing tools, force a model's reasoning setting, or make separate agents statistically independent.

## What makes the analysis deep

- A visible decision contract and procedure before screening.
- A broader universe than familiar tickers, including adjacent value-chain beneficiaries.
- Source and accounting reconciliation before company comparisons.
- Industry-specific methods for banks, insurers, REITs, software, semiconductors, commodities, utilities, biotech and other business models.
- A causal test for tangents: external change → business driver → cash flow or funding → shareholder outcome.
- Reverse valuation to identify expectations already embedded in price.
- Five-, seven- and ten-year forecasts, adverse sensitivities, dilution and funding outcomes.
- Independent countercases and neutral reconstruction of decisive claims/calculations.
- A substantial research memo, generally with five company dossiers, comparative tables, dissent and linked appendices.
- Dated forecasts that can later be scored without rewriting history.

The workflow emphasizes evidence and decision-relevant depth. It does not require artificial delays, endless debate or repetitive prose. The research basis includes 20 primary-source references; see [RESEARCH.md](RESEARCH.md).

## How rankings work

Success defaults to **a positive nominal total return and beating a declared broad-market total-return benchmark over the same horizon**. The output keeps success probability, expected return, severe-loss exposure and evidence quality separate.

The default policy asks for at least 60% modeled success probability and at most 20% modeled probability of losing 40% or more at the horizon, across the selected sensitivity sets. It also requires a positive conservative annualized expected wealth return and adequate evidence. These thresholds are configurable preferences, not scientific constants or a guarantee.

Among eligible candidates, the tool identifies the **Pareto frontier**: companies for which another candidate is not at least as good on return, success probability and severe-loss exposure simultaneously. It then orders the frontier by conservative annualized expected wealth, showing probability-first and upside comparisons alongside it. It preserves nonqualifiers and reasons, and permits tied tiers or no qualifying opportunity.

Scenario probabilities are conditional assumptions unless an estimation/calibration process supports more. If probabilities or current inputs cannot be defended, the report uses ranges and conditional conclusions. A software-generated rank cannot override missing evidence. See [full method](references/ranking-method.md).

## Custom instructions

You can override any research preference in your request:

> Use $equity-council for industrial automation. Include global listings, use EUR returns, model ten years, compare with a suitable global benchmark, focus on small and mid caps, and include at least two overlooked suppliers. Prioritize probability of benchmark outperformance over maximum upside. Produce detailed dossiers for the top eight.

The director records the overrides and changes the ranking procedure consistently. The bundled calculator supports the default success event; another event requires a transparent adapted calculation. The plugin never silently treats a new objective as the old one.

Persistent package defaults are in [config/defaults.json](config/defaults.json). Prefer per-run changes in `mandate.json` or the prompt; installed caches may be replaced during updates. Custom specialist instructions live in each `skills/<name>/SKILL.md`; shared contracts are in `references/`. There is no hidden prompt or service dependency.

## Included tools and artifacts

Python 3.10+ is needed only for the optional deterministic helpers; they use the standard library.

```text
python scripts/new_run.py --industry "Semiconductor equipment" --output /path/to/new/research-run
python scripts/scenario_rank.py /path/to/research-run/scenario-input.json --output /path/to/research-run/ranking.json
python -B -m unittest discover -s tests -v
```

Use quoted Windows paths where appropriate. `new_run.py` refuses an existing directory or a destination inside the plugin. It creates a mandate, procedure checklist, evidence/universe/assumption/conflict/tangent/forecast ledgers, a briefs folder and checkpoint. It deliberately creates no invented financial model. The calculator's [input contract](references/calculator-input.md) and [fictional fixture](tests/fixtures/scenario-example.json) explain the schema and math.

## Installation status and portability

This deliverable is a **portable plugin source folder and ZIP**, not a claim that the plugin is already installed. The ZIP has one `equity-council/` root containing `.codex-plugin/plugin.json` and `skills/`.

For installation in Codex, use the host's supported local-plugin import or the `plugin-creator` personal-marketplace workflow. On this Windows setup that workflow uses the user's personal plugin directory and existing personal marketplace; preserve unrelated entries/files. Ask Codex to install the supplied ZIP and verify `codex plugin list` shows `equity-council` enabled, then start a new task. No marketplace entry is embedded in this portable archive, because installation paths and existing catalogs differ by user.

## Boundaries and validation

Website and optional tip jar: [Quiet Engine on Ko-fi](https://ko-fi.com/quietengine). Tips are entirely optional.

The plugin conducts research; it does not place trades or create scheduled monitors. Source/model verification does not establish future returns, calibrated stock-selection odds or a tested investment track record. A full report is only as current and reliable as the available evidence.

See [VALIDATION.md](VALIDATION.md) for actual structural, mathematical and behavioral checks, observed fixes and remaining limitations. Future meaningful validation is a live industry research run with human source review, followed by forward forecast tracking.
