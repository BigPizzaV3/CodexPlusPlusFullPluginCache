---
name: qr-analytics-report
description: Report how CodeQR QR codes and short links are performing - scan and click counts, trend over time, top cities, devices and referrers, and which codes lead. Triggers on how many scans, how many clicks, which cities, best performing, or any request for a campaign report. Not for creating or editing codes, and not for conversion or revenue reporting.
---

# Scan and click reports

Answer performance questions from recorded CodeQR data through `get_analytics`.
Never estimate, extrapolate, or fill a gap with a plausible number.

## The two parameters that are always required

`get_analytics` requires **both** `event` and `groupBy` on every call. Omitting
either one fails the call.

### `event` — pick by resource type, not by phrasing

| Resource | `event` |
|---|---|
| QR code | `scans` |
| Short link | `clicks` |

This is the trap in this workflow. Asking for `clicks` on a QR code does not
error — it returns a well-formed response with nothing in it, which reads exactly
like a code nobody scanned. If a result comes back empty, check that the event
type matches the resource before reporting zero.

`leads`, `sales` and `composite` also exist, but conversion reporting is out of
scope for this skill.

### `groupBy` — shape of the answer

Valid values: `count`, `timeseries`, `countries`, `cities`, `devices`,
`browsers`, `os`, `referers`, `top_links`, `top_qrcodes`, `top_urls`.

Do not pass `clicks`, `scans` or `views` as a `groupBy`. The upstream API accepts
them and currently answers 500, so they are not offered here.

## Scoping and window

- One QR code: `qrcodeId`. One link: `linkId`. Either can also be reached with
  `domain` plus `key`.
- Omit all of them for the whole workspace.
- `interval` accepts `1h`, `24h`, `7d`, `30d`, `90d`, `ytd`, `1y` and `all`. It
  defaults to `24h`, which is short enough to look like a dead code if the user
  meant "ever" — so pass it explicitly whenever the question implies a window.
- Map the user's words to the closest of those and **say which window you used**.
  "This year" is `ytd`, not `90d`. "Ever" or "in total" is `all`.

### Long windows depend on the plan

The API refuses windows above the workspace's plan limit with a 403. It is not
an empty result and not a permissions error the user can fix by re-authorizing:

| Plan | Longest window | Refused |
|---|---|---|
| free | 30 days | `90d`, `ytd`, `1y`, `all` |
| starter | 90 days | `ytd`, `1y`, `all` |
| pro | 1 year | `all` |
| business and above | no limit | — |

`get_workspace` returns the plan. Call it once before a report that needs a long
window, rather than discovering the limit through a rejection.

When the plan blocks the window the user asked for, report the longest one
available, say which plan limit applied, and let them decide — do not silently
substitute a shorter window and present the number as the answer to what they
asked.

## Build the report in this order

1. **Headline** — `groupBy: "count"` for the total over the window.
2. **Trend** — `groupBy: "timeseries"` only when the user asks how it is moving,
   or when the answer is about growth or decline.
3. **One or two breakdowns** — `cities` or `countries` for where, `devices` or
   `os` for how, `referers` for where the traffic came from.
4. **Ranking across codes** — `top_qrcodes` for scans, `top_links` for clicks.

Each of these is a separate call. Run only the ones the question needs: four
breakdowns nobody asked for buries the answer instead of supporting it.

## Reporting rules

- Lead with the number the user asked for, then the context.
- Always state the window and the scope alongside the number. "1,240 scans" on
  its own is not an answer; "1,240 scans in the last 30 days, for the menu QR
  code" is.
- If a query returns empty, report it as no recorded data for that window and
  scope. Do not present it as zero performance without checking the `event` type
  first, and never substitute a made-up figure.
- Scans and clicks are recorded per code with time, country, city and device.
  Personal identity is not part of this data, so do not describe results as
  individual people.
