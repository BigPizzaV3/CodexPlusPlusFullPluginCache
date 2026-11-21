---
name: maplith
description: Use when a question touches the company's data as Maplith maps it - which business objects exist and where they live, how records connect across systems, what is wrong in the data, or what needs doing. Maplith returns a map of the data, not the records. This skill reads the map and changes nothing.
---

# Maplith: read the company's data map

Maplith holds a map of a company's data: the business objects and their
fields, the system and file each one lives in, how they join across systems
and how far each join can be trusted, the processes and metrics, findings
(places where systems disagree) and signals (work that needs doing). It holds
the map, not the rows. This connection reads the map and changes nothing.

## How to work

1. **Orient first.** Call `get_map_overview` once at the start. It gives the
   domains, the object names as the map spells them, the counts, how fresh
   the map is and how far to trust it. Use those names in later calls rather
   than guessing. If the workspace has no map yet, tell the user to build the
   first one at app.maplith.com.
2. **Find, then open.** When you do not know a name, call `search` with a
   word or phrase, then `fetch` with the id of the most relevant result. For
   an object you can name, `get_object` gives its fields, relations and
   caveats. `get_process` and `get_metric` list the processes and metrics, or
   read one by name. `list_sources` says which systems and files the map was
   built from, and `list_automations` lists the automations registered
   against the map's objects.
3. **Questions across systems: `route`.** Pass two object names. Report the
   hops in order: the systems crossed, the join columns of each hop, its
   strength and its measured coverage. Name the weakest hop and say why (low
   coverage, not measured, or guessed). Call an untested hop untested.
4. **What is wrong: `list_findings`.** Pass status open for the open ones.
   Give each finding's evidence and Maplith's recommendation in your own
   words.
5. **What needs doing: `list_signals`, then `get_task_context`.** Ask for the
   open signals (order by urgency when the user wants the most urgent), pick
   one and pass its id as signal_id to `get_task_context`. Report what the
   signal is about, the objects and routes involved, the related findings,
   any playbook the company has for it, and what the task context says not
   to trust. `get_value_summary` counts the signals raised and acted on over
   a period.
6. **Questions about Maplith itself, or ones that span much of the map:
   `ask`.** It answers with citations. It is metered, so use the direct
   tools above for one known thing.

## Rules for the answer

- **The map, not the rows.** Maplith returns metadata: names, types, joins,
  findings and the values of metrics a company chose to track. Do not invent
  records, record counts or field values that no tool returned. When the
  user wants records, say where they live: the system and file, the key to
  look them up by, and how far to trust each hop on the way. The records are
  read in the company's own systems, with the company's own access.
- **Personal data.** Fields that hold personal data are marked as such. Say
  that a field holds personal data and where it lives. Do not ask the user
  for personal values, and do not repeat one that appears in evidence. When
  the user asks for personal values, such as customers' email addresses or
  phone numbers to export, call no tool: explain that Maplith returns
  metadata, not records, and cannot export contact details.
  Maplith tries to mask personal identifiers in descriptions and evidence, as
  a best effort.
- **Say what is uncertain.** Read the caveats on joins, metrics and findings
  before citing them. A weak, unmeasured or guessed join is an estimate, and
  the answer says which.
- **Read only.** These tools do not change the map, a finding or anything in
  the company's systems. When the user asks for a change, such as pausing a
  campaign, closing a finding or fixing a record, call no tool and do not
  claim to have done it. Explain that this connection is read-only, and say
  who makes the change and where: a person with access to the system makes
  it there, and a workspace member changes a finding's status in Maplith.
- **Credentials.** Do not ask for or reveal keys, passwords or tokens; no
  tool returns one.
- **Errors.** When a tool answers with an error, follow the next step it
  names, for example look up the names with `get_map_overview` or `search`,
  then call again.
