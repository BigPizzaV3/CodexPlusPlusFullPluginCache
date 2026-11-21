# Search and Evidence Guidance

## Vehicle categories

- Minicamper, mini camper, and micro camper map to `tiny_camper`, not `campervan`.
- Kastenwagen and Campingbus map to `campervan`.
- Wohnwagen maps to `wohnwagen`; Alkoven to `alkoven`; teilintegriert to `teilintegrierter`; vollintegriert to `integrierter`; Liner to `liner`.
- Broad Camper or Wohnmobil requests do not identify a single category. Do not narrow them without a stated reason.
- Do not repeat category synonyms in `preferences.query`: despite its name, this field requires a text match and can exclude valid results.

## Requirements and unknowns

- Enum arrays match any selected value; different constraint fields and selected extras combine as requirements.
- Inclusive capacity ranges use distinct units: watts, amp-hours, and litres are not interchangeable.
- Equipment presence and capacity are separate facts. Missing extras do not prove absence.
- Seller-reported seats do not certify belted travel seats. Weight and category do not establish driving-licence eligibility.
- Do not infer off-grid duration, winter suitability, roadworthiness, or condition from equipment, category, weight, or photos.

## Novice search example

For "up to EUR 60000, six months in Spain and Portugal, bright and cosy, working on a laptop, sometimes with my partner", clarify travel seats versus beds if ambiguous, then show the first useful widget. Keep the budget hard; do not add a body category without a reason. Use `photo_interests: ["interior"]` for the aesthetic wish, not `preferences.query` or an exterior-colour filter. To inspect workspace context, use up to three interests: `living_area`, `dining_area`, `kitchen`. A table photo does not establish ergonomics, connectivity or electrical capacity.

If the buyer later says "a toilet is mandatory, a shower maybe, three or four days off-grid", keep the toilet as a hard filter and the shower optional. Unknown off-grid needs do not justify invented solar, battery or water minima; identify the missing capacity and usage facts instead. If there are zero matches, ask whether any specific requirement may change and wait for permission. Do not show a camper lacking the mandatory toilet as an alternative first.

Use two or three short evidence-based highlights beside the widget, including a trade-off or open question. Describe "bright" or "cosy" as subjective impressions only after inspecting actual photos; otherwise offer interior inspection. Leave the full specifications in the widget.

## Photo evidence

Photo interests select images, not inventory. Labels are predictions, not proof of equipment presence, absence, or functionality. Respect partial coverage and `scan_complete`; the server's bounded scan is not a guarantee that every photo was classified. Photo pages are live and can shift after gallery edits. Missing matches should lead to an explicit all-photos option, not an absence claim.

## Buyer decision checks

Use these only when relevant to the buyer's decision, not as extra mandatory search filters. Unsupported requirements remain questions for the seller or an independent inspector.

- Fit: weekend trips versus long stays, parking/storage constraints, bed access, standing space and daily bed conversion can matter more than body style. Encourage trying a similar layout if uncertain.
- Capacity: check approved travel seats separately from beds. Ask about actual vehicle weight and remaining payload with passengers, water, luggage and fitted accessories; brochure values and a spacious interior do not establish usable capacity. Request weighing and verification against vehicle/axle limits rather than calculating legal eligibility from incomplete advert data.
- Condition: request damp-inspection history and an independent moisture check when needed. Look around plumbing, windows and roof openings, under cushions/mattresses, and beneath the vehicle. Neither photographs nor a seller statement certify freedom from damp.
- Function: review service invoices, complete inspection reports and documented modifications; arrange a test drive and demonstrations of heating, fridge, water, toilet and electrics. Potentially unsafe equipment needs competent inspection; do not prescribe DIY gas tests.
- Handover: inspect before paying, use a written contract, and coordinate verified payment with vehicle, keys and documents. For private sales, avoid advance transfers to an unknown seller. Do not recommend unverified escrow or shipping arrangements.

Example seller-question draft: "Could you confirm the documented travel seats, share the latest moisture and service reports, and arrange a test drive and appliance demonstration?" Tailor this to actual gaps and omit already answered questions. Draft only when useful or requested; the plugin cannot send it.

## Sources

First-party guidance retrieved and cross-checked on 2026-10-17:

- [ADAC: buying a used motorhome](https://www.adac.de/rund-ums-fahrzeug/auto-kaufen-verkaufen/gebrauchtwagenkauf/gebrauchtes-wohnmobil-kaufen/): needs-first selection, damp inspection, equipment-sensitive payload and weighing. Its linked checklist separates belted seats from beds.
- [TUV NORD: motorhome buying guide](https://www.tuev-nord.de/de/wissen/ratgeber-und-tipps-mobilitaet/wohnmobil-kaufratgeber/): vehicle inspection, records, test drive and equipment checks.
- [Caravan and Motorhome Club: buyers' guide](https://www.caravanclub.co.uk/advice-and-training/guide-to-buying-hiring-vehicles/buying-a-car-caravan-or-motorhome/buying-a-motorhome/): layout, moisture measurement, service history and practical checks. UK guidance is not DACH legal authority.
- [ADAC: motorhome payload](https://www.adac.de/reise-freizeit/ratgeber/tests/ueberladung-wohnmobil/): people and accessories consume payload; historical model figures are not specifications for a current advert.
- [ADAC: safe vehicle payment](https://www.adac.de/rund-ums-fahrzeug/auto-kaufen-verkaufen/kauftipps/auto-sicher-bezahlen/): inspect first and coordinate payment with handover; avoid private-sale advance transfers.

These sources support buying guidance, not listing verification or a guaranteed increase in sales. Recheck guidance before making time-sensitive claims. Driving-licence, inspection and gas rules depend on jurisdiction and current law; do not generalize UK or German rules across DACH.