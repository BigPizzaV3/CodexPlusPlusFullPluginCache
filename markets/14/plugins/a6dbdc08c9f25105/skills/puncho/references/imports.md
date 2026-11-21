### 4c. Imported ads: read them and write their copy

The human imports finished ads — Figma exports — into Generated ads. Each is a
concept whose image is the ad, waiting for you: no copy, placeholder
attributes, and it cannot be approved until you read it. When they ask for the
copy on imported ads:

1. `list_imported_ads`, then open every `imagePath` with `view_image` and look.
2. Load the `ad-copy` skill and `get_generation_context` for the voice.
3. `complete_imported_ad` per ad. `texts` is every word drawn in the image,
   top to bottom, exactly as drawn — transcribe, never correct or translate —
   with exactly one `HEADLINE`. Classify the ad as it is, not as you would have
   written it, `adFormat` and `productMode` included: without them its results
   fall in a group with no name. Then write `primaryText`, `headline` and `description` in the
   brand's voice; they sit beside the image, so they add to it and never repeat
   its words.
4. Your reading is saved, and the ad's picture then waits in `list_text_reads`
   for a blind read-back (see "Reading the words back"). Do it straight away:
   a human cannot approve the ad until that read is recorded, and a mismatch
   sends the ad back to this list with the words that differ. Look again and
   fix what you wrote.

**Videos.** An imported video (`kind: "video"`) is read from `framesPath` (open it
with `view_image`; raise `maxSide` to 2048 if captions are small): nine frames
across its whole length. Transcribe every word shown on screen across
them — titles, captions, subtitles — each distinct line once. You cannot hear
it: if it shows no words, pass `texts: []` and `hook` with the line it opens on,
and say you inferred it from the frames. Launch takes videos as it takes images.

**A corrected image comes back to this list.** When the human fixes a typo in
Figma and replaces the image on the board, words that changed put the ad back
to waiting for copy. Transcribe the new image and keep the rest of the reading —
attributes and Meta copy — unless the fix changes what the ad says.

**Ads made in Ads Manager.** `sync_insights` reports `unmatchedAdIds`: ads
spending that no concept owns, so their results are invisible. Say so, and
offer to link them: `list_unlinked_meta_ads` names them. The order is fixed,
because only an approved import can be linked: the human imports the same
creative; you read it (`complete_imported_ad`) and then read its words back
(`list_text_reads`), which is what lets them approve it; they approve it on
the board; and only then `link_meta_ad` joins them and takes the copy the ad
actually runs. A link cannot be undone from here, so never guess which concept
an ad belongs to: name the ad and the concept, and ask. Claude Code asks them
again before it runs.

Never render an imported ad; its image is finished. If it has no 9:16 version,
say so: the human adds it from the inspector, or Meta crops the 4:5 image for
Stories and Reels.
