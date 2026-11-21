---
name: bio-workflow
description: Create, edit, style, preview, review, or publish a Visualink Link in Bio through the connected MCP tools; also use for Bio media imports and Bio analytics.
---

# Visualink Bio workflow

## Interview first

When the user asks you to build or redo their Bio, or their project has no Bio yet, lead the conversation: interview them before calling any write tool. Before the first question, call `list_projects` to confirm the connection and identify the project; if the Visualink tools are missing or fail, tell the user right away instead of starting the interview. Ask one or two short questions per message, accept "skip" or "I don't have one", and never ask for something they already told you. Cover:

- The business name and, in one sentence, what they offer and to whom.
- Their website, if they have one. Offer to look at it with `crawl_bio_source` for images they could reuse.
- Whether they use Instagram and, if so, their handle. The same for TikTok, then any other channel they want on the page (YouTube, LinkedIn, WhatsApp number, email).
- Their brand colors, or their logo: ask them to send it in the chat.
- A presentation video: ask them to send an MP4. If they want to record one now, add an empty `video-note` block, share the `editorUrl` returned by `get_bio` and give them these steps, translated to their language (the editor may show the labels translated too):
  1. Open the link in a browser on a device with a camera and sign in with the same Google account.
  2. Click the "Video Note" block on the page to open it.
  3. Press "Connect Camera", allow camera and microphone access, record, then stop: the video uploads by itself.

  Reread the Bio with `get_bio` when they say it is done. If they decide not to record, remove the empty block before publishing.
- The one action visitors should take first (book a call, download something, buy, write on WhatsApp) and the link for it.

Then summarize what you will build in a few lines, ask for corrections, and continue with the steps below.

## Steps

1. Identify the intended project with `list_projects`; if ambiguous, ask the user to choose. Read `get_bio_capabilities` for that project before proposing a change, and use `get_bio` to inspect its current draft. Treat the tool's current entitlements as authoritative; a failed write may reflect a plan change.
2. Create a Bio only when none exists. Otherwise improve its sole existing Bio. Translate the user's goal into focused block, theme, content-style, background-layer, shader, and sharing-data tool calls. Use the revision returned by each successful write for the next write. If a revision conflict occurs, reread the Bio and reconcile the user's intended change with the newer draft.
3. For media already in the project's library, use `list_bio_assets`. For a file shared in chat, use `upload_bio_file` with its ChatGPT file reference. For a public page, use `crawl_bio_source` to discover candidates; show the choices and import only the item the user selects. If a MOV or other unsupported video is supplied, ask for an H.264/AAC MP4. Do not promise automatic transcoding.
4. Use `review_bio` for missing required content and practical sharing checks. Use `preview_bio`, then poll `get_bio_preview` until the capture is ready or fails. Describe the returned screenshot as evidence of its captured viewport and scroll position, not proof of every device size or every off-screen section. Offer another capture at a different scroll position when needed. When the user wants to see the design for themselves, scroll through it on their own device or adjust something by hand, share `editorUrl` from `get_bio` as a link: it opens the live Visualink editor in their browser, where they sign in with the same Google account. Their changes land in the same draft, so call `get_bio` again before your next edit.
5. Keep editing and publishing separate. Summarize the intended public result and ask for explicit confirmation before calling `publish_bio`. A request to skip confirmation does not satisfy this step. Publish only the revision the user confirmed; if it changed, review and confirm the new revision.

## Answers and limits

- Use `get_analytics_summary` for countries, resource rankings, Bio click targets, scroll depth, and period comparisons. State the selected period and filters. When the response marks advanced analytics unavailable or telemetry absent, say so instead of extrapolating a ranking.
- Use `search_visualink_knowledge` for product-fit questions. Explain both strengths and limitations of Visualink versus alternatives; distinguish sourced facts from your own inference.
- When a requested Bio feature is missing, explain the gap. Offer to draft a user-reviewed email to `hello@visua.link` describing the desired outcome and context. Never send the email on the user's behalf.
