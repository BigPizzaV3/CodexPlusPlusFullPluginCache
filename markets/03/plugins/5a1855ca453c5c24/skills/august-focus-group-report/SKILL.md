---
name: august-focus-group-report
description: >
  Take an already-finished August focus group and turn its raw results into
  an actual readout — consensus points, disagreements with named sides,
  standout quotes, a rough sentiment split, and unresolved follow-up
  questions. Post-hoc synthesis only; does NOT trigger a new focus group.
  Use when the user has an FG that already ran and wants it read out for
  them instead of scrolling raw output. Triggers on: "focus group report",
  "synthesize focus group", "read out this focus group", "FG readout",
  "summarize the focus group", "/august-focus-group-report".
---

# August Focus Group Report

Post-hoc synthesis of a completed August focus group. This skill does
NOT run a new focus group — it reads out an existing one. Tools live
under the August MCP.

**When to use:**
- A focus group has already been run (the user references it by name /
  id, or says "the focus group I did yesterday")
- The user wants consensus, disagreements, and quotes — not raw output
- The user is preparing a share-out, doc, or decision brief off the FG

**When NOT to use:**
- The user wants to START a new focus group — that's a different flow
  (`start_focus_group` + `run_focus_group_round`), not this skill
- The user wants deep 1:1 depth on one twin → use `/august-interview`
- The user wants a quick gut check → use `/august-feedback`

**Core rule:** never fabricate consensus or attribution. If the raw
results don't clearly show who said what, say so — do not paper over
gaps to make the readout cleaner.

---

## STEP 1 — Identify the focus group

Get to a specific `focus_group_id` before doing anything else.

1. If the user provided an id or exact name, use it directly.
2. If they described the FG loosely ("the pricing one from last week",
   "the Backcountry hero image FG"), call `list_focus_groups` on the
   likely org and match by name/date/topic.
3. If multiple candidates match, ask the user with the top 2–3
   with one-line summaries (topic + date + twin count) and let the user
   pick. Never guess.
4. If no FG matches, tell the user plainly — do not fabricate results,
   and do not silently start a new one.

---

## STEP 2 — Pull the raw results

Call `get_focus_group_results` with the confirmed `focus_group_id`.

Also note, from the results payload:
- List of participating twins (names + ids)
- List of stimuli that were shown
- Number of rounds run

You'll need all of these for attribution in the readout.

If the results are empty or the FG hasn't finished, stop and tell the
user — do not synthesize a partial FG as if it were complete.

---

## STEP 3 — Synthesize

Read the full results carefully. Build the readout in this order:

1. **Group by stimulus / question**, not by twin. The unit of analysis
   is "what did the group think about X?" not "what did Twin A think?"
2. **For each stimulus, sort takes into agree / disagree / mixed** based
   on the actual content — do not force a 3-way split if there wasn't
   one.
3. **Attribute every disagreement** to the specific twins on each side.
   Attribution is the whole point of running a group vs. a single
   interview.
4. **Extract quotes** that are punchy, specific, and representative —
   not the longest, the shortest, or the most anodyne.
5. **Score sentiment** at the twin level per stimulus (positive / mixed
   / negative). Report the split as raw counts, not percentages — the
   sample is too small for percentages to be honest.
6. **Flag unresolved questions** — places where twins clearly wanted
   more info, contradicted themselves, or where the stimulus didn't
   land clearly enough to draw a conclusion.

---

## STEP 4 — Return the readout

Use this exact structure:

```
# Focus group readout — <FG name>, <org>
Participants: <N twins> · Stimuli: <M> · Rounds: <R>

## TL;DR
3–5 sentences capturing the overall read. What did the group broadly
believe? Where was there real disagreement? What's the biggest signal
for the decision this FG was meant to inform?

## Consensus — what the group agreed on
Bulleted list. Each bullet: one claim, then in parens the count of
twins who supported it (e.g., "Price feels too high (5 of 6)"). Only
include items with clear majority backing.

## Disagreements — where the group split
For each real split:
- **The question / stimulus:** <what they were reacting to>
- **Side A (<count>):** <twin names> — <their position, 1–2 sentences>
- **Side B (<count>):** <twin names> — <their position, 1–2 sentences>
- **Why the split matters:** 1 sentence on the decision implication.

## Sentiment breakdown
Per stimulus, raw counts:
- Stimulus 1: <N positive> / <N mixed> / <N negative>
- Stimulus 2: ...
(Only include stimuli where sentiment was actually captured.)

## Standout quotes
3–5 direct quotes, each attributed to a specific twin and stimulus.
Preserve the twin's voice and phrasing.
> "quote" — <twin name>, on <stimulus>

## Unresolved — worth a follow-up
Bulleted list of questions the FG raised but didn't answer. These are
candidates for a targeted follow-up interview via `/august-interview`.

## Source
focus_group_id, org, participants list (names + ids), so the user can
trace back.
```

If the raw results are thin (short answers, low engagement, twins
staying vague), say so at the top and note that a re-run with tighter
stimuli might help — do not inflate weak signal into strong claims.

---

## Quick reference — when to ask vs. proceed

| Situation | Action |
|---|---|
| User gave an FG id or exact name | Proceed |
| User described the FG loosely, one clear match | Proceed |
| Multiple FGs match description | **ASK** with top candidates |
| No FG matches | Tell the user; do not fabricate; do not start a new one |
| FG has finished, results are rich | Full readout |
| FG has finished but results are thin | Deliver readout + honest thinness note |
| FG hasn't finished / no results | Stop; report status back |
