---
name: propalt-csv-export
description: "Use when a user wants to export the final selected UK property list from the conversation to a Propalt.io-compatible CSV for My Lists or direct-mail workflows, with exactly address1, town, and postcode columns. Trigger only after the intended property set is clear; do not use during ongoing audience refinement."
---

# Propalt CSV Export

Convert the final agreed property list into a Propalt My Lists CSV.

## Required CSV schema

Exactly these columns, in this order:

`address1,town,postcode`

- `address1`: building number/name plus street address, excluding town/postcode where the structured record makes that separation possible.
- `town`: town/city from the property record or a clearly established address component.
- `postcode`: full UK postcode.

## Workflow

1. Identify the most recent final property set in the conversation. Exclude properties explicitly removed or discussed only as examples.
2. If the set is genuinely ambiguous, confirm the list once before exporting.
3. Prefer structured address fields already returned by Propalt. If a property is only a free-text reference and cannot be reliably resolved, use `address_lookup` before export.
4. Deduplicate the list by a stable property identifier when available; otherwise use normalized full address/postcode.
5. Never infer a missing town or postcode from vague context. Leave the field blank or flag the record for verification.
6. Escape CSV values according to standard CSV rules; UTF-8; one property per row; no extra columns.

## Delivery

If the host supports file creation, create `propalt-export.csv` and provide it to the user. If file creation is unavailable, return the exact CSV content in a fenced code block so the user can save it as UTF-8 CSV. Do not depend on a host-specific delivery tool or fixed filesystem path.

After export, state the number of rows and flag any records with incomplete address data. Do not add unselected properties merely to increase list size.
