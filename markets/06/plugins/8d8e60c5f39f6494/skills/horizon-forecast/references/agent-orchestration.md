# Specialist orchestration

## Roles are assignments, not credentials

The director owns the plan, shared definitions, source deduplication, scenario consistency, ratings, and final report. Specialists provide bounded research outputs. Use relevant roles; omit a role with no useful independent assignment and document material coverage elsewhere.

| Specialist | Question and required contribution |
|---|---|
| Opportunity scout | Which overlooked segments have an emerging mechanism of growth? Return a diverse longlist, established comparator, and weak-evidence candidates. |
| Demand and adoption analyst | Who pays, from which budget, for what measurable benefit? Examine retention, substitution, switching costs, diffusion, and regional purchasing power. |
| Technology and supply analyst | Can the service be delivered at required cost, reliability, yield, and scale? Find actual performance, capacity, energy, materials, labor, and deployment limits. |
| Institutions and geopolitics analyst | Which rules, trade conditions, public procurement, financing structures, or social reactions affect commercial timing by region? |
| Market and value-chain economist | What is counted, how much activity exists, what grows net of substitution, and who captures revenue or surplus? Reconcile overlapping estimates and map neglected complements. |
| Scenario forecaster | Build independent initial probabilities or ranges, reference classes, capacity-constrained scenarios, and sensitivity analysis. |
| Skeptical challenger | What would make the preferred thesis fail? Find contrary evidence, historical failures, hidden dependencies, saturation, and a stronger alternative. |
| Evidence and numerical auditor | Can key citations and calculations be reproduced? Check source lineage, dates, definitions, arithmetic, evidence gaps, and response to challenges. |

## Scheduling on any host

1. Discover the actual delegation tools and concurrency limit. Never invent callable names or set a fixed agent count greater than capacity.
2. Keep one slot for the director. With four total slots, run up to three specialists concurrently. Reuse or retire completed specialists using actual host controls; do not assume that a completed agent frees a slot. Queue further assignments as needed.
3. Wave A: scout/market definition, demand, technology/supply. Director builds the evidence schema, initial reference classes, and geography coverage.
4. Wave B: institutions, deeper market economics, independent scenario estimates once definitions and baseline data are available. Director merges claims and identifies contradictions.
5. Wave C: skeptical challenge and evidence/numerical audit of the draft. Director resolves only the issues that can change rankings or confidence. No recursive agent spawning by specialists.
6. Wait for all required assignments or record failures. Use bounded waits with progress communication; timeout is not success. Reassign failed critical work once when a different approach can help; otherwise handle locally or qualify the affected result.

For a small scoped update, fewer roles may suffice. If delegation is unavailable, perform explicitly labeled sequential specialist passes and independent tool checks; say that actual multi-agent execution was unavailable. Never invent agents, votes, meetings, or consensus.

## Independence before discussion

For a probability or top ranking, obtain initial specialist estimates before revealing the director's preferred number or conclusion. Give a neutral task, definitions, raw sources, and the information cutoff. Where possible, use fresh contexts without previous conclusions; record shared context or source overlap if isolation is unavailable. Later share counterevidence for one focused revision. Agreement alone must not raise confidence.

Aggregate only predictions with exactly matching events, deadlines, and resolution rules. With no validated track record, an equal-weight mean of initial probabilities is a transparent starting point, not a calibrated ensemble. Show individual estimates, dispersion, and correlation concerns; the director may depart from the mean with an evidence-based explanation. Do not multiply marginal probabilities for dependent milestones or mechanically extremize an ensemble.

## Assignment template

```text
Act as the [specialist role] for this bounded Horizon Forge assignment.
Question: [one decision-relevant research question]
Scope: [segment, geography, metric, endpoints, information cutoff]
Inputs: [raw evidence paths/URLs and common definitions; no preferred answer]
Read: [absolute SKILL.md/reference paths relevant to this assignment]
Investigate: [specific unknowns, including a disconfirmation search]
Deliver to: [unique task-local file path]
Return: conclusions; supporting and contrary claims with original URLs, dates,
units and source lineage; assumptions; estimate/range if defensible; confidence;
material tangents; unresolved questions; and a concise director summary.
Distinguish retrieved evidence from inference. Do not browse beyond the cutoff
for a restricted historical exercise. Do not edit shared ranking/ledger files,
spawn further agents, or perform external writes. Report tool-access limitations.
Stop when this question is answered or further searches cease to change it;
surface blocking gaps instead of filling them with invented facts.
```

Each specialist writes only its own memo and raw evidence extracts. The director alone merges shared artifacts. Source IDs may be namespaced by specialist before deduplication.
