---
name: heffl-field-service
description: "Create field-service jobs, contracts, recurring maintenance visits, and customer properties in Heffl, or report on scheduled service visits."
---

# Field-service jobs and visits

Read ../heffl-crm/references/operating-rules.md. Canonical objects: fs_jobs, fs_properties, fs_schedules, clients, products. Describe fs_jobs on its write/create surface once; resolve the named client and list the requested service in products. Use the actual returned product ID and price.

List fs_properties filtered by the resolved clientId and inspect name, address and city to select the intended site. Do not search globally by customer name. Clarify only remaining ambiguity. If no site exists, describe fs_properties and collect required address data before creating one.

Collect missing service date and price together. Do not invent dates or reuse historical pricing unless requested. A zero catalogue price does not imply the service is free. Create a normal one-off with records_create, object:"fs_jobs", values including type:"ONEOFF", fsPropertyId, startDate and requested service lineItems. The client is derived from the property; do not send clientId. Do not send generated numbers, totals or status. Use productId:null for a free-text service.

Omit fsSchedules unless custom visits are explicitly requested; the server generates visits and IDs. Dates use YYYY-MM-DD. All-day visits omit startTime/endTime; timed visits supply both as ISO timestamps in the workspace timezone. Contracts use type:"CONTRACT" and require endDate. Supply frequencyRule only for requested recurrence; paymentsCount must be nonnegative and no greater than visit count. Resolve assignees only when named.

For reports describe unfamiliar read fields once. Filter jobs directly by clientId and preserve requested visit date versus completion date semantics. Do not add invoiceRequired or count parent job totals once per visit. Return the actual receipt and link; do not claim that a timeout proves creation failed.
