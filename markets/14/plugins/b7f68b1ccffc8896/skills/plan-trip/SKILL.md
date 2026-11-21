---
name: plan-trip
description: Plan a trip together, format an existing itinerary as Traviz travel notes, and open the itinerary in Traviz for visualization. Use when the user asks to plan with Traviz or send a travel plan to Traviz.
---

# Plan with Traviz

Use the user's language (English or Chinese). This plugin uses the host conversation; no additional AI API key is needed.

1. Call the `get_planning_prompt` tool with locale `en` (or `zh`) and follow that planning prompt. It is extracted from Traviz's actual planning and formatting prompts. The copy/paste instruction is a manual fallback; use the handoff below when available.
2. Reuse already discussed information. Recommend a reasonable route with useful reasons. Ask one helpful question at a time; topics are examples, not a questionnaire. Respect skipped topics. Do not invent reservations, addresses or travel dates. Verify locations and current practical details with available search tools; distinguish suggestions from confirmed arrangements. Never book or pay without the user's specific confirmation.
3. When the user confirms the itinerary or asks to visualize it, produce the full formatted notes. Use just the itinerary text (no code fences). Use the format exactly, including dates, full addresses, localized role markers, and transport before its arriving stop. Preserve useful detailed notes.
4. Call `prepare_trip` with the title, complete notes, and locale. Correct any parsing error before continuing. Never construct or guess a base64 payload yourself. Do not put private booking references, passport or payment details in the itinerary.
5. If the host can open URLs on the user's device and the user requested opening/visualizing, open the returned HTTPS `url` with its supported browser/computer integration. Otherwise provide the returned HTTPS `url` as an “Open in Traviz” link. Never claim a remotely running tool opened the user's iPhone. The link contains the itinerary; anyone holding it can read it. Do not send it to an unrelated service.
6. Updated Traviz imports into a new plan and invokes the same parser, location matching and visualization used by Travel Notes. Unsaved-work confirmation and the saved-trip limit still apply. Verify the map is visible when device control is available. Older builds show the import preview instead: import and tap Visualize trip. If Traviz isn't installed, provide its App Store link https://apps.apple.com/app/id6821230405 and the notes as a fallback.

Do not claim a plugin is installed/published, a trip saved, or a location matched without a tool result or visible app confirmation. Opening links may require a tap on mobile or a browser confirmation.
