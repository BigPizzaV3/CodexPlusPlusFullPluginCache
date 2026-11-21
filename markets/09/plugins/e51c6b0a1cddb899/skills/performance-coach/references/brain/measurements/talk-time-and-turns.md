---
key: talk-time-and-turns
type: measurement
measurement_key: turn_taking
dimension: Engagement
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#talk-time-balance; CardHelpProvider.tsx#speaker-turns-and-time; CardHelpProvider.tsx#insight-summary; registry"
last_verified: "2026-07-18"
---

# Talk Time and Turns

## What it measures

How speaking time and speaking turns are distributed between participants: your percentage of total active speaking time, each speaker's turn count, and total speaking duration in seconds. Multi-party calls combine all non-focus speakers into one comparison bar on the balance card. Research anchor: the foundational turn-taking systematics of conversation analysis (Sacks, Schegloff and Jefferson 1974).

## Where you see it

The Talk Time Balance card (Overview tab), Speaker Turns and Speaking Time (Detailed tab), the Session Insight Summary, the swimlane bars on the Communication Timeline, and per-speaker talk share in team views.

## How to read your number

Targets adjust by conversation type; look for the On Target / Review / Off Target badge on the balance card. The card's stated context targets for your share:

- Discovery calls: 30-45% (let the prospect talk more).
- Demos and presentations: 55-70% (you lead, but check in).
- Coaching sessions: 25-40% (guide, do not lecture).
- Negotiations: 40-55% (balanced exchange).

General guidance elsewhere in the product treats 40-60% as balanced two-way dialogue. Turn shape matters too: balanced alternating turns suggest collaborative dialogue; one speaker dominating turns may indicate monologuing; short turns with frequent switches suggest high engagement; if you take about three times more turns than the other side, you may be interrupting. In multi-party meetings, compare each person against an equal share (one divided by the number of speakers).

## What moves it

- Down (when too high): asking open questions and stopping; pausing after key points; handing the floor back after one sentence of explanation.
- Up (when too low): summarizing and sharing your perspective; answering with a position instead of deflecting.
- The corner-coach guideline for discovery calls is a talk ratio near 43:57 (you:them) with monologue runs kept under about 76 seconds. These are coaching guidelines from the skill's anchor table (expert-estimate provenance), cited as correlations, never promises. The shipped timing detector separately flags your unbroken runs at a 90-second floor (see [[timing-critical-moments]]).

## Drills

- Land-and-hand: feel the run starting, land the point in one sentence, hand it back with an open question. Check your longest-run stat next session. See [[drills-library]].
- One question then silence, when your share runs high.

## FAQ

**They asked me to walk through everything. Does that count against me?**
No. A requested walkthrough answers a request; the coach checks the preceding utterance before counting a long run as drift. Demos are also read against demo targets, not discovery targets.

**Is more talking ever right?**
Yes: demos and presentations legitimately run 55-70% your side. The measurement is about fit to the conversation's purpose, not minimizing your voice.

**What is a healthy turn count?**
No published universal number. Compare the shape: balanced alternation versus one-sided runs, and your own history for that call type.

## Related

[[engagement]] · [[timing-critical-moments]] · [[questions-asked]] · [[interruptions]] · [[power-dynamics]] · [[drills-library]]
