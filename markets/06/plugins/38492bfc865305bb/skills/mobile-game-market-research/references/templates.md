# Research Templates and Schemas

Use only the sections justified by the research level. Follow the receiving project's metadata and file-naming conventions.

These are content schemas. For an authorized durable research deliverable, assemble
the relevant content into one complete HTML report using
[html-report.md](html-report.md). Markdown examples may serve as internal authoring
inputs; they do not require separate reader-facing files. Include report ID,
version, updated date, evidence cutoff, scope and approval status in the report.

## Research brief

```markdown
# [Direction] Market Research Brief

Owner:
Date:
Entry route: Evaluate a proposal / Discover new concepts
Research level: Scan / Exploration / Investment
Status:

## Research question
## Decision to make
## Market scope
- Platform:
- Geography:
- Business model:
- Genre / subgenre:
- Defining mechanic or player need:
- Target audience:
- Time window:

## Studio mandate and constraints
- Business objective and definition of success:
- Available team / skills / allocation:
- Test budget and timebox:
- Production budget and horizon:
- UA / distribution and LiveOps capacity:
- Hard exclusions:
- Unknowns and provisional assumptions:
- Research stopping rule:
- Decision owner and commitment being considered:

## Inclusion criteria
## Exclusion criteria
## Key questions
## Initial hypotheses
## Success criteria for this gate
## Known risks
- Market:
- Product:
- UA:
- Production:
- Business:

## Available and missing sources
```

## Canonical competitor record

### Identity and research role

- Game, developer, publisher, release date, platforms, markets
- Genre, subgenre, business model
- Research group: Direct / Mechanic / Audience / Business / Weak or failed
- Relevance to each linked study

### Performance snapshot

- Snapshot date, source, methodology
- Platform, countries, date window, granularity
- Downloads and revenue for comparable current, medium, and lifetime windows when available
- Growth or decline over comparable periods
- Revenue/download only as a rough proxy when appropriate
- Main countries and concentration
- Update, season, ranking, or UA context

### Product deconstruction

- Positioning, USP, audience, fantasy
- Core, session, and meta loops
- Controls, skill, strategy, build depth, RNG
- Progression and collection
- Economy and monetization
- Social, competition, and LiveOps
- Content structure and scalability
- UX and onboarding
- Production complexity
- Strengths, weaknesses, unresolved questions

For notable features, add: `Feature -> player need -> product role -> business role -> evidence that it works`.

## Player-feedback record

| Field | Purpose |
|---|---|
| Game | Canonical name |
| Source and link | Traceability |
| Date | Recency |
| Market / language | Sampling context |
| Sentiment | Positive / Neutral / Negative |
| Journey stage | Install / Early / Mid / Late / Churn / Payer |
| Topic | Normalized theme |
| Statement summary | Preserve meaning without unnecessary quotation |
| Interpretation | Need or friction indicated |
| Confidence | Strength and representativeness |

## UA creative record

| Field | Purpose |
|---|---|
| Game and platform | Context |
| Date observed | Recency |
| Creative URL or ID | Traceability |
| First 3 seconds | Hook |
| Fantasy | Promise sold |
| Mechanic shown | Player action |
| Problem -> action -> payoff | Structure |
| Emotional trigger | Motivation |
| Authenticity | Real / Hybrid / Misleading / Unknown |
| Longevity or scale signal | Performance evidence, if any |
| Notes | Variants and product mismatch |

## Opportunity record

```markdown
### Opportunity

Target player and need:
Evidence of demand:
Existing solutions:
Gap and why it persists:
Proposed product space, not yet a fixed concept:
Player-visible differentiation:
UA, retention, and monetization logic:
Execution fit:
Counter-evidence:
Risks and assumptions:
Confidence:
Cheapest next validation:
```

## Opportunity scorecard

Use this sequence; do not combine attractiveness and execution into one automatic investment score.

### 1. Feasibility screen

| Constraint | Required limit | Current evidence | Pass / Fail / Unknown | Consequence |
|---|---|---|---|---|
| Team / technical capability | | | | |
| Test cost / time | | | | |
| Production cost / time | | | | |
| Content / LiveOps / distribution | | | | |

A failed hard constraint blocks the proposed scope. Re-scope explicitly and re-evaluate; an Unknown calls for the smallest resolving action, not an assumed Pass.

### 2. Separate comparison panels

| External attractiveness | Execution feasibility |
|---|---|
| Player demand | Confirmed team capability and availability |
| Sustainable momentum / accessible audience | Prototype cost and learning speed |
| Competitive access / substitution | Production affordability and schedule |
| Player-visible differentiation | Content and operational throughput |
| Distribution / creative potential | UA and distribution capacity |
| Repeat-engagement logic | Technical and delivery risk |
| Monetization / value exchange | Strategic fit and opportunity cost |

Use 1-5 only when useful, with claim-specific rationale, source, confidence, and reversal assumption. Anchor 1 = adverse evidence or major mismatch, 3 = plausible but materially mixed, 5 = strong relevant support with manageable counter-evidence; 2 and 4 interpolate. Define more specific anchors before scoring a study. Missing evidence is **Unknown**, never an automatic 3.

Optional weights must be chosen for the study's objective before comparing outcomes and sum to 100 within each panel. Do not merge the two panels. Do not publish a complete-looking total for partial data or impute unknowns; show coverage. Test whether modest weight/assumption changes reorder the shortlist; unstable rankings should be presented as ties or uncertain.

### 3. Test priority

Prioritize high decision impact, high uncertainty, low test cost/time, and useful learning across multiple concepts. Do not infer that the most attractive market is the first experiment to run.

## Decision memo

- Question, entry route, research level, and date:
- Recommendation and exact commitment requested:
- Strongest supporting evidence:
- Strongest counter-evidence:
- Feasibility screen and unknowns:
- Selected concept(s), alternatives rejected, and why:
- Reversal assumptions and confidence by claim:
- Next test, owner, cost/time cap, and decision enabled:
- Owner approval: Pending / Approved / Declined; date and scope:
- Revisit trigger:

## Product thesis

```markdown
We believe [target players]
want [player need or outcome]
because [market and player evidence].

Current games solve this through [existing solutions]
but under-serve [evidenced gap].

The proposed product can differentiate through [player-visible proposition]
and reach the audience through [credible UA or distribution logic].

This thesis depends on [key assumptions].
We will test it with [experiments and thresholds].
```

## Validation plan

| Assumption | Risk if false | Evidence today | Experiment / target sample | Metric / threshold basis | Pass / Fail / Inconclusive | Cost / time cap | Decision enabled |
|---|---|---|---|---|---|---|---|

Prioritize assumptions by decision impact and uncertainty. Test the cheapest high-impact uncertainty first.

## Working-state handoff

```markdown
Goal:
Completed:
Confirmed decisions:
Current findings and confidence:
Artifacts changed:
Open issues / blockers:
Next step:
```

Use the Concept Card and shortlist schema in concept-development.md and the complete experiment specification in validation-playbook.md when those outputs are required.

