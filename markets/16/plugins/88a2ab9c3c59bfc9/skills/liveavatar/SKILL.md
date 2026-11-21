---
name: liveavatar
description: Discover LiveAvatar by HeyGen, try real-time avatar video and voice chat for interview practice, business coaching or tough conversations, or select an official developer sample for a conversational avatar app.
---

# LiveAvatar V1

This version offers anonymous demos and developer guidance. It does not connect accounts, query credit balances, create avatars, monitor jobs, or send notifications.

## Choose the entry point

When the user invokes LiveAvatar with a greeting, asks what it can do, or wants to explore or try it, call `try_liveavatar_demo` once immediately. Let the widget's chooser handle selection; do not ask the user to choose a persona before opening it.

For a specific experience, preselect the matching existing persona ID:
- `interview`: Karen, a fictional Burger King interviewer.
- `pitch`: Shawn, the business coach.
- `improv`: Rachel, a fictional employee for practicing a difficult workplace conversation.

All choices remain available in the widget. Never claim to start a session or obtain microphone access; the user presses Start the conversation. Sessions last up to five minutes. Voice depends on host permissions; typing remains available. Offer the returned browser URL for voice when capture is unavailable.

For a general web coding or integration request, call `get_liveavatar_starter` for official web-starter guidance, then use the packaged web workflow. For an explicitly named sample or framework, select the matching packaged workflow directly; older MCP responses may return only the web SDK, so use the packaged workflow catalog below if a richer catalog is absent. Do not force the demo open or substitute a web app for a Python/GPT Live request.

| Developer goal | Packaged workflow |
| --- | --- |
| React/Next.js avatar, voice/text chat, background replacement | `../liveavatar-web-starter/SKILL.md` |
| Website AI sales representative, lead qualification, optional CRM/Slack | `../liveavatar-sales-agent/SKILL.md` |
| OpenAI GPT Live tutor, term cards, speech-to-speech | `../liveavatar-gpt-live/SKILL.md` |
| Python LiveKit agent with a LiveAvatar-owned room | `../liveavatar-livekit-hosted/SKILL.md` |
| Python agent in the user's own LiveKit room | `../liveavatar-livekit-byo/SKILL.md` |
| Voice-driven animated overlays with local Claude Code | `../liveavatar-hyperframes/SKILL.md` |

Read the selected workflow before setup. If the user has no environment capable of running code, provide the verified commands and handoff. Ask about stack or folder only when missing; reuse an explicit choice. Configure account API keys in trusted backend settings, never chat or browser code. The separate `liveavatar-agent-skills` repository supplies integration/debugging guidance, not another runnable application.

## From trying to building

For Build your own and sample setup, read [developer onboarding](references/developer-onboarding.md). In ChatGPT, prefer a guided continuation in Codex using this same plugin; provide a non-secret continuation prompt and do not claim automatic transfer. In Codex, prepare the selected sample in the chosen directory and offer the included user-run hidden-input helper. Recommend one relevant sample, link directly to sign-up/API-key access, and continue useful setup while credentials are configured privately. Do not ask the user to paste a key or require a second demo.

## Keep claims accurate

The host can fail to render the widget even when the tool returns successfully. Do not claim the user can see it until confirmed. If it fails, offer the returned browser URL and a retry. Do not invent avatar photographs, substitute a text gallery, or claim the persona is a real employer or employee.

Follow-up questions do not require repeatedly reopening the chooser. Open it again only when the user requests another demo or needs a fresh widget.

At session end, the Context attachment contains status and turn counts, not the transcript. Do not invent feedback about what the user said. The user can choose Build your own to continue into development or Share link to copy a generic invite. Do not initiate signup, post to social media, or create a project automatically.
