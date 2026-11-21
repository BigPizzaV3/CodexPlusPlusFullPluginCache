# Generate, inspect, then separate


Use only the host's built-in image tool, never Anga's story-assist endpoint or a
paid API. The request authorizes the listed targets and at most one corrective
regeneration per defective sheet. It does not authorize extra variants or
replacing existing pictures. A sample is one standalone image and never a batch.
Compare the latest draft to the approved snapshot before generation and before
attachment. If story text, characters, stage, locale or style changed, stop for
review. Preserve the latest version and existing images.

For multiple targets:

1. Plan a sheet with **at most nine square panels**. Use a 2×2 or 3×3 layout as
   appropriate, with a row-major map from each occupied cell to cover or page
   ID. Leave unused cells blank; no extra scenes. Keep consistent characters,
   style and palette, but vary camera distance and action. No labels, borders
   over scenes or lettering. For more than nine targets, use separate sheets
   and the same character reference. Never cram more panels onto one sheet.
2. **Inspect the full generated sheet with vision before cropping.** Check
   every cell against its page: intended scene and objects, consistent faces,
   clothes and proportions, hands/limbs, merged or duplicated objects, missing
   characters, unwanted text, scary details, panel order and count, and subjects
   crossing cell edges. Record pass/fail and any defects by cell. Do not claim
   a visual check based only on the prompt, file existence or dimensions.
3. If any cell fails, regenerate the defective sheet once with explicit fixes
   and the accepted character reference. Inspect the new sheet again. If it
   still fails, or visual inspection is unavailable, stop and explain; do not
   crop or attach a known defective sheet. Ask the adult before further attempts.
4. After the sheet passes, inspect actual panel boundaries and crop each
   approved occupied cell separately, excluding gutters and neighbouring art.
   Use the packaged `scripts/split_sheet.py` when local Python with Pillow is
   available. Supply measured square boxes and the recorded visual review.
   The script validates geometry; it does **not** perform vision. In a host
   without local execution, use available image-processing tools or explain
   that automatic separation is unavailable. Never pass a whole sheet off as
   one page picture.
5. Inspect the resulting crops with vision for seams, cut-off details and
   accidental neighbouring panels. Prepare metadata-free square JPEGs within
   Anga's limits. Transfer each as a real host file attachment to
   `attach_story_illustration`, then assign its confirmed `imageId` to the mapped
   cover/page with a versioned draft update. Never send a local path or invented
   URL to the tool. Re-read after a conflict and preserve the adult's edits.
6. Let the open Studio refresh, or open the draft if the panel is closed. Report the pictures as attached only after tool
   confirmation. The adult reviews the whole illustrated story before saving.

If transfer is unavailable, say the pictures are not attached and offer Studio
upload/cropping with the prepared individual files. Never hide a partial batch
or claim a library save. Temporary file URLs never enter story text or notes.
Do not expose tokens, passwords or account identifiers.

