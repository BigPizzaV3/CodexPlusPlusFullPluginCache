---
name: automate-optimization
description: Create and manage standing AdStellar automation rules (for example pause campaigns whose 7-day CPA exceeds a threshold) and work the approval queue they produce. Use when the user says "whenever", "automatically", "every day", "set up a rule", or wants to review, approve, or reject suggested actions.
---

Use this skill for recurring optimization logic. A rule evaluates synced Meta data on a schedule and either queues suggested actions for approval ("suggest_only") or executes them itself ("auto_run"). Automations are enabled per team; if a tool says they are not enabled, tell the user to contact AdStellar and stop.

## Authoring a rule

1. Call `get_automation_rule_schema` once. It returns the exact rule shape, the valid metrics, operators, windows, scopes and action kinds, a valid example, and authoring guidance. Follow it exactly.
2. Translate the user's request into a rule: a name, "ad_account_ids" from `list_ad_accounts`, a scope (campaign, ad set within ABO or CBO, or ad), a condition tree of metric predicates (for example spend at least 50 and CPA above 40 over the last 7 days), an action (pause, resume, archive, scale budget with a percentage, or notify only), a schedule interval in minutes with the user's timezone, and an execution mode. Default to "suggest_only" unless the user explicitly asks for autonomous execution.
3. Scaling actions require a hard budget ceiling ("max_budget_cap"). Ask the user for it; never pick one yourself.
4. Optionally dry-run with `preview_automation_rule` passing the `rule` to show how many entities it evaluates and which would match right now.
5. Call `create_automation_rule` with the `rule`. The first call validates it, dry-runs it, and returns a preview and a `confirmationToken`. Show the user the rule in plain language, the current matches, and whether it will act on its own. After a yes, call again with the identical `rule` plus the token.

## Managing rules and the queue

- `list_automation_rules` shows every rule with its status. `set_automation_rule_active` with `isActive` false pauses a rule immediately; turning one on returns a `confirmationToken` first because an active rule can act on live ads.
- `list_pending_automation_actions` shows suggested actions awaiting a decision with the entity, proposed action and rule. Present them as a short table.
- `approve_automation_action` applies one suggestion to Meta and is two-step with a `confirmationToken`. `reject_automation_action` declines it with a `reason` from the schema's rejection reasons; the reason teaches the rule (for example protecting a winner from future pauses).

## Do not

- Do not create "auto_run" rules unless the user explicitly asked for autonomous execution and understands the rule will change live ads without asking.
- Do not invent metric names, windows, or action kinds; use only values returned by `get_automation_rule_schema`.
- Do not approve queued actions in bulk without listing each one and getting approval that covers the list.
