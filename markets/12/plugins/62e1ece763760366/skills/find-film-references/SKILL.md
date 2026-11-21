---
name: find-film-references
description: Find, inspect, discuss and attach Cineboard Film Search frames to Shot Cards or Moodboards, including continuing a search, choosing a numbered frame, replacing a reference, and saving a spoken or typed selection. Use in an active Cineboard workflow without requiring another plugin mention.
---

# Film reference workflow

Discover connected tools and use `get_capabilities` before saying the operation
is unavailable. Keep the established account/project and read the requested shots.
Call `get_film_search_status`, then `search_film_references` with concise visual
terms, its period and a stable requestId. Every new search costs one allowance
unit. A Shot Card search binds its exact returned target, including proposalId
for an unsaved draft; it need not be saved before searching or selecting.

Reuse stored results with `get_film_search_results`. Its offset pages the existing
batch for free. Use returned frameNumber; never reconstruct numbers from another
search. `inspect_film_frames` supplies actual pixels. Describe only what those
pixels show, retaining differences from the shot. Metadata is supporting evidence.

Show an exact candidate with `render_film_search_results` using the same requestId,
period, target and focusFrameId. It opens that frame enlarged, with Back to results
returning to its containing page. Do not search again merely to show an image.
Use that native card as the authoritative photo, not a web image or generated
illustration labelled with its film name/number. If a previous displayed image
disagrees with the stored frame, show the actual candidate before accepting an
ambiguous 'save that' instruction.

An explicit spoken/typed 'use this for 2B' after viewing that exact frame is the
same authorization as its save button. Call `save_film_reference` with the stored
requestId/period, frameId, current target, role and mode. `replace` replaces
the reference set with this frame; `add` preserves existing photos.
Ask which only when the user has not made their intent clear. Preserve shot text
and technical fields. Validate the returned frame and target identity and status;
draft target attachment updates the draft, not the saved storyboard. Whole-draft
saving still uses the returned `delivery.reviewed.nextTool` on the approved version.

For model-curated multi-shot proposals use `propose_storyboard_references`, inspect
its native preview, then apply the exact version upon approval. For Moodboard use
`propose_canvas_reference_addition` with authorized frame receipts and review/apply. Reuse
existing saved media without another search or duplicate upload. User-requested
web/attached images use `propose_image_reference` with their actual source; never
present them as a numbered Film Search result. For multiple photos, combine pending
Storyboard drafts through revise_storyboard_references companions with replacements: [].
For Moodboard, combine them through propose_canvas_composition companions. Render
one complete proposal after combining, then save its exact approved version; never
claim all photos were saved because the last individual draft succeeded.

Read a receipt after an uncertain response. A genuine auth failure needs the
account connection flow; denied access and temporary capacity are different
errors. Do not tell users to repeat the plugin name as a recovery mechanism.
After saving, return the exact editor link and useful scene/reference status.
Render current Storyboard/Moodboard when requested; no extra host image montage.
