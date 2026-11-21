---
name: campaign-diagnosis
description: Diagnose a campaign - how it is doing, why replies dropped, or how two campaigns compare. Checks reply classification first, then sending, bounces, human clicks, steps and segments, and proposes one change. Also reads experiment findings.
---

# Campaign diagnosis

This skill answers the three questions people ask most about a campaign: how is it doing, why did replies drop, and how do two campaigns compare. You read the numbers in a fixed order, prove each one is real before you lean on it, and end with one change to try and the reason for it.

This skill only reads. When the fix is a copy change, hand it to `campaign-improvement`, which asks the user before it writes anything. When it is a sending, bounce or inbox problem, give the user the numbers and say the fix is in their sending setup in Kenso, not in the copy.

Every call takes an optional `workspace_id`. Send it when the user can see more than one workspace: `list_workspaces()` lists them. Dates are ISO-8601 instants (`2026-10-01T00:00:00Z`). Rates come back as fractions from 0 to 1.

## The rules for numbers

- A reply is a person, not a message: every count here is distinct contacts. Out-of-office is not a reply.
- Never report opens. Open tracking is off for deliverability, so open numbers mean nothing.
- Put the counts next to every rate: "2.1% reply rate (21 of 1,004 contacted)". With fewer than about 100 contacted, give the counts and leave the rate out.
- Missing data is N/A, never 0. A metric that did not load is unknown, not zero.
- Clicks are human clicks. Use `clickCount` and the returned `clickRate`. `botClickCount` counts scanners and never shows interest.
- Say what the numbers show first. Then say what you think caused it, and mark that part as your read.

## Step 0 - Find the campaign and the window

1. `list_campaigns(q="Acme")` finds the campaign by name. `get_campaign(campaign_id=42)` gives its status, schedule and launch date.
2. Pick the window. The default is the last 30 days. For "why did replies drop", compare two windows of the same length: the last 14 days against the 14 days before.

If an operation this skill names is not listed for you, or a campaign the user named answers 404, stop and say: "I can't read that campaign's analytics from here. You can see it in Kenso at https://app.ken.so/<workspace id>/campaigns/<id>." A 404 means the campaign is not in this workspace or the read is not on for you. Do not retry it, and do not tell the user the campaign does not exist.

## Step 1 - Check reply classification first

The interested count is only as good as the classifier behind it, and the classifier has failed silently before: replies arrived for weeks without being classified, so interested counts read near zero while real interest sat in the inbox. Check it before you blame copy or targeting.

`get_reply_breakdown(from_time="2026-10-01T00:00:00Z", to_time="2026-10-27T23:59:59Z", campaign_id=42, by_segment=True)`

`totalCount` is the people who replied and `interestedCount` the positive ones. `counts` splits them by class (`interested`, `not_interested`, `out_of_office`, `automated`, `unclassified` and others), and each person counts once.

- Replies are `totalCount` minus the `out_of_office` count.
- Classification is behind when `unclassified` holds a large share of the replies, or when a campaign that had interested replies shows none for several days while replies keep arriving. Spot-check with `list_inbox_threads(campaign_id=42, interest="unclassified", limit=20)` and read a few.
- If classification is behind, stop the diagnosis there. Tell the user the positive-reply numbers for this window are not reliable, give the reply count, and say the Kenso team needs to look at classification. Do not explain a drop the classifier made.

Done when you know whether the interested count can be trusted.

## Step 2 - Did it send?

`get_campaign_performance(from_time="2026-10-01T00:00:00Z", to_time="2026-10-27T23:59:59Z", campaign_id=42, group_by="day")`

Read `sentCount` and `contactedCount` by day. Fewer sends come before fewer replies, so a reply drop that follows a send drop is a sending question, not a copy question.

- Status: a paused, completed or errored campaign stops sending. `get_campaign(campaign_id=42)` says which.
- Holds: `list_auto_pauses()` lists the inboxes, domains and campaigns Kenso paused on its own, with the reason and the rate that tripped it. `isActive` true means the hold still blocks sending.
- Leads: `get_campaign_weekly_report(campaign_id=42)` returns `next`, which says how many leads are left and when the last one starts. A campaign with no leads left stops sending.

Report any sending, hold or inbox problem with its numbers, and say the fix is in the sending setup in Kenso.

## Step 3 - Bounces

The same performance read carries `bounceCount`, `bounceRate` and `bounceBreakdown` (hard, soft and the reasons). A bounce rate near 3%, or near 100 bounces, is a list or domain problem that hurts every later send. Raise it with the user before you judge the copy. `get_deliverability(from_time="2026-10-01T00:00:00Z", to_time="2026-10-27T23:59:59Z", group_by="domain")` shows whether one domain carries the bounces.

## Step 4 - Human clicks

Clicks show that people read past the first lines. Many clicks with few replies points at the call to action or the page behind the link. No clicks on a campaign with links points at the opening or at tracking. Step rows carry raw click volume but no unique clickers, so compare clicks between steps only as volume.

## Step 5 - Steps and segments

- By step: the same performance call with `group_by="step"` shows which email gets the replies. A step with no replies after a few hundred sends is a candidate for `campaign-improvement`.
- By segment: `group_by="segment"`, and the classification read's `bySegment`, show which audience answers. Different segments are different people, so a gap between segments is a targeting finding, not a copy finding.
- By variant: there is no per-variant read here. The diagnosis works without it.

## Step 6 - What already changed

Read what was tried before you suggest anything.

- The weekly report's `changed` lists the newest sequence versions, paused or resumed variants and added segments, with their dates.

Never suggest an angle the record shows already failed. If the drop lines up with a change, name the change and its date, and keep it a read, not a proof: the leads and the weeks changed too.

## Step 7 - One change, with a hypothesis

Propose one change: what to change, the numbers behind it, and the result that would prove it right ("If the step 2 rewrite works, step 2 gets at least 4 interested replies in the next 600 sends, against 1 in the last 600"). One change at a time, so the next read can credit it.

| Finding | Hand to |
|---|---|
| A weak step, opening or call to action | `campaign-improvement` |
| Sends, bounces, holds, inbox health | the user, in the sending setup in Kenso |
| One audience answers and another does not | a new segment for that audience, after the user's yes |

A pause, volume or schedule change on a client campaign needs a yes that names that client. Report the order you checked, each finding with its numbers, the change, and when to read the result again.

## Compare two campaigns

When the user names two or three campaigns:

- Read each one with `get_campaign_performance(from_time="2026-10-01T00:00:00Z", to_time="2026-10-27T23:59:59Z", campaign_id=12)` over the same window and set them side by side. Their leads differ, so any gap is a hunch: say which campaign got more interested replies per person contacted, with the counts, and never say one won.

## Answer cards

Three tools show the diagnosis as a card with charts, or as text where cards are not on for the workspace. Each takes a `window` (`{"preset": "last_30_days"}`, or `from` and `to` dates):

- How one campaign is doing: `show_campaign_health` with `campaign_id`.
- Why one campaign's replies dropped: `explain_reply_drop` with `campaign_id`.
- Two or three campaigns side by side: `compare_campaigns` with `campaign_ids`, the first one the baseline.

Each also returns a text summary. Quote its figures as they are. Run Step 1 anyway: the card does not check classification for you.

## Experiments

Experiment findings are not readable here. When the user asks about tests, findings, a winning version or making a version the default, say those are in Kenso, and never call a version a winner from the reads above.

## What this skill cannot do yet

- Test significance between two arms. There is no significance helper, so never call one arm a winner.
- Count held meetings. Meetings booked are on the performance rows. Meetings held are not tracked yet.
- Split steps by variant.
