---
name: get-started
description: Set up Masonry, then make a first video or product photo, and a first Studio product shoot. Use right after Masonry is installed, or when someone asks how to start with Masonry, how to connect it, or what it can do.
license: MIT
---

# Get started with Masonry

Masonry makes videos, product photos, voiceovers and music in the person's
own Masonry workspace. This guide is a default path for a new user. When the person asks
for something specific, do that instead, and skip any step they don't want.

## 1. Check the connection

Call `get_credits`.

- It answers: Masonry is connected. Say which workspace is connected and its
  credit balance, in one line. Don't mention prices or plans.
- The host asks the person to sign in: wait for them. Sign-in happens on
  masonry.so, where they choose a workspace and select Allow. Nothing needs to
  be copied or pasted.
- It fails for another reason: say what failed and stop.
- There is no `get_credits` tool: Masonry isn't connected in this app yet.
  Say so, and give the one setup step for the app they are in. The server is
  `https://masonry.so/mcp` everywhere, and sign-in happens on masonry.so the
  first time a tool runs:
  - Claude Code: `claude mcp add --transport http masonry https://masonry.so/mcp`
  - Codex: `codex mcp add masonry --url https://masonry.so/mcp`, then
    `codex mcp login masonry`
  - Cursor: add `{"mcpServers":{"masonry":{"url":"https://masonry.so/mcp"}}}`
    to `~/.cursor/mcp.json`
  - OpenClaw: `openclaw mcp add masonry --url https://masonry.so/mcp --transport streamable-http --auth oauth`,
    then `openclaw mcp login masonry`
  - Hermes: `hermes mcp add masonry --url https://masonry.so/mcp --auth oauth`,
    then `hermes mcp login masonry`
  - Any other app: see https://masonry.so/connect

  Don't run these commands yourself unless the person asks you to.

## 2. First video

If they want a video (most people do), ask what it is for in one short
question, unless they already said.

1. Offer one short clip built from the answer, for example: "a 6-second
   vertical clip of steam rising from your coffee on a sunlit counter".
2. After they agree, call `generate_video`. Leave `model` out unless they name
   one. To animate a photo they already have, use `animate_image` instead.
3. For a longer video (an ad, a story, a music video), agree on a few scenes
   first, generate each one, then edit them together with `combine_clips`. It
   does the whole edit in one call: a narrator (`voiceover`, made with
   `generate_audio` kind speech), music, sound effects, captions timed to the
   spoken words, and on-screen text such as a hook or a call to action.
4. Every result comes back with a `job_id`. Keep each scene's id and pass
   those ids to `combine_clips` in order. If a result says it is still
   rendering, call `check_generation` with its id until it is finished, then
   continue. Send each call once: a slow call is still working, and sending
   it again does not make it faster.
5. For shorts from a long video they already have: `add_media` brings in
   their file and `transcribe_media` shows the strongest moments; cut each
   one with `clip_video`, which keeps the speaker in a vertical frame. For a
   video link they have the right to use, `read_youtube_video` and
   `clip_youtube_video` do the same. Finish each clip in `combine_clips`
   with captions from clips. When these tools are not listed, ask for the
   video file and use `combine_clips` with `trim_start` and `trim_end`.
6. For a title card, kinetic text or an animated chart, write one
   self-contained HTML page and call `render_motion_graphics`; its job_id
   works as a clip in `combine_clips`.
7. To keep the same person or mascot across shots, make one clear image of
   them, call `save_character`, and pass the name in `characters` afterwards.
8. For a person who says exact words: make the line with `generate_audio`
   (kind speech), then call `animate_image` with their photo and
   `speech_job_id`. The clip is lip-synced and as long as the line. To put
   new words on an existing video, use `edit_video` with `speech_job_id`.
9. You cannot watch a video from its link. Before you present or combine a
   clip, call `inspect_video`: it returns labelled frames as images. Look
   at them, fix what is wrong, and describe only what you saw. To cut on
   the music, `inspect_audio` gives the tempo and the second of every beat.

## 3. First image

1. Ask what they sell, in one short question, unless they already said.
2. Offer one starter shot built from the answer, for example: "a product photo
   of your ceramic mug on a pale stone surface in soft daylight".
3. After they agree, call `generate_image` for one image. Leave `model` out
   unless they name one.
4. Tell them they can ask for changes in plain words ("warmer light", "add a
   eucalyptus sprig"); `remix_image` applies the change to that image.

## 4. First product shoot

Explain in one sentence: a Studio shoot turns one photo of their real product
into a matching set of finished photos. Ask for a photo of the product (an
attachment, an image link, or a product page link). Then follow the
`product-shoot` skill.

## 5. What to know

- Everything is saved in the Masonry workspace. `list_creations` shows what
  the person made here earlier, for when they ask to see past work. Don't use
  it to find something you just made: use the `job_id` from that result.
- Every generation uses the workspace's credits. When a tool reports that the
  workspace is out of credits, pass its message on as written, don't retry,
  and don't add your own suggestion to buy anything.
- Videos can take a few minutes; a video joined from several scenes takes
  longer.

## Don't

- Don't generate anything the person hasn't agreed to.
- Don't invent the person's product, brand name, or results.
- Don't promise features the tools don't have, such as deleting creations or
  opening another workspace.
