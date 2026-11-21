> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# Image Art Direction and Placement

## Plan Before Generation

For each visual role record:

- `role`: concrete narrative purpose, not `image 1` or `gallery`.
- `target`: hero or the exact media section it explains.
- `source`: reuse, reference-guided generation, or new generation.
- `asset_type`: hero photo, section photo, educational diagram, poster, or
  comparison visual.
- `aspect_and_crop`: intended frame, focal point, and mobile-safe crop.
- `information_value`: what the visitor understands faster because this image
  exists.

Reject a role when `information_value` cannot be stated clearly.

Judge placement by the visual area and decision it creates in the saved page. A
role can be an illustration, a material detail, an observable action, or a recurring
motif as well as a photograph. When the direction is illustration-led or photo-story,
do not satisfy it by shrinking every body asset into a small gallery and leaving the
experience or proof chapters as a plain text band. Use a supplied or safely grounded
subject at a meaningful scale, with copy that explains the same moment. This does
not impose an image count, require images in specs/calendar/map, or override an
explicit image-free request.

## Prompt Brief

Write one prompt per distinct role. Include only relevant fields, but normally
cover these in this order so the image model receives the decision hierarchy
before decorative detail:

- Use case
- Asset type
- Primary subject and action
- Input images and whether each is a reference, edit target, or supporting
  material
- Composition/framing, desktop crop, mobile-safe crop, and usable negative space
- Materials/textures, lighting/mood, color palette, and brand relationship
- Style/medium and coherence with the other LP assets
- Exact text, only when text belongs inside the asset
- Constraints
- Avoid

Choose the medium, lighting, materials, palette and typography to express the
page's art direction and the user's preferences. For photographic work, make
people, spaces and materials convincing. Preserve a requested illustration or
graphic direction. Avoid rendering defects, unsupported factual details and
fake interactive controls. Include text when the asset's role calls for it.

## Hero Medium and Key Visual

Design a complete opening, not a photo followed by a box containing every fact.
Choose the strongest fit among a supplied original or finished key visual, a
pixel-grounded edit or composite, and a separate generated image for a distinct
needed role. Use an already high-quality finished source unchanged when suitable. Low-resolution
PDF photographs should be restored through source-pixel editing without inventing
subject details. For a new LP, prefer a text-bearing key visual unless
the user requests original-only, generation-prohibited or editable overlay output.
Prepare all selected source edits in one tc_lp_edit_image_assets call; retain
originals with tc_lp_use_source_image_assets only when their quality or constraints
make this appropriate. Pass the returned sourceIds directly to the page maker. Call an edit or composite faithful
only when the image tool receives the source pixels. When a new text-bearing key
visual best serves the opening, preserve the subject's identity and credible
details, and select a visual idea for the brief: photographic typography,
collage, graphic invitation, or an illustration-led campaign. Do not
force a fixed composition, palette, font, or template across unrelated events.

For a composed image hero:
- Set `generated_hero_visual_mode=image-only` and omit `hero_visual_plan`.
- Give each input image a role and identify the subject features to preserve.
- Define one focal point and only a short headline plus indispensable identity.
  Use `Text (verbatim): "..."` for every verified string. Specify typography,
  hierarchy, position, contrast and breathing room. Prohibit extra lettering.
- Choose the canvas and text placement for the intended desktop and mobile use.
  Keep the main message visible and readable in the opening at both sizes.
  Detailed information can remain in the page rather than crowding the artwork.
- Keep detailed date/venue/conditions in native LP content even if some identity
  also appears in the image. Retain semantic title/alt without visible duplication.
- No fake buttons, inputs, navigation, invented logos or watermarks in the pixels.
  Connect real booking CTAs to `#booking-section` at useful decision points.
  Do not repeat adjacent CTAs.

For editable HTML copy over an unchanged source photo, or when the user requests
an editable overlay, choose `generated_hero_visual_mode=overlay` and define
`hero_visual_plan`. Only this route uses the returned text-free
`heroImageGenerationBrief` for a new image. Choose editorial-cover for short copy
over calm negative space, framed-photo for a complete photograph with separate
copy, split-panel for independent information and imagery, or photo-spread for a
wide image and separate type. Do not pass an HTML composition with image-only
mode. Preserve existing overlay heroes during partial edits. When a new
text-bearing key visual is selected, resolve mobile readability through
legible typography and canvas composition.

For both modes, review the complete first viewport and its transition into the
next section. Verify focal hierarchy, exact copy, image identity, mobile size,
CTA placement and continuity; absence of overflow is not visual acceptance.
If the bitmap composition itself fails, regenerate only that hero from the same
references and verified copy. Keep successful body assets and sections. Do not
substitute a narrow poster column or move a standalone booking button ahead of
the hero merely to satisfy the first-viewport check.

## Paired Photos and Booking

Choose equal grid frames for equally important photos. Intentional asymmetry
needs a dominant subject, clear shared alignment and balanced negative space.
Do not merely reduce the second image and leave a large empty hole above it.
A deliberate overlap can use a selected free-design region; preserve native
blocks elsewhere. A short reservation title/date belongs above its calendar in
`calendar.content.presentation=stacked`; use split only for balanced content.
Never hide the calendar or invent future dates to improve a screenshot.

## Coherence Lock Across Assets

Keep these stable across the LP unless the source material requires a change:

- season and time of day
- color temperature and contrast
- camera realism and lens character
- treatment of people and architecture
- brand accent relationship
- border radius, crop logic, and media frame proportions

When one source is assigned to both hero and body, vary the information it adds:
the hero can establish the whole event or value, while the body can show a
detail, another action or moment, or a materially different crop/diagram. This
is valid reuse when the visitor learns something new and the source remains
factually intact. Treat an unchanged person, action, background, and frame as
a repeated composition; with one source or original-photo-only input, keep the
source rather than inventing a replacement.

## Role Examples

Bus tour example, when supported by source facts:

- Hero: the whole tour promise; family welcomed beside the bus and a credible
  construction context; wide crop with a clear focal point.
- Structure highlight: expert explaining visible framing or insulation at an
  active but safe construction site; details must be legible.
- Owner-home highlight: lived-in brightness, spatial scale, and natural family
  movement; do not depict a generic showroom.
- Mini-lecture highlight: approachable explanation of design and finance with
  real materials or plans; no unreadable fake charts.

These are roles derived from that event, not defaults for every housing LP.

## Placement Rules

- The first role maps to the hero.
- Each later role maps to one semantically matching media block or one gallery
  image in the same reading order. Two to four complementary views can share an
  editorial gallery: wide/detail, materials/result, or plan/photograph. Each image
  retains its own role, descriptive alternative and concise informative caption.
  Do not force a full paragraph section for every image in a shared experience.
- Do not place an image in a later gallery merely because all earlier slots are
  occupied.
- A gallery is appropriate for a purposeful set: several owner-home examples,
  material variations, workshop results, or event atmosphere. Give it a
  heading and contextual copy; never use captions such as `画像 1`.
- Do not repeat the hero's unchanged person, action, background, and frame in a
  supporting section. Reusing a source for a distinct whole/detail, action,
  moment, crop, or diagram is allowed when the body role adds a new fact.
- Venue photos belong in access only when they depict the actual venue.
- Generated maps are prohibited; bind the real map block to event location.

## Output QA

Review every generated asset before saving the LP:

1. Does it communicate the assigned role without relying on adjacent copy?
2. Is the scene factually compatible with the event and source materials?
3. Does the crop work in its target block on desktop and mobile? When a supporting
   image is also used in the hero detail frame, check both placements.
4. Are people, hands, architecture, signage, and tools plausible, with gaze,
   body orientation, and object placement consistent with the depicted action?
5. Does lettering fit the intended image role? A text-bearing hero integrates its
   short, accurate headline into the artwork; do not repeat it over the image.
   Keep dates, venue and real booking controls in editable HTML. Supporting photos
   need no lettering unless their explanatory role benefits from it.
6. Does it differ meaningfully from the other assets while preserving the same
   visual world?
7. Is it actually placed in the saved LP?

If one item fails, iterate that asset with one targeted change rather than
regenerating the whole set.

- When the opening depends on typographic emphasis, choose `titleAccent` as an exact, short phrase already in `title`. Keep the title itself complete and editable. A distinctive benefit or verified number can be stronger than an event-name headline. Do not emphasize every word.
- For illustration-led split panels, consider `panelTone: page`: the copy uses the page canvas and its normal ink, with the accent reserved for the emphasized phrase and CTA. Specify that same page background color in visualLanguage and lpTheme so the image and typography form one composition. Use `brand` when the solid color panel serves the concept; this is a design decision, not a required preset.
