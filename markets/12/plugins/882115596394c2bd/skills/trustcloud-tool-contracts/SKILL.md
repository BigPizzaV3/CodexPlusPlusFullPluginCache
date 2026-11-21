---
name: trustcloud-tool-contracts
description: "Use when choosing and executing Homin Cloud MCP tools safely, including discovery, authorization, preview or review, apply, retries, and readback."
---

# Homin Cloud external tool contract

Shared references provide business knowledge. Runtime, UI, tool, or save examples
inside them describe the internal surface and must not be executed as written.
Follow this external workflow, the current live contract, and its confirmation
requirements.

Discover the operation or dedicated tool instead of guessing a name or payload.
Read its current contract and use only arguments supported by that contract. Live
schemas, visible operations, and authorization results override examples in skills.

In ChatGPT Apps, use the individually exposed tools and their declared input
schemas directly. Each tool fixes one operation and execution mode. Do not send
an operation selector or arbitrary executor payload. Native MCP clients may use
their separately exposed discovery and execution tools. These native examples do
not apply to the ChatGPT Apps surface.

Classify the action before execution:

- `read` returns current state and must not be described as a change.
- `preview` or proposal preparation validates and binds a proposed change but does
  not apply or publish it.
- `apply` requires the matching fresh preview, review, or confirmation reference
  when the contract requires one.

Preserve the same idempotency key when retrying the same intended mutation. When an
apply or paid operation has an unknown outcome, read status or current state before
retrying. Never create a new key merely because the transport timed out.

After a write, read back the authoritative resource and compare the relevant IDs,
version, timestamps, fields, and publication state with the confirmed proposal.
Report partial failure, conflict, expired confirmation, and missing authorization
as unresolved results. Never convert them into fabricated success.

Keep secrets, signed URLs, authorization headers, raw file bytes, and redacted
fields out of chat and logs. Use opaque returned identifiers for follow-up calls.

## Selective references

Open only the references needed for the current task. In an installed package, use the relative links below. With an MCP-only client, fetch the exact document ID shown for the reference.

- [references/tool-contract-schema.json](references/tool-contract-schema.json) — MCP doc ID: `skill/trustcloud-tool-contracts/v1/references/tool-contract-schema.json`
