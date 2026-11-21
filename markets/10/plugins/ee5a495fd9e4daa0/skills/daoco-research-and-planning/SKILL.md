---
name: daoco-research-and-planning
description: Ask Daoco to research audiences or competitors, plan campaigns, or review marketing performance; read how the brand's posts did and what its results show works; say what to make next; and record ideas and learnings. For a personal or business brand.
---

# Research and plan with Daoco

Read [the shared Daoco workflow](../daoco-marketing/SKILL.md) for selection, execution, retries, results, and approvals.

## Start from what Daoco already knows

These reads use no workspace tokens; answer from them before starting paid work.

- `get_results`: the brand's recent published posts by account, who made each, and, once a post has been out three days, its views, interactions, engagement rate, and a verdict against the account's usual (`above`, `usual`, `below`, or `unknown`). `channelId` keeps one account; `ideaId` reads the posts made from one idea.
- `get_brief` with a `channel`: the What's working lines for that channel, each marked measured (from the brand's own results), untested, or the person's own.
- `list_content_ideas`: pages and posts Daoco and other agents suggested, each with evidence, a score, status, and `startWork`, the request that makes it. `view: "history"` shows what was made and how it did, and `whatWorked` sums that up by format and platform. Answer "what should I post or write next" from these first. Start an idea only when the person picks it, passing its `startWork` as given (and its `ideaId` to `start_work`).
- `list_updates`: what happened lately, including milestones and What's working changes.

## Ask Daoco to research or plan

Frame the request around the decision the person wants to make. Keep any named competitors, audience, region, period, channels, budget, and success measure; do not require every field for an exploratory request. Adapt to the brand's real goals rather than assuming them. Send it through `start_work`, or `run_workflow` for one of Daoco's workflows where it is listed (a performance review, a competitor scan, an audience poll, a fresh plan of what to make next). Do not promise data from an account merely because the platform has an integration.

Read the report with `read_work`, keeping sources, periods, limitations, and the line between observed results and recommendations. Use `get_output` for a chart or report. Report unavailable data as unavailable, not zero. A plan does not authorize doing every recommendation; start production only when the person asks.

## Match evidence to the decision

- Performance reviews name their sample, the denominator for rates, and the posts behind each conclusion. Raw totals across differently sized accounts do not show which approach works.
- Audience and competitor research separates observed behavior, quoted statements, and inferred motives. A handful of examples suggests a hypothesis; it does not prove a pattern.
- Campaign plans keep the objective, offer, audience, channels, dates, and budget given. A list of channels is not a plan, and planned spend is not authorized spend.
- SEO and website work separates measured search data from page observations and hypotheses. A proposed fix is not a deployed one.

Check that each recommendation ties to evidence and names how to judge it. Keep the uncertainty of small samples. If a conclusion is unsupported, say so instead of strengthening it. One focused correction on the same thread is fine; after that, return what is supported and the gap.

## Add ideas and learnings

`add_content_ideas` adds up to 5 post ideas this app found to the brand's queue: a one-line `title`, a `subject`, and where you have them the `platforms`, an `https` `sourceUrl`, and one line of `evidence`. Repeats come back with `repeatOf` instead of being added twice. An app holds at most 25 open ideas per brand. Add ideas the person asked for, or that your role on a team is to find.

`record_learning` records a claim about what performs, such as "carousels with a face on the first slide get more saves on Instagram", in the brand's What's working as an untested line named with this app, with the `postIds` it rests on. Daoco's own measurements confirm or replace it, and it expires after 60 days otherwise. Record only a pattern that clearly held across several of the brand's own posts; never one post, a hunch, or a claim the results do not show.

For fixes on the brand's own site, use `daoco-website-improvements`. For a recurring review, use `daoco-automations`.
