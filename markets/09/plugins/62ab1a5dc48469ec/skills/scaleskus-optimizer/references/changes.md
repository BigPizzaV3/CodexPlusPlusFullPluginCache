# Changes: how anything reaches the Amazon account

No ScaleSKUs tool writes to Amazon directly. Every change goes through ScaleSKUs' tasks pipeline and is recorded in the account's audit log. Nothing is changed unless the user asks.

## Two steps, two separate go-aheads

1. **Queue**, only for the items the user picked. After a `run_workflow` plan, "apply 1, 3", "queue these" or "do it" means queue. Call `apply_plan` with the account's `profile_id`, the plan's `plan_ref` and the chosen `items`; set `all=true` only when the user said all, and if it is unclear which items the user means, ask. For items that didn't come from a plan, call `apply_plan` with `actions` (up to 25 of `add_negative`, `harvest_keyword`, `adjust_bid`, `adjust_budget`, `pause_entity`, `update_placement`, `adjust_ad_group_bid`, `create_keyword`), or call the single write tool with its default `mode="task"`. Queued tasks change nothing on Amazon. Report what was queued (task ids and what each one changes) and what was skipped, with the reason.
2. **Apply live**, only when the user explicitly asks for the queued changes to go live now. First restate exactly what will change (each entity, its current value and its new value) and get a clear yes. Then call `execute_tasks` with those task ids. Alternatively the user can approve the tasks in ScaleSKUs under Tasks.

A single write tool called with `mode="execute"` is the same live change and needs the same explicit go-ahead. Never apply live because a plan "looks good", because the user approved a different set of items earlier, or on your own initiative. An approval covers the items it names, once.

## Presenting a plan for approval

- One table: `#, move, ASIN, keyword/target/campaign, current → proposed, estimated impact, confidence, reversible`.
- Offer three explicit choices: all, a group ("negatives only"), or specific numbers. Don't read blanket approval into "looks good".
- For negate and harvest items, show the fit evidence you judged, and hold back items that fail it, saying which and why.

## Order of changes

Negatives, then bid decreases, then bid increases, then budget changes, then pauses. Shape which searches the ads show for before re-bidding, limit spend before extending it, and pause last.

## What ScaleSKUs enforces

- Live changes require two-factor verification on the user's ScaleSKUs login. If a response says verification is missing, the change stays queued: tell the user to verify in ScaleSKUs or approve under Tasks, and don't retry.
- A per-account daily limit on applied changes applies. Anything beyond it stays queued for approval.
- A workflow plan can be applied for 7 days. If `apply_plan` reports a plan as expired or missing, re-run the workflow for fresh numbers.
- There is no dry run on live accounts: a live change is live. Use `get_change_task` to inspect a queued task (proposed action, the checks made, recent history of the same entity) before running it, and to verify what happened afterwards.

## Automations and schedules

`create_automation_rule`, `create_strategy` and `create_dayparting_schedule` create switched-off drafts. Enabling one (`set_automation_state`, `set_dayparting_state`) lets it change the account on a schedule, so it needs the user's explicit yes to that exact rule or schedule. Where `preview_automation` is available, show its sample of changes before asking. Changing a running rule needs the same explicit yes.

## When something fails or is refused

- Never retry a failed change automatically, and never route around a refusal with another tool. Report the error and its likely cause, and ask.
- If write tools aren't available on this connection, give the plan as a checklist the user can apply in ScaleSKUs or in Amazon Ads, and never say that anything was queued.
- Items the user rejects stay out. Don't propose them again in the same conversation unless the data has changed.

## Checks before recommending any change

- Don't scale a product flagged low on stock or unhealthy: the fix is stock or the listing, not spend.
- Don't undo a deliberate recent change (`get_optimization_history`) without saying why the reversal is warranted.
- If the user asks to skip ScaleSKUs and "just change it on Amazon", explain that ScaleSKUs applies every change through its approval and audit path, then offer to queue it, or to apply it live on their explicit go-ahead.
