---
name: manage-request-drafts
description: Find, review, delete, or submit an existing Physical Validation account draft, including drafts started in the browser. Use when a person asks about their saved experiment requests.
---

Use the host's managed OAuth connection for the person's Physical Validation account. If the connector requests sign-in, use the host's connection flow. Work only with drafts returned for that connected account.

- Use `list_request_drafts` to find the requested draft. Follow a returned cursor when needed. Identify the draft by its returned title and ID, and clarify if several match the person's description.
- Use `get_request_draft` before reviewing, deleting, or submitting. Preserve its full contents, ID, and current revision. Surface missing information and offer its returned browser review link for editing or attachments.
- The exposed MCP draft tools list, read, and delete existing drafts. `prepare_request` produces a review link without persisting an account draft. Do not claim a draft was created or updated by one of those reads or preparation calls. If the person wants edits saved, use the browser review link.
- Delete only the draft the person explicitly asked to remove, using its current revision with `delete_request_draft`. A revision conflict means the draft changed. Read it again and verify that the deletion still matches the person's intent before retrying.
- Submit a saved draft only after the person agrees to its complete contents and the service terms and privacy notice. Use `submit_request` with the draft ID and current revision, preserving the idempotency key for an unchanged retry. Report the returned submission receipt and any `draftDeleted` result accurately.

The draft tools do not provide live request progress. Use the service's returned links when the person needs information beyond the exposed tools.
