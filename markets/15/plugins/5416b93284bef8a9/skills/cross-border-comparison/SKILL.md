---
name: cross-border-comparison
description: Compare statutory rights or obligations across two or more named supported jurisdictions, including EU-versus-national law, employment, contractual liability and compliance requirements. Retrieve evidence for each jurisdiction and report differences and coverage gaps. Do not treat the absence of a search result as the absence of a rule.
license: Proprietary
metadata:
  author: Augment Ltd
  version: "1.3.14"
  compatibility: Requires the connected and authorised EULEX.AI MCP server.
---

# Compare jurisdictions

1. Fix the common issue, countries, event date and entity/person context. Ask
   only for missing facts that could change applicability. Confirm `list_scopes`.
2. Research each requested jurisdiction independently in its legal language.
   Use `search` with explicit scopes, then read the relevant complete articles.
   Preserve each source's jurisdiction, article, version and official URL.
3. Check status and temporal support. German snapshots are not historical
   validity evidence; EU past-date article text is unavailable. Do not blend
   dates or silently substitute current law for an event date.
4. For a common EU directive, `eu_transposition` gives reported measures only.
   Open the relevant national provisions before comparing operative obligations.
5. Return a table: issue, jurisdiction, retrieved rule, qualifications/exceptions,
   source and version. Explain practical differences after the table and identify
   unresolved questions. Do not compare similarity scores or infer equivalence
   merely because two provisions share a title.

Never turn an unsupported country, empty search or missing exception into a
statement that no obligation exists. The output is comparative research, not a
conclusion on which law governs the user's transaction.
