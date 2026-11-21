---
name: portravo-review-estimate
description: "Recover an existing Portravo takeoff, inspect source-linked quantities and unresolved scope, and download a reviewed, priced estimate."
---

# Review and export an estimate

Use https://portravo.com/mcp through normal OAuth. Documentation: https://portravo.com/developers/mcp. Use `get_profile` and `list_projects` to find actual owned work. Resolve ambiguous project selection before accessing another project; preserve returned IDs and reviewUrl.

Use `get_takeoff_status` for asynchronous progress and interruption recovery. This reads state without advancing work. Do not rerun extraction to recover a status or satisfy a request to review an existing estimate.

Read `get_takeoff` when available. Preserve line IDs, source links, quantities, units, confidence, selected trades and human-review status. Explain unresolved lines and scope gaps, separating automated scope, team work and any unsupported trade. Compare against the actual plan when accessible; confidence and completed status do not prove completeness, correctness or 95% whole-plan accuracy. Do not fabricate source pages or claim all trades were measured.

Complete estimator review, assembly mappings and pricing in the owned project page. These MCP tools do not edit takeoff lines or override review status. `export_reviewed_estimate` succeeds only after every line is reviewed and the estimate is priced or final. On review_required, return its actual review link and remaining step; never bypass it or label a provisional artifact final.

After success, return the actual short-lived Excel download. If it expires, request a fresh export of the same reviewed project. A progress check or export request does not authorize a new takeoff, credit purchase or billed overage.
