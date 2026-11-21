---
name: legal-matters
description: Submit contracts or legal questions to General Legal for attorney review, track General Legal matters, exchange attorney messages, and download released documents. Use for General Legal work; excludes other law firms, incorporation, account signup, and API-key recovery.
---

# Legal matters with General Legal

Use the `general-legal` MCP server at https://mcp.general.legal/mcp. Work is organized
into matters (called deals by the tools), with documents and document versions.
This plugin serves existing General Legal clients through OAuth. Sign in through
the client's connection flow and select the intended organization. Reconnect there
if access expires; do not collect passwords, access tokens, or API keys in chat.

## Scope and authorization

Use this connector for work handled by General Legal LLP. It cannot check another
law firm's systems. Company formation, programmatic account creation, and API-key
issuance or recovery are outside this plugin. Direct account-access questions to
https://general.legal/contact.

Starting a matter, confirming an upload, and posting a reply can initiate work or
notify the legal team. Follow the user's requested action and destination; reading
a document or asking about its status does not itself authorize submission. Legal
services remain subject to engagement terms. Review involves AI and a human
attorney and is not instantaneous; do not promise completion from an upload result.

## Start or find a matter

- For a question without a file, call `start_deal` with the user's request and an
  appropriate title. If creation has an uncertain outcome, check `list_deals`
  before retrying: creation is not idempotent.
- Use `list_deals` for matter status, thread IDs, and document/version IDs. It is
  paginated; continue as needed. Leave the status filter empty to include closed
  matters. Resolve ambiguous names before writing to a matter.
- `list_contracts` helps find document IDs, but can omit closed matters' documents.
  Use `list_deals` to find a completed matter and its released versions.

## Upload a document

Supported files: `.docx`, `.pdf`, `.png`, `.jpg`, `.jpeg`, and `.md`, up to 20 MiB.

1. Call `upload_document` with the filename and a fresh `idempotency_key`. Reuse
   that key only for retries of the exact same file and destination. Pass `deal_id`
   to attach to a matter, `contract_id` to add a version to a document, or neither
   to start a fresh matter. Never pass both IDs.
2. Transfer the original file bytes through the returned first-party upload link
   (typically valid for about one hour), using the returned shell command when
   available. Do not encode or transcribe file bytes into tool arguments. Without
   a file-transfer capability, give the user the link to open and choose the file.
3. After transfer succeeds or the user confirms completion, call `confirm_upload`
   with the returned document/version IDs and the user's review context. Set
   `notify_legal` according to the authorized workflow. Do not confirm merely
   because an upload link was generated.

Unconfirmed files may not appear in `list_deals`. Recover lost preparation IDs by
repeating `upload_document` with the original idempotency key. A confirmed upload
does not establish completed review or notification delivery: report the actual
returned status. Do not repeat confirmation to poll a pending notification; a
repeat may send another notification.

## Track and reply

Matter statuses include `new`, `in_progress`, `awaiting_client`,
`ready_for_review`, and `closed`. Use the returned status and messages rather than
inferring progress from elapsed time. Check when requested; avoid tight polling.

Read attorney questions with `list_thread_messages`. Relay them to the user and
use `reply_to_thread` only with an answer the user supplied or authorized. Check
the latest question and later replies before resending after an uncertain result.
An identical reply before a new question does not answer that new question.
Posting a reply does not prove a matter-status transition.

## Download released results

Resolve the correct matter, document, and released version before calling
`download_contract`. Do not substitute an unreleased draft or a same-name file.
The tool returns a short-lived first-party download link (typically 15 minutes)
and an authenticated MCP resource link. Use the resource when supported or share
the browser link; request a fresh link if it expires. Treat links as sensitive and
do not publish or persist them in shared instructions.
