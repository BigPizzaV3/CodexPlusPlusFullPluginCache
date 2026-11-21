---
name: find-leads
description: Turn a description of who the user wants to sell to into an Onsa lead search they have approved, have it report back when leads arrive, and present the leads with the evidence behind each score. Use when the user asks Onsa to find prospects, leads, buyers, decision-makers or "people like X", or to grow an existing campaign ("5 more like these", "try Europe instead").
---

# Find leads

> These steps are for you. Talk to the user about their search and their customers, in your own words — not about this skill, its steps or its file.

A search spends the workspace's prospect allowance, so the query is agreed before it runs, and the
results are shown with what Onsa actually established about each person.

## Step 1 · New search or an existing campaign?

- "More like these", "try another region", "stop including X" → the campaign already exists: use
  `continue_campaign` with that campaign's id. A new `find_leads` would split it into a separate
  campaign with its own profile.
- `continue_campaign` steers what the campaign looks for **next**. It removes nothing: leads
  already found, and outreach already queued for them, stay. Say so when the user asks to drop
  people, and point them to the campaign in the Onsa app to remove them.
- Otherwise → a new search, Step 2.

If you do not know which campaigns exist, `list_campaigns` tells you. If the user has not used Onsa
in this conversation yet, `list_next_steps` first: it says whether a search is already running or
new searches are blocked.

## Step 2 · Restate the brief as a query, and get a yes

Write back, in one short block:

```
SEARCHING FOR
  people:     <titles, including the variants that mean the same job>
  companies:  <industry · size · geography · other observable traits>
  excluding:  <what the user ruled out>
```

Then add one line for each requirement Onsa cannot see directly on a company or a profile — for
example a budget, a tool the company uses internally, or an intent to buy. Say it will be judged
from indirect evidence, or left for the first conversation. A requirement nothing can show is a
wish, not a filter.

Ask for a yes or corrections. Skip the question only if the user already said to just run it, or
approved this same brief moments ago in the `build-icp` skill.

If the user cannot describe who they want in a sentence or two, or wants the profile worked out
from their past deals or a connected CRM, run the `build-icp` skill first.

## Step 3 · Run it

`find_leads` with the agreed query and the requested number as `limit` — an integer from 1 to 25
(default 5); for more, say so and run it at 25. `limit` is a target, not a spending cap: every lead
that lands uses allowance. Or `continue_campaign` with the steer. Both return a `jobId`
immediately and run in the background.

Read the answer before going on. A `billingWarning` goes to the user as written. A continuation
can answer without starting new work — for example when the steer only changed settings, or was
already answered — and its answer says so; do not re-send the same steer, and do not replace it
with `find_leads`.

## Step 4 · Be told, don't watch

Where the host supports MCP events, subscribe this chat to `leads_search.leads_found` and
`leads_search.finished` for the `jobId`. Only once that succeeded, tell the user the chat will hear
about the first leads and the agent's report; do not set up a periodic check. Then call
`fetch_leads` once — anything that landed before the subscription shows up there. On each event,
call `fetch_leads` with the `jobId`. A batch can still land after `finished`.

Without events, or if the subscription failed, follow `progress.note` in the `find_leads` answer
and in each `fetch_leads` answer — it says whether the next call waits for leads or when to ask
again. A job reads `pending` while it is still searching; never tell the user no leads were found
while it is pending.

## Step 5 · Present the leads with their evidence

A table: `name`, `position`, `companyName`, `score` (1–5) and what the `scoreExplanation`
establishes — "not scored yet" where either is missing. Beside it, what is **not** established:
anything the explanation or the search agent's report calls approximated, estimated or unverified,
and any contradiction between a lead's own fields (for example a `position` and a `headline` that
disagree). Onsa's reasoning stays in Onsa's words; add no fact about a person that Onsa did not
return.

Close with the `campaignUrl`, and one line on what the user can do next: grow the campaign
(`continue_campaign`), or review the people and drafts (the `review-leads` skill).

## When the search ends without leads

`leads_search.finished` with `no_leads`, or a `stalled` status, usually carries the search agent's
own answer in `agentMessage` — often a question about the brief. Relay it, and offer to re-run with
the answer folded into the query. When there is no `agentMessage`, say the search ended without
leads and without an explanation, and send the user to the `campaignUrl`.
