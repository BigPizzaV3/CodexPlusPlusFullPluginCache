---
name: investigate-friction
description: Step-by-step investigation of where and why visitors struggle on a site, from frustrated pages down to the exact element and the session replays that prove it. Use when the user asks about rage clicks, dead clicks, error clicks, broken buttons, confusing pages, or "where are users frustrated?".
---

# Investigating friction

Work from broad to specific, and stop as soon as the user's question is answered. Each step narrows the evidence.

## 1. Find the pages

`compare_pages_by_frustration` ranks every page by one signal:
- `rageClicks`: repeated fast clicks, usually something that looks clickable but doesn't respond, or is slow.
- `deadClicks`: clicks that change nothing, often on non-interactive text or images that look like links.
- `errorClicks`: clicks followed by a JavaScript error, usually a real bug.

If the user didn't name a signal, start with rage clicks and mention the other two. Judge a page by **affected sessions relative to page views**, not raw clicks: 200 rage clicks from one session is one frustrated visitor, not a site-wide problem. Say when that's the case.

## 2. Find the element

For the page that matters, call `get_page_heatmap` with `type: "clicks"`. It lists elements ranked by frustration, with the visible text and a selector. Name elements by their visible text ("the 'Apply coupon' button"), not by selector.

To see how far people read or where the mouse goes, use `type: "scroll"` or `type: "movement"`.

## 3. Get the proof

`get_element_interactions` with the element's selector returns how many sessions interacted with it and the **sessions where it frustrated users**, with replay links. Offer 2–3 replays as evidence.

For a broader view, `search_sessions` with filters such as `hasRageClicks`, `hasDeadClicks`, `hasErrorClicks`, `hasJsErrors` or `hasNetworkErrors` finds sessions with those signals across the site.

## 4. Explain what happened

Use `get_session` on one representative session to read its timeline (clicks, errors, network failures, idle time) and explain in plain words what the visitor tried to do and what went wrong.

## 5. Suggest a fix

Tie the suggestion to the evidence:
- Dead clicks on text or images → make them clickable, or stop styling them like links.
- Rage clicks on a real button → check that it responds and shows loading state; look for slow network calls in the session.
- Error clicks or JS errors → name the error message and page so a developer can reproduce it.
- Form abandonment → `get_form_analytics` for completion rates.

Quantify the impact ("affects about 12% of sessions on /checkout") and suggest watching the replays before changing anything.

## Notes

- Device matters: if a problem looks mobile-only, check with `get_page_heatmap`'s `device` filter or `get_breakdown` by device.
- If nothing stands out, say so. Low frustration is a valid answer.
