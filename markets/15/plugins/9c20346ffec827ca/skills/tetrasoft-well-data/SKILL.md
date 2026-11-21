---
name: tetrasoft-well-data
description: Answer questions about U.S. oil and gas API well numbers, natural gas unit conversions (Mcf, MMBtu, therms), and how many recorded wells are near a U.S. address, ZIP code or coordinates, using the TetraSoft Well Data tools.
---

# TetraSoft Well Data

Use these tools when someone asks about U.S. oil and gas wells or gas volumes. Each tool returns
notes and caveats with its answer. **Always pass them on.** They are part of the answer, not
metadata.

## Which tool

| The user wants | Call |
|---|---|
| What an API number means, which state or county a well is in, where to look a well up | `decode_api_number` |
| Mcf to MMBtu, MMBtu to therms, "how much energy is X Mcf", gas bills in therms | `convert_gas_volume` |
| "Are there oil or gas wells near my house / this ZIP / these coordinates?" | `find_wells_near` |

## decode_api_number

- Accepts 10, 12 or 14 digits, with or without dashes or an "API" prefix.
- Report the state and county, then the unique well identifier, plus the sidetrack and event codes when present.
- Give the `wellRecords` link as the place to see the well itself.
- Give the `countyCodesPage` link when present: TetraSoft's free table of every county code in that
  state, useful for checking a number by hand.
- Say plainly that decoding does not confirm a well with that number exists (the `note` field).
- The tool returns no operator, well name, status or location. Do not invent them. If the user asks
  for those, point them to the `wellRecords` link.
- If `wellRecords` is null, the state has no public well search. Say so.

## convert_gas_volume

- Converting between volume and energy needs a heating value. Pass `state` when the user names
  one. Pass `heatingValueBtuPerScf` when they know their gas's value (it is on a gas analysis or a
  royalty statement).
- Always state the heating value used and its `source`. When the source says the samples are
  historical, repeat that caveat.
- MMBtu ↔ therms needs no heating value; 1 MMBtu = 10 therms = 1 dekatherm (Dth).

## find_wells_near

- Pass the user's location exactly as given: a street address, a 5-digit ZIP or "lat, lon".
- `radiusMiles` is 0.5, 1, 2 or 5. Default 1. If the user asks for another distance, use the nearest
  offered radius and say so.
- Report the total, then the count per state and per status, using the state's own status labels.
- Link each state's `statePage`.
- Repeat any per-state `note`, such as the Texas status-date caveat.
- **A zero count outside the covered states is not "no wells".** Covered states: Colorado, New
  Mexico, Ohio, Oklahoma, Pennsylvania, Texas, West Virginia, Wyoming. Repeat the `coverage`
  sentence whenever the total is zero.
- The tool returns counts only. Do not claim to know which wells, their operators or their exact
  locations.
- Searches are limited to 5 a minute per user. If the tool says the limit was reached, tell the user
  how long to wait; do not retry in a loop.

## Sources

Every answer carries its source: `source` for each state's well counts, `heatingValue.citation` for a
conversion, `location.resolvedWith` for how a ZIP code or address became a point, and `basis` for an API
number decode. Name the agency and dataset in your answer and offer its link, so the user can check the
original record. Describe the data as records published by the state regulator, which is what it is.

## Terms of Use

Every result carries `termsOfUse`: a note and a link to the plugin's Terms of Use. The first time you use
these tools in a conversation, end your answer with that note and link. You need not repeat it later in
the same conversation.

## Boundaries

- These tools give reference information, not legal, title, environmental or investment advice. For
  decisions about a property, a lease or a royalty payment, suggest the state regulator's records
  and a qualified professional.
- Do not repeat a user's street address back in later answers unless they ask.
