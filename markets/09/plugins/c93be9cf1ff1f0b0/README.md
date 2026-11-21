# Welder: TikTok, Instagram & YouTube Autoposting

## Make it here. Post it everywhere.

Make a post in your AI chat and Welder puts it on TikTok, Instagram, YouTube, Facebook Pages, Threads, Bluesky and X — now or at a time you choose.

Turn a photo or video into a post, write a text post, or plan your week in one conversation. You see every post before it goes live. Review available performance and prepare replies without leaving the conversation.

### One message. Your accounts.

Ask your assistant to post a Reel, upload a Short or share your photos. Welder connects it to your TikTok, Instagram, Facebook Page, YouTube, Threads, Bluesky and X accounts. Review the content and let your assistant handle the steps.

### Get ahead of your next post

Build a content plan with your assistant, then schedule the posts you approve up to 30 days ahead. Keep creating while Welder gets each post out at its scheduled time. Stop a pending post when plans change.

### Make more of what works

Ask which posts people responded to and what to try next. Your assistant can read available post metrics, compare measured results and turn them into your next creative brief. Read comments and prepare thoughtful replies on supported networks.

### Keep your content moving

Creators can share a finished video without switching between upload screens. Small businesses can plan a week of posts from one conversation. Social media managers can publish to the right profiles and check each result. Builders can connect an existing content workflow to their audience.

Welder provides the connection, posting, scheduling and account data. Your assistant helps prepare the content. Recurring agent tasks use your host's scheduling feature when supported and requested; Welder schedules individual posts rather than agent runs.

## Start with a goal

- “Write a post about my business and share it on Facebook and Threads.”
- “Post my photo to Instagram with a caption you write.”
- “Plan 3 posts for this week and show me each one before it goes out.”
- “Post this video to my TikTok and Instagram with the caption we just approved.”
- “Which of my posts got the best response this month? Give me three ideas to test.”
- “Show the comments on my latest video and draft replies in my voice.”
- “Cancel tomorrow's scheduled post; the offer has changed.”

## Connect Welder

Install the plugin in your supported assistant, sign in to [Welder](https://weldergtm.com) or create an account when you connect, and connect your social accounts when a post needs them. Provider sign-in happens on the network's own website. You do not share social passwords with your assistant.

Attach a photo or video in the chat and your assistant passes it to Welder; coding apps upload local files directly. One post can carry per-network captions through `options.<network>.caption`. YouTube visibility defaults to public when the account allows it; for TikTok, your assistant asks who can see each video. Your assistant can use the options you approve.

Read access supports context, account lists and stored performance reports. Uploading, connecting accounts, posting, canceling and deleting require publishing access. Refreshing post metrics and reading comments also require publishing access because they may update state or consume account usage. X posting and comment reads require the appropriate X entitlement. Account and format support depend on each network's permissions. Some analytics and comment permissions remain unavailable; Welder identifies missing data rather than reporting it as zero. Live-post deletion is supported on X and Bluesky, and on YouTube and Facebook where the connection allows it.

## What Welder adds

Welder is a publishing service for AI assistants, not a thin proxy to network APIs.

Publishing on TikTok, Instagram, Facebook Pages, Threads and YouTube is open only to developer apps that pass each network's own review, and X needs paid API access. A person cannot simply plug these APIs into an assistant. Welder has been through those reviews, so people only sign in on each network's own site.

On top of that access, Welder provides:

- **Checks before posting:** `validate_post` tests media, duration, caption length and account access against each network's rules, without publishing anything.
- **One request, many networks:** a single post can go to several networks and accounts, with a different caption per network.
- **One scheduler:** approved posts can be scheduled up to 30 days ahead across all networks, and pending ones can be canceled.
- **Publishing that survives failures:** every network gets its own queue entry with saved progress and resumable uploads. Retrying with the same `idempotency_key` never creates a duplicate. If a network loses a response, Welder checks whether the post went out instead of posting again.
- **Media handling for chat:** photos and videos attached in the chat reach Welder with no separate upload step for the person, and images are prepared for each network's format.
- **Results across networks:** post metrics and supported comments in one place. Data a network does not share is reported as missing, never as zero.
- **Account safety:** network tokens are encrypted on Welder's servers and never reach the assistant. Access is scoped, a person can grant read-only access, and tools that publish are marked so the host asks first.

## Claude Code

```text
/plugin marketplace add Endless-River-Labs/welder-plugins
/plugin install welder-social-manager@welder-plugins
```

The Claude Directory listing is available after Anthropic review. Direct installation from this repository is a separate distribution path.

## ChatGPT and Codex

The root portable manifest and remote connection configuration package the same five workflows for supported hosts. OpenAI Directory availability follows OpenAI review. The package also includes Claude-compatible manifests.

For direct Git marketplace installation in Codex CLI:

```bash
codex plugin marketplace add Endless-River-Labs/welder-plugins
codex plugin add welder-social-manager@welder-plugins
```

Sign in to Welder through the host's OAuth connection flow. Direct Git installation is available separately from the reviewed OpenAI Directory listing.

For a direct remote connection, use [Welder's MCP endpoint](https://weldergtm.com/mcp) and the assistant's sign-in flow. Per-assistant setup guides are in the [Welder help center](https://weldergtm.com/docs).

## Cursor

Add `https://weldergtm.com/mcp` in Cursor's MCP settings and sign in to Welder. To install the plugin, unpack the Welder package for Cursor into `~/.cursor/plugins/local/welder-social-manager` and reload Cursor.

## Gemini CLI

Add `https://weldergtm.com/mcp` as an HTTP server in Gemini CLI's MCP settings and sign in to Welder when prompted. To install the extension, run:

```bash
gemini extensions install https://github.com/Endless-River-Labs/welder-plugins
```

## Antigravity

Add `https://weldergtm.com/mcp` in Antigravity's MCP settings and sign in to Welder. To install the plugin, unpack the Welder package for Antigravity, then run:

```bash
agy plugin install /path/to/welder-social-manager
```

## Kimi

Add `https://weldergtm.com/mcp` in Kimi Code's MCP settings and sign in to Welder with `/mcp-config login welder`. To install the plugin, unpack the Welder package for Kimi and run `/plugins install /path/to/welder-social-manager` in Kimi Code. Complete the Welder sign-in when prompted.

## Kiro

Add `https://weldergtm.com/mcp` in Kiro's MCP settings and sign in to Welder. To install the power, unpack the Welder package for Kiro, then choose **Add Custom Power** → **Import power from a folder** and select `welder-social-manager`. In CLI v3, run `/powers install /path/to/welder-social-manager`.

## Grok Build

Run `grok mcp add --transport http welder https://weldergtm.com/mcp` and sign in to Welder when prompted. To use the plugin, unpack the Welder package for Grok Build and start Grok with `grok --plugin-dir /path/to/welder-social-manager`.

After connecting, ask your assistant to show your accounts or prepare your first post.

## What the plugin sends and runs

This package contains readable instructions, connection metadata and brand images. It installs no executable server, lifecycle hooks or background process. On a tool call, your host sends the requested content, media references, account selection and options to Welder at `weldergtm.com`. Welder stores and processes them through its service, then sends an approved post to the selected connected social platforms through their APIs. Direct uploads go to Welder's Supabase storage through a short-lived destination returned by Welder. Welder may fetch a public HTTPS media URL when you request an import. Credentials and media upload destinations are never bundled in this repository. OAuth discovery uses `https://weldergtm.com/.well-known/*`; registration, consent and tokens use `https://weldergtm.com/oauth/*`, with `read` and `publish` scopes.

Original media is normally kept for seven days; a scheduled post keeps it until seven days after its scheduled time. Post history retains the caption, metadata and one small cover image while the workspace exists. Available metrics and comments come from connected networks; their privacy policies also apply. Your assistant can use them to prepare recommendations, without guaranteed reach or growth.

[Support](https://weldergtm.com/support) · [Help](https://weldergtm.com/docs) · [Privacy](https://weldergtm.com/privacy) · [Terms](https://weldergtm.com/terms) · [Data deletion](https://weldergtm.com/data-deletion)

The package instructions and configuration are MIT licensed. Welder's name and visual identity remain the property of their owner. The hosted service and private server implementation are not distributed by this package.
