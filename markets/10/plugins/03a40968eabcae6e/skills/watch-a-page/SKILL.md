---
name: watch-a-page
description: Create a monity.ai monitor that alerts on what the user cares about, without duplicates, and show the evidence once the first check has run.
---

# Watch a page well

Use when the user asks to monitor, track, watch or be alerted about a web page.

- **Check first.** Call `list_monitors` (filtering by what you know) and look for the same address. Reuse an existing monitor rather than creating a second one; if the user wants a different condition on the same page, use `update_monitor`.
- **Say what matters.** Put the user's condition in `notifyWhen` in their own words ("price drops below £40", "a new role in Berlin appears", "the cancellation clause changes"). Without one, every meaningful change alerts.
- **Numbers and thresholds.** When the user needs exact thresholds without AI judgement, use `notifyConditions` with `outputExtractor` (or `jsonPath` for JSON endpoints) as the tool describes.
- **Frequency.** Match the page: stock and prices every few hours, listings and news daily, legal and policy pages daily or weekly. Only offer frequencies `get_account` lists as allowed, and check it has a monitor slot left in the workspace before creating. State the choice.
- **One element.** Pass a CSS `selector` only when you know it exists on the page (the user gave it, or you have seen the page's markup); the rest of the page is then ignored. Never guess one: a selector that is not on the page makes every check fail. Otherwise describe the part in `notifyWhen` ("the price of the 2 TB model") and let monity.ai watch the page.
- **Workspace.** On accounts with several workspaces, ask where the monitor belongs before creating it.
- **After creating.** The saved card shows where alerts go, what the schedule costs in credits and, once it completes, the first check: tell the user those in a sentence and do not open the check again yourself. When the user asks about the result later, use `get_latest_result` (its card is the check; do not also call `get_check` for it); for older checks use `get_check_history` then `get_check` once.
- **Pages behind a login, cookie walls that need decisions, or multi-step flows** are set up in the monity.ai dashboard; never ask the user for passwords, cookies or codes in chat.
- **Blocked checks.** When a check's `pageAccess.reachedContent` is false, it saw a captcha, login or error page: tell the user the site blocked that check rather than describing a change.
- Describe changes from the evidence monity.ai returns. If there is no completed check yet, say when the next one is due rather than guessing.
