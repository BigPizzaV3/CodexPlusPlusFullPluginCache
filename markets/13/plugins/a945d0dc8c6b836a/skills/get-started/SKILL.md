---
name: get-started
description: Load when the user sets up Espresso AI, connects their Espresso account, asks what Espresso can do here, or wants a tour of their current Snowflake or Databricks optimization settings.
---

# Get started with Espresso AI

Help the user confirm their Espresso account is connected, pick the account
they want to work on, and see what Espresso is doing for it today.

## Workflow

1. Call `list_accounts`. If it fails with an auth error, ask the user to
   reconnect Espresso and sign in with the email they use for the Espresso
   dashboard. If it returns no accounts, tell them their organization has no
   Espresso accounts yet and to contact support@espresso.ai.
2. Show the accounts as a short list (name and product). If there is more than
   one, ask which to look at; otherwise use the only one. Every other tool takes
   its `customer` slug.
3. Summarize the current state for that account in a few lines:
   - Snowflake: `get_snowflake_warehouse_agent_settings` and
     `get_snowflake_scheduler_settings`. Say whether each agent is on and how
     many warehouses it manages.
   - Databricks: `get_databricks_settings`, `get_databricks_scheduler_settings`
     and `get_databricks_spark_jobs_settings`. Say whether each agent is on and
     how many warehouses or jobs it manages.
4. Call `get_settings_history` with `since: "-7d"` and mention the latest few
   changes, if any.
5. Close with two or three things they can ask next, such as turning an agent
   on for a warehouse, changing cluster bounds, or reviewing recent changes.

## Changing settings

Every write tool previews by default. Show the user the diff from the
`dry_run: true` call, and apply with `dry_run: false` and the returned
`versions` as `expected_versions` only after they confirm. Always pass a short
`notes` describing why; it is recorded in the settings history. Never change
settings during setup unless the user asks.
