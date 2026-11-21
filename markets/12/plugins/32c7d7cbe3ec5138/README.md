# Polyglota Live Practice — 0.4.0
Audio-first language missions with authored characters, correction-language
choice, word review, quizzes and a host-powered story relay. Same listing/package
as 0.1.0; the older unsaved two-scenario text preview is superseded.

ChatGPT supplies conversation and voice where its client/account supports it.
A single recommended beginner mission appears immediately. Choose practice and
explanation languages, then Start. Live Practice guidance follows the selected
explanation language (eight supported languages); Words/Games retain authored
en/uk content. Start speaking, then use ChatGPT's Voice icon in the SAME chat, or
start in text and type in ChatGPT's own message box. Language changes preserve the
current mission. Word review and games sit at the bottom of the card.
The widget cannot start the microphone, synthesise speech or animate speech from
host audio. Text fallback remains useful. No Polyglota AI-provider call.

Save selected authored phrases through the existing first-party Polyglota signup/
sign-in, explicit confirmation, My Vocabulary and recall review. No OAuth/private
MCP account access, password sharing or conversation export.

Optional anonymous feature counts are user-controlled and disabled unless the
server-side metrics flag is deliberately enabled after manual SQL. No third-party
trackers, per-user host IDs or recorded conversations. No digital commerce.

Build: node scripts/build-chatgpt-public-package.mjs
Test: node scripts/check-chatgpt-public-package.mjs
Runbook: docs/CHATGPT_COMPANION_PRODUCT_2026_10.md
Actual HTTPS/host voice QA, real walkthrough and publisher review remain separate.
No credentials, app IDs or unverified host screenshots are invented in this ZIP. The review manifest references the owner's public walkthrough for OpenAI reviewers.

0.3.0: call render_live_practice first with no arguments for a one-mission start. Pass explicit correctionLanguage from the user accurately. The selected explanation language controls all Live Practice help in eight languages. Start uses native ChatGPT host context/messages; Type sends a real learner reply only to ChatGPT with the feedback policy refreshed on each submission. The card cannot activate Voice or auto-play host audio. On supported mobile clients, the user can enable Start with Voice in ChatGPT Settings → Voice. No new SQL, native binary, private linking or owned AI calls.

0.4.0: Live-Practice-first card. One explanation-language choice drives the card; starter missions show situation and goal in all eight languages; one Start speaking button plus a text option; after Start the card shrinks to a mission bar and points to ChatGPT's own Voice button or message box (no second typing box in the card). Words, games and privacy moved to a small bottom section.
