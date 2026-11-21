---
name: "setup"
description: "Set up SolarSENS. Use right after the plugin is installed, or when the user asks to set up or start with SolarSENS. Checks sign-in and Plant access, then suggests where to start. Read-only. The user can skip it."
---

# Set up SolarSENS

Use only the tools this server lists. Read-only.

Setup is a short conversation, not a form. Write a few lines in each message and ask one question at a time. Do not use headings. Do not name these steps. If the user asks for a check or says skip, stop setup and do their request with the matching Skill.

## Procedure

1. Sign in. If no SolarSENS tools are listed, SolarSENS is not connected. Tell the user how to sign in, then stop. Claude Code: run /mcp and sign in to SolarSENS. Codex CLI: run codex mcp login solarsens. If Codex does not find that server, run codex mcp list and use the SolarSENS name it shows. ChatGPT or another app: sign in to SolarSENS from the plugin settings, then start a new chat.
2. Account. The app manages connected-account labels and account selection. Do not call get_profile during setup. If the user wants another account, tell them to add or select it in the SolarSENS plugin settings, then start a new chat.
3. Plants. Call list_accessible_plants with no arguments. If it fails with a sign-in error, ask the user to finish sign-in in the app, then call it again. If the response says the account is not linked to an active SolarSENS user, tell the user to contact their AVA admin to link the account, then stop. If no Plants are returned, tell the user that the account has no Plant access and to contact their AVA admin, then stop.
4. Welcome. In one message: SolarSENS reads live and daily data for solar Plants, such as yield, performance ratio, devices, strings, and alarms. It cannot change equipment, alarms, or work orders. Give the number of Plants. Name at most three Plants. Ask what the user does with these Plants, with short examples: O&M for a site, asset owner, performance analyst.
5. Where to start. Suggest the three Skills below that best fit the answer. Give one line for each: the Skill title and a first question that uses a returned Plant name. Run nothing yet. Ask which one to start with, or what else they want to check.

## Skills to suggest

- Plant performance review (plant-performance-review): Use when the daily PR of one Plant on one day looks low.
- String fault review (string-fault-review): Use when you think a string on one Plant gives less power than its peers.
- Daily portfolio check (daily-portfolio-check): Use at the start of the day to find the Plants that need attention.
- Alarm triage (alarm-triage): Use when a Plant has active alarms and you want to know what the device data shows.
- Missing value check (missing-value-check): Use when a Plant value is blank, zero, old, or missing for one day.

## Limits

Setup stores nothing. Do not save the user's answer outside this chat. Do not show Plant IDs.
