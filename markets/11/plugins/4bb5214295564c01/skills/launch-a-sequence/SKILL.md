---
name: launch-a-sequence
description: Turn a Oneprofile table into an email and LinkedIn outreach sequence, show the messages it will send, clear its launch checks and launch it when the user says so. Use when the user asks to write a cold email campaign, set up outreach or follow-ups to a list, build, edit or tailor a sequence, change its steps, voice or goal, pick senders, preview messages, find out what blocks a launch, or launch, pause or resume a sequence.
---

# Launch a sequence

Build a draft sequence from a table, let the user judge real messages, clear what blocks it, and launch only when the user says to. A draft sends nothing. A launch reaches real people and cannot be undone.

## Reaching the tools

`build_sequence`, `get_sequence` and `write_sequence_previews` are listed by name. Other sequence tools are listed by `list_sequence_tools`, the AI writer's tools by `list_outbound_agent_tools`, message tools by `list_message_tools` and sender tools by `list_sender_tools`. Reach them through one of three runner tools, passing `{"name": "<tool>", "arguments": {...}}`:

- `run_read_tool` for a call that only reads
- `run_change_tool` for a call that changes the workspace
- `run_send_or_remove_tool` for a call that sends to people, removes something, changes where a payout goes or loosens what waits for a person's approval. Launching, resuming and test sends go through this runner.

Read exact arguments with `describe_tool` (up to 8 names per call). When a runner refuses a call, it names the runner to use.

## 1. Read the workspace

Call `get_business_context` and `list_reference_documents` through `run_read_tool`. The sequence's writer uses them, and they answer most of what you would otherwise ask the user.

For a new sequence, or advice on cadence, openers or tone, call `search_playbooks` and then `read_playbook` on what fits (for example `oneprofile-outbound-agents`). Skip the playbooks when the user has fully specified the change they want, and make exactly that change.

## 2. Check the audience

Read the table with `get_table`. Email steps need an email column, and LinkedIn steps need a LinkedIn URL column. If many rows have no email, say how many, and offer to find them first (the `enrich-a-table` skill) or later with `find_missing_emails`.

To write to only part of a table, use a saved view (`list_table_views`) or specific rows.

## 3. Build the draft

Call `build_sequence` with:

- `name`: unique in the workspace
- `table_id`, and `view_id` when writing to only part of the table
- `intent`, plus the goal and voice the user described
- `senders`: leave it empty when the workspace has one sender, since it is assigned for you, or to choose later. List them with `list_senders`.
- `steps`: leave it empty. The sequence is then built on a library campaign tailored to this audience. Give steps only when the user specified the cadence, because what you give replaces the cadence whole.

`build_sequence` builds email steps only. To add LinkedIn steps or condition branches, or to replace the emails with LinkedIn steps, use `edit_sequence_steps` after it.

Building is free and sends nothing. Its answer says roughly what sending will cost.

## 4. Show real messages

In the same reply, call `write_sequence_previews` for a few contacts. It is free but has a daily cap. Show two or three previews as written, with each one's subject and body, so the user judges the actual writing and not a description of it.

Change what the user asks for:

- **Voice, goal or call to action**: `update_outbound_agent`. Priced, so say the price.
- **One step's instructions**: `edit_message_prompts`. Also priced.
- **One contact's message**: `pin_message_for_contact` with the new body
- **The steps themselves**: read them first with `get_sequence` or `read_sequence_steps`, then call `edit_sequence_steps` with the full list. Mark every step you keep with `keeps_step`, because a step left out is deleted.
- **A spam check on the copy**: `check_message_for_spam`

When the user wants to see a message in a real inbox, `send_test_email` sends one step, rendered for one contact, through `run_send_or_remove_tool`. With `to_address` empty it goes to the signed-in user. It costs no credits and enrols nobody.

## 5. Clear the launch checks

`get_sequence` with the sequence lists what blocks launch, such as no sender, no audience, a missing subject, or no business context. For each blocker:

- fix it with the matching tool when the user's request covers it, or
- tell the user exactly what to do, with the link the tool returned when one is needed in the app. Connecting a mailbox or a LinkedIn account happens in Oneprofile.

`find_missing_emails` and `verify_sequence_emails` are optional and priced. Offer them with their price, and run them only on a yes.

## 6. Launch only on an explicit instruction

Launch only when the user has asked for it in so many words, such as "launch it" or "start sending". Approving the draft, liking the previews or saying "looks good" is not a launch instruction. Ask.

Right before launching, say in a few lines:

- who it reaches: the number of contacts, and how many are left out and why
- who it sends as
- the steps and their timing
- when the first messages go out
- what it costs

Then call `launch_sequence` through `run_send_or_remove_tool`. Pass on the price line and the link from its answer.

- **Pause**: `pause_sequence`, through `run_change_tool`. No confirmation needed when the user asks.
- **Resume**: `resume_sequence`, through `run_send_or_remove_tool`. It sends again, so confirm first.

### Example

> **Ready to launch "UK fintech RevOps"**
> - Reaches 284 contacts. 16 are left out: 11 have no email, 5 are on your do-not-contact list
> - Sends as Maya Chen (2 mailboxes)
> - 3 emails: day 0, day 3, day 7, each written per contact
> - First emails go out today from 9:00, in each sender's own timezone
> - Up to [N] credits, from the launch check
>
> Say "launch" and I'll start it.

## Next steps

- Replies as they come in: the `triage-replies` skill
- How it is performing: the `outreach-review` skill
