---
name: nowistay-portfolio-reporting
description: Build privacy-minimized Nowistay financial and operational reports across many properties. Use for CSV or spreadsheet exports, revenue and fee totals, OTA commissions, cleaning costs, team-member billing, workload reports, owner statements, and booking-to-mission reconciliation.
---

# Nowistay Portfolio Reporting

Favor complete table-shaped extraction over repeated detailed calls.

## Collect data

1. Confirm the requested date range, portfolio scope, grouping dimensions, and output format. Infer obvious values from the prompt instead of asking unnecessary questions.
2. Resolve properties once with `list_properties`. Omit `property_ids` from later list calls when the user wants every eligible property.
3. Call `list_bookings` with `response_format=table`, `include_details=false`, `limit=500`, and `offset=0`.
4. Append each page's `rows` under the returned `columns`. Continue with `resultMetadata.nextOffset` while `resultMetadata.hasMore=true`.
5. Call `list_missions` in the same table mode only when the report needs cleaning, operations, assignments, workload, or team-member data.
6. Join booking and mission rows with `bookingId` when combining finances and operations. Use property IDs only as a secondary key.

Never restart the extraction property by property unless the user explicitly requests separate queries or the server requires it. Never use `get_booking`, `get_mission`, or `include_details=true` for a bulk export.

## Minimize personal data

- Select and retain only the source columns needed for the requested report.
- Exclude guest names, contact details, reservation references, message content, private notes, and mission descriptions from financial, owner, billing, and workload reports unless the user explicitly requests a specific field and it is necessary for that report.
- Do not call tools with contact-detail or private-note include flags for aggregate reporting.
- Team-member names may be included when the user requests assignment, workload, or billing by team member. Do not include their contact details.

## Calculate and verify

- Keep currencies separate. Never sum EUR and USD into one total.
- Keep cancelled or unavailable bookings separate from active revenue unless the user defines another rule.
- Preserve source columns in the detailed sheet and add calculated summary sheets or tables.
- Support grouping by property, team member, mission type, booking channel, status, month, or currency.
- Reconcile row counts against pagination metadata before reporting completion.
- State filters, exclusions, currency handling, and any missing source values in the result.

## Deliver

For a requested CSV or spreadsheet, create the file from the complete concatenated rows. Include a readable summary plus a privacy-minimized detail sheet containing only the columns needed to audit the totals. If the user only asks a question, return the totals directly without creating a file.

Do not claim data is truncated when `hasMore=false` and all pages were collected. A shortened tool card is a display behavior, not evidence that the structured result is incomplete.
