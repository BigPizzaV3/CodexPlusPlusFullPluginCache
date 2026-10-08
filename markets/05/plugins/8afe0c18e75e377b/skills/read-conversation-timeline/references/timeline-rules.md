# Conversation Timeline Rules

## Contents

- Turns and bursts
- Link prediction
- Parallel topics
- Direction selection
- Worked cases

## Turns and bursts

The timeline is chronological. Consecutive real messages from one author form a
message burst within the same conversational turn until the other author or a
state event appears.

A burst is not guaranteed to be one topic. Treat punctuation and message
boundaries as presentation choices, not proof of semantic separation. Evaluate
every message in the burst before deciding what the sender is doing.

Example latest burst:

```json
[
  {
    "id": "m17",
    "kind": "message",
    "author": "her",
    "text": "Yeah, I went there last summer"
  },
  {
    "id": "m18",
    "kind": "message",
    "author": "her",
    "text": "The old town was beautiful"
  },
  {
    "id": "m19",
    "kind": "message",
    "author": "her",
    "text": "I mostly travel for food though 😄"
  },
  {
    "id": "m20",
    "kind": "message",
    "author": "her",
    "text": "Where would you go next?"
  }
]
```

The reply target is `m17`–`m20`, not only `m20`. The travel experience, food
angle, tone, and question jointly define the turn. A natural reply can answer
the question and connect to food or the old-town detail without responding to
each line mechanically.

## Link prediction

For each latest-burst message, test candidate links backward.

### Explicit link

The wording directly identifies its source: a direct answer, quote, named
callback, correction, or explicit reference such as “about your Italy idea.”

### Probable link

The message is difficult to understand without one earlier thread and shares
specific entities, actions, or unresolved meaning with it. Example: “Thursday
works better” probably links to an earlier scheduling proposal.

### Possible link

The connection is plausible but alternatives remain. Example: “That sounds
dangerous 😂” could refer to either of two recent jokes. Preserve the ambiguity;
do not select one without evidence.

### No link

The message is self-contained or begins a clearly unrelated topic.

Recency supports a link but does not prove one. Specific semantic dependence is
stronger than keyword overlap. A resumed topic can skip over intervening turns,
so stop at understanding rather than an arbitrary lookback count.

## Parallel topics

Maintain one ledger entry per meaningful thread. Merge entries only when they
share the same underlying subject or decision.

Response priority usually follows:

1. explicit boundary, correction, or safety-sensitive statement;
2. direct question or practical decision;
3. emotionally meaningful disclosure or disagreement;
4. active story, joke, flirtation, or callback;
5. ordinary informational statement;
6. decorative filler that needs no response.

Priority decides emphasis, not whether every other topic disappears. For each
lower-priority open thread, decide explicitly to integrate, acknowledge, park,
or omit as resolved/non-obligatory.

If the latest burst says both “Thursday works” and “I’m nervous about crowded
places,” a response that handles only Thursday may be confusing or dismissive.
The topics can be combined: acknowledge the concern while resolving logistics.

If the burst contains three playful observations and one direct question, it is
usually sufficient to answer the question and react to the most distinctive
observation. Listing four separate answers would sound like form processing.

## Direction selection

### Continue

Use when the current thread can naturally support the next exchange. Strong
signals include questions, incomplete stories, disclosures, concrete shared
subjects, logistics, callbacks, and reciprocal curiosity.

### New topic

Use when the current thread has reached a natural endpoint and no meaningful
response obligation remains. Avoid interrogative topic-hopping solely to keep
the chat alive.

### Continue and introduce a new topic

Respond to what matters first, then use one organic transition. The new topic
may grow from a detail in the latest turn or be fresh after a clean closure.
Never use a topic switch to dodge substance.

### Wait

Use when the user's message burst is last and nothing from the match follows.
Whether a follow-up is later appropriate belongs to strategy and event rules,
not to timeline reconstruction.

## Worked cases

### Hidden callback

Earlier:

```text
me: My cooking experiments are usually a little chaotic.
```

Latest burst:

```text
her: So did the kitchen survive? 😄
her: And was it at least edible?
```

Both messages probably link to the cooking thread. The selected window must
include its origin. Treating only “was it edible?” as a generic food question
would lose the joke and conversational continuity.

### Two independent topics

Latest burst:

```text
her: Work was brutal today.
her: But your dog photo made me laugh.
her: Is that actually your dog?
```

Topic ledger:

- difficult workday: `acknowledgement_needed`;
- dog/photo: `open`, with a direct question.

The next reply should account for both. It can acknowledge her day briefly and
answer the dog question, rather than ignoring the disclosure or writing two
disconnected mini-essays.

### Topic exhausted

```text
me: Glad the exam went well.
her: Thanks 😊
```

The exam topic is naturally closed unless earlier context leaves a specific
thread open. A new topic may be more organic than forcing another exam question.
