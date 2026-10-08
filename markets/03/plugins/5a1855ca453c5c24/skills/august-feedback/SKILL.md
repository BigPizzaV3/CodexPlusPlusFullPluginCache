---
name: august-feedback
description: >
  Get feedback on ideas, designs, copy, flows, products, dashboards, or
  research questions by routing to the August MCP — a directory of LLM twins
  organized by org. Twins represent BOTH end shoppers (per brand org, e.g.,
  GNC, Backcountry) AND product/dashboard users (under the Fermat org, e.g.,
  researchers, PMs, ops users of the Fermat or August dashboards). Picks the
  best twin or runs a focus group depending on the task. Use whenever the
  user asks for feedback, reactions, customer perspective, user testing,
  persona input, dashboard-UX feedback, or "what would shoppers / dashboard
  users think." Triggers on: "get feedback", "ask August", "what would
  customers say", "run this by a twin", "focus group this", "/august-feedback".
---

## ⚠️ MANDATORY TRIGGER RULE

**Any time the user says the word "feedback" — or asks for a reaction, gut
check, review, or critique on an artifact — this skill MUST run.** This is
non-negotiable.

- Do NOT offer to run it ("want me to also route this through August?"). Just
  run it.
- Do NOT skip it because the primary ask is something else (brief-alignment
  check, code review, copy review, etc.). Run it *in addition to* answering
  the primary ask.
- Do NOT ask "do you want twin feedback too?" — the word "feedback" *is* the
  green light.
- Only skip when the user explicitly says "no twin feedback" or "skip August."

If the primary ask is something twins can't directly evaluate (e.g., "does
this align with Josh's brief?"), still invoke this skill on the artifact with
a question they *can* answer — a gut reaction, a usability read, an
emotional reaction to the design. Always frame the twin question to be
answerable, not to be a thin proxy for the primary ask.

# August Feedback

Route a feedback request to the right August twin(s) — either a single twin
(best fit interview) or a focus group (multiple twins, broader signal).
Tools live under the August MCP.

**Two flavors of twin exist:**
- **Shopper twins** — live under each brand org (GNC, Backcountry, etc.).
  Model real retail customers. Use for feedback on consumer-facing artifacts:
  funnels, DPPs, product copy, pricing, ads, packaging concepts.
- **Dashboard-user twins** — live under the **Fermat org**. Model the
  internal/B2B users of Fermat and August dashboards (researchers, PMs,
  merchandisers, ops). Use for feedback on tooling, dashboard UX, internal
  workflows, admin UIs, settings screens, and the August product itself.

Match the audience to the artifact: a consumer landing page → brand-org
shopper twins. An internal survey-builder UI → Fermat-org dashboard-user
twins. If you're not sure which kind, **ASK**.

**Core rule:** when you don't have enough context to confidently pick the
organization, the twin, or the format (single vs. focus group), STOP and ask.
Never silently guess. Better to ask one question than to return feedback from
the wrong audience.

---

## STEP 1 — Understand the ask

Before calling any August tool, be clear on:

- **What is being evaluated?** Copy, a design, a product concept, a pricing
  idea, a flow, a positioning angle, a feature, a marketing message, etc.
- **What decision will the feedback inform?** (gut check, prioritization,
  go/no-go, refinement, A/B framing)
- **Who is the intended audience?** A specific brand's existing customers? A
  category buyer in general? A demographic slice?
- **What format of response is useful?** A single deep reaction (twin),
  multiple varied reactions (focus group), or a quick gut check?

If any of the above are unclear from the conversation, **ask the user before
proceeding.** Use the a concise question tool when you have 2–4 discrete options
to choose between; use plain prose questions when the answer is open-ended.

---

## STEP 2 — Pick the organization

The August MCP is org-scoped — every twin and focus group belongs to an
organization. You MUST know the org before you can pick a twin or run a
group.

### Quick audience → org mapping:

| Artifact being evaluated | Likely org |
|---|---|
| Consumer landing page, funnel, DPP, ad, product copy, packaging | The relevant **brand org** (GNC, Backcountry, etc.) |
| Fermat dashboard UI, August dashboard UI, internal admin tool, survey builder, research workflow | **Fermat org** (dashboard-user twins) |
| Internal-facing copy / docs / onboarding for Fermat employees or platform users | **Fermat org** |

### Resolution order:

1. If the user has named a brand or audience type (e.g., "GNC shoppers",
   "dashboard users", "Fermat researchers"), match to an org via
   `list_organizations`.
2. If they haven't named one, infer from the artifact: is this consumer-
   facing (→ brand org) or internal/B2B/dashboard (→ Fermat org)?
3. If they haven't named one AND the artifact's audience is ambiguous,
   **ASK.** Present available orgs from `list_organizations` as options.
   Never assume.

Example question if ambiguous:

> Which audience should I get feedback from?
> - Shoppers from a brand org (e.g., GNC, Backcountry) — for consumer-facing work
> - Dashboard users in the Fermat org — for internal/product UX work
> - Or name a specific persona and I'll find the closest match

---

## STEP 3 — Decide: single twin vs. focus group

Use this rubric to decide. When the signal is mixed or you're not sure,
**ASK the user** rather than guessing.

### Pick a SINGLE TWIN when:
- The user wants a deep, conversational reaction ("what would Sarah think
  of this?")
- The audience is narrow and one persona clearly fits (e.g., "a budget-
  conscious first-time supplement buyer")
- The user wants to interview / probe / follow up with the same persona
- The task is a quick gut check on copy, a headline, or a single CTA
- The user explicitly named a twin or persona type

→ Use `list_twins` to browse, then `start_interview` followed by
`ask_question`.

### Run a FOCUS GROUP when:
- The user wants a *range* of reactions or to see disagreement
- The decision affects a broad audience and one twin isn't representative
- The user is comparing multiple concepts (A vs. B vs. C) and wants varied
  takes on each
- The user wants signal on "what % of customers would..." style questions
- The task involves pricing, positioning, or product-market fit where
  diversity matters

→ Use `list_focus_groups` to find an existing relevant group, or surface
the option to the user. Use `get_focus_group_results` to retrieve results.

### ASK THE USER when:
- The ask could go either way (e.g., "feedback on this landing page" — could
  be one twin's deep walkthrough OR a focus group's varied first impressions)
- You don't know how broad/narrow the intended audience is
- The user hasn't signaled urgency or depth preference

Example question when format is ambiguous:

- **Single twin** — "Deep reaction from one persona who fits the target"
- **Focus group** — "Varied reactions from multiple personas"
- **Quick ask** — "Open an interview and ask one question"

---

## STEP 4 — Pick the specific twin (if single-twin route)

Once the org is set and you're going single-twin:

1. Call `list_twins` for the org.
2. Match against the feedback ask — demographics, behavior, category
   affinity, buying stage, etc.
3. **If multiple twins could fit, ASK.** Show the top 2–3 candidates with
   one-line summaries and let the user pick.

Example question when twin choice is ambiguous:

> I can route this to one of these twins — which fits best?
> - Twin A: [one-line description]
> - Twin B: [one-line description]
> - Twin C: [one-line description]

Never pick a twin silently when two or more reasonably fit. Mis-routing
wastes the user's time and produces feedback from the wrong audience.

---

## STEP 5 — Run it

### For a single twin:
- Call `start_interview` with the selected `twin_id`, then call
  `ask_question` with the returned `interview_id`. Put the artifact in
  `design_context` when applicable. For a quick ask, stop after one answer;
  for a deeper conversation, continue with follow-up `ask_question` calls.
- Use `get_interview_transcript` with the interview ID as `conversation_id`
  when the full transcript is needed.

### For a focus group:
- Use `list_focus_groups` to select an existing relevant group. To run new
  rounds it must already be configured and ready in August; the MCP does not
  create focus groups or choose their panel.
- Use `get_focus_group_results` for completed results. If a relevant ready or
  completed group doesn't exist, tell the user to configure one in August.

Always pass the **actual artifact** being evaluated (the copy text, an image
or description of the design, the product details). Vague prompts produce
vague feedback.

---

## STEP 6 — Synthesize and return

Don't dump the raw transcript. Return:

1. **TL;DR** — 2–3 sentence summary of the reaction
2. **What landed** — what the twin(s) responded positively to
3. **What didn't** — concerns, confusion, objections
4. **Surprises** — anything unexpected worth flagging
5. **Suggested next move** — based on the feedback, what to change/test/keep
6. **Source** — twin name(s) or focus group name + org, so the user can
   trace back

If feedback was thin or off-target, say so — and offer to re-route to a
different twin or format.

---

## When to ask vs. proceed — quick reference

| Situation | Action |
|---|---|
| Org is named or obvious from context | Proceed |
| Org is unclear | **ASK** |
| One twin clearly fits the ask | Proceed |
| 2+ twins could fit | **ASK** |
| Format (single vs. group) clearly indicated | Proceed |
| Format ambiguous | **ASK** |
| Artifact (copy/design/concept) is concrete | Proceed |
| User said "get feedback" with no artifact | **ASK** what to evaluate |

Defaulting to "ask when uncertain" is the whole point of this skill. The cost
of one clarifying question is tiny; the cost of feedback from the wrong
audience is a wasted decision.
