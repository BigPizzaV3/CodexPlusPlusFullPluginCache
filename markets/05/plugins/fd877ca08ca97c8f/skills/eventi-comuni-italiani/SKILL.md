---
name: eventi-comuni-italiani
description: Use when the user asks what is going on in an Italian town or area on given dates, or looks for sagre, village feasts, patron saint festivals, food and wine fairs, street markets, concerts or exhibitions in Italy. Covers how to resolve a town identifier, how to filter by date and category, and how to report admission and sources without overstating what the data says.
---

# Local events in Italian towns

The catalogue is rebuilt every day from the notices that Italian town halls are
required to publish on their official register (the *albo pretorio*). That is
why it covers very small towns that no other calendar lists, and it is also why
the records are only as complete as the underlying document.

## Finding the right events

1. **Resolve the town before searching by town.** The `comune` argument is an
   identifier in lowercase with hyphens, such as `barolo` or
   `santo-stefano-belbo`, not a display name. Call `comuni_coperti` first when
   the user names a town, and use `regione` to narrow the list.
2. **Prefer a region search when the user names an area, not a town.** Places
   like the Langhe, Salento or Val di Susa span many towns and are not a single
   identifier. Search the region, then filter what you report.
3. **Dates are `YYYY-MM-DD`.** Turn "this weekend" or "next month" into an
   explicit `dal` and `al` range before calling. Without a range you get what is
   upcoming, which may be months away.
4. **Free text needs at least three characters** and matches title and
   description, so it works well for a theme such as a chestnut festival and
   badly as a substitute for a place.

## Reporting results honestly

- **Silence about admission is not "free".** The detail of an event states the
  admission only when the source document does. If no admission line is
  present, say it is not stated rather than assuming it costs nothing. The same
  applies to times, which are frequently absent.
- **Give the link to the event page** with any event you report. It carries the
  link to the official document the record came from, so the user can check.
- **Say where it comes from.** These records are extracted from municipal acts
  with the help of a language model. When you present details such as dates and
  times, tell the user they are worth confirming on the source, especially for
  anything they would travel for.
- **Do not invent the missing parts.** Venue, organiser and programme are often
  partial. Report the gap instead of filling it.

## Out of scope

This covers scheduled public events only. It has no restaurants, no
accommodation, no weather, no opening hours of museums or shops, and it does not
sell or reserve tickets. It also does not expose the municipal acts themselves,
only the events derived from them. For anything in that list, answer from your
own knowledge or other tools and do not force a search here.
