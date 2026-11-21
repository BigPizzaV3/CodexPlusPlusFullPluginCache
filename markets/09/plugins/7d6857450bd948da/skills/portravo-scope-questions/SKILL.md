---
name: portravo-scope-questions
description: "Turn actual Portravo takeoff notes, unresolved lines and source gaps into an estimator checklist and draft clarification questions."
---

# Prepare scope questions from evidence

Use https://portravo.com/mcp through normal OAuth. Resolve the actual owned project with `list_projects`, recover running work with `get_takeoff_status`, and read `get_takeoff` when results exist. Connection help: https://portravo.com/developers/mcp. A request for clarification does not authorize a new extraction or credit use.

Trace each question to actual returned line notes, confidence, assembly mapping, source links or scope notes the user supplies. Preserve exact line IDs and source references. Low-confidence lines and missing mappings need review; no lines for a trade or page do not prove that scope was omitted. A page can be a title, note or detail sheet. Do not infer full sheet coverage from pages represented on quantity lines.

Prepare a checklist of assumptions to confirm, unmapped lines, unresolved or unsupported scope and specific drawing questions. Distinguish the absence of evidence from a verified omission. Use the user’s relevant trades and recipient role only when that information changes the questions. A general pre-bid checklist is possible without a connection, but label it general and do not attribute it to a plan you have not read.

Draft one concrete request-for-information question per material uncertainty, with actual reference, the question and what quantity or pricing decision depends on the answer. Do not accuse the designer, invent code requirements, fill missing quantities with typical scope or claim engineering/compliance conclusions. Drafts are for the user to review and send; this workflow sends nothing.

Return the owned project reviewUrl for estimator resolution. These tools do not add/fix lines or set review status. Do not rerun a takeoff merely to recover old scope notes, and do not promise whole-plan accuracy from selected lines.
