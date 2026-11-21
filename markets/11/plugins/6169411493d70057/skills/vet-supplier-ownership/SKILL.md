---
name: vet-supplier-ownership
description: Check a supplier's declared ownership, foreign ties and exclusions from public records.
---

Use this when someone needs to know who owns or controls a supplier, or whether it is excluded from government contracting.

1. Resolve the company with `search_companies`, confirming the exact entity by its identifier.
2. Call `get_company` for the registry record and summary.
3. With an account, call `get_ownership_and_control` for declared parents and controllers and how each link was matched, and `get_adverse_findings` for exclusions, sanctions-list matches and integrity records.
4. Report each item with its source and how it was matched. A name match is a lead to verify, not a finding. Say what the public record cannot show (beneficial owners beyond declared parents, facility clearance or FOCI mitigation status, classified work).
5. Do not draw conclusions about individuals. Never give a verdict on whether the supplier is acceptable; present facts for the user's own review.
