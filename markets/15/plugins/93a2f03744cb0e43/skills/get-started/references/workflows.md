# Worked sequences

Each step names the tool and the one fact to carry to the next. How to write
a good film is in [film-craft.md](film-craft.md).

## Make a launch film from a template

1. `create_project { name }`, then `set_brief` with what the product is, for
   whom, and the call to action, and `set_brand_style` with its colours.
2. `list_templates { usage: "launch" }` (or `feature`, `format: "9:16"`): keep
   the two or three whose `story` is true of the product.
3. `inspect_template { template }` on each: `fitsNot` rules one out. Every
   place has an `id`, its limits (`maxChars`, `maxLines`, `charsPerLine`), the
   template's `example` line and whether it is `required`. Places marked
   `fromBrief` (the name, the call to action) come from `set_brief`: do not
   write them.
4. Show the person the `preview.video` of your pick, in one sentence on why.
5. Add their screenshots and logo: `add_asset_from_url { projectId, url }` for
   each public image, keeping the `id` it returns.
6. `use_template { projectId, baseRevision, intent, template, look, lines: [{ id, text }], pictures: [{ id, assetId }] }`
   with every required line written by you, within its limits. A refusal
   names the line (`operationIndex`) and why; fix that line and send again.
   It replaces the whole film: ask first when the film already has shots.
7. `apply_turn { projectId, turnId }`: the answer is `awaiting_studio`. Tell
   the person their open Studio places it, then poll `get_turn` until
   `appliedRevision` is set.

## Make a film of a release

1. `create_project { name }`, then `set_brief { projectId, workflow: "feature_announcement", releaseUrl }`
   with a public GitHub release (`.../releases/tag/<tag>` or `.../releases/latest`)
   or a public changelog page. It answers the `brief` it wrote and the `release`
   it read: show the person the title and the changes, and call `set_brief`
   again with your own `brief` to correct a line. A private repository reads
   as no release.
2. `list_templates { usage: "feature" }` (or `changelog`), then the launch film
   steps from step 3, writing the lines from the release's changes only.

## Retitle the opening shot

1. `get_project { projectId }`: keep `project.studio.revision`.
2. `find_layers { projectId, shot: 1 }`: pick the layer whose `text` is the title.
3. `inspect_layer { projectId, layerId }`: find the `text-content` control's
   `field` and its limits (`maxChars`, `charsPerLine`, `maxLines`).
4. `propose_edits { projectId, baseRevision, intent, operations: [{ type: "setText", layerId, field, value }] }`:
   read `fit` (a line too wide for its box: shorten it or split it) and
   `exportLosses` before going on.
5. `apply_turn { projectId, turnId }`: keep `appliedRevision` as the next `baseRevision`.

On a film made from a template, `inspect_layer` lists only the template's
places, each with its limits; a change outside them comes back
`rejected_operation` with the limit in `message`.

## Change the brand, the font, the music or the format

1. `list_library { kind: "music" }` for a track by mood (or `kind: "sounds"`
   for effects).
2. `edit_film { projectId, baseRevision, intent, edits }`: the brand name, the
   logo (an asset `id`), the brand colours, the font, the music and its level,
   effects on a shot, the narrator, where a shot or one of its elements sits,
   and the format.
3. `apply_turn`: the answer is `awaiting_studio`; poll `get_turn` as above.

## Repaint a film in the brand colours

1. `get_brand { projectId }` for the three colours (ground, accent, ink).
2. `find_layers { projectId }` returns 12 layers at most; when `omitted` is not
   zero, ask again shot by shot (`shot: 1`, `shot: 2`, ...) until every layer is read.
3. `inspect_layer` on each layer, keeping its `color` controls.
4. One `propose_edits` batch of `setColor` operations (32 at most), then `apply_turn`.

## Place a picture

1. `list_assets { projectId }`: pictures of `kind: "image"`.
2. `inspect_layer` to find an `image` or `asset` control.
3. `propose_edits` with `setAsset` and the asset `id`. A URL or a `data:` URI is refused.

A picture that is not in the project yet: `add_asset_from_url { projectId, url }`
with its public HTTPS address first, then use the `id` it returns. A project
that is full answers `asset_limit_reached`: reuse a picture already in
`list_assets` or ask the person to remove one.

## Join two shots with a transition (free film)

1. `list_transitions` for the names and the three lengths.
2. `propose_edits` with `{ type: "setTransition", scene: 2, transition: "whip-pan-right", length: "short" }`
   (the passage INTO shot 2), then `apply_turn`. `transition: null` cuts.
   A template keeps its own transitions.

## Add or remove a shot

1. `find_components { query }` for a component and its text fields.
2. `propose_structure { projectId, baseRevision, intent, operations: [{ type: "addShot", component, text }] }`.
3. `apply_turn`: the answer is `awaiting_studio`; poll `get_turn` before the next change.

## Show a product screen no template carries

1. `get_project` for `baseRevision`, `list_assets` for a screenshot to frame
   (a real screenshot alone beats a composed one: place it with `setAsset`).
2. `compose_screen { projectId, baseRevision, intent, screen: { version: 1, tone, blocks }, images, seconds }`:
   a `window` over the whole grid (col 1, row 1, w 12, h 8), two or three
   `card`, `list` or `badge` blocks inside it with a column of margin and no
   two touching, one `button`, and an `image` block naming `image: 1` for the
   first of `images`. Words and figures come from the person.
3. A refusal is `rejected_operation` with `reason` (the first issue) and
   `issues`: every block at fault, the format (`16:9`, `1:1`, `9:16`) and a
   hint such as the characters that fit. Fix all of them and call again.
4. `apply_turn`: `awaiting_studio`, the Studio adds it as the last shot. To
   change it later, `compose_screen` again with `scene` set to its shot.

## A free film when no template fits

`start_storyboard_job { projectId, prompt }` writes a film from a prompt and
spends the person's AI generation budget; `get_storyboard_job` until it
succeeds, then the person places it by opening the project in the Studio.
Prefer a template.

## Export and fetch the file

1. `check_export { projectId }`: `blocked` says why; `ready` gives `playedSeconds` and `notes`.
2. Tell the person the export spends credits, only if it succeeds, and ask.
3. `start_render { projectId, baseRevision }` with the `scenivia:render` scope.
4. `get_render` every 15 to 30 seconds until `succeeded` or `failed`.
5. `get_render_download`: the link lasts five minutes; ask again rather than keep it.
6. On `failed`, `retry_render { projectId, renderId }` redraws the film as it stands.
