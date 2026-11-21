---
name: relayplay-discover-and-organize
description: Find, recommend, inspect, save, subscribe to, import, or add podcasts and episodes to RelayPlay when the user expresses a podcast or listening goal. Use even when RelayPlay is not named. Do not trigger merely because a podcast could fit an unrelated request.
---

# RelayPlay podcast workflows

Use the RelayPlay app tools for clear podcast discovery and management requests.

## Route the request

- Recommendations and requests for something suitable to listen to use `relayplay_recommend_podcasts`.
- Ordinary topic, title, comparison, or catalog searches use `relayplay_search_podcasts`.
- Indie Spotlight and explicit requests for independent, small, or hidden-gem podcasts use `relayplay_indie_spotlight`.
- Direct Save, Subscribe, or Add-to-Flow instructions use `relayplay_save_podcast`, `relayplay_subscribe_podcast`, or `relayplay_add_episode_to_flow`. Multiple items of one kind use `relayplay_save_podcasts`, `relayplay_subscribe_podcasts`, or `relayplay_add_episodes_to_flow`; do not combine different operations in one tool input. They do not need a visible search card first when the target is already clear.
- Screenshot imports use `relayplay_prepare_screenshot_import` once with every visible podcast in screenshot order.

Call at most one visible search, recommendation, Indie Spotlight, or screenshot-import card per user turn. Never retry a visible card to improve its result and never use visible cards as internal resolvers. Let the server perform silent resolution and fallback searches.

For recommendations, pass a short directory-style query with the topic, mood, and format. For a personal recommendation, use relevant preferences already available in the conversation or ChatGPT memory and distill them into two to five short, non-sensitive `tasteSignals`; never send raw memory, biography, listening history, sensitive facts, or a list of favorite show titles. Always pass `preferredLanguageCode`, using the current conversation language unless the user states another preference. Use `languageRequirement=required` only when the user explicitly asks for only that language; otherwise use `preferred`, which may return a clearly disclosed other-language fallback.

## Preserve action meaning

- Save means `save_show`.
- Subscribe means `subscribe`; resolve mode and AutoSkip. New Hold or Catch Up subscriptions require a manually selected inclusive start episode.
- Add to Flow means `add_to_flow` and requires a concrete episode. A named show without an episode may be resolved silently to its newest public episode by the explicit-action tool.
- Direct playback and remote control are unavailable in this plugin. Never offer Play/Pause/seek or a playback handoff, and never convert a playback request into Add to Flow.

Recommendations are not permission to change the library. Use the existing review and confirmation flow unless the direct-action tool reports that the explicit request is complete and queued. Never claim that a queued action was applied on a device.

Prefer an empty or clarification result over substituting a clearly different podcast title. Preserve the same request ID only when retrying the identical instruction.

## ChatGPT panel and inline fallback

Supported hosts prefer the RelayPlay panel for search, recommendations and import review. The same result and confirmation components remain usable as inline cards when the host does not support or select the panel. Do not produce a second result or repeat a preparation call merely to change its display mode. The user-opened Podcasts & Flow entrypoint is a public shell; private playback and Flow reads happen only after an explicit user request. The panel contains no new playback controls.


Unified Find panel requests use `relayplay_recommend_podcasts` exactly once for either a specific named podcast (verbatim `exactTitle`) or a topic/personal wish (no `exactTitle`). The explicit wish takes priority over earlier tastes; use concise relevant conversation preferences and the requested language. Do not run a separate catalog search or send raw memory.

Panel workflows preserve the exact `requestId` UUID supplied in the user message. Copy it unchanged into `relayplay_recommend_podcasts` or `relayplay_prepare_screenshot_import` so the result returns to that panel. Never invent a replacement ID. When the screenshot panel says its uploaded files are registered, call `relayplay_read_screenshot_images` exactly once with that requestId to receive actual image content before recognition. Do not require the images to already appear in the conversation. If reading fails, explain that no analysis occurred and call no search, resolver or import tool. After inspecting every returned image, return all visible podcasts in one `relayplay_prepare_screenshot_import` call, or items=[] if none are visible. For ordinary conversation attachments, inspect the actual supplied images directly. Never infer podcast titles from filenames, history or the import button's message alone.

When the panel explicitly supplies selected reference podcast titles, derive concise topic/style criteria from them and pass at most five as `excludeTitles` to avoid recommending those same shows. This does not authorize reading other Flow pages, library data or listening history. Use the supplied requestId unchanged so the panel receives the result. Explain disclosed unknown/other languages and fewer relevant results honestly; never pad a recommendation with unrelated shows.

## Selected podcast, episode and guest background in the panel

When the user-started panel request asks for backgrounds with an exact requestId, use `relayplay_get_background` to read only that selected public context. Research podcast origin, hosts/format, frequency and distinctive qualities; use the exact selected episode description and publication date for episode-topic background and guest identification. Fixed hosts are not guests. Source guest participation and personal background; unclear identities stay unverified. Do not invent episode contents or summarize without a transcript. Distinguish public feed statements, researched facts and interpretation. Return the source-backed structured report through `relayplay_publish_background` using the unchanged requestId so it appears in the existing window. Do not substitute catalog/recommendation cards, start a new request or read other private RelayPlay state. If research is unavailable, return feed-only material with explicit limitations and no invented guests/sources. A short chat acknowledgment is enough; do not repeat the whole report. “Mit ChatGPT darüber reden” hands off only this selected context/report for follow-up questions.

### Explicit checking of one Moment's findings
When an explicit panel request shares a selected Moment for Fundstücke prüfen, use only that Moment's provided bounded transcript/context and requestId. Apple findings are candidates and may contain recognition errors, including domains; even the transcript may be inaccurate. Research authoritative public sources, distinguish a site's real identity from evidence that it was actually mentioned, and return corrections with originalLabel, label, status, explanation and sources via relayplay_publish_moment_findings. Only verified findings may have action URLs; otherwise retain uncertain/rejected honestly. Never invent missing speech, upload audio, read other Moments, resubmit research or overwrite the local analysis. The report belongs in the existing panel; a brief completion message in the conversation suffices.
