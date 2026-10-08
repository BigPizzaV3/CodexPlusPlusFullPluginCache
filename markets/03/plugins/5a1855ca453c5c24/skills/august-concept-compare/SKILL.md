---
name: august-concept-compare
description: >
  Run the same concept, design, or copy past August twins across two or more
  variants (A/B/C/D) and return a side-by-side comparison instead of one
  twin's take at a time. Use whenever the user has multiple candidate
  concepts and wants twin-simulated preference signal before committing —
  landing page variants, packaging concepts, positioning angles, hero
  designs, pricing framings, ad creatives. Different from /august-feedback
  (single artifact). Also handles text-only variants (headlines, CTAs,
  taglines) — hard-scope output to phrase-level notes in that case. Triggers
  on: "compare these concepts", "A/B test with twins", "which variant do
  twins prefer", "run these variants past twins", "concept test",
  "/august-concept-compare".
---

# August Concept Compare

Compare 2–4 variants of the same concept across August twins and return a
matrix of reactions plus a recommended winner. Tools live under
the August MCP.

**When to use:** the user has multiple candidate concepts and wants relative
preference signal (which is stronger, and why).

**When NOT to use:**
- Only one concept exists → use `/august-feedback` instead.
- User wants step-by-step friction on a flow → use `/august-flow-audit`.

**Text-only variants (headlines, CTAs, taglines, body copy):** still use this
skill, but hard-scope the output to phrase-level notes — comment only on
wording, not on layout, imagery, or design drift. Flag any design/layout
observations that surface anyway as "out of scope — worth a full concept
test?" rather than including them in the main matrix.

**Core rule:** if the org, the audience, or the comparison format is
unclear, ASK once. Don't silently pick — mis-routed comparisons are worse
than mis-routed single feedback because they influence a choice.

---

## STEP 1 — Confirm the variants + audience

Before any MCP call, be clear on:

- **How many variants?** (2, 3, or 4 — cap at 4; more than that dilutes
  signal.)
- **What form?** Text, image/screenshot, Figma link, full page mock?
- **What are they variants OF?** A hero section, an entire landing page,
  a pricing card, a value prop, a packaging design, etc.
- **What audience should judge?** Brand shopper twins (consumer artifact)
  or Fermat-org dashboard-user twins (internal tool)?

If any of these are missing, ASK. Ask the user for closed choices
(2–4 options); prose otherwise.

---

## STEP 2 — Pick the organization

Call `list_organizations`. Then match audience → org:

| Artifact | Likely org |
|---|---|
| Consumer landing page, DPP, ad, packaging, pricing | Brand org (GNC, Backcountry, etc.) |
| Fermat/August dashboard UI, admin tooling, internal workflow | Fermat org |

If the user named a brand or audience, resolve directly. If ambiguous, ASK
with `list_organizations` results as options.

---

## STEP 3 — Pick the comparison format

Three viable shapes. Default to (B) unless the user signals otherwise.

**(A) Single twin sees all variants (one interview)**
- Best for: tight cost, quick gut check, one strong-fit persona.
- Method: pick 1 twin via `list_twins`, call `start_interview(twin_id)`, then
  call `ask_question(interview_id)` once per variant with matching framing
  and the artifact in `design_context`. Do NOT reveal that other variants
  exist until the final preference question.

**(B) One focus group sees all variants together — DEFAULT**
- Best for: real A/B/C preference signal with diversity.
- Method: use `list_focus_groups` to select an existing ready group, then
  `start_focus_group`. Attach Figma variants with `add_focus_group_stimuli`;
  for text or described-image variants, include the labelled artifacts in
  the round question instead. Run the reaction round, then a preference
  round, then `end_focus_group` → `get_focus_group_results`. If no suitable
  ready group exists, ask the user to configure one in August or use (A).

**(C) One focus group per variant (parallel groups)**
- Best for: when priming across variants would contaminate reactions
  (e.g., strongly branded concepts where seeing variant B changes how you
  read variant A).
- Method: use N existing ready groups with matched twin composition, one per
  variant. The MCP cannot create groups or select their panels. If those
  groups do not exist, use (A) or ask the user to configure them in August.

If the user didn't specify, ASK which shape — offer A/B/C as options.

---

## STEP 4 — Run it

For each MCP call, pass the actual artifact content — the copy text, image
description, Figma frame contents, or pasted screenshot description.
Vague stimuli = vague comparison.

**Prompts to use in the group / interview:**
1. Reaction round: "Here are [N] variants of [artifact]. React to each one
   independently: what stands out, what confuses you, what makes you want
   to click / keep reading / bounce."
2. Preference round: "Now pick the one that would most make you [target
   action — buy, sign up, keep browsing]. Explain why in one sentence."

Retrieve results via `get_focus_group_results` or
`get_interview_transcript` depending on the route.

---

## STEP 5 — Synthesize into a side-by-side matrix

Do NOT dump raw transcripts. Return this template:

```
## Concept Comparison: [artifact name]
Audience: [org] · Format: [single twin / focus group / N parallel groups]
Twins: [names or count]

| Variant | What landed | What didn't | Who preferred it | Why |
|---|---|---|---|---|
| A — [label] | ... | ... | [twin names or count] | [core reason] |
| B — [label] | ... | ... | ... | ... |
| C — [label] | ... | ... | ... | ... |

### Recommended winner: **Variant [X]**
- **Why it wins:** [1–2 sentence synthesis of the strongest signal]
- **Tradeoff to know:** [what it loses vs. runner-up — every winner has one]
- **Suggested next move:** [ship as-is / merge X's headline + Y's visual /
  re-test with tighter audience / etc.]

### Source
[Focus group name(s) or twin name(s), org, dates]
```

If signal is thin, tied, or contradictory across twins, SAY SO explicitly
in the "Recommended winner" section — don't force a call. Offer to re-run
with a different format (e.g., swap to parallel groups) or a different
audience.

---

## Quick reference

| Situation | Action |
|---|---|
| 2–4 concrete variants + clear audience | Proceed with default (B) |
| Only 1 variant | Redirect to `/august-feedback` |
| Text-only variants | Proceed, but hard-scope output to phrase-level notes |
| Variants strongly primed / branded | Ask about (C) parallel groups |
| Org or audience unclear | ASK once, then proceed |
