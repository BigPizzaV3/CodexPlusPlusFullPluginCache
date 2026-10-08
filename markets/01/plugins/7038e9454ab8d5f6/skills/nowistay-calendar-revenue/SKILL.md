---
name: nowistay-calendar-revenue
description: Review and safely update Nowistay calendar availability, nightly rates, minimum or maximum stays, stop-sell rules, and arrival or departure restrictions. Use for pricing changes, bulk date-range updates, weekday rules, availability checks, and revenue-management tasks.
---

# Nowistay Calendar and Revenue

Read the current state before changing it, and change only fields the user requested.

## Review

1. Resolve the target properties once with `list_properties`.
2. Call `get_calendar_ari` for each target property and exact date range.
3. Summarize current availability, rates, and stay rules. Keep property currencies separate and preserve local dates.

Do not infer that a date is available from the absence of a booking alone. Use calendar availability as the source of truth.

## Update

1. Translate the request into an exact property, date range, optional weekdays, and only the fields to change.
2. Do not send availability, price, stay rules, or restrictions that the user did not ask to modify.
3. Use `update_calendar_ari_preview` once per property. For weekday updates, use 0=Monday through 6=Sunday and never send an empty `days_of_week` list.
4. Summarize the staged changes by property, dates, weekdays, rate, and rules.
5. If the user asked only for a proposal or preview, stop. If the user explicitly asked to apply the change, continue through the platform confirmation with the matching `update_calendar_ari_confirm` token.

For portfolio-wide updates, collect one approval token per property and confirm each token exactly once. Never rebuild the update payload during confirmation.

## Guardrails

- Do not silently convert currencies or copy one property's absolute rate to properties using another currency.
- Do not close dates, set stop-sell, or change arrival/departure restrictions unless explicitly requested.
- When the request is ambiguous between a percentage change and an absolute rate, ask one focused clarification before staging.
- Report partial failures per property without repeating successful updates.
