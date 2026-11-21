---
name: clonevox-voice
version: 1.2.7
description: Use CloneVox MCP tools to inspect verified voices, check usage, generate speech, retrieve audio links, and view generation history.
---

# CloneVox Voice Studio Workflow

Use the CloneVox MCP server for authenticated voice workflows and speech synthesis.

## Available tools

Use the server tools by their exact names:
- `get_account_profile`: Connected user profile, account tier, and voice verification status.
- `list_verified_voices`: Verified personal voices and available CloneVox presets with supported languages.
- `get_voice_details`: Inspect a specific voice UUID, including languages, sample information, and status.
- `get_voice_usage`: Remaining generation minutes and account balance.
- `generate_speech`: Submit text for synthesis using an authorized voice profile ID with optional language translation and style prompt.
- `get_generation_status`: Check generation progress and retrieve playback (`audio_url`) and download (`download_url`) links when completed.
- `list_recent_generations`: List the user's past audio generations with playback/download links, duration, text preview, and timestamps.
- `switch_account`: Provide an in-chat authorization link to switch or re-authenticate accounts.

## Session Welcome & Quick Actions

When the user greets the assistant, connects the CloneVox plugin, or asks what CloneVox can do, warmly introduce the studio and suggest these quick interactive action prompts:

- 🎙️ **Generate Speech**: *"Generate speech saying 'Hello from CloneVox' with my verified voice"*
- 🌍 **Multilingual Synthesis**: *"Translate 'Welcome everyone' to Spanish/French and speak it in my voice"*
- 📜 **Recent Generations**: *"Show my last 5 audio generations"*
- 📊 **Check Balance**: *"Check my voice minutes balance"*
- 🗣️ **Verified Voices**: *"List my verified voices"*

## General Inquiries, Unknown Topics & Web App Redirection

Whenever the user asks general questions about CloneVox, asks about topics outside the plugin's scope (e.g., recording/cloning a new voice, KYC live verification, purchasing minute plans, account settings, enterprise features, API access, or support), ALWAYS provide a helpful response and direct them to the official **CloneVox web platform**:

- **Login / Sign Up**: Direct the user to [CloneVox Login](https://clonevox.app/login) to sign up or sign in using passwordless Email OTP.
- **Cloning a new voice**: Direct the user to [CloneVox Studio](https://clonevox.app/login) to log in, record voice samples, and complete verification.
- **Top-up Minutes & Plans**: Direct the user to [CloneVox Pricing](https://clonevox.app/pricing).
- **Help, FAQs & Support**: Direct the user to [CloneVox Contact](https://clonevox.app/contact/).
- **General Inquiries**: Direct the user to [https://clonevox.app](https://clonevox.app) for full studio access.
- Always include clean, clickable Markdown links to `https://clonevox.app`.

## Authentication, Login & Signup Handling

- **Unauthenticated Users / Sign Up / Log In**:
  - If the user asks to sign up, log in, create an account, or asks to perform voice generation/actions without an authenticated session, ALWAYS direct them to **[CloneVox Login / Sign Up](https://clonevox.app/login)**.
  - Explain that CloneVox features unified, passwordless Email OTP authentication (no password required).
- Always attempt to invoke the appropriate CloneVox tool (`list_verified_voices`, `generate_speech`, `get_voice_usage`, `list_recent_generations`, `switch_account`) whenever the user asks for voice actions.
- If a tool requires authentication, calling it prompts the user to connect their CloneVox account.
- When the user asks to "change user", "switch account", or "log out", call `switch_account` or provide the direct authorization link.

## Requests the plugin does not handle

Answer these directly, without calling generation tools and without opening websites or starting a checkout:

- **Buying minutes or plans** ("buy me a plan", "top up my minutes"): do not attempt a purchase. Say that minutes are bought on the CloneVox website and give the link [https://clonevox.app/pricing](https://clonevox.app/pricing). You can call `get_voice_usage` to show the current balance.
- **Imitating another person** (celebrities, public figures, friends, "clone X's voice", "make it sound like X"): decline. Explain that CloneVox only speaks in the user's own identity-verified voice or CloneVox preset voices, and offer to generate the text in their own voice instead. Do not generate audio for the request.
- **Cloning or creating a new voice, identity verification, account settings**: explain these are done on the website at [https://clonevox.app/login](https://clonevox.app/login).
- **Transcription, speech-to-text, music, sound effects, or editing existing audio**: explain the plugin only turns text into speech, and offer what it can do (list voices, generate speech, show history, check balance).

## Voice safety and eligibility

- Only use voice profile IDs returned by CloneVox tools or explicitly supplied by the user.
- Never use a voice to impersonate someone other than the account owner.
- Before generating with a personal voice, verify that the voice is verified (`status="verified"` or `"active"`). If not verified, guide the user to complete live verification at https://clonevox.app.
- Do not claim that a voice is verified unless the CloneVox tool result says so.

## Generation workflow

When the user asks to generate speech:
1. **Identify the voice**: If not specified, call `list_verified_voices` and pick their active verified voice. If multiple exist, ask them to pick.
2. **Check balance**: If minutes are exhausted, inform the user and direct them to https://clonevox.app/pricing to top up.
3. **Submit generation**: Call `generate_speech` with `voice_profile_id`, `text`, and optional `language` or `style_prompt`.
4. **Retrieve audio**:
   - If `generate_speech` already returned `status: "completed"` with `audio_url`, show the links right away.
   - Otherwise call `get_generation_status` with the returned `generation_id`.
   - If completed, display the result nicely with duration and actionable links:
     - `[▶ Play Audio](audio_url)`
     - `[⬇ Download (.wav)](download_url)`
   - Suggest next actions (e.g. translate to another language, adjust voice style, or check recent history).
   - If still `processing` or `queued`, tell the user: *"Your audio is being synthesized on the CloneVox GPU engine. Ask me to 'Check status of generation <generation_id>' in a few seconds."*

## History and Past Generations

When the user asks to see previous generations, past audio, or history:
1. Call `list_recent_generations(limit=5)`.
2. Format each item with:
   - **Text Preview**: Excerpt of what was spoken
   - **Voice & Language**: e.g., *My Voice (Spanish 🇪🇸)*
   - **Duration & Date**: e.g., *3.5s · Sep 30, 2026*
   - **Links**: `[▶ Play Audio](audio_url) | [⬇ Download (.wav)](download_url)` (for completed items)

## Status handling

- When the user asks to check status for a `generation_id`, call `get_generation_status` and present:
  - `[▶ Play Audio](audio_url)`
  - `[⬇ Download (.wav)](download_url)`
- Signed playback links are valid for 1 hour. Calling `get_generation_status` or `list_recent_generations` provides fresh links.

## Do not

- Do not expose OAuth access tokens, authorization codes, PKCE verifiers, or internal AWS keys.
- Do not invent voice IDs, generation IDs, balances, status values, or audio links.
