---
name: add-to-website
description: Put an Anam persona, a real-time AI video avatar, on a website or in an app, with a share link, the no-code website widget, or code using Anam's SDKs and a server-side session token. Use when the user wants to embed an AI avatar in a web page, React or Next.js app, Express or FastAPI backend, LiveKit or Pipecat agent, or mobile app.
compatibility: Needs the Anam MCP server connected to an Anam account (the Anam plugin in ChatGPT, or https://lab.anam.ai/mcp elsewhere). Writing code into a project needs a coding agent; in chat, hand the files to the user.
---

# Add a persona to a website or app

## The one rule

The Anam API key stays on the server. The server swaps it for a short-lived
session token for each conversation, and only that token reaches the browser
or app. Never put the API key in client code, a mobile app, a committed file
or the chat.

## 1. Pick the persona and the way in

1. Call `anam_connection_info` to confirm the organization.
2. Find the persona with `anam_persona_list`, or create one with the
   `create-persona` skill. Note its ID.
3. Choose with the user, simplest first:
   - **Share link**: a URL that opens the persona in a browser. Nothing to
     build; link to it from a site or email. `anam_share_link_create`
     (`expiresInHours`, `usageLimit`; 168 hours and 10 uses by default).
   - **Website widget**: an embed with no server code, for sites built with
     tools such as WordPress, Shopify, Squarespace, Wix or Framer.
   - **Code**: the user's own app, with full control of the page.

## 2a. Website widget

Call `anam_integration_guide` with `stack: "widget"` and `personaId`. In
short: open the persona in Anam Lab, select Deploy, then Website widget, add
the site's origin under Allowed domains, select Publish, and paste the embed
code into the page. The guide links the steps for each site builder.

## 2b. Code

1. Work out the stack from the user's project (`package.json`,
   `requirements.txt` and so on) or ask.
2. For Next.js, Express or FastAPI, call `anam_scaffold` with `stack`
   (`nextjs`, `express` or `fastapi`) and `personaId`. It returns
   ready-to-run files: a server route that swaps `ANAM_API_KEY` for a session
   token, a page using `@anam-ai/js-sdk`, an env file without the key, and
   install and run commands.
3. For anything else, call `anam_integration_guide` with `stack`
   (`javascript`, `react`, `livekit`, `pipecat`, `python`, `elevenlabs` or
   `mobile`) and `personaId`. It returns the package to install, a minimal
   snippet and the guides to follow. Read a guide in full with
   `anam_docs_read`, and look anything else up with `anam_docs_search`.
   Don't rely on remembered SDK APIs.

For browser apps, the shape is always the same:

- a server endpoint, such as `POST /api/session-token`, that reads
  `ANAM_API_KEY` from the environment and asks Anam for a session token for
  the persona;
- client code that fetches a token from that endpoint, creates the client
  with `@anam-ai/js-sdk`, streams to a `<video>` element with `autoplay` and
  `playsinline`, and stops streaming when the page or component goes away;
- `ANAM_API_KEY` in `.env.example` without a value, and real `.env` files
  ignored by git.

For LiveKit, Pipecat and Python, the key lives in the agent's or service's
environment; follow the guide.

In a coding agent, write the files into the project. In chat, give the user
the files and commands to copy.

## 3. Test

The user creates an API key at https://lab.anam.ai/api-keys and puts it in
their server's environment themselves. Run the app and check that the avatar
appears and answers. Every session uses the organization's minutes.

To try the persona before the app is ready, give them a share link.

## Troubleshooting

- 401 from the session-token call: the key is wrong, revoked or missing from
  the server's environment.
- No video: check the `<video>` element has `autoplay` and `playsinline`, and
  that the page asked for microphone access.
- Widget doesn't load: check the site's origin is in the widget's Allowed
  domains and the widget is published.
- Look up errors with `anam_docs_search` before guessing.
