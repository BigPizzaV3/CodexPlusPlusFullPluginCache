# Delivery, packaging and policies

Use for physical fulfillment, shipping-profile selection/creation and delivery copy. Help choose a feasible configuration; do not invent logistics facts to complete fields.

## Physical goods: collect two different measurements

**Product:** actual dimensions, weight/capacity if relevant, count and units. These describe the item to buyers and category attributes.

**Packed parcel:** exterior length/width/height, scale weight including all items, box/envelope, padding, stand/accessories and packaging. These support shipping calculations. Product size alone cannot establish parcel size. Never guess a package from a photo or reuse another product's measurements without confirmation.

Use [packaging worksheet](../templates/packaging-worksheet.md). If unmeasured, provide a packing plan and request actual measurement; label any proposed box size an estimate for purchasing/testing, not a verified shipping value. For multiple quantities, obtain the real combined parcel or carrier packing rules rather than multiplying dimensions.

Normalize units explicitly: 1 inch = 2.54 cm, 1 lb = 16 oz, 1 kg = 1000 g. Preserve original measurements and conversion precision; do not imply measurement accuracy beyond the source. Carrier dimensional/billable weight rules vary by carrier/service/date: retrieve the applicable rule and calculate it only from confirmed packed values. Never invent a divisor or quote.

## Processing and transit

Keep production/processing (time to dispatch) separate from carrier transit. Record ready-to-ship versus made-to-order, seller working calendar, minimum/maximum, origin country/postal code, carrier/service, destinations and rates. Show estimates as estimates. Avoid “arrives by Christmas” without a supported order cutoff, production capacity and service commitment. Check current holidays/cutoffs rather than extrapolate last year's dates.

Compare shipping choices by delivered price, feasible service, tracking, actual product protection and margin where cost inputs are provided. Free shipping means cost is absorbed, not nonexistent. Do not enable worldwide delivery merely because the seller's app serves worldwide; obtain seller-approved destinations and rates. Customs/packaging compliance is country-specific; verify relevant current official requirements when asked rather than invent universal legal terms.

## Select versus modify a profile

1. Read `etsy_get_shop_shipping_profiles`, then `etsy_get_shop_shipping_profile` and relevant destinations/upgrades. A profile title such as “Paid worldwide” does not prove its actual rates.
2. Compare origin, destinations, primary/secondary costs, service/transit, processing and approved package assumptions. Show the selected profile and why it matches.
3. Assign one listing with `etsy_update_listing` → `body.shipping_profile_id`; reread the listing.
4. If no profile fits, prepare an approved new profile through `etsy_create_shop_shipping_profile`; add destinations/upgrades with the matching tools and reread them. Bind the returned real ID.
5. To modify rates, use `etsy_update_shop_shipping_profile_destination`, not `etsy_update_shop_shipping_profile` (which edits title/origin/processing). Show all affected listings before changing a shared profile. Creating a separate profile can preserve unrelated items when that is the requested scope.

Processing profiles have their own `etsy_get_shop_readiness_state_definitions`, create/update/read methods. Their `processing_time_unit` uses `days`/`weeks`; shipping-profile units use `business_days`/`weeks` in the saved schema. Do not interchange enums. Read the live schema and attach the appropriate readiness state where exposed.

The direct `item_weight` and `item_length/width/height` shipping fields need the units and meaning documented by the current Etsy form/schema. Keep buyer-facing product dimensions separate. If calculated shipping or a carrier feature is not exposed, prepare the manual field instructions; do not invent a supported API call.

## Returns and exchanges

Read `etsy_get_shop_return_policies`; present returns/exchanges and applicable deadline before selection. Assign `body.return_policy_id` with `etsy_update_listing` and read back. Creation uses `etsy_create_shop_return_policy`; consolidation can move many listings and delete a source policy, so requires authorization for that entire consequence. Never choose “no returns” automatically because an item is personalized. Do not claim a policy overrides consumer rights; use seller-approved terms and seek current jurisdiction-specific guidance when necessary.

## Offline settings and digital delivery

Offline: give the exact named profile to choose, its confirmed terms or unresolved inputs, and separate manual steps in Etsy's listing Pricing & shipping/processing/returns sections. Draft text is useful before profile IDs exist; it is not verified logistics setup.

Digital: no parcel or carrier. Confirm instant download versus seller-made/custom delivery, files, access instructions, editing requirements and production timeline where applicable. Do not describe a custom digital item as instant if the finished files do not already exist. API `type` must follow the live enum; MakeBox convenience `digital` is not automatically the direct `download` value.
