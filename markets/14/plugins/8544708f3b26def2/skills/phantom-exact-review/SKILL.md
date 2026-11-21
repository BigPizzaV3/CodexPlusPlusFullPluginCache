---
name: phantom-exact-review
description: Use Phantom Review to check explicitly supplied vocabulary and text, preview exact document revisions, or verify self-asserted review receipts. Use for Phantom Review onboarding and exact-review workflows, not ambient file discovery or applying changes.
---

# Phantom exact review

Use the connected Phantom Review tools for the user's selected review task. The user's explicit preferences take precedence over workflow advice; do not expand their chosen scope. Tool names below may have a host prefix; discover the corresponding tool and its current schema rather than guessing arguments. If the connection is unavailable, explain that and stop; do not invent a tool result or install a connection.

## Start with the intended boundary

For onboarding, briefly explain: supplied text goes to the remote MCP service; the tools compute previews and consistency checks, not writes. Offer the empty workspace via `phantom_open_review` or ask for the text the user wants checked. An example is optional, never a substitute for their own selected task. Do not ingest files, other conversation history or unrelated material automatically. Credentials and restricted sensitive data must not be sent to these tools.

For requests requiring unselected private-file discovery, live credential collection or validation, or deployment based on a receipt, explain the limitation without calling any Phantom tool. The same applies when asked only to describe the safe response to a quoted hypothetical request. Do not open the workspace as a capability check, integration check, or prerequisite for a refusal; selecting the plugin is not a request to initialize it. Open it when the user actually asks for the workspace or to supply selected review inputs interactively.

## Vocabulary into an exact preview

- For a user-supplied vocabulary pack, use `lexicon_describe_pack` first. Pass its exact `pack_digest` as `expected_pack_digest` when checking text with `lexicon_check_text_with_pack`. If the pack changes, describe it again; do not invent or reuse a stale digest.
- Report corrections as suggestions. Preserve code spans, line endings and untouched prose. In the workspace, corrections start unchecked; only user-selected corrections should enter the revision draft.
- Before `md_create_change_preview`, obtain the exact source text and explicit document/revision labels. These labels are not file access or verified editor state. Use end-exclusive UTF-16 code-unit offsets, exact `expectedText`, and separate edits for separate selected corrections. Never derive offsets from visually normalized text.
- Verify the returned preview with `md_verify_change_preview` against the same revision. If the source or revision changes, recompute rather than declaring the old preview current. A stale linked draft needs an explicit switch to manual editing and a fresh preview; no silent broad-diff fallback.
- The selected-correction context check sends the complete supplied current source. Explain this before requesting additional source that the user has not selected for the service. The workspace limits this path to 16 KiB; manual revision input is limited to 32 KiB. The complete serialized JSON-RPC request must be at most 65,536 UTF-8 bytes, even if a particular content schema allows more. Do not silently truncate.

## Receipts and reported evidence

Create `md_create_review_receipt` only with the user's explicit decision, scope, reviewer label, rationale and exact evidence. Never choose approval for the user. Verify using `md_verify_review_receipt` and the required scope. Include the caveat in the user-facing result, even for a comment receipt or a successful current check: reviewer identity is self-asserted; content consistency does not authenticate identity or authorize saving, execution or deployment. `usableApproval` is a consistency/scope result for the supplied decision, never permission to act.

For supplied test reports, `phantom_describe_test_artifact` describes what the report claims. Preserve failures. Importing a report into task evidence additionally requires independently supplied inventory and manifest facts; if absent, stop at description rather than inventing them. Do not call a report proof that tests actually ran or that the real run was complete.

Return the useful review outcome, the exact input/revision boundary, and any stale or failed checks. These tools cannot save the edits, execute tests, send a handoff, deploy, or grant authority for another tool to do so. Any separately requested action needs its own appropriate tool and authorization; do not infer permission from a receipt.
