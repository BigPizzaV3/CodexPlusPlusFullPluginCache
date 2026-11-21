---
name: schengen-days
description: Count Schengen short stays under the rolling 90/180 rule, plan consecutive trips, show days returning and download daily CSV calculations.
---

Use `calculate_schengen_days` for a list of past and planned stays plus an explicit `check_date`. Pass `stays` as entry_date/exit_date pairs, e.g. March 5, 2026 through March 20, 2026. An omitted exit ends at the check date.

Use `plan_schengen_trip` with closed `past_stays`, an `entry_date` and optional `planned_length` from 1 to 90 days. State the maximum consecutive stay, last legal exit and first entry supporting the requested length. Days left on one date can differ from maximum consecutive stay because days expire during the trip.

Use `find_schengen_reset_dates` with `past_stays` and preferably an explicit `reference_date`. Omission uses America/New_York today. This projection assumes departure by that date and no further stays. It shows window headroom, not trip length.

Accept ISO YYYY-MM-DD or English US text dates. Refuse ambiguous numeric slash dates; request ISO form. Entry and exit count; shared exit/entry dates count once and merge. Other overlaps are refused. Up to 60 stays spanning 1,100 days, years 1900–2100. Use [] for no stays.

Report key numbers, warnings and the CSV link. For a large itinerary, the CSV and widget include the full daily records and stay results. This is a calculation aid, not legal advice; a border officer makes the decision. Exclude residence permits and long-stay type D visas. Bilateral agreements, special visa-waiver rules, visa validity, number of entries and shorter visa-sticker allowances are outside the calculation. Do not ask for nationality or passport data. Include only days in Schengen; historical country membership is not inferred.
