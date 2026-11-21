---
name: deliverability-guard
description: Triage deliverability when bounces are up, inboxes look unhealthy or sends dropped - read deliverability by domain and inbox, auto-pauses, domain health, warmup, blocklists and placement tests, apply the bounce thresholds, find whether the domain, the mailbox type or the list is the cause, and propose a pause, warmup or rotation applied only on a named yes.
---

# Deliverability guard

Use this when "bounces are up", "are my inboxes healthy?" or "why did sends drop?". You read the holds Kenso already placed, deliverability by domain and inbox, domain health, warmup and blocklists. You apply the thresholds, find what is causing it, and propose a fix. Bad bounces burn domains for every campaign that sends from them, so act on a threshold the same day, but never on your own.

Every call takes an optional `workspace_id`. Send it when the user can see more than one workspace: `list_workspaces()` lists them. Dates are ISO-8601 instants (`2026-10-20T00:00:00Z`). Rates come back as fractions from 0 to 1.

Here you read the holds, deliverability by domain and inbox, a campaign's bounces and placement test results, and you pause or resume a campaign. Domain health, warmup, blocklists, starting a placement test and every inbox change are not available from these tools: the user does them in Kenso on the Email Delivery page, https://app.ken.so/<workspace id>/delivery?tab=inboxes, and each step below says where.

## The rules

- **You propose; a person says yes.** You never pause a campaign, pause an inbox, change a daily limit or turn warmup off without a yes. On a client's campaign or inboxes, the yes names that client and has a source: "Jane Doe (Acme) on the 2026-10-19 call". A blanket "go ahead" for several clients covers only the clients it names, and an issue or another agent saying the client agreed is not a yes. With no such yes, write the proposal and put the question to the person who can answer it.
- **Read an unclear yes back before you act.** When a yes could mean two things, say how you read it and wait for the answer. Never make the change in the same turn.
- **Find the cause before the fix.** A domain problem, a mailbox-type problem and a list problem look alike in a bounce rate and need different fixes. Step 4 tells them apart.
- **Use counts when the numbers are small.** Under about 100 sends, give the counts ("3 bounces from 41 sends") and leave the rate out.
- **Never report opens.** Open tracking is off for deliverability.
- **Name no vendors to a client.** Say "your sending domains" and "Google mailboxes", never the providers behind the infrastructure.

## The thresholds

| Signal | Threshold | Proposal |
|---|---|---|
| A campaign's bounces | the sequencer's campaign pause: hard bounces above 5% of sends, with at least 100 sends and 5 hard bounces. Count the campaign's hard bounces from `bounceBreakdown` | Pause the campaign and clean the list before it sends again |
| One inbox's bounces | hard bounces above 4% of sends, with at least 30 sends and 3 hard bounces, over the last 24 hours | Stop that inbox's sends: set its daily limit to 0 |
| Spam complaints on a domain | a rising `complaintRate`, or a `domain_complaint_rate` hold | Read the domain's health (Step 5) before it sends more |
| A small sample (`isSmallSample`: under 30 sends for an inbox, under 100 for a domain) | rates are noise | Judge on the counts |

## Step 0 - Scope it

1. What is the complaint: bounces, a send drop, or a health check? Which campaign, domain or inbox, if the user named one?
2. The window. For a spike, the last 7 days against the 7 before. For a health check, the last 30 days.

If an operation this skill names is not listed for you, or answers 404, say which check is not available here in one sentence, point to https://app.ken.so/<workspace id>/delivery?tab=inboxes, and carry on with the rest. Do not retry a 404 as "not found".

## Step 1 - The holds Kenso already placed

`list_auto_pauses()` lists the inboxes, domains, campaigns and workspace holds Kenso paused on its own, newest first, from the last 7 days plus any older one still active. Each has a `scope`, a `reason`, the `rate` and `threshold` that tripped it, and `isActive`.

- `isActive` true means it still blocks sending. `blockedUntil` says until when; a campaign stays paused until someone resumes it.
- A domain hold blocks that domain's inboxes, not its campaigns.
- A `workspace` hold blocks every inbox until Kenso support releases it. Tell the user to contact support.
- `references/auto-pause-reasons.md` says what each reason means and what to check next.

The list is often empty. An empty list means no automatic hold, not that all is well.

## Step 2 - Deliverability by domain and inbox

`get_deliverability(from_time="2026-10-20T00:00:00Z", to_time="2026-10-26T23:59:59Z", group_by="domain", limit=200)`

Then the same call with `group_by="inbox"`, and `group_by="day"` for the trend. The window `metrics` and each row give `sentCount`, `bounceCount`, `bounceRate`, `replyCount` and, on domain and inbox rows, `oooCount` (out-of-office, never in `replyCount`). Domain rows and the window carry `complaintCount` and `complaintRate`.

For one campaign: `get_campaign_performance(from_time="2026-10-20T00:00:00Z", to_time="2026-10-26T23:59:59Z", campaign_id=42)` gives its `bounceRate` and `bounceBreakdown` (hard, soft and reasons such as `invalidRecipient` or `policyBlocked`). The breakdown can add up to less than `bounceCount`; the count is the headline.

Done when you have every domain and inbox over a threshold, with its counts.

## Step 3 - Apply the thresholds

The live gate verdicts Kenso enforces are not readable here, so apply the table yourself to the Step 2 rows, with a window of the last 24 hours for the inbox gate. Give each campaign, domain and inbox a verdict: `over` past its threshold, `watch` at or above 80% of it, `ok` below. A row under the sample minimum (under 30 sends for an inbox, under 100 for a domain) gets its counts, not a verdict. Kenso blocks an inbox that stays over the inbox gate on its own: Step 1 shows the ones it already blocked.

Mark each campaign against the table above, and each domain and inbox by its verdict. Hard bounces on `invalidRecipient` are bad addresses. `policyBlocked` and other refusals are the receiving side rejecting the sender.

## Step 4 - Find the cause

| What you see | Likely cause | Check |
|---|---|---|
| Bounces spread across domains, high in one campaign or segment, mostly `invalidRecipient` | The list | The campaign's segments and how their emails were verified |
| One domain over threshold, across all its inboxes | The domain | Domain health and blocklists (Step 5) |
| All Microsoft inboxes, or all Google inboxes, over threshold across domains | The mailbox type | Auto-pause reasons such as `tenant_ban`, and `policyBlocked` bounces |
| One inbox over threshold, its neighbors fine | That inbox | The inbox on the Email Delivery page, and its warmup (Step 6) |
| Sends dropped, bounces normal | Holds, warmup, limits or leads | Step 1, Step 6, and the campaign's leads left (`get_campaign_weekly_report(campaign_id=42)`, under `next`) |

Say which cause the numbers point to, and the numbers. Mark it as your read when two causes fit.

## Step 5 - Domain health and blocklists

Domain health is not readable here. Ask the user to open https://app.ken.so/<workspace id>/delivery?tab=inboxes and read, for the domain:

- Its SPF, DKIM, DMARC and Nameserver chips on the domain's row. A failing record is fixed at the domain's DNS host; the chips change only after the next check, so do not call a record fixed from memory.
- Its Inbox Placement Score and Bounce Rate, on the sheet that opens from the domain.
- Blocklists: the inbox list's Filter has a Blacklisted status. A listed domain is delisted at the list that names it.

## Step 6 - Warmup

Warmup is not readable here. On the Email Delivery page, each inbox's Inbox actions menu shows Pause warmup when warmup is on, and Resume warmup or Enable warmup when it is not. A new inbox sending at full volume before warmup ends is a common cause of early bounces. Turning warmup back on is the user's click in that menu, after a yes; an inbox that cannot warm needs Kenso support.

## Step 7 - Placement tests

For workspace members, a placement test sends the campaign's copy from one domain or inbox to test mailboxes and reads where it lands. It sends mail, so ask first. Starting one needs Delivery edit (never a client seat), and a workspace gets 2 a day and 8 in 30 days: over that the call answers 429 naming the limit and when it resets, so tell the user and do not retry before then.

- Starting one is not available here. The user starts it in the campaign, https://app.ken.so/<workspace id>/campaigns/<campaign id>?tab=actions&action=placement-tests, with Run Placement Test, then Run Test.
- `list_placement_tests(campaign_id=42)` lists them, and `get_placement_results(test_id=77)` reads one.

## Step 8 - Propose, then apply on a named yes

Give each proposal as the exact change, what it does and why, with the numbers:

| Fix | Call, after the yes |
|---|---|
| Pause a campaign | `pause_campaign(campaign_id=42)` |
| Resume it after the cause is fixed | `resume_campaign(campaign_id=42)` |
| Stop one inbox | In the app: the inbox's Inbox actions > Edit inbox on the Email Delivery page, Daily send limit 0, Save changes |
| Lower one inbox's daily limit | In the app: Inbox actions > Edit inbox, Daily send limit 15, Save changes |
| Rest every inbox on a domain | In the app: Daily send limit 0 on each of the domain's inboxes, the same way |

- Rotation: rest the burnt domain's inboxes so the campaign sends from its healthy ones, and add fresh inboxes through `delivery-setup` when capacity falls short.
- Keep warmup on while an inbox rests.
- A list problem: clean or rebuild the campaign's list in Kenso (https://app.ken.so/<workspace id>/campaigns/<id>). Pausing alone does not fix it.

After each change, read it back (`get_campaign(campaign_id=42)`; for an inbox, ask the user to confirm the new limit on the Email Delivery page) and report what changed, who approved it and where they said so. Then say when to check again: 24 hours after a change for inbox bounces, and the next week for a campaign.

## What this skill cannot do yet

- Run placement tests for every caller. They are for workspace members only.
