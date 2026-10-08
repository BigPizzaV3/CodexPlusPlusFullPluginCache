---
name: horizon-forecast
description: Produce deep multi-agent forecasts of industry growth and overlooked economic opportunities, with an executed research plan, scenarios, evidence-backed ratings, and falsifiable milestones. Use for cross-industry rankings or full future-of-a-field research.
---

# Horizon Forge: research director

Turn a broad question about the future into an auditable forecast of economic outcomes. Optimize for careful research, causal explanation, and useful decisions. Give a substantial, readable report; length must come from distinct evidence and analysis.

## Start here

1. Read [operating instructions](references/operating-instructions.md) and [defaults](../../config/defaults.json). User instructions override these defaults. Calculate dates from the current date; do not copy dates from examples.
2. Establish the decision, sectors, geography, baseline year, primary 5- and 10-year endpoints, and economic measure. Ask only questions that materially change the research. Proceed with clearly stated defaults while optional answers are pending.
3. Before substantive research, write and show the research plan and ordered procedure using [the plan template](templates/research-plan.md). Include questions, specialists, sources, dependency map, scoring choices, verification gates, and stopping rules. Execute it without waiting for approval unless approval is actually required. Keep its status current.
4. For a full forecast, use real specialist subagents when the host exposes delegation. This skill explicitly requests delegation for independent research and review. Read [agent orchestration](references/agent-orchestration.md). Respect available slots and existing host limits. The lead remains responsible for synthesis and verification. Do not create user-owned tasks or change account/model settings to obtain more agents.

## Execute the plan

Follow [research procedure](references/research-procedure.md), loading the detailed references when entering the relevant stage:

- Broad discovery: use [horizon-scan](../horizon-scan/SKILL.md). Include mundane infrastructure, services, and emerging-market opportunities; do not anchor the universe on popular technologies.
- Claims and contradictions: use [horizon-evidence](../horizon-evidence/SKILL.md). Retrieve original sources and reconcile definitions before comparing numbers.
- Quantification: use [horizon-scenarios](../horizon-scenarios/SKILL.md) and [scoring](references/scoring.md). Give real annual size, incremental size, adoption, scenarios, and confidence where defensible. Abstain from unsupported numerical estimates.
- Challenge: delegate [horizon-red-team](../horizon-red-team/SKILL.md) after initial specialist findings. Seek external counterevidence and identify the premise that would reverse the ranking.
- Revisions: use [horizon-update](../horizon-update/SKILL.md) when updating an existing forecast. Preserve the original record.

Research material tangents with a causal link to demand, cost, adoption, supply, timing, or economic capture. Keep speculative distant connections in a bounded watchlist. Prioritize the unknowns most likely to change the decision, not a fixed volume of searches.

## Deliver and verify

Use [report template](templates/report.md) and [artifact contracts](references/artifact-contracts.md). A full dossier usually supports 4,000–8,000 words, excluding source and calculation appendices. Adapt to scope, user preferences, and output limits; save the full dossier when it will not fit comfortably in chat. Never pad or invent evidence to reach a word count.

Before completion, verify leading claims against opened sources, calculations against inputs, score explanations against anchors, scenario coherence, overlapping market boundaries, and all material critic findings. Report plan completion and any gaps. Distinguish an implemented research process from proven forecasting accuracy.

Default deliverables: readable report, ranking table, research plan with completion status, evidence ledger, assumptions and disagreement log, scenario/scoring inputs and results, and dated forecast register with update triggers. Use writable task-local paths and link only actual deliverables.

For methodological provenance and limits of prompting techniques, read [research basis](references/research-basis.md) when explaining or modifying this plugin.
