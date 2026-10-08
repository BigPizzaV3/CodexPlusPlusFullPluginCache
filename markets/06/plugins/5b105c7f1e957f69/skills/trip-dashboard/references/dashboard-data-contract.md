# Dashboard data contract

The builder accepts one UTF-8 JSON object. It produces a standalone decision workspace; the JSON therefore carries the useful facts and image provenance that would otherwise force the traveler back to booking sites.

## Required top-level arrays

- `assumptions`: editable party-total budget inputs.
- `fixed_costs`: non-editable included, optional, or excluded line items.
- `hotels`: one group per trip base with exactly one selected option.
- `activities`: selectable experiences, tours, tickets, and admissions.
- `restaurants`: dining candidates the traveler can shortlist.
- `transport`: one group per meaningful transfer with exactly one selected option.
- `days`: ordered itinerary days.
- `sources`: direct research, verification, and booking links.

Arrays may be empty only when the category genuinely does not apply. A complete leisure trip normally includes candidates in every relevant category.

## Meta

`meta` requires `title`, `currency`, `travelers`, `trip_days`, `route`, `researched_at`, nonnegative `canonical_total`, and nonnegative `contingency_rate`. It may include `subtitle`, numeric or null `target`, `confidence`, `readiness`, `largest_uncertainty`, and stable `id` for browser-local decision persistence.

Use a three-letter uppercase currency. Amounts must already be converted to that currency by `$trip-budget`.

## Shared image object

Every hotel option, activity, restaurant, and transport option requires a non-empty `images` array. Prefer two to four images per item. Each image object requires:

- `url`: a stable direct `https://` or `http://` image URL that was browser-checked.
- `alt`: concise, descriptive alternative text for that exact image.
- `credit`: visible provider, photographer, property, operator, tourism board, or publisher credit.
- `source_url`: the page that establishes the image provenance.

Images must depict the actual place, property, dish, vehicle, or experience. If only a representative destination image is available, label it as representative in both `alt` and `credit`; never imply it is the exact product. Broken primary media blocks release.

## Budget records

Each assumption requires unique `id`, `label`, `category`, nonnegative numeric `value`, `min`, `max`, and `step`, plus `status` and optional `note`.

Each fixed cost requires `label`, `category`, nonnegative numeric `amount`, and `status`: `included`, `optional`, or `excluded`.

Each hotel base requires `base` and `options`. Each option requires unique `id`, `name`, party-total `amount`, `nights`, `location`, Boolean `selected`, `description`, `why_fit`, and `images`. Exactly one option per base is selected. Add useful decision fields when verified: `nightly_rate`, `room`, `rating`, `review_count`, `neighborhood_vibe`, `walkability`, `amenities`, `cancellation`, `pros`, `cautions`, `url`, `confidence`, `status`, and `checked_at`.

Each activity requires unique `id`, `name`, party-total `amount`, Boolean `selected`, `day`, `source_type`, `description`, `why_fit`, and `images`. Add marketplace and direct URLs plus `duration`, `start_times`, `meeting_point`, `group_size`, `cancellation`, `includes`, `rating`, `review_count`, `pros`, `cautions`, `confidence`, `status`, and `checked_at` when known. Compare GetYourGuide, Viator, Klook, Tripadvisor, and the direct operator where relevant; do not infer equivalence from similar titles.

Each restaurant requires unique `id`, `name`, `location`, `cuisine`, Boolean `selected`, `description`, `why_fit`, `images`, and nonnegative party-total `amount` (use `0` when the meal is already represented by a general food assumption). `budget_mode` is `included` or `additive`; only selected additive meals enter the total. Add `meal`, `price_level`, `reservation`, `rating`, `review_count`, `signature_dishes`, `dietary`, `pros`, `cautions`, `url`, `confidence`, `status`, and `checked_at` when verified.

Each transport group requires `leg` and `options`. Each option requires unique `id`, `name`, `mode`, party-total `amount`, Boolean `selected`, `description`, `why_fit`, and `images`. Exactly one option per leg is selected. Add `duration`, `frequency`, `luggage`, `comfort`, `transfer_count`, `pros`, `cautions`, `url`, `confidence`, `status`, and `checked_at` when known.

## Itinerary and sources

Each day requires `label`, `date`, `base`, `morning`, `afternoon`, `evening`, `transit`, `notes`, and nonnegative integer `commitments`. Optional `image_url`, `image_alt`, and `image_credit` add a visual day overview.

Each source requires `label`, valid `https://` or `http://` `url`, `type`, `checked_at`, and optional `note`. Links point to the actual property, activity, operator, attraction, transport provider, restaurant, or authoritative page—not search results.

## Invariants

- Initial choices and values exactly match the audited canonical plan.
- The builder recomputes the initial total and rejects data unless it equals `meta.canonical_total` to the cent, including contingency.
- Selected transport is included in the total. Restaurant amounts enter only when `budget_mode` is `additive`.
- Target is null when none exists. No negative or non-finite amount is permitted.
- All key decision facts appear in the dashboard; outbound links are secondary verification and booking actions.
- Critical unknown accessibility, allergy, equipment, or medication links set `meta.readiness` to `not_ready` and remain visible.

