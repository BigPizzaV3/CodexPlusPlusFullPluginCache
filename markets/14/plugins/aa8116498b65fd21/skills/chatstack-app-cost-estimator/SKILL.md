---
name: chatstack-app-cost-estimator
description: "Estimate app and AI solution development costs and hours, scope an MVP, and generate a software PRD (Product Requirements Document) with user stories, requirements, and a technical specification. Use when the user asks for an app or software development cost estimate, a software quote, development hours, MVP scope, or a software PRD for an app idea. Do not use for definition-only questions such as “What is a PRD?”, code editing, calendar lookup, general project-management advice, or managing existing ChatStack portal projects."
---

Use the ChatStack App Cost Estimator MCP tools. Do not invent a quote, timeline, or contact details.

## Session

Call `start_session` first. Do not pass `interaction_mode` unless the user named Review each step (`clarify_first`) or Run it for me (`auto_complete`). Asking for an estimate is not auto-complete.

Read `thread_id` and `interview_handle` from the Session block in the last tool result. Pass both on every later call. Never invent them. Never re-run `start_session` to recover them.

## Next tool

Follow `next_tool` on the last result:

- `send_turn` — user text, interaction-mode choice, typed clarifying answers (including `1B, 2A`), or requested table edits. While clarifying questions are waiting in Review each step, `next_tool` is `send_turn`.
- `send_action` — approve a pending gate using the `action_type` on the Your choices line, not the visible label. For clarifying questions this is only Submit my answers. In Run it for me, call it once per result with an empty payload while `next_tool` is `send_action`.
- `get_estimate_status` — recover the current stage only
- `submit_prd` — only at estimate, after the user confirms contact

Relay Markdown pipe-tables, Assumptions, and Risks verbatim. After a reject or request-changes, call `send_turn` with the user's exact words. In Review each step, show the regenerated table and wait for approval.

For clarifying questions, use the full question and option labels returned by the tool. When a native form is present, do not repeat the same questions as prose beside it.

After a successful PRD submission or submitted-status recovery, relay `post_submit_notice` verbatim. Do not omit its URLs or add an email-delivery caveat.

## Do not

- Invent first name, last name, email, country, or project name
- Call `submit_prd` again after a successful receipt
- Skip these tools and guess a cost
