---
name: aviation-identity
description: Resolve and cross-check aviation identifiers (airports, airlines, aircraft types, registrations, flight designators) with the Airside Labs Aviation Tools, on the right date, and report confidence and sources honestly.
---

# Aviation identity: resolve, date, cross-check

Use this workflow whenever a question names an airport, airline, aircraft type, registration or
flight number and the answer depends on which entity that identifier means.

## Steps

1. **Fix the date first.** If the question is about the past, pass `as_of` (YYYY-MM-DD) on every
   call. Airport codes move (ATH, HKG) and airline two-letter designators are reused (SN was
   Sabena, then Brussels Airlines). Without a date the tools answer for today, which is silently
   wrong for historical data.
2. **Resolve each identifier** with the matching tool: `resolve_airport`, `resolve_airline`,
   `resolve_aircraft_type`, `resolve_registration`, `parse_flight_identifier`. Prefer ICAO
   identifiers (four-letter airports, three-letter airlines) when carrying a result forward; they
   are not recycled the way IATA codes are.
3. **Read `status` and `confidence` before the value.** `resolved` at 1.0 is a unique match.
   0.7 to 0.99 came through an alias or a historical record; say so. 0.4 to 0.69 means
   `alternates` is populated: ask the user which one rather than choosing. `ambiguous` with a
   `country_hint` available: call again with the hint. `unresolved` is a real answer, not an
   error; do not invent one.
4. **Cross-check** when identifiers come from more than one source (a registration from a
   movement message and an address from a surveillance track, a flight number and an airline):
   call `validate_identifiers` with all of them and the date. `contradicted` means at least one
   check failed; never average it away. `consistent_where_checkable` with
   `unverifiable_count` above zero is partial coverage, not a pass: say which checks were silent.
5. **Cite.** Every field in `best` has an entry in `provenance` with a source id and retrieval
   date. Quote the source when the answer will be relied on.

## Output requirements

- State the date the answer applies to.
- Give the resolved entity with both code systems where the tool returns them.
- Name the confidence band in words (exact match, via alias, one of several candidates).
- If anything was unresolved, ambiguous or unverifiable, say so in the first sentence, not the last.

## Do not

- Use these tools for live status, schedules, slots, fleet lists or routes; they answer identity
  questions only.
- Present an unresolved result as a hint that the thing does not exist; coverage is not global.
- Drop the date from a follow-up question because the first call had one.

## Example

User: "Which airline was SN in 1995, and is BA117 a British Airways flight?"

1. `resolve_airline` with identifier `SN`, `as_of` `1995-06-01`: read `status`; if `ambiguous`,
   report the best candidate and the alternate with the tool's reason.
2. `validate_identifiers` with airline `BA`, flight `BA117`, `as_of` today: report the verdict
   and the checks.
3. Answer with the date, the entities, the confidence in words, and the sources.
