---
name: feedback-loops
description: >
  Run an iterative feedback loop with August twins: put the same artifact
  (copy, design, concept, variant set) in front of a panel of twins round
  after round, applying the top suggestion from each round as a new variant,
  until the responses converge on a preferred direction. Auto-invokes
  /fix-question when a twin response is vague or hedged and re-asks that
  twin with a sharper prompt. Meta-skill that orchestrates other August
  skills so you don't have to manually kick each round. Triggers on: "run
  a feedback loop", "iterate feedback with twins", "keep iterating until",
  "loop twins on this", "converge on a variant", "/feedback-loops".
---

# Feedback Loops

Orchestrate an N-round twin panel: same question, same twins, evolving
artifact, until responses converge. Tools live under
the August MCP. This skill calls out to `/fix-question` for
sharpening prompts mid-loop.

> **Wall-clock note:** each round makes one MCP call per twin plus any
> rephrase retries. Expect **several minutes per round**. Let the user know
> up front so they don't ctrl-C mid-run.

---

## When to use

- User wants to converge on the best variant of copy / a headline / a
  concept, not just get a one-shot reaction.
- User has an explicit stopping condition ("until 4 of 5 twins pick the
  same variant", "until reactions stabilize").
- User is willing to wait multiple rounds.

## When NOT to use

- Single-round gut check → `/august-feedback`.
- Deep 1:1 discussion guide → `/august-interview`.
- Comparing pre-existing variants without iteration → `/august-concept-compare`.

---

## STEP 1 — Nail the inputs

Confirm you have:

- **Artifact** — the concrete copy, design description, concept, or
  variant set being tested. If vague, ask.
- **Convergence criterion** — the explicit stopping rule. Common shapes:
  - "≥ K of N twins pick the same variant"
  - "responses stabilize (no new objections in a round)"
  - "top objection from round 1 is resolved"
- **Org + twin panel** — which org and which twins are on the panel. If
  the user hasn't picked, use `list_organizations` + `list_twins` and
  propose a 3–5 twin panel matching the target audience.

**Hard cap: 4 rounds.** State this to the user at kickoff.

---

## STEP 2 — Round 1 (baseline)

For each twin in the panel:

1. Call `start_interview` with its `twin_id` and retain the returned
   `interview_id` for every round.
2. Call `ask_question` with that `interview_id`, the question, and the
   artifact in `design_context` when applicable.
3. Capture the answer directly; call `get_interview_transcript` with the
   interview ID as `conversation_id` only when the full thread is needed.

Reuse the same interview IDs in later rounds so each twin retains context.

Record for each twin: preferred variant (if applicable), top suggestion,
top objection, one-line summary.

---

## STEP 3 — Detect weak responses and repair

After each round, scan every twin response for:

- Vagueness ("it's fine", "I guess it works")
- Hedging without content ("kind of", "maybe", "depends")
- Off-topic drift (twin answered a different question)
- Missing the concrete artifact (twin talked in generalities)

For any twin whose response fails this check:

1. Invoke `/fix-question` internally with the original question. The skill
   returns a sharper rewrite.
2. Re-ask that twin using `ask_question` with the same `interview_id`.
3. Replace the weak response with the repaired one.
4. Cap re-asks at **1 per twin per round** — if it still comes back weak,
   note "twin response remained thin" and move on.

---

## STEP 4 — Convergence check + next-round variant

After every round, evaluate:

- Does the panel meet the user's convergence criterion? → **STOP**, go to
  STEP 5.
- Are we at round 4? → **STOP** with "hit hard cap without convergence".
- Otherwise → mint the next variant:
  - Cluster the top suggestions from this round.
  - Apply the highest-signal suggestion (most twins raised it, or the
    strongest single suggestion) to produce a new variant of the artifact.
  - Announce the change in the round trace ("Round 3 variant: shortened
    headline per twin B's suggestion").
- Loop back to STEP 2 with the new variant.

Do NOT silently change more than one dimension per round — one variable
per round keeps the signal clean.

---

## STEP 5 — Return the trace

Output structure:

```
# Feedback loop — {artifact name}

*Panel:* {twin A}, {twin B}, … from {org}
*Convergence criterion:* {criterion}
*Rounds run:* {N} of 4
*Outcome:* {converged | hit cap | stopped early}

## Round-by-round

### Round 1 — baseline
- Variant: {description of artifact}
- Responses:
  - {twin A}: {one-line takeaway}
  - {twin B}: …
- Top suggestion applied to next round: {suggestion}

### Round 2 — {what changed}
…

## Final winner
{variant description}

## Convergence commentary
{2–4 sentences on how the panel moved across rounds — what shifted, what
stayed stable, whether the panel actually agreed or just fatigued}

## Suggested next move
{one line — ship it, run another loop with a fresh panel, escalate to a
focus group, etc.}
```

---

## Output rules

- Always show the round-by-round trace, not just the final winner — the
  journey is the signal.
- Be honest about non-convergence. "Panel did not converge; twin B held
  out on X" is more useful than a forced consensus.
- Never fabricate a round. If a twin didn't respond or the MCP call failed,
  say so in the trace.
- If `/fix-question` had to be invoked, note it inline: "(re-asked with
  sharpened prompt)".
