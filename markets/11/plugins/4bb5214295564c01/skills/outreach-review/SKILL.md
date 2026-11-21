---
name: outreach-review
description: Report how outreach and the Oneprofile workspace are doing. Covers replies and positive replies by sequence, which step, sender or mailbox is underperforming, bounces and deliverability, what is waiting on the team, and credits spent and left, with the next actions worth taking. Use when the user asks how campaigns or sequences are going, for a daily or weekly summary or standup, for reply rates or which email works best, why replies dropped, how many credits they have used, or what to do next.
---

# Outreach review

Give a short, honest status of the user's outreach and workspace, built only from what the tools report, and finish with the few actions worth taking. Everything in this skill only reads, so it is free. Make no changes unless the user asks for them afterwards.

## Reaching the tools

`get_sequence` and `read_inbox` are listed by name. The analytics tools are listed by `list_sequence_tools`, credit balance and spend by `list_billing_tools`, the approval queue by `list_task_tools` and mailboxes by `list_mailbox_tools`. Reach them through `run_read_tool`, passing `{"name": "<tool>", "arguments": {...}}`. Read exact arguments with `describe_tool` (up to 8 names per call).

## 1. Pick the window

Use the user's window. Otherwise use the last week for a daily or weekly check-in, and all time for "how is it going overall". The analytics tools take `period` (`all`, `week` or `month`), or `since` and `until` as `YYYY-MM-DD` for any other range. Use the same window everywhere in one report.

## 2. Gather

Make these reads, in parallel where you can:

- `get_outreach_analytics`: the workspace's contacted, sent, replied, positive, bounced and opted out, and the leaderboard of mailboxes and LinkedIn senders, worst performer first
- `get_sequence` with no `sequence`: every sequence, with its status and anything blocking it
- `get_sequence_performance` for each live sequence: its funnel, each step's sent, replies and bounces, and where contacts stand now
- `read_inbox` with `view: "all"` and with `view: "needs_approval"`: what waits on the team
- `list_approval_queue`: messages held for approval
- `get_credit_balance` and `get_credit_spend`: what is left and what it went on

Add these when they are relevant: `list_sending_mailboxes` or `check_mailbox_activity` when bounces are high, and `list_connections` when a connected tool may be broken.

## 3. Read the replies before judging the copy

Counts say how many people replied, not why. Before calling a step or a message weak or strong, call `read_inbox` for that sequence and `read_conversation` on two or three representative replies. If no replies came back, read what was sent and say that no replies were available to judge.

## 4. Rules for the numbers

- **There are no open or click rates.** Oneprofile sends plain-text email without tracking. Never report, estimate or ask for them. Reply rate and positive reply rate are the measures.
- Name steps the way the product does, such as "Step 2 · Email 2", never by an email's subject line.
- Report only numbers a tool returned. If a number is missing, say so.
- A bounce rate that the tool flags as above the health threshold is the first thing to raise, because it puts the sending domain at risk.

## 5. Write the report

Lead with what matters, keep it short, and link each sequence with the link the tools return.

> **Outreach, last 7 days**
> 412 contacted · 31 replied (7.5%) · 9 positive (2.2%) · 6 bounced (1.5%)
>
> **By sequence**
> - **UK fintech RevOps**: 18 replies, 7 positive. Step 1 · Opener earns most replies.
> - **Agency founders**: 2 replies from 140. Step 2 has none so far.
>
> **Needs attention**
> - 3 replies wait on you in the inbox, and 2 AI drafts wait for approval
> - Mailbox maya@outreach.example.com bounces 6.8%, above the health threshold
>
> **Credits**: [N] left. [M] spent this week, mostly on work emails.
>
> **Suggested next steps**
> 1. Pause maya@outreach.example.com and check its health
> 2. Rewrite the Agency founders opener: the replies say it reads as generic
> 3. Answer the 3 waiting replies (I can draft them)

Each suggestion should name what you would do. For optimisation advice beyond the obvious, call `search_playbooks` and `read_playbook` first, and say when a suggestion comes from them.

## Next steps

- Acting on the replies: the `triage-replies` skill
- Changing a sequence's copy, steps or senders: the `launch-a-sequence` skill
- A low credit balance: say what is left and that credits are managed under Credits and billing in Oneprofile's settings. This app can't buy credits or change plans, so don't offer to.
