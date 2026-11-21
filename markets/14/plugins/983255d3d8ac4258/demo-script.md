# Sellerity Roleplay: Demo Recording Flow

This is a recording script for the public ChatGPT plugin package `sellerity-roleplay` version `1.0.1`. It is a plan, not evidence that any case has been run. Record the actual ChatGPT interactions and results; do not stage or invent outputs.

## Before recording

- Use the ChatGPT browser experience and the hosted Sellerity Roleplay connection. This plugin uses a remote MCP endpoint and must not depend on Codex desktop or a local server.
- Use only the dedicated review workspace and its sample data. Check the exact company, bot, and scorecard names before recording; substitute those names wherever this script uses brackets.
- Sign in through the ChatGPT connection flow as `admin@test.com` for the full walkthrough. Keep passwords and authentication screens off-camera; never narrate or display credentials.
- Start with a fresh chat. Show the plugin name and connected state, but not private browser tabs, account secrets, or unrelated data.
- Have a disposable company available for bot and scorecard creation steps. Approved creation changes workspace data. If there is no disposable company, show confirmation gates but do not approve saves; mark those parts as not demonstrated rather than changing persistent review fixtures.
- Do not replace real tool results with prepared text. Pause long enough for responses to be readable. If a request fails, stop and resolve it before recording.

## Recording script

### 1. Opening and connection

**Show:** ChatGPT with Sellerity Roleplay connected and, where the host displays it, the packaged version `1.0.1`. Keep connection/OAuth credentials out of frame.

**Say:** “This is Sellerity Roleplay running in ChatGPT through Sellerity’s hosted service. I’ll show account access, bots, scorecards, and company access boundaries using dedicated review data—all as a company admin.”

### 2. Account and accessible companies — positive case 1

**Account:** `admin@test.com`

**Ask:** “Show my Sellerity account and the companies I can access.”

**Show:** The returned account name/email, accessible company names and roles, and onboarding status. Do not expose internal IDs. Use the exact company name returned in later prompts.

### 3. Bot inventory — positive case 2

**Ask:** “How many roleplay bots do I have in [exact company name from my profile]?”

**Show:** The count and bot names (or list summary) from the tool response for that company only. Do not expose internal IDs.

### 4. Find a bot and get its start link — positive case 3

**Ask:** “Find the [existing review bot name] roleplay bot in [exact company name] and give me its start link.”

**Show:** The matching bot and the clickable start link. Do not expose raw URL parameters or internal IDs. Do not launch or complete a roleplay session unless it is separately approved and needed for the review.

### 5. Bot draft and creation review — positive case 4

**Account:** Keep the admin account connected. Use the disposable review company.

**Ask:** “As an admin, draft a roleplay bot named Review Demo [short unique suffix] for a buyer at [fictional prospect company], using this scenario: [brief, harmless sales-training scenario]. Show me the draft to review before saving it.”

**Show:** The generated draft and its details. Make clear that it is only a draft.

**Then ask:** “Create the bot using the draft you just showed me.”

**Show:** Check whether the assistant presents the reviewed details and asks for approval before saving. Record the observed behavior. Do not approve unless using a disposable company and the details are suitable.

**If using a disposable company and the displayed details are suitable, say:** “I approve creating this bot with the details shown.”

**Show:** The creation response and resulting bot confirmation. If the response is not successful, do not claim success.

### 6. Scorecard creation with approval — positive case 5

**Ask:** “In [exact company name], create a custom scorecard named Review Demo Scorecard [short unique suffix] for basic call quality: greeting, discovery, and next steps. Show me the full scorecard and wait for my approval before saving it.”

**Show:** The proposed scorecard (name, description, criteria) and the confirmation gate. If using a disposable company and the proposal looks correct, approve explicitly and show the success response. If not demonstrating a save, stop at the confirmation gate and note that creation was not approved on camera.

### 7. Inaccessible company boundaries — negative cases 1–3

**Account:** Stay signed in as `admin@test.com`. Use the same chat or a fresh chat on the same account—do not switch users. Use a clearly fictional company name that is not in the accessible-company list from case 1 (for example, “Fictional Unlisted Demo Company”).

**Ask (negative case 1):** “List the roleplay bots for Fictional Unlisted Demo Company.”

**Show:** Refusal or access-denied response with no bot data for that company. The response should steer the user toward companies in their profile.

**Ask (negative case 2):** “Show recent roleplay calls for Fictional Unlisted Demo Company.”

**Show:** Same boundary behavior—no call data for the inaccessible company.

**Ask (negative case 3):** “List teammates in Fictional Unlisted Demo Company.”

**Show:** Same boundary behavior—no team or membership data for the inaccessible company.

### 8. Close

**Say:** “Sellerity Roleplay lets authorized users see their workspace, count and find bots, open session links, and create training content like bots and scorecards from ChatGPT. Review steps are available for supported changes. Requests for companies outside your profile are blocked.”

**Show:** The plugin connection or listing name briefly, then stop recording.

## After recording

- Play back the saved video and verify the prompts and actual results are readable, all shown interactions succeeded as represented, and no credentials, private tabs, or unrelated customer data appear.
- Host it somewhere the reviewer can open without requesting access; test playback in a signed-out/private browser window.
- Only after the recording URL is actually verified, add it to `extensions.com.openai.review.demo_recording_url` in `plugin.json` and rebuild the submission ZIP.
- Record actual case outcomes in the portal/preparation notes. Mark cases `Passed`, `Failed`, `Blocked`, or `Not run` based on what happened; the script itself does not count as a test result.
