---
name: metadata-cleaner-setup
description: Set up the existing hosted Metadata Cleaner connection in ChatGPT or Codex, check which account is connected, and explain how to start a confirmed Word or PDF inspection.
---

Use this setup workflow when the user runs setup after installing Metadata
Cleaner or asks how to begin. This is the hosted edition: selected documents
upload to Myworkingmemory. Ordinary DOCX and PDF inputs are limited to 2 MiB.
Original files remain unchanged. It is not the separate Local edition.

1. If the existing connection is available, call `get_account` with `{}` to
   check it. Report connection status and any actual balance text returned.
   Do not infer a purchased pack from an internal account type, an account ID,
   or a reviewer/test account. If no balance is supplied, say it is unavailable.
2. If sign-in or connection is required, use the client's normal connection
   controls and the informational
   [account help](https://www.myworkingmemory.ai/metadata-cleaner-help.html).
   Account keys belong only on the Myworkingmemory authorization page, never
   in chat, skills, tool arguments or a public upload. Do not create an
   account, change permissions, start a purchase, or grant credits yourself.
3. Once connected, explain the next action plainly: select one ordinary Word
   DOCX or PDF, up to 2 MiB, and ask to inspect its supported author, company
   and document-property metadata before sharing. Do not choose or upload an
   unselected file. A filename or a mentioned local path alone is not a
   completed file upload.
4. Before inspection uploads the file, obtain the user's explicit confirmation
   that it excludes personal health records, payment-card/security details,
   government-ID numbers, passwords, API keys and other authentication secrets.
   Never infer that confirmation. Do not request the excluded data or claim
   that the cleaner detects it automatically.
5. Hand the confirmed document to the packaged `metadata-cleaner` workflow.
   Inspect first. Cleaning that accepts tracked changes or removes hidden text
   or custom XML needs the user's separate explicit approval. Inspection does
   not spend a cleaning credit; a verified cleaned copy spends one clean from
   the existing account, subject to the actual returned account limits.

Setup itself must not clean a file, consume a cleaning credit, change billing,
or claim that installation grants service access. A ChatGPT/Codex subscription
or an Apple purchase does not establish this hosted account's entitlement.
Do not display prices, checkout links, upgrade offers or subscription pitches.

When setup is complete, finish with one clear next instruction, for example:
“Choose a Word document or PDF, then ask me to inspect its metadata before
sharing.” Do not report a completed inspection or cleaned download from setup
alone. The [customer and agent README](../../README.md) explains the supported
workflow and its limits.
