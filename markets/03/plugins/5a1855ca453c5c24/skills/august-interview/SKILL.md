---
name: august-interview
description: >
  Run a structured 1:1 interview with a single August twin off a discussion
  guide (a list of questions or topics the user provides), and return a
  clean synthesized write-up instead of raw back-and-forth. Use when the
  user wants depth on one persona and does NOT want to read the full
  transcript themselves. Triggers on: "interview a twin", "structured
  interview", "run a discussion guide", "walk a twin through these
  questions", "1:1 twin interview", "/august-interview".
---

# August Interview

Drive a structured 1:1 interview with a single August twin using a
discussion guide, then hand back a clean write-up. Tools live under
the August MCP.

**When to use:**
- User has a list of questions/topics they want walked through with one twin
- User wants depth on a single persona (not a range of reactions)
- User explicitly does not want to read the full transcript

**When NOT to use:**
- User wants varied reactions across personas → use focus group tooling
- User wants a single gut-check reaction → use `/august-feedback`
- User just wants to find the right twin → use `list_organizations` and
  `list_twins` directly

**Core rule:** if org, twin, or the discussion guide itself is unclear, ASK
before calling any tool. Better one clarifying question than an interview
with the wrong persona off the wrong questions.

---

## STEP 1 — Confirm the discussion guide

Before touching August, make sure you have:

- A concrete list of questions or topics (the "discussion guide")
- A rough sense of interview depth per question (one probe, or several
  follow-ups?)
- The intended audience for the twin (which org / persona type)

If the user pasted a wall of text, extract the questions into an ordered
list and mirror it back for confirmation. If the guide is vague ("ask them
about pricing"), ASK for the actual questions — do not invent them.

---

## STEP 2 — Pick the organization

The August MCP is org-scoped. Every twin belongs to an org.

1. If the user named a brand or audience (GNC, Backcountry, Fermat
   dashboard user), match to an org via `list_organizations`.
2. If they haven't, infer from the discussion guide: consumer-facing
   questions → brand org; internal/dashboard/workflow questions → Fermat
   org.
3. If ambiguous, ask the user with 2–4 candidate orgs pulled from
   `list_organizations`. Do not guess.

---

## STEP 3 — Pick the specific twin

Call `list_twins` for the chosen org.

- Match twin traits to the discussion guide's target persona.
- If exactly one twin clearly fits, proceed.
- If 2+ twins reasonably fit, ask the user with the top 2–3
  candidates and one-line summaries. Never silently pick.

Record the selected `twin_id` for the interview call.

---

## STEP 4 — Start the interview and loop the guide

1. Call `start_interview` with the selected `twin_id` and save the returned
   `interview_id`.
2. For each question in the discussion guide, call `ask_question` with that
   `interview_id`. Include the discussion framing in the first question and
   preserve the guide order.
3. If a response is thin or dodges the question, follow up with ONE
   clarifying `ask_question` before moving on. Do not spiral — the goal
   is coverage of the full guide, not exhaustive probing on one item.
4. Once every guide question has been asked (and any needed follow-ups are
   done), call `get_interview_transcript` with the interview ID as
   `conversation_id` to retrieve the full record.

Pass the actual artifact (copy, screenshot description, product details)
when a question references one. Vague prompts produce vague answers.

---

## STEP 5 — Synthesize the write-up

Do NOT return the raw transcript. Return this structured format:

```
# Interview write-up — <twin name>, <org>

## TL;DR
2–3 sentence overall read on the twin's stance across the guide.

## Per-question responses
For each question in the original guide order:

### Q1 — <the question, verbatim>
- **Summary:** 1–3 sentences capturing the twin's answer.
- **Key points:** 2–4 bullets of the specific things they said.
- **Confidence / hedging:** note if they hesitated, hedged, or were firm.

(Repeat for each guide question.)

## Cross-cutting themes
Patterns that showed up across multiple questions (e.g., recurring
concern about price, recurring positive on brand trust).

## Surprises
Anything the twin said that you did not expect given the persona
profile — worth flagging to the user.

## Verbatim quotes
3–6 short direct quotes from the transcript, attributed with the
question they came from. Preserve tone and phrasing exactly.

## Source
Twin name + twin_id + org + interview id, so the user can trace back.
```

If the transcript came back thin, off-topic, or the twin refused
questions, say so explicitly at the top of the write-up and offer to
re-route to a different twin.

---

## Quick reference — when to ask vs. proceed

| Situation | Action |
|---|---|
| Discussion guide is concrete | Proceed |
| Discussion guide is vague ("ask about X") | **ASK** for the actual questions |
| Org is named or obvious | Proceed |
| Org is unclear | **ASK** from `list_organizations` |
| One twin clearly fits | Proceed |
| 2+ twins fit | **ASK** with top 2–3 candidates |
| Twin dodges one question | Follow up once, then move on |
| Twin dodges most questions | Stop, flag, offer to re-route |
