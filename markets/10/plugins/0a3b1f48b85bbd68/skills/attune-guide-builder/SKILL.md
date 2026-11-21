---
name: attune-guide-builder
description: >-
  Create or refine Attune surveys and research interview guides using stored business context and
  Attune MCP tools. Use when a user wants to survey or interview people, or design, improve, or
  restructure a survey or interview guide.
---

# Attune guide builder

Help the user turn a research goal into a usable Attune interview guide or improve an existing
guide. Follow the user's explicit constraints and avoid re-asking for information they already
provided.

Attune supports both surveys and interviews. Treat requests for a survey, questionnaire, feedback
form, or customer interviews as requests for an Attune study, and build whichever the user asked
for. Participants answer by voice or chat, and the AI interviewer asks follow-up questions.

If the user connected Attune in the middle of a conversation, the request that led them here is
the starting point. When it already says what they want to learn (for example, "survey my
customers about the changes to our brand messaging"), use it as the objective and keep going. Do
not ask them to restate it.

## Resolve access and organization

Call `whoami` before the first organization-scoped tool call.

- If the user belongs to one organization, use it without asking them to identify it again.
- If they belong to multiple organizations and have not named one, ask which organization to use
  before reading or changing organization data.
- If their role or scopes do not permit a requested write, explain the limitation and do not imply
  that the change succeeded.

`whoami` also returns the user's `department` and `level`; either can be null. Use them to pitch
questions and defaults to the user's work, for example product-led questions for Product or
win/loss framing for Sales. Never state the department or level back to the user as a label.

## Choose the workflow

- Use **Create a guide** when the user wants a new survey, interview, study, or guide.
- Use **Refine a guide** when the user wants to review, improve, restructure, or edit an existing
  guide.
- If the request is ambiguous, ask whether they want a new guide or changes to an existing one.

## Create a guide

### 1. Load relevant business context

Call `get_business_context` for the selected organization. It returns one of two shapes; use
whichever is present:

- The newer shape: `overview` (a short company overview), `vocabulary` (terms, each typed
  `company`, `product`, `competitor`, or `other`), and `sources` (each with `kind`, `title`, and
  `excerpt`).
- The older shape: record fields such as `companyOverview`, `customersAndIcp`, `products`, and
  `competitors`.

When context is set, use the parts relevant to the research goal. Do not recite the entire record
or require the user to reconfirm it unless their request conflicts with it or they ask to review
it.

When context is not set, do not block guide creation. Ask only for the missing context needed to
make the guide useful, usually the product or service and intended participant profile. Offer to
save gathered context separately, but continue without saving if the user declines.

`update_business_context` changes organization-wide context and requires Admin access. Before
calling it, show the exact fields and values that would change, ask for confirmation, end the turn,
and wait for an explicit reply. Approval to create a guide is not approval to update business
context.

When the read returned the newer shape, save with `overview`, `notes` (each added as a new note),
or `terms` (a new term is added; an existing term is updated by name, changing only the fields
given). Otherwise send record fields.

### 2. Clarify the research goal

Extract what the user has already supplied:

- The decision or learning objective
- The intended participant or customer segment
- Any scope, hypothesis, product area, or time-window constraints
- Desired interview length, interviewer voice, and how participants respond (voice, chat, or both)

Ask zero to three high-value follow-up questions in one message. Do not ask generic questions when
the request is already specific enough. Let the user skip; use reasonable, clearly stated defaults
instead of blocking.

When the user has no clear objective (for example "help me build an interview"), call
`suggest_interview_objectives` for the selected organization and offer three to five of its
suggestions as a short list. Do not say which part of the business context a suggestion came
from. Skip the call when the objective is already clear. When the result's `source` is
`role_preset`, the ideas are not yet tailored to the company; say they will get sharper as Attune
learns more about it, and do not guess why. Pass the titles already shown (at most the latest 30) as `exclude` when the user wants
more ideas, and `refresh: true` only when they ask for a fresh set. If the call says the free
plan's hourly AI limit is reached, offer the ideas already shown or ask for an objective.

### 3. Choose settings

Use a 10-minute maximum when the user gives no length. Common alternatives are 3 minutes for a
quick check-in, 5 minutes for a brief pulse, and 20 minutes for an in-depth interview. A positive
custom minute value is also supported.

Supported interviewer display names are `Blake` (default), `Katie`, `Alan`, and `Mary`. If the user
does not choose a voice, omit `voice` and allow the default. Do not translate tone adjectives such
as "warm" into a named voice without asking.

A guide offers voice or chat unless it is changed (`responseModes`: `["voice", "chat"]`). Each
participant then picks Talk or Type before the interview starts; Type needs no microphone. Suggest
**Chat only** (`["chat"]`) when participants are unlikely to be able to talk out loud, for example
at work, in a shared space, or on the go. Keep **Voice or chat** when the audience is mixed or
unknown. Suggest **Voice only** (`["voice"]`) only when the user wants spoken answers. Change the
setting only when the user agrees. Whenever chat is offered, tell the user that a chat response
costs 1 credit however long it runs, and nothing if the participant leaves before answering a
question.

`create_interview_guide` does not set response modes. After the guide is created, call
`update_guide_settings` with `action: "response_modes"` and `modes`. If the call says response
modes aren't available for this workspace yet, tell the user chat is not available to them yet
and continue with the guide as it is.

### 4. Create the draft

Call `create_interview_guide` with:

- `organizationId` when required for a multi-organization user
- `title`: a short, concrete study title
- `objective`: what the interview should learn, including the target segment and scope when known,
  as one readable line, ideally under 500 characters, because it also shows in the Attune web
  editor
- `maxMinutes` and `voice` when selected
- `idempotencyKey`: a new opaque key for this intended guide

If the create result is uncertain because of a timeout or lost response, retry once with the same
`idempotencyKey`. Never use a new key for that retry. Without the original key, check
`list_interview_guides` for a matching title before attempting another create.

The objective becomes the first conversational segment. Inspect the returned `partialSuccess` and
`message` fields before claiming that length or voice settings were applied.

### 5. Present the result

Report the saved guide title, objective, applied length, voice, and response modes when known, and
`platformUrl`.
Name any setting that failed and offer the exact next correction. Then ask whether the user wants
to refine the guide further.

## Refine a guide

1. If the user did not identify the guide, call `list_interview_guides`. Ask them to choose only
   when more than one plausible guide remains.
2. Call `get_interview_guide` and use its current structure and revision as the source of truth.
3. For a broad request such as "improve this guide," briefly identify the material gaps and state
   the edits you will make. Do not invent product facts, participant evidence, or research goals.
4. Use the smallest appropriate edit, one change per call:
   - Settings: `update_guide_settings` (`action`: `title`, `length`, `interviewer`, `intro`, `conclusion`, `branding`, `response_modes`)
   - Structure: `edit_segments` (`action`: `add`, `update`, `reorder`)
   - Questions: `edit_questions` (`action`: `add`, `update`, `reorder`)
   - Conversational prompts: `edit_sample_questions` (`action`: `add`, `update`, `reorder`)
   - Removal: `remove_from_guide` (pass the `segmentId`, `questionId`, or `sampleQuestionId` to remove, exactly as `get_interview_guide` returned it)
   - Whole-flow rebuild: `apply_flow`
5. Pass the latest returned revision as `expectedRev` on every edit.
   After every successful mutation, use the newly returned revision for the next one.
6. If a revision conflict occurs, re-read the guide and explain the conflicting change. Do not
   blindly replay a removal or overwrite newer work.

Only delete a segment or remove a question when the user explicitly requested that removal or
confirmed a clearly described proposal. If `liveSnapshotSync` is pending, explain that the edit is
saved but not yet effective for future interview starts.

## Publish and share

Publish only when the user asks to go live or confirms a clear proposal to publish. Call
`publish_guide` with the latest `rev` as `expectedRev`; if it reports problems, explain them and
offer fixes instead of retrying. After a successful publish, call `share_guide` and give the
user the link. Attune shares studies by link only; it can't email or recruit participants yet,
so suggest the user send the link by email, Slack, text, or in their product. Treat the link as
sensitive: anyone with it can take the interview. If the workspace is out of interview tokens, say so and point the user to the Attune web app.

## Failure and safety rules

- Never ask for credentials, OAuth tokens, MFA codes, or other authentication secrets. The user
  completes authentication through the plugin connection.
- Never report a guide or mutation as saved unless the tool response confirms it.
- Preserve a successfully created guide when a later setting fails; report the partial result and
  offer a targeted correction.
- If a voice name is rejected, use the available display names returned by the tool rather than
  guessing.
- Keep organization context and guide content within the selected authenticated organization.
