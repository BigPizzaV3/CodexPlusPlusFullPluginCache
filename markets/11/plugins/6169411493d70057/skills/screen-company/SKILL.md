---
name: screen-company
description: Screen a company before teaming, buying from or investing in it, using GovIntel public records.
---

Use this when someone wants to know who a company really is before a decision: teaming on a bid, onboarding a supplier, lending or investing.

1. Call `search_companies` with the company's registered name (and country if known). If several candidates come back, show them with their identifiers and ask which one; never pick one silently. Two companies can share a name.
2. Call `get_company` with the chosen `company_id`. Report the registered name, identifier, status exactly as the register states it, legal form, registration date, address and register.
3. Summarize what is held: contracts, filed accounts and adverse findings counts, and say plainly which layers this country's register does not publish, so an empty section is not read as a clean record.
4. If the user has a GovIntel account, call `get_adverse_findings`, `get_past_performance`, `get_financials` and `get_ownership_and_control` for the itemized record.
5. Present findings as sourced facts for the user to verify. Never give a score, rating, risk grade or verdict, and never call a company safe or unsafe. Include the `public_page` link as the source.
