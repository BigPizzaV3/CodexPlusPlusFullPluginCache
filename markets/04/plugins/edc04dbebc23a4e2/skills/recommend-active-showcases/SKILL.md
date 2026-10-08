---
name: recommend-active-showcases
description: Identify currently active or date-specific Pokémon GO PokéStop Showcase categories from contemporaneous observed early-region reports, then rank eligible Pokémon from the connected PoGo Showcase Manager data. Use when a user asks which active showcases to enter or prioritize, which Pokémon to use in them, or for a recurring showcase recommendation.
---

# Recommend Active Showcases

Use live public observations to establish showcase categories and the PoGo Showcase Manager MCP server as the authoritative source for the user's Pokémon, entries, and season results. Never substitute expected rotations or event predictions for observations.

## 1. Establish the target period

Determine the requested showcase date or period and the user's timezone from the request or available context. If neither is supplied, use the current date and the user's local timezone when known.

For a request tied to a local cutoff, convert every source timestamp to the user's timezone and state the converted time. Account for daylight-saving time. Do not assume Europe/Brussels unless it is the user's known timezone.

Determine the Pokémon GO season that contains the target showcase date, including its exact start and end dates. Prefer an official Pokémon GO season announcement or other authoritative source; use reliable secondary sources only when an authoritative source is unavailable. Do not assume the season from its name or from a fixed three-month pattern. For a historical target date, use the season active on that date rather than the current real-world season.

## 2. Verify the active categories

Search the web for contemporaneous reports from regions where the showcases were already live at the relevant time.

1. Look first for a direct New Zealand report from `@AKiwiIsNotAFru1`, when available, or an equivalent established New Zealand or Australian observer.
2. Verify that the post was published before the requested cutoff and explicitly describes observed PokéStop Showcases. A prediction, infographic, datamine, event announcement, or rotation-based inference is not an observation.
3. Extract the complete observed category set, including every independently running species, type, size, buddy, or other restriction. Do not collapse distinct categories.
4. Cross-check the complete set against at least one independent contemporaneous source when possible. Prefer another early-region observation, such as a separate observer or an on-the-ground report in r/TheSilphRoad.
5. Ensure supposedly independent sources do not merely repeat the same underlying report.
6. When sources conflict, prefer direct contemporaneous observations over later archives or summaries. Explain the conflict instead of silently choosing.

Classify each category as:

- **Confirmed**: supported by direct observation and independently corroborated when possible.
- **Observed but not corroborated**: supported by one credible direct observation only.
- **Conflicting**: contemporaneous observations disagree.
- **Unconfirmed**: predicted, inferred, incomplete, or unsupported.

Use only confirmed categories for firm recommendations. A credible but uncorroborated category may receive a clearly provisional recommendation when useful. Never promote an unconfirmed or conflicting category to confirmed by guessing.

If web access is unavailable, say that the active categories cannot be verified. Do not use model memory as current evidence. Cite or link the observation sources and include their publication times in the response.

## 3. Read the user's showcase data

Use the connected PoGo Showcase Manager tools rather than assuming a Google Sheets filename or tab. Inspect the available tool schemas first, then retrieve enough records to evaluate all confirmed categories. Handle pagination and do not rank only the first page of results.

Use all relevant fields exposed by the service, including:

- species and form;
- type;
- showcase score;
- buddy level;
- last showcase win date;
- entered, reserved, unavailable, or equivalent status information.

Treat the service data as authoritative for the user's collection. Do not invent a value for a missing field or silently treat an unknown value as favorable.

## 4. Apply eligibility rules

Match Pokémon only against the exact confirmed category constraints. Respect species, form, type, size, buddy, and any other stated restrictions.

Interpret buddy requirements exactly:

- **Great Buddy or higher**: Great, Ultra, and Best qualify.
- **Ultra Buddy or higher**: Ultra and Best qualify.
- **Best Buddy**: only Best qualifies.
- Blank, unknown, or unrecognized Buddy Level does not qualify unless another authoritative service field explicitly proves qualification.

Compare each Pokémon's last showcase win date with the exact boundaries of the season containing the target showcase date:

- Exclude the Pokémon when the last win date falls within that season, including the first and last date.
- Do not exclude it when the last win date is before that season.
- Treat a blank last win date as no recorded showcase win unless the service exposes a separate field indicating otherwise.
- If the last win date is malformed, lacks enough precision to place it relative to a season boundary, or conflicts with another authoritative service field, label the candidate **cannot assess** rather than assuming eligibility.
- Interpret a date-only value as the user's local calendar date. For a timestamp, convert it to the user's timezone before comparing calendar dates.

Do not compare the last win against the current real-world season when evaluating a different target date.

Respect entered, reserved, unavailable, or equivalent status fields. An already-entered Pokémon may be reported as current coverage but must not be presented as freely available for another simultaneous showcase unless the service data proves that it is reusable.

Use these outcomes consistently:

- **Eligible**: every required rule was evaluated and passed.
- **No eligible candidate in the data**: the necessary fields were available, but every candidate failed at least one rule.
- **Cannot assess from available data**: records or required fields were missing, inaccessible, incomplete, or ambiguous.

Do not turn **cannot assess** into **no eligible candidate**.

## 5. Prioritize recommendations

Rank eligible candidates within each category primarily by showcase score, highest first. Then account for availability, current entry status, and useful coverage across multiple simultaneous categories. Do not claim a score advantage that is absent from the service data.

Prioritize showcase targets using the strength and availability of the user's eligible candidates. Prefer a category with a strong available candidate over one with no assessable or eligible candidate. When exact competitive odds, local participation, or opponent scores are unavailable, describe the recommendation as collection-relative rather than predicting a win.

Avoid recommending the same Pokémon for simultaneous placements unless reuse is explicitly possible. When allocation matters, provide a practical assignment of distinct Pokémon across the target showcases.

## 6. Respond concisely

Lead with the prioritized action list. Include:

1. Confirmed categories, plus any provisional, conflicting, or unconfirmed categories.
2. Which showcases to target in priority order.
3. The best specific eligible Pokémon for each target, with score and the fields material to eligibility.
4. Relevant alternatives when they improve allocation across simultaneous showcases.
5. Categories with no eligible candidate, kept distinct from categories that cannot be assessed.
6. Source links, observed publication times, and any evidence or data caveats.

Keep research confidence separate from candidate eligibility: a well-supported category can still have no eligible Pokémon, and a strong candidate does not make an uncertain category confirmed.
