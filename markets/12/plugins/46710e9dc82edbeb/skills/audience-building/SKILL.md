---
name: audience-building
description: Agree, count, save, export or change an audience of contacts with Apsis Vega. Use when the user wants to find, target or count a group of contacts by their properties, events or subscriptions, see who they are as a list or get them as a CSV or Excel file, save one as a segment, explain who a saved segment targets, or change an existing segment.
---

Apsis Vega works on the user's Apsis account. The company is Apsis, with a capital A and the rest in lower case, never in all capitals, and the product is Apsis Vega. Once the user has picked an account and a section, pass the same `account` and `section` to every later call. When a tool result asks for the user's go-ahead, say what the next call would do and wait for their answer in a new message. The user's explicit instructions take priority over this skill, and a tool's own refusals and notes always apply.

## Start from what exists

- A subscription, or a segment the account already has (`list_segments`), needs no interview. Reuse it. To know who a saved segment targets, see "Explaining a segment" below.
- For an audience built from conditions, call `describe_segment_target` first. It returns the section's attributes and events, each with its `name`, its type and the operators it allows. Match the marketer's words against those names.

## Agree the audience before building it

- Ask one question at a time, in plain, non-technical language, and wait for each answer.
- Keep it proportional: an audience with one condition needs one confirming question.
- Point out, as a choice the marketer can check, anything that quietly changes who is included:
  - "is not X" on a field that can be empty also includes people with no value at all;
  - "contains" or "starts with" catches more than the literal word;
  - an open-ended or overlapping time window widens the group.

## Describe it in plain words

- No operators, parentheses, comparison symbols, "&" or "+", in replies, option labels and headings alike. Write "and" and "or" as words.
- Phrase each condition in words: "is", "contains", "more than". Write a true or false field as a trait: "marked as VIP".
- Only mixed or nested and/or logic gets an outline, indented under "Match ALL of:", "Match at least ONE of:" or "Match NONE of:".
- Where a result carries `audienceDescription` or `audience_description`, relay it as written. It is rendered from the query itself, so it describes what was actually counted.

## Count freely

`count_profiles` saves nothing. Use it as often as refining needs, with `aql` for the conditions agreed so far or `segmentId` for an existing segment. Give the marketer the count with the plain-language description beside it. For how many people are subscribed to one subscription, `count_subscribed` is the count.

## Getting the people in an audience

- When the marketer wants the people themselves rather than a number, `export_profiles` takes the same `aql` or `segmentId` a count takes, with the `section` the audience is on.
- List or file: `as: "list"` shows up to 200 people here, for looking at them or following a few up. `as: "file"` is a CSV or Excel file of everyone, for a spreadsheet, work elsewhere or bringing changes back in later. Above 200 people the list's `followUp` offers the file.
- Ask what the people are for before choosing columns, then pass as `attributes` only the ones that answer it, from `describe_segment_target`. Email, first name and last name are always included.
- A list's `followUp` is one question for the marketer: relay it as written and wait for the answer. A list's `matches` is each person's number of matching events, such as a form's submissions, and it is only there when the audience's events are one condition or several joined by or, with nothing excluded.

- Say before the call that it can take up to a minute. A `still-processing` answer, for a list or a file, means calling again with the same arguments and its `resumeToken`.

### As a file

- When the file is ready, relay the result's first text block as written and end the turn there. It carries the link, the count, the columns, when it was built and the personal-data and retention lines, and the link only works for 15 minutes. The marketer opens the link themselves.
- The file is personal data throughout, also once the conversation turns to analysing it.

## Saving is a separate decision

- Most requests are answered by a count, or by sending to a subscription narrowed by a segment that already exists.
- If the marketer may want the same group again, ask whether to keep it as a reusable segment or whether seeing who matches was enough. A saved segment can't be deleted, only hidden. Call `create_segment` only on a clear yes. A marketer who asked for a reusable segment has already answered.
- `set_segment_visibility` hides or unhides a segment. Hiding is reversible and never changes who it targets.

## Explaining a segment

- To say who a saved segment targets, call `describe_segment` and relay its `audienceDescription` as written. A segment's name does not say who it targets, so never answer from the name.
- When `describable` is false, say plainly that what the segment targets cannot be put into words, and give the reason in the result's note. Segments built in the product can use conditions that cannot be described. Do not guess from the name, and do not fall back to a count as if it explained the segment.

## Changing a segment

1. Call `describe_segment` first. Build the new conditions from the `conditions` it returns with the change made, never from scratch: what is sent replaces what is stored, and a condition left out is gone. When `describable` is false there are no `conditions` to build on: agree the complete new audience with the marketer as for a new one, starting from `describe_segment_target`, and say that it will replace what the segment targets now.
2. Call `edit_segment` with those conditions and no `confirm`. It saves nothing and returns a preview: what the segment targets now (`current`) and after the change (`next`), the `profileCount` of each, `changes` and a `confirmToken`.
3. Put it to the marketer in plain words: who the segment targets now, who it would target, and both sizes. Name each entry in `changes.removed` and ask whether losing it is intended. When `current.describable` is false, say that what it targets now cannot be put into words, so the edit replaces its conditions as a whole, and give its current size beside the new one.
4. Wait for the marketer's go-ahead in a new message. Then call `edit_segment` again with the same inputs, `confirm: true` and the `confirmToken`. A refusal because the segment changed since the preview means preview again, and show what it targets now.
5. A segment is re-evaluated each time it is used, so the edit also changes who any unsent or scheduled email using it will reach. Say so when such an email exists; it is allowed, not a reason to refuse.

A rename alone changes nobody's membership: one `edit_segment` call with `name`, no preview.
