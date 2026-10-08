---
name: dating-response-strategy
description: Convert grounded Match, Wiki, timeline, event, profile, and router briefs into an organic dating-message strategy using reciprocity, cognitive load, topic momentum, calibrated self-disclosure, humor, curiosity, and consent. Use after routing and before generating or reviewing message candidates.
---

# Dating Response Strategy

Choose what the next message should accomplish and how it should be shaped. Do
not draft final copy in this skill.

Read [references/response-principles.md](references/response-principles.md)
before selecting a strategy or comparing candidate directions.

## Required inputs

Consume the relevant outputs of:

- `interpret-match-context` for grounded facts and evidence classes;
- `interpret-property-map` for private Wiki meanings and assessments;
- `read-conversation-timeline` for the latest complete turn, active topics, and
  response obligations;
- `event-state-engine` for event boundaries and retry eligibility;
- `personal-profile` for truthful self-reference and voice constraints;
- `task-and-ruleset-router` for task, language, effort, ruleset, blockers, and
  missing-context status.

If the router selected `pause_for_context`, `wait`, or `close`, honor it. Do not
invent a strategy that bypasses missing facts, event limits, or boundaries.

## Strategic objective

Optimize for an honest, organic exchange that makes the next conversational
step easy and helps both people reveal compatibility. Do not optimize for a
reply at any cost, emotional dependency, control, extracting information, or
performing a tactic on the match.

Evaluate a direction through six lenses:

- `relevance`: it responds to what matters in the current turn;
- `reciprocity`: its investment fits the interaction without mechanically
  copying length or style;
- `ease`: it is cognitively simple to understand and answer;
- `distinctiveness`: it sounds specific enough not to be interchangeable with
  any match;
- `truthfulness`: every explicit and implied personal fact is supported;
- `consent`: it respects boundaries, pressure limits, and event retry rules.

Truthfulness and consent are hard gates. A direction that fails either is
invalid even if it seems engaging.

## Choose the conversational move

Select one primary move:

- `answer`: satisfy a direct question or practical decision;
- `acknowledge`: show that a disclosure, emotion, joke, correction, or boundary
  was received;
- `relate`: add proportionate, verified self-disclosure;
- `play`: continue a shared humorous or flirtatious premise;
- `explore`: ask one specific question that grows from the active thread;
- `clarify`: resolve material ambiguity without interrogation;
- `callback`: revive a meaningful earlier detail or shared joke;
- `bridge`: complete the current topic and enter a related or fresh one;
- `discover`: surface one unresolved checklist or personality topic naturally;
- `reenter`: open one low-pressure fresh thread when the event engine permits;
- `advance`: offer one optional Instagram or Facebook exchange under CTA;
- `close`: end respectfully;
- `hold`: send nothing yet.

Add at most one secondary move when it makes the response more organic. A short
reply may acknowledge then answer, answer then relate, or continue then bridge.
Do not stack goals merely because the data contains them.

## Shape the response

Use this flexible architecture when helpful:

1. `receive`: answer or acknowledge the most important current signal;
2. `contribute`: add a specific reaction, true detail, interpretation, or
   playful extension;
3. `open`: leave an easy path forward through a question, unfinished thought,
   choice, or natural statement.

Not every message needs all three parts, and not every message needs a question.
A relevant statement can invite response more naturally than repeated
interviewing.

When several topics are active, satisfy every must-address obligation from the
timeline brief. Combine compatible topics, acknowledge important secondary
ones, and explicitly park only what cannot fit naturally. Never choose one topic
at random and silently ignore questions or meaningful disclosures.

## Apply messaging theory

### Reciprocity

Calibrate to her demonstrated engagement, not assumptions about interest. Match
the level of informational and emotional investment while still answering the
whole turn. Low effort suggests a simpler response; multiple thoughtful messages
can support a richer one. Do not punish short replies or overreward long ones.

### Cognitive load

Use one clear center of gravity. Prefer one answerable opening over stacked
questions, multiple decisions, or an elaborate setup. Easy to answer does not
mean generic: a constrained, specific question is often both easier and more
distinctive.

### Curiosity and information gaps

Create curiosity through a real specific detail, contrast, callback, or partial
thought. Do not use clickbait, false suspense, withholding, jealousy, or a claim
that requires invented facts.

### Self-disclosure

Reciprocal self-disclosure can build familiarity when it is true, relevant, and
proportionate. Share enough to create exchange rather than interrogate, but do
not overshare to manufacture intimacy. Never infer a personal story from a
photo, interest, profession, personality label, or profile aesthetic.

### Humor and play

Humor works best from a shared premise. Sarcasm, dark humor, absurdity, ASCII,
or Unicode novelty may fit the user's voice when the task and current tone
support them. Tease situations, contradictions, or shared material—not
insecurities, appearance, identity, trauma, competence, or boundaries.

### Emotional attunement

Recognize meaningful emotion without diagnosing or becoming a therapist. Match
the weight of the disclosure: avoid jokes that bypass it, generic reassurance,
premature advice, or exaggerated intimacy.

### Topic momentum

Continue when there is unanswered substance, reciprocal curiosity, a story,
playful tension, logistics, or a strong callback. Change topic only after the
current turn is sufficiently received. When both are needed, bridge rather than
abruptly switching.

## User-specific limits

- Never propose coffee, a date, meeting, or “going out” on the user's behalf.
- CTA may advance only to one optional Instagram or Facebook exchange unless
  the current user explicitly changes this rule.
- Do not use generic or scenario-based questions as a default.
- Do not reveal Wiki scoring, attractiveness, blockers, private notes,
  personality hypotheses, or internal effort level.
- A checklist question may be integrated only when the router selected it and
  the current thread can carry it naturally.
- Do not lie about the user's view to conceal a negative assessment. Use a
  truthful neutral explanation, defer, or keep the private rubric undisclosed.

## Effort calibration

- `minimal`: choose one direct, low-complexity move; no deep callbacks or extra
  discovery unless necessary.
- `normal`: use the current thread, one specific contribution, and an organic
  opening when useful.
- `high`: compare at least two materially different directions, check hidden
  callbacks and all active topics, then choose the strongest grounded option.
- `pause`: return no message strategy until the router's question is answered.

High effort means better analysis, not longer or more ornate output. Minimal
effort never permits low-quality, disrespectful, or untruthful wording.

## Strategy output

Return a strategy brief:

- `task`, `language`, `ruleset`, and `effort`;
- current conversational state;
- primary and optional secondary move;
- must-address and optional topics;
- intended emotional tone and pressure level;
- response architecture;
- specific Match hook or callback, if any;
- permitted verified self-disclosure, if any;
- optional checklist discovery goal;
- question form or non-question opening;
- facts and private assessments that must remain hidden;
- candidate directions that are materially distinct;
- risks, assumptions, and rejection criteria.

Reject any direction that could be sent unchanged to almost anyone when a
specific grounded alternative exists.
