# Car-rental workflows

## Tool discovery

Inspect the connected Jinko MCP tool descriptors before acting. This skill intentionally does not fix a car-search tool name or schema because deployments can expose different capabilities.

If no advertised tool searches car rentals, stop and state that the current Jinko connection does not support car-rental search. Do not call unrelated tools, guess a hidden endpoint, or represent general web results as Jinko inventory.

## Search basis

Use the advertised schema and collect only the inputs it needs. Common rental inputs may include pickup and drop-off locations, pickup and drop-off date-times, driver age or residency, currency, vehicle preferences, and supplier or policy filters. Their presence here does not prove that a field is supported. Send a field only when the active descriptor accepts it.

1. Preserve exact local pickup and drop-off dates and times. Do not reduce them to dates when time affects the quote.
1. Do not assume the drop-off location matches pickup unless the tool applies that default and reports it in the returned criteria.
1. Do not invent airport, station, city, or branch identifiers. Resolve ambiguity through the advertised tool flow or ask the user.
1. Never fabricate a driver's age, residency, license status, or eligibility. Ask when the tool requires missing information.
1. Preserve every hard constraint. If no results match, offer returned relaxation suggestions or ask what the user wants to change. Do not silently broaden the search.

## Interpret results

Treat returned search criteria as authoritative. State the resolved locations, rental period, driver context, currency, and applied filters before comparing options.

Model each result as a hierarchy:

```text
vehicle option
|-- vehicle or category facts
|-- supplier and pickup facts
`-- rate plans[]
    |-- customer-facing total and included fees
    |-- mileage, fuel, coverage, deposit, and payment terms
    |-- cancellation and no-show terms
    `-- exact offer or rate-plan identifier
```

Use the actual returned hierarchy even when field names differ. A missing array or field means unknown or unavailable, not free or included. Keep supplier, vehicle, and rate-plan identifiers with the data that owns them.

When multiple records describe the same vehicle category, do not merge them unless the response supplies a stable shared identifier and explicitly defines them as rate plans for that option. Similar labels, images, capacities, or prices are insufficient.

## Refine and continue

Use only filters supported by the active tool descriptor. Preserve locations, rental period, driver context, currency, and hard constraints across a new search. Label client-side sorting and filtering as operating on loaded results only.

For pagination or continuation, use the exact returned continuation mechanism. Do not guess offsets, handles, or cursor structure.

## Selection and booking boundary

Persist a selection as the exact vehicle, supplier, rate plan, selection token, and search criteria that produced it. Before any supported cart or booking action, revalidate when required and present:

1. the exact rental period and locations;
1. the selected vehicle or category and any "or similar" qualification;
1. the supplier and pickup instructions when returned;
1. the final returned price, included and excluded taxes or fees, and currency;
1. mileage, fuel, coverage, deposit or excess, payment, cancellation, and no-show terms when returned.

Obtain explicit approval for that exact rate plan. Proceed only if the active Jinko descriptors advertise a compatible car-rental booking action. Otherwise stop at selection and explain the boundary.
