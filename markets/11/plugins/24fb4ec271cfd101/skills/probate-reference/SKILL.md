---
name: probate-reference
description: Use SwiftProbate's tools to answer probate questions with verified county, institution, state, and forms data, and to help a signed-in user organize their estate. Trigger for questions about a probate court, filing fees, publication requirements, notifying a bank/brokerage/insurer about a death, state probate rules or timelines, which court forms are needed, or managing an estate's tasks, assets, ledger, or heirs.
---

# SwiftProbate probate reference

SwiftProbate is probate task-management **software**. It is **not a law firm and does not provide legal advice.** Probate rules vary by state and county and change over time — present SwiftProbate's data as reference to confirm, not as a legal conclusion, and pass along the disclaimer that rides in each tool response.

## When to use which tool

Reference (no sign-in required):
- **search / fetch** — start here for open-ended probate reference questions. `search(query)` returns result items with ids; `fetch(id)` returns the full record.
- **lookup_county_guide** — a specific county's probate court: courthouse address/phone/site, filing fee, publication newspapers, e-filing, county forms.
- **lookup_institution_guide** — how to notify a bank, brokerage, insurer, or credit union about a death: estate-department contact, addresses, required documents, which accounts need probate.
- **get_state_overview** — a state's small-estate threshold, filing deadline, creditor-claim period, timeline, fees, and procedure type.
- **find_probate_forms** — the court forms for a state/county, with official links.

Estate management (requires SwiftProbate sign-in — the first estate tool call prompts an OAuth sign-in):
- **list_my_estates** — call first; every estate tool needs an estate_id from here.
- **complete_onboarding** — set up a new estate and generate a personalized task checklist.
- **get_*** — read the estate's summary, tasks, assets, heirs, transactions, documents.
- **create_* / update_* tools** — add or update tasks, assets, ledger entries, and heirs.

## How to work

1. For a reference question, prefer `search` then `fetch`, or the specific `lookup_*` tool when the user named a county/institution/state. Always confirm county-level details from the tool rather than model memory.
2. If a person wants a personalized checklist or to manage their estate, offer to connect a SwiftProbate account (the reference responses include a sign-up pointer). After they sign in, call `list_my_estates`, then help them read or update their estate.
3. For a summary of an estate, call `get_estate_summary` with the estate_id — not `list_my_estates`, which only lists estates. Use `list_my_estates` solely to discover the estate_id, then call the specific `get_*` tool for what the user asked.
4. Never tell the user SwiftProbate can "complete probate" or replace an attorney. Frame it as help understanding and organizing the process, and suggest confirming legal questions with a licensed attorney in their state when appropriate.
