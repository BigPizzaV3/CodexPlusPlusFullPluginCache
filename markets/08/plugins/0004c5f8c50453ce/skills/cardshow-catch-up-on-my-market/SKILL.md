---
name: cardshow-catch-up-on-my-market
description: Brief a signed-in collector on saved upcoming shows, followed-shop and seller activity, current CardShow plans, and shop alert choices. Use when a user asks what changed, what is coming up, what they missed, what needs attention, or wants to follow one shop, save one show, or adjust CardShow shop alerts.
---

# Catch up on the collector's CardShow market

Summarize only the signed-in collector's current CardShow relationships and time-sensitive activity. Do not turn a chronological feed into noise.

## Build the briefing

1. Call `cardshow_get_my_alerts` for saved upcoming shows, followed activity, current shop alert choices, and the delivery notice.
2. Call `cardshow_get_my_planning` when private plans, saved or followed IDs, or next actions are relevant.
3. Group the result into:
   - saved shows approaching soon;
   - meaningful new shop or seller activity;
   - plans that still need preparation; and
   - alert choices that may not match the user's stated intent.
4. Prioritize by actual date and relevance. Do not promote the first returned record merely because of response order.
5. Distinguish public business activity from the collector's private saved, followed, plan, and alert state.

Do not expose location history, another collector's activity, push tokens, or delivery logs. Do not claim an alert was delivered. CardShow alert choices still depend on notification permission on the customer's device.

## Prepare one relationship change

When the user asks to follow a shop, save a show, or change alerts:

1. Resolve one exact shop or show with `search`, `fetch`, or a current CardShow read.
2. Refresh planning and alerts before previewing the change.
3. State the exact target and desired final state. Never use a blind toggle.
4. For alerts, list only the choices that will change and state that omitted choices will be preserved.
5. If the shop is not followed, preview the exact follow and alert effects together; apply the follow first, refresh alerts, then apply only the confirmed alert merge.

## Confirm and verify

Ask for explicit confirmation immediately before each listed final-state action. Then use only the matching tool:

- `cardshow_set_shop_follow`;
- `cardshow_set_saved_show`; or
- `cardshow_set_shop_alert_preferences`.

Re-read alerts or planning after the action and report the final state plus the device-permission limitation. Refuse bulk follow, save, attendance, or alert changes that bypass exact targets and confirmation.
