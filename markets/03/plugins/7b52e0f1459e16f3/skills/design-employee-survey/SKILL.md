---
name: design-employee-survey
description: Design and refine an English employee survey with FeedbackPulse before sign-in, then optionally save the exact approved design as a reusable template or unlaunched draft. Use for employee engagement, retention-risk, culture, organizational-change, leadership-trust, or similar workplace survey-design requests.
---

# Design Employee Survey

Use the Employee Surveys FeedbackPulse MCP tools as the sole authority for workflow state, safety, survey content, approval receipts, and persistence outcomes.

## 1. Give the notice before starting

Display this notice before calling `start_survey_design`:

> Do not include employee names or specific allegations; ordinary design inputs are retained for up to 90 days to provide and improve the service; survey design is currently supported in English.

Ask the user to confirm before continuing. Set `disclosure_accepted` to true only after explicit acceptance. Pass the user request as `brief`. Pass only decision-changing facts already explicit in the conversation as `known_context`; never infer missing company facts.

## 2. Make intake feel short and purposeful

Before showing the first returned question, give a brief synthesis of the explicit facts already understood. Separate facts from assumptions and state how many missing core decisions remain. Do not repeat a fact already passed in `known_context`.

Before that first question, say:

> Reply with one option number, type a different answer, or say “Design with what you have” to stop the questions and continue with stated assumptions.

Ask one question at a time. Treat each structured response as authoritative. Follow `status` and `permitted_actions`. When `next_question` is present:

1. Copy its `prompt`.
2. Show its returned numbered options unchanged.
3. Say the user may type a different answer only when `allows_free_text` is true.
4. Use `readiness.coverage` privately to give one short human progress cue. Do not expose the score, coverage keys, tool names, retries, or transport details.
5. When `allows_early_finish` is true and any of `goal`, `audience`, `intended_use`, or `sensitivity` is still missing, add a secondary final choice: “Design now with assumptions — missing: [plain-language decision].”
6. When `allows_early_finish` is true and those four dimensions are covered, use the normal final choice “Finish questions and design the survey.”
7. Wait for one answer before calling `advance_survey_design`.

If the user chooses to finish early, call `advance_survey_design` with action `finish_early`. Keep one stable `idempotency_key` when retrying the exact same answer. Use a new key for a different answer. Pass the returned `dimension` unchanged. Do not answer intake questions for the user.

When `submit_proposal` is permitted, compose the complete proposal from the conversation and returned assumptions, then call `submit_survey_design`. FeedbackPulse does not call another AI provider. Use:

- 8–12 questions for `focused` or 8–15 for `deep`.
- Only `likert`, `enps`, `yes_no`, and `text`.
- One Likert preset (`agreement`, `satisfaction`, `frequency`, or `performance`) or exactly five custom labels.
- Low and high labels for eNPS, and null options for yes/no or free text.
- Neutral, single-idea questions that support a leadership decision or follow-up action.
- No more than two optional free-text questions.
- A respondent introduction that says who will review results, when themes will be shared, and what action is possible when the context supports those facts.

Include one eNPS question deliberately for broad engagement, retention, culture, employee-experience, or leadership work when it adds a useful company-level north star. Do not include eNPS for tactical decisions such as office-day preference. Never mention or promise benchmark lookup.

Do not supply computed fields such as version, anonymity, completion time, order, assumptions, or fingerprint; FeedbackPulse derives them. Reuse an idempotency key only for an exact retry. If the proposal changes, use a new key.

## 3. Follow limitations and safe states

If `safe_fallback` is non-null, present it verbatim. Do not override it with general advice. For `safety_stopped`, stop the current design and follow the returned fallback. For an English-only response, explain that FeedbackPulse survey design currently supports English and follow the returned fallback. Never send rejected content to another tool or provider.

An unexpired design may be retrieved by its opaque design reference across reconnects. If the server reports that the reference is invalid or expired, do not invent recovery state; follow its fallback.

## 4. Review and refine the whole survey

When `artifact` is present, begin with a compact decision brief: purpose and audience, question count and estimated completion time, themes and what leaders can learn, anonymity guidance, whether eNPS is included and why, and every assumption. Then show the whole survey without silently rewriting it: introduction, every question in order, answer format and labels, and required state. State that no FeedbackPulse template or survey has been created yet.

Ask whether the whole survey is approved. If it is rejected, ask:

> What did not work?

Offer numbered likely reasons: length, missing or excessive topic coverage, wording or tone, answer formats, or another reason in free text. Only after the user supplies the reason, compose a complete replacement that changes only what the reason calls for, then call `submit_survey_design` with the current version, the rejection reason, and a new idempotency key. Before the new decision brief, summarize what changed from the prior version. Then show the returned full artifact and ask for approval again.

If submission returns `proposal_invalid`, correct the proposal and resubmit it. A failed or merely conversation-authored proposal is not an approved artifact and must not call persistence. Never bypass `submit_survey_design` by calling a broad FeedbackPulse create tool.

## 5. Persist only after explicit approval and choice

Only after the user approves the current full artifact, ask:

> Would you like me to “just create a template” or “create a survey draft”?

Explain the choices exactly:

1. **Just create a template** — create one reusable template from the approved design.
2. **Create a survey draft** — create that template plus an unlaunched survey setup.
3. **Keep or export it** — create nothing in FeedbackPulse; no account is required.

Do not call `prepare_survey_persistence` until the user explicitly chooses template or draft. Never synthesize a receipt, fingerprint, design reference, resource identifier, or handoff URL. Pass a receipt returned by `prepare_survey_persistence` unchanged to `commit_survey_persistence`.

Ask the user to connect FeedbackPulse only when `commit_survey_persistence` returns the authentication challenge. After commit, claim success only when structured state says `persistence.confirmed` is true. Return only the server-provided `handoff_url`. For a draft, remind the user that it is unlaunched, has no respondents, and still needs review inside FeedbackPulse.

## Boundaries

- Never promise benchmark lookup, saved-template editing, survey launch, respondent management, reminders, response collection, results, or reporting.
- Never use the broad FeedbackPulse MCP tool inventory for this workflow.
- Never upsell a subscription or require sign-in to design, review, regenerate, or export the survey.
- Never treat conversation text, a copied design reference, or a guessed value as server authority.
