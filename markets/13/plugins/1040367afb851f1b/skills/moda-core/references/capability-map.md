# Everything Moda can do

One table set, whole surface. **FREE** = deterministic and unlimited. **METERED** = charges
credits; the model cards publish each model's price and billing basis, every result carries a
usage receipt, and `moda_bootstrap` reports the balance.

Ids are prefixed (`cvs_`, `bk_`, `file_`, `fld_`, `task_`); anywhere a canvas is named you may pass
its id, a raw UUID, or a pasted moda.app canvas or share URL.

## Canvas authoring — FREE, the substrate under decks, documents, social, diagrams

| Do | Verb |
|---|---|
| Create pages, sized by category or from a team template, with a brand kit bound | `canvas_create` |
| Add content in Moda markup — append, or an atomic whole-page replace | `canvas_apply_markup` |
| Add more pages to an existing canvas | `canvas_edit create('page', …)` |
| Edit precisely: sandboxed JS over the short node ids, all-or-nothing | `canvas_edit` |
| Read state: lossless snapshot, whole-canvas, page-scoped, or a summary index | `canvas_read` |
| See it: page images, three per call, with degradation warnings | `canvas_screenshot` |
| Delete nodes, pages, or the canvas (soft delete) | `canvas_delete`, `canvas_delete` |
| Reuse pages from another canvas, including cross-team via a share token | `canvas_import_pages` |
| Copy a whole canvas as-is, then edit the copy | `canvas_create(template_canvas_id=…)` |
| Rename, re-describe, re-brand, or flag as a team template | `canvas_update(name=…)`, `canvas_update(brand_kit_id=…)`, `canvas_update(template_type=…)` |
| Read a canvas's owner guidance before editing someone else's work | `canvas_read (agent_instructions)` |
| Read the comment threads reviewers left on a canvas | `canvas_comments` |
| Share: a public link, view-only or view-and-remix | `canvas_share` |
| Find work again: newest first, or by name | `canvas_list`, `canvas_search` |

Resize in place is a recipe, not a verb: group the page's content, set the new page size, scale the
group. Never recreate a canvas to resize it.

Markup speaks 24 elements: shapes, paths, lines, anchored connectors, rich text (markdown or HTML,
with hyperlinks), image fills (`src`, or `icon="query"` for a searched UI icon), video fills, groups
and clip masks, flex rows/columns/layers, HTML tables, charts (bar, line, area, scatter, combo, pie
from pipe-delimited rows), QR codes, LaTeX, maps, backgrounds (solid, gradient, procedural shader,
image), comments, `repeat`, and JS `generate` blocks. Fills take gradients and shader fills;
effects are shadow, layer blur, and backdrop blur/glass.

**Scripts and languages.** Text is vector-shaped: full Unicode, including CJK, and complex scripts
(Arabic, Hebrew, Indic, Thai) shape and reorder correctly inside a paragraph. Paragraph base
direction is left-to-right today, so for an RTL block set `text-align="right"` yourself and confirm
with a screenshot. Missing glyphs fall back to a Noto family, and an export warns
`font_substituted` when a requested font could not be used.

## Formats it produces

| Artifact | What lands | Skill |
|---|---|---|
| Slide decks | native editable PPTX (real shapes and text layers) or text-layer PDF; PowerPoint import runs in the Moda app (moda-deck-pptx routes there) | moda-deck, moda-deck-pptx |
| Documents and reports | one page or fifty; real PDF with selectable text (unflattened keeps links live) | moda-document |
| Print pieces | poster, flyer, brochure, menu, resume, certificate, invitation, business card | moda-document-print |
| Social creative | platform-sized posts, stories, carousels (multi-page images arrive as one zip; a LinkedIn carousel is ONE PDF), channel art, ad and banner sets | moda-social and its children |
| Diagrams | flowcharts, org charts, architecture, swimlanes, 2x2s — connectors stay anchored when nodes move | moda-diagram |
| Data charts | bar, line, area, scatter, combo, pie from a CSV, a table, or pasted numbers | moda-chart |
| UI mockups | app and site screens at real viewport sizes — pictures of interfaces, not hosted pages | moda-mockup |
| Websites | multi-page hosted sites at a public `*.moda.page` URL; reads are live here, building and publishing are app-only | moda-website |
| Motion and video | keyframes, easing, staggers, timeline cuts and transitions; one animated page exports mp4 or gif, FREE | moda-video-motion |

## Image generation inside designs — METERED

`canvas_edit_image` requires a canvas and existing image-capable node. operation.kind selects generate, edit, outpaint, remove_background or upscale. The call waits for placement; then inspect with canvas_screenshot. If still working, repeat the identical call to wait on the same job. Load `omni-and-media` for shared image craft and live model capabilities. Standalone image/audio/video generation, video reframe and video upscale are unavailable.

Existing assets remain usable: `media_remove_background` for ordinary matting, `media_fetch_logo` for company marks, and `media_video_frames` for frame inspection. The latter two are FREE.

## Brand kits — FREE

List kits and read model-safe tokens (palette, fonts, tagline, logos, guide prose); create a kit
from a website URL **or** from tokens the user gave you — never both in one call; update it
(palette and font lists REPLACE wholesale), attach images, set the team default, and audit an
existing canvas against the kit. Bind the kit at create time; never retype hexes from memory.
`brand_list`, `brand_show`, `brand_create`, `brand_update`, `brand_show(guides=true)`.

## Files, drive, templates — FREE

Upload local files or by URL; search team assets, stock photography (placeable directly, with the
result's attribution credited wherever the photo appears), and icon packs; read an uploaded PDF,
DOCX, PPTX, XLSX, or CSV as text — the "ground the design in the user's own brief" lane; browse and
organize folders (a folder owns its contents' visibility); list team templates, LOOK before
choosing (a template IS a canvas — screenshot it), then instantiate one as a full copy; or search
single pages inside templates and themes and import just the one you need.
`upload`, `file_search`, `file_read`, `drive_tree`, `drive_organize(action='create_folder')`,
`drive_organize(action='move')`, `drive_organize(action='set_visibility')`, `template_list`, `template_list + canvas_screenshot`,
`template_search`.

Moda designs NEW pages grounded in the user's files; it never rewrites the uploaded source file in
place. A DOCX or PDF goes in as reference and comes out as a new designed artifact.

## Delivery and jobs — FREE

Export png, jpeg, pdf (flattened by default; unflattened keeps text selectable and links live),
native pptx, and mp4 or gif from one animated page (`export`). Read the typed warnings channel
— rasterized shapes, dropped content, flattened links, substituted fonts — and relay caveats
honestly rather than withholding the file. A long render returns a job handle: poll it with
`task_status`. An identical re-call reuses the job instead of running it twice.

A long `queued` is not always queue contention — a task whose attempt died is retried
automatically and sits in `queued` through the backoff. `attempts_started` counts attempts BEGUN
(`0` = never claimed), and the claim itself increments it, so `queued` + `attempts_started >= 1` is
a retry while `running` + `attempts_started == 1` is an ordinary first run — the threshold is `>= 1`,
not `>= 2`. On a non-terminal task `error` describes the PREVIOUS, already-dead attempt: keep
polling, do not report the job failed or start a replacement. `created_at` → `first_started_at` is
the true queue wait (`started_at` restarts on every attempt, so it overstates it); `first_started_at:
null` means unknown, never "never started".

## Meta — FREE

`moda_bootstrap` (identity, plan, teams, entitlements, remaining credits — and the health check),
each tool's own description and schema as ground truth, the typed error on any failed result, the
`team` argument for workspaces, the loadable skill guides, and `ask_expert` — the live product
expert, free. There is no install step, no update step, and no repo-level config here.

Some lanes live elsewhere: web research is your host's own browsing, PowerPoint import runs in
the Moda app, and local footage analysis and OpenTimelineIO timeline interchange run on the
user's own machine, outside this surface.

## Not available here — say so plainly, and route to the Moda app

- **Creative identity work** — generating a brand-guide document (kits are read, created from a URL
  or tokens, and applied here; the guide itself is authored in the app).
- **Decomposing a flat image into editable layers** — the in-app design agent serves exactly this.
  Hand over the app link; do not decline, and do not fake it with traced shapes.
- **Stateful hosted web apps** behind a site, and site authoring beyond what moda-website teaches.
- **Sending mail.** There is no send verb and no mail provider — delivery is always the user's own
  ESP. The email HTML itself is NOT outside Moda: the canvas pipeline never emits it (it exports
  png/jpeg/pdf/pptx/mp4/gif), but you write the self-contained document out yourself — load moda-document (or
  moda-website), which carries the email-HTML craft.
- **Any generation mode the roster does not list.** `load_skill("omni-and-media")` is the authority; check it
  before promising an image mode. Audio and video generation are unavailable on this connector.

When something is genuinely outside Moda, say so in one line, then offer the nearest thing Moda
CAN do. Unsure whether it is outside? `ask_expert` first — free, and faster than a wrong no.
