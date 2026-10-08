# 01_NEGOTIATION_AGENT_ARCHITECTURE.md

**Status:** Approved architecture baseline  
**Version:** 1.0.1  
**Date:** 1 September 2026  
**Authority:** `00_FREEMAN_RESEARCH_BASE.md`  
**Purpose:** Define a stable architecture for a stateful ChatGPT negotiation adviser based primarily on Seth Freeman's methods, without yet writing the individual skill prompts.

---

## 0. Document authority and notation

`00_FREEMAN_RESEARCH_BASE.md` is the authoritative research source. This architecture may operationalise that research but must not silently alter it.

The research classifications are preserved:

- **[FREEMAN]** — attributable to Seth Freeman in the research base.
- **[EXTERNAL]** — independent supporting or qualifying evidence in the research base.
- **[SYNTHESIS]** — a traceable interpretation of the research.
- **[DESIGN]** — an architectural or implementation decision made for the ChatGPT negotiation adviser.

All `[Fxx]` and `[Exx]` citation identifiers in this document refer to the source list in `00_FREEMAN_RESEARCH_BASE.md`. This document does not create new research claims.

The negotiation-case evidence classifications are also preserved:

- **KNOWN** — directly provided or evidenced.
- **SUPPORTED_INFERENCE** — supported by identifiable evidence but not directly confirmed.
- **HYPOTHESIS** — plausible and worth testing.
- **UNKNOWN** — material information not established.

These labels describe the evidence within an individual negotiation. They are separate from `[FREEMAN]`, `[EXTERNAL]`, `[SYNTHESIS]` and `[DESIGN]`, which describe the provenance of the negotiation methodology.

---

# 1. Executive architecture decision

## 1.1 Recommended architecture

**[DESIGN]** Use a **thin stateful orchestrator with one canonical negotiation state and modular, mostly stateless specialist skills**.

```text
User
  │
  ▼
┌─────────────────────────────────────────────┐
│ NEGOTIATION ADVISER / ORCHESTRATOR          │
│                                             │
│ • understands the current request           │
│ • owns canonical negotiation state          │
│ • chooses analysis depth                    │
│ • asks only material questions              │
│ • routes to specialist skills               │
│ • reconciles skill outputs                  │
│ • challenges weak strategy                  │
│ • owns the final recommendation             │
└─────────────────────────────────────────────┘
                │
                │ canonical state snapshot
                ▼
     ┌──────────────────────────────┐
     │ SPECIALIST FREEMAN SKILLS    │
     │                              │
     │ F01 Preparation / I FORESAW  │
     │ F02 TTT / Offer Design       │
     │ F03 BATNA & Leverage         │
     │ F04 Who / Stakeholders       │
     │ F05 Interaction / Process    │
     │ F06 Role-play / Red Team     │
     │ F07 Communication Drafting   │
     │ F08 Deal Review              │
     └──────────────────────────────┘
                │
                │ structured results / proposed patches
                ▼
┌─────────────────────────────────────────────┐
│ STATE RECONCILIATION                         │
│ • evidence check                             │
│ • conflict detection                         │
│ • state update                               │
│ • concession ledger                          │
│ • decision/event log                         │
└─────────────────────────────────────────────┘
```

The specialist skills do **not** own separate persistent memories of the negotiation. They receive a controlled view of the canonical state and return analysis plus proposed state changes.

The orchestrator remains responsible for the advice given to the user.

---

# 2. Architecture alternatives considered

The user asked that multiple plausible approaches be analysed rather than one being chosen silently.

## Approach A — One large negotiation skill

A single large skill would contain I FORESAW IT, TTT, BATNA, stakeholder analysis, role-play, drafting and deal review.

### Advantages

- simplest packaging;
- low routing overhead;
- all context is immediately visible to one skill;
- easy first prototype.

### Disadvantages

- high context consumption on simple negotiations;
- greater risk of framework dumping;
- difficult to test one capability independently;
- difficult to protect independent deal review from earlier advocacy;
- a change to one technique can destabilise unrelated behaviour;
- future addition of other negotiation frameworks would make the prompt increasingly monolithic;
- harder to distinguish Freeman research from later methods.

### Assessment

**[DESIGN] Not recommended.**

It contradicts the research objective of using cognitive aids proportionately rather than forcing a complete checklist onto every negotiation. It also weakens modularity and auditability.

---

## Approach B — Thin orchestrator + canonical state + modular skills

The orchestrator owns the negotiation and calls specialist skills only when their analysis is materially useful.

### Advantages

- preserves one coherent negotiation state;
- limits unnecessary specialist calls;
- supports simple, standard and full-depth analysis;
- skills can be tested independently;
- future negotiation methods can be added behind stable interfaces;
- red-team and deal-review modules can be isolated from persuasion work;
- Freeman's research layer remains separable from `[DESIGN]` implementation;
- well suited to iterative conversations where new offers and facts arrive over time.

### Disadvantages

- requires disciplined state contracts;
- routing mistakes could under-use or over-use specialist skills;
- orchestrator must resolve conflicting specialist advice.

### Assessment

**[DESIGN] Recommended.**

This is the baseline architecture defined by the remainder of this document.

---

## Approach C — Multi-agent negotiation team

A lead agent would delegate to persistent specialist agents: strategist, BATNA analyst, psychologist, stakeholder analyst, red team, deal reviewer and drafter.

### Advantages

- strong conceptual separation;
- potentially useful for exceptionally large negotiations;
- parallel analysis can surface diverse interpretations.

### Disadvantages

- duplicated context;
- high token and invocation cost;
- specialist agents may develop inconsistent versions of the negotiation;
- reconciliation becomes difficult;
- greater risk of unsupported assumptions multiplying across agents;
- disproportionate for ordinary workplace and commercial negotiations;
- harder to maintain a single source of truth.

### Assessment

**[DESIGN] Do not use as the default.**

A future implementation may permit selective parallel specialist analysis for unusually consequential negotiations, but the canonical state and final decision authority must still remain with the orchestrator.

---

# 3. Architectural principles

## AP-01 — The agent owns the negotiation; skills own methods

**[DESIGN]** The orchestrator is the negotiation adviser. A skill is not a separate adviser competing for authority.

This follows the earlier system-level distinction:

```text
Agent = adviser and process owner.
Skill = specialist method available to the adviser.
```

---

## AP-02 — One canonical negotiation state

**[DESIGN]** All modules operate on the same canonical state.

No specialist may silently maintain a conflicting BATNA, stakeholder map, target or concession history.

---

## AP-03 — Snapshot plus event history

**[DESIGN]** Maintain:

1. a concise **current-state snapshot** for efficient reasoning; and
2. an **append-only event/change log** for material state changes.

This gives the agent a compact working memory without losing the reason why a target, assumption or recommendation changed.

---

## AP-04 — Freeman research is immutable at runtime

**[DESIGN]** Negotiation events may update the negotiation state. They may not update the meaning of Freeman's methods.

Any methodology change must occur through research change control in `00_FREEMAN_RESEARCH_BASE.md`.

---

## AP-05 — Proportional reasoning

The research base notes that Freeman's preparation can range from rapid use to extensive preparation and describes I FORESAW IT as a map rather than a script. [F03]

**[DESIGN]** The agent shall select a **LIGHT**, **STANDARD** or **FULL** reasoning depth rather than invoking every specialist on every turn.

---

## AP-06 — Evidence precedes confidence

**[DESIGN]** The agent may reason from incomplete information, but it must not silently convert inference into fact.

Counterpart motives, authority, constraints and BATNAs require evidence labels.

---

## AP-07 — Challenge over compliance

Research requirement R-12 states that the system should challenge strategically poor user proposals.

**[DESIGN]** The orchestrator must be able to say that a proposed email, concession, threat, acceptance or escalation is strategically weak and explain why before helping execute it.

---

## AP-08 — Trade before concession

Freeman's TTT framework and the research synthesis favour searching for cross-topic and within-topic trades before unilateral movement. [F03]

**[DESIGN]** A concession recommendation triggers a trade search unless the issue is immaterial or reciprocity would be counterproductive.

---

## AP-09 — Deal review is independent

Freeman's Measures of Success and Deal Dashboard concepts separate getting to "yes" from deciding whether "yes" is good. [F03][F07][F08]

**[DESIGN]** The architecture therefore separates deal-generation from deal-acceptance review.

---

## AP-10 — Relationship sensitivity is not concession bias

Win Warmly supports strong substantive outcomes combined with relationship awareness. [F01][F02][F03]

**[DESIGN]** The system shall not equate warmth with agreement, accommodation or avoidance of escalation.

---

## AP-11 — Material strategic changes must be surfaced

**[DESIGN]** In STANDARD and FULL negotiations, the agent must not silently change a material strategic judgement. If new evidence materially changes the recommended strategy, BATNA, target, walk-away position, decision-maker/authority assessment, or deal-review outcome, the orchestrator must tell the user what changed and why.

This does not require exposing routine internal state maintenance. The rule applies where the changed judgement could reasonably alter the user's decision or next move.

---

# 4. Agent responsibilities and boundaries

## 4.1 Orchestrator responsibilities

**[DESIGN]** The orchestrator shall:

1. detect whether the user is dealing with a negotiation, disagreement, concession request, conflict, offer, counter-offer or deal decision;
2. identify the current lifecycle stage;
3. assess the required analysis depth;
4. create or retrieve the canonical negotiation state;
5. identify material missing information;
6. decide whether questions are justified;
7. invoke only specialist skills likely to change the recommendation;
8. reconcile outputs against the evidence model;
9. update state and append material changes to the event log;
10. maintain the TTT model where relevant;
11. maintain stakeholder and authority information;
12. maintain BATNA information and its confidence;
13. maintain the concession ledger;
14. identify strategically weak user moves;
15. generate the final advice;
16. decide whether communication drafting is appropriate;
17. trigger independent deal review before recommending acceptance;
18. recognise when the state is too uncertain for a confident recommendation;
19. retain a clear distinction between Freeman material and additional `[DESIGN]` rules.

---

## 4.2 Orchestrator boundaries

**[DESIGN]** The orchestrator shall not:

- invent counterpart motives;
- assume a stated position equals an underlying interest;
- assume the visible contact has decision authority;
- treat an option within an agreement as a BATNA;
- treat a hoped-for future alternative as an actual BATNA;
- silently move a target, walk-away threshold or pre-commitment criterion;
- recommend a concession merely because the counterpart asked;
- call a specialist only because the skill exists;
- expose the user to the whole internal framework when a concise answer is sufficient;
- allow role-play output to directly overwrite state;
- allow drafting output to become evidence;
- allow a deal-review skill to negotiate against its own acceptance criteria;
- attribute `[DESIGN]` mechanisms to Freeman.

---

## 4.3 Specialist-skill boundary

**[DESIGN]** A specialist skill:

- receives a state snapshot or a bounded subset;
- applies one defined method;
- identifies assumptions;
- returns structured findings;
- may propose a state patch;
- may recommend questions;
- may identify warnings;
- may cite the research basis;
- does not directly persist state;
- does not make the final user-facing strategic decision unless explicitly delegated by the orchestrator.

---

# 5. Negotiation lifecycle and state machine

The lifecycle is an AI implementation and is therefore **[DESIGN]**.

The architecture separates the **negotiation lifecycle stage** from the **analysis depth**. A high-stakes negotiation can be at `INTAKE`; a simple negotiation can be at `OFFER_RECEIVED`.

## 5.1 Lifecycle stages

```text
NEW
 │
 ▼
TRIAGE
 │
 ├──────────────► QUICK_ADVICE
 │                    │
 │                    ▼
 │                 ENGAGED
 │
 ▼
PREPARING
 │
 ▼
STRATEGY_READY
 │
 ▼
ENGAGED
 │
 ├──────────────► IMPASSE
 │                    │
 │                    └────► ENGAGED
 │
 ├──────────────► OFFER_RECEIVED
 │                    │
 │                    ▼
 │                DEAL_REVIEW
 │                /    |     \
 │             ACCEPT REJECT COUNTER
 │                │      │      │
 │                ▼      ▼      └────► ENGAGED
 │              CLOSED NO_DEAL
 │
 ├──────────────► PAUSED
 │                    │
 │                    └────► ENGAGED
 │
 └──────────────► NO_DEAL
```

---

## 5.2 Stage definitions

### `NEW`

A negotiation has been detected but no reliable state exists.

### `TRIAGE`

The agent establishes what the negotiation is, what the user is trying to achieve and how much analysis is justified.

### `QUICK_ADVICE`

A temporary state for low-complexity cases where a concise diagnosis and recommendation can be produced without full preparation.

### `PREPARING`

Material I FORESAW IT, TTT, BATNA, evidence or stakeholder preparation is being built.

### `STRATEGY_READY`

The agent has enough information to recommend an initial strategy, recognising that unknowns may remain.

### `ENGAGED`

The user is actively exchanging proposals, messages or meetings with the counterpart.

### `IMPASSE`

Progress has stalled, repeated positions are being exchanged or the current route appears blocked.

### `OFFER_RECEIVED`

A sufficiently concrete offer or proposed agreement exists to be tested.

### `DEAL_REVIEW`

The acceptance gate is running independently of deal advocacy.

### `PAUSED`

Negotiation is temporarily inactive but state should be retained.

### `CLOSED`

The user has accepted or completed an agreement.

### `NO_DEAL`

Negotiation has ended without agreement or the user has deliberately walked away.

---

## 5.3 Stage-transition rules

**[DESIGN]**

- A new message does not automatically advance the lifecycle.
- A lifecycle change must be supported by a material event.
- `DEAL_REVIEW` is mandatory before the orchestrator recommends accepting a material deal.
- `IMPASSE` does not imply failure. It triggers leverage, options, stakeholder, process or BATNA re-analysis.
- `CLOSED` does not mean the deal was good; the final state should retain the deal-review result and any user override.
- A negotiation can return from `OFFER_RECEIVED` or `DEAL_REVIEW` to `ENGAGED` after a counter-offer.

---

# 6. Analysis-depth model

## 6.1 LIGHT mode

**Research basis:** rapid Interests/Facts/Options concept and proportional use of Freeman's methods. [F03]

**[DESIGN]** Use where:
- stakes are low;
- there are few negotiable issues;
- consequences are reversible;
- the user's objective is already clear;
- counterpart authority is not materially uncertain;
- no major concession or acceptance decision is involved.

Typical processing:

```text
Interests
Facts
Options
→ quick strategic check
→ draft/recommendation
```

Specialist invocations: normally 0–2.

---

## 6.2 STANDARD mode

**[DESIGN]** Use where:
- money, scope, programme, employment terms or commercial relationships matter;
- there are several negotiable topics;
- the counterpart is pushing for concessions;
- power/authority is uncertain;
- the user wants preparation for a meeting;
- a material counter-offer has arrived;
- relationship management matters.

Typical processing:

```text
Focused I FORESAW IT
+ TTT
+ BATNA/leverage or Who analysis as relevant
+ optional drafting/role-play
```

Specialist invocations: normally 2–4.

---

## 6.3 FULL mode

**[DESIGN]** Use where:
- consequences are substantial or difficult to reverse;
- the negotiation is multi-party or politically complex;
- there is a pronounced power imbalance;
- major financial, contractual, career or reputational consequences exist;
- the user is preparing an important opening strategy;
- a high-value agreement is near acceptance;
- there is a serious impasse;
- the user explicitly requests full preparation.

Typical processing:

```text
Full relevant I FORESAW IT
+ complete TTT
+ bilateral BATNA/leverage
+ stakeholder/authority map
+ process strategy
+ red-team rehearsal
+ pre-commitment / acceptance criteria
+ deal review when offer arrives
```

Specialist invocations are still selective. `FULL` does not mean "call every skill".

---

## 6.4 Escalation rule

**[DESIGN]** Start with the lightest plausible mode and escalate when additional complexity becomes material.

Do not downgrade analysis simply to save context if the missing analysis could change:
- the user's walk-away decision;
- major risk allocation;
- a material concession;
- the identity of the correct decision-maker;
- the acceptance recommendation.

---

# 7. Canonical negotiation-state schema

The research base contains a provisional state structure. This section stabilises it for architecture purposes.

**[DESIGN]** The state is a **working decision record**, not a transcript.

```yaml
negotiation:
  meta:
    negotiation_id:
    title:
    state_version:
    lifecycle_stage:
    analysis_depth: LIGHT | STANDARD | FULL
    status: active | paused | closed | no_deal
    created_at:
    updated_at:

  objective:
    user_stated_objective:
    strategic_objective:
    desired_outcome:
    success_definition:
    relationship_importance: low | medium | high | unknown
    reversibility: high | medium | low | unknown

  parties:
    user:
      role:
      authority:
      constraints: []
    counterpart:
      organisation:
      visible_contact:
      stated_role:
      authority_status:
        value:
        evidence_status: KNOWN | SUPPORTED_INFERENCE | HYPOTHESIS | UNKNOWN
        evidence_refs: []
    other_parties: []

  evidence_register:
    items:
      - evidence_id:
        proposition:
        evidence_status: KNOWN | SUPPORTED_INFERENCE | HYPOTHESIS | UNKNOWN
        basis:
        source_ref:
        materiality: low | medium | high
        last_reviewed:
    contradictions: []
    unresolved_material_unknowns: []

  positions:
    user_positions: []
    counterpart_positions: []

  interests:
    user:
      - interest:
        priority:
        evidence_status:
        basis:
    counterpart:
      - interest:
        priority:
        evidence_status:
        basis:
    common:
      - interest:
        specificity_test:
        evidence_status:
        basis:

  facts_and_research:
    established_facts: []
    research_questions:
      - question:
        why_it_matters:
        expected_decision_impact:
        status:
        answer:
        evidence_ref:

  options:
    in_agreement:
      - option:
        topics_affected: []
        expected_value_user:
        expected_value_counterpart:
        evidence_status:
    rejected_options: []

  topics_targets_tradeoffs:
    topics:
      - topic_id:
        topic:
        priority:
        current_position_user:
        current_position_counterpart:
        best_target:
          value:
          rationale:
          evidence_status:
        minimum_acceptable:
          value:
          rationale:
          evidence_status:
        opening_position:
        tradeoffs_within_topic: []
        cross_topic_trade_links: []
        status: open | provisionally_agreed | agreed | withdrawn

    cross_topic_tradeoffs:
      - trade_id:
        give:
        receive:
        rationale:
        status:
        risk_notes:

  alternatives:
    user:
      batna:
        description:
        value:
        evidence_status:
        evidence_refs: []
      watna:
        description:
        evidence_status:
      improvements: []
      notional_batna:
        description:
        probability:
        timing:
        cost:
        downside:
        evidence_status:
        status: not_used | provisional | validated_for_decision_support

    counterpart:
      batna:
        description:
        evidence_status:
        evidence_refs: []
      watna:
        description:
        evidence_status:
      constraints: []
      estimated_dependency_on_agreement:
        value:
        evidence_status:

  independent_criteria:
    - criterion:
      relevance:
      likely_counterpart_credibility:
      evidence_ref:
      evidence_status:

  stakeholders:
    - stakeholder_id:
      person_or_role:
      organisation:
      formal_authority:
      practical_influence:
      interests: []
      stance:
      relationship_to_visible_counterpart:
      evidence_status:
      evidence_refs: []
      possible_engagement:
      engagement_risk:

  process:
    current_channel:
    meeting_setting:
    timing_constraints: []
    deadlines: []
    sequence:
      current_step:
      proposed_steps: []
    agenda:
    process_risks: []

  rapport_reactions_responses:
    relationship_state:
    likely_reactions:
      - reaction:
        evidence_status:
        prepared_response:
    interaction_notes: []

  proposals:
    opening_offer:
    least_acceptable_package:
    creative_package:
    current_user_offer:
    current_counterpart_offer:
    proposal_history: []

  concessions:
    ledger:
      - concession_id:
        timestamp:
        party: user | counterpart
        topic:
        from:
        to:
        stated_reason:
        requested_exchange:
        received_exchange:
        conditional: true | false
        reciprocal: true | false | unknown
        strategic_assessment:
        source_event_id:

  precommitment:
    created: true | false
    created_at:
    acceptance_criteria:
      - criterion:
        importance: critical | important | desirable
        threshold:
        evidence_basis:
    disqualifiers: []
    relationship_requirements: []
    fairness_or_independent_criteria_requirements: []
    implementation_risk_limits: []
    later_changes:
      - criterion:
        previous_value:
        new_value:
        new_evidence:
        reason:
        approved_by_user: true | false

  strategy:
    current_strategy:
    strategic_rationale:
    leverage_sources: []
    vulnerabilities: []
    current_priority:
    recommended_next_move:
    moves_to_avoid: []
    confidence:
    assumptions: []

  roleplay:
    last_snapshot_version:
    red_team_findings: []
    accepted_findings: []
    rejected_findings: []

  deal_review:
    status: not_required | required | in_progress | pass | fail | conditional | insufficient_information
    offer_reviewed:
    interest_test:
    batna_test:
    independent_criteria_test:
    hidden_timebomb_test:
    priority_topic_test:
    relationship_test:
    implementation_test:
    precommitment_test:
    conditions: []
    recommendation:
    reviewer_rationale:
    override:
      occurred: true | false
      user_reason:
      new_evidence:
      timestamp:

  history:
    material_events:
      - event_id:
        timestamp:
        type:
        summary:
        source_ref:
        state_changes: []
        rationale:
```

---

## 7.1 State invariants

These must always hold.

### SI-01 — Options are not alternatives

`options.in_agreement` cannot contain BATNAs.

### SI-02 — Counterpart psychology is evidence-labelled

A counterpart interest, motive, constraint or likely reaction cannot exist without an evidence status.

### SI-03 — Material targets have rationale

A `best_target` or `minimum_acceptable` threshold in STANDARD/FULL mode should have a rationale rather than appearing as an unexplained number.

### SI-04 — Concessions are append-only

Past concessions are not deleted if later regretted or reversed.

### SI-05 — Pre-commitment changes are visible

Acceptance criteria cannot be silently overwritten.

### SI-06 — Red-team findings are proposals, not facts

Role-play output remains segregated until reconciled.

### SI-07 — Deal review cannot self-authorise

A failed deal review cannot be changed to `pass` merely because the orchestrator prefers closure.

### SI-08 — Unknown remains unknown

Missing information cannot become `SUPPORTED_INFERENCE` without an identifiable basis.

---

# 8. Specialist skill/module architecture

The names below are architectural working names. Individual prompts are deliberately out of scope.

---

## F01 — Freeman Preparation

**Purpose:** focused or full I FORESAW IT analysis.  
**Research basis:** I FORESAW IT. [F03]

### Owns analysis of

- Interests;
- Factual and Financial Research;
- Options;
- Rapport, Reactions and Responses;
- Empathy and Ethics;
- Setting and Scheduling;
- Alternatives;
- Who;
- Independent Criteria;
- initial Topics, Targets and Tradeoffs capture.

### Does not own

- final deal acceptance;
- final communication wording;
- persistent state;
- red-team role-play.

### Typical invocation

- preparation for a meaningful negotiation;
- material gaps in existing state;
- significant change in negotiation conditions;
- FULL analysis.

---

## F02 — TTT and Offer Design

**Purpose:** convert state into Topics, Targets and Tradeoffs and design packages.  
**Research basis:** TTT and offer preparation. [F03]

### Owns analysis of

- topics;
- priorities;
- ambitious researched targets;
- minimum acceptable thresholds;
- cross-topic trades;
- within-topic trades;
- opening package;
- least acceptable package;
- creative package;
- conditional movement.

### Does not own

- evidence classification;
- independent deal acceptance;
- stakeholder mapping except where needed to explain a trade;
- persistent state.

---

## F03 — BATNA and Leverage

**Purpose:** analyse bilateral alternatives, leverage and possible improvements.  
**Research basis:** Alternatives, weak-position analysis and later Notional BATNA teaching. [F03][F06]

### Owns analysis of

- user BATNA/WATNA;
- counterpart BATNA/WATNA estimates;
- BATNA improvement;
- dependency on agreement;
- sources of leverage identifiable from research-base concepts;
- provisional Notional BATNA analysis.

### Special restriction

Notional BATNA must remain uncertainty-aware and cannot be treated as equivalent to an existing alternative unless later research defines a validated procedure.

---

## F04 — Who, Stakeholders and Process

**Purpose:** identify authority, influence, counterpart selection, allies, sequence and process.  
**Research basis:** Who and Setting/Scheduling. [F03]

### Owns analysis of

- decision-maker;
- visible contact versus authority holder;
- hawks/doves where evidence supports the distinction;
- allies;
- agents;
- coalitions;
- possible escalation paths;
- negotiation sequence;
- meeting/channel/process design.

### Trigger example

Repeated "policy", "I cannot approve this", unexplained delay or multi-party negotiation.

---

## F05 — Interaction and Difficult Conversation

**Purpose:** advise on productive interaction where misunderstanding, tension or power dynamics affect the negotiation.

**Research basis:** Rapport/Reactions/Responses, Exactly! Challenge, Paraphrase–Praise–Probe, common interests, APSO and process principles. [F01][F03][F04][F05]

### Owns analysis of

- accurate paraphrase;
- genuine acknowledgement;
- probing questions;
- common-interest framing;
- response to hostility or defensiveness;
- upward-communication structures where the evidence base is sufficient;
- preparation for difficult reactions.

### Research-gap restriction

Golden Minute, APSO, Exactly! Challenge and some later named tools shall not be encoded as claimed exact Freeman procedures until the research gaps in `00_FREEMAN_RESEARCH_BASE.md §25` are resolved.

---

## F06 — Role-play and Red Team

**Purpose:** independently attack the current strategy from a credible counterpart perspective.  
**Research basis:** Freeman's role-play recommendation under Rapport/Reactions/Responses. [F03]  
**Isolation protocol:** `[DESIGN]`.

### Owns

- counterpart simulation;
- objections;
- exploitation of weak assumptions;
- identification of missing evidence;
- stress-testing of proposals;
- identification of likely reactions.

### Does not own

- canonical state;
- final recommendation;
- deal acceptance;
- automatic creation of new "facts".

---

## F07 — Communication Drafting

**Purpose:** turn an approved strategy into usable communication.

### Research basis

Communication wording is an implementation layer **[DESIGN]**. It should reflect Freeman-derived strategy and interaction principles where relevant, but drafting itself is not claimed as a Freeman method.

### Owns

- email;
- chat message;
- meeting opening;
- call notes;
- agenda wording;
- offer wording;
- response wording.

### Critical restriction

The drafting skill may not change:
- targets;
- BATNA;
- concessions;
- deal-acceptance recommendation;
- evidence status.

If the requested wording would make an unapproved concession or materially change the strategy, it must return a warning rather than silently drafting it.

---

## F08 — Independent Deal Review

**Purpose:** test a proposed agreement independently before the orchestrator recommends acceptance.

**Research basis:** I FORESAW IT offer tests, Measures of Success and Deal Dashboard/pre-commitment. [F03][F07][F08]

### Owns

- interest test;
- BATNA test;
- independent-criteria test;
- hidden "time bomb" review;
- priority-topic review;
- relationship review;
- implementation-risk review;
- comparison with pre-commitment criteria;
- recommendation: `PASS`, `FAIL`, `CONDITIONAL`, or `INSUFFICIENT_INFORMATION`.

### Special restriction

The module must not present the 2026 Deal Dashboard as a scientifically validated predictive score. [F08]

---

# 9. Routing logic

## 9.1 Routing principle

**[DESIGN]** Invoke a specialist when its output has a plausible chance of changing the recommended action, reducing a material uncertainty or protecting against a known failure mode.

Do not invoke a skill merely because a keyword matches.

---

## 9.2 Core routing table

| Situation | Depth | Mandatory analysis | Optional analysis |
|---|---|---|---|
| Simple wording with stable strategy | LIGHT | orchestrator strategy check | F07 |
| Minor concession request | LIGHT/STANDARD | Interests/Facts/Options; concession check | F02, F03 |
| Important negotiation preparation | STANDARD/FULL | F01 + F02 | F03, F04, F06 |
| Salary/fee negotiation with uncertain leverage | STANDARD | F01 + F03 + F02 | F04, F06 |
| "They say it is policy" | STANDARD | F04 | F03, F05 |
| Relationship-sensitive conflict | STANDARD | F01 focused + F05 | F04, F06 |
| Repeated impasse | STANDARD/FULL | F02 + F03 | F04, F06 |
| Major opening offer | STANDARD/FULL | F02 | F03, F06 |
| User plans unilateral concession | STANDARD | F02 trade search | F03 |
| Concrete material offer received | STANDARD/FULL | F08 | F02 for counter-offer |
| User says "just accept it" on material deal | STANDARD/FULL | F08 | none before gate |
| High-stakes negotiation with incomplete preparation | FULL | F01 + F02 + F03 + F04 | F06 |
| Hostile message needs response | LIGHT/STANDARD | strategic check | F05 + F07 |

---

## 9.3 Draft-before-diagnosis rule

Research requirement R-01 requires diagnosis before drafting.

**[DESIGN]** Diagnosis may be very small.

A low-stakes message may require only:

```text
What do we want?
What are they asking?
Does this wording concede anything?
Is there a material unknown?
```

The agent shall not make the user complete a full preparation exercise merely to improve an email.

---

## 9.4 Re-routing after new information

New information may change the route.

Example:

```text
Initial request:
"Can you make this fee email firmer?"
→ LIGHT

New fact:
"They are our largest client and have threatened to retender all work."
→ STANDARD or FULL
→ F03 BATNA/leverage
→ F04 stakeholder/process
→ F05 interaction
```

State is updated rather than recreated.

---

# 10. Question-asking policy

Freeman's preparation method identifies many useful questions. The research base also explicitly requires that the future agent not over-interrogate.

The policy below is **[DESIGN]**.

## 10.1 Materiality test

Ask the user a question only where a plausible answer could materially alter at least one of:

- recommended next move;
- BATNA assessment;
- acceptance threshold;
- target;
- trade;
- stakeholder route;
- timing/process;
- relationship strategy;
- wording of a material proposal;
- decision to accept, reject, pause or escalate.

If the answer would merely make the analysis more complete but would not affect action, do not block on it.

---

## 10.2 Question priority

Questions are prioritised:

### Priority 1 — Decision-blocking

Without the answer, giving strategic advice could be materially wrong.

Examples:
- "What happens if you do not agree?"
- "Is £95k genuinely your minimum, or just the figure you were hoping for?"
- "Can this person actually approve the change?"

### Priority 2 — High-value information

The answer may improve the strategy substantially but the agent can proceed provisionally.

### Priority 3 — Nice-to-know

Do not ask unless the user requests exhaustive preparation.

---

## 10.3 Question budget

**[DESIGN]**

- LIGHT: normally 0–1 questions before advice.
- STANDARD: normally 0–3 material questions per analysis pass.
- FULL: questions may be iterative, but they are asked in priority order rather than as the entire I FORESAW IT checklist.

The user can ask for a full interview/checklist explicitly.

---

## 10.4 Proceed-under-uncertainty rule

If a useful answer can be given without blocking:

```text
Known:
...
Working hypothesis:
...
Unknown that could change the advice:
...
Recommendation on current evidence:
...
```

The agent should not force a clarification merely to make the state look complete.

---

## 10.5 No repeated questions

**[DESIGN]** If the information already exists in the current negotiation state, do not ask again unless:

- the previous answer is stale;
- the user has contradicted it;
- new evidence makes it materially doubtful.

---

# 11. Evidence and uncertainty controls

## 11.1 Evidence object

Every material uncertain proposition should be representable as:

```yaml
proposition:
status: KNOWN | SUPPORTED_INFERENCE | HYPOTHESIS | UNKNOWN
basis:
source_ref:
materiality:
```

---

## 11.2 Evidence promotion rules

**UNKNOWN → HYPOTHESIS**

Allowed when a plausible possibility is identified.

**HYPOTHESIS → SUPPORTED_INFERENCE**

Requires identifiable supporting evidence.

**SUPPORTED_INFERENCE → KNOWN**

Requires direct confirmation or reliable evidence establishing the proposition.

**KNOWN → disputed**

If later evidence conflicts, do not silently retain `KNOWN`. Create a contradiction and reassess.

---

## 11.3 No assumption laundering

The following sequence is prohibited:

```text
User: "I think they may be short of budget."
Agent state: counterpart interest = reduce price [KNOWN]
```

Correct handling:

```text
Hypothesis:
Counterpart may have budget pressure.

Basis:
User impression.

Test:
Ask whether their objection was expressly budget-related or whether another constraint was stated.
```

---

## 11.4 Materiality

**[DESIGN]** Not every sentence needs an evidence tag. Formal evidence tracking is required where an uncertain proposition could affect strategy.

Typical high-materiality items:
- authority;
- BATNA;
- walk-away thresholds;
- counterpart constraints;
- deadlines;
- threatened consequences;
- legal/contractual restrictions;
- promise of future work;
- exclusivity;
- implementation commitments.

---

# 12. State-update rules

## 12.1 State versioning

**[DESIGN]** Every material update increments `state_version`.

A skill is invoked against a specific version.

```text
Input state: v14
Skill output: proposed patch based on v14
Current state before application: v14
→ patch may be reconciled

If current state has become v15:
→ check for conflict before applying
```

This prevents stale specialist analysis from silently overwriting new facts.

---

## 12.2 Material event types

```text
USER_CORRECTION
NEW_FACT
NEW_EVIDENCE
COUNTERPART_MESSAGE
MEETING_OUTCOME
OFFER_MADE
OFFER_RECEIVED
CONCESSION_MADE
CONCESSION_RECEIVED
TARGET_CHANGED
BATNA_CHANGED
STAKEHOLDER_CHANGED
DEADLINE_CHANGED
STRATEGY_CHANGED
DEAL_REVIEWED
USER_OVERRIDE
NEGOTIATION_PAUSED
NEGOTIATION_CLOSED
```

---

## 12.3 Append versus overwrite

### Append

Use history for:
- offers;
- concessions;
- changed targets;
- changed BATNA;
- changed acceptance criteria;
- major strategy changes.

### Overwrite current snapshot

The current snapshot may show only the latest:
- current offer;
- current recommendation;
- current stage;
- current strategy.

The historical event must remain available.

---

## 12.4 Corrections

If the user says an earlier state item was wrong:

1. mark the earlier item as superseded;
2. record the correction event;
3. update dependent reasoning;
4. identify recommendations that are no longer valid.

Do not merely replace the text without consequence analysis.

---

## 12.5 Derived state

**[DESIGN]** Derived judgements such as "counterpart leverage appears high" must be recalculated when underlying evidence changes.

They must not become permanent facts.

---

# 13. Negotiation decision rules

These rules operationalise the research and are primarily **[DESIGN]**.

## DR-01 — Interests before positions

Before treating a demand as non-negotiable, consider the interest it may represent. [F03]

---

## DR-02 — Options before deadlock

Where positions conflict, generate possible agreement terms before assuming the negotiation is zero-sum. [F03]

---

## DR-03 — BATNA before walk-away recommendation

A recommendation to accept or reject a material deal must compare it with realistic alternatives. [F03]

---

## DR-04 — Bilateral alternatives

Power analysis includes the counterpart's alternatives and constraints, with evidence status. [F03]

---

## DR-05 — Search for topics before reducing price/value

When the negotiation appears to be about one issue, search for other negotiable topics. [F03]

---

## DR-06 — Targets require justification

Ambitious targets should be realistic and researched rather than aspirational numbers. [F03]

---

## DR-07 — Prefer conditional movement

Where appropriate:

```text
If you can move on X, we can consider movement on Y.
```

rather than:

```text
We can reduce Y.
```

This implements the TTT trade logic. [F03]

---

## DR-08 — Authority before escalation

Before escalating, identify who has formal and practical authority and the likely relationship cost. [F03]

---

## DR-09 — Understand before challenging

Where conflict is relationship-sensitive or emotionally charged, formulate the counterpart's legitimate case accurately before rebuttal. [F01][F04][F05]

---

## DR-10 — Consequences must be credible

Agreement/disagreement consequence framing must rely on credible consequences rather than fabricated threats. [F03]

---

## DR-11 — Weak BATNA does not end leverage analysis

Search other Freeman-derived sources of influence: information, criteria, Who, sequence, options and BATNA improvements. [F03]

---

## DR-12 — Notional BATNA remains provisional

Do not use a speculative future alternative as though it were an existing option. [F06]

---

## DR-13 — Do not reward aggression automatically

Hostility, urgency or a demand for a concession is an input to analyse, not a reason to concede.

This rule is **[DESIGN]** and is consistent with Win Warmly plus firm substantive negotiation.

---

## DR-14 — Do not create false certainty

Where the evidence supports several plausible interpretations, preserve alternatives and propose a test.

---

## DR-15 — User strategy may be rejected

If the user's requested tactic would materially damage his or her stated interests, the agent should explain the concern before assisting with execution.

---

# 14. Concession and trade management

## 14.1 Concession definition

**[DESIGN]** A concession is any material movement away from a prior position, target or contractual/commercial entitlement in a way that gives value to the counterpart.

It can involve:
- price;
- scope;
- programme;
- liability;
- risk;
- payment;
- access;
- exclusivity;
- resource;
- service level;
- future rights;
- decision control;
- another negotiable topic.

---

## 14.2 Concession gate

Before recommending a material concession, the orchestrator asks internally:

```text
1. Why are we moving?
2. What interest does the movement protect?
3. Is movement necessary now?
4. Can we trade instead?
5. What should we receive?
6. What precedent does this create?
7. Does it cross a target or minimum threshold?
8. Does it weaken future bargaining unnecessarily?
```

---

## 14.3 Conditionality

**[DESIGN]** Where strategically appropriate, the agent should frame concessions conditionally.

A concession ledger distinguishes:

```text
offered
accepted
conditional
reciprocal
unreciprocated
withdrawn
```

---

## 14.4 No accidental concessions in drafting

F07 Communication Drafting must compare proposed wording with the canonical TTT and concession state.

If wording:
- reduces price;
- accepts scope;
- removes a condition;
- acknowledges responsibility;
- changes programme;
- weakens a reservation;
- grants a new right;

the skill must flag the strategic change.

---

## 14.5 Concession pattern detection

**[DESIGN]** The orchestrator should detect:
- repeated one-sided movement;
- shrinking concession intervals;
- reciprocal movement;
- counterpart pocketing of concessions without exchange;
- re-trading of previously agreed topics.

This is behavioural analysis of the negotiation history, not a Freeman-branded formula.

---

# 15. Role-play and red-team isolation

Freeman recommends role-play as preparation. [F03] The isolation protocol below is **[DESIGN]**.

## 15.1 Immutable input snapshot

F06 receives:
- state version;
- strategy;
- proposed offer/message;
- evidence register;
- explicit assumptions.

It may not change those inputs.

---

## 15.2 Red-team stance

The red team should model a **competent plausible counterpart**, not an exaggerated villain.

It should ask:
- where is the user's argument weak?
- what does the user's offer reveal?
- what assumption would the counterpart challenge?
- what additional concession might they seek?
- what alternative explanation of their behaviour exists?
- what evidence would they use?
- where can they exploit ambiguity?
- which user's threat is not credible?
- which proposed trade is unattractive to them?

---

## 15.3 Output contract

```yaml
red_team_result:
  based_on_state_version:
  strongest_counterarguments: []
  weak_assumptions: []
  exploitable_concessions: []
  missing_evidence: []
  likely_reactions:
    - reaction:
      evidence_status:
  recommended_tests: []
  proposed_strategy_changes: []
```

No item is automatically promoted to evidence.

---

## 15.4 Reconciliation

The orchestrator classifies each finding:

```text
ACCEPT — supported and material
TEST — plausible but unconfirmed
REJECT — inconsistent with evidence
DEFER — low materiality
```

Only `ACCEPT` findings can directly modify strategy. `TEST` findings normally become hypotheses or research questions.

---

# 16. Independent deal-acceptance gate

This is one of the strongest separations in the architecture.

## 16.1 Trigger

**[DESIGN]** F08 is mandatory before the orchestrator recommends acceptance where any of the following apply:

- the deal is materially consequential;
- a minimum threshold is involved;
- the agreement creates meaningful future obligations;
- risk/liability is being accepted;
- a concession package is being finalised;
- the negotiation was analysed in FULL mode;
- pre-commitment criteria exist;
- the user asks, "Should I accept this?"

A trivial everyday agreement can remain LIGHT.

---

## 16.2 Independence protocol

F08 receives:

- current canonical state;
- current offer;
- BATNA information;
- independent criteria;
- TTT priorities;
- pre-commitment criteria;
- evidence uncertainties.

**[DESIGN]** It should not receive a prompt saying, "The orchestrator thinks this is a good deal; verify it."

The reviewer is asked to test the deal, not validate the existing strategy.

---

## 16.3 Gate tests

Derived from the research-base offer tests, Measures of Success and pre-commitment concept. [F03][F07][F08]

### A — Interests test

Does the offer materially serve the user's priority interests?

### B — BATNA test

Is the offer better than the realistic alternative, allowing for uncertainty and implementation cost?

### C — Independent-criteria test

Can important terms be defended against credible external standards?

### D — Time-bomb test

Are there hidden obligations, ambiguities, dependencies or risks likely to create later problems?

### E — Priority-topic test

Does the package preserve acceptable outcomes on the most important topics?

### F — Relationship test

Does the agreement leave the required relationship workable?

### G — Implementation test

Can the deal actually be delivered and enforced as understood?

This test is **[DESIGN]**, derived from the research concern with hidden problems and practical success.

### H — Pre-commitment test

Does the deal satisfy the criteria defined before deal momentum took hold?

---

## 16.4 Gate outcomes

```text
PASS
The deal satisfies critical criteria on current evidence.

CONDITIONAL
Potentially acceptable if specified conditions are resolved.

FAIL
One or more critical criteria fail.

INSUFFICIENT_INFORMATION
A material acceptance question cannot be assessed reliably.
```

The architecture deliberately avoids a pseudo-scientific numerical "Freeman score".

---

## 16.5 Override

The user remains the decision-maker.

If the user accepts despite a `FAIL` or unresolved `CONDITIONAL` result:

```yaml
override:
  occurred: true
  previous_gate_result:
  user_reason:
  new_evidence:
  changed_precommitment_criterion:
  timestamp:
```

The agent should not repeatedly lecture the user after the decision. It records the divergence and assists with the consequences.

---

# 17. Skill interface contracts

Stable interfaces allow individual skills to be implemented and tested independently.

## 17.1 Common request envelope

**[DESIGN]**

```yaml
skill_request:
  skill_id:
  request_id:
  negotiation_id:
  state_version:
  lifecycle_stage:
  analysis_depth:
  user_request:
  task:
  state_view:
  evidence_constraints:
  output_budget:
```

`state_view` should contain only the fields needed by the specialist where practical.

---

## 17.2 Common response envelope

```yaml
skill_response:
  skill_id:
  request_id:
  based_on_state_version:

  findings:
    - finding:
      importance:
      research_provenance: FREEMAN | EXTERNAL | SYNTHESIS | DESIGN
      research_refs: []
      evidence_status:
      evidence_refs: []

  proposed_state_patch: []

  questions:
    - question:
      priority: 1 | 2 | 3
      decision_impact:
      blocking: true | false

  recommendations: []

  warnings: []

  conflicts_with_state: []

  deliverable:                       # optional; only for skills that produce a bounded artefact
    kind: draft | talking_points | agenda | roleplay | other
    content:

  confidence:
```

---

## 17.3 State patch restrictions

A specialist may propose:

```text
ADD
UPDATE_WITH_EVIDENCE
SUPERSEDE
FLAG_CONTRADICTION
```

A specialist may not:
- delete history;
- silently change pre-commitment criteria;
- upgrade evidence without basis;
- close the negotiation;
- mark a deal accepted;
- persist directly.

---

## 17.4 Research-provenance field

**[DESIGN]** Specialist outputs should be able to identify whether a recommendation is:

```text
FREEMAN
EXTERNAL
SYNTHESIS
DESIGN
```

This is primarily for development, testing and audit. The final user-facing answer does not need to expose provenance labels on every sentence.

---

# 18. Failure modes and safeguards

## FM-01 — Copywriter mode

**Failure:** user asks for a firm email; agent improves wording without noticing that the message gives away leverage.

**Safeguard:** mandatory proportional strategic check before F07 drafting.

---

## FM-02 — Framework dumping

**Failure:** agent forces I FORESAW IT questions into every negotiation.

**Safeguard:** LIGHT/STANDARD/FULL routing plus question budget.

---

## FM-03 — Assumption laundering

**Failure:** user suspicion becomes an asserted counterpart motive.

**Safeguard:** evidence register and promotion rules.

---

## FM-04 — Price tunnel vision

**Failure:** fee/price becomes the only negotiable variable.

**Safeguard:** F02 must search for additional topics and tradeoffs before material price movement.

---

## FM-05 — BATNA hallucination

**Failure:** a hoped-for alternative is treated as real.

**Safeguard:** BATNA evidence status; separate Notional BATNA field.

---

## FM-06 — Visible-contact bias

**Failure:** agent assumes the person emailing is the decision-maker.

**Safeguard:** authority status plus F04 routing.

---

## FM-07 — Concession amnesia

**Failure:** the agent forgets earlier movement and recommends another concession.

**Safeguard:** append-only concession ledger.

---

## FM-08 — Reciprocity blindness

**Failure:** counterpart takes several concessions without providing value.

**Safeguard:** concession-pattern analysis.

---

## FM-09 — Deal euphoria

**Failure:** movement after a long negotiation is mistaken for a good deal.

**Safeguard:** independent F08 gate and pre-commitment comparison. [F08]

---

## FM-10 — Moving the goalposts

**Failure:** minimum acceptable terms change because the user is invested in closure.

**Safeguard:** logged pre-commitment changes and override history.

---

## FM-11 — Warmth becomes weakness

**Failure:** relationship preservation leads to unnecessary concessions.

**Safeguard:** AP-10 and explicit substantive-interest review.

---

## FM-12 — Aggression mimicry

**Failure:** the agent mirrors a hostile counterpart and escalates needlessly.

**Safeguard:** F05 interaction analysis and Win Warmly principle. [F01][F02]

---

## FM-13 — Red-team contamination

**Failure:** simulated counterpart claims become accepted as facts.

**Safeguard:** immutable snapshot, separate red-team result and reconciliation stage.

---

## FM-14 — Specialist state drift

**Failure:** different modules reason from different BATNAs or targets.

**Safeguard:** one canonical state, versioned requests and proposed patches only.

---

## FM-15 — Stale analysis

**Failure:** advice generated against an earlier state overwrites later information.

**Safeguard:** `state_version` conflict check.

---

## FM-16 — Over-attribution to Freeman

**Failure:** an AI implementation choice is described as Freeman's method.

**Safeguard:** research-provenance field and frozen research authority.

---

## FM-17 — False precision

**Failure:** the system produces arbitrary scores implying scientific validation.

**Safeguard:** qualitative structured gates unless a validated quantitative method is later researched.

---

## FM-18 — Named-tool overclaim

**Failure:** incomplete research on Golden Minute, APSO, Exactly! Challenge or Notional BATNA is encoded as an exact Freeman procedure.

**Safeguard:** research-gap restrictions inherited from `00 §25`.

---

## FM-19 — Premature threat or escalation

**Failure:** agent recommends pressure before checking authority, alternatives, credibility and relationship effects.

**Safeguard:** F03/F04 analysis before material escalation.

---

## FM-20 — Endless analysis

**Failure:** the agent keeps searching for marginally useful information and delays action.

**Safeguard:** value-of-information question policy and proportional analysis depth.

---

# 19. Context and efficiency architecture

Efficiency matters because a stateful negotiation may run over many turns.

This section is **[DESIGN]**.

## 19.1 Keep raw transcript separate from working state

Do not place the entire conversation into every specialist call where a concise state view is sufficient.

Use:

```text
Raw evidence/messages
        ↓
Canonical state
        ↓
Bounded state view
        ↓
Specialist
```

---

## 19.2 Context tiers

### Tier A — Always available to orchestrator

- objective;
- lifecycle;
- current strategy;
- material evidence;
- TTT summary;
- BATNA summary;
- current offer;
- key stakeholders;
- concession summary;
- next move.

### Tier B — Load on demand

- full I FORESAW IT fields;
- detailed evidence;
- complete stakeholder map;
- complete offer history;
- full concession ledger.

### Tier C — Specialist-only historical material

- previous role-play transcripts;
- superseded option sets;
- old drafts;
- detailed low-materiality notes.

---

## 19.3 State compaction

When the history grows:

- do not delete material events;
- maintain a concise current-state summary;
- preserve references to the underlying evidence/event;
- archive superseded low-value reasoning outside the active context where the platform permits.

---

## 19.4 Specialist invocation budget

The orchestrator should prefer:

```text
one well-scoped specialist call
```

over:

```text
several overlapping specialists all analysing the whole negotiation
```

Parallel invocation should be reserved for genuinely independent analyses where the benefit outweighs duplication.

---

# 20. Proposed repository structure

**[DESIGN]**

```text
negotiation-adviser/
│
├── 00_FREEMAN_RESEARCH_BASE.md
├── 01_NEGOTIATION_AGENT_ARCHITECTURE.md
├── 02_NEGOTIATION_BEHAVIOUR_CONTRACT.md
├── 03_DECISION_LOG.md
│
├── schemas/
│   ├── NEGOTIATION_STATE.md
│   ├── SKILL_REQUEST.md
│   ├── SKILL_RESPONSE.md
│   └── DEAL_REVIEW_RESULT.md
│
├── agent/
│   ├── ORCHESTRATOR.md
│   ├── ROUTING_RULES.md
│   └── STATE_UPDATE_RULES.md
│
├── skills/
│   ├── freeman-preparation/
│   │   └── SKILL.md
│   ├── ttt-offer-design/
│   │   └── SKILL.md
│   ├── batna-leverage/
│   │   └── SKILL.md
│   ├── stakeholder-process/
│   │   └── SKILL.md
│   ├── difficult-conversation/
│   │   └── SKILL.md
│   ├── roleplay-redteam/
│   │   └── SKILL.md
│   ├── communication-drafting/
│   │   └── SKILL.md
│   └── deal-review/
│       └── SKILL.md
│
├── tests/
│   ├── ARCHITECTURE_ACCEPTANCE.md
│   ├── ROUTING_SCENARIOS.md
│   ├── STATE_TRANSITION_SCENARIOS.md
│   ├── EVIDENCE_CONTROL_SCENARIOS.md
│   ├── NEGOTIATION_SCENARIOS.md
│   └── ADVERSARIAL_SCENARIOS.md
│
└── research/
    └── future-frameworks/
```

### Research isolation

Any future Voss, Fisher/Ury, behavioural-economics or specialist commercial methodology should enter through `research/future-frameworks/` first.

It must not be inserted directly into a Freeman skill without a recorded architecture decision.

---

# 21. Future-framework extension mechanism

The architecture must allow future negotiation methods without contaminating the Freeman layer.

## 21.1 Extension rule

**[DESIGN]** A new methodology requires:

1. its own research source;
2. explicit provenance;
3. a defined problem it solves better or differently;
4. interface compatibility;
5. conflict analysis against existing Freeman-derived rules;
6. an Architecture Decision Record in `03_DECISION_LOG.md`;
7. tests demonstrating routing and conflict handling.

---

## 21.2 No silent blending

If a future method conflicts with a Freeman-derived strategy, the orchestrator should know which method produced which recommendation.

Possible future state:

```yaml
method_conflict:
  issue: opening_offer_style
  freeman_recommendation:
  other_framework_recommendation:
  conflict:
  orchestrator_resolution:
  reason:
```

This prevents the agent from producing an untraceable hybrid and calling it "Freeman".

---

# 22. Proposed Architecture Decision Records

These decisions should be copied into `03_DECISION_LOG.md` once approved.

## ADR-001 — Thin orchestrator

**Decision:** use a stateful orchestrator rather than one monolithic skill or persistent multi-agent swarm.  
**Status:** recommended.

## ADR-002 — Canonical state ownership

**Decision:** only the orchestrator persists negotiation state.  
**Status:** recommended.

## ADR-003 — Specialist statelessness

**Decision:** specialists operate on versioned state snapshots and return proposed patches.  
**Status:** recommended.

## ADR-004 — Snapshot + append-only material history

**Decision:** use a compact snapshot with a material event log.  
**Status:** recommended.

## ADR-005 — Proportional routing

**Decision:** LIGHT/STANDARD/FULL depth controls specialist invocation.  
**Status:** recommended.

## ADR-006 — Value-of-information question policy

**Decision:** ask only questions capable of materially changing strategy; use question budgets.  
**Status:** recommended.

## ADR-007 — Red-team isolation

**Decision:** role-play cannot write directly to canonical state.  
**Status:** recommended.

## ADR-008 — Independent deal gate

**Decision:** material acceptance recommendations require F08 review.  
**Status:** recommended.

## ADR-009 — No pseudo-scientific negotiation score

**Decision:** use structured qualitative gates unless later research validates quantitative scoring.  
**Status:** recommended.

## ADR-010 — Research provenance

**Decision:** preserve Freeman/External/Synthesis/Design provenance in development artefacts and specialist outputs.  
**Status:** recommended.

---

# 23. Architecture acceptance criteria

The architecture is suitable to proceed to behaviour-contract and skill design only if these tests are satisfied.

## AC-001 — Research authority

A developer can identify `00_FREEMAN_RESEARCH_BASE.md` as the methodology authority and cannot mistake this architecture for new Freeman research.

## AC-002 — Provenance preservation

Every architectural mechanism not established as Freeman's method is identifiable as `[DESIGN]`.

## AC-003 — Single source of negotiation truth

There is one canonical state. No specialist has independent persistent negotiation memory.

## AC-004 — Evidence control

The state can distinguish KNOWN, SUPPORTED_INFERENCE, HYPOTHESIS and UNKNOWN for material claims.

## AC-005 — Semantic separation

The state structurally distinguishes:
- positions;
- interests;
- options;
- alternatives;
- BATNA;
- TTT.

## AC-006 — Target preservation

Material targets and minimum thresholds cannot silently move.

## AC-007 — Stakeholder awareness

Authority, influence and visible counterpart are separately representable.

## AC-008 — Concession memory

The system can show every material concession and whether it received reciprocal value.

## AC-009 — Proportional questioning

A low-stakes negotiation can produce useful advice without the full I FORESAW IT questionnaire.

## AC-010 — Escalation capability

The agent can move from LIGHT to STANDARD/FULL when new facts make the negotiation more consequential.

## AC-011 — Challenge behaviour

The orchestrator can identify that the user's requested move is strategically weak and explain the issue before execution.

## AC-012 — Drafting containment

A drafting skill cannot silently alter strategy or concede value.

## AC-013 — Role-play isolation

Simulated counterpart content cannot become canonical evidence without reconciliation.

## AC-014 — Deal independence

A material deal can fail acceptance review even after successful negotiation movement.

## AC-015 — Pre-commitment integrity

Changes to acceptance criteria remain traceable.

## AC-016 — State continuity

A new offer can update an existing negotiation without restarting the analysis.

## AC-017 — Stale-output protection

A specialist result generated from an outdated state version cannot silently overwrite a newer state.

## AC-018 — Token/context efficiency

A simple negotiation does not require loading or invoking all specialist skills.

## AC-019 — Future-method isolation

A new negotiation framework can be added without modifying the Freeman research base or silently changing Freeman skills.

## AC-020 — Research-gap restraint

Named Freeman tools with incomplete primary-source capture are not implemented as falsely exact procedures.

## AC-021 — No false scoring

Deal acceptance is not represented by an arbitrary precision score.

## AC-022 — Independent testing

Each specialist can be tested against a fixed input state and expected structured output without running the entire agent.

## AC-023 — Material strategic changes are visible

In STANDARD/FULL mode, a material change to strategy, BATNA, targets, walk-away position, authority assessment or deal-review outcome is surfaced to the user with the reason for the change.

---

# 24. Example end-to-end flows

These examples test the architecture, not the eventual prompt wording.

## 24.1 Simple fee-reduction email

User:

> They want another £2,000 reduction. Can you draft a reply?

Routing:

```text
TRIAGE → LIGHT
orchestrator:
  identify objective
  check current fee position
  check whether reduction is a concession
  search for trade
F02 only if useful
F07 draft
```

The agent should not launch a full I FORESAW IT interview.

If the state shows the user already made two fee concessions without reciprocal value, the orchestrator should flag this before drafting.

---

## 24.2 Salary negotiation

User:

> My employer is moving me to another employment arrangement and we now need to agree the salary conversion basis.

Routing:

```text
TRIAGE → STANDARD
F01 focused preparation
F03 BATNA/leverage
F02 TTT
F04 if decision authority/process is unclear
F06 optional rehearsal
```

Potential TTT topics might extend beyond the apparent single issue of exchange rate if evidence shows other negotiable terms.

---

## 24.3 Counterpart says "company policy"

Routing:

```text
ENGAGED → STANDARD
F04:
  Is it a real constraint?
  Who owns the policy?
  Who can approve an exception?
  What is the cost of escalation?
F03:
  alternatives / leverage if material
```

"Policy" remains KNOWN only as a statement made by the counterpart unless documentary evidence confirms its binding effect.

---

## 24.4 Major offer arrives

Routing:

```text
OFFER_RECEIVED
→ F08 DEAL REVIEW

if PASS:
  orchestrator may recommend acceptance

if CONDITIONAL:
  F02 may create counter-package

if FAIL:
  orchestrator must not recommend acceptance
  unless user later overrides after being told the failed criteria
```

---

## 24.5 User insists on a strategically weak email

User:

> Just tell them we can cut the fee by 10% to get this sorted.

State shows:
- no reciprocal concession requested;
- user's BATNA is acceptable;
- fee has already moved;
- programme/scope are still tradeable.

The orchestrator should respond conceptually:

```text
This would be a further unilateral concession and would weaken the position
without testing whether they can trade on scope/programme/payment.
I would not send that as written.

Recommended move:
conditional trade.

If the user still wants the original approach after understanding the risk:
assist, but record the concession.
```

This demonstrates adviser behaviour rather than blind compliance.

---

# 25. Approved architecture decisions

The following decisions were approved by the user on 1 September 2026 and form part of the frozen architecture baseline.

## UAD-01 — Persistence model

### Option A — Conversation/project memory only

Simpler, but long negotiations may suffer state loss or compression.

### Option B — Explicit state artefact/file

Maintain a structured negotiation-state file per material negotiation.

### Option C — Hybrid

Use conversational state for LIGHT cases and an explicit state artefact for STANDARD/FULL negotiations.

**Decision: APPROVED — Option C.**

It keeps small negotiations frictionless and gives important negotiations durable state.

---

## UAD-02 — Visibility of negotiation state

### Option A — State mostly internal

Cleaner user experience, but less auditable.

### Option B — Show full state continuously

Highly auditable, but burdensome.

### Option C — Internal working state with user-requestable or milestone summaries

**Decision: APPROVED — Option C.**

The agent can surface:
- current objective;
- key assumptions;
- TTT;
- BATNA;
- concessions;
- recommended next move

when useful, without printing the entire schema every turn.

---

## UAD-03 — Deal gate strictness

### Option A — Advisory only

The agent may still recommend acceptance after a failed review.

### Option B — Hard recommendation gate

The agent cannot recommend acceptance when the review is `FAIL`; the user can override.

### Option C — Hard action gate

The system refuses to help the user execute acceptance after `FAIL`.

**Decision: APPROVED — Option B.**

This preserves strong advice without taking the decision away from the user.

---

## UAD-04 — Specialist parallelism

### Option A — Sequential by default

Lower context duplication and easier state control.

### Option B — Parallel specialists routinely

Potential breadth but higher cost and reconciliation complexity.

### Option C — Sequential default; parallel only for deliberately independent FULL-mode analysis

**Decision: APPROVED — Option C.**

---

## UAD-05 — High-stakes trigger

### Option A — Fixed monetary threshold

Easy but inappropriate across different users and negotiation types.

### Option B — User declares stakes

Simple but can miss risk.

### Option C — Consequence-based triage

Assess materiality, reversibility, relationship, complexity, risk and user concern.

**Decision: APPROVED — Option C.**

Avoid false precision.

---

## UAD-06 — Notional BATNA automation

### Option A — Include it now as an ordinary BATNA method

Risk of overclaiming and optimism bias.

### Option B — Exclude until primary procedure is fully researched

Safest but loses potentially useful concept.

### Option C — Permit as explicitly provisional decision support with mandatory uncertainty fields

**Decision: APPROVED — Option C**, subject to the research limitation already recorded in `00 §17.2` and `§25`.

---

## UAD-07 — Named Freeman tools with research gaps

Golden Minute, APSO, Exactly! Challenge, Common Interest Hack and some later tools still require deeper primary-source capture.

### Option A — implement from secondary descriptions now;
### Option B — omit completely;
### Option C — retain general principle but defer claims of exact procedure.

**Decision: APPROVED — Option C.**

---

# 26. Recommended next design step

Once this architecture is approved, create:

`02_NEGOTIATION_BEHAVIOUR_CONTRACT.md`

That document should define how the orchestrator behaves towards the user, including:

- when it challenges;
- how it asks questions;
- how direct it should be;
- how it handles uncertainty;
- how it avoids becoming merely agreeable;
- how it handles user overrides;
- how much internal framework it exposes;
- how it communicates risks;
- how it distinguishes strategic advice from drafting.

Only after the behaviour contract and unresolved architecture decisions are approved should the individual `SKILL.md` files be written.

---

# 27. Traceability to the research base

| Architecture area | Research-base foundation |
|---|---|
| Win Warmly / relationship-aware firmness | `00 §2`, [F01][F02][F03] |
| Cognitive aids rather than scripts | `00 §3`, [F01][F02][F03] |
| LIGHT Interests/Facts/Options | `00 §4` |
| I FORESAW IT preparation | `00 §5`, [F03] |
| Options vs alternatives | `00 §5.3`, [F03] |
| Reactions and role-play | `00 §5.4`, `§10`, [F03] |
| Perspective-taking | `00 §5.5`, [F03][E01][E02] |
| Process/timing | `00 §5.6`, [F03] |
| BATNA/WATNA | `00 §5.7`, `§17`, [F03][F06] |
| Who/stakeholders/authority | `00 §5.8`, `§9`, [F03] |
| Independent criteria | `00 §5.9`, [F03] |
| Topics, Targets and Tradeoffs | `00 §5.10`, `§6`, [F03] |
| Trade rather than concede | `00 §7` |
| Weak positions/leverage | `00 §8`, [F01][F02][F03] |
| Exactly!/PPP/difficult interaction | `00 §12–13`, [F01][F04][F05] |
| Common interests | `00 §14`, [F03] |
| APSO | `00 §15`, [F01] with research limitation |
| Consequence framing | `00 §16`, [F03] |
| Notional BATNA | `00 §17.2`, [F06] with research limitation |
| Deal review | `00 §18`, [F03][F07] |
| Pre-commitment / Deal Dashboard | `00 §19`, [F08] |
| Do not over-attribute AI design to Freeman | `00 §21` |
| Behaviour requirements R-01–R-22 | `00 §22` |
| Initial state concept | `00 §23` |
| Behaviour-contract seed | `00 §24` |
| Research gaps | `00 §25` |

---

# 28. Architecture conclusion

**[DESIGN]** The recommended system is deliberately **not** a "Seth Freeman chatbot".

It is a stateful negotiation adviser whose core operating methods are grounded in the Freeman research base.

Its most important structural characteristics are:

1. one canonical negotiation state;
2. a thin orchestrator that owns judgement;
3. modular specialist skills that do not own separate memories;
4. proportional LIGHT/STANDARD/FULL reasoning;
5. explicit evidence and uncertainty controls;
6. persistent TTT, BATNA, stakeholder and concession state;
7. role-play isolated from factual state;
8. independent deal acceptance review;
9. traceable pre-commitment changes;
10. strict separation between Freeman research and later `[DESIGN]` choices.

This architecture should make the eventual agent capable of handling a quick workplace email without ceremony, yet capable of expanding into a disciplined negotiation adviser when the consequences justify it.

It also creates stable interfaces against which individual skills can later be developed and tested independently.

---

## Change control

Changes to this architecture should be recorded in `03_DECISION_LOG.md` once that file exists.

Any proposed change affecting Freeman's methodology must first be checked against `00_FREEMAN_RESEARCH_BASE.md`.

Any proposed architectural change should state:

```text
Decision:
Current architecture:
Proposed change:
Reason:
Research impact:
State/interface impact:
Skill impact:
Test impact:
Decision:
```
