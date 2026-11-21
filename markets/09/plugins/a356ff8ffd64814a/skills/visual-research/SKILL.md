---
name: visual-research
description: Browse real app flows, screens, and UI elements in Flownato, or compare captured examples for UX research. Use when someone asks for Flownato references or visual examples from real apps.
---

Use the connected Flownato tools to present real visual references in the conversation.

Retrieve catalog content, screenshots, and the interactive interface through the connected production Flownato service. Do not read a local checkout, local fixture, or localhost preview as a substitute for the installed plugin. If the connection needs authentication, use the host's normal OAuth connection flow; do not bypass sign-in or fabricate results.

## Choose the result

- A task across apps, such as onboarding or hotel booking: call `search_flows` once. Pass the requested number as `limit` (1–20); use the tool default when no number is given. Each gallery preview opens its flow without another chat message.
- All journeys in one app: call `search_flows` with an empty `query` and the named `app`. A task across all apps: set `query` to that task and omit `app`. Keep the same app scope when refining a task unless the user changes it.
- A named app and task, or a specific selected flow: call `show_flow`. Use the returned canonical path for exact follow-ups.
- A screen pattern such as login or order review: call `find_screens`. Set `app` when the user names an app; omit it for references across apps.
- A UI element such as a sticky button or tab bar: call `search_elements`. Set `app` when requested; omit it for references across apps.
- Which apps are covered: call `list_apps`.

A request to browse ten flows is complete when the gallery contains the matching results. Do not enumerate apps and search each one, or open every result individually. Describe missing coverage without quoting a total. For comparisons, retrieve only the selected flows needed to support the analysis.

## Keep browsing continuous

Each request gets its own focused result card: flow gallery, selected flow, screenshot references, elements in their original full screens, or apps. Search and refine through conversation, using the current selection and returned canonical paths for follow-ups. Do not tell the user to use a search box or global tabs inside a result: those controls are intentionally absent. Connected account and disconnect controls belong in the host's plugin settings.

For a general tour, show one requested capability at a time and explain a useful next prompt. Do not call every research tool in one burst: hosts may keep only the final view visible. Results load in small batches as the user scrolls toward the end of a continuous strip. The widget requests continuation itself; do not call `load_more` from chat or narrate pagination. Loaded cards and scroll position stay in place. A Load more button provides a keyboard and retry fallback. Do not show page numbers or result totals. Element results keep the full original screenshot and outline the relevant element; never describe these as cropped previews. A selected flow progressively renders its captured steps in an ordered horizontal strip, with images loaded as needed. Clicking a screenshot enlarges it in place. Its app, screen, element label or flow step becomes the context for follow-up questions. Use that selection to resolve “this element” or “this step”; verify the screenshot before making visual claims. An explicit Open in workspace control gives the same selection more room when supported; never claim expansion is available or occurred without evidence. Use a single appropriate tool for a specific requested view and do not replace it with a different view afterward.

Let the result card carry the screenshots and controls for inspecting that result. Accompany a browsing result with a brief sentence explaining the useful next action; avoid repeating the result as a Markdown image table or a list of website links. Keep browsing in the conversation card unless the user explicitly asks to open a website or another view.

If the user reports a stale or missing view, acknowledge it. Successful tool data alone does not prove the host rendered the UI. Do not repeatedly call the opener or present a localhost preview as the installed plugin. Provide a text fallback only when useful and identify it as a fallback.

## Research from the evidence

For analysis, distinguish what the captured screens show from design recommendations. Cite the returned app, flow, and step; use a returned source link when it is useful to the research. Do not infer conversion rates, unseen steps, or behavior that the captures do not establish.

Respect the account's available screens. If access is limited, say once that the locked screens are part of Flownato Premium, use the available evidence, and do not invent their contents or promote a purchase. If a tool says today's free allowance is used up, say so and when it resets; do not suggest upgrading or mention prices. Follow the host's connection flow when sign-in is required.

## Keep library size out of the experience

Never display or announce counts of apps, flows, screenshots, elements, patterns, categories or examples, including result totals, per-app flow totals and “N+” or “over N” claims. Counts in tool data are internal metadata for pagination and coverage, not user-facing copy. Name relevant apps and flows instead. Individual step labels may identify where to navigate. The catalog is live; use current tool results rather than a memorized inventory or a fixed library size.
