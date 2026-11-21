# Import Fiteno templates

Available only to Reteno publishers. Use the selected organization's MCP connection.
`<skill-dir>` is the installed `reteno-email-editor` directory for the current provider;
resolve assets and scripts from that directory, for both Codex and Claude.
Follow MCP callable discovery in `../SKILL.md` before preparing an upload.

`../assets/fiteno/abandoned-subscription/index.json` lists the 17 templates. Each `<slug>/` holds:

- `model.json` — the complete native editor model, including Inter and Poppins font stacks,
  their `resources.fonts` declarations, and the native preheader in `metadata.preheader`.
- `metadata.json` — `name`, `subject`, `tags`, `blockCount`, and `modelSha256`.

Upload each model exactly as packaged. Never edit, recompose, or rebrand it, and never re-upload
its images: they are hosted on `picscdn.io` and serve from any organization.

## 1. Resolve

- **Templates.** All 17 unless the user names some; match by slug or `name`. For several organizations,
  finish and verify each organization separately with its own sender and MCP connection.
- **Kind.** Saved Templates (`template: true`) unless the user asks for regular emails.
- **Sender.** Call `list_email_interfaces`. The sender must equal one interface `value` exactly.
  If the user named a sender that is not in the list, stop and say so. If they named none and
  there is more than one, ask. With exactly one, use it.
- **Duplicates.** Search existing emails for each `name`. If any already exists, ask before
  creating a second copy.

## 2. Create each template, one at a time

1. `create_email_shell(name, subject, tags, sender, template)` with the values from
   `metadata.json`. Record the new message ID.
2. `prepare_email_model_upload(message_id=<id>, operation="create")`.
3. Upload the template's `model.json` to the returned upload URL:
   `python3 <plugin-root>/scripts/transfer.py upload --url <upload-url> --input <model.json> --content-type application/json`
4. `update_email_model(message_id=<id>, upload_session_id=<session id>, idempotency_key=<slug>-<id>)`.

Never pass the model as a tool argument, and never set the preheader separately: it travels inside
the model.

## 3. Verify

An acknowledgement is not proof. For every template:

1. Call `get_email_model(message_id=<id>)`, download the model with
   `python3 <plugin-root>/scripts/transfer.py download --url <download-url> --output <live.json>`,
   then run
   `python <skill-dir>/scripts/check_fiteno_template.py --template-dir <slug dir> --live-model <live.json>`.
   It checks the block count, fonts, font resources, and preheader against the packaged template.
2. Call `get_email_message_export(message_id=<id>)` and confirm `template` matches the requested kind.
3. Obtain and inspect saved desktop/mobile PNG previews; report incomplete visual verification if either is unavailable.

If the check reports a single placeholder block, the model did not land. Repair once on the
**same** message: `prepare_email_model_upload(operation="update")`, upload, `update_email_model`,
then check again. Never create a second shell for a repair. A validation or transport failure stays unresolved until both the receipt and fresh read-back establish success. After an uncertain write, inspect the same ID first. For a repair update, acquire its fresh model, retain that exact base and use the native base/target merge workflow; never replace a populated document with a stale snapshot.

## 4. Report

One row per template: name, message ID, kind, blocks, preheader, and verified status. Never send,
schedule, or activate anything.
