---
name: capture-product-ui
description: Capture a live product page or app screen into a Wevi scene. Open the page in Wevi's browser, move to the right view one step at a time, let the user sign in themselves, pick the components the template's frames are made for, and re-pick when the choice looks wrong. Use when a scene's template needs real UI (requiresUiCapture or scenesNeedingCapture), when the user wants their dashboard, table, chart, form or editor in the video, or when a capture came out wrong.
---

# Capture product UI into a scene

How it works: the page is opened in a real browser, every visible element is measured and listed as a candidate; the chosen elements are cut onto their own layer and the background is recaptured with them hidden, so the animation moves a clean component over an intact page. Framing is automatic: the view zooms and scrolls so the components fill about 60% of the frame, sticky bars and cookie banners are hidden. Use `frame: "current"` to keep the view exactly as browsed, `"full"` for the top of the page.

## Procedure per capture scene

1. Know what the scene must show: its narration plus the template's `slots.guide` and `slots.prefer` (the template's own rubric, with the author's notes in `slots.smartGuide`). When present, `slots.frameShape` is the width over height its frames show whole and `slots.frameSize` how large a frame shows a component, in the page's own pixels: pick pieces near that shape and no smaller than about half that size, or they are cut or blown up.
2. Public page and the shot is near the top: call `wevi_capture_scene` with `url` and `focus` keywords.
3. Otherwise `wevi_open_page`, read the outline, reach the right view, then `wevi_capture_scene` with the `sessionId`.
4. If the pick looks wrong in the numbered screenshot, choose by number or id with `wevi_select_capture`. Re-picking is free. Unsure up front? Call `wevi_capture_scene` with `autoSelect: false` to get the candidates and the numbered screenshot first.
5. `wevi_close_page` when the site is done.

## Moving around the page

One step at a time, reading the outline after each: `wevi_go_to` (one of the app's own routes from the outline: dashboard, reports, settings), `wevi_click` (pass `opensMenu: true` when the click opens a dropdown or menu that must stay open for the capture), `wevi_type`, `wevi_scroll`, `wevi_hover`, `wevi_wait`, `wevi_press_key` (Escape dismisses a popover), `wevi_go_back`. Template notes written for the editor translate directly: "navigate to a page that shows X" means a better url or `wevi_go_to`; "click a component" means choose it by focus keyword, selector or number; "keep popovers off the text" means dismiss it first.

## Picking well

- Choose cards, buttons, inputs, charts or media that carry the scene's message. Avoid full-width sections and paragraphs unless the template is a text template (then pick a headline first).
- Thin page? Stay on the product's own domain and look further: first `wevi_scroll` the same page (the best cards, tables and widgets are often below the fold; the outline's sections say where), then try another page of the same site (pricing, features, docs, a dashboard view) with `wevi_go_to`. Never switch to another domain for the product's UI.
- Capturing fewer than the template's maximum slots is fine; fewer than its minimum is not, and a weak pick is worse than scrolling or a second page.
- `fullPageBackground` templates take the whole page and need no picks. A screenshot the user shares at a public URL can fill them through `wevi_capture_from_image`; element templates still need the live page.

## Private apps

Every outline carries `authWall` and `loginUrl`. When `authWall.detected` is true, or `wevi_capture_scene` returns `loginRequired`, send the user `loginUrl` so they sign in themselves in that same browser (SSO and 2FA work), then call `wevi_wait_for_login` with the `sessionId`: it returns when they confirm or the sign-in screen goes away, with the signed-in page's outline and routes. Then `wevi_go_to` the route the scene needs and capture there. Never ask for a password and never type one. A sign-in screen never costs a credit.

## Guardrails

Steps that look like payments, purchases, deletions or account changes are refused; 150 steps per session; only http(s) pages. Browser time is free for the first 5 minutes of a session, then costs 1 credit per started 5 minutes, so close sessions when done.
