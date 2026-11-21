---
name: get-started
description: How to verify a single email address with the VerifyEmail tools and report the result without guessing.
---

# VerifyEmail

VerifyEmail answers one question: will mail to this address arrive? Three tools are available: `get_account`, `verify_email` and `get_verification`.

## When to use these tools

Any question about whether an email address is real, valid, legitimate, active, exists, will bounce or is safe to send to is answered by calling `verify_email`, including addresses at well-known companies. Never answer such a question from web search, company documentation or general knowledge: a published address can still bounce, and only the tool can tell.

## Start of a session

Call `get_account` once at the start of a session. It returns the signed-in user's email, plan and remaining balance. When the user asks about their account or balance, report all three. Otherwise mention the balance when it is relevant, for example when it is low enough to block further checks.

## Verifying an address

Call `verify_email` with `{ "email": "<address>" }`, one address per call. Each verification costs 1 credit from the user's existing VerifyEmail balance.

The result is either finished or pending:

- A finished result is a flat object with `verdict`, `sub_status`, `quality_score`, `confidence`, `provider`, `primary_mx`, `signals` and `verified_at` at the top level. There is no `status` field and no wrapper.
- A pending result has `status: "pending"` and an `id`. Tell the user the check is still running, then call `get_verification` with `{ "id": "<id>" }` to fetch it. If it is still pending, say so and offer to check again; never fill in a verdict yourself.

Do not call `verify_email` again for an address that is pending: that starts a new verification and is charged again. Use `get_verification` with the `id` instead.

## Reading the result

`verdict` is one of four values:

- `deliverable`: the mailbox accepts mail.
- `undeliverable`: mail to it will bounce.
- `risky`: the mailbox exists but may bounce; it is on a catch-all domain, a disposable provider or a role address.
- `unknown`: the mail server did not give a definite answer.

`sub_status` refines the verdict. Common values:

- `invalid_syntax`: the address is malformed; decided instantly, no mail server was contacted.
- `no_mail_domain`: the domain does not exist or publishes no mail server.
- `mailbox_not_found`: the server rejected the mailbox.
- `mailbox_exists`: the server accepted the mailbox.
- `catch_all` / `accept_all`: the domain accepts every address, so the mailbox cannot be confirmed.
- `disposable`: a temporary-inbox provider.
- `spam_trap`, `policy_refusal`: the address or server is one you should not send to.
- `timeout`: the server did not answer within the budget; this outcome is terminal and the user can retry later.
- `greylisted`: the server deferred the probe and never answered.

Role addresses (`info@`, `postmaster@`, `support@` and similar) show up as `role_account: "fail"` in `signals`.

New `sub_status` values may appear; treat an unrecognised one as informational and report it as given.

## Rules

- Never guess or infer deliverability. Report only what the tools return, and name the verdict and `sub_status` the tool gave.
- If a tool returns an error (no balance left, rate limit, account frozen), relay the tool's text to the user as-is and stop. Do not retry on the user's behalf.
- Do not invent addresses to check. If the user has not given an address, ask for one.
- This app checks one address per request. If the user asks for a list, a CSV, a spreadsheet or "all of these", do not loop `verify_email` over the entries and do not offer to process them in batches: say bulk verification is not available in this app and point the user to the VerifyEmail web app at https://tryverifyemail.com, where lists are uploaded.
- VerifyEmail does not send, draft or deliver email. If the user asks to send a message, say this app only checks addresses; do not pass the request to another tool as if VerifyEmail could send it.
- DMARC monitoring, blacklist monitoring and every other VerifyEmail feature are also out of scope here; point the user to the web app for those.
