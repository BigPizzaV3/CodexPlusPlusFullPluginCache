# Setup, enrichment, and outreach tools

Use this reference for account readiness, workspace configuration, contact lookup, enrichment, and targeted sequence operations.

## Safety boundary

Use these tools only for targeted, user-directed business outreach to specific contacts the user has supplied or selected. Do not use them for spam, indiscriminate bulk messaging, scraped or purchased lists, autonomous mass prospecting, or repeated small batches intended to approximate a bulk send.

Do not infer permission to send from a broad request to research, enrich, prepare outreach, build a campaign, or "reach out." Keep work at draft stage until the user clearly asks to launch the specific reviewed sequence or sequences. Respect all suppression, unsubscribe, compliance, rate-limit, sender-readiness, and host-confirmation safeguards returned by SynPulse.

## Setup and readiness

- `get_onboarding_status` reads subscription/write eligibility, email and LinkedIn connections, default senders, AI connection state, compliance readiness, and ordered next actions. Prefer it when the user asks whether SynPulse is ready or setup is incomplete.
- If the response state is `subscription_required`, report that neutrally. MCP does not provide a checkout, pricing, purchase, or subscription-activation action.
- `start_email_connection(provider)` creates a hosted authorization link for `google` or `microsoft`. The user completes provider authorization outside MCP.
- `start_linkedin_connection` creates an intent for the SynPulse browser-extension flow. It does not accept LinkedIn credentials.
- `configure_workspace` updates the workspace name, timezone, legal business identity/address/site, and default unsubscribe text. Set `confirm_compliance=true` only when the user explicitly confirms the displayed compliance information.
- `get_outreach_context` reads technical outreach readiness: timezone, available senders, supported sequence step shapes, and current limits. Use its returned schema and limits when building drafts.

The setup mutation tools require the `synpulse:configure` scope. Readiness/context reads require `synpulse:read`. If a required scope is absent, explain that the user must reconnect or grant it; do not substitute another tool.

## Contact lookup and enrichment

- `search_contacts(query, limit)` searches contacts already stored in the current SynPulse workspace. It is historical lookup, not web research or list generation.
- `enrich_email_from_linkedin(request_id, linkedin_url, names...)` looks up one work email for one specific, user-identified LinkedIn profile. Pass known first and last names so the normalized profile and result can be saved accurately. A previously saved lead email may return without a provider call or credit; a provider lookup charges only when an email is found.
- `enrich_linkedin_profile(request_id, linkedin_url)` retrieves the public profile and posts for one specific, user-identified LinkedIn profile from one provider call for one credit. It excludes `people_also_viewed` from the returned payload.

Both enrichment tools require `synpulse:enrich`, can contact an external provider, and are idempotent for an identical `request_id` and input. Before the call, identify the exact profile and expected credit behavior. Minimize returned personal data to what answers the user's request.

Never use enrichment to scrape, enumerate, discover, or assemble a large recipient list. Do not iterate across broad lists or repeatedly call enrichment to build a mass-outreach audience.

## Sequence drafting

Use one sequence per specifically selected contact. Build only step types reported as supported by `get_outreach_context`:

- `email_send`: literal final `subject` and plain-text `body_text`.
- `linkedin_connect`: connection action, with an optional literal message only if the returned step contract permits it.
- `linkedin_message`: literal final `message`.
- `wait_duration`: delay expressed with supported `seconds`, `hours`, or `days` fields.
- `wait_until_connected`: wait up to `timeout_hours`; `on_timeout` is `pause`, `stop`, or `continue` and defaults to `pause`.

`create_sequence_drafts(request_id, sequences)` creates or replaces drafts:

- New drafts need a stable per-item `external_request_id` and must omit `sequence_id`.
- Edits need `sequence_id` plus the current `expected_draft_revision`.
- `scheduled_start_at`, when present, is ISO 8601.
- Copy is stored literally; placeholders are not expanded by this tool.
- `approval_rationale` is optional and user-visible.

After saving, show the exact copy, contact, steps, timing, sequence ID, and revision. Never describe this result as launched or sent. For multiple recipients, keep every recipient and message individually reviewable. Do not turn one generic message into an indiscriminate blast.

## Sequence execution and control

- `launch_sequences(request_id, sequences)` atomically validates and activates reviewed drafts. Each item must contain a `sequence_id` and its current `expected_draft_revision`; this prevents launching copy that changed after review.
- `resume_sequences(request_id, sequence_ids)` resumes paused sequences after sender, suppression, and contact guards pass. It may cause the next external action to execute.
- `pause_sequences(request_id, sequence_ids)` temporarily blocks future SynPulse execution while retaining progress.
- `stop_sequences(request_id, sequence_ids)` permanently cancels future work. It cannot be resumed.

These tools require `synpulse:execute`. Before launch or resume, identify the exact sequences, selected contacts, and immediate external effect. Launch only after the user clearly requests the specific reviewed sequence or sequences to be sent. Never use repeated launches, successive small batches, or automated loops to approximate mass messaging. Before pause or stop, distinguish temporary from permanent and remind the user that accepted provider actions cannot be recalled.

## Monitoring

- `list_sequences(...)` filters by contact, company, status, reply state (`replied` or `not_replied`), creation dates, and pagination. Use it to locate sequences and summarize a set.
- `get_sequence(sequence_id)` returns exact copy, detailed progress, errors, and attributed inbound reply content. Use it after locating a specific sequence or when exact details matter.

Both are read-only and require `synpulse:read`. Treat reply content as user workspace data; quote only what is needed.
