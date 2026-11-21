---
name: places-and-trip-planning
description: Use Cerca when the user wants to recall, save, rate, annotate or remove places, plan travel from their own place history and friends' picks, compare places with someone, or import places and shared Google Maps lists.
---

# Use Cerca as the user's place memory

Use the connected Cerca MCP server and its actual tool schemas. Sign in through
the host's OAuth connection flow if access is needed; keep credentials out of
messages and files. See [tool guide](references/tools.md) for supported inputs.

## Plan a trip or decide where to go

1. Call `get_travel_context` first with the destination and, when known, its
   center latitude and longitude. Clarify ambiguous destinations.
2. Put the user's `want_to_go` places first. Treat `loved` as the strongest
   personal signal; use `get_taste_profile` for broader preferences.
3. Exclude `avoid` places from recommendations. Keep friends' recommendations
   attributed to the named people returned. Credit `cerca_picks` and
   `cerca_rating` to Cerca separately.
4. When a person is named, use `compare_with_friend`; `list_friends` can resolve
   a name to a username. Ask when a match needs confirmation. Do not reveal
   private want-to-go notes belonging to anyone else.
5. Ground names, statuses, notes, links and place facts in returned data.
   Explain gaps and pagination. Never invent hours, availability or bookings.

`search_places` searches Cerca's catalogue. It does not search Google or the
web. The assistant can use other available search tools for new discoveries
and then, when requested, save them to Cerca. Do not misattribute those
discoveries to a Cerca search result.

## Record places

- Use `save_place` for somewhere the user wants to try and `rate_place` for
  somewhere they visited. Valid ratings are `loved`, `liked`, `meh`, `disliked`.
- Prefer an exact `place_ref` returned by Cerca. Otherwise supply a Google
  Maps place URL or name plus location. If `needs_confirmation` is returned,
  ask the user to choose a candidate; retry with that candidate's real ref.
- Want-to-go notes are private. Rating notes are public on the user's profile.
  Explain that visibility and ask before publishing personal information.
- Saving with a nonblank note can replace an existing private note.
  `update_note` replaces the current note; an empty string clears it.
- Rating a saved place removes its want-to-go save, including its private note.
  Explain this consequence when moving an existing save to a rating. Obtain
  confirmation for replacements or deletion when the user's request has not
  already authorized that exact change.
- Confirm with the user before `remove_place`. It removes their save or rating
  and associated note. It does not delete the shared place or anyone else's data.
- Inspect mutation results before claiming success. A tool may return an error,
  `already_saved`, `already_rated`, `needs_confirmation`, or another outcome.

## Import places

Use `import_places` for 1–25 items with per-item status and place identity.
Inspect every result; ask about unresolved candidates and explain skipped or
failed items. Batch ratings have the same visibility and replacement effects.

Use `import_google_maps_list` only for a shared list URL supplied by the user.
It starts a background import. Report that it started, then use
`get_import_status` with the returned import ID; do not claim completion until
the returned status says so. Imports are limited to three per user per day.
Cerca cannot read all private Google lists or continuously synchronize them.

## Respect access and service limits

A read-only connection cannot mutate places. Explain how to reconnect with
write access through the host. Do not work around OAuth scopes or profile
privacy. Reauthentication, exhausted lookup budgets and provider errors must
be reported accurately. Prefer catalogue results and returned refs to avoid
unnecessary external lookups; never retry repeatedly to bypass quotas.

Cerca cannot reserve tables, book accommodation, buy tickets, charge a card,
or manage another user's account. Explain those limits without invoking
unrelated tools or claiming unsupported actions succeeded.
