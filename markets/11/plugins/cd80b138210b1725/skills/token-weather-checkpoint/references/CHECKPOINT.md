# Checkpoint updates

Use a small JSON object, for example:

```json
{
  "decisions": ["Keep the full local plugin as a separate edition."],
  "next_action": "Inspect the final Skills-only archive.",
  "followups": ["Check the intended host before a directory upload."]
}
```

The existing checkpoint core validates fields, sizes, worktree identity,
generation and the current write lease. Do not bypass a rejected update.
Notes and evidence paths can contain private task information. They remain
in `.codex/handover-skills/<workflow>` until manually removed. Reading a checkpoint
does not authorise rerunning an external action.

Use short summaries rather than raw chats or tool output. Evidence paths must
be workspace-relative; store only the reference and hash needed for this task.
`prepare` and `bootstrap` read evidence files only with `--verify-evidence`.
Recorded hashes alone are not a current verification result. Common credential
patterns are rejected before writing; this does not detect all sensitive data.
Older ledger and generation copies remain after a note is updated. Read
[the privacy notice](../../../docs/PRIVACY.md) before explaining deletion.
