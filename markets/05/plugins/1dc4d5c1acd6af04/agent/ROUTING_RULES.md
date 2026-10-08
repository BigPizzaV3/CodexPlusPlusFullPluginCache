# ROUTING_RULES.md

**Status:** Canonical routing rules  
**Version:** 1.0

## Principle

Route by **decision need**, not by keyword or by words appearing in the user's message. A mention of “BATNA”, “policy”, “hostile” or “offer” does not itself require the matching skill.

Prefer sequential calls where one specialist's result determines what the next needs. Parallel calls are reserved for genuinely independent FULL-mode analyses where duplicate context is justified.

## Depth

### LIGHT
Use for low-stakes, reversible, well-understood cases. Normally 0–1 material questions and 0–2 specialist calls. Do not create explicit persistent state by default.

### STANDARD
Use for material fee/scope/programme/employment/commercial matters, several topics, concession pressure, uncertain authority, meaningful relationship effects or continuing negotiation. Normally invoke only the 2–4 relevant specialists.

### FULL
Use for high consequence, low reversibility, multi-party complexity, pronounced power imbalance, major risk/career/financial exposure, serious impasse or important final agreement. FULL still does not mean “call every skill”.

## Skill routes

| Skill | Invoke when | Do not invoke merely because |
|---|---|---|
| **F01 freeman-preparation** | preparation is materially incomplete; focused/full I FORESAW IT can change strategy | any negotiation exists |
| **F02 ttt-offer-design** | topics, targets, trades, opening/counter/creative package or concession design is needed | price is mentioned |
| **F03 batna-leverage** | fallback, walk-away credibility, dependency or leverage is material | the user says the word BATNA |
| **F04 stakeholder-process** | authority, policy ownership, escalation, sequence, allies or process can change outcome | a manager is mentioned |
| **F05 difficult-conversation** | hostility, defensiveness, misunderstanding or sensitive disagreement is blocking progress | the message sounds slightly firm |
| **F06 roleplay-redteam** | an important strategy/proposal needs rehearsal or independent stress-test | every meeting is upcoming |
| **F07 communication-drafting** | strategy is resolved enough to turn into usable wording | strategic diagnosis is still unsettled |
| **F08 deal-review** | a concrete material agreement is being considered for acceptance | a preliminary idea is floated |

## Common dependency patterns

### Important preparation
`F01 → F02`, then add `F03` and/or `F04` only where BATNA/authority can affect the plan. Use F06 after a candidate strategy exists.

### Fee/salary negotiation
`F01 focused → F03 → F02`; F04 if authority/process is uncertain; F07 after strategy is chosen.

### “Company policy”
`F04` first when the material question is whether the constraint is binding and who can vary it. Add F03 only if alternatives/leverage matter; F05 only if interaction is blocking progress.

### Unilateral concession
`F02` trade/concession check; add F03 when leverage/BATNA determines whether movement is necessary.

### Impasse
`F02 + F03`; use F04 if counterpart/sequence may be wrong; F06 if a revised move needs stress-testing.

### Hostile response
Run an orchestrator strategic check. Use `F05`; add `F07` only when final wording is requested. F06 is rehearsal, not a synonym for difficult-conversation analysis.

### Material offer
`F08` is mandatory before acceptance recommendation. If result is `CONDITIONAL` or `FAIL` and a counter-package is appropriate, route to F02 after review.

## Question filter

Specialists may propose questions. The orchestrator asks only those with material decision impact and respects the default budget:
- LIGHT: 0–1 before useful advice;
- STANDARD: 0–3 per pass;
- FULL: iterative, ordered by impact.

Do not block on a non-critical unknown when supportable provisional advice can be given.

## Parallelism gate

Parallelise only if:
1. tasks are genuinely independent;
2. neither requires the other's output;
3. each can use the same immutable state version;
4. expected decision value outweighs duplicate context/reconciliation cost.

F08 should remain independent of advocacy; do not run it as a “vote” alongside deal-promoting modules and average the answers.
