---
name: daoco-website-improvements
description: Work through the website fixes Daoco's site audits and AI visibility checks found, such as titles, meta descriptions, structured data, FAQ sections, or missing pages, and record progress back in Daoco. Use when the person asks to fix their site's SEO or AI visibility issues, or to work on improvements queued for an AI app.
---

# Fix the brand's website from Daoco's findings

Read [the shared Daoco workflow](../daoco-marketing/SKILL.md) for brand selection and tool boundaries.

Daoco audits the brand's site and checks how AI answer engines cite it, and records each fix on the Improve tab. This app sees the same list. A coding agent working in the site's own codebase can make the change, then tell Daoco. These tools change only Daoco's record; nothing on the website changes through them.

## Pick the work

Work on improvements only when the person asks. "Work on my queued improvements" means `list_improvements` with `status: "queued"`: the ones set aside in Daoco with Queue for AI app. `get_brand_context` says how many are queued. Otherwise list by `status` or `route` and let the person choose; results page with `cursor`.

Each improvement has a plain-words `why`, its target page, priority, `status`, and `progress`. `in_flight` means a Daoco thread is on it, and `started` means an app or an unpublished page is; leave both alone unless the person says otherwise. `open` with `stillFoundAt` means a fix marked done that a later check still found; it can be taken on again. `route` says how the brand wants that kind of fix made: `ai_app` (this app), `cms`, or `github` (Daoco makes it), or `none` (a fix on another site).

Call `get_improvement` before changing anything. It gives the measured signal, the suggested change, what the audit saw on the page, the target query, and when it counts as done. When the brand's Search Console is connected, `get_site_report` shows how the page or query is doing now, with no workspace tokens.

## Make the change

1. Record `update_improvement` with `status: "in_progress"` before starting, with a `note` (the branch or what is changing). Pass `ids` for up to 20 at once. If the reply says someone else already has it, stop and tell the person.
2. Make the change in the codebase the person is working in, following its conventions. Base copy on the suggested change and the brand's saved context (`get_brand_context` with a `task`). Do not invent facts, prices, authors, reviews, or data to satisfy a finding; ask the person or leave it.
3. Record `status: "done"` with a `note` and a `link` (commit, pull request, or live page) once the change is live, not when it is only committed or in review. If it is merged but not deployed, keep it `in_progress` and say so.
4. Hand an improvement back with `status: "todo"` when the app will not finish it.

Daoco confirms fixes itself. Anything a page audit measures (title, meta description, headings, alt text, structured data, canonical, robots, Open Graph, FAQ, comparison table, named author) waits as `waiting_live` until the next audit of that page measures it fixed. Other fixes count as live unless the check that found them records them again. Then Daoco measures the result. Report the status the reply gives, not "fixed".

## When Daoco should make the change

For a fix routed to `cms` or `github`, or when the person would rather Daoco did it, ask Daoco to make it: the `fix-site` workflow with the improvement's id through `run_workflow` where it is listed, or `start_work` asking in words to fix that improvement. It uses workspace tokens, and its changes to a live site ask for approval in Daoco. A suggested new page is made from its idea's `startWork` (see `list_content_ideas` in `daoco-research-and-planning`).
