---
name: apollo-io-audit
description: Run the GTM Works audit of an Apollo.io workspace and explain the findings. Use when the user asks to audit or health-check their Apollo.io, or asks about duplicate accounts, contacts in two sequences, emails Apollo.io did not send, mailboxes that cannot send, paused sequences, or deactivated users who still own records.
---

# Apollo.io audit

The audit only reads from Apollo.io. It does not write to it.

## Running it

1. Call `list_apollo_audits` first. If a recent audit exists, read it with `get_apollo_audit`
   instead of starting a new one.
2. If there is none, call `start_apollo_audit`. If it returns `needs_connection`, give the user the
   `connect_url`: they sign in with Apollo.io (or try the demo workspace) on app.gtmworks.ai, then ask
   again.
3. The nine checks finish in seconds. The duplicate account scan reads every saved account and can
   take a long time on a large workspace: read its progress with `get_duplicate_account_scan`, and
   tell the user the result also arrives by email.

## Presenting findings

- Most serious first. For each finding: what is wrong, how many records, why it matters, how to fix
  it, and the Apollo.io link when the finding has one.
- To show the records behind a finding, call `get_audit_finding_rows` and page through them. Show a
  short table, not every row.
- A check listed under `could_not_check` did not run. Never call it clean or passed. When it has
  `sign_in_cannot_read`, say that Apollo.io's sign-in does not give apps this access.

## Limits

- Never ask for, accept or repeat an Apollo.io API key, password or token in the chat. If the user
  pastes one, do not use it, tell them not to share keys in chats, and point them to "Sign in with
  Apollo.io".
- This plugin cannot merge, edit, delete, enrich, prospect or add anyone to a sequence. Say so, show
  which records are affected and how to fix them in Apollo.io.
- Do not quote prices or link to checkout.
