---
name: read-conversation-timeline
description: Reconstruct the current conversational turn from a chronological Date Chatbot message timeline, including consecutive-message bursts, callbacks to earlier context, parallel active topics, and whether the next reply should continue, introduce a new topic, or do both. Use before planning or generating a reply from Match messages.
---

# Read Conversation Timeline

Identify what the latest messages mean together and what a reply must respond
to. The final array item is only a starting point. The relevant unit is the
latest conversational turn plus any earlier context it depends on.

Read [references/timeline-rules.md](references/timeline-rules.md) when deciding
whether messages are linked, tracking simultaneous topics, or choosing the
smallest sufficient context window.

## Read the current turn

`match.messages` is chronological, oldest to newest.

1. Start at the final timeline item.
2. If it is a state event rather than `kind: "message"`, identify it as the
   current boundary and hand its strategic meaning to the event-state skill.
   Inspect preceding messages only to explain what the event follows.
3. Otherwise group the final message with every immediately preceding message
   from the same author. This is the latest message burst. Never discard part of
   the burst merely because only its final message contains a question.
4. If the latest burst is from the match (`author: "her"`), treat the whole
   burst as the initial reply target. Four consecutive messages may contain four
   connected thoughts, several questions, or multiple independent topics.
5. If the latest burst is from the user (`author: "me"`), there is no new reply
   from the match to answer. Report the pending user turn; do not pretend the
   match responded.

## Trace earlier context

For each message in the latest burst, predict whether understanding it requires
earlier messages. Trace backward by conversational turns, not a fixed message
count.

Look for:

- direct answers to earlier questions;
- pronouns, demonstratives, ellipsis, or phrases such as “that,” “it,” “also,”
  “still,” “then,” or “what about you?”;
- repeated people, places, plans, jokes, claims, or unusual wording;
- corrections, clarifications, reactions, callbacks, and unfinished stories;
- a topic resumed after an intervening side topic;
- timing or logistics that only make sense with an earlier proposal;
- a private note that identifies otherwise missing context.

Classify each proposed link as `explicit`, `probable`, `possible`, or `none`.
Expand the working window for explicit and probable links. Preserve possible
links as uncertainty unless they materially change the reply; then inspect
farther or flag the ambiguity. Do not manufacture continuity from generic words
or superficial similarity.

Stop expanding when every important statement in the latest burst is
understandable, all active topics have an origin or are clearly new, and older
turns add no decision-relevant meaning.

## Track every active topic

Build a topic ledger for the selected window. A topic may span non-adjacent
messages. For each topic record:

- the supporting message IDs;
- its latest contribution;
- whether it contains a direct question, disclosure, joke, disagreement,
  logistical point, boundary, or ordinary statement;
- whether it is `open`, `answered`, `acknowledgement_needed`, `paused`, or
  `closed`;
- whether omitting it would confuse the match or feel dismissive.

Do not randomly select one topic and silently drop the rest. Account for every
meaningful open topic. This does not mean answering every sentence separately:

- combine connected topics in one natural response;
- directly answer clear questions and decisions;
- acknowledge an important disclosure even when another topic becomes primary;
- briefly park a lower-priority topic when handling everything at once would
  sound mechanical;
- omit only material that is already resolved, merely decorative, or naturally
  requires no response.

If two interpretations compete, keep both hypotheses and identify which reply
would remain natural under either one.

## Decide conversational direction

When there is no overriding state event, classify the next move:

- `continue`: an active topic has momentum, an unanswered question, meaningful
  disclosure, unresolved logistics, playful tension, or a clear callback.
- `new_topic`: the current exchange is complete, closed, repetitive, or offers
  no useful thread worth extending.
- `continue_and_new`: first respond to the current turn, then bridge naturally
  into a related or fresh topic. Use this when continuity matters but the thread
  alone would stall.
- `wait`: the latest turn belongs to the user and no event or explicit request
  supports another message yet.

Prefer continuity while it remains organic. A new topic must not function as an
escape from an unanswered question, emotional disclosure, disagreement,
boundary, or practical decision. When changing topics, use a bridge when the
relationship between subjects is real; do not invent one.

## Handoff

Return a timeline brief, not a drafted reply:

- `latestItemId` and type;
- latest burst author and all burst message IDs;
- selected context window message IDs;
- link hypotheses with confidence and supporting IDs;
- active topic ledger, including response obligations;
- current event boundary, if any;
- `direction`: `continue`, `new_topic`, `continue_and_new`, or `wait`;
- what the next reply must address, may address, and should not assume;
- unresolved ambiguity.

Keep raw wording and sender attribution intact. Never convert a private note,
topic hypothesis, or inferred callback into something the match explicitly said.
