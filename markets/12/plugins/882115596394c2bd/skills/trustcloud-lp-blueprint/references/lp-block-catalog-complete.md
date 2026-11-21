> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# LP Block Catalog (Complete)

## Scope

This is the complete block-type catalog for event LP authoring.
Source of truth for schema enforcement is:
`apps/api/src/trustcloud/features/events/_shared/dto_lp_metadata.py`
(`LP_BLOCK_TYPES`) and the generated Web contract.

## Complete Block Types

Total block types: `29`

`section`, `hero`, `free-design`, `kpi`, `buttons`, `header`, `text`, `image`, `media`, `form`, `cardgrid`, `benefit`, `publisher`, `relatedevents`, `comparison`, `calendar`, `faq`, `map`, `specs`, `gallery`, `notice`, `share`, `spacer`, `stickycta`, `script`, `testimonials`, `process`, `metrics`, `policy`

## Catalog

| Block Type | Purpose | Required Content Keys | Recommended Keys |
|---|---|---|---|
| `free-design` | Responsive HTML/CSS composition with editable bound content | `title`, `html` | `css`, `texts[]`, `images[]` |
| `section` | Section heading and transition | `title` | `subtitle` |
| `hero` | First-view key visual and semantic event identity | none (schema) | `title`, `subtitle`, `imageUrl`, `visualMode`; `ctaText`, `ctaAnchor` only for overlay heroes |
| `kpi` | Highlight one KPI | `value`, `label` | `subLabel` |
| `buttons` | CTA group | `buttons[].label` + (`buttons[].href` or `buttons[].anchor`) | `buttons[].variant` |
| `header` | Heading text block | `text`, `level` | - |
| `text` | Narrative text | `text` | - |
| `image` | Single image | `url`, `alt` | - |
| `media` | Split/stacked/editorial/photo-story media narrative | `title` | `presentation`, `body`, `imageUrl`, `imageAlt`, `chips`, `list`, `metaItems`, `note` |
| `form` | Lead/contact form | `title`, `fields[]` | `submitLabel`, `note` |
| `cardgrid` | Structured proof cards | `cards[]` (`cards[].title`) | `columns`, `cards[].text`, `cards[].icon` |
| `benefit` | Single visit benefit or conversion incentive | `title`, `label` | `description` |
| `publisher` | Current publisher profile and company-site link | `title` | `showLogo`, `showAddress`, `showPhone`, `phoneSource`, `showHomepage` |
| `relatedevents` | Current published events from the same branch or organization | `title`, `scope` | `limit` |
| `comparison` | Left/right comparison table | `leftTitle`, `rightTitle`, `rows[]` | `caption` |
| `calendar` | Reservation slot entry | none (schema) | `title`, `note` |
| `faq` | Objection handling Q&A | `items[]` (`items[].q`, `items[].a`) | - |
| `map` | Venue/access information | none (schema) | `address`, address parts, `detailItems`, `directions` |
| `specs` | Spec/key-value table or editorial fact spread | `items[]` (`items[].key`, `items[].value`) | `title`, `eyebrow` |
| `gallery` | Multi-image showcase | `images[]` (at least one valid image URL) | `columns`, `presentation` (`grid` / `editorial`), `images[].alt`, `images[].caption` |
| `notice` | Important notice/disclosure | `text` | `style` |
| `share` | Social share controls | none (schema) | `showX`, `showFacebook`, `showLine` |
| `spacer` | Vertical spacing control | none (schema) | `size` |
| `stickycta` | Persistent CTA | `label`, `href` | - |
| `script` | Script injection | `code` | `placement` |
| `testimonials` | Social proof quotes | `items[]` (`items[].quote`) | `items[].author` |
| `process` | Reservation/visit steps | `steps[]` (`steps[].title`) | `steps[].text` |
| `metrics` | Prominent source-backed figures | `items[]` (`items[].label`, `items[].value`) | - |
| `policy` | Policy/terms notices | `items[]` | `title` |

## Optional Rendering Choices

For a new full LP or complete redesign, author the body in free-design HTML/CSS.
Use native rendering options for real functions and fitting compositions. Do not
apply every option or reuse one treatment across the page. Omitted/null options
keep default renderer behavior; copy-only edits preserve options already present.

| Scope | Field | Choice |
|---|---|---|
| `hero` | `content.imageHeightMode` | Prefer `natural` when the artwork's original ratio should define its full-width composition or a finished text-bearing key visual would lose lettering to a framed crop; omit or use `framed` when natural height does not fit. `image-only` and `imageFit=contain` alone do not imply natural height. |
| `hero` | `content.composition` | `editorial-cover`, `framed-photo`, `split-panel`, or `photo-spread`, based on the artwork and copy. |
| `section`, `cardgrid`, `metrics`, `specs`, `faq`, `notice` | `content.presentation` | Prefer `editorial` when that block's information structure benefits; omit only where legacy rendering better fits. |
| `media` | `content.presentation` | `photo-story`, `editorial`, `split`, or `stacked`, based on the image and explanation. |
| `gallery` | `content.presentation` | Prefer `editorial` when a deliberate size hierarchy helps; otherwise keep the standard grid. |
| `calendar` | `content.presentation` | Choose `stacked` for a short heading/date, or `split` when substantial copy balances both columns. Omit/null only when legacy rendering better fits. |
| LP theme | `theme.designPreset` | `editorial` is a shared palette foundation; pair it with event-specific font and colors. It does not choose block composition. |

## High-Impact Validation Notes

- `buttons`: each button must provide either `href` or `anchor`.
- `form`: field IDs must be unique.
- `gallery`: at least one image URL must be non-empty.
- `script`: legacy compatibility only; this does not enable arbitrary JavaScript execution.
- `free-design`: bind all copy through `data-lp-text` and images through `data-lp-image`.
  Preserve field IDs while editing layout. Use `data-lp-role` for semantic sections and
  `data-lp-action="booking"` on booking buttons. HTML/CSS must pass the generated contract;
  scripts, forms, CSS URLs and remote stylesheets are prohibited. Keep reservation/calendar,
  access/map and publisher behavior in native blocks. Complete normal edits after their
  authorized save and readback. Use `tc_lp_review_saved` only for an explicit inspection;
  source validation and draft completion do not certify that a capture succeeded.
- For conversion outcome, include at minimum:
  - `hero`
  - source-backed proof, using the block that fits the evidence (`media`, `gallery`, `specs`, `metrics`, or another suitable block)
  - `process` only when the provided sequence adds useful participation guidance
  - `calendar`
  - `map` only for a physical venue with a supplied address
  - CTA (`buttons` or `stickycta`)

## Premium LP Usage Notes

Use these blocks deliberately. A beautiful LP is not a large collection of blocks; it is a sequence where each
block removes one user concern and leads to reservation.

| Block Type | Premium LP Use |
|---|---|
| `hero` | Prefer a reference-guided, concise text-bearing key visual for image-led campaigns (`visualMode=image-only`). Use overlay for an explicit photo-only/HTML-editable request or when preserving an existing overlay. Keep booking controls outside the bitmap; do not force one mode universally. Choose `imageHeightMode=natural` only when the original artwork ratio is part of the full-width composition. |
| `section` | Short transition only. It renders title/subtitle, not body or lists. Normally use tight spacing and align its outer axis with the following content. `content.presentation=editorial` is optional when the transition benefits. Do not repeat body copy from the next block. |
| `media` | Best for concept, flyer-derived explanation, photos, family/timing narrative, and visual proof. Choose `content.presentation=photo-story`, `editorial`, `split`, or `stacked` to fit the evidence and copy; prefer the fitting composition for new LPs. |
| `cardgrid` | Best for short, parallel 2-4 items. Columns are fixed responsive choices: 2 stays 2 columns on mobile, 3 becomes 1, and 4 becomes 2. Choose from actual copy density on PC and mobile; `content.presentation=editorial` is optional when the card information benefits. Use selective `free-design` when the required reflow is not expressible. |
| `benefit` | Best for one clear visit benefit. Use when a single promise should stand out more than a full card grid. |
| `process` | Best for a short factual sequence. The renderer adds number badges, so titles must omit `01`, `1.`, and `STEP 1`. Layout is fixed at PC 3 columns, tablet 2, mobile 1; avoid it when 3 or 4 items create a harmful orphan row, or use selective `free-design` for that sequence. |
| `calendar` | Required for event reservation. Use `presentation=stacked` for a short heading/date and a centered calendar; use `split` only with balanced explanatory copy. Omit to preserve legacy layout. Do not replace it with `form`. |
| `notice` | Best for privacy, reservation conditions, capacity, childcare, and no-pressure sales promises. `content.presentation=editorial` is optional when a source-backed notice benefits. |
| `faq` | Optional: answer supported questions that add information beyond the visible overview. `content.presentation=editorial` is optional when it improves the question sequence. Do not repeat overview values as questions just to fill a section. |
| `map` | Best for venue/access. Do not invent address details. |
| `buttons` | Final CTA. Prefer one primary button anchored to `#booking-section`. |
| `gallery` | Use when there are multiple uploaded or approved photos. Insert it near the concept/proof area if the baseline template does not already contain a gallery block. Do not fabricate photo evidence. |
| `specs` | Use for source-backed key/value facts. `content.presentation=editorial` is optional when it improves their reading rhythm. |
| `metrics` / `kpi` | Use only when short, source-backed numbers exist. `metrics` wraps flex items at a minimum width of 160px; `content.presentation=editorial` is optional when the numeric story benefits. Place primary price, area, or quantity figures near the opening, with each label and value paired. Preserve units, ranges, and qualifiers; put long dates, time ranges, sentences, and detailed conditions in `notice`, `specs`, or `text`. Do not force numbers into every event. |
| `testimonials` | Source-backed short quotes. Fixed 2 columns on PC, 1 on mobile; internal padding is fixed. No `columns` or inner `padding` option. For long quotations, use full-width text with attribution, or selective free-design when custom quote composition is necessary. Preserve the original quote and author. |
| `script` | Prohibited without explicit approval. |

## Layout Values

Valid layout values are interpreted by the Web renderer. Use them consistently:

- `variant=full-bleed`: full-width hero or meaningful body imagery/compositions.
- `variant=container`: standard body axis, maximum 1080px.
- `variant=content`: narrow text-heavy axis, maximum 720px.
- `variant=grid`: full viewport-width axis. Use it for an intentional edge-to-edge transition, not as a generic card layout. A heading and its answer normally share the same outer axis.
- `surface=default`: neutral section.
- `surface=muted`: problem, process, FAQ, or dense information section.
- `surface=warm`: final CTA and closing section.
- `surface=contrast`: rare emphasis only; avoid overuse.
- `spacing=none`: hero only.
- `spacing=tight`: section headers and notices.
- `spacing=normal`: media and map.
- `spacing=loose`: cardgrid, process, FAQ, and final CTA.
