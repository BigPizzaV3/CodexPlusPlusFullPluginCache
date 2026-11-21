---
name: pipeline-review
description: Review the deal pipeline - open opportunities by stage and age, stale deals flagged against real activity, one next action per deal, stage and next-step updates on the user's yes, and a weekly sales update.
---

# Pipeline review

Deals rarely die on a call. They die afterwards, quietly: no next step written down, a close date that passed weeks ago, a nurture pile nobody has touched in two months. This skill reads the opportunities in Kenso, flags the deals that are stuck against what actually happened on each account, proposes one next action per deal, and writes the week's update.

It ends with a short pipeline report, a list of next actions with owners, and each deal change the user approved applied.

Deals have no tool in this app: you cannot read or change them here. The user gives you the open deals from Kenso, you read the meetings and email around each one, flag the stuck deals, propose the next actions and write the update, and the user makes each approved change on the deal in Kenso.

## The rules

- **Deals change only on the user's yes.** Propose every stage, amount, close date, owner or next-step change; the user makes the ones they approve in Kenso. A field a person set stays as it is unless they say otherwise.
- **Never invent an amount, a close date, a probability or a reason.** Use what the deal, its account and its meetings say. Missing data is reported as missing (N/A), never as 0.
- **Moving a deal to won can block the account.** A won deal marks its account a customer and stops outreach to its domains, so its contacts stop getting campaign email (the won stage on https://app.ken.so/<workspace id>/demo/settings/pipeline says so). Say that before the user moves a deal to a won stage.
- **Stages belong to the workspace.** Never propose renaming, reordering, adding or removing one. Propose a change to a stage's win probability only when the user asks for that exact change.
- **Replies are distinct contacts.** Out-of-office is not a reply. Never report opens.
- **A booked meeting is not a held meeting.** Held meetings are not tracked yet: never report bookings as meetings held.

Every tool here takes `workspace_id`. Send it on every call when the user can see more than one workspace (`list_workspaces()` lists them).

## Step 0 - Check what you can use

| Part | Tools | Needs |
|---|---|---|
| Deals, stages, settings | none here: the user reads them in Kenso | Opportunities on |
| Meetings on an account | `list_meetings()` | full access and Meetings on |
| Email threads | `list_inbox_threads()` | every member |
| CRM sync health | `list_crm_connections()`, `get_crm_sync_status()` | every member |
| Top-of-funnel numbers (optional) | `get_campaign_performance()`, `get_reply_breakdown()` | every member |

Opportunities is in beta. If https://app.ken.so/<workspace id>/demo/accounts/opportunities does not open for the user, stop: say "Opportunities is not on for this workspace yet". Any other part that is missing: skip it, say which, and carry on.

Then check whether the CRM is feeding deals in:

`list_crm_connections()`, then for each live connection `get_crm_sync_status(connection_id=3)`.

If `status` is paused, `lastError` is set, `needsAttentionCount` is above 0 or `queueDepth` is large, say first that deal data may be behind, with the numbers, and point the user to `https://app.ken.so/<workspace id>/settings/integrations/crm`. There is no "sync now" from here.

## Step 1 - Read the pipeline

Deals have no tool here, so the user brings them. Ask them to open https://app.ken.so/<workspace id>/demo/accounts/opportunities and give you every open deal in scope: its name, account, stage, when it entered that stage, amount, close date, next step and owner. A pasted table or a list is fine. Ask for the currency and each stage's win probability too (https://app.ken.so/<workspace id>/demo/settings/pipeline shows the stages); without the probabilities, leave the weighted amount out.

When the user asks about one rep, stage, campaign or company, take only those deals.

Done when you hold every open deal in scope. A field the user did not give is N/A, never 0 or a guess.

## Step 2 - Flag the stuck deals

Check each open deal against these signals. `references/stale-signals.md` in this skill's folder has the details and the default thresholds. Tell the user the thresholds you used and change them when they say so.

| Signal | How you see it |
|---|---|
| Too long in its stage | days since `stageChangedAt` above the stage's threshold |
| Close date passed | `closeDate` before today on an open deal |
| No next step | `nextStep` empty |
| No recent activity | nothing on the deal or its account in the last 14 days: no meeting, no email either way and nothing the user reports from the account's page |
| Stage does not match what happened | for example a meeting-booked stage with no meeting on the calendar, or a meeting-held stage whose meeting was cancelled |
| Late stage with no amount | `amount` empty at proposal or later |

Read activity for the deals that need it, largest amount first, at most 25 per pass (tell the user if you stopped there):

- `list_meetings(account_id=101, from_time="2026-09-27T00:00:00Z")`: meetings past and upcoming. The account id is the number in the account's page address in Kenso (`/demo/accounts/<account id>`); ask the user for it when you do not have it.
- `list_inbox_threads(q="acme.com", limit=10)`: email with the account, with `direction` showing who wrote last.

Touches and the account's timeline have no tool here: ask the user to check the account's page for touches planned, waiting or sent, and for its recent activity.

A deal is stale when it trips two or more signals, or the close date passed. One signal is a watch item.

## Step 3 - One next action per deal

For each flagged deal, propose one action with an owner and a date:

- **Follow up**: the contact wrote last and nobody answered. Hand the thread to the reply-handling skill.
- **Book the next meeting**: interest but no meeting. Draft the ask with real times (the meeting-prep-and-followup skill does this).
- **Fix the record**: a passed close date, a missing next step, a stage that does not match. Propose the new values.
- **Write the summary**: the deal has activity but no summary or next step. Write a one-line summary and next step from what the meetings and threads say, for the user to paste into the deal's Summary and Next step.
- **Close it**: no activity for a long time and no answer to the last two touches. Propose moving it to a lost stage, or to nurture if the workspace has one, with the reason.

Never draft or send outreach from this skill. Name the skill that does it.

## Step 4 - Apply what the user approves

Show the proposed changes as a list: the deal, the field, the current value, the new value and why. Deals have no tool here, so the user applies each change they approve in Kenso:

1. Open https://app.ken.so/<workspace id>/demo/accounts/opportunities and click the deal. Its sheet shows Stage, Amount, Close date, Next step, Owner and Probability ("Open full page" gives it a page of its own).
2. Change the field to the approved value. A stage change goes through the Stage picker; a lost stage asks for a Reason, written from what the contact said.
3. Tell you when it is done, so the update you write matches the pipeline.

- Stage names differ per workspace: use the stages the user's pipeline shows (https://app.ken.so/<workspace id>/demo/settings/pipeline lists them).
- A field a person set stays as it is unless the user says otherwise.
- Moving a deal to another account, or changing a stage's win probability, only on the user's explicit request.

A deal that should not exist goes to a lost stage with a reason, on the user's yes.

## Step 5 - The weekly update

Write it in this order. `references/weekly-update.md` in this skill's folder has the layout.

1. **Pipeline now**: open deals, total and weighted amount, by stage, from the deals the user gave you. Amounts in the workspace currency.
2. **This week**: deals opened, moved, won and lost this week, with amounts and lost reasons, as the user reports them. When they did not give a date, write N/A rather than a guess.
3. **Stuck**: the stale deals, with their signals and next actions.
4. **Next actions**: the list from Step 3, by owner.
5. **Top of funnel** (optional): sent and replies for the workspace from `get_campaign_performance(from_time="2026-10-24", to_time="2026-10-30")`, and interested replies from `get_reply_breakdown(from_time="2026-10-24", to_time="2026-10-30")`, each for the week and the week before. Meetings booked is N/A here. Never report opens.

There is no stage history yet. "Moved this week" counts only a deal's latest stage change, so a deal that moved twice shows once: say so in the update.

If replies came in but `interested` is 0, the replies may not be classified yet. Say that, and do not report a 0% positive rate.

## What this skill cannot do yet

- No stage history and no stale-deal or forecast report: Step 2 rebuilds staleness from activity each time.
- No deal delete, and no stage edits beyond win probabilities.
- No "sync now" for the CRM: `sync-get` is status only.
- No reading or changing deals, stages or pipeline settings from this app: the user reads and changes them in Kenso.
- Held meetings are not tracked yet.

`references/stale-signals.md` holds the thresholds and how to read each signal. `references/weekly-update.md` holds the update layout and the metric definitions. Both are in this skill's folder.
