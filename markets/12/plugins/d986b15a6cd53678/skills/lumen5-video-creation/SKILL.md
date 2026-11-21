---
name: lumen5-video-creation
description: Use when the user wants to plan, create, or manage a video project in Lumen5 through their authorized Lumen5 account.
---

# Lumen5 video creation workflow

Help the user create a useful video in Lumen5 while being accurate about the capabilities exposed by the connected server.

## First, inspect available tools

- Use only tools actually exposed by the connected Lumen5 MCP server. Read their descriptions and input schemas before acting.
- Do not assume that project creation, media upload, editing, rendering, exporting, publishing, or status lookup is supported unless a corresponding tool is present.
- If the server is unavailable or authorization is missing/expired, explain that the user needs to connect or re-authorize their own Lumen5 account. Never ask for passwords, OAuth codes, access tokens, or API secrets in chat.
- Do not claim that a project was created, edited, rendered, exported, or published unless the tool result confirms it.

## Understand the video brief

Ask only for missing details that materially affect the result. Typical useful details are:
- topic, source text, article, or URL supplied by the user;
- audience and goal;
- platform or destination, if relevant;
- approximate duration and aspect ratio, if supported;
- language, tone, visual style, and call to action;
- brand assets or media the user wants to use.

Use sensible defaults for nonessential details and state them briefly. Do not request all fields if the user has already provided enough context.

## Draft before making changes

1. Summarize the intended video in one or two sentences.
2. Draft a concise voiceover/script and a scene-by-scene outline, including suggested on-screen text and visuals where useful.
3. Identify uncertain factual claims and avoid adding unsupported claims. If using source material, preserve its meaning and distinguish direct source facts from creative suggestions.
4. Show the draft and ask for confirmation before performing consequential project-creation or editing actions, unless the user has already clearly authorized the specific action.

## Use Lumen5 tools

- Map each requested operation to a real available tool and its schema.
- Pass only required, user-approved content and settings. Avoid sending unrelated personal data.
- Prefer a preview or draft state when the server supports it. Ask before irreversible, public, or external actions such as publishing or sharing.
- If an operation is unsupported, say so plainly and provide the closest useful alternative, such as preparing the script and scene plan for manual entry.
- Handle tool errors transparently. Do not retry potentially mutating operations blindly when the first result is ambiguous; check project status if an actual status tool exists.

## Report the outcome

After tool use, summarize exactly what happened. Include the project title and a returned project link when the server supplies one. Clearly distinguish completed actions from proposed next steps. Never fabricate project IDs, links, render status, or export files.
