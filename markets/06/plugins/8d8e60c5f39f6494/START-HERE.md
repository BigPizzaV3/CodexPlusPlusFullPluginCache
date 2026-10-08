# Horizon Forge

## A research team for the future economy

**Optional tip jar:** [Support on Ko-fi](https://ko-fi.com/quietengine). Tips are entirely optional.

Horizon Forge is a personal Codex plugin for deep analysis of future industry growth and overlooked economic opportunities. It writes a research plan and ordered procedure, executes research with specialist agents, checks evidence, models scenarios, challenges its initial conclusions, and produces a substantial report with inspectable ratings.

Your defaults are built in: **global industry opportunities**, **5–10-year primary forecasts**, **1–3-year signposts**, and **10–20-year longer-term scenarios**. Quality takes priority over speed. Full reports usually target **4,000–8,000 words**, with supporting sources and calculations; the actual length adapts to the question and available evidence.

## Start a forecast

Once the plugin is installed, start a new Codex task and select Horizon Forge or use:

```text
Use $horizon-forecast to identify the most overlooked industries likely to grow substantially across the global economy over the next 5–10 years. Create a deep research plan and procedure first, then execute it using specialist agents. Research material upstream, downstream, and second-order effects. Prioritize quality over speed. Give me a full dossier with industry growth ratings, overlooked-opportunity ratings, evidence confidence, scenarios, failure conditions, and measurable signposts.
```

For a first narrow investigation, replace the broad discovery request with a field you care about. You do not need to specify every research step; the plugin provides the procedure. More ready-to-use requests are in [Prompt library](PROMPT-LIBRARY.md).

Choose the model and reasoning level you prefer in the host app. The plugin inherits those settings; instructions cannot silently raise them. Actual specialist concurrency depends on the host. If subagents are unavailable, the report must say it used sequential specialist passes. The plugin requires no paid data subscription or external API key of its own; it uses the research and delegation tools available in the task. More research and subagents can consume substantially more usage.

## What it produces

The main answer explains which fields have the strongest growth cases and why, where overlooked opportunities sit inside them, and what could invalidate the conclusion. It is accompanied by a record of what was researched and calculated.

| Deliverable | What it lets you inspect |
|---|---|
| Executed research plan | Questions, procedure, specialists, evidence gates, completion and gaps |
| Comparative ranking | Defined segments, horizons, growth, overlookedness and confidence |
| Field assessments | Buyer economics, causal mechanisms, constraints, regions and competition |
| Scenario analysis | Possible annual economic sizes, assumptions and critical dependencies |
| Skeptical review | Strong contrary evidence and how it changed the result |
| Source and assumption records | Original evidence, conflicts, units, dates and missing information |
| Forecast register | Measurable predictions, deadlines, resolution rules and future updates |

The report will save the full dossier when it is too long for a comfortable chat response. It examines tangential factors when they can materially change demand, cost, adoption, supply, timing, or economic capture. Less-supported distant possibilities stay visible in a watchlist.

## How to read the ratings

**Growth potential /100** considers demand, adoption, feasibility, economic scale and resilience. **Overlooked opportunity /100** considers underprovision, attention gaps, bottleneck importance, approaching inflections and entry paths. **Evidence confidence** states how well the underlying case is supported.

These are distinct judgments. An 85 growth rating is not an 85% chance of success. A field with great upside and weak evidence stays provisional. Unknown components produce score bounds, and low-confidence candidates do not quietly enter the main ranking. Weight sensitivity shows where rankings reverse under modest changes to priorities.

When the evidence allows a probability forecast, the plugin defines a measurable event separately. Its editable starting convention for a global segment is at least **2× real annual economic size and USD 10 billion in added annual size within ten years**. It adjusts that definition when the comparison calls for another scale and states the choice before ranking.

The ratings and thresholds are custom research conventions, not a statistically trained forecasting model. They are designed to make judgment explicit and reviewable. A high-growth industry also does not automatically provide high investment returns; valuation, competition, margins and access are separate questions.

## The specialist team

The research director coordinates eight specialist assignments:

1. Opportunity discovery.
2. Demand and adoption.
3. Technology and supply feasibility.
4. Institutions and geopolitics.
5. Market economics and value chains.
6. Scenarios and forecasting.
7. Skeptical challenge.
8. Evidence and numerical audit.

These are functional roles rather than eight agents that must run simultaneously. The director schedules relevant work in waves within available capacity, keeps initial estimates separate where possible, then reconciles evidence and disagreement. Specialists write their own memos; the director owns the final comparison.

## Six reusable skills

| Skill | Use it for |
|---|---|
| `$horizon-forecast` | The full plan-to-dossier workflow |
| `$horizon-scan` | Finding and screening candidates |
| `$horizon-evidence` | Checking claims and conflicting market estimates |
| `$horizon-scenarios` | Modeling outcomes and applying ratings |
| `$horizon-red-team` | Challenging an existing thesis or ranking |
| `$horizon-update` | Revisiting forecasts and scoring resolved predictions |

The main skill selects the supporting workflows as needed. Individual skills are useful when you already have a report or only need a particular stage.

## Research choices behind the instructions

The design draws on forecasting tournament research, retrieval-based language-model forecasting, OECD foresight methods, analytic standards, economic measurement guidance, and official OpenAI documentation. The [research basis](skills/horizon-forecast/references/research-basis.md) links the sources and explains where their findings do and do not transfer.

Practical techniques include independent initial estimates, original-source tracing, comparison with historical failures, explicit falsification conditions, causal dependency maps, external verification, and sensitivity analysis. They improve the structure of the work; this build does not claim a measured increase in forecast accuracy. That requires freezing forecasts and observing outcomes over time. The included Brier calculation supports that future evaluation.

## Customizing it

For one run, simply state a different geography, horizon, number of fields, report length, or objective. Your request overrides defaults.

For durable changes, edit the following source files and reinstall the revised plugin so new tasks load it:

- [Default profile](config/defaults.json): horizons, scope, depth and output targets.
- [Custom operating instructions](skills/horizon-forecast/references/operating-instructions.md): research behavior and depth requirements.
- [Scoring rubric](skills/horizon-forecast/references/scoring.md): rating definitions, weights and eligibility.
- [Agent orchestration](skills/horizon-forecast/references/agent-orchestration.md): specialist responsibilities and assignments.
- [Report template](skills/horizon-forecast/templates/report.md): final report structure.

If changing rubric dimensions or weights permanently, keep the calculator constants and tests synchronized. A one-run weight override is already supported through calculator inputs. Keep your changes to this plugin's source; do not put its instructions into global settings unless you want them to affect unrelated tasks.

## Package and installation

The distributable is a skills-based Codex plugin. Its manifest is `.codex-plugin/plugin.json`; all methods, templates and calculations are included inside this folder. There is no hosted service, background daemon, external account, or hidden dependency. The arithmetic helper requires Python 3; research itself uses Codex's available tools.

For a personal installation, place this `horizon-forge` folder in your personal plugin source directory, add its entry to your personal marketplace with Codex's plugin-creator workflow, then install `horizon-forge@personal` (or the actual name of your personal marketplace). Start a new task after installation. The build handoff reports whether this installation was completed on the current machine.

The downloadable/output folder and an installed personal source folder are separate copies. To update an installed plugin, copy your revised files into its personal source folder before reinstalling; editing a downloaded copy alone does not update the active plugin.

## Validation and limits

See [Validation record](VALIDATION.md) for actual checks and observed workflow behavior. Synthetic examples in [examples](examples/) are only arithmetic fixtures. No real industry recommendations, forecast accuracy claims, or hidden success metrics are embedded in them.

The plugin defines update triggers, but it does not schedule recurring monitoring unless you ask. When you want a fresh assessment, use `$horizon-update` and identify the saved forecast. Its source records and dated revisions make the change explainable.
