---
name: email-model-editor
description: "Edit an existing Reteno email or template through its native JSON model. Use for native preheader, copy, link, image-source, theme, style, and block additions, removals, or duplication when a live message_id has an editor model. Uses a generated SDK mutation module, validated file-based execution, base/target merging and durable read-back. Use email-from-reference for a new email or full rebuild. Do not use for raw-HTML editing, sending, scheduling, or a message without a native model."
---

# Email Model Editor

Edit an existing Reteno email through its native JSON model. Use `email-from-reference` for
a new email or full rebuild. Read the topic for the current stage; do not load all references
or the full tool/resource catalog at startup.

| Stage | Read when needed |
| --- | --- |
| Acquire | [Download and inspect the target](reference/acquire-and-inspect.md) before editing. |
| Mutate | [SDK module, examples, validation, completeness](reference/mutate-and-validate.md) before constructing the change. |
| Persist | [File upload, recovery, durable and visual checks](reference/persist-and-verify.md) before writing. |
| Attached or Ctrl+V image | [Upload supplied images](reference/image-upload.md) before hosting original bytes. Keep the original asset if hosting fails; do not regenerate a supplied image. |

Use the connected Reteno MCP. If the host installs `HOST.md` beside this file, read its concrete
transfer commands and available image workflow.

`<skill-dir>` is this installed skill directory; `<bundle-root>` contains `skills/` and `packages/`.

## Invariants

- The model is a file. Never paste the complete model into the conversation or pass it as an MCP
  argument.
- The candidate and base are complete models. Persistence applies the differences from the base
  to the candidate on top of the live state. Omitting an acquired optional key requests deletion,
  not "unchanged" (see [Model completeness](reference/mutate-and-validate.md#model-completeness)). Never strip keys or upload a partial document; the runner
  rejects a candidate that lost a key the acquired model had, except for supported explicit clears.
- Express each request as a small JavaScript module that mutates the supplied `email` SDK handle.
  Return nothing; the runner finishes its tracked session and rejects returned replacement documents.
  Do not edit the raw JSON object or regenerate the full model.
- Run the module with `run-sdk.mjs --input <model> --script <module> --output <candidate>`.
  Every edit receives the full SDK handle for content, style, insertion, removal, and duplication.
  The runner rejects scripts with no SDK mutations, selector misses, and schema-invalid output.
  A model without blocks permits metadata edits only; other edits must leave at least one block.
- Keep the acquired model untouched as the base uploaded alongside the candidate; retain its `modelHash`.
- A successful local mutation is not completion. Verify the saved model and inspect fresh
  desktop and mobile PNG previews of the persisted email.

## Boundaries

- Do not create, clone, translate, send, schedule, activate, or delete an email.
- Do not edit subject metadata as an implicit part of a model edit.
- Preheaders use `metadata.preheader` through the native model path above. Preserve them during
  unrelated edits. A requested preheader is complete only when its saved value is verified,
  including a fresh read confirming an already-correct value.
- Do not use compiled HTML as the editable source of truth.
- Do not mutate a message that has no native editor model.
- Delegate image creation and editing to the documented host image workflow.
- Do not infer MCP endpoints, credentials, or authentication.
- Use `email-from-reference` for a new persisted email.
