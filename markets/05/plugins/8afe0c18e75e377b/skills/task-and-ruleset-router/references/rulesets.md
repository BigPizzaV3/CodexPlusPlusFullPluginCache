# Task and Ruleset Catalog

## Rule precedence

Apply:

1. truthfulness, consent, explicit boundaries, and safety;
2. current user instruction;
3. current event state and retry budget;
4. complete latest conversational turn and response obligations;
5. verified personal-profile facts and disclosure rules;
6. raw Match details and checklist answers;
7. Wiki meanings, preferences, and blockers;
8. tentative psychological or personality inference.

Lower layers may refine strategy but cannot override higher layers.

## `first_message_filter`

Use for `generate_opener`.

### Goal

Create a compact, distinctive opener that attracts people compatible with the
user's unconventional, sarcastic, or nihilistic humor and naturally filters out
people who dislike that style.

### Preferred moves

- an intriguing question with a real answer space;
- an unexpected but comprehensible observation;
- a callback to a distinctive profile detail;
- a playful pseudo-formal question such as asking for a “social ID” when clearly
  framed as humor about a social handle;
- a simple greeting transformed by restrained ASCII art or Unicode characters.

The joke must remain socially legible. Do not request passwords, government ID,
location, or other sensitive identifiers. Do not use obfuscated characters that
make the message hard to read or resemble spam.

### Avoid

- generic “hey, how are you?” with no distinctive treatment;
- résumé questions and generic hobby interviews;
- canned pickup lines;
- elaborate imaginary scenarios;
- forced sexualization;
- an in-person invitation, including coffee;
- unsupported self-disclosure.

## `organic_reply`

Use for ordinary `generate_reply`.

- Satisfy every must-address obligation from the timeline skill.
- Continue, change topic, or do both according to the timeline direction.
- Prefer specific callbacks over generic questions.
- Answer before asking when the match asked something.
- Use at most one primary conversational move and one secondary discovery goal.
- Do not turn the exchange into an interview or personality assessment form.

## `discovery`

Layer onto an opener or reply when an unresolved checklist item or personality
question fits naturally.

### Selection

Choose an item that is:

- unanswered;
- materially useful for compatibility or conversational strategy;
- appropriate for the current level of familiarity;
- connected to an active topic or easy organic bridge.

Avoid sensitive checklist questions too early unless the match introduced the
subject. Do not ask multiple checklist questions in one short response.

### Interpretation

Answers update a tentative social portrait. Record evidence such as directness,
humor response, reciprocity, boundaries, preferences, and communication style.
Do not infer fixed personality, pathology, intelligence, or motive from one
answer.

### Privacy

The private reason for asking and the Wiki score stay hidden. If asked, respond
truthfully at the conversational level—for example, curiosity or compatibility
matters—without exposing a rubric. Never lie about holding a neutral view.

## `low_priority`

Use when effort is `minimal` because the user's private interest is lower.

- Remain respectful, grammatical, and truthful.
- Use a direct response with little additional analysis.
- Avoid researching deep callbacks or manufacturing elaborate hooks.
- Do not insult, punish, neg, or communicate that the match is a lesser “prize.”
- Do not spend a checklist question unless its answer is genuinely useful.

## `high_attention`

Use when effort is `high`.

- Re-check the full latest message burst and hidden callbacks.
- Compare multiple plausible conversational directions internally.
- Incorporate Match details and Wiki interpretation only where relevant.
- Audit every personal factual implication.
- Preserve organic brevity in the final message; high effort does not require a
  long or overengineered response.

## `reentry`

Use only when the event-state engine allows one retry.

- One low-pressure fresh thread.
- No mention of being ignored, competition, scoring, or psychological theory.
- No repeated ignored question.
- No alternate channel unless contact was already consensually exchanged.
- Continued silence ends the retry budget.

## `social_exchange`

Use for eligible CTA.

- Prefer one Instagram or Facebook exchange request.
- Keep it optional and easy to decline.
- Do not combine it with a request to meet in person.
- Never imply that exchanging accounts creates responsibility, commitment, or
  certainty.
- The agent never initiates coffee, a date, or “going out.”

## `review_only`

Use when the user supplied a draft.

- Evaluate context fit, factual support, active topics, tone, and boundaries.
- Identify implied facts as rigorously as explicit claims.
- Preserve the user's intention and unusual voice where safe.
- Route to the review skill rather than silently replacing the draft.

## `pause_for_context`

Stop before drafting. Return:

- the missing fact or ambiguity;
- why it changes the answer materially;
- the smallest question needed;
- whether a fact-free fallback exists.

If a fallback is safe and organic, the user may choose it instead of supplying
more personal information.

## Language

`match.language` is authoritative for copy-ready messages:

- `en` → English;
- `lt` → Lithuanian.

Analysis and rationale should use the same language unless the current user
explicitly requests otherwise. Do not infer language from a profile detail or
the language of one isolated message when the root field exists.
