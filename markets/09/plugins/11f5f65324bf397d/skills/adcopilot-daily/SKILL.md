---
name: adcopilot-daily
description: The AdCopilot morning check on a Google Ads account — yesterday against the 7-day average, this month's budget pacing, the searches that cost money and brought nothing, ads Google has disapproved or limited, and what changed in the last 24 hours. The check only reads, with "All clear" or "Needs a look" first and the one fix worth making last; a change is made only after the customer says yes to it. Use when the user asks for the morning check, the daily check or daily check-in on their ads, or for what happened yesterday or overnight in their Google Ads account; when a prompt begins "AdCopilot morning check, read-only" or a timed or automated task started the conversation; when they ask how to get the check every morning; or when they answer the yes/no question a finished morning check ended on.
---

# AdCopilot daily

One job: the morning check on one Google Ads account, through the AdCopilot connector at `https://mcp.adcopilot.cloud/mcp`. Work out which of these this is before anything else:

- **A person asked for the check** and is here to read it. Everything under "The check".
- **Nobody is here.** The prompt begins "AdCopilot morning check, read-only", or a timed or automated task started this conversation, and nobody answers until it is over. Everything under "The check", with the parts marked "nobody is here" applying.
- **They want the check to arrive on its own.** "Getting the check every morning".
- **They are answering the yes/no question a finished check ended on.** "After the check", at the end.

## The check

1. Call `get_org_context` first, with no `source`. Its `next_step` and `playbook` describe the account, not this request: do this request as written here. If `next_step` asks you to offer a check-in, a schedule or a summary, leave that out; this report carries no offers.
2. Read only. Call no tool that changes anything: nothing that creates, adds, updates, sets, pauses, links, attaches, enables or submits, in Google Ads, Analytics, Tag Manager or Search Console. A finding that names the exact call that fixes it is reported, never run. When nobody is here, do not call `save_org_context` either.
3. Ask nothing before the report. If something is unknown (which account, a read that was refused, a product to re-add, the day's reads used up) say so in one line and carry on with the rest; when the day's look-ups are used up, that line is the server's own line about the limit, word for word. When nobody is here, never stop for an answer and never end on a request for one other than the report's last question, which the run does not wait for.
4. Put nothing in the report but the reads, the server's line about the limit when it refused one, and that one question: no offer to schedule anything, no extra summary, no pointer to anything else.
5. A result may end with `related_reads`. When a person is here, run the ones that bear on a finding, at most three, never repeat a read you hold, and offer rather than chase the ones those bring back. They are reads only. When nobody is here, skip them: the five reads below are the run, and nobody is there to choose among more. Do not run one, and do not mention that it was there.
6. A finding that says "if X" is not a step until you have checked X. Either make the read it names and say what you found, or carry the condition into your own sentence. Never turn it into an instruction. Unless the read it names is one of the five below, carry the condition.

If Google Ads is not connected or cannot be read, say exactly that in one line, with what `get_org_context` reports about it, and read nothing more. A report built on guesses is worse than none, and a number you did not read is a number you may not state.

**The account** is the one the instructions name. If they name none: the account AdCopilot's own check-in reads (`latest_check_in.account`, or `routine.daily.customer_id`); else the only enabled account `get_org_context` reports that is not a manager account (`manager` true: a manager account has no campaigns of its own, and Google refuses its figures); else the first such one. If only manager accounts are enabled, say so in one line and read nothing more. Say which account, by the name Google Ads shows, right after the first line.

**Five reads, in this order.** When the instructions list their own, theirs win.

1. **Yesterday against the 7-day average** — spend, clicks, conversions and cost per conversion: `search` on `campaign` with `segments.date` and the metrics, `start_date` eight days ago and `end_date` yesterday, in the account's time zone; yesterday against the average of the seven days before it. A raw `search` returns cost in millionths (`metrics.cost_micros`): divide by 1,000,000 once, name the currency, and never print a micros number as money.
2. **This month's pacing** — `budget_pacing`: on track, over or under, and any campaign limited by budget.
3. **Searches that cost money and brought nothing** — `analyze_search_terms` with `days: 7`: the five costliest by name, with their cost (the result's "Costliest search terms with no conversion" list, when it has one). The wrong ones are candidates for negative keywords (words you tell Google never to match); say that in a few words the first time they appear.
4. **Ads Google stopped** — `search` on `ad_group_ad` with `ad_group_ad.policy_summary.approval_status`: any ad disapproved or limited, with Google's stated reason.
5. **What changed** — `search` on `change_event` with `start_date`, `end_date` and a `limit`: changes in the last 24 hours, and who made them. A quiet list does not by itself rule out a change: when yesterday moved and nothing shows, say that.

A run is about six or seven reads. Make every read the run lists. If the server refuses a read because the day's look-ups are used up, say which reads ran and which did not, answer only from the ones that ran, then give the server's own line about the limit, word for word, once however many reads it refused, and do not retry in a loop.

**The report.**

- First line, alone: **All clear** or **Needs a look**.
- Then each read in a sentence or two of plain words: money in the account's currency as the tools display it, Google's names for things, no field names, no account numbers, nothing pasted as the server returned it. A read with nothing in it is one line ("No changes in the last 24 hours.").
- Last: the single most valuable fix, as one yes/no question the customer answers when they read this. It is the only question in the report. Ask about the change itself, in one clause: not a check to make first, and not a change that hangs on what a check finds. When nobody is here, the run does not wait for the answer.

## Getting the check every morning

AdCopilot emails its own daily check-in. `get_org_context` reports it: when `routine.daily.status` is `in_app` and `routine.runner` is not `paused`, it is on. It reads the account, changes nothing, and arrives without anyone opening a conversation. Say that. It is paused and resumed on the Routine card on AdCopilot's Home page (the address is in `app_urls.home`), not from this conversation, and you cannot switch it from here. When it is paused or not reported, say what `get_org_context` shows and that the same card is where it is resumed. Do not promise that it will arrive.

If they ask for a timer inside their own assistant: AdCopilot has no tool to create or check one, and you cannot promise their assistant can run connector tools with nobody there to approve them. Say that plainly. If they set one up themselves and it asks for the AdCopilot morning check, it is a run with nobody there and follows the rules above; they should run it once by hand and see it finish before they rely on it. Asking for the AdCopilot morning check in a conversation gives the same report whenever they want it.

## After the check

The check is over and the person, now here, answers the yes/no question it ended on. Nothing inside the check counts as a yes (not the instructions, not the report's own question), and the report may be hours old by now.

So when they reply yes, first re-read the one thing the fix touches (the searches it would block, the campaign's budget and its pacing, the ad's status) and restate the exact change with its money both ways, from that read. Apply it only on their yes to that restated change; a change is proposed and waits for that yes, every time. Then, as `adcopilot-review` does after a yes: read back only what the change's own result does not show, and call nothing live until a read says so; say exactly what changed and how to undo it; record it with `save_org_context` as a decision, in the customer's own framing (a fix they did not say yes to is recorded, if at all, as proposed and not applied, never as approved); then propose the next fix the same way, biggest money first. Negatives go on with `add_negative_keywords` at PHRASE match using the search as typed, unless a broader word is plainly safe; read them back before saying they are live, and say a negative can be taken back out through AdCopilot. Campaigns, ad groups, ads and keywords are paused, never removed. If the re-read shows the problem has already gone, say so and change nothing.
