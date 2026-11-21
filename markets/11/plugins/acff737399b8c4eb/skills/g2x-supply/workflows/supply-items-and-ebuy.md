# Supply items, DIBBS and GSA eBuy

Goal: identify an item, find who supplies it, and find open buys, without overstating what a catalog entry proves.

## Steps

1. Identify the item. For a known NSN, call `g2x_nsn_lookup`, for example `{"nsn": "5305-01-599-0244"}`. To discover items, call `g2x_nsn_search` with exactly one of item name, part number or CAGE, for example `{"item_name": "hydraulic hose assembly", "federal_supply_class": "4720"}`. Page a CAGE search with its cursor. Item name and part number searches return no total; narrow them instead of paging.
2. Handle replacements. When DLA cancelled or reclassified the NSN, list the replacement items the answer returns and re-check buys against the replacements. CAGE codes from the catalog are part number holders, not approved sources.
3. Find open buys. Call `g2x_search_opportunities` with the NSN as the query; only notices that name it answer. Or call `g2x_search_supplementary` with the `dibbs` family for DLA DIBBS opportunities and attachment text. Open a candidate with `g2x_get_record` and read its documents before quoting quantities or delivery terms.
4. Check GSA eBuy in parallel when the user sells on schedule. Call `g2x_search_ebuy` with keywords, schedule or SIN filters. Open a candidate with `g2x_get_ebuy` for deadlines, amendments and questions, and list its files with `g2x_list_ebuy_attachments`. If the answer says to connect eBuy or ask the account owner for access, give that step and stop.
5. Price the labor side when services are involved. Call `g2x_labor_rates` in `search` or `statistics` mode. Report ceiling rates as ceiling rates, with the category and filters used.
6. Track on request. Add promising notices with `g2x_watch_records`. eBuy quotes are submitted through GSA eBuy, never through these tools.

## What to tell the user

Give the item identity, supply class, part numbers and catalog suppliers, then the open buys with deadlines and links. State clearly that a catalog entry does not prove stock, price, eligibility or an open requirement.
