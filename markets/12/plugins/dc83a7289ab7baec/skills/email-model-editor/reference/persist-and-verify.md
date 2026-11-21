# Persist and verify the edit

## 4. Preserve and edit native fonts

Custom fonts use `resources.fonts` in the native document. Use `email.setFonts([...])` to
replace the font-resource collection; include every existing resource still used by the email.
Each entry has `fontFamily` and `importMethod`: `link` or `import` requires a stylesheet `url`;
`fontFace` requires ready-to-inline `css` and accepts an optional source `url`.

Use the complete assigned stack as the resource key: `Inter, Arial, sans-serif` in settings
matches `fontFamily: "inter,arial,sans-serif"` in the resource. The editor canonicalizes case,
quotes, and spacing when matching. The family inside `@font-face` CSS stays the primary name.

Update native `fontFamily` settings through the SDK. Preserve requested fallback stacks and
unrelated inline typography. The validated output from `run-sdk.mjs` is the upload candidate;
its native schema and change checks apply to fonts just as they do to other fields.

## 5. Persist by file reference

Prepare two distinct update uploads for the same message and client:

```text
prepare_email_model_upload(message_id=<id>, operation="update")   # target: <updated-model.json>
prepare_email_model_upload(message_id=<id>, operation="update")   # base: <downloaded-model.json>
```

Upload the edited candidate to the target ticket and the byte-exact, untouched acquisition to
the base ticket through the host's authorized transfer mechanism. Never swap the files or ticket
IDs. Finalize with:

```text
update_email_model(
  message_id=<id>,
  upload_session_id=<target session id>,
  base_upload_session_id=<base session id>,
  expected_model_hash=<acquired modelHash>,
  idempotency_key=<fresh stable key>
)
```

The service merges only the base-to-target changes, preserving unrelated concurrent edits.
`expected_model_hash` verifies the uploaded base, not the newer live document. The idempotency
key binds both files: reuse it only for the identical base/target pair. A changed file requires
a new key. Both tickets are consumed on successful persistence; dry runs, no-ops, and failures
retain them. Expired or consumed tickets require fresh uploads of both files. A dry run validates
the inputs but cannot predict whether their changes will still apply to a changing document.

Never pass a model inline or drop `base_upload_session_id` to force a write. Without a base,
the service replaces the live document; that is not a recovery path for an edit conflict.
After an uncertain write or persistence failure, read the live model and durable export first.
If the requested changes are already saved, verify them and stop. If the intended node was
deleted, report the conflict without recreating it or retargeting the edit. Otherwise, reconcile
the requested change against a fresh acquisition, rerun the SDK module, and upload that fresh
base and target with a new key. Do not restore a stale snapshot. If readback fails, report the
uncertainty without writing again. Allow at most one repair retry before reporting the failure.
Treat `reason:"no_change"` as success only after checking the live requested values.

## 6. Verify durable state

A merge receipt reports `writeMode: "merge"`, `appliedModelHash: null`, and
`readbackRequired: true`; it is not the resulting document or proof of target equality.
Acquire a fresh model for verification and use that new file and hash for the next edit.

Verify `resources.fonts` and changed font-family settings in the fresh model. For font changes,
check the exported HTML/CSS font connections and inspect typography in both previews.

Read both surfaces after persistence:

```text
get_email_model(message_id=<id>)
get_email_message_preview_png(message_id=<id>, mode="both")
```

Download the fresh model and both PNG artifacts through the authorized transfer path. Inspect
the model for the exact requested values, link destinations, image URLs, alt text, merge tags, and
preserved content. Compare its depth-agnostic per-type block census with the acquisition census.
Structural node IDs may change between reads, so compare counts and types rather than those ids.
Saved-library `moduleId` values are persistent identities and must still match. For an explicit
module request, verify the requested ID and content on the final saved target; translated text,
a matching module count, or a successful write receipt alone cannot establish replacement.
After a structural edit, compare the census with the intended additions, removals, or duplication.
The merged result may also contain concurrent edits. Whole-target equality or an unchanged
block count is not required: verify the requested changes and investigate unexplained loss,
while preserving unrelated live additions and edits.
After a preheader edit, compare the fresh model's `metadata.preheader.text` and
`metadata.preheader.fillSpace` exactly with the requested values. Use `get_email_message_export`
to check the persisted canonical `esd-hidden-preheader` text, allowing the editor's invisible
filler; a clear must contain no old preview text. Duplicate canonical preheaders or unavailable
read-back are not success. Preserve the body, sending subject, and unrequested metadata.
For a preheader-only edit, these saved JSON and compiled-preheader checks complete verification;
desktop/mobile PNG checks are required when the request also changes visible content.

### Inline-style verification

For intentional inline-style changes, verify the requested CSS properties, values or removals
on the intended elements in fresh native content against the checked candidate, allowing harmless
serializer changes in quoting, whitespace, and declaration order. A write receipt does not
prove the styles were saved. An incorrect local candidate is a mutation failure;
a correct candidate followed by a native styling mismatch is a persistence discrepancy.
When the host exposes the saved HTML/CSS export, verify the requested CSS values or removals
and effective styling on the corresponding compiled elements before judging the PNGs. Correct
native CSS followed by an unexpected compiled styling mismatch is a compilation or rule
discrepancy. Report unavailable compiled-style verification explicitly.
If retained styling still renders incorrectly, inspect the affected elements, applicable rules,
and layout constraints. A preview showing literal merge placeholders does not establish a
recipient-data rendering defect.

To undo CSS property changes, reacquire live content and change only properties still matching
this repair, including continued absence after a removal: restore the acquired value of a
replaced or removed property, or remove only a newly added property. Preserve concurrent edits,
links, and merge expressions. Stop on a conflicting value and report it for reconciliation;
never restore a stale block or model snapshot.

Open and visually inspect both PNG files with the host's image-viewing tool. Check the requested
visible changes, text readability, image loading, spacing, alignment, clipping, and responsive
layout. A successful preview call or download alone is not visual verification. Screenshots do
not prove link destinations, asset URLs, or hidden values; use the saved model for those checks.
Compare against the untouched baseline and requested changes, not only the latest candidate.
Check that branding remains, text and buttons retain effective side spacing, and heading scale
works on mobile. Treat unrequested losses as defects, not as successful simplification.

If either preview shows a defect, write a targeted repair for the same draft, persist it, then
obtain and inspect fresh previews of both sizes again. Do not replay a successful structural edit
as a verification step. Stop when the requested result passes review or a concrete limitation
prevents repair. Report "saved, visual defects unresolved" with the defect if repair cannot
complete; do not describe that email as ready to launch.
If the preview includes `modelHash`, compare it with the fresh model manifest and reacquire on a
mismatch. A matching hash is supporting evidence, not proof that the rendered content is current;
confirm requested visible changes in the PNGs. Hidden preheaders use the checks above.
For a requested hosted preview link, call the discovered `get_email_message_view_link` operation.
Missing URL fields in an HTML/metadata export do not prove that this capability is unavailable.

Do not rerun the change module for verification. Report full success only when persistence, model
checks, and the required visual checks pass. If PNG generation, download, or inspection is unavailable or
fails after a bounded retry, report "saved, visual verification incomplete" when persistence and
model checks passed. Keep the same id for a later preview retry. Do not substitute an HTML
export, inspect HTML as the visual check, or repeat a successful write to obtain a preview.
