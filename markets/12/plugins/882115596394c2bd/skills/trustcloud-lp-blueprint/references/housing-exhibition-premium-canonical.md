> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# Canonical Example: Housing Exhibition Premium

## Source of Truth

- Template ID: `housing-exhibition-premium`
- Builder: `buildHousingExhibitionBlocks`
- Source files:
  - `apps/web/src/lib/lp/templates/housing-exhibition-v1.ts`
  - `apps/web/src/features/events/components/event-lp-editor.tsx`

If this reference and source code diverge, source code is authoritative.

## Applicability

The sequence, slots, and layout rules below apply when the
`housing-exhibition-premium` example is selected. They do not require other
event structures or unrelated partial edits to adopt this template. Factual
copy, supported blocks, event bindings, reservation readiness, and publication
confirmation remain required regardless of the chosen structure.

## Canonical Block Sequence (Baseline Recommended Order)

| Order | Slot | Block Type | Core Content Keys | Conversion Role |
|---|---|---|---|---|
| 1 | hero | `hero` | `title`, `subtitle`, `ctaText`, `ctaAnchor` | First-view promise and reservation entry |
| 2 | section-concept | `section` | `title` | Introduce concept |
| 3 | media-concept | `media` | `title`, `body`, `imageUrl` | Narrative proof |
| 4 | section-pains | `section` | `title` | Audience pain framing |
| 5 | cardgrid-pains | `cardgrid` | `cards[].title` | Structured value proof |
| 6 | media-timing | `media` | `title`, `body` or `list[]` | Timing/fit explanation |
| 7 | section-process | `section` | `title` | Process header |
| 8 | process | `process` | `steps[].title` | Booking-to-visit flow |
| 9 | section-booking | `section` | `title` | Reservation header |
| 10 | calendar | `calendar` | (optional) `title`, `note` | Slot selector |
| 11 | notice-booking | `notice` | `text` | Privacy/booking notice |
| 12 | section-faq | `section` | `title` | FAQ header |
| 13 | faq | `faq` | `items[].q`, `items[].a` | Objection handling |
| 14 | section-access | `section` | `title` | Access header |
| 15 | map-access | `map` | `address` or address parts | Venue and transit |
| 16 | section-closing | `section` | `title` | Final intent framing |
| 17 | buttons | `buttons` | `buttons[].label` + (`anchor` or `href`) | Final CTA |
| 18 | copyright | `text` | `text` | Footer/host line |

Optional insertion:

- If multiple approved photos form a purposeful collection that visitors should
  compare or browse together, insert a contextualized `gallery` block near the
  section it supports.
- When each image explains a different highlight, use separate `media` blocks
  instead of collecting the images in a gallery.
- Never append a gallery merely because generated images remain unplaced.

## Canonical Distribution

- Total blocks: `18` baseline, `19` when approved gallery images are inserted.
- Type counts:
  - `hero`: 1
  - `section`: 6
  - `media`: 2
  - `cardgrid`: 1
  - `process`: 1
  - `calendar`: 1
  - `notice`: 1
  - `faq`: 1
  - `map`: 1
  - `buttons`: 1
  - `text`: 1

## Block-Level Authoring Contract

Use the following rules when filling a selected premium template's canonical
slots. These are that template's authoring contract, not a required sequence
for every ChatKit LP.

| Slot | Layout | Copy / Data Rule |
|---|---|---|
| `hero` | `full-bleed`, `spacing=none`, `surface=default` | For newly generated artwork, use `visualMode=image-only`, integrate exact event identity/date/short promise into the image, retain title/subtitle semantically, and leave `ctaText` empty. Preserve `visualMode=overlay` for existing or explicitly editable-overlay heroes. The real CTA belongs in a later `buttons` or `stickycta` block. |
| `section-concept` | `container`, `spacing=tight` | Introduce the LP theme in one line. Use event kind wording: 見学会 / 相談会 / ワークショップ. |
| `media-concept` | `container`, `spacing=normal` | Reflect uploaded flyer/photo facts, event description, main highlights, and atmosphere. Use `chips` for the top 2-3 highlights. |
| `section-pains` | `container`, `surface=muted`, `spacing=tight` | State the target user's concern. Do not write generic marketing copy that could fit any event. |
| `cardgrid-pains` | `container`, `surface=muted`, `spacing=loose` | Use 3-4 cards. Each card should map to a hearing answer such as push point, benefit, offer, target concern, or promise. |
| `media-timing` | `container`, `spacing=normal` | Explain why attending now is useful. Include a short `list` for target situations, promises, or decision triggers. |
| `section-process` | `container`, `surface=muted`, `spacing=tight` | Introduce the flow. |
| `process` | `container`, `surface=muted`, `spacing=loose` | Use 3 steps. Step 1 is reservation, step 2 is visit/consultation/workshop, step 3 is next action or take-away. |
| `section-booking` | `container`, `spacing=tight` | Place immediately before `calendar`. |
| `calendar` | `container`, `spacing=loose` | Reservation calendar is central to conversion. Confirm calendar binding before publish recommendation. |
| `notice-booking` | `container`, `spacing=tight` | State privacy use and sales stance such as 完全予約制, 強引な営業なし, 訪問営業ゼロ, or 追客なし when provided. |
| `section-faq` | `container`, `surface=muted`, `spacing=tight` | Introduce FAQ. |
| `faq` | `container`, `surface=muted`, `spacing=loose` | Use 3-5 questions. Cover reservation, duration, children, sales pressure, parking/access, or online support depending on event kind. |
| `section-access` | `container`, `spacing=tight` | Introduce venue. If address is not available, mark it as publish-before-confirmation instead of inventing a location. |
| `map-access` | `container`, `spacing=normal` | Include `address`, optional address parts, parking, transit, and contact/operation notes when available. |
| `section-closing` | `container`, `surface=warm`, `spacing=loose` | Restate the next positive step without pressure. |
| `buttons` | `container`, `surface=warm`, `spacing=tight` | Final CTA. One primary reservation button is usually enough. |
| `copyright` | `container`, `surface=warm`, `spacing=tight`, `align=center` | Footer only. Use the actual organizer/host name. Do not output Homin Cloud unless Homin Cloud is the organizer. |

## Hearing-To-Block Mapping

Use collected event facts as follows.

| Hearing Fact | Primary Destination |
|---|---|
| Event purpose / concept | `hero.subtitle`, `media-concept.body`, `section-closing.title` |
| Event kind | `hero.ctaText`, `process.steps`, `faq.items`, section titles |
| Property type / consultation theme / workshop type | `section-concept`, `media-concept.title`, `cardgrid-pains.cards` |
| Push points / what users can learn / workshop appeal | `media-concept.chips`, `cardgrid-pains.cards`, `media-timing.list` |
| Target audience | `section-pains.subtitle`, `media-timing.list`, FAQ wording |
| Benefits / visit gifts | `cardgrid-pains.cards`, `notice-booking.text`, FAQ |
| Childcare / children support | FAQ and `notice-booking` |
| Sales promise | `notice-booking.text`, FAQ, final section subtitle |
| Uploaded flyer/photo | `hero.imageUrl`, the semantically matching `media.imageUrl`, or a purposeful `gallery.images`; extracted text informs copy |
| Venue / access | `map-access.address`, `map-access.detailItems`, `directions` |
| Calendar / reservation settings | `calendar`, `section-booking`, process step 1 |
| Organizer / host name | Footer `text`, not the main CTA or hero |

## Event Kind Adaptation

- 見学会: lead with property type, push points, target family, taste, and the top 3 things to see.
- 相談会: lead with theme, what users learn, current anxiety, format, and lecturer profile when available.
- ワークショップ: lead with workshop type, audience, appeal, atmosphere, instructor, schedule, and belongings.

When the premium template is selected, keep its baseline sequence while adapting copy. If an approved photo collection has a shared
narrative purpose, insert `gallery` beside that purpose; otherwise distribute images into matching
`media` blocks. If a block is not useful, change its copy purpose;
do not drop reservation-critical blocks.

## Quality Checks

Before saving a draft or recommending publication, apply the relevant checks:

1. Sequence check
- For a selected premium template, preserve its canonical order unless a structural change is requested. For other structures and partial edits, validate the affected reservation flow without imposing premium slots.

2. Required presence check
- Required types for reservation outcome: `hero`, `process`, `calendar`, `map`, CTA (`buttons` or `stickycta`).

3. Data readiness check
- Access block should carry venue information.
- Calendar block should align with configured reservation operations.
- Footer should not contain vendor-branded placeholder text.
- User-visible strict-schema copy should remain Japanese.

4. CTA check
- CTA block count should be 1-2.
- Last CTA should be near page end.

5. Safety check
- `script` block is prohibited unless explicitly approved.

## Deviation Policy

If customization is requested:

- Keep the reservation-critical chain.
- Include a short deviation note only when the user requests a comparison or the change requires a user decision:
  - what changed
  - why it changed
  - conversion or operational impact

## Related Variant

- `housing-exhibition-classic` (`buildHousingExhibitionBlocksV2`) is a spacing/hierarchy-tuned variant.
- When the user wants a recommendation between these housing-exhibition templates, offer premium (`v1`) first. This preference does not prescribe the structure of other events or partial edits.
