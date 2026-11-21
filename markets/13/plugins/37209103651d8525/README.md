# CleverX

Use your CleverX research workspace from your AI assistant. Ask about your studies and results in plain language: "What did people say about onboarding in my latest interviews?", "Which tasks did testers struggle with?", "How many studies are live?" You can also draft a new survey, usability test or AI interview, check whether it's ready to launch, and see what it would cost.

CleverX is a user-research platform for surveys, unmoderated usability tests, AI-moderated interviews and video interviews, with a B2B participant panel. This plugin needs a CleverX account on a paid plan.

## What it can do

- **Read:** your studies, participant progress (names shortened, no contact details), survey answers, usability task results, transcripts, highlights and the AI analysis of each study.
- **Draft:** create and edit draft studies, check launch readiness and estimate the price. Editing a draft can change or remove its questions, tasks or targeting, so your assistant asks before it does.
- **Stays in CleverX:** launching studies, recruiting and contacting participants, approving responses and paying them, buying credits, and team and account settings. Nothing launches from the chat, and nobody is contacted.

## Connect

1. Install the plugin and choose **Connect**.
2. Sign in with your CleverX account (or create one).
3. Pick the workspace the assistant should see: your personal workspace or one of your teams. To switch workspace later, reconnect.

To disconnect, remove the connection in your assistant, or go to CleverX → Settings → AI tools → Connected AI tools → Disconnect. Access ends within a few minutes.

## What this plugin runs and sends

- It adds one remote connection, the CleverX server at `https://mcp.cleverx.com/mcp` (the ChatGPT package uses `https://mcp.cleverx.com/mcp/chatgpt`, where each draft edit is its own tool). Your assistant sends it your requests (for example a study id or a search term) and receives your CleverX data in reply.
- You sign in through CleverX's own sign-in page (OAuth). The plugin stores no passwords or keys.
- It includes one skill, `get-started`, with written guidance for the assistant. It runs no local programs and fetches nothing else.

## Help, privacy and terms

- Guide: https://cleverx.com/guides/use-cleverx-in-claude-and-chatgpt/
- Help: https://help.cleverx.com
- Privacy policy: https://cleverx.com/privacy-policy
- Terms: https://cleverx.com/terms
- Support: support@cleverx.com

## License

Apache License 2.0, see `LICENSE`. The license doesn't grant rights to the CleverX name or logo (section 6); don't use them in a way that suggests endorsement.
