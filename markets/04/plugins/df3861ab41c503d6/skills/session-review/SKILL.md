---
name: session-review
description: Use when diagnosing user-reported issues, investigating bugs, analyzing user behavior, or validating UI correctness using Fullstory session recordings.
---

# Session Review

Review Fullstory sessions to understand what happened — whether diagnosing a customer-reported bug or validating UI changes during development.

## When to Use

- User reports a bug and provides a session URL
- Investigating an error or unexpected behavior
- Understanding user flow through the application
- Debugging issues that are hard to reproduce
- Validating UI changes locally after testing

## MCP Tools

The tools follow this pattern:

```
fullstory:session_open  →  (fullstory:session_screenshot | fullstory:session_get_a11y_tree | fullstory:session_diff)*  →  fullstory:session_close
```

1. **`fullstory:session_open`**: Pass `session_id`. Returns event summaries and a `client_id`. The `session_id` accepts a bare id (`<device-id>:<session-id>`), a full session URL, or a short link.
2. **`fullstory:session_screenshot`**: Rendered screenshot at a timestamp. Pass `client_id`, `page_id`, `timestamp` (ms from session start); optional `full_page` for the whole scrollable page. Sequential calls with increasing timestamps are faster.
3. **`fullstory:session_get_a11y_tree`**: Page structure (accessibility tree / DOM) at a timestamp. Pass `client_id`, `page_id`, `timestamp`.
4. **`fullstory:session_diff`**: Highlights changes between two timestamps within a page. Pass `client_id`, `page_id`, `from_ts`, `to_ts`.
5. **`fullstory:session_close`**: Always call when done to free resources. Pass `client_id`.

`session_view` is deprecated and removed — it was split into `session_screenshot` (the rendered image) and `session_get_a11y_tree` (page structure). Use those two instead.

## Workflow

### 1. Open the Session
```
fullstory:session_open(session_id="https://app.fullstory.com/ui/<org-id>/session/<device-id>:<session-id>")
```
Returns: event summaries (navigation, clicks, errors, custom events) and `client_id`. You can also pass a bare `<device-id>:<session-id>` id or a short link as `session_id`.

### 2. Identify Key Moments
Scan event summaries for:
- **Page navigations** — entry points into different views
- **Click events** — user interactions with buttons, links, forms
- **Error events** — console errors, network failures, renderer errors
- **Rage clicks / mouse thrash** — signs of UX friction
- **Custom events** — application-specific telemetry

Note the `page_id` and `timestamp` for each moment you want to inspect.

### 3. Visual Inspection
At each key moment, capture the screenshot — and the accessibility tree when you need the structure or text content:
```
fullstory:session_screenshot(client_id="<id>", page_id="<page>", timestamp=<ms>)
fullstory:session_get_a11y_tree(client_id="<id>", page_id="<page>", timestamp=<ms>)
```
Check for:
- Layout correctness (elements positioned properly)
- Content rendering (text, images, icons present)
- Responsive behavior (no overflow, proper sizing)
- Empty/loading states handled

### 4. Compare States
For before/after analysis:
```
fullstory:session_diff(client_id="<id>", page_id="<page>", from_ts=<before_ms>, to_ts=<after_ms>)
```
Returns a screenshot with changed regions highlighted plus a text summary of component changes.

### 5. Report Findings
Summarize what was observed:
- What the user saw at each key moment
- Any errors, visual regressions, or unexpected behavior
- Root cause analysis if diagnosing a bug
- Confirmation of correctness if validating changes

### 6. Cleanup
Always close the session:
```
fullstory:session_close(client_id="<id>")
```

## Example

When a user reports "the checkout button didn't work" and provides a session URL:

1. Call `fullstory:session_open` with the session URL as `session_id`
2. Find the checkout-related events in the summaries (note the `page_id` and `timestamp`)
3. Use `fullstory:session_screenshot` — and `fullstory:session_get_a11y_tree` if you need the DOM — to see the UI state just before the button click
4. Use `fullstory:session_diff` to compare before/after the click attempt to see what changed (or didn't)
5. Report findings: what the user saw, any errors, why the action may have failed
6. Call `fullstory:session_close` to clean up

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Forgetting to close session | Always call `fullstory:session_close` — even on errors |
| Using `session_view` | Removed — use `fullstory:session_screenshot` + `fullstory:session_get_a11y_tree` |
| Random timestamp access | Use sequential increasing timestamps for faster access |
| Skipping the diff tool | `fullstory:session_diff` highlights changes automatically — faster than comparing two screenshots manually |
| Not checking for error events | Scan event summaries for errors before visual inspection |
