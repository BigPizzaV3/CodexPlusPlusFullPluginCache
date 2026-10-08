---
name: clio-manage
description: Work with the firm's own records in Clio Manage — a matter's status, parties, notes and custom fields; documents and folders; tasks and what is due; the calendar; time entries, expenses and bills; logged calls and emails; and searching inside document and note bodies. Use it whenever the answer is in the firm's records rather than in the law, and for creating or updating those records. Clio Manage only: Grow leads and Operate matters are different products, and legal research belongs with clio-research.
---

# Clio Manage

Vincent reaches into the firm's live Clio Manage records: it can read them, and it
can create, update and delete them.

There is no Clio tool on this server. It is the same `start_research` /
`continue_conversation` conversation as everything else; what selects Clio work is
that the question is about **the firm's own records** rather than about the law.
Carry the user's own specifics — the matter, the client, the dates — into it.

## What is Clio work rather than research

The dividing line is where the answer lives. "What did the court hold in *Smith*" is
research. "What is the status of the Smith matter, and what is due on it next week"
is Clio: nothing in the law library knows it.

| The user asks about | Reaches |
| --- | --- |
| A matter's status, stage, parties, notes, custom fields; contacts and companies | matters and contacts |
| Documents, folders, templates, text snippets | documents |
| What is due, outstanding or done; task templates; docketing | tasks |
| What is scheduled — hearings, depositions, appointments, reminders | calendar |
| Time entries, timers, expenses, bills, payments, balances | time & billing |
| Logged calls and emails, message history with a client | communications |
| Users, groups, custom field definitions, reports, webhooks | admin |
| A phrase buried *inside* a document or a note | matter content search |

The last row is the one people get wrong. Listing notes returns note **records**;
finding the sentence where the client agreed to something searches note **bodies**.
Ask for the one you mean — "search the matter's documents for…" reads bodies, "list
the notes on the matter" reads records.

## Phrase the question so it lands

Name the matter the way the user named it, and say which product: a firm may have
the same client in Manage and in Grow. If the user gives a matter number, pass it
through verbatim rather than describing the matter.

Ask for a date window when one is implied — "what is due" almost always means this
week or this month, and an unbounded task list is not an answer.

## Writing to the record stops for approval

Creating, updating and deleting are gated per resource: the run parks with a
`tool_approval` interruption naming what Vincent is about to write. Resolve it as
every approval is resolved here — **put it to the user in your own words and carry
back their answer**. Never approve a write to the firm's records on the assumption
that an earlier instruction covered it; a matter closed or a time entry deleted is
not something an apology undoes.

`list_approval_keys` shows what can be pre-granted through
`start_research(initial_approval_keys=[...])`. Pre-grant only what the user actually
asked to allow, and read the labels back to them when you do.

Two writes worth double-checking before you relay them, because they are easy to ask
for casually and hard to reverse: deleting anything, and changing a matter's status
or stage.

## When the tools are not there

Clio Manage tools appear only for a session opened with **Clio Work credentials**,
on a firm licensed for Manage, with the integration enabled. The token decides it,
not the person: the same user arriving with a vLex token has no Clio tools at all.

Without them Vincent answers from legal research instead, which reads like a thin
answer rather than a missing connection. If the reply covers doctrine when firm
records were asked for, or Vincent says it cannot see the matter, say the session
may not have Clio access and let the user confirm — do not retry, and do not present
the research fallback as the Clio answer.

A session with no Clio credential at all does not reach Vincent: the connection is
established by signing in to Vincent on the web through Clio, and every tool here
answers with that until it is. If that is what you see, relay it — sign in there,
then try again — rather than reporting it as a Vincent failure.

## What the records are, and are not

A Clio record is what the firm wrote down, not what happened. An empty task list
means nothing was logged, which is not the same as nothing being due, and a note is
one person's account. Say which you are reporting when it matters.

Report counts and dates as the records gave them. Do not total hours, fees or
balances yourself from a list of entries — ask Vincent for the figure, so it comes
from the record rather than from arithmetic in the reply.
