---
name: homeload
description: Size a home's air conditioner, heat pump or furnace, size a portable or standby generator, or check whether an existing electrical panel can take a new load such as an EV charger or heat pump, for houses in the US by city or ZIP code. Use when a user asks what size system their house needs, whether a quoted size is right, or whether their panel has room.
---

# HomeLoad workflow

Use the connected HomeLoad tools whenever the task is sizing residential HVAC, a generator, or
electrical-panel capacity for a house in the United States.

## Tools
- `size_hvac` — cooling and heating load and the Manual S tonnage range from ZIP, square feet
  and construction. Needs conditioned square feet and where the house is. A city and state is enough:
  pick a residential ZIP code in that city rather than asking, and name the county the result used. Never use a place
  the user has not stated, and never ask for a street address.
- `size_generator` — running and starting watts and the generator class from a list of load ids
  (plus custom loads with nameplate watts). Ask which appliances matter before listing a whole house.
- `panel_headroom` — NEC 220.83 calculation for an existing service: ZIP, square feet, panel
  rating, existing 240 V appliances, and what is being added. Set `strip_kw` when a heat pump
  with electric auxiliary heat is added.

## Behaviour
- Every result is a range or a calculated figure with its inputs; present it as an estimate to
  confirm with a contractor's Manual J or a licensed electrician. Keep the tool's note; do not
  raise the certainty.
- The card shows the range, a scale with the Manual S band, the assumptions, how the size
  moves if the insulation differs (`sensitivity`), what the figures were checked against (`basis`)
  and a button that opens an installer or electrician sheet. Write three sentences: the range; the one assumption
  that moves it most, taken from `sensitivity`; that a contractor's Manual J (or a licensed
  electrician) confirms it. Do not repeat the card's table or basis, and do not paste the link
  unless the card fails to load.
- When the user is checking a contractor's number or an installed unit ("they said 4 tons"), pass it
  as `quoted_tons`, ask the year built and the window type before calling if they are not given, and
  lead with the verdict in `quote_text`. A "near" verdict is not a finding against the contractor.
- When the user asks whether a generator they have will run the loads, pass its running rating as
  `have_kw` in kW (7.5 for 7,500 W), and `have_starting_kw` if known. An advertised peak is not the
  running rating: ask if unsure.
- `size_hvac` gives a heat pump's output at the design temperature and the backup it leaves
  (`heat_pump_text`). If the user then asks about the panel, pass `backup_strip_kw` as `strip_kw`.
- Do not recommend brands or models, quote prices, or advise on financing.
- Do not use the tools for commercial buildings, single rooms, RVs, job sites, subpanels or
  three-phase services, or for homes outside the 50 US states and DC.
- If a tool reports an unknown ZIP code you picked, try a nearby residential ZIP. If the user typed it, say it was not
  found and which ZIP you used instead; if it reports invalid
  input, relay the message and ask for the corrected value.

If the tools are unavailable, say that the HomeLoad sizing service could not be reached. Do not
fabricate a HomeLoad result.
