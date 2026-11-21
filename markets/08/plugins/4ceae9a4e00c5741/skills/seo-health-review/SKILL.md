---
name: seo-health-review
description: Review the SEO health of one of the user's SERPHub sites and turn it into a short, prioritized list of fixes. Use when the user asks how a site is doing, what to fix first, for an SEO check-up or health review, or for a weekly or monthly SEO summary.
---

Use this skill when the user wants an overall picture of how one of their sites is doing and what to fix, rather than a single number.

## Inputs
- The site. If the user did not name it, or named one that `list_sites` does not return, call `list_sites` and ask which site. Never guess a `site_id`.

## Steps
1. Call `get_site` for the chosen site to see whether an audit is running and which integrations are connected.
2. Call `get_audit`.
   - If it reports an audit is running, say so and do not start another. Offer to check `get_audit_progress`.
   - If there is no completed audit, say so and offer to start one with `run_audit`. Ask first: it crawls the site and replaces audit results older than the account's retention limit.
3. Call `get_issues` with `severity` set to `high`. If there are fewer than five, call it again for `medium`.
4. If Search Console is connected, call `get_search_overview` for the trend in clicks, impressions and position. Remember that a lower position is better, and that Search Console data runs about two days behind.
5. Call `get_uptime`. If monitoring is off or there are no checks, say that rather than reporting the site as up.

## Output
- One line on overall health: the audit score and the direction of search performance.
- Up to five fixes, most important first. For each: what is wrong, how many pages it affects, and one example page URL from `get_issues`.
- Anything urgent outside the audit, such as downtime or a sharp drop in clicks.

Then offer to create SEO tasks for the fixes with `create_task`. Only create tasks the user agrees to, one call per task, with the priority they choose.

## Do not
- Do not invent issues, page counts, scores or trends. Report only what the tools returned, and say plainly when a tool returned nothing.
- Do not start an audit or create a task without the user's confirmation.
- Do not compare the site with competitors unless the user asks, and then only with `get_competitors` data.

If the user's own instructions conflict with this skill, follow the user.
