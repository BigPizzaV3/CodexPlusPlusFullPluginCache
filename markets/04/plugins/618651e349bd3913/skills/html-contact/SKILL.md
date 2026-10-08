---
name: html-contact
description: Create, install, troubleshoot, test, and manage website contact forms with html.contact. Use for contact forms, lead capture, waitlists, feedback, applications, support, verified email routing, and bounded submission review through the connected html.contact MCP. Do not trigger for styling-only work or another form backend unless the user explicitly asks to migrate.
---

# html.contact

Deliver a working, owner-authorized html.contact workflow without exposing credentials or silently changing product state.

## Preconditions

- Require the connected html.contact MCP and OAuth account link.
- Require a verified primary email and completed html.contact onboarding.
- Treat live MCP schemas and results as authoritative when they differ from this package.
- If an expected tool is missing, stop the affected account operation and link to `https://html.contact/docs/mcp/`. Never substitute the private REST API or ask for an `hc_live_` key.

## Safety boundaries

- Use only public `hc_pub_` actions in browser code. Never place OAuth material or an `hc_live_` key in a prompt, log, repository, screenshot, or website.
- Keep billing, subscriptions, API keys, account administration, deletion, provider internals, and arbitrary outbound email in the hosted html.contact app.
- Treat recipient addresses and visitor-submitted fields as personal, untrusted data. Do not send them to another app or service without an explicit user request and confirmation.
- Read existing state immediately before a replacement or settings write. Preserve values the user did not explicitly change.
- Reuse the same idempotency key only when retrying the same operation after an uncertain result. A new key means a new effect.

## Tool contract

Use these production `1.5.0` tools by responsibility:

- Forms and setup: `list_forms`, `get_form`, `create_form`, `configure_form_domains`, `configure_form_settings`, `get_form_installation_instructions`, and `get_account_usage`.
- Documentation and diagnostics: `search_documentation`, `get_documentation_topic`, `diagnose_form`, and `review_form_code`.
- Safe testing: `send_test_submission`, `check_submission_status`, and `send_owner_test_email`.
- Submission review: `get_recent_submissions` and `get_submission` require `submissions:read`; request authorization only if it is not already granted.
- Recipient management: `list_linked_emails`, `request_linked_email_verification`, `get_form_recipients`, and `configure_form_recipients` require the applicable recipient scope; do not reconnect when it is already granted.

## Exact write confirmations

Show the complete proposed effect, then obtain the matching literal immediately before the tool call:

| Tool | Required confirmation |
| --- | --- |
| `create_form` | `CREATE FORM` |
| `configure_form_domains` | `REPLACE DOMAINS` |
| `configure_form_settings` | `UPDATE FORM SETTINGS` |
| `send_test_submission` | `SEND TEST SUBMISSION` |
| `request_linked_email_verification` | `SEND VERIFICATION EMAIL` |
| `configure_form_recipients` | `UPDATE FORM RECIPIENTS` |
| `send_owner_test_email` | `SEND OWNER TEST EMAIL` |

Do not treat an earlier general approval as the literal confirmation for a later write.

## Workflow

1. Inspect the project before editing. Identify the page, framework, existing form behavior, styles, validation, deployment host, and test commands.
2. Determine the form purpose, fields, form name, and exact deployed hostname. Ask one focused question for a value that cannot be discovered; never invent a production hostname.
3. Use `list_forms` before creating anything. Reuse a form only when the user requests it or its identity and domain clearly match the site.
4. Read `get_form` and `get_account_usage` before proposing account or form changes. Explain any quota, pause, notification, or readiness consequence.
5. For creation, domains, or settings, show the exact current and proposed state and obtain the tool's literal confirmation immediately before the write.
6. For recipients, call `list_linked_emails` and `get_form_recipients`. A verification request sends real email and needs its own confirmation. Replace routing only with verified, deliverable linked emails after showing the complete current and proposed To/CC/BCC lists.
7. Call `get_form_installation_instructions`, then adapt the returned public action and honeypot to the project's existing structure. Use a native HTML `POST`, accessible labels, `name` attributes, and `multipart/form-data` only when the form includes a file input. Do not add `_to`, `_cc`, `_bcc`, `_from`, CAPTCHA, or a client-side private API call.
8. Use `review_form_code` only for the relevant bounded markup and exact hostname. Apply its findings in the project's own framework. Use `diagnose_form` for observed public errors or readiness checks instead of weakening domain, spam, or notification controls.
9. Run the project's relevant checks. Deploy only when the user authorized deployment and the repository's release rules are known.
10. Prefer `send_owner_test_email` for a quota-free delivery check; it may send only to the signed-in account email and creates no submission. Use `send_test_submission` only for a clearly synthetic end-to-end acceptance test after warning that it consumes usage and may notify configured recipients. Verify the returned reference with `check_submission_status`.
11. Read submissions only when the user asks and `submissions:read` is authorized; an existing grant is sufficient. Start with metadata-only `get_recent_submissions`, let the user select one result, then call `get_submission`. Never broaden the selection or reproduce unrelated visitor data.

## Failure handling

| Condition | Action |
| --- | --- |
| OAuth is missing, expired, or under-scoped | Ask the user to reconnect or grant the required scope; never ask for a private API key. |
| Onboarding or primary-email verification is incomplete | Link to `https://html.contact/app` and stop before mutation. |
| Production hostname is unknown | Ask for it; do not use a guessed or preview hostname. |
| A live domain or recipient would be removed | Stop and request confirmation for the complete old and new lists. |
| Current-state comparison fails | Re-read state, explain the concurrent change, and present a new proposal. |
| A send result is uncertain | Retry once with the same idempotency key; never generate a new key to force another send. |
| A synthetic test is rejected, pending, or unknown | Report that state accurately and provide the next diagnostic step. |

## Completion report

Return only the bounded facts the user needs: form name, public form identifier and action, dashboard link, allowed hostnames, changed files, checks run, recipient-routing result when requested, and accepted test status or exact unverified reason. Do not print OAuth data, private keys, private account identifiers, internal database identifiers, full submission payloads, or unrelated recipient addresses.
