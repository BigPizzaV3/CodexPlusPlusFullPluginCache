# DLA, NSN and DIBBS

These tools answer from DLA's public supply catalog. A catalog match does not prove stock, current price, eligibility to supply or an open purchase requirement. CAGE codes here are catalog references: the part number holders in the catalog, not the approved sources for a buy.

To find open DIBBS buy opportunities for an item, search opportunities with the NSN, or use the supplementary search in [Opportunities and documents](opportunities.md) with the `dibbs` source family.

### `g2x_nsn_lookup`

Return what one National Stock Number is.

- Inputs: `nsn` (required, an NSN dashed or undashed, or the bare 9-digit item number).
- Output: one answer with the item, its federal supply class, the part numbers it is known by with the CAGE supplier behind each, and, when DLA cancelled or reclassified the NSN, the items that replaced it. When the catalog has no item for an NSN, it lists the open notices in G2X that name it.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"nsn": "5305-01-599-0244"}`

### `g2x_nsn_search`

Find NSNs by item name, by part number or by a supplier's CAGE code. Give exactly one of the three.

- Inputs: `item_name` (every word must appear), or `part_number` (letters and digits are compared, so dashes and spaces do not matter), or `cage` (five letters or digits, lists the supplier's catalog items); `federal_supply_class` (4-digit code, narrows an item name search only); `cursor` (CAGE searches only: pass the next cursor with the same CAGE to continue); `limit` (1 to 50, default 10). Items are in stock number order.
- Output: NSN rows. A CAGE search returns the supplier, its catalog item total when known and a cursor when another page exists. Item name and part number searches have no total or cursor; narrow the search when more match. A part number search lists each NSN once with its catalog references. Each NSN links to the DIBBS opportunity search for it in G2X.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"item_name": "hydraulic hose assembly", "federal_supply_class": "4720"}`
