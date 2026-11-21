---
name: hypd-get-started
description: Welcome users who are new to Google Tag Manager by HYPD or ask how to get started, show the getting started steps and lead them to a first audit of their container. Use when someone has just installed it or asks what to do first; a concrete Tag Manager question goes straight to that task instead.
---

# Get started with Google Tag Manager by HYPD

Google Tag Manager by HYPD reads the user's connected Tag Manager containers: workspaces, tags, triggers, variables, versions and what is live. With the user's approval it also drafts and applies changes.

## Show the steps

Call `hypd_show_getting_started`. It returns the user's own steps: connect Tag Manager and select a container, audit the live container, then add the user's other platforms. A step the user has finished comes back marked done.

- Where the client renders MCP Apps, the steps appear as a widget with a button each. A click sends that step's prompt as the user's next message or opens the HYPD app. The user can already see every step, so one short sentence pointing to them is enough, and a step runs when the user clicks it.
- Elsewhere, list the steps with their links and prompts.
- If the tool is not available, `gtm_list_containers` shows which containers are connected.

## When the user already knows what they want

If the user names a concrete task, such as a tag that does not fire, a consent mode check or a comparison of two versions, start on that task instead of showing the steps. Questions about HYPD itself, such as connecting accounts or privacy, are answered from `hypd_search_help`, citing the article.
