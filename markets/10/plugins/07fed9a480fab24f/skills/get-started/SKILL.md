---
name: get-started
description: Set up AnyShare and choose a first document-sharing or engagement task after installation.
---

# Get started with AnyShare

Explain that AnyShare can share an original document with a protected link, organize documents in an existing data room, or report recorded engagement. Offer those choices if the user has not already chosen a task. Continue an existing request without asking them to repeat it.

Use the host's AnyShare OAuth connection when a task needs account access. The user signs in and selects one organization and permissions in AnyShare; never request passwords, tokens or verification codes in chat. Check `get_connection` when beginning the chosen task and identify the connected organization. A dashboard organization switch does not retarget a connection.

Installation alone authorizes no upload, new share link, room placement or private engagement lookup. Once the user requests a supported task, follow `../share-documents/SKILL.md` with the actual available tools. Files must preserve their original bytes and be no larger than 5,242,880 bytes. New links require verified email and disable downloads by default.

When reporting the connection, identify the organization and explain any billing restriction using the returned `billing` details. State the known reason and relevant date, the affected actions, what remains available, and the recovery step. For an expired trial, explain that uploads, new share links and adding documents to rooms are paused while existing documents and engagement reports remain readable with the required permissions. `can_use: false` does not mean the connection failed or all AnyShare usage is unavailable. If billing details are absent, state that the reason is unavailable; do not invent a trial expiry or payment failure. Follow the access-and-errors guidance in `../share-documents/SKILL.md` for other billing states and failures.

Direct billing questions to the organization owner or https://share.anysoft.ai/support. Do not promote subscriptions or lead to checkout. Disconnecting in AnyShare Settings → AI connections stops future assistant access; existing documents and recipient links remain.
