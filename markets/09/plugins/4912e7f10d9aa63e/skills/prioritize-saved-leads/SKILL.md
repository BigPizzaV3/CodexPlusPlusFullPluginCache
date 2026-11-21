---
name: prioritize-saved-leads
description: Prioritize saved Linkeddit leads against a product and buyer profile when a user asks which prospects to review, why a lead fits, or what evidence supports a relevant outreach draft.
---

# Prioritize saved leads

## Availability check

Saved-lead tools are currently disabled in the hosted connector. First check whether `search_leads` is available in the connected tool list. If it is absent, explain that this workflow is unavailable and stop; do not call it, use profile or insight tools as a workaround, invent leads, or diagnose an account permission problem. The instructions below apply only if the publisher re-enables the tools.


Use the user's product and buyer criteria. If product context is missing, `list_projects` can retrieve lead-project positioning; these are different from visibility projects returned by `answer_projects_list`. Clarify ambiguous product choices.

Use `search_leads` with supported filters: query, subreddit, status, min_score, and limit. Its query matches username, bio, audience, and industry; do not assume it searches every pain statement. Results are ranked by contactability, not purchase probability. No date filter is defined in this source; for a requested period, use returned timestamps if present and disclose when the available results cannot establish complete coverage. Never invent a supported filter.

For selected Reddit leads, `get_lead_insights` returns generated interpretations. Verify material claims using `get_user_posts` or `get_user_comments` when available and relevant. These tools take the returned username. Use public discussion evidence to identify stated business needs; avoid inferring personal or sensitive traits from a profile. `get_user_profile` is optional when its business context is actually needed.

Rank the retrieved candidates by explicit product fit, evidenced need, recency when known, and blockers. Preserve the stored contactability score separately from your reasoning. Show the source, evidence date when available, and why each candidate merits review. Say when results are a limited sample. A scraped profile or generated insight does not establish consent, a verified identity, or current buying intent.

Draft outreach only when requested, using supported statements and a useful response to the person's actual question. Do not send messages, post replies, change lead status, or claim contact occurred. If there are no matches, report that result and suggest a specific filter adjustment rather than silently broadening the search.
