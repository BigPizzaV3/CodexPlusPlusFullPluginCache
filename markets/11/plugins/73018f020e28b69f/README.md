# QualifyBase for ChatGPT and Codex

Qualify leads with AI automations. Version 0.3.1 pairs the QualifyBase connector with eight workflows for onboarding, Instagram setup, agent setup, prompt editing, lead review, conversation and campaign review, appointments, and weekly customer insights.

## Get started

1. Enable the plugin in ChatGPT, then connect QualifyBase from its plugin page.
2. Sign in to QualifyBase as an administrator of the workspace you want to use. Review the permissions on the consent page before approving.
3. Ask ChatGPT a question or try one of the workflows below. A QualifyBase account and a configured workspace are required; available data depends on your connected channels, calendars, and account configuration.

| Workflow | Example request |
| --- | --- |
| `account-setup` | Help me set up my QualifyBase workspace. |
| `instagram-setup` | How do I connect Instagram to my agent? |
| `agent-setup` | Help me configure a receptionist agent. |
| `prompt-editing` | Review my current agent prompt and make its tone friendlier. |
| `lead-review` | Which leads need attention, and why? |
| `conversation-review` | Summarize this lead's conversations and calls. |
| `appointments` | Find an available appointment tomorrow. |
| `weekly-insights` | What did my leads struggle with last week? |

You can also describe your request naturally. Setup workflows guide you through the dashboard. The plugin does not connect Instagram or other integrations, create agents, send messages, start calls, or launch campaigns.

## Prompt editing

Agent prompt reading and writing are separate optional permissions. Existing connections retain their original 19 tools. Approving prompt reads exposes 22 tools, including `list_agents`, `get_agent_prompt`, and `preview_agent_prompt`. Approving both prompt permissions exposes 23 tools, including `apply_agent_prompt`, when safe saving is enabled by QualifyBase. These permissions apply to the connected workspace. If the tools are absent, reconnect and review the requested permissions; you can still ask ChatGPT to draft changes for the dashboard.

ChatGPT reads the current prompt, previews exact replacements or additions, and shows you the proposed change. It saves only after you explicitly approve that preview. A changed revision, ambiguous replacement, or altered preview is rejected. A verified save updates the text and voice prompt, backs up the original, and preserves the greeting and other settings. Test the affected behavior in a fresh Playground session before resuming live activity.

Direct saves require an administrator to enable safe editing in the agent's Playground → Instructions. The agent must already be paused, use supported private voice access, have no assigned inbound phone number, and have no outstanding voice credentials or sessions. A browser credential can remain valid for 15 minutes. Unsupported configurations stay in the dashboard workflow. ChatGPT does not pause agents or change routes, authentication, billing, or integrations to make a save eligible.

If a save returns an uncertain or pending result, ChatGPT reports it as unconfirmed and provides the operation ID for dashboard repair. It cannot bypass that block with a new request. Repair restores the original configuration on an isolated private voice target and leaves the agent paused; it does not save the interrupted edit. A recovered agent needs a new read, preview, and approval to apply that edit.

For dashboard drafts, compare the current text with the draft's original before pasting. A difference requires refreshing the draft. Keep the greeting unchanged, pause before saving, and test a fresh session afterward.

## Customer insights

Weekly insights use accessible chat messages and stored call transcripts to identify observed objections, questions, and booking barriers. ChatGPT states the date range, timezone, sources, and coverage. Counts from lead analytics describe leads created in that period, not necessarily every lead who spoke during it.

Conversation discovery is capped at 100 threads, individual message fetches at 200 messages, and call lists at 200 calls without pagination. A report that reaches these limits is explicitly partial. For a complete workspace reporting view, open [AI Reporting](https://www.qualifybase.com/assistant), available to workspace administrators. The plugin does not manufacture reasons from qualification scores or claim missing transcripts were reviewed.

## Permissions and data

- **Read workspace data:** leads, qualification insights, conversations, calls, campaigns, calendars, and appointments.
- **Lead and appointment updates:** optional permission for changes the user requests. Booking changes can affect a connected external calendar.
- **Agent prompt reading:** separate optional `qualifybase.prompts.read` permission for reading prompts and previewing edits.
- **Agent prompt saving:** separate optional `qualifybase.prompts.write` permission, requiring prompt reads as well, for explicitly approved guarded saves.

The connector URL is `https://www.qualifybase.com/api/mcp`, the same URL as the QualifyBase directory connector. Use an existing QualifyBase connection where ChatGPT offers it, and review any additional requested permissions.

The plugin contains instructions, metadata, and a brand icon. It contains no passwords, API keys, executable scripts, hooks, or local MCP servers. Tool calls go to QualifyBase; results become part of the ChatGPT conversation. Read and preview tools make no requests to a voice provider. An approved save updates the eligible agent's voice prompt through QualifyBase. Disconnecting or revoking the OAuth connection removes future access. Never paste integration passwords or access tokens into chat.

## Development and support

The plugin bundle is licensed under MIT. QualifyBase service use is governed by its [Terms](https://www.qualifybase.com/terms) and [Privacy Policy](https://www.qualifybase.com/privacy). For help, use [QualifyBase Support](https://www.qualifybase.com/support).

Build the complete upload ZIP with `python3 scripts/build-qualifybase-plugin.py` from the application repository. Upload the ZIP as a new version of the existing QualifyBase plugin in OpenAI Platform. Package validation and review are separate from deploying the hosted MCP service. Test connected tools in the intended workspace before submitting.
