---
name: event-state-engine
description: Interpret Date Chatbot timeline events—liked message, ghosted, CTA, and lost interest—and convert them into psychologically grounded, low-pressure strategy without claiming certainty about motives. Use when a Match timeline or status contains one of these event states.
---

# Event State Engine

Interpret state events as changes in conversational strategy. An event records
what happened operationally; it does not reveal why it happened.

Read [references/event-catalog.md](references/event-catalog.md) before applying
an event-specific strategy or recommending re-entry, contact exchange, or
closure.

## Resolve the current state

`match.messages` is chronological. Supported event kinds are:

- `liked_message` — she reacted to a message without adding a written reply;
- `ghosted` — no reply arrived within the user's chosen waiting period;
- `cta` — the user marked that the interaction is ready for a next-step call to
  action;
- `lost_interest` — the user marked that interest has been lost by one or both
  sides; the event does not encode whose interest changed.

Use the latest timeline item as the current boundary. A later real message from
either author means the conversation is active again and supersedes an earlier
event for current-state strategy. Retain the older event only as history.

Inspect the immediately preceding conversational turn and relevant private note
before interpreting an event. Do not infer missing timing, who initiated an
event, or whether an event represents an explicit statement.

## Psychological frame

Use uncertainty-aware, situational explanations first. Dating apps can create
high message volume, fragmented attention, choice overload, notification
fatigue, competing priorities, and accidental forgetting. These are plausible
non-personal explanations for low effort or silence—not established facts and
not claims about women as a group.

Also preserve other plausible explanations: the previous message may not have
invited a response, the thread may have felt complete, timing may be poor, the
match may be busy, interest may have decreased, or the match may have chosen not
to continue. Do not diagnose attention span, attachment style, personality, or
intent from an event.

Apply these principles:

- avoid the fundamental attribution error: behavior does not prove character;
- match effort rather than escalating after low-effort feedback;
- reduce cognitive load with one easy conversational move;
- preserve autonomy and an easy way not to engage;
- avoid pressure, guilt, scorekeeping, or mentioning competition;
- treat uncertainty as a reason for restraint, not repeated testing.

## Strategy by event

### Liked message

Treat a like as acknowledgement with low conversational investment. It often
means the current thread is paused and no further written answer should be
expected immediately. It is weak positive evidence that the message was seen or
received, but it does not establish attraction, rejection, exhaustion, low
attention span, or future intent.

Check whether the liked message naturally required a reply. If it was a joke,
photo, compliment, or closing statement, a reaction may be a complete social
response. If it contained a clear question, the like still does not answer it;
the conversation remains paused.

Do not instantly chase the reaction with another demand for attention. Either
wait or later open one easy, fresh thread. Do not ask why she only liked it.

### Ghosted

Treat silence as missing behavioral response, not an explanation. A useful
self-protective interpretation is that the conversation did not retain enough
attention in a competitive, overloaded environment; this is a strategy model,
not proof that the user was uninteresting or that she forgot.

Review whether the last user turn was answerable, overly demanding, closed, or
dependent on missing context. If no explicit rejection or boundary exists, one
later low-pressure reintroduction may be considered. Prefer a fresh, specific,
easy-to-answer topic over “why did you disappear?” or repeating the ignored
message.

After one unanswered re-entry, stop. Never recommend repeated follow-ups,
alternate-account contact, guilt, urgency, or confrontation.

### CTA

Treat CTA as readiness to propose a concrete next step, not evidence that the
match has already consented. The user's preferred sequence is exchanging
Instagram or Facebook before an in-person meeting, because preserving contact
reduces the practical risk of losing the connection after an unmatch.

Confirm that the recent interaction has enough reciprocal engagement for an
ask. Recommend one clear, low-pressure action with an easy opt-out. Prefer a
social-contact exchange first unless the current user explicitly requests a
meeting or the conversation already contains mutual meeting plans.

Do not present contact exchange as creating responsibility, certainty,
commitment, exclusivity, or safety. Do not request multiple channels at once or
pressure after hesitation.

### Lost interest

First determine whose interest appears to have changed from direct messages,
notes, and the current user request. If this cannot be established, keep it
ambiguous.

If the match explicitly rejected contact, set a boundary, unmatched, blocked,
or clearly asked not to continue, close the interaction. Do not recommend a
retry regardless of attractiveness or other favorable details.

If no explicit rejection exists and the event is the user's own uncertain or
temporary loss of interest, the user may reconsider once. High attractiveness
or favorable non-blocking Wiki assessments may explain the user's desire to
re-evaluate, but they do not create entitlement or evidence of her interest. A
retry must be one low-pressure, contextually plausible message with no complaint
or demand. If it receives no response, stop.

## Precedence and retry budget

Apply this order:

1. explicit rejection, consent, safety issue, or boundary;
2. latest real message after an event;
3. latest current event;
4. direct conversational evidence;
5. private user note and current instruction;
6. Wiki preferences and compatibility assessments;
7. psychological hypotheses.

Explicit boundaries cannot be overridden by attractiveness, a positive Wiki
assessment, prior chemistry, a liked message, or the belief that silence was
accidental.

Across `liked_message`, `ghosted`, and ambiguous `lost_interest`, allow at most
one suggested re-entry after the current pause unless a later real message
reactivates the conversation. The event engine must surface whether that retry
has already occurred; it must not reset the budget by changing wording or
channel.

## Handoff

Return an event brief rather than drafting the message:

- `eventKind` and event ID;
- whether it is current or superseded;
- directly observed behavior;
- plausible explanations, labeled as hypotheses;
- explanations that must not be claimed;
- strategic state: `wait`, `low_pressure_reentry`, `advance`, `close`, or
  `active_again`;
- retry eligibility and remaining retry budget;
- relevant boundary or consent constraint;
- recommended effort level;
- what the next strategy may do and must avoid.

Keep private psychological framing, attractiveness assessments, competition,
and Wiki judgments out of copy-ready messages.
