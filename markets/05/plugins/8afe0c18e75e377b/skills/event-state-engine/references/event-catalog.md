# Event Catalog

## Shared interpretation rule

An event is a user-recorded operational state. It is stronger than a weak tone
inference but weaker than an explicit statement in a real message. Event kinds
do not contain timing, motive, consent, or the identity of the person whose
interest changed unless surrounding context supplies it.

## `liked_message`

### Observed

The match added a reaction to a message and did not add written content in that
event.

### Reasonable hypotheses

- acknowledgement was sufficient for that message;
- she had low available effort at that moment;
- the thread felt complete;
- she was distracted, overloaded, or unsure what to add;
- interest was present but not strong enough for a written response;
- interest may have decreased.

None is certain. A like is normally more informative than no interaction, but
it is not a promise of continued conversation.

### Strategy

Default to `wait`. If the conversation remains inactive, one later low-friction
topic can be considered. Match the low effort; do not interrogate the reaction.

## `ghosted`

### Observed

No reply arrived by the user's chosen threshold after the last user message.

### Reasonable hypotheses

- notification or choice overload;
- competing conversations or priorities;
- accidental forgetting;
- poor timing;
- the previous message was hard to answer or naturally closed the thread;
- reduced or absent interest.

Silence cannot distinguish these explanations. Use a non-personal explanation
to avoid unnecessary self-blame, but never present it as known truth.

### Strategy

If there is no explicit rejection and no prior re-entry attempt, allow one
`low_pressure_reentry`. The re-entry should provide fresh value or an easy
specific prompt and must not mention being ignored. Continued silence closes the
retry path.

## `cta`

### Observed

The user marked that a next-step ask is strategically appropriate. This is an
instructional marker, not an action already taken by the match.

### Preferred ladder

1. Confirm recent reciprocal interaction and absence of a boundary.
2. Offer one low-pressure Instagram or Facebook exchange.
3. If mutually accepted, continue there.
4. Consider an in-person meeting when both sides show readiness.

The ladder is the user's preference, not an inflexible social rule. A direct
meeting can be appropriate when the current instruction or conversation already
supports it. Contact exchange does not create certainty, responsibility,
identity verification, or guaranteed continuity.

### Strategy

Set state `advance`. Make one clear ask, avoid stacking social exchange and a
meeting into one demand, and accept hesitation or refusal without persuasion.

## `lost_interest`

### Observed

The user recorded that interest is lost or fading. The schema does not say
whether this refers to the user, the match, or both.

### Resolution

- Direct rejection or boundary from her: `close`, no retry.
- User's own temporary uncertainty without rejection: optionally reassess
  Match facts and Wiki compatibility.
- Mutual conversational fade without explicit rejection: one low-pressure
  re-entry may be eligible if none was already attempted.
- Unknown owner of the state: preserve ambiguity and ask or choose a strategy
  that does not depend on knowing.

Attractiveness and positive Wiki properties describe the user's motivation to
reconsider. They never outweigh consent or prove reciprocal interest.

## Event transitions

Events remain history when later messages arrive:

```text
message(me) -> ghosted -> message(her)
```

Current state is `active_again`; the ghosting event may inform effort and tone
but must not be used to punish, test, or guilt her.

```text
message(me) -> liked_message -> ghosted
```

Current state is `ghosted`; both events belong to the same paused interaction
and share one retry budget.

```text
lost_interest -> message(me)
```

A user message alone shows the user resumed outreach, but it does not establish
her renewed interest. If no reply follows, do not grant another retry merely
because a new event marker was added.

## Psychological safeguards

- Situational attribution reduces self-blame but must remain hypothetical.
- Effort matching avoids overinvestment after weak feedback.
- Low cognitive load can make re-entry easier; it must not become a covert
  pressure technique.
- Autonomy and reactance matter: pressure, guilt, and repeated asks generally
  make engagement less likely and disrespect the recipient's choice.
- Variable reinforcement from occasional replies can tempt repeated pursuit;
  the one-retry budget prevents that pattern from driving strategy.
- Do not generalize individual behavior to women, diagnose motives, or promise
  that a psychological tactic will restore attention.
