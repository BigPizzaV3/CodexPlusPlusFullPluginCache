# Create, persist, and verify

### 6. CREATE the shell

For an explicit full rebuild, skip shell creation. Acquire the named target with `get_email_model`,
download its untouched model as `<shell-model.json>`, and preserve its `modelHash`. Use that
baseline and the same message id throughout persistence and repair.
Set the brief's `model.settings` and font resources from the requested source design. The builder
fills schema defaults; do not copy the target's visual settings merely to make a rebuild complete.
The target model supplies the persistence baseline, while the reference supplies typography,
width, borders and layout.

For creation, call `create_email_shell` once with the resolved Reteno message metadata, then
call `get_email_model` and retain the untouched shell as the baseline. Font definitions and
assignments are already in the complete candidate document. Keep the extracted brandkit and
brief unchanged. After an ambiguous create, find the existing message before retrying.

After acquiring a new shell, rerun the builder with `--baseline <shell-model.json>` using the
same creation brief, output, and diagnostics paths. This validates against the actual target
and records the intended replacement of its shell sections. Keep this output for persistence
retries; do not rerun the builder after a successful save.

### 7. PERSIST the new Reteno model

The complete model carries `metadata.preheader` through the same upload and finalize as the
body. Never call `update_email_metadata(preheader=...)` or hand-edit `esd-hidden-preheader`.
After persistence, verify the exact native `text` and `fillSpace` in a fresh `get_email_model`
download, and verify the compiled hidden preheader in `get_email_message_export`. Allow
invisible filler in the compiled text; reject stale or duplicate canonical preheaders. A
successful HTTP acknowledgment alone does not prove a requested preheader was saved.

1. Call `prepare_email_model_upload(message_id=<new id>, operation="create")`.
2. Upload `<new-model.json>` to the returned upload URL through the consuming agent's authorized transfer mechanism.
3. Call `update_email_model(message_id=<new id>, upload_session_id=<session id>, idempotency_key=<stable key>)`. Never pass the complete model as a tool argument.

For a rebuild, replace `<new id>` with the explicit target id and pass
`operation="update"` to **both** upload preparations. Upload the complete rebuilt candidate to
one ticket and the untouched acquired target to a separate base ticket, then finalize:

```text
update_email_model(
  message_id=<target id>,
  upload_session_id=<target session id>,
  base_upload_session_id=<base session id>,
  expected_model_hash=<acquired modelHash>,
  idempotency_key=<stable key for this base/target pair>
)
```

`expected_model_hash` verifies the uploaded base. The service applies the base-to-target changes
on top of the current document. Never swap the two tickets or drop `base_upload_session_id` to
force a write. Creation does not accept a base ticket or `expected_model_hash`; use the three
create steps above only for a registered new shell. Apply an explicitly requested subject change
through `update_email_metadata` and verify its read-back.

Merge receipts report `writeMode: "merge"`, `appliedModelHash: null`, and `readbackRequired: true`.
Reacquire the saved model; it may include concurrent changes and need not equal the submitted
target. Use its fresh file and hash for the next edit. Successful persistence consumes both
tickets; dry runs, no-ops, and failures retain them. Expired or consumed tickets require fresh
uploads of both files. A dry run cannot establish that a later merge will succeed.

After an uncertain merge or persistence failure, read the live model and durable export before
retrying. Verify already-saved changes rather than writing them again. A deleted target node is
a conflict: report it without recreating it or restoring a stale snapshot. Otherwise reconcile
against a fresh acquisition and use a new idempotency key when either file changes. Reuse a key
only for the identical base/target pair. If readback fails, stop and report the uncertainty.
Allow at most one repair retry before reporting the failure.

If an authorized local image must be persisted, follow [Upload supplied images](image-upload.md)
before building the model. A completed host image job already returns a hosted URL: use it
directly without another upload or compression pass.

If persistence or verification fails, read the live state and repair the same draft. Use its
fresh untouched model as the baseline for bounded repairs; preserve node IDs and unrelated
settings and font resources. Rebuild through the SDK, inspect the model diff, and do not
repeat an identical rejected payload. Initial-create retries retain the
original shell baseline until a write succeeds.

Reteno can canonicalize native fields during a successful save. Never append sections or
repair layout by editing the pre-save candidate; download the fresh saved model first and
apply only the next bounded change to that file. If a complete initial document returns
`document_state_set_failed` and read-back still shows only the shell, isolate the failure on
the same draft: try an ordered prefix of the candidate, read the resulting model, then append
remaining sections from that fresh baseline in small groups. If a group fails, narrow it to
the offending section or field; do not drop the rest of the email or create another shell.
Retain the original section order and IDs, and verify the final native model and both PNGs.
This staged recovery is a sequence of distinct, read-back-guarded changes, not repetition of
the rejected full payload. Report any native block that still cannot be saved.

### 8. VERIFY

Verify the saved `resources.fonts` and requested font-family assignments in the fresh model;
confirm font connections in exported HTML/CSS and typography in both previews.

Re-read the saved message with `get_email_model(message_id=<new id>)` and request
`get_email_message_preview_png(message_id=<new id>, mode="both")`. Download the fresh model and
both PNGs through the host's authorized transfer mechanism.
When a hosted view link is requested, discover and call `get_email_message_view_link` for the
saved message. The metadata/HTML export is not the view-link operation; absent URL fields in
that export do not establish that a hosted link is unavailable.

Inspect the saved model for every intended block, exact copy, CTA href, asset URL, merge tag,
unsubscribe link, and postal/legal detail. Compare the per-type block census with the intended
model.
Verify the stored subject and sender from the preview manifest's `subject` and `sender`
fields or the host's authorized metadata read; do not infer hidden metadata from an image.

For intentional inline styling, follow the shared [inline-style verification](../../email-model-editor/reference/persist-and-verify.md#inline-style-verification)
before judging the saved previews.

Open and visually inspect both PNGs with the host's image-viewing tool. Compare the desktop and
mobile layouts with the reference intent, including readable text, loaded images, spacing,
alignment, clipping, and the CTA. A successful tool call or download alone is not visual
verification.
Compare the saved desktop/mobile previews with the original reference and intended changes,
not only with the most recent generated model. Account for missing branding or blocks, actual
side spacing around text and buttons, and heading scale on mobile. A deliberate design change
is valid in Tailored or Creative when it serves the request; Exact changes require the user's
instructions or a documented native limitation.
For an agent-authored text reference, review both saved previews against its proposed structure,
copy, primary action, and visual direction. No source PNG comparison is required when none
exists; the saved desktop and mobile visual checks are still required.

For **Exact**, when source PNGs are available, compare PNG to PNG against the original source
at matching viewport widths.
Check content order, section dimensions, colors, typography, spacing, image crops, alignment,
and mobile stacking. Correct visible differences in the same draft and repeat the comparison.
Use side-by-side views or an overlay; a pixel-diff score alone cannot establish fidelity.
If only one source viewport is available, compare that viewport and separately inspect the
other target layout, stating that its source comparison is unavailable. If perfect reproduction
is impossible, keep the closest editable result and report the specific differences and causes
(for example an unavailable font, asset, or unsupported layout). Do not claim an exact match
or silently change to Tailored or Creative.
When source PNGs are unavailable, compare the saved model and available target previews with
the inspected source HTML/CSS and report that source visual fidelity is unverified. Continue
the saved-target checks below; missing source PNGs do not require another user-supplied artifact.

If either preview shows a defect, repair the same draft, persist it, then obtain and inspect
fresh previews of both sizes again. Use the existing model-editor workflow for a saved draft;
do not rerun an insertion or duplication module just to verify it. Stop when the intended result
passes review or a concrete limitation prevents repair. In the latter case, report "saved,
visual defects unresolved", name the defect, and do not describe the email as ready to launch.
If a preview supplies `modelHash`, compare it with the fresh model manifest and
reacquire on a mismatch. Matching hashes do not replace inspecting the rendered content.

Report full success only when the persisted id exists, persistence and model checks pass, required
metadata reads back correctly, and both visual checks pass. If PNG generation, download, or
inspection fails after a bounded retry, report "saved, visual verification incomplete" when the
other checks passed.
Keep the same message id for a later preview retry; do not create another
shell or repeat a successful write. Never use an HTML export as the visual-verification fallback
for the saved target; rendering source HTML as reference evidence is allowed.
Return the message id and a concise summary of deliberate deviations from the references.
