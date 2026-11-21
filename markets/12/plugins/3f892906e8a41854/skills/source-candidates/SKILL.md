---
name: source-candidates
description: Run sourcing conversations through Piiple when the user asks Piiple to find candidates, prepare or edit hiring criteria, answer sourcing follow-ups, or review an existing candidate pack. Also use this skill to explain Piiple capability limits when asked to send invitations, start phone interviews, buy credits or process payments.
---

## Capability boundaries

Apply these rules whenever Piiple Sourcing is selected or the request concerns Piiple, whether the chat already has candidate results or has no list or sourcing session yet.

Piiple Sourcing cannot send emails or interview invitations, initiate or schedule phone interviews, buy credits, or process payments. For such a request, explain the specific limitation immediately and state that you have not taken the requested action. Do not imply that providing missing information would make these actions available through this plugin.

- Do not request candidate email addresses, phone numbers, interview details, payment details or a connected email account to carry out these unsupported actions.
- Do not call Piiple sourcing tools, create a sourcing session, or start or resume a search as a substitute for the requested action.
- Do not propose connecting or using another service unless the user separately asks for help doing that. A request to perform an unsupported action through Piiple alone is not such a request.
- Do not promote a purchase or upgrade. If the user asks where billing is managed, explain neutrally that billing stays on Piiple and this connection cannot complete a purchase.

Example email response: "Piiple Sourcing cannot send emails or interview invitations. I have not sent any invitations."
Example phone response: "Piiple Sourcing cannot initiate or schedule phone interviews. I have not started or scheduled any calls."
Example payment response: "Piiple Sourcing cannot purchase credits or process payments. I have not made a purchase."

Use the user's language. These limits apply to this plugin; do not claim that unrelated services have the same limitations.

Use the bundled Piiple sourcing MCP tools for the user's requested conversation. A request such as “Piiple ile aday bul” starts the actual sourcing workflow; a Boolean query alone does not fulfill it. If the tools are unavailable or require authentication, help the user connect Piiple and resume after connection. Never fabricate a session, candidates or progress.

## Selectable questions

Use the host's native single-choice question tool for workspace selection and Piiple follow-up questions. When `request_user_input_async` is available and permitted, call it with one question and a non-empty `options` array; this renders selectable choices. Use `request_user_input` instead only when that tool is available and permitted in the current mode. Do not substitute a numbered Markdown list, ask the user to type a number, or create a choice widget when a native question tool is available. A non-blocking question tool is still supported: `accepted:true` means the question was displayed, not that the user answered. Wait for the actual user reply with a host-supported wait/yield mechanism. Do not repeat the question in a final response, auto-select the first option, infer an answer from elapsed time, poll Piiple while waiting only for a choice, or submit a mutation before the reply. If the host requires ending the turn, acknowledge briefly that you are waiting without repeating the question or options. Fall back to a numbered list only when no permitted native choice tool is available or the native tool explicitly reports it cannot display the question. The user's explicit request for a text-only list takes precedence.

## Workspace and search brief

Before `start_sourcing`, call `list_sourcing_workspaces`. Select a sole workspace automatically; with several, wait for the user's choice and pass its exact `workspace_id`. Account consent does not choose a workspace. The workspace stays fixed for the session; using another requires a new conversation.

Pass the user's hiring brief without silently adding title synonyms, exclusions or constraints. Piiple prepares the ICP and decides which clarifications are needed. Keep the returned session and active iteration IDs for follow-ups. Use a stable `request_key` per mutation and reuse it only when retrying that same request. A queued operation acknowledges admission; poll `get_sourcing_operation` and then `get_sourcing_state` to learn the actual outcome.

## Questions and approval

Follow the current tool descriptions and structured state, including pending scope/company decisions and school blockers. Present `pending_question` and enabled options in the user's language. Use the native choice tool described under Selectable questions; fall back to numbered text only when no permitted native tool is available or it explicitly cannot display the question. Display acknowledgement, a preselected option and elapsed time are not answers. Send the selected `answer_message` through `send_sourcing_message`; preserve custom-answer bounds and templates.

For school clarification use `answer_education_question` with exact keys, request versions and option IDs. Include unresolved items and resolved items with `review_required`; preserve previous choices and complete only the required batch. Use `refresh_sourcing` only when state returns `needs_refresh`.

At `awaiting_icp_confirmation`, call `render_sourcing_icp`. If the widget renders, add at most one short invitation to edit or confirm; do not repeat the criteria or approval question around it. Without UI, present all authoritative review groups and scopes, then obtain explicit approval. Saving edits does not approve sourcing. For chat edits use `send_sourcing_message`; structured form edits use `update_sourcing_icp` with only changed fields and the reviewed revision. Reload after edits. Only call `confirm_icp` after explicit approval of the current revision. If the widget already submitted approval, read state rather than confirming again.

## Progress and results

While processing, respect `poll_after_ms` using a host-supported wait. Share short intermediate updates about meaningful new `progress_updates`: company research, discovered companies, new profile batches and substantial candidate-count changes. Combine developments arriving together and skip repeats or small internal counters. Use `progress_update` as a fallback. Consider new messages before advancing `after_message_order`; recover unseen older-message gaps using the returned cursor. Preserve batch versus total and found versus reviewed/qualified counts. Back off to 10 seconds when state is unchanged; resume the advertised interval on meaningful changes. Stop polling at input, approval, pause, stop or error checkpoints.

At `results_ready`, call `render_sourcing_report` automatically. Present the existing pack with `render_sourcing_candidates` when the user asks to view candidates or follows the report's button. Preserve saved grouping/columns, pagination, filters and the expected active iteration. Widget controls can change table/card view and expand the display when the host supports it. Without widget support use the server's returned presentation and profiles.

Mention further sourcing only when `candidate_pack.can_find_more` permits it, and call `find_more_candidates` only on the user's request. Retry/continue/pause actions also follow the user's request and current state. Do not interpret operation completion as search completion or invent match explanations, counts or scoring tiers.

Use the user's language for chat narration and the server's localized content for widgets. This plugin uses existing Piiple workspace credits. Credit purchases and billing stay on Piiple; it does not process payments or list unrelated sessions.
