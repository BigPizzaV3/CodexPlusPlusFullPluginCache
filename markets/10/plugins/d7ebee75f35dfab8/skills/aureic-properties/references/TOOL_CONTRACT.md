# Aureic Properties tool contract

## Shared catalogue metadata

- `catalog_id`: human-readable generated catalogue identifier.
- `catalog_sha256`: integrity identifier for the normalized export.
- `generated_at_utc`: time the export was produced.
- `release_status`: `validated` or `development-unreconciled`.
- `record_count`: active public records in the export.

Never present a `development-unreconciled` catalogue as publication-ready.

## Property semantics

- `status: active` means the public source classified the listing as active when
  exported. It is not a live availability check.
- `price.amount` is the published asking price.
- `price.verified_at` is the stored verification date, not today's date unless
  the source explicitly says so.
- `location.precision: area` prohibits presenting a precise street address.
- `source.semantics.property_data: FACT` identifies published catalogue facts.
- `aureic_assessment.classification: ADVISORY` identifies Aureic's editorial
  judgement and must remain labelled.
- An absent field is `UNKNOWN`, not zero and not an invitation to estimate.

## Search

Hard filters are applied server-side. `match.score` only orders records that
already satisfy them. `match.reasons` explains applicable criteria without
constituting an investment recommendation.

`total_matches` is the full number of active public matches. `result_count` is
the displayed subset, capped at six, and `all_result_ids` preserves the full
ordered set for the fullscreen catalogue. Do not imply that the displayed
subset is the complete result set when `total_matches` is larger.

## Comparison

The comparison supports two to four unique active public properties. Compare
the same dimensions and preserve null or absent values. The model may explain
trade-offs against user priorities but must not manufacture a universal score.
The component is a visually formatted property comparison; it is not a
photographic or architectural visual analysis unless a future tool explicitly
adds that capability.

## Rendering

The three `render_property_*` tools are decoupled presentation tools. They
resolve canonical IDs against the same validated catalogue and return one of
three visual modes: `search_results`, `property_detail`, or
`property_comparison`. They do not search, change catalogue data, or confirm
live availability. Their MCP Apps resource is optional; the original data-tool
response remains complete and usable without UI.

The `search_results` presentation uses an inline carousel of no more than six
properties. When the full result set is larger, the same component can request
fullscreen mode and display `all_properties` as a vertically scrolling
catalogue. Both views preserve the original search order and filters.

Visual property records, photographs and the complete fullscreen result set are
returned in tool-result `_meta` for the component only. Render-tool
`structuredContent` contains only a concise receipt (view, catalogue, selected
IDs, count and limitations), so the model does not create a redundant native
carousel from the same images. Search, detail and comparison data exposed to
the model likewise omit image URLs; their matching render tools remain the
authoritative visual presentation.

The property-detail presentation contains no more than eight published
photographs. This is a curated selection, not the complete source gallery. The
model-visible record never exposes a source photograph count, and the assistant
must not state one. The official property URL is the only destination described
as containing the complete gallery.

## Enquiry submission

`submit_property_enquiry` is the only write tool. It requires one canonical
active public property, a name, a valid email address, an optional phone,
optional budget, a short message and `privacy_consent: true`. The user must see
and review the exact submission before the tool is called. A successful result
means only that Aureic received the enquiry; it never confirms availability,
books a viewing or reserves a property. The response contains no submitted
personal data, internal request identifier or telemetry. The temporary server
record is retained for no more than 60 days.
