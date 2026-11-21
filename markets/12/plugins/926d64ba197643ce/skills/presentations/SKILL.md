---
name: presentations
description: Create or edit a PowerPoint presentation with Plus AI, including generating a deck from a brief, editing an uploaded or workspace PowerPoint, and applying follow-up changes to a Plus AI Presentation Agent session. Use when the user requests Plus AI or is working with a deck created through this plugin.
---

# Plus AI presentations

Use the connected Plus AI MCP tools to create or edit the requested presentation.
The user connects their Plus AI account through OAuth. Never request credentials
in chat or store them in files. Presentation generation and edits consume the
organization's Plus AI credits; avoid duplicate creation or edit requests.

## Create a presentation

Use `create_presentation_with_agent` for a new presentation by default. Build a
self-contained prompt with the user's intended audience, purpose, slide count,
language, tone, and any supplied source material. The agent receives only the
tool prompt, so carry relevant facts, figures, and notes into it. Preserve
uncertainty in supplied material and do not invent missing facts.

Ask only for details essential to completing the request. Otherwise choose
reasonable defaults and proceed. State slide count in the prompt, and pass a
language tag or `auto` when appropriate.

Use `create_presentation` for classic template-based generation when the user
prefers that workflow or faster generation over the agent's iterative design.
It accepts a prompt, an optional slide count, and an optional ISO 639-1 language.

## Edit an existing PowerPoint

For follow-up changes to an agent-created deck, use
`continue_presentation_agent_session` with its existing session ID. Include the
requested changes in the prompt. Keep using that conversation for later edits.

For another existing deck, find its file ID with `list_files`. Use name filtering
and pagination as needed. Resolve ambiguous matches before editing. Never invent
a file ID or select an unrelated deck.

If the user attached a PowerPoint, use `upload_file` with the supported attachment
parameter. If the file is local and shell access is available, call `upload_file`
with `file_name`, then run the returned upload command for that file. If neither
method is available, the user can upload the deck on the Plus AI web app's New
presentation page, then locate it with `list_files`.

Pass the returned file ID as `pptx_file_id` to
`create_presentation_with_agent`, together with a self-contained editing prompt.
Uploaded files are kept for eight days; the agent edits a copy.

## Wait for completion

Agent creation and continuation calls return within about 45 seconds. A `RUNNING`
result means the work is still in progress. Retain its `sessionId`, tell the user
briefly that the presentation is being prepared, and call
`get_presentation_agent_session` with that ID until it returns a terminal result.
The polling tool waits itself, so no extra sleep is needed.

Never repeat a creation or continuation request just because it returns
`RUNNING`; that can start and bill another operation. If a call times out without
a session ID, do not silently resubmit it. Explain that the outcome is uncertain.
On a failed or stalled terminal result, report the returned error and any
available recovery action rather than claiming completion.

## Deliver the result

Use the returned PowerPoint and PDF links, and show the returned thumbnail when
available. Do not invent download URLs or claim to have inspected slides you
have not viewed. Preserve the session ID in the conversation for future changes.

If the server reports expired sign-in, direct the user to reconnect Plus AI.
If it returns `PLAN_REQUIRED` or exhausted credits, explain that the requested
feature is unavailable with the account's current entitlements. Do not repeatedly
retry account errors. Users may connect an existing Plus AI account with the
required access. Do not promote upgrades, subscriptions, or credit purchases,
or direct users to checkout, billing, or other purchase flows.
