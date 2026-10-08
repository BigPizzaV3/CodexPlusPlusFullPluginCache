---
name: task-and-ruleset-router
description: Route Date Chatbot requests into opener, reply, review, explanation, re-entry, CTA, or pause workflows; select effort, language, discovery goals, and conversational rules from Match, Wiki, timeline, event, and personal-profile context. Use before dating-message strategy or generation.
---

# Task and Ruleset Router

Decide what work should happen before any response is drafted. The router must
consume the grounded outputs of `interpret-match-context`,
`interpret-property-map`, `read-conversation-timeline`, `event-state-engine`,
and `personal-profile` when their data is relevant.

Read [references/rulesets.md](references/rulesets.md) before routing an opener,
lowering effort, selecting a checklist discovery goal, or pausing for context.

## Preflight

Before choosing a task:

1. Confirm one Match record and its relevant Wiki payload were interpreted.
2. Read the complete latest conversational turn and all active topics.
3. Resolve the current event state and retry budget.
4. Inspect relevant details, checklist answers, Wiki meanings, positive or
   negative assessments, blockers, and attractiveness.
5. Load only relevant verified personal-profile facts and disclosure rules.
6. Determine response language from root `match.language`: `en` means English;
   `lt` means Lithuanian.
7. Run the missing-context gate. If required context is absent, stop before
   strategy or generation and ask the smallest question that unlocks the task.

Do not skip preflight because the latest message appears easy.

## Select the task

Choose one primary task:

- `generate_opener`: no real conversation exists and the user wants a first
  message;
- `generate_reply`: the latest complete turn belongs to the match;
- `review_draft`: the user supplied a candidate message for evaluation;
- `reentry`: the current event permits one bounded low-pressure restart;
- `advance`: CTA is current and a next-step proposal is appropriate;
- `explain`: the user asks for interpretation or strategy rather than copy;
- `wait`: the user's message is latest and no follow-up is currently justified;
- `pause_for_context`: generation requires missing or ambiguous information;
- `close`: a blocker, boundary, explicit rejection, or user instruction ends
  the interaction.

The user's explicit current request controls when compatible with facts,
consent, event limits, and disclosure rules.

## Opener rules

For `generate_opener`, prefer something unexpected and compact that tests for a
compatible sense of humor. The opener may:

- ask an intriguing, slightly unconventional question;
- make a playful observation from a distinctive Match detail or profile prompt;
- use a line such as “I know your name. What's your social ID?” as an absurdist
  joke about a social handle—not a demand for legal identity or private data;
- use one restrained ASCII-art or Unicode-styled greeting when visual novelty is
  the whole hook.

Do not default to cheesy fantasy hypotheticals, impossible “what if” scenarios,
generic interview questions, generic compliments, or copied pickup lines.
Examples to avoid include “What superpower would you choose?”, “How was your
day?”, and “What do you do for fun?” unless the existing context makes that exact
question specific and meaningful.

Unicode styling or ASCII art is optional, not a requirement. Keep it readable,
short, and copyable. Do not fake platform-native bold or italic formatting when
the platform may not support it.

Never generate an invitation for coffee, a date, or going out. The user does not
want the agent to initiate an in-person meeting. CTA may route toward a
low-pressure Instagram or Facebook exchange under the event-state rules.

## Effort selection

Choose:

- `minimal`: low user priority, low attractiveness, several explicit negative
  non-blocking assessments, a weak/closed thread, or a simple factual response;
- `normal`: ordinary viable interaction with adequate context;
- `high`: high user priority, strong relevant positives, several active topics,
  hidden callbacks, CTA, sensitive ambiguity, or a strategically important
  turn;
- `pause`: a blocker, prohibited action, or missing context makes generation
  inappropriate.

Attractiveness and Wiki assessments represent the user's private prioritization,
not the match's human worth. Lower effort means less analysis, fewer callbacks,
and less personalization—not a rude, careless, deceptive, or incoherent reply.
A blocker may route to `close` or `pause`; it must not be silently averaged away
by attractiveness.

## Checklist and personality discovery

Maintain awareness of unresolved `check_list` items. When an unanswered item is
relevant and the conversation offers a natural opening, choose at most one as a
secondary discovery goal. It may be asked directly or approached indirectly,
but never through deception, pressure, or a hidden psychological test.

Do not force checklist questions into every message. Answering the current turn
and keeping the conversation organic take precedence. Never expose that an
answer was privately scored as good, bad, or blocking.

If the match asks why a topic matters, do not lie. Give a neutral truthful answer,
defer the private evaluation, or say the user is curious how she sees it. Never
invent agreement or claim a neutral opinion the user does not hold.

Build an early social/personality portrait only from direct messages, explicit
details, checklist answers, and clearly labeled Wiki interpretation. Keep traits
tentative and evidence-linked. Do not diagnose, stereotype, or infer character
from MBTI, autism, profile aesthetics, response latency, or a single answer.

## Factual-grounding invariant

Never generate wording that asserts or implies an unsupported fact about the
user. Audit implications, not only literal statements.

For example, a photo with a Glock imitation/air pistol does not support “I go to
the shooting range,” “I own a gun,” or a shared shooting hobby. The only usable
facts are those explicitly present in the personal profile, Match conversation,
or current user instruction and permitted by disclosure rules.

If an appealing response depends on an unknown personal fact, route to
`pause_for_context` or choose a response that does not depend on it.

## Missing-context gate

Pause and ask when generation materially depends on:

- a referenced image, voice note, profile item, or earlier conversation that was
  not supplied;
- ambiguous sender, event owner, reply target, or conversation link;
- a factual claim about the user absent from the personal profile;
- unclear language or intended task;
- missing consent/boundary context for re-entry or CTA;
- a contradiction that changes what may safely or honestly be said.

Ask one precise question or a small tightly related set. Do not pause for merely
optional color when a grounded organic response is already possible.

## Router output

Return a routing brief before generation:

- `task`;
- `language`;
- `effort` and evidence-based rationale;
- active event state and retry eligibility;
- primary conversational obligation;
- active secondary topics that cannot be ignored;
- optional checklist discovery goal;
- tentative personality/social hypotheses relevant now;
- relevant profile facts permitted for use;
- blockers, boundaries, and forbidden moves;
- missing context and the exact question to ask, if paused;
- ruleset name from the reference.

Do not draft response candidates in this skill.
