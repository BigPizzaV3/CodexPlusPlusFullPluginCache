# Reply Generation Orchestration Contract

## Pipeline state

Maintain a compact internal state as each skill contributes:

```json
{
  "matchId": "match_uuid",
  "language": "lt",
  "evidence": {},
  "propertyInterpretations": [],
  "timeline": {},
  "event": {},
  "profile": {},
  "route": {},
  "strategy": {},
  "audit": {}
}
```

This is an internal coordination shape, not the application response. Do not
copy entire Match or Wiki payloads into every stage.

## Stage gates

### 1. Match gate

Require exactly one root Match object with a non-empty `id`. Its current shape
contains root identity, language, status, messages, flat `details`,
`check_list`, string `summary`, and `ai_generations`.

Reject mixed legacy shapes and cross-match context. Prior AI generations and
summary are non-authoritative context.

### 2. Property gate

Resolve relevant Wiki paths and exact observed values. Keep Match data separate
from the user's private interpretation. Do not expose good/bad/blocker labels in
copy.

### 3. Timeline gate

Treat the complete latest same-author message burst as the initial reply target.
Resolve explicit/probable callbacks and account for parallel active topics. A
candidate cannot pass if it randomly ignores a direct question, meaningful
disclosure, correction, boundary, or practical decision.

### 4. Event gate

Resolve whether the current state is active, liked-message pause, ghosted,
CTA, lost interest, reactivated, or closed. Enforce one bounded re-entry and all
explicit boundaries.

### 5. Profile gate

Select only relevant verified and disclosable facts. Audit exact implications.
For example, the imitation/air-pistol photo cannot support shooting-range
experience or real firearm ownership.

### 6. Router gate

Require:

- eligible generation task;
- `en` or `lt` from root language;
- effort;
- ruleset;
- response obligations;
- no unresolved required context;
- no stop state.

### 7. Strategy gate

Require a primary conversational move, message architecture, topic plan,
pressure level, permitted hook or self-disclosure, and candidate diversity plan.

## Stop-state contract

The application result is a discriminated union:

```json
{
  "resultType": "clarification",
  "analysisSummary": "Why more context is required",
  "question": "Smallest question that unlocks generation",
  "suggestions": []
}
```

```json
{
  "resultType": "hold",
  "analysisSummary": "Why no message should be sent yet",
  "question": "",
  "suggestions": []
}
```

```json
{
  "resultType": "close",
  "analysisSummary": "Why the interaction should close",
  "question": "",
  "suggestions": []
}
```

Do not reinterpret a stop state as permission to produce messages.

## Draft construction

Draft from the strategy brief rather than directly from raw Match fields.

For each candidate:

1. choose one strategic direction;
2. satisfy the primary response obligation;
3. integrate or acknowledge required secondary topics;
4. add only a supported hook or self-disclosure;
5. create one easy path forward when appropriate;
6. keep the final text compact and copy-ready.

Not every candidate needs a question. Avoid stacked questions, generic biography
requests, elaborate hypothetical scenarios, and unnecessary explanations.

## Diversity contract

Before drafting, name candidate directions internally. Examples:

- `direct_answer_and_callback`;
- `acknowledge_and_specific_question`;
- `playful_shared_premise`;
- `true_self_disclosure_and_bridge`;
- `unusual_opener_presentation`;
- `optional_social_exchange`.

Use only directions eligible for the task. At least three returned candidates
must differ by direction, not merely adjectives, punctuation, or word order.

## Factual implication audit

Extract conceptual claims from each candidate:

- facts about the user;
- facts about the match;
- shared history;
- preferences and opinions;
- availability and plans;
- possessions, experience, location, work, hobbies, and relationships;
- emotional or psychological claims.

For each claim, record an internal source. Remove or rewrite anything without a
source. Plausibility is not evidence. A question can also imply a fact; audit its
premise.

## Privacy audit

Copy-ready text must not reveal:

- private notes;
- Wiki wording or assessments;
- attractiveness or internal effort;
- checklist scoring or why an answer is being evaluated;
- private personal-profile classifications;
- tentative personality/social portrait;
- prior AI analysis.

The user-facing rationale may explain strategy but should still avoid dumping
sensitive profile or Wiki data unnecessarily.

## Final application result

Return:

```json
{
  "resultType": "suggestions",
  "analysisSummary": "string",
  "question": "",
  "suggestions": [
    { "text": "string", "rationale": "string" },
    { "text": "string", "rationale": "string" },
    { "text": "string", "rationale": "string" }
  ]
}
```

Constraints:

- exactly the four root properties;
- 3–5 suggestions;
- no additional suggestion properties;
- analysis, rationales, and copy in `match.language` unless the user explicitly
  requested a different analysis language;
- no unsupported claims;
- no promise that any suggestion will work;
- no statement that a suggestion was sent.

## Final checklist

- One correct Match ID throughout internal state.
- Every applicable skill ran in order.
- No unresolved stop condition.
- Complete latest turn understood.
- All response obligations handled.
- Current event and retry limits obeyed.
- Language correct.
- Factual implication audit clean.
- Privacy audit clean.
- No in-person invitation.
- Candidates materially distinct.
- Output conforms exactly to the application schema.
