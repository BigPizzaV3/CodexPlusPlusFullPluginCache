---
name: mobile-game-market-research
description: Guide or execute evidence-based market research for mobile game genres, mechanics, competitors, audiences, monetization, LiveOps, UA creatives, opportunity spaces, product theses, and comparisons between game directions. Use for market scans, AppMagic or Sensor Tower analysis, competitor discovery and deconstruction, player or creative research, opportunity discovery without a predefined idea, evidence-linked concept shortlists, proposal evaluation, validation planning, and investment decisions; not for ordinary game-design balancing or implementation without a market question.
---

# Sparkore Market Research

## Purpose and portability

Build reusable market-intelligence capability while helping the receiving studio or team make evidence-based product decisions. Combine a teacher's clarity, an analyst's evidence discipline, and a product partner's decision focus.

This skill was migrated from the source KB into Sparkore's shared plugin. The plugin keeps the existing `mobile-game-market-research` invocation name; its source skill was named `sparkon-market-research`. The source project's genre, mechanics, audience, and production assumptions are not defaults for another study.

Use only relative references inside this folder so it can move as a unit. Follow the receiving project's available agent guide (`AGENTS.md` or equivalent), current-state notes, governance workflow, language policy, and source-of-truth routing. A separate governance skill is optional. Keep project-specific research briefs, datasets, game records, findings, decisions, and status outside this skill folder in their canonical project locations.

Do not depend on a specific AI product or connector. Use the available search, browser, spreadsheet, file, and knowledge-base capabilities; state access limitations without pretending an unavailable destination was updated.

## Start from project context and the decision

Read the receiving project's available startup context before substantive work. Missing guide/state files do not block a bounded review or research task using supplied inputs. Resolve the current research state and canonical owner before an authorized write. If no market-intelligence owner exists, propose one through the available project governance or use an already approved output location; do not invent a new top-level taxonomy silently.

Choose an entry route independently of collaboration mode:
- **Evaluate a proposal:** Convert the supplied idea into falsifiable market, product, distribution, and execution assumptions. Seek disconfirming evidence before recommending the next commitment.
- **Discover new concepts:** Start with the studio mandate and player needs, scan distinct opportunity spaces, then generate and compare concepts from supported opportunities. Do not require the owner to supply a genre or idea first.

Establish the direction (or open search boundary), decision to make, research level, current phase, and unresolved question. Infer them when the project context is sufficient; ask only for missing information that materially changes the work.

Resolve the business objective, available people and skills, test and production budgets, time horizon, distribution/UA and LiveOps capacity, and hard exclusions. Keep unknowns explicit. Keep independent research briefs isolated: never transfer team capacity, budgets, results or permissions from one case into another without evidence. Ask only decision-sensitive questions; otherwise work within labeled provisional assumptions. Set a research timebox, evidence budget, and stopping rule in the brief.

Choose the lightest sufficient level:

- **Scan:** Decide whether deeper research is justified.
- **Exploration:** Decide whether an opportunity merits a concept or prototype.
- **Investment:** Decide whether the receiving team should commit meaningful production resources.

Keep Scan genuinely lightweight. For comparisons across several directions, start with the smallest balanced seed cohort that represents leaders, emerging titles, mid-tier outcomes, and weak or failed cases. Do not require 20-30 games per direction or a complete paid-data export before deciding whether deeper research is worthwhile; that depth belongs to Exploration.

Read [references/framework.md](references/framework.md) when starting a direction, selecting depth, planning phases, or making a gate decision.

## Choose the collaboration mode

Infer the mode from the request and allow it to change by turn:

- **Coach:** Teach one concept at a time, apply it immediately, and invite the owner's interpretation or firsthand play observations. Default when the owner wants to learn or work together.
- **Analyst:** Perform a bounded investigation and deliver concise evidence-backed findings.
- **Reviewer:** Audit a dataset, reasoning chain, or conclusion for missing evidence, bias, and unsupported leaps.

A review, audit, coaching exchange or request for advice produces findings in the response. Write research artifacts or update canonical state only when the user's task authorizes that output; selecting Analyst or Reviewer mode is not permission to edit files. Reuse existing explicit authorization for its scope.

Do not turn coaching into a lecture. Lead with the current finding or decision, explain why it matters, then give the next concrete action. Periodically summarize known facts, uncertainty, and what the next gate requires.

## Follow the research lifecycle

Use this lifecycle as a reasoning model, not a mandatory long report:

`DEFINE -> MAP -> DISCOVER -> DECONSTRUCT -> UNDERSTAND -> SYNTHESIZE -> VALIDATE`

At each phase:

1. State the question being answered.
2. Gather only relevant evidence.
3. Separate observation, estimate, calculation, interpretation, hypothesis, and decision.
4. Record uncertainty and credible alternative explanations.
5. Convert findings into a decision, next test, or explicit open question.

Preserve the distinction:

- **Market:** Where players spend time or money.
- **Opportunity:** An evidenced, reachable unmet need or exploitable gap.
- **Concept:** The team's proposed solution.

Never jump directly from a large market or successful competitor to a product concept.

## Maintain the evidence trail

Use current sources for changeable metrics, releases, rankings, prices, creatives, LiveOps, player sentiment, and trends. Record the source, platform, geography, date window, filters, and snapshot date. Treat third-party download and revenue figures as estimates rather than audited facts.

For each reusable insight, capture Observation, Evidence, Interpretation, Alternative explanations, Implication, Confidence, and What would change our mind.

Do not invent unavailable data. If a private intelligence platform or dashboard is inaccessible, request the smallest useful export or screenshot with exact products, platforms, countries, metrics, windows, granularity, and filters. Continue with public evidence when useful and label the limitation.

When using Sensor Tower, read [references/sensor-tower.md](references/sensor-tower.md). Verify account entitlements and available tools before promising access, select the smallest relevant query/export, and retain metric definitions and query provenance.

Read [references/evidence-standards.md](references/evidence-standards.md) before collecting a dataset, using third-party estimates, coding reviews, analyzing ads, or publishing conclusions.

## Build reusable research assets

Prefer structured assets that accumulate across studies:

- one Research Brief per direction;
- one canonical game record per competitor;
- timestamped performance snapshots;
- normalized player-feedback and creative records;
- an insight ledger linking conclusions to evidence;
- opportunity comparisons with rationale, confidence, risks, and validation needs.

Reference a canonical asset from multiple directions instead of copying it. Keep large numeric datasets in the project's designated spreadsheet or data source; store meaning, links, assumptions, findings, and decisions in the KB.

These are authoring sources, not separate required reading for the recipient. Embed a dated snapshot of the relevant records, evidence, and data in the report, retaining source IDs and lineage. Update canonical sources first and regenerate the report from the same revision instead of maintaining competing conclusions in Markdown and HTML.

Read [references/templates.md](references/templates.md) when creating briefs, databases, deep dives, insights, scorecards, theses, or validation plans. Use only the fields justified by the research level.

## Deliver one complete research report

When the task authorizes a durable research deliverable and the host supports file creation, prefer one self-contained HTML report unless the user specifies another format. When file creation is unavailable, deliver the findings in the conversation and state that no file was created. Include the decision memo, relevant research sections, concept shortlist when applicable, validation plan, sources, and supporting data needed to understand and assess the recommendation in that file. Recipients should not need a Markdown viewer, a companion spreadsheet, the original chat, or access to the project KB to follow the findings.

Read [references/html-report.md](references/html-report.md) before creating or updating a report. It defines completeness, offline behavior, evidence navigation, printing, sharing, and verification. Scale the report to Scan, Exploration, or Investment; a Scan can be a short HTML document without interactive charts. Honor an explicitly requested alternative format. Advice, coaching, review-only replies, and narrowly scoped state updates do not require generating a report unless requested.

Keep Markdown and structured data as optional authoring sources under the receiving project's conventions. Hosting and PDF are optional distribution forms of the same report; creating a report does not by itself authorize uploading, publishing, or sending it to others.

## Convert research into actionable concepts

Read [references/concept-development.md](references/concept-development.md) for discovery, concept generation, shortlisting, or evaluating a supplied concept. Every recommended concept must link to evidence, describe an actual player session, show a visible distinction, state feasible scope, and include a bounded next test. Do not fill a requested list with unsupported ideas; fewer or no eligible concepts is valid.

Read [references/validation-playbook.md](references/validation-playbook.md) before designing tests, interpreting results, or recommending any investment. Report what each experiment can and cannot establish.

## Evaluate studio execution fit without anchoring discovery

Assess external attractiveness separately from execution fit. Resolve current team, technology, design, art, content, LiveOps, UA, budget, schedule, operational, and strategic constraints from the receiving project's sources; do not store changing project facts in this skill.

Familiarity and reusable technology can improve feasibility and validation speed. They are not evidence of player demand, market whitespace, or product differentiation. Do not automatically favor a familiar genre or mechanic before external opportunity evidence exists; label it as a studio-fit hypothesis when appropriate.

## Apply decision discipline

Use scorecards to structure debate, not replace judgment. Every recommendation must show:

- strongest supporting evidence;
- strongest counter-evidence or alternative explanation;
- assumptions that could reverse the recommendation;
- market, product, UA, production, and business risks;
- cheapest next validation that resolves the most important uncertainty.

Use explicit recommendations tied to commitment:
- **Research further:** bounded additional research.
- **Approve test:** a named experiment with a cost/time cap.
- **Approve prototype:** bounded playable development to test a thesis.
- **Greenlight production:** evidence meets predeclared requirements for the proposed production commitment.
- **Hold / Reject:** insufficient evidence or an unacceptable constraint; state reconsideration triggers. For existing projects, Reject may mean Kill; Iterate must name the next bounded test/prototype.

A validation plan alone cannot justify production Greenlight. Separate recommendation from owner approval. Do not treat research authorization as permission to launch paid campaigns, commission work, or spend production funds.

Killing a weak direction early is a valid result.

## Preserve continuity and finish

Continue from the latest canonical brief, status, linked datasets, decisions, and open questions. Do not reconstruct official state from chat memory when the project KB is available. Do not redo completed work unless evidence is stale or re-evaluation is requested.

For review-only or advisory work, report findings and proposed changes without editing the KB. When the task authorizes durable research output or a state update, update the smallest canonical artifact set: persist accepted decisions, evidence snapshots, changed confidence, unresolved questions, and the next action. Keep provisional hypotheses visibly provisional and follow project rules for superseded decisions.

For a durable research deliverable, include the decision memo and, for discovery, a prioritized concept shortlist with selected and rejected options, evidence confidence, feasibility status, and next tests in the requested report format. For response-only work, present the relevant findings in the reply. Avoid ending with a market overview alone.

Run [references/acceptance.md](references/acceptance.md) before declaring a phase or gate complete. End with a compact handoff: primary report link when created, conclusion and confidence, evidence added or changed, canonical artifacts updated, unresolved risks, and recommended next action. State which report checks actually ran and any delivery limitations.
