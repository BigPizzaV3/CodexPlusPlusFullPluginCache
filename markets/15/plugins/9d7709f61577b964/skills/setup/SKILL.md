---
name: setup
description: Set up Sken.io after installation. Confirms the connected account and its check allowance, makes sure detected changes have somewhere to be reported, and creates the first monitor from a page the user names.
---

# Set up Sken.io

Sken.io watches web pages and reports when they change. Work through the steps below in order, in a single pass. Report what you find after each step and ask before creating anything.

## 1. Confirm the connected account

Call `sken_account_info`.

Report the plan, the remaining points and how many monitors already exist. Points are spent by every check a monitor runs and by one-off scans, so the balance decides what check interval the account can afford. A monitor checked every 30 minutes runs roughly 1,440 checks a month.

If the call fails with an authorisation error, the Sken.io account is not connected. Say so and stop. An account is created at https://sken.io.

If monitors already exist, this is a returning user. Skip step 3 unless they ask for a new monitor, and offer `sken_list_changes` instead.

## 2. Make sure alerts have somewhere to go

Call `sken_list_integrations`.

A monitor with no notification channel still detects changes, but nothing is sent anywhere. The user has to come back and ask. Say this plainly rather than implying an alert will arrive.

If no channel exists, call `sken_list_integration_types` and offer the available ones, which include e-mail, Slack, Discord, Google Chat, webhooks and Zapier. Create the one the user picks with `sken_create_integration`, then confirm it works with `sken_test_integration` and report the result of that test send.

If the user does not want notifications, continue without them and note that changes will only be visible when they ask.

## 3. Create the first monitor

Ask which page to watch and what matters on it.

The second part is the one users forget. Sken.io can watch a described area, so "the price of the main product" or "the list of open roles" is a valid answer and is usually better than watching the whole page, which reports every cookie banner and timestamp as a change.

Then agree a check interval against the point balance from step 1, and create the monitor with `sken_create_job`, attaching the channel from step 2.

Confirm what was created: the URL, the watched area, the interval, the monitor id and where its alerts go.

## 4. Say what happens next

Tell the user they can ask what changed at any time, and that each detected change keeps a before and after screenshot with the changed area highlighted, so the answer describes the page rather than only reporting that something moved.
