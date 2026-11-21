---
name: find-activity
description: Match a business to licensable UAE business activities with Dubai Setup Index, and report which free zones and the Dubai mainland list each activity, with codes, approvals, premises and documents. Use when the user asks what activity or licence they need, or whether a free zone allows their business.
---

# Find the right business activity

Explicit user instructions take priority over this workflow.

1. `search_activities` with the business in plain words; narrow with `lane`
   (ifza, afz, ded) if the user has a route in mind.
2. `get_activity` for the candidates: the authority's own description, each
   lane's activity code and licence type, facility and approval requirements,
   and documents.
3. Report the best matches with what each covers in the authority's words.
   A match is a candidate scope, not a confirmed one; the authority confirms
   the final activity. If nothing matches well, say so rather than stretching
   a near match.
4. Report each match's regulation level and approvals. Regulated finance,
   crypto and construction lines also need their regulator's own licence;
   name the regulator from regulatoryNotice or the activity's regulators.
