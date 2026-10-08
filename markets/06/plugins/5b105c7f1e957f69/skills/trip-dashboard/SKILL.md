---
name: trip-dashboard
description: Build a responsive, image-rich trip decision workspace from an audited plan. Use after a full plan is stable or when the user asks for an interactive travel dashboard that compares hotels, activities, restaurants, transport, itinerary, and budget in one place; do not use it to invent or repair research.
---

# Trip Dashboard

Create the interactive companion to the written plan. The dashboard is the traveler’s all-in-one decision desk: it makes the meaningful choice understandable without requiring a booking-site scavenger hunt. It presents audited data and never replaces research, source verification, budget reconciliation, or accessibility gating.

Read [dashboard-data-contract.md](references/dashboard-data-contract.md). Generate the interface only through `scripts/build_dashboard.py`, which uses the validated `assets/trip-dashboard-template.html`.

## Build the decision dataset

1. Convert the stable plan into the complete contract JSON. Preserve the canonical currency, travelers, target, selected recommendations, budget inputs, route, days, and evidence ledger.
2. For every hotel, experience, restaurant, and transport option, include enough verified detail to decide inside the dashboard: description, traveler fit, logistics, price basis, quality signals, pros, cautions, confidence, and freshness.
3. Add two to four truthful, attributable images per option where available. Check every primary image in a browser. Do not use a similar-looking substitute for an exact property, venue, dish, or tour. Label representative destination imagery plainly when it is the only defensible choice.
4. Include at least two credible alternatives for each meaningful decision when the market actually offers them. Preserve the recommended default, but make the tradeoffs visible.
5. Use party-total amounts unless the field explicitly says otherwise. Mark evidence status and keep checked dates visible.
6. Ensure restaurant costs are not double-counted: use `budget_mode: included` when the food assumption already covers the meal; use `additive` only for separately priced splurges or prepaid dining.

## Build and verify

1. Run the builder. If validation fails, repair the canonical data rather than weakening validation or hand-editing generated totals.
2. Open the generated dashboard in a real browser at desktop and mobile widths.
3. Verify the first view shows total, per-person cost, target status, research date, route, decision completion, and visual current selections.
4. Change an assumption, a hotel, a transport option, an activity, and a restaurant shortlist. Confirm the total changes only for budget-bearing choices and the decision rail updates immediately.
5. Compare two or three like-for-like choices and verify the comparison drawer shows their most useful differences.
6. Exercise image thumbnails, broken-image fallback, reset, browser-local persistence, every itinerary anchor, and every source link.
7. Confirm no horizontal page overflow at 320px. Print the selected plan and verify it remains legible.

## Required behavior

- The page is one continuous, sectioned workspace; important categories are not hidden behind tabs.
- Hotel and transport groups are single-choice. Experiences and restaurants support shortlisting. Compare mode is limited to three like-for-like items.
- Each decision card displays useful context, images, tradeoffs, and practical details before its secondary external link.
- Editable assumptions and budget-bearing choices recalculate total and per-person cost immediately.
- Reset restores the audited recommendation. Local persistence is disclosed and recoverable.
- The itinerary exposes morning, afternoon, evening, transit, practical notes, and scheduled-commitment count.
- Sources distinguish marketplace, operator/direct, official, and secondary evidence.
- Unknown critical accessibility or medical links remain **not ready** and are never hidden by presentation.
- Image credits remain accessible from the item they support.
- Print styling produces a useful static selected-plan record rather than printing all alternatives indiscriminately.

