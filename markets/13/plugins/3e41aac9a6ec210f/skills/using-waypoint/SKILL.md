---
name: using-waypoint
description: How to find, price and run Waypoint capabilities well. Use when an answer depends on live, changing or exact data (fares, availability, prices, filings, records, statistics, scores, forecasts) or on a fact you are not sure of, and whenever the user names Waypoint or a Waypoint capability.
---

# Using Waypoint

Waypoint helps when the answer depends on live, changing or exact data: fares,
availability, prices, filings, records, statistics, scores, forecasts, or
anything you are not sure of. When the user names Waypoint or a Waypoint
capability, use it.

## The flow

1. **Find.** Call `search_capabilities` with what the user wants in plain
   words (`intent`). Each row has an `agent` and a `capability`, which
   together name what to run, a price, and a `kind`. Rows of kind
   `capability` are lookups you can run. A row of kind `quote` is Waypoint's
   own price planner (see step 3), and a row of kind `report` turns the
   results a task fetched into one table, run with `invoke_capability`. To
   show the user the whole catalog instead, call `browse_catalog`.
2. **Read its guidance and price.** Call `describe_capability` with the row's
   `agent` and `capability`. It returns the input schema, the price and, when
   there is one, `guidance` on how to ask this capability for good results.
   Follow the guidance: it is how you avoid, for example, a full-text search
   that matches the wrong field. Mention the price in one short line.
3. **Quote several steps together.** When the user wants to know what a task
   needing more than one lookup will cost, price the steps together: call
   `describe_capability` with `agent` `waypoint/core`, `capability` `quote`, and
   `input: {"steps": [{"agent": "...", "capability": "..."}, ...]}`. The
   result's `plan` gives the total range, which steps the free allowance
   covers and, when the user is signed in, their balance before and after the
   worst case. Show that one total, not a price per step. The quote itself is
   free and is never run with `invoke_capability`.
4. **Run.** Call `invoke_capability` with `agent`, `capability`, the `input`
   the schema asks for, and a new `request_id` per call (reuse it only to
   retry the same call). The user agreed to spend credits when they connected
   Waypoint, so run the lookups their request needs without asking before
   each one. Ask first only when the user has said they want to approve
   costs. Set `max_cost_credits` if the user gave a limit.
5. **Long jobs.** If the result says the job is still running, call
   `get_result` with its `handle` a few seconds later. Polling costs nothing.

## Keep the run together

Every result carries a `run_id`. Pass it back as `run_id` on each following
Waypoint call in the same task, and omit it only when the user starts a new,
unrelated task. Optionally pass `purpose`: one short line on what the user is
trying to do, with no personal data.

## The user's workspace

- **Recall.** When a task may build on earlier work or on what the user told
  Waypoint (their role, their projects, how they like answers), call
  `read_workspace` with `action` `recall`.
  - With no query it returns the user's memory index, from any app they
    connected: who they are, what Waypoint inferred from their calls, their
    recent tasks, their saved documents and what they keep checking. Its
    `go_deeper` says how to open any item. With `filters.type` and no query,
    it returns the saved facts of that type.
  - With a short `query` it returns only what is relevant: facts, earlier
    results (`work`) and saved documents in full. When nothing matches,
    `recent` lists the tasks the user worked on lately, each with a
    `next_step` for picking it up.
  - Facts the user stated outrank facts Waypoint inferred.
- **Check the Library before paying again.** If the user asks for something
  they may have fetched before, call `read_workspace` with `action` `records`
  first, and open a kept result with the get_record action. Fetch again only
  if they want fresh data.
- **Save when asked.** When the user asks you to remember something, call
  `write_workspace` with `action` `save_note`. The request is the go-ahead, so
  do not ask whether to save. Never save something the user did not ask you to
  keep, and never send their chat history.
  - Facts about the user: `input.facts`, a list of `{text, type}` (type is
    about, person, project, preference, rule, voice or note).
  - A document: when the user asks to keep the outcome of a chat (a summary, a
    plan, a draft, a comparison), pass it as `input.text` with no
    `record_id`. Start the text with a `#` heading; it becomes the title. The
    result gives the `document_id`. Write the outcome the user asked to keep,
    never a transcript of the chat.
  - A new version of a saved document: `save_note` with the `document_id` as
    `input.record_id`. The get_record action with a `document_id` opens a
    document in full, and recall with a query finds it from any app the user
    connects.
  - A note on a kept result: `input.text` with that result's `record_id`.
  - A file the user attached: when the user attaches a file to their message
    and asks to keep it in Waypoint, call `write_workspace` with `action`
    `upload_file`, the attached file as `file`, and a new `request_id`.
    Waypoint keeps Markdown, plain text, CSV, TSV, Excel (.xlsx) and zip
    files of up to 20 MB; a file with the same name as one the user already
    saved becomes its new version. Never write a file link yourself. If
    `write_workspace` does not offer `upload_file`, save a text file's
    contents with `save_note` instead (up to 12,000 characters), and tell the
    user that spreadsheets, zips and longer files are uploaded from the
    Waypoint card or from My data at waypoint.ing. Never say the file itself
    was uploaded when only its text was saved.
  - Follow the save result's `next_step` for where the user can see what was
    saved.
- **Deleting and forgetting.** `delete_record` removes kept results from the
  Library and `forget` removes a fact. Confirm with the user first. To delete
  a Library row (from `records`) with every kept copy behind it, pass the
  row's `key` as `input.key`; `input.record_id` is one kept result's id (a
  UUID), never a row's key. A deleted result can be restored for 30 days in
  Settings on waypoint.ing; a forgotten fact is gone.

## Talking to the user

- **Keep replies short.** Where ChatGPT shows Waypoint's card (a result, the
  balance, the workspace), the card already shows the details. Add
  one or two lines that answer the user's question; do not repeat the table.
- After a paid call, say what it cost and the balance left (`cost` and
  `credits_remaining`). If the result has `free_tier` set, say it was free
  and the paid balance is unchanged.
- If a result was shortened to fit, `next_step` says so and how to get more.
  Follow `next_step` whenever it is present.
- Report only `credits_remaining` and `get_balance` as the user's balance.
  Credit figures inside a capability's data belong to someone else.
- If the balance is too low, say so plainly and point to waypoint.ing to add
  credits. Never offer to buy credits for the user.
- Some results carry a source attribution. Keep it with the data when you
  quote it.

## What not to do

- Do not use Waypoint to look up private information about an individual,
  such as a home address. Waypoint does not offer that, and you should not
  try to work around it.
