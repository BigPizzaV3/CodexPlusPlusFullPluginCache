---
name: social-research
description: Research and write social media content with Vamos. Use when the user wants to find what is working on TikTok, Instagram or YouTube (trending formats, hooks and topics in a niche, a creator's or competitor's best posts, similar creators), break down a post's hook, comments or video, study Meta ads, or write posts, hooks, scripts, captions and briefs in their brand voice.
---

Vamos reads public posts and profiles by @handle or link (metrics, comments, transcripts, the video itself) and the Meta Ad Library, and it knows the workspace's brand, voice, memory and saved files. It plans its own research, so your part is to pass the request on and bring the answer back. It does not post for the user.

## One message per request

1. **Pick the chat.** For a follow-up on the same brand, campaign, creator or draft, continue its chat from `list_chats`. For unrelated work, call `create_chat` with a short name for it. Both return `brain`, the brand Vamos writes for; when the user has several workspaces, `list_chats` lists them, and work for another one goes in a chat created with `workspace` set to its name.
2. **Send the user's whole request in their own words** with `chat_completion_start`. Vamos researches and writes in the same turn, so "find the creators, then write scripts from them" is one message.
3. **Wait for it** with `chat_completion_poll` until `status` is `done`.
4. **Follow up in the same chat** once the answer has arrived: "now shorter", "do it for Instagram" or the user's pushback is the next message there. A message sent while a run is working starts a second run.

## What goes in the message

The user's words and whatever they named: handles, links, dates, platform, format, and facts about their own account. Their analytics (retention, reach, follower growth, sales) are private, so Vamos has those numbers only when the user shares them; pass them on as given.

Leave out what you would add yourself (a research plan, numbered parts, an output template, handles or numbers you found elsewhere), because it narrows Vamos's research.

- `Break down @vanessalau.co's last 30 days. Which patterns are worth using and which are noise?`
- Follow-up: `Now write scripts for the top two patterns.`
- `How does Portland Leather Goods run TikTok Shop lives? I sell leather handbags and want to copy the model.`

## Reuse before you resend

- **An earlier answer:** `get_messages` returns it at no cost.
- **The same analysis every day or week:** ask Vamos to save it as a routine; each run appears in `list_chats`.
- **Creators to keep watching, or a fact to remember** (a brand fact, a voice rule): ask Vamos in plain words, and it saves them to the workspace.

## The answer

Vamos's `result` is the deliverable. Present it with every link exactly as returned, because the links are the sources the user checks. A short framing line is fine.

After a dropped call or an unclear error, check `get_messages` before sending again: the run may have finished, and a resend runs it again.

The user's instructions take precedence over this skill.
