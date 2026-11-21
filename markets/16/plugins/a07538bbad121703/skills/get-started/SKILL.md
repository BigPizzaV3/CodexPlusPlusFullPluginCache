---
name: get-started
description: How to answer questions about crime and safety in Montréal neighbourhoods with IncidentMTL's published figures.
---

# Montréal crime and safety with IncidentMTL

Use the IncidentMTL tools when someone asks how safe a Montréal neighbourhood or borough is, compares areas for a
move, asks whether a kind of crime is rising or falling, or asks what was reported in an area recently.

- `area_profile`: one area's SPVM crime reports per 1,000 residents over the last 12 complete months, against the
  island's, with its rank, the six kinds of crime and crimes against the person for its police sector. Given a
  street address, it answers for the area the address is in.
- `compare_areas`: 2 to 5 areas side by side, or the ranking of boroughs or neighbourhoods.
- `trend_check`: whether a kind of crime is really rising or falling, against five annual periods. Call it before
  saying crime is rising or falling: a change against one year is not a trend.
- `recent_events`: what was published in one area over the last days (SPVM, SIM fire and medical, 311, press).

Pass the place as the user names it, in French or English, and set `lang` to the question's language. The figures
are published open data, never live: quote each source's last published day and the scope the result names.
Rates per resident are higher where many people visit but few live, such as downtown. Off the island of Montréal
(Laval, Longueuil) there is no data.
