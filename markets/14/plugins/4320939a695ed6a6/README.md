# Wile

Share finished work as short video updates in your Wile feed and receive the human's answers on the same thread. This Wile-maintained plugin connects to `https://api.wile.ai/mcp` using OAuth. Sign in with your existing Wile account through the host's connection flow; never paste passwords or tokens into a conversation.

## Capabilities

- `post_context` sends the selected work summary, source, optional links, and question to Wile. Rules and the daily limit determine whether a video is made.
- `get_feedback` returns new answers for a thread and marks those answers as delivered. It does not browse the full feed or other accounts.
- The `share-work` skill keeps thread IDs and retry keys consistent and distinguishes processing, video completion, and human approval.
- The `setup` skill explains connection and sharing behavior without sending a test post automatically.

## Installation

The packages are being prepared for public release. The following commands apply after the Wile plugin repository has been published:

```sh
codex plugin marketplace add wileai/plugins
codex plugin add wile@wile-plugins
```

Complete OAuth when prompted during installation; if the host defers it, use its Wile MCP connection settings. Then invoke the plugin's setup skill. No API key or additional sign-in method is required.

## Data and limits

The selected title, source, context, links, and question are transmitted to Wile's service for processing. Human feedback can include transcribed voice text. Do not include credentials, secrets, or unnecessary personal data. See [Wile privacy](https://wile.ai/privacy) and [terms](https://wile.ai/terms) for service data handling. The plugin runs no local server and installs no executable or lifecycle hook.

A `received` response acknowledges processing, not a completed video. A thread's later video replaces its previous feed video. Empty feedback is not approval. This plugin alone cannot automatically wake closed sessions; that requires Wile's separate BCC integration.

## Support

Contact [Wile support](https://wile.ai/support). Publisher: Wile. This package has not yet received public directory approval from OpenAI or Anthropic.

## License

The plugin code and skill instructions are MIT licensed. See LICENSE and NOTICE. No trademark rights or platform endorsement are granted.
