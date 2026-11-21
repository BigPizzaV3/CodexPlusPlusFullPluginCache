# Troubleshoot a screen

Start every "blank / offline / wrong content" report with:

1. `optisigns_screen_search(query)` → the screen (status `online|hdmiOff|offline|unknown`, `lastSeenAt`).
2. `optisigns_screen_diagnose(screenId)`.

Diagnose reads what OptiSigns last stored; it does not contact the device. Mention `evaluatedAt` if the
user just changed something ("as of 2 minutes ago…"). Fields: `checks.online`, `checks.content`,
`checks.storage`, `checks.opsSchedule`, `onHold`, `reachability` (online|display_off|offline|unknown),
`remoteSessionPossible`, `deviceTimezone`, `screen` (id, name, model, platform, os).

Walk the tree top to bottom; report the first failing check, then any others.

## 1. `onHold: true`

The screen is in the account's **OnHold** folder: it has no license slot, so it won't play content. This
happens when a screen is paired with no free license, or someone put it on hold. Tell the user plainly:
free up or add a license, then move the screen out of OnHold in the OptiSigns portal. Billing questions go
to Support (support@optisigns.com). Don't guess at billing reasons.

## 2. `checks.online.pass: false`, by `reason`

**HDMI_OFF**: the player is running but the display is off or on another input.
- Check the TV is on and set to the input the player is plugged into.
- Reseat the HDMI cable at both ends; try another HDMI port.
- If the TV turns itself off on a timer, check its power-saving or sleep settings.

**OFFLINE**: the player stopped reporting in. Use `lastSeenAt` to say since when.
- Check the player has power (light on) and the TV shows something.
- Check the network: Wi-Fi or Ethernet connected, internet working at the site.
- Restart the player (unplug for 10 seconds, plug back in).
- Content already downloaded keeps playing offline; new changes arrive when it reconnects.

**NEVER_CONNECTED**: the screen was added but has never reported in.
- Check the OptiSigns app is installed and open on the player and it has internet.
- If the screen still shows a pairing code, pair it (`optisigns_screen_pair`) or re-pair it in the portal.

**CACHE_UNAVAILABLE**, or `inconclusive: true`: OptiSigns couldn't read the status right now. Not a
fault. Try diagnose again in a minute; if it repeats, ask what the screen physically shows.

## 3. `checks.content`

- **`NOT_ASSIGNED`**: nothing is assigned. Offer to assign content ([assign-and-conflicts.md](assign-and-conflicts.md)).
- **Pass** only means something is assigned. If the screen shows the wrong thing or blank:
  - `contentType` tells you asset, playlist or schedule.
  - Playlist: `optisigns_playlist_get`, check items are ready (`optisigns_asset_get` → `ready`) and
    not deleted (`missing: true`).
  - Schedule: `optisigns_schedule_item_list` for today; check an item covers the current local time
    (`deviceTimezone`). A gap outside the dayparts shows the schedule's default content, set in the portal
    ([scheduling-rrule.md](scheduling-rrule.md)).
  - Web asset blank: the page may refuse to load inside other sites or need a sign-in; suggest a built-in
    app or a file version.

## 4. `checks.storage.pass: false` (≥ 90 % used)

The player is nearly full, so new content may not download. Suggest removing unused content from what
this screen plays (fewer or shorter videos), then restarting the player. `storage: null` means the player
never reported it; skip.

## 5. `checks.opsSchedule`

- **`state: OFF`**: the screen is outside its operating hours, so it is meant to be off. Give
  `nextChangeAt` in the screen's local time ("it turns back on at 7:00 am"). The hours are set in the
  portal.
- `UNKNOWN` with `unknownReason`:
  - `INHERITED`: follows the account or team default hours, not checked here. Not a fault.
  - `NOT_EVALUABLE`: the hours have no timezone or usable times, or couldn't be read; try again later.
  - `SCHEDULE_NOT_FOUND`: the operating-hours schedule it points to is missing; fix it in the portal.
- `opsSchedule: null`: operating hours are off for this screen.

## 6. All checks pass but the user still sees a problem

Ask what they see (photo, error text, which content). Then point to the right article and offer Support.

## Wording

- Lead with the likely cause in one line, then up to five steps, then a next action.
- Translate fields: "OptiSigns last heard from it 3 hours ago", not `lastSeenAt`.
- Device-specific steps: find the matching article in
  [kb-troubleshooting.md](kb-troubleshooting.md) and link it. Anything you can't ground, or a hardware
  fault: OptiSigns Support, support@optisigns.com or https://support.optisigns.com.
