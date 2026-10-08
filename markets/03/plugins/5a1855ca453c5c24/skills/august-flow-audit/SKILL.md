---
name: august-flow-audit
description: >
  Walk August twins through a proposed onboarding, checkout, signup, or
  funnel step-by-step and surface friction points before we ship.
  Screenshots, Figma frames, or step descriptions are attached as focus
  group stimuli one step at a time; twins call out where they'd get
  confused, hesitate, or drop off. Pre-launch, twin-simulated version of
  the friction points Commerce Graph measures post-launch. Triggers on:
  "audit this flow", "walkthrough with twins", "onboarding friction check",
  "test this funnel with twins", "friction check", "flow audit",
  "/august-flow-audit".
---

# August Flow Audit

Walk twins step-by-step through a proposed flow and produce a per-step
friction report plus a top-3 overall list. Tools under
the August MCP.

**When to use:** the user has an ordered flow (onboarding, checkout,
signup, quiz, guided-shopping funnel, dashboard first-run) and wants
friction signal before shipping.

**When NOT to use:**
- Single screen or artifact → `/august-feedback`.
- Comparing variants of the same screen → `/august-concept-compare`.
- Text/microcopy only → `/august-feedback` for one version or
  `/august-concept-compare` for multiple versions.
- Already-shipped flow with live traffic → skip this and pull the real
  friction points from Commerce Graph.

**Core rule:** the flow order MATTERS. Twins react to step N with step
N-1's context in their head. Never scramble the order and never merge
steps into one stimulus batch — the whole point is step-by-step signal.

---

## STEP 1 — Confirm the flow

Before any MCP call, be clear on:

- **Ordered list of steps** — screenshots, Figma frame URLs, or written
  descriptions. Cap at ~8 steps per audit; if longer, chunk into two
  audits (e.g., "onboarding" and "first-purchase").
- **What is this flow FOR?** (new-user onboarding, checkout, guided
  quiz-to-recommendation, dashboard first-run, etc.)
- **Who is the target user?** (first-time visitor, returning buyer,
  internal dashboard user, etc.)
- **What's the desired end state?** (completed purchase, activated
  account, added product to cart, etc.)

Missing any → ASK. A flow audit without a stated goal produces
directionless friction complaints.

---

## STEP 2 — Pick the organization

Call `list_organizations`. Map audience → org:

- Consumer flow (checkout, funnel, onboarding on a brand site) → brand
  org.
- Internal flow (Fermat dashboard first-run, admin setup wizard, August
  research-builder onboarding) → Fermat org.

If unclear, ASK.

---

## STEP 3 — Start the focus group

Use a focus group, not single-twin — friction signal wants diversity. Call
`list_focus_groups` for the org and select an existing ready group whose
configured panel matches the target user. Then call `start_focus_group` with
its `focus_group_id`. The MCP cannot create a group or choose its panel; if
no suitable ready group exists, ask the user to configure one in August.

Keep this focus group open across every step. Do NOT end it between
rounds — the twins' running memory of prior steps IS the signal.

---

## STEP 4 — Run the walkthrough, step by step

For each step in order:

1. For a Figma URL, attach it with `add_focus_group_stimuli`. For a screenshot
   description or text step, include the full labelled artifact directly in
   the round question; the stimuli tool accepts only Figma URLs.
2. `run_focus_group_round` with a friction-focused prompt:

   > This is step [N] of [total]: [step name]. Imagine you just came from
   > the previous step. React honestly:
   > - Where would you get confused here?
   > - Where would you hesitate, second-guess, or want to go back?
   > - Where might you drop off entirely?
   > - What would you expect to happen next?

3. Optionally, on complex steps, run a second `run_focus_group_round`
   asking each twin to score friction 0–3 on that step (0 = smooth, 3 =
   would abandon) — this gives a rough severity anchor.

After the last step:

- `end_focus_group`
- `get_focus_group_results` for the full transcript across all rounds.

---

## STEP 5 — Synthesize into a friction report

Do NOT dump transcripts. Return this template:

```
## Flow Audit: [flow name]
Audience: [org] · Twins: [N] · Goal state: [end state]

### Per-step friction report

**Step 1 — [name]**
- Top friction points:
  - [point 1 — one line]
  - [point 2 — one line]
- Standout quote: "[verbatim from a twin]" — [twin name]
- Severity: **[low / med / high]**
- Suggested fix: [one line — concrete change, not vibes]

**Step 2 — [name]**
- ...

(repeat per step)

### Top 3 friction points overall
1. **[step + issue]** — [why it matters + severity]
2. **[step + issue]** — [...]
3. **[step + issue]** — [...]

### Cross-step patterns
- [e.g., "twins repeatedly forgot what step 2 asked them, suggesting
  progress indicator is under-weight" — patterns visible only across
  steps, not within a single step]

### Post-launch note
Worth running a real Commerce Graph friction-points check on this flow
after ship — the twin signal above is directional, not measured. Compare
the top-3 twin frictions against actual drop-off funnels once live traffic
accrues.

### Source
Focus group [name/id], org [name], twins [names]
```

Severity guidance:
- **High** — twin explicitly said they'd bounce, or multiple twins hit
  the same wall.
- **Med** — twin hesitated / had to re-read / needed to guess.
- **Low** — nit or preference, not a blocker.

If any step's signal was thin (twins just said "looks fine"), SAY SO —
don't pad. Suggest re-running with a different twin composition or a more
specific prompt.

---

## Quick reference

| Situation | Action |
|---|---|
| Ordered flow with 3–8 steps + clear goal | Proceed |
| >8 steps | Chunk into 2 audits, run separately |
| Single screen | Redirect to `/august-feedback` |
| Already-shipped flow with traffic | Pull real Commerce Graph friction points instead |
| Twin signal thin on a step | Note it; offer to re-run with different panel |
