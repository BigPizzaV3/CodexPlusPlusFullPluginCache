# Orvo

Connect your AI assistant to Orvo to search people, read notes and relationship intelligence, and update records with your permission.

This package uses the Agent Plugins manifest with OpenAI listing and OAuth metadata. Upload its ZIP to the OpenAI Plugins portal after completing review preparation. It is intended for supported ChatGPT and Codex surfaces.

## Connect

Install the plugin, then sign in with Orvo in the browser. Choose **Read only** or **Read and make changes** on Orvo's consent screen. Read only is selected by default. The package contains no account credentials or API keys.

The hosted endpoint is https://www.getorvo.com/api/mcp. Orvo provides its tool schemas and instructions at connection time. There are no bundled skills, fixed workflows, commands, hooks or local executables, and no package-level tool allowlist. The assistant can combine all tools available to the user's grant with its other connected services.

## What you can do

Search people and raw notes; read relationship summaries, personality and stakeholder intelligence; filter the network; retrieve actions, opportunities, reconnect suggestions and birthdays. With write permission, update people, notes, tags, groups, actions, opportunities and reporting lines, or request a summary refresh when Orvo AI is enabled. Access to shared records follows Orvo's permissions.

Examples, not prescribed workflows:

- Find people whose notes mention a conference and explain the context.
- Read someone's notes and existing intelligence, then offer your own analysis.
- Save a new note, update a person's role and create a follow-up action.

Orvo does not expose synced email or calendar events, send messages, manage billing, or permanently erase records through MCP. Calendar and email operations require separate tools connected to the assistant. An Orvo action is not a calendar event.

## Account and data

Free to install. An active Orvo web account with a 14-day trial or a paid plan is required. Mobile-only plans are not eligible. Payments happen through Orvo; this plugin has no checkout. Your assistant provider may have its own access requirements.

Data retrieved from Orvo is processed by the connected assistant provider under that provider's terms and your account settings. Orvo's built-in AI switches are separate from an external assistant's access. To revoke access, open **Orvo Settings > Integrations** and disconnect the assistant. Reconnect to change read/write consent.

## Help

- [Setup, troubleshooting and support contact](https://www.getorvo.com/ai-assistants)
- [Privacy](https://www.getorvo.com/privacy)
- [Terms](https://www.getorvo.com/termCondition)
- Support: office@getorvo.com

Published as Orvo, operated by Sorin Constantin Ciornei. This thin integration package is MIT licensed; the hosted Orvo service and trademarks are separate.
