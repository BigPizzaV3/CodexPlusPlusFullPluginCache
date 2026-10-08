# 00_FREEMAN_RESEARCH_BASE.md

**Status:** Canonical research source for the Freeman-based Negotiation Adviser  
**Version:** 1.0  
**Date:** 1 September 2026  
**Purpose:** Preserve the researched basis of Seth Freeman's negotiation methods before agent architecture, prompts or specialist skills are designed.

---

## 0. Authority and use of this document

This file is the **research authority**, not the agent specification.

Later architecture, prompts and skills may:
- operationalise the material here;
- simplify it for execution;
- add other negotiation frameworks;
- add AI-specific controls.

They must **not silently rewrite Freeman's teaching** to fit an implementation.

Every material proposition in this document is classified as one of:

- **[FREEMAN]** — directly attributable to Seth Freeman through his own published material, teaching material, interview, or institutional description of his method.
- **[EXTERNAL]** — independent negotiation or behavioural research that supports, qualifies or challenges a related idea.
- **[DESIGN]** — an AI-agent design decision proposed for the future system. This is not presented as Freeman's own teaching.
- **[SYNTHESIS]** — an interpretation that combines Freeman material into a coherent model. It must remain traceable to the underlying sources.

### Evidence confidence for future agent use

The eventual agent should separately label negotiation-case information as:

- **KNOWN** — directly provided or evidenced.
- **SUPPORTED INFERENCE** — a conclusion with identifiable evidence, but not directly confirmed.
- **HYPOTHESIS** — plausible and worth testing.
- **UNKNOWN** — material information not yet established.

**[DESIGN]** This evidence model is an AI safeguard. It is not a Freeman framework.

---

# 1. Scope

This research base covers Freeman's negotiation philosophy and the tools most relevant to a reusable ChatGPT negotiation adviser:

1. Win Warmly
2. Interests / Facts / Options
3. I FORESAW IT
4. Topics, Targets and Tradeoffs (TTT)
5. Role-play and preparation for reactions
6. Power, leverage and weak-position negotiation
7. Who / stakeholder and coalition analysis
8. Targeted negotiation
9. Golden Minute / process management
10. Exactly! Challenge
11. Paraphrase–Praise–Probe
12. Common interests
13. APSO
14. Agreement / disagreement consequence framing
15. BATNA and Notional BATNA
16. Measures of Success
17. Deal Dashboard and structured pre-commitment
18. Updating the negotiation plan as new evidence appears

This document does **not** claim that every concept originated with Freeman. BATNA, interest-based negotiation, objective criteria, integrative bargaining and perspective-taking have broader histories. Freeman's contribution is often in the form of **memorable, low-cognitive-load tools for applying negotiation principles under pressure**.

---

# 2. Freeman's overall negotiation philosophy

## 2.1 Win Warmly

**[FREEMAN]** Freeman repeatedly describes the objective of his tools as helping a negotiator to **"win warmly"**: do well for oneself whilst caring about the other person. His official book page frames the methods as usable under stress, adversity and power imbalance, rather than as a theory applicable only to cooperative negotiations. [F01][F02]

This produces a two-dimensional objective:

- protect and advance substantive interests;
- avoid avoidable damage to the relationship, dignity or future cooperation.

**[SYNTHESIS]** Win Warmly should not be interpreted as "split the difference", "always collaborate" or "preserve harmony at any price". Freeman's own material includes ambitious targets, walk-away positions, BATNA analysis, leverage analysis, persuasion based on the cost of saying no, and preparation for difficult resistance. [F03]

**Agent implication [DESIGN]:** the future system should be capable of recommending firmness, refusal, escalation, changed counterpart, better alternatives or walking away where those moves protect the user's interests. The tone should remain proportionate and relationship-aware.

---

# 3. Cognitive aids rather than scripts

**[FREEMAN]** A recurring feature of Freeman's work is the use of mnemonics, one-page play cards, checklists and repeatable tools to reduce cognitive burden. His book materials expressly describe phrases, mnemonics and "glance-and-go" play sheets designed to remain usable when the negotiator is stressed. [F01][F02]

**[FREEMAN]** I FORESAW IT is described as a **map, not a script**. Freeman states that negotiation is too dynamic for a predetermined script and that the preparation tool should help the negotiator understand the terrain and steer towards the objective as events unfold. [F03]

**[DESIGN]** This is a central architectural requirement. The ChatGPT system should:
- maintain a live negotiation model;
- prepare moves and contingencies;
- avoid pretending it can predict the counterpart's exact response;
- update its plan when new information arrives.

---

# 4. Rapid diagnosis: Interests, Facts, Options

**[FREEMAN/SYNTHESIS]** Freeman's larger preparation method repeatedly returns to three basic thinking tasks:

### Interests
What does each side actually care about, beneath its stated demand?

### Facts
What information would materially change the negotiation: documents, financial data, market evidence, history, authority, organisational structure, law, policy, precedent or technical information?

### Options
What possible terms or arrangements might satisfy the interests? Freeman encourages deliberate creativity before premature criticism. In I FORESAW IT he asks negotiators to generate multiple options for each topic. [F03]

**[DESIGN]** This trio can provide a **lightweight mode** for low-stakes negotiations. A full I FORESAW IT analysis should not be forced onto every short email or minor disagreement.

---

# 5. I FORESAW IT — Freeman's principal preparation framework

The primary source is Freeman's own paper and planning form, *I FORESAW IT: A Way to Improve Your Preparations for Negotiating*, copyright 1996 and updated through 2018. [F03]

Freeman describes it as a mnemonic covering factors a negotiator should consider before talks. It may be used relatively quickly, but he notes that important negotiations can warrant hours, days or weeks of preparation. [F03]

## 5.1 I — Interests

**[FREEMAN]** Identify:
- the negotiator's interests;
- the other person's interests;
- common interests.

The emphasis is on the underlying reasons for demands rather than demands themselves. Freeman advises ranking interests and considering intangible concerns as well as material ones. For significant organisational negotiations, interests may need to be mapped separately for individual players. [F03]

**Agent implication [DESIGN]:**
- distinguish **position** from **interest**;
- do not convert guessed motives into facts;
- seek evidence for counterpart interests;
- identify common interests that are specific enough to be operationally useful.

---

## 5.2 F — Factual and Financial Research

**[FREEMAN]** Freeman treats knowledge as a source of negotiating strength. His examples include:
- market prices;
- relevant documents;
- expert or industry information;
- published information;
- relationship history;
- cultural norms;
- legal constraints;
- financial analysis;
- the other organisation's structure. [F03]

**Agent implication [DESIGN]:** identify research questions explicitly rather than filling knowledge gaps with assumptions.

A future state object should be able to store:

```text
Research question:
Why it matters:
Current evidence:
Source:
Confidence:
Action to resolve:
```

---

## 5.3 O — Options

**[FREEMAN]** Brainstorm possible negotiable solutions and terms without immediately judging them. Freeman's planning paper recommends generating multiple possibilities for each topic before narrowing the field. He distinguishes these negotiated **options** from **alternatives to agreement**. [F03]

This distinction is fundamental:

- **Option:** a possible term inside an agreement.
- **Alternative:** what a party can do if no agreement is reached.

**Agent implication [DESIGN]:** the future system must never use "option" and "BATNA" interchangeably.

---

## 5.4 R — Rapport, Reactions and Responses

**[FREEMAN]** Prepare the tone of the conversation and anticipate difficult things the other side may say. Freeman recommends considering responses and, for important negotiations, role-playing with another person. [F03]

The aim is not to create a word-for-word dialogue. The aim is to make difficult reactions less surprising and to prepare constructive responses.

**Agent implication [DESIGN]:**
- generate credible objections;
- stress-test the user's proposal;
- rehearse responses;
- avoid cartoonishly aggressive role-play unless the evidence supports it.

---

## 5.5 E — Empathy and Ethics

**[FREEMAN]** Freeman asks the negotiator to put himself or herself in the other person's position, including attempting to describe the situation in the counterpart's internal voice. His framework also explicitly raises ethical dilemmas and boundaries. [F03]

**[EXTERNAL]** Galinsky, Maddux, Gilin and White (2008) found across three studies that **perspective-taking** improved negotiators' ability to discover hidden agreements and to create and claim resources. Emotional empathy did not show the same bargaining advantage and sometimes reduced individual profit. [E01][E02]

**Research qualification:** Freeman uses the language of empathy broadly. The external evidence suggests a useful distinction between:
- cognitive perspective-taking; and
- emotional empathy.

**Agent implication [DESIGN]:** the system should seek to understand how the situation looks from the other side without automatically prioritising the other side's welfare over the user's legitimate interests.

---

## 5.6 S — Setting and Scheduling

**[FREEMAN]** Freeman asks negotiators to consider:
- where the negotiation occurs;
- medium: face-to-face, telephone, email or other;
- public or private setting;
- timing;
- deadlines;
- sequence of meetings;
- possible discussion rules;
- whether allies should be approached before others. [F03]

**SYNTHESIS:** this makes process design part of negotiation rather than treating the conversation as a fixed event.

**Agent implication [DESIGN]:** before optimising wording, the system may need to question whether the proposed timing, channel or meeting sequence is strategically sensible.

---

## 5.7 A — Alternatives to Agreement

**[FREEMAN]** Freeman asks each side what it will do if there is no deal. He recommends:
- generating several alternatives;
- ranking them;
- identifying best and worst alternatives;
- improving them with research and creativity;
- analysing the other party's alternatives;
- using alternatives to understand leverage. [F03]

His planning form expressly refers to BATNA and WATNA. [F03]

**Agent implication [DESIGN]:** BATNA analysis must be bilateral. A strong user BATNA matters, but so does the counterpart's dependency on agreement.

The system should distinguish:
- existing BATNA;
- possible BATNA improvements;
- WATNA/downside;
- counterpart BATNA estimate;
- confidence in each estimate.

---

## 5.8 W — Who

**[FREEMAN]** Freeman's "Who" analysis extends beyond the person sitting opposite. It asks:
- who can influence the outcome;
- whether another person would be better to negotiate with;
- who holds more discretion;
- who each negotiator answers to;
- who the hawks and doves are;
- whether agents or mediators should be involved;
- who the likely allies are;
- whether coalitions can be formed or need to be blocked;
- which other stakeholders could affect or contribute resources to the negotiation. [F03]

**Agent implication [DESIGN]:** do not assume the visible counterpart equals the decision-maker.

A stakeholder entry should eventually include:

```text
Person / role:
Formal authority:
Practical influence:
Likely interests:
Relationship to counterpart:
Likely stance:
Evidence/confidence:
Possible engagement:
```

---

## 5.9 I — Independent Criteria

**[FREEMAN]** Freeman asks for objective or external standards that the other side is likely to regard as credible. His examples include market values, appraisals, industry standards, precedents, contract terms and fair procedures. [F03]

This allows a proposal to be grounded in something other than the negotiator's own assertion that it is fair.

**Agent implication [DESIGN]:** for commercial and technical negotiations, independent criteria should be treated as a core form of leverage.

Potential categories include:
- market benchmarks;
- signed contracts;
- technical standards;
- documented precedent;
- programme evidence;
- cost evidence;
- policy;
- statutory requirements;
- independent expert evidence.

---

## 5.10 T — Topics, Targets and Tradeoffs

This is where Freeman turns broad preparation into a compact operational negotiation plan. [F03]

### Topics

**[FREEMAN]** List what will be negotiated. Look beyond the obvious issue for hidden or additional negotiable topics. [F03]

### Targets

**[FREEMAN]** For each topic, establish:
- the best realistically achievable target;
- the least acceptable / walk-away target.

Freeman says the best target should be ambitious but realistic and grounded in research. The lower target should relate to the value of the best alternative to agreement. [F03]

### Tradeoffs

Freeman distinguishes:

**Tradeoffs between topics**  
Rank topics by importance and exchange movement on lower-priority matters for gains on higher-priority matters.

**Tradeoffs within a topic**  
Find alternative ways of satisfying the underlying interest on that topic. [F03]

---

# 6. The TTT Grid as a live negotiation play card

Freeman's TTT structure is:

| Topic | Targets | Tradeoffs between topics | Tradeoffs within topic |
|---|---|---|---|

The 2018 I FORESAW IT source shows the grid directly and explains how it can be used to prepare proposals. [F03]

Freeman recommends preparing, at minimum:

1. an **opening offer**, based on strong targets with a reasonable cushion for concessions;
2. a **least acceptable offer**;
3. at least one **creative proposal** for use if the negotiation stalls. [F03]

He cautions against treating those prepared agreements as the only possible acceptable outcomes. They define a useful negotiating field, not a rigid script. [F03]

## 6.1 Offer testing

The same planning document gives tests for proposed agreements. The substance of the tests is:

- do they satisfy the interests identified;
- are they at least as good as the best alternative;
- can they be defended using independent criteria;
- do they contain future "time bombs";
- do they preserve good outcomes on priority topics;
- how is the other side likely to react? [F03]

**Agent implication [DESIGN]:** these tests should become machine-readable validation rules rather than advisory prose buried in a prompt.

---

# 7. Trade rather than concede

**[SYNTHESIS]** Freeman's TTT structure naturally favours **conditional movement** and cross-topic exchange over isolated concession.

A weak negotiating pattern is:

> "They pushed back on the fee, so reduce the fee."

A TTT analysis asks:

- What do they value?
- What do we value?
- What does movement cost each side?
- Can price be exchanged against scope, programme, payment timing, liability, access, volume, future work, decision speed or another term?

**Agent rule [DESIGN]:** before recommending a unilateral concession, search for:
1. a reciprocal concession;
2. a cross-topic trade;
3. a within-topic alternative;
4. a change to process or decision-maker;
5. a BATNA improvement.

A unilateral concession may still be rational, but it should be recognised as such.

---

# 8. Weak positions and hidden power

**[FREEMAN]** Freeman explicitly addresses situations in which the other side appears much more powerful. His official book material uses the image of a "Godzilla" counterpart and presents the tools as aids for negotiating under pressure and adversity. [F01][F02]

**[FREEMAN]** In the I FORESAW IT material he argues that a weak BATNA does not exhaust the sources of negotiating power. Careful work on other parts of the framework may reveal:
- hidden topics;
- new options;
- persuasive independent criteria;
- stakeholders;
- allies;
- alternative counterpart representatives;
- sequencing advantages;
- improved alternatives. [F03]

**Agent implication [DESIGN]:** never reduce power analysis to "who needs the deal more?" alone.

The system should assess at least:

```text
Alternatives
Information
Time/deadlines
Authority
Stakeholder support
Coalitions
Objective criteria
Counterpart constraints
Implementation dependency
Switching cost
Reputational exposure
Process control
Ability to create value
Ability to delay
Ability to escalate
```

This extended list is **[DESIGN]**; it draws on Freeman's broad logic but is not represented as his formal taxonomy.

---

# 9. Targeted negotiation / negotiating with the right person

**[FREEMAN]** Freeman's "Who" work asks whether someone else would be a better person to deal with and notes that people at different organisational levels may have very different discretion. [F03]

His broader teaching uses targeted negotiation and stakeholder analysis to avoid treating the currently visible counterpart as the only route to agreement. [F01]

**Agent implication [DESIGN]:** when a negotiation repeatedly stalls on "policy", "authority" or "I cannot approve that", investigate:
- whether the stated constraint is real;
- who owns the constraint;
- who can grant an exception;
- whether escalation is constructive or damaging;
- whether an ally should engage that person instead.

---

# 10. Role-play and red-team preparation

**[FREEMAN]** Role-play appears directly in Freeman's preparation work under Rapport, Reactions and Responses. It is intended to uncover surprises and build readiness for resistance. [F03]

**Agent implication [DESIGN]:** role-play should be separated from strategy generation.

A useful AI sequence is:

```text
1. Build current strategy.
2. Freeze it temporarily.
3. Assume the role of a competent counterpart.
4. Attack weak assumptions and exploit poorly protected interests.
5. Return to adviser role.
6. Revise the strategy where the red-team case is credible.
```

This prevents "role-play" from becoming theatrical reassurance.

---

# 11. Golden Minute and negotiation process

**[FREEMAN]** Freeman's recent teaching and book discussions include a "Golden Minute" technique intended to improve the opening/process of difficult negotiations and reduce tension. It is referenced in discussions of his 15 Tools work. [F01][F09]

**Research note:** the available primary online material examined for this file does not provide the same level of detailed canonical wording for the Golden Minute as the I FORESAW IT paper provides for that framework.

**Authority level:** retain the concept, but **do not hard-code a detailed procedure as "Freeman's exact Golden Minute"** until the relevant primary text is captured.

**Agent implication [DESIGN]:** the general process principle is safe to adopt: important negotiations may benefit from an explicit opening agreement about purpose, agenda, tone or discussion process.

---

# 12. Exactly! Challenge

**[FREEMAN]** Freeman's broader 15 Tools teaching includes an "Exactly!" challenge: understand and state the other person's position well enough that they recognise it as an accurate account before attempting to persuade them. [F01]

**SYNTHESIS:** this is stronger than waiting for one's turn to argue. It uses accurate understanding as a precondition for productive disagreement.

**Agent implication [DESIGN]:** in contentious exchanges, first prepare a neutral statement of the counterpart's strongest legitimate concern. Do not use this mechanically when the issue is straightforward.

---

# 13. Paraphrase – Praise – Probe

Columbia SIPA describes Freeman teaching a three-part method for disagreement:

1. **Paraphrase** — listen actively and restate the person's position;
2. **Praise** — identify something genuine and non-trivial that can be affirmed;
3. **Probe** — ask a question to understand further or gently challenge. [F04][F05]

**[FREEMAN]** The purpose is to bring curiosity and courage into difficult dialogue without unnecessarily escalating it. [F04]

**Important implementation qualification [DESIGN]:**
- do not manufacture praise;
- do not praise harmful conduct merely to complete a formula;
- do not use the sequence on every email;
- use it where misunderstanding, defensiveness or identity threat is blocking progress.

**[EXTERNAL]** Perspective-taking research provides independent support for the value of understanding the counterpart's thinking in negotiation. [E01][E02]

---

# 14. Common interests

**[FREEMAN/SYNTHESIS]** Freeman's preparation tool explicitly asks negotiators to identify common interests: shared needs the parties may satisfy together. [F03]

A useful common interest must be more specific than a platitude.

Weak:
> We all want a successful outcome.

Useful:
> Neither party benefits from a redesign after construction starts, so resolving the interfaces before release protects the client's programme and prevents the consultant carrying uncontrolled design risk.

**Agent implication [DESIGN]:** reject vague "common ground" statements unless they can influence a decision or proposal.

---

# 15. APSO and upward negotiation

Freeman's 15 Tools framework includes **APSO**, commonly presented as a compact structure for raising a difficult issue, particularly where the listener has greater authority:

- **A — Attention**
- **P — Problem**
- **S — Solution**
- **O — OK? / seek permission or agreement to proceed**

**[FREEMAN]** This tool belongs to the "during the negotiation" group in Freeman's broader practical system. [F01]

**Research note:** the primary online excerpts inspected here establish the existence and intended practical use of APSO but do not provide a full canonical specification comparable with the 2018 I FORESAW IT paper.

**Agent implication [DESIGN]:** use APSO as a candidate structure for concise upward-management communication, subject to later verification from the full primary book text.

---

# 16. Agreement and disagreement consequence framing

**[FREEMAN/SYNTHESIS]** Freeman's preparation material explicitly encourages the negotiator to consider how saying **yes** serves the counterpart's interests and how saying **no** may expose the counterpart to poorer alternatives. [F03]

This permits consequence-based persuasion without turning every negotiation into a threat.

**Agent implementation [DESIGN]:**

Prefer:
> If we can agree the scope now, we can retain the current delivery team and protect the programme. If it moves into the following month, those resources may need to be reassigned.

Avoid:
> Agree today or you'll lose the team.

The factual consequence may be similar; the first framing is more informative, credible and relationship-preserving.

---

# 17. BATNA and Notional BATNA

## 17.1 Conventional BATNA in Freeman's method

**[FREEMAN]** I FORESAW IT expressly requires analysis of alternatives for each side, including the best and worst alternatives, and recommends improving alternatives through research and creativity. [F03]

## 17.2 Notional BATNA

**[FREEMAN]** Freeman's later teaching introduces the idea of a **Notional BATNA** for cases where today's observable alternative is weak or effectively absent, but a credible better alternative may arise within a realistic near-future period. He describes estimating that future possibility systematically rather than concluding that a negotiator with no current BATNA should accept virtually any offer. [F06]

**Critical qualification [DESIGN]:** a Notional BATNA is vulnerable to wishful thinking.

The agent must not treat:
> "I could probably find a better client/job/supplier later"

as equivalent to an actual alternative.

A future assessment should include:
- probability;
- expected timing;
- switching/search cost;
- uncertainty;
- downside if the alternative fails;
- evidence supporting the estimate.

---

# 18. Measures of Success — agreement is not the objective

**[FREEMAN]** Freeman explicitly rejects the idea that "yes" automatically means success. In an interview discussing his framework, he describes using a Measures of Success dashboard to test whether an offer:
- serves key interests without hidden "time bombs";
- is favourable or at least better than the alternative;
- is fair;
- leaves the relationships in a sound condition. [F07]

This is consistent with the offer-testing questions embedded in the I FORESAW IT planning material. [F03]

**Agent implication [DESIGN]:** acceptance review must be logically separate from the negotiation-generation process.

The agent should be able to say:

> The negotiation produced movement, but the current deal is still worse than your acceptance criteria.

---

# 19. 2026 Deal Dashboard — structured pre-commitment

In May 2026 Freeman published the working paper:

*Deal Dashboard™: A Structured Pre-Commitment Instrument for Negotiation Preparation and Offer Assessment*. [F08]

## 19.1 Core idea

**[FREEMAN]** The paper proposes a structured instrument allowing deal teams, boards and advisers to establish relevant criteria before becoming committed to a transaction and to assess an offer systematically before accepting it. It explicitly connects the approach with behavioural decision risks and with the use of structured instruments in other high-stakes fields. [F08]

**[SYNTHESIS]** For an AI system, the important principle is **pre-commitment**:

> Define what a good deal looks like before negotiation momentum creates pressure to redefine success.

## 19.2 Evidence status and limitation

This source must be handled carefully.

- It is a **2026 SSRN working paper**.
- It proposes an instrument and theoretical/practical rationale.
- It should not be represented as a universally validated predictive algorithm.
- Freeman discloses a commercial relationship to the Deal Dashboard instrument in the paper materials.

**Agent implication [DESIGN]:** use the Deal Dashboard concept as disciplined decision support, not as scientific proof that an offer should be accepted or rejected.

---

# 20. Independent evidence relevant to the Freeman-based system

## 20.1 Perspective-taking

Galinsky et al. (2008), *Psychological Science*, examined perspective-taking and empathy in negotiation. Across three studies, perspective-taking increased the ability to discover hidden agreements and to create and claim value; emotional empathy did not produce the same result and could sometimes be disadvantageous. [E01][E02]

**Relevance:** supports the future agent's emphasis on modelling the counterpart's viewpoint, priorities and likely reasoning.

**Limit:** this does not empirically validate the entirety of Freeman's framework.

---

## 20.2 Ambitious targets

Negotiation research has repeatedly examined the value of ambitious targets. Freeman himself has written on the "goal-setting paradox": high negotiation goals can improve objective outcomes whilst producing less subjective satisfaction. [E03]

**Relevance:** supports using ambitious but researched targets rather than merely choosing a comfortable desired figure.

**Agent implication [DESIGN]:** after a good negotiated result, do not interpret user disappointment alone as evidence that the strategy failed. Compare the result to benchmarks and pre-agreed targets.

---

# 21. What must NOT be attributed to Freeman

The following are proposed implementation choices for the ChatGPT system and should remain labelled **[DESIGN]**:

1. `KNOWN / SUPPORTED INFERENCE / HYPOTHESIS / UNKNOWN` evidence tags.
2. A machine-readable negotiation-state object.
3. Mandatory confidence scoring for counterpart motives.
4. Automatic routing between lightweight and full analysis.
5. A dedicated red-team sub-skill.
6. A formal concession ledger.
7. An override log when the user accepts a deal against prior criteria.
8. Rules controlling when the agent may ask questions.
9. An agent architecture composed of an orchestrator and modular skills.
10. Any future integration of Voss, Fisher/Ury, behavioural economics, game theory, procurement, contract or sector-specific negotiation.

These may be consistent with Freeman's principles, but they are **our architecture**, not his.

---

# 22. Research-derived requirements for the future agent

The following requirements are **[DESIGN]**, derived from the research above.

### R-01 — Diagnose before drafting
If a user asks for negotiation wording, the agent should perform at least a proportionate diagnosis before writing.

### R-02 — Do not over-interrogate
Do not force the user through every I FORESAW IT field. Ask a question only if the likely answer can materially change the strategy.

### R-03 — Separate fact from speculation
Counterpart motives, authority, BATNA and constraints must be labelled according to evidence confidence.

### R-04 — Separate positions from interests
A demand is not automatically an interest.

### R-05 — Separate options from alternatives
Do not confuse possible deal terms with BATNA.

### R-06 — Search for additional topics
Before bargaining only over the obvious issue, look for other negotiable variables.

### R-07 — Set targets deliberately
For material topics, establish an ambitious researched target and a lower acceptance boundary where practicable.

### R-08 — Analyse bilateral alternatives
Assess the user's and counterpart's BATNA/WATNA, with explicit uncertainty.

### R-09 — Search for leverage before surrendering value
Consider information, criteria, stakeholders, authority, sequence, options and BATNA improvements before recommending compromise.

### R-10 — Prefer trades over concessions
Movement should normally seek reciprocal value.

### R-11 — Track concessions
Record what moved, by how much, why and what was received in return.

### R-12 — Challenge strategically poor user proposals
The system is an adviser, not a stylistic compliance engine.

### R-13 — Preserve relationships intelligently
Avoid unnecessary hostility or humiliation, particularly where future cooperation matters.

### R-14 — Do not confuse warmth with weakness
Walking away, escalating or refusing can remain consistent with Win Warmly.

### R-15 — Rehearse serious negotiations
Use role-play/red-team analysis for important negotiations or where the user requests it.

### R-16 — Understand before challenging
For contentious interactions, accurately formulate the counterpart's legitimate case before proposing rebuttal.

### R-17 — Use objective criteria
Where credible external standards exist, integrate them into proposals and persuasion.

### R-18 — Treat process as negotiable
Venue, timing, agenda, sequence and participant choice may materially affect the outcome.

### R-19 — Update the plan
After each new offer, meeting or material fact, update rather than restart the negotiation model. Freeman expressly advises keeping detailed notes and revising the plan after negotiation sessions. [F03]

### R-20 — Independent deal gate
Do not recommend agreement solely because the counterpart has moved.

### R-21 — Pre-commitment for high-stakes deals
Capture acceptance criteria before the user becomes invested in closing the transaction.

### R-22 — Record justified overrides
If new evidence justifies changing a prior walk-away or acceptance criterion, record the reason rather than silently moving the goalposts.

---

# 23. Proposed canonical negotiation state

This is **[DESIGN]** and is included here only to preserve the research-to-architecture bridge.

```yaml
negotiation:
  objective:
  stage:
  stakes:
  relationship_importance:

  interests:
    user: []
    counterpart: []
    common: []

  evidence:
    known: []
    supported_inferences: []
    hypotheses: []
    unknowns: []

  research_questions: []

  topics:
    - topic:
      priority:
      best_target:
      walkaway_target:
      within_topic_options: []

  tradeoffs_between_topics: []

  alternatives:
    user:
      batna:
      watna:
      improvements: []
      notional_batna:
    counterpart:
      batna:
      watna:
      confidence:

  stakeholders: []

  independent_criteria: []

  process:
    channel:
    timing:
    sequence:
    agenda:
    decision_authority:

  reactions_and_responses: []

  concessions:
    made: []
    received: []

  proposals:
    opening:
    least_acceptable:
    creative: []

  precommitment:
    acceptance_criteria: []
    disqualifiers: []

  current_strategy:
  recommended_next_move:
```

This is **not** final architecture. It should be revised in `01_NEGOTIATION_AGENT_ARCHITECTURE.md`.

---

# 24. Proposed agent behaviour contract extracted from the research

Also **[DESIGN]**, subject to later formalisation.

The eventual agent should:

- seek the user's interests rather than merely polishing the user's stated position;
- challenge unsupported assumptions;
- identify material unknowns;
- distinguish fact, inference and hypothesis;
- avoid inventing counterpart motives;
- search for additional negotiable topics;
- identify targets and acceptance boundaries;
- analyse BATNAs on each side;
- look for leverage before recommending a concession;
- prefer trades to unilateral movement;
- identify the real decision-maker;
- use independent criteria;
- prepare for reactions;
- use role-play when the stakes justify it;
- listen and accurately paraphrase before challenging contentious positions;
- use common interests only where they are substantive;
- preserve dignity and working relationships where compatible with the user's legitimate interests;
- recommend "no" where the deal fails the acceptance test;
- reassess strategy when new evidence appears;
- resist deal euphoria and escalation of commitment;
- make the user aware when a proposed move would weaken his or her position unnecessarily.

---

# 25. Research gaps to resolve before implementation freeze

The following items need deeper primary-source capture before they are encoded as exact Freeman procedures:

1. **Golden Minute** — exact steps and conditions of use.
2. **Exactly! Challenge** — exact Freeman formulation and any associated sequence.
3. **APSO** — full primary specification and examples.
4. **Common Interest Hack** — exact tests Freeman applies to a useful common interest.
5. **Targeted Negotiation / Who I FORESAW** — full tool specification beyond the core "Who" material in I FORESAW IT.
6. **Win Warmly Card / 5% Experience Rule** — verify exact form and intended use from primary text.
7. **Notional BATNA** — capture complete calculation/decision procedure rather than rely on interview-level explanation.
8. **Measures of Success / Yes-No Compass** — capture the complete primary dashboard from the book.
9. **Deal Dashboard 2026** — review the whole working paper before formalising a machine decision rule.
10. **15-tool taxonomy** — freeze exact names, order and relationships from the published book.

These gaps do **not** prevent architecture work. They do prevent us from claiming exact fidelity to a detailed tool we have not yet captured in full.

---

# 26. Source hierarchy

For later design work, use sources in this order:

### Tier 1 — Primary Freeman sources
Freeman's own published papers, book extracts, forms, templates and working papers.

### Tier 2 — Institutional Freeman descriptions
NYU Stern and Columbia pages describing his teaching and methods.

### Tier 3 — Freeman interviews
Useful for explanation and later-developed concepts where the primary text is not yet captured.

### Tier 4 — Independent peer-reviewed research
Used to support, qualify or challenge underlying negotiation mechanisms.

### Tier 5 — Secondary summaries
Use only where better sources are unavailable. Do not use them to override a primary source.

---

# 27. Sources

## Primary / Freeman

**[F01] Seth Freeman — 15 Tools to Turn the Tide, official page**  
Professor Freeman website.  
https://professorfreeman.com/15tools/  
Used for: Win Warmly, tool philosophy, cognitive aids, negotiation under adversity, preparation-to-decision scope.

**[F02] NYU Stern — 15 Tools to Turn the Tide: A Step-by-Step Playbook for Empowered Negotiating**  
https://www.stern.nyu.edu/experience-stern/faculty-research/15-tools-turn-tide-step-step-playbook-empowered-negotiating  
Used for: institutional corroboration of the tool-based approach, play-card concept and Win Warmly.

**[F03] Seth Freeman — I FORESAW IT: A Way to Improve Your Preparations for Negotiating, 2018 edition**  
https://professorfreeman.com/wp-content/uploads/2019/01/I-FORESAW-IT-2018-Edition-Really.pdf  
Used for: canonical I FORESAW IT framework, TTT, targets, alternatives, Who, independent criteria, role-play, map-not-script principle, offer testing and plan updating.

**[F04] Columbia SIPA — Teaching Civil Discourse in Polarized Times**  
https://www.sipa.columbia.edu/news/teaching-civil-discourse-polarized-times  
Used for: Freeman's Paraphrase–Praise–Probe method and rationale.

**[F05] Columbia SIPA — So You Really Disagree With Someone About Politics. Now What?**  
https://www.sipa.columbia.edu/news/so-you-really-disagree-someone-about-politics-now-what  
Used for: corroboration and explanation of paraphrasing, truthful praise and probing.

**[F06] Breakfast with Stephen — Negotiation: Turn the Tide, featuring Seth Freeman**  
Amazon Music episode page/transcript excerpts.  
https://music.amazon.com.au/podcasts/d2f0050c-0551-413a-8e86-77d16460eef6/episodes/01bf0983-b8c8-4a4a-951b-c86eb7c17f4e/breakfast-with-stephen-negotiation-turn-the-tide---featuring-seth-freeman  
Used for: Freeman's explanation of Notional BATNA.

**[F07] Adam Mendler interview with Seth Freeman — Be Both Strong and Kind**  
https://www.adammendler.com/blog/seth-freeman/  
Used for: Freeman's statement that "yes" is not the goal and his description of Measures of Success.

**[F08] Seth Freeman — Deal Dashboard™: A Structured Pre-Commitment Instrument for Negotiation Preparation and Offer Assessment, SSRN, 2026**  
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6768278  
Used for: structured pre-commitment concept and 2026 Deal Dashboard research status.

**[F09] Negotiate Anything — Stop Relying on Scripts. Start Using This Strategy, 19 June 2025**  
https://podcasts.apple.com/us/podcast/stop-relying-on-scripts-start-using-this-strategy/id1101679010?i=1000713545011  
Used as supporting evidence for contemporary discussion of TTT and Golden Minute. Secondary to Freeman's own written material.

---

## External evidence

**[E01] Galinsky, A.D., Maddux, W.W., Gilin, D., & White, J.B. (2008).  
Why It Pays to Get Inside the Head of Your Opponent: The Differential Effects of Perspective Taking and Empathy in Negotiations. Psychological Science, 19(4), 378–384.**  
DOI: 10.1111/j.1467-9280.2008.02096.x  
https://journals.sagepub.com/doi/10.1111/j.1467-9280.2008.02096.x  
Used for: independent evidence on perspective-taking.

**[E02] Columbia Business School research record for Galinsky et al. (2008)**  
https://business.columbia.edu/faculty/research/why-it-pays-get-inside-head-your-opponent-differential-effects-perspective-taking  
Used for: independent institutional summary of the same research.

**[E03] Freeman, S. & co-author research discussion — Managing the Goal-Setting Paradox: How to Get Better Results from High Goals and Be Happy. Negotiation Journal.**  
https://direct.mit.edu/ngtn/article/25/2/217/122069/Managing-the-Goal-Setting-Paradox-How-to-Get  
Used for: qualification on ambitious targets and subjective satisfaction.

---

# 28. Research conclusions to carry forward

The strongest foundation for a Freeman-based ChatGPT negotiation adviser is not a library of clever phrases. It is a **stateful preparation and decision system** built around:

- interests;
- factual research;
- option generation;
- anticipated reactions;
- perspective-taking and ethics;
- process design;
- alternatives;
- stakeholder power;
- objective criteria;
- targets and trade-offs;
- disciplined rehearsal;
- relationship-aware firmness;
- independent acceptance testing.

Freeman's distinctive contribution for our purposes is the conversion of these ideas into practical, low-cognitive-load tools that can be used under pressure.

The future system should preserve that character. It should make the user **better prepared, harder to manipulate, less likely to concede accidentally, more capable of finding trades, and less likely to accept a superficially attractive but poor deal**.

---

## Change control

Any later document that changes an interpretation in this research base should record:

```text
Research item:
Existing interpretation:
Proposed change:
New evidence:
Source:
Reason:
Effect on architecture/skills:
```

Do not modify a **[FREEMAN]** proposition merely because a different implementation would be easier.

