# Work with an existing budget

Use this path when the user asks about a saved Presuo budget or wants to act on one. First identify the intended budget when needed; never start a new-budget draft for an existing-budget request. Use the connected read and write tools that are actually available, and explain results in plain language.

## Open the editor

- Open an editor only on the user's clear request and through the authorized `budget.editor.open` handoff.
- The embedded UI consumes `handoff_url` automatically as a one-time iframe bootstrap. Never expose it as a clickable chat link; it will be consumed or expire before the user can open it.
- If a clickable fallback is useful, link `direct_url` instead. It opens the ordinary Presuo editor and may require the user's normal Presuo login.

## Find and browse items

- Choose the budget first. Use `budget.list_accessible` only to locate a budget by name; when the user is working on the current page's budget, use that budget.
- Inside the chosen budget, use `budget.find` for any section, line item or measurement the user names or describes: a code (leading zeros are ignored, so 2-1 finds 002-01), an exact label, or partial words. Do not search for the same reference with several tools.
- `resolved` is one exact match and answers a read directly. `ambiguous` lists exact candidates: show them and ask which one. `matches` are partial hits: answer from a single clear hit, naming it, or present the relevant choices; a partial hit is never a write target until the user chooses it. `none` means nothing in that budget matched; say so rather than paging through the budget.
- Use `budget.browse` when the user asks what the budget or a section contains: sections by default, one section's items, or all items. A page is not the whole budget: state the total and whether more remains, and fetch further pages only as the question needs. Never page through an entire large budget to answer a lookup.
- Show the returned display references (code and name), never internal IDs.

## Answer questions

- Use the found or browsed records to answer the user's question. Keep the response focused and cite the relevant section/item or measurement details from returned data. Do not fabricate missing records or totals.
- Use activity history for “what changed,” recent-work, or audit questions. Summarize who did what and when based on the returned activity.
- If the user's wording could refer to multiple budgets or records, present the matching choices and ask which one they mean.

## Approvals

- For pending or resolved approvals across a budget, call `approvals.list` with the budget. Counts cover the whole budget; item lists and history are pages, so say when more remain.
- When the user picks an item from partial or ambiguous `budget.find` results, read that item's activity or approvals before commenting on it or requesting or closing an approval.
- Every comment, approval request and approval closure needs an `idempotency_key`. Generate a new random key (for example a UUID) right after the user confirms each action, and reuse it only to retry that same call. Do not build keys from the item, date or text, and never reuse a key for another action.
- For “request approval,” explain what will be submitted and use the approval request action for the intended budget or workflow. Report the returned result.
- For “close/complete approval,” establish which approval they mean and what closing it will do. Always obtain explicit confirmation before closing. Never imply that a request or closure succeeded until Presuo confirms it.

## Report field quantities

- When the user reports work completed or quantities observed, clarify which line item/measurement they mean only if needed. Preserve the reported quantity, unit, and price as stated; do not invent missing values.
- Record quantities only when the user asks to report them. Find the target, then read its line item with `measurement.list_for_line_item` before every measurement write, show the proposed quantity/note change, and get explicit confirmation immediately before submitting with `measurement.report` (one or several measurements of one line item, each with its returned revision). Report the returned result. Measurement reporting records progress; it does not alter pricing or finalize the line item, and it does not change the approved baseline.
- Call `measurement.preview` with the exact write arguments first when a report replaces values, copies planned quantities, covers every measurement of a line item (`all_measurements`) or more than 25 measurements, and before clearing anything but a note. Show its counts and totals; when `full_list` is false, say the samples are partial, state the overwrite count, and confirm the rule ("copy each planned quantity") rather than a list. Write with the same arguments within 10 minutes; if Presuo reports that the measurements changed, preview again and reconfirm.
- Treat "job done" or "finished" as copying planned quantities only after that preview and an explicit yes. Use `measurement.clear` or `measurement.revert` for one measurement only after confirming exactly what is cleared or restored.
- In execution, approved scope and baseline are not ordinarily editable. Users may report quantities, add eligible out-of-scope measurements, and make eligible baseline changes only through the supported workflow. Do not promise an unavailable editor or unsupported change.

## Boundaries and errors

- Respect the budget's current lifecycle status and the capabilities exposed by the tools. If the requested action is unavailable in that status, explain the limitation and offer the supported next step when known.
- Do not expose internal IDs, permission details, or hidden records. On access errors, report that access was unavailable without guessing another budget or identity.
- Do not claim an action completed unless the tool confirms it. If a write's outcome is uncertain, follow the tool's idempotency/recovery behavior; do not repeat it as a new operation to bypass uncertainty.
