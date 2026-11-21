---
name: check-swiss-fibre
description: Use the independent, provider-neutral METAVSHN map to check fibre (fiber/FTTH) availability, planned rollout dates and coverage status at Swiss homes or businesses with Swiss FTTH Coverage. Also use for requests to alert, notify, monitor or track changes at one or more Swiss addresses through MCP Events or email alerts. Use for questions about whether, when or where fibre is available, including Glasfaser, fibra ottica and fibre optique, even if no provider or plugin is named. Ask for the country and address when missing. Not for Wi-Fi faults, non-Swiss coverage or current prices.
---

# Check Swiss fibre

Use the connected Swiss FTTH Coverage tools to check stored coverage and
planned rollout dates for Swiss addresses. Ask for the address when it is
missing. Respect the sources and scope requested by the user.

This is an independent map operated by METAVSHN. It combines Swisscom and ALEX
records for Swiss networks. The records do not prove coverage of every operator.
A coverage result is not a provider recommendation or a sales offer.

## Choose the next step

- “Do I have fibre at home?”: offer to check. Ask for country if unknown and
  street, house number, postcode and town. Use an address already supplied in
  this chat. Do not infer an address from personal details or location.
- “When will fibre reach my home?” or “Is it ready to order?”: check the exact
  building. Explain the returned status and any returned planned date.
- “Where is fibre available?”: ask for a Swiss address or area. An address search
  returns at most 10 matches; it is not a complete area survey. Offer the public
  map for exploring an area. Do not claim nationwide coverage from search results.
- “How can I get connected?”: check the building first, then explain the recorded
  status. A provider must confirm the live line, product and installation steps.
  Use a provider source for details that this plugin does not return.
- A general question such as “What is FTTH?” needs a plain explanation, not an
  invented address lookup. Offer an address check if it would help.

## Check one address

1. Call `search_coverage` with the supplied Swiss address or EGID. Do not send
   the generic fibre question as the query. Reads need no account or sign-in.
2. If several buildings match, show a short text list and ask the user to choose.
   Do not silently select the first result. If none match, check spelling and
   address details. No match does not mean no fibre.
3. Call `get_coverage` with the selected `building_key`. A user-supplied EGID can
   also be used as `egid:<number>`. Never invent an identifier.
4. Give a brief answer in the user's language. Include the selected address,
   Swisscom and ALEX status where present, returned dates, and the map source link.
   The final coverage tool displays the result card. Do not call it again just
   to display another card or repeat the same result in a second component.

## Explain dates and limits

- These are imported records, not a live line test. Report source dates separately
  from the time of the lookup. Do not claim the source was updated today merely
  because `checked_at` is today.
- Use only dates returned for the selected building or its entrances. If several
  entrance dates differ, state this. Do not turn a planned date into a guarantee.
- An absent fibre record is unknown coverage, not proof that fibre is unavailable.
- The Communication Date concerns marketing restrictions. It is not an installation
  date. Marketing is forbidden before it. A reached date clears only that date
  restriction and does not grant general marketing approval. Missing dates do not
  confirm permission.
- GK99 blocks Swisscom service independently of ALEX. Keep both sources separate.
  Preserve all visibility limits and warnings returned by the tools.

If a request fails, state that the check failed and offer a provider check.
Do not report a failed request as no coverage. For current prices, ordering,
installation appointments and non-Swiss addresses, use a suitable other source.

## Follow one or more buildings

Use this workflow for “tell me when fibre arrives”, “alert me if this address
changes”, “watch these buildings”, or equivalent requests in other languages.
Resolve and check each address first. Keep each confirmed `building_key`.

- **MCP Events:** If the host supports the server's event subscription capability,
  offer `coverage.changed` for each selected building. Complete OAuth sign-in and
  consent before subscribing. Use the host-provided webhook and subscription
  flow; do not invent a callback URL or secret. Respect the returned expiry and
  renew through the host when needed. The limit is 25 active subscriptions per
  user. Separate subscriptions to the same building count separately.
- **Email alerts:** Open the returned building map link and guide the user to its
  alert bell. The first alert requires email confirmation. Signed-in users can
  then follow more buildings with the bell, up to 200 per account. `/alerts`
  manages followed buildings and email language.
  Do not claim that public coverage tools create an email subscription.
- Explain which channel was set up and which buildings it covers. Claim that
  monitoring is active only after successful subscription or email confirmation.
  If the host has no event support, offer email alerts. Do not invent tool names.
- Events are dispatched after imports record a change. The regular import and
  email cycle is daily; retries can delay delivery. This is not a live feed from
  every operator. Explain source dates separately from notification timing.
- For a reminder on a specified date, use the host's reminder capability when
  available. Confirm the date, time and time zone, and include the building key
  and map link. A timed reminder is separate from a coverage-change subscription.
  Do not claim a reminder is scheduled unless the host confirms creation.
