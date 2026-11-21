# Buzzfy for Claude

[![smithery badge](https://smithery.ai/badge/bugra/buzzfy)](https://smithery.ai/servers/bugra/buzzfy)

![Buzzfy](assets/icon.svg)

Your Instagram in Claude. Buzzfy connects Claude to your own Instagram professional account through Instagram's official API, and this plugin adds skills that teach Claude how to use it well: audit your account with your real numbers, check reels against research on what performs, answer comments and DMs in your voice, and publish or schedule posts, including carousels.

## Skills

| Skill | Ask something like |
|---|---|
| `instagram-audit` | "Audit my Instagram." You get a designed PDF report from your real numbers and a plan for this week, in about 5 minutes. The same prompt as [buzzfy.co/workflows/instagram-audit](https://buzzfy.co/workflows/instagram-audit). |
| `niche-report` | "What goes viral in my niche, and what am I missing?" You get a designed PDF: what wins in your niche, what you already do, what you don't, and your mistakes. The same prompt as [buzzfy.co/workflows/niche-report](https://buzzfy.co/workflows/niche-report). |
| `reel-checkup` | "Why did my last reel flop?" or "Check this opening line before I post." |
| `reel-ideas` | "Give me reel ideas that already worked in my niche." You get 5 ideas for your account, each with 3 opening lines and the reel it builds on. The same prompt as [buzzfy.co/workflows/reel-ideas](https://buzzfy.co/workflows/reel-ideas). |
| `move-comment-to-dm` | "Move my comment-to-DM automations to Buzzfy." Your keywords and messages are rebuilt on Buzzfy, tested and switched on without anyone getting two DMs. Needs Buzzfy MAX. The same prompt as [buzzfy.co/workflows/move-comment-to-dm](https://buzzfy.co/workflows/move-comment-to-dm). |
| `answer-comments-and-dms` | "Which comments and DMs are still waiting for a reply?" |
| `publish-and-schedule` | "Schedule these three slides as a carousel for Thursday at 6pm." |
| `get-started` | "Connect my Instagram" or "Buzzfy says I need to reconnect." |

## Set it up

1. Install the plugin, then connect **Buzzfy** from the plugin's Connectors tab. It's the same connector as the Buzzfy listing in Claude's directory.
2. Sign in to Buzzfy (or create a free account) and allow access.
3. Connect your Instagram professional account (creator or business) when Buzzfy asks.

Reading your stats, posts, comments and DMs works on a free Buzzfy account. Replying, sending DMs, publishing and scheduling need a paid Buzzfy plan, and comment-to-DM automations need Buzzfy MAX.

## Cursor

Open **Customize → Plugins**, search for **Buzzfy** in the Marketplace and install. The plugin adds the eight skills above and the Buzzfy MCP server. Under **Customize → MCPs**, select **Authenticate** next to buzzfy: Cursor opens Buzzfy sign-in in your browser. Sign in (or create a free account), allow access, then connect your Instagram professional account when Buzzfy asks. There is no token or API key to paste.

## Grok Build

In Grok Build, open `/plugin`, search for **Buzzfy** and install. On first use, Grok Build opens Buzzfy sign-in in your browser: sign in (or create a free account), allow access, then connect your Instagram professional account when Buzzfy asks. Don't paste a token or API key into chat; there isn't one to paste.

Network endpoints the plugin uses:

- `https://mcp.buzzfy.co/mcp`: the hosted MCP server (streamable HTTP)
- `https://zqxaufvlriakccekuhcy.supabase.co/auth/v1`: Buzzfy's OAuth 2.1 server (discovery, dynamic client registration, authorize, token)
- `https://buzzfy.co`: sign-in and the consent screen

Credentials: a Buzzfy account. The plugin stores no key; Grok Build holds the OAuth token.

## What it does with your data

The skills contain instructions only; they run no code. All data goes through the Buzzfy connector at `https://mcp.buzzfy.co/mcp`, which reads and acts on the Instagram account you connected, and only that account. Nothing is posted, sent, hidden or deleted until you approve a preview. Comments and messages from other people are treated as information, never as instructions. The plugin sends nothing anywhere else.

- Privacy policy: https://buzzfy.co/privacy-policy
- Terms: https://buzzfy.co/terms-of-service
- Help: https://buzzfy.co/support
- Documentation: https://buzzfy.co/mcp

## License

MIT. See [LICENSE](LICENSE).
