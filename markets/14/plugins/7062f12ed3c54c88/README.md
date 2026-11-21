# Notii

Your Notii notes, tasks and calendar, right in the chat. Ask what you wrote about something and get answers with links to your notes. Save a conversation, a plan or meeting notes as a well-shaped note. Get a brief of your day from your calendar, tasks and daily note, and tick tasks off without leaving the chat.

## Install

- **Claude (claude.ai, the desktop app, Cowork):** Customize → Plugins → Add → Upload plugin, and choose `notii-claude-plugin.zip`. Then connect it from a chat, as below.
- **Claude Code:** `claude plugin install notii --marketplace https://app.notii.io/plugins/claude/marketplace.json`
- **ChatGPT:** add it from ChatGPT's Plugins, or as a custom MCP server with the address `https://app.notii.io/mcp`.

Notii's **Settings → Connected apps** has the downloads and these steps.

## Connect

The plugin connects to your Notii account through Notii's MCP server (`https://app.notii.io/mcp`). You sign in to Notii once and approve the app.

- **Claude:** from a chat (claude.ai, or the Claude desktop app's Chat), open **Customize → Plugins → Notii → Connectors**, select **notii** and **Add** it, then **Connect**. Sign in to Notii and **Allow**. Notii is then one of your connectors in chat, Cowork and Claude Code.
- **The desktop app's Code tab:** **Connect** there signs in only Claude Code on that computer, through an open Code session (it stays greyed out until one is open). The plugin's list still says **Not added**, because Notii isn't on your account's connectors, and chat and Cowork can't use it. To add it to your account, connect from a chat on claude.ai as above.
- **Claude Code in a terminal:** run `/mcp`, choose notii and authenticate.

It acts with your access: anything you can open in Notii, it can open. Disconnect it any time in Notii under **Settings → Connected apps**.

## Skills

- **notii**: how to work in your Notii (which tool for what, your time zone, links to notes, asking before deleting or sharing).
- **capture**: save this conversation, a decision, meeting notes or to-dos as a clear note.
- **today**: today's schedule, tasks due and overdue, reminders and your daily note.
- **find**: answer a question from your notes, citing the notes it comes from.

Results such as searches, task lists, the calendar and saved notes show as Notii cards where the app supports them; you can tick tasks off right in the card.

## Help

Notii's help is in the app under **Help**, and **Settings → Connected apps** shows the apps connected to your account.
