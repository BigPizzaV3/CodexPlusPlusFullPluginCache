> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# Event LP composition reference

## Intent

Create a complete page around the user's request, available facts and the visitor's
reasons to attend. The housing template is one optional example; it does not set a
canonical sequence, style, image count or chapter count for new pages.

Use `tc_lp_tools_reference` for the current block schema and real booking bindings.
Use `tc_lp_design_reference` for complete code and desktop/mobile views of five
reviewed LPs. Read any useful example while planning, writing or revising. Adapt
its techniques without copying example facts, image URLs or event details.

## Composition and imagery

Develop the middle and ending as carefully as the hero. Give each chapter a
specific question or decision to answer through concrete copy and appropriate
imagery. For a rich event, five or more illustrated chapters can be useful, but
this is never a requirement or save condition. Respect concise and image-free
requests. Do not invent benefits, performance claims, gifts or testimonials to
increase length.

Copy, HTML/CSS and images can be developed in any useful order. Write the body
first when that clarifies the images it needs. Generate independent images in a
batch for speed, then add or edit an individual image if the evolving composition
needs it. Source-photo editing receives the original pixels and preserves subject
identity. With no source photos, create concrete photographic scenes that convey
the event, without claiming they document an actual venue or past event.

Use an original photo or finished key visual unchanged when it is the strongest
suitable source. For a new image-led LP, consider a short text-bearing hero. Use `visualMode=image-only`
for that artwork, retain its natural composition, and do not overlay the same
headline. Keep dates, venue and real booking actions in HTML. Respect editable
overlay, original-only or no-generation requests. For a new full LP or complete
redesign, author the body in free-design HTML/CSS. Native blocks remain useful for
real functions and fitting compositions; preserve the scope of partial edits.

## Facts and functional content

Ask only for genuinely missing event settings that cannot be resolved from the
request, supplied material or current event. Do not require a fixed number of
selling points, a detailed design brief or a complete asset plan from the user.

The current event is the source of truth for dates, location and calendar bindings;
respect explicit changes from the user. Never invent an address, performance fact
or organizer. Use a native calendar for booking; a native form collects additional
questions or inquiries. Use a native map when a physical location calls for it. Connect authored booking buttons with
`data-lp-action="booking"`. A `process` is for an actual chronology or participation
sequence; it is not a mandatory three-step chapter.

## Copy and layout

Use clear headlines, informative body copy and readable Japanese paragraphs.
Preserve distinct source facts rather than forcing text into arbitrary character
budgets. Split long content by meaning, vary image scale and layout, and avoid
repeated bands that only restate the preceding section. FAQ and CTA counts follow
the content. The authoring schema owns actual field limits.

Keep visual order, focal points, line length and controls usable on desktop and
mobile. Do not limit full-width imagery to the hero or force every body chapter
into the same preset. Compare the whole page with relevant examples where visual
evidence is available.

## Completion

Save through `tc_events_update_draft` with the current source version and confirm
readback. Technical validation, authorization and concurrency protection remain
required. Editorial suggestions are not additional draft-save gates. Booking
availability and publication are separate from draft completion; the client
chooses whether to publish.
