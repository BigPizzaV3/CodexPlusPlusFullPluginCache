---
name: get-started
description: First steps with Onsa right after connecting it — reads what the Onsa workspace already holds, asks for the two lines a search needs if it holds nothing, starts the first lead search and has it report back to this chat when leads arrive. Use right after install, or when the user says "get started with Onsa", "what can Onsa do", "set up Onsa", or asks for leads without any brief.
---

# Get started with Onsa

> These steps are for you. Talk to the user about their search and their customers, in your own words — not about this skill, its steps or its file.

Onsa finds real B2B prospects — people with LinkedIn profiles — scores each one 1–5 against an
ideal-customer profile with the reasoning written out, and keeps every search as a campaign.

## Step 1 · Read the workspace before asking anything

Call `list_next_steps` with no arguments and follow what it says. The usual cases:

- **A search is already running** → say so, give its `jobId`, and go to Step 4 for that job. Do
  not start a second search.
- **New searches are blocked** (trial ended, allowance used up, no active subscription) → relay
  that blocker in the tool's own words. Do not start a search, and do not offer any purchase or
  upgrade. What the workspace already holds stays readable: offer to review its campaigns, leads
  and replies (the `review-leads` skill) if it has any.
- **The workspace has campaigns** → name the most useful one or two in a line each and ask
  whether to continue one of them or start a new search.
- **The workspace is new** → Step 2.

If the answer says it could not tell whether a search is running, say that, and ask before
starting one.

## Step 2 · The two lines a search needs

Ask in one message:

> 1. Who do you want to reach? (the role, the kind of company, size, geography)
> 2. Who should Onsa never include? (segments, geographies, company types — "none" is fine)

Add one line to that message: *"Not sure yet? I can work it out with you from your past deals —
including from your CRM, if one is connected here."* If the user takes that offer or answers
vaguely ("SMBs", "anyone who needs sales"), run the `build-icp` skill. When it comes back with an
approved profile and the user chose to search now, continue at Step 3 with that profile as the
brief — it is already approved, so do not read it back again.

Use the user's own words. Do not invent an audience, and do not fill it in from what their company
seems to sell: a search spends the workspace's prospect allowance, and a guessed brief spends it on
the wrong people. If a brief the user has not yet approved is already in this conversation, read it
back in one line and get a yes before using it.

## Step 3 · Start the search

Call `find_leads` with the brief as `query` and the number of people asked for as `limit` — an
integer from 1 to 25 (default 5); for more, say so and run it at 25. `limit` is a target, not a
spending cap: every lead that lands uses allowance. It returns a `jobId` at once; the search itself
runs in the background, first leads usually within about 5 minutes.

## Step 4 · Have the search report back

Where the host supports MCP events, subscribe this chat to both events for the `jobId`:

- `leads_search.leads_found` — each batch of leads as it lands
- `leads_search.finished` — the agent posted its report (`leads_delivered`) or ended without
  leads (`no_leads`)

Only once the subscription succeeded, tell the user the chat will be told when the first leads are
ready and when the agent reports. Then call `fetch_leads` once with the `jobId`: anything that
landed before the subscription shows up there. Events replace polling and any periodic scheduled
check.

When an event arrives, call `fetch_leads` with the `jobId` and show the leads (Step 5). A batch can
still land after `finished`; it arrives as another `leads_found`.

Where the host has no events, or the subscription failed, follow `progress.note` in each
`find_leads` / `fetch_leads` answer: it says whether the next call waits for leads or when to ask
again. Never tell the user no leads were found while the job reads `pending`.

## Step 5 · Show the leads honestly

For each lead: `name`, `position`, `companyName`, and the 1–5 `score` with its `scoreExplanation`
where Onsa returned them — say "not scored yet" rather than inventing one. Keep Onsa's words for the
reasoning. Where the explanation or the search agent's report says something was approximated or
not verified, say so next to that lead rather than presenting it as fact. Never add facts about a
person that Onsa did not return.

End with the `campaignUrl` so the user can see the campaign in Onsa.

## Outreach

Connecting LinkedIn and setting up a campaign's outreach happen once, in the Onsa web app at the
`campaignUrl`; Onsa then writes drafts for the campaign's leads. Those drafts can be reviewed and
rewritten here, and a single approved message can be queued with `send_outreach` — the
`review-leads` skill covers how. Do not offer to send anything during first steps.
