---
name: il-pipeline
description: "This skill should be used when an InvestorLists founder asks where they stand: \"where am I with <firm>\", \"what's due\", \"what did I send\", \"what changed\", \"show my batches\", \"mark <firm> passed\", \"they booked a meeting\", \"push <firm> a week\". It is the agent's memory: it reads the notes the other skills wrote. Light by default (what the agent did itself); fuller tracking only if the founder opted in. Never reads mail unless connected and asked in that run; never adds reminders; never sends anything.\n"
metadata:
  version: "0.1.3"
  author: InvestorLists.vc
---

# Raise Pipeline (the agent's memory)

Where every investor stands, from the notes. Quiet by default.

## Source of truth

Firm notes in the `[IL]` grammar written by Shortlist, Brief, Path to Connect and Messages, plus the lists. Read them with `my_notes`; the latest `[IL]` line per firm wins.

## Two modes

- Light (default): the agent shows only what it knows from its own actions: batches worked, briefs done, paths chosen, messages drafted or sent and their dates, follow-ups due by the sequence dates, and database changes on list firms. It never asks the founder for status updates.
- Full (opt-in): offered once, at the end of the first Messages run: "If you tell me when an investor replies, passes or books a meeting, I can keep a fuller picture: replies to handle, who is silent, what is due. One line from you per event is enough. Want that, or keep it light?" Default stays light. In full mode the founder volunteers events or pastes replies; the agent never chases.

## On request

- "Where am I with <firm>": the firm's note lines, newest first, in three lines.
- "What's due": follow-up touches whose date has arrived or is this week, revisit dates (full mode), in five lines or fewer. "Nothing due" is a valid answer.
- "What did I send": sends from `send-log` and the notes, by firm and date.
- "What changed": from `il_status` (or `list_changes`): new database import, new news on list firms, firms removed from the database since the founder's last run. One line, then one offer: "Refresh the pool?"
- "Show my batches": one table per batch: firm, decision-maker, channel, last action and date, next action and date.
- Updates, each one `add_note` line, on the founder's word: replied (then one offer to draft the reply through il-messages), passed with the reason, not-now with a revisit date, meeting booked, second meeting, term sheet, push a week.

## Rules

- Reports only what the notes hold. Every row shows the note line it came from.
- Never reads mail unless the mailbox is connected and the founder asked in that run ("check my inbox for replies from my list"), and then only threads with list firms' domains or decision-makers.
- Never creates a schedule, a reminder or a digest. Never sends anything.
- Five lines or fewer unless the founder asks for the table.
- The portal mirrors the same statuses on the list page.
