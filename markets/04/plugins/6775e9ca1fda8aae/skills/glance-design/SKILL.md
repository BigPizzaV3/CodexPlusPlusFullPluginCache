---
name: glance-design
description: Design native iOS Home Screen widgets in Glance layout language. Apple-like, glanceable. Use registry types only — chart with variant, never bar_chart or webview.
---

# Glance Widget Design Skill

You design **iOS home screen widgets** that feel native, calm, and glanceable — like Apple built them. This skill covers **visual design and composition only**. Workflow, tools, integrations, and sizing math live in the main agent skill.

**Diversity over templates:** Every widget should fit its data and the user's intent. These are principles and patterns — not a single layout to copy. Vary structure, density, and emphasis. Never force one recipe when another fits better.

---

## Design north star

Widgets should feel like **Apple system UI**: clear hierarchy, generous whitespace, restrained color, SF typography. A user glancing at their home screen should read the widget in under two seconds.

| Trait | What it means in practice |
|---|---|
| **Glanceable** | One clear takeaway — a number, status, or headline |
| **Native** | System fonts, semantic colors, no "web app" density |
| **Calm** | Mostly neutral surfaces; color carries meaning, not decoration |
| **Intentional** | Every element earns its space — if it doesn't help, remove it |

---

## Color — Apple-native default, user-guided override

### Default (no user color preference)

Think **Settings / Stocks / Weather** — not marketing landing pages.

| Role | Guidance |
|---|---|
| **Background** | Omit `background` on root for system adaptive fill, or `#FFFFFF` / `#F2F2F7` (light) — never loud gradients unless the user asks |
| **Primary text** | `#000000` or omit `color` (system primary) |
| **Secondary / labels** | `#8E8E93` (iOS secondary label) — captions, timestamps, units |
| **Tertiary / hints** | `#AEAEB2` — de-emphasized metadata only |
| **Accent** | **One** semantic accent per widget — e.g. `#007AFF` (system blue) for links/active, `#34C759` success, `#FF9500` warning, `#FF3B30` alert |
| **Progress / fills** | Muted track `#E5E5EA`, fill = single accent |

**Rules:**
- Never use more than **one accent hue** unless the user requests a colorful or branded look.
- Never fill large areas with saturated color — accents belong on small elements (badge, progress fill, status dot, one headline word).
- Prefer **opacity and weight** over more colors to create hierarchy.

### iOS color format (critical on device)

The iOS renderer only parses **6-digit hex** (`#RRGGBB`). Values like `#FFFFFFCC` or `#FFFFFF40` are **ignored** and fall back to system `.primary` (often black on light widgets).

- Use solid 6-digit hex for every `color`, `background`, `backgroundColor`, `trackColor`, `fillColor`.
- For muted/secondary text on dark or gradient backgrounds, pick a lighter solid tint (e.g. `#FFE8F5` on purple gradients) — not alpha suffixes.
- On colorful widgets, desaturated label colors still beat 8-char hex.

### When the user gives color direction

**Follow the user.** If they say "dark purple theme", "brand pink #E91E8C", or "match my logo colors" — apply their palette to backgrounds, accents, and text while keeping hierarchy and readability. Still use muted variants for labels (`#8E8E93` or a desaturated version of their accent).

If they share no preference, use the Apple-native defaults above.

---

## Typography

Use **SF Pro** (`sf-pro` or omit `fontFamily`). Reserve `sf-rounded` for playful/countdown widgets; `sf-mono` for code/GitHub hashes only.

| Role | fontSize | fontWeight | color |
|---|---|---|---|
| **Hero value** | 24–32 | `bold` or `heavy` | primary |
| **Section title** | 15–17 | `semibold` | primary |
| **Body / detail** | 13–15 | `regular` or `medium` | primary or secondary |
| **Caption / label** | 10–12 | `regular` or `medium` | `#8E8E93` |
| **Unit / suffix** | 11–13 | `medium` | secondary — on `stat` via `suffix` |

**Limits:** At most **3 distinct font sizes** per widget. At most **2 weights** in active use (e.g. semibold + regular).

Always set `maxLines: 1` on titles and hero lines in `small` and `medium` widgets. Use `maxLines: 2` sparingly on `large` only when content demands it.

---

## Spacing rhythm

Pick one rhythm and stick to it for the whole tree:

| Token | Use |
|---|---|
| **8 pt** | Tight gaps inside a row (icon + label) |
| **12 pt** | Root `padding`, default `spacing` within sections |
| **16 pt** | Between major sections on `large` widgets |

Root container: **`padding: 12`** minimum (16 for airy large layouts). Never mix 6 / 10 / 14 randomly.

Use `spacer` with `flex: 1` to push footer elements (badge, timestamp) to the bottom on `large` — don't stack everything at the top.

---

## Visual hierarchy — the one-hero rule

Every widget needs **one focal point**:

| Size | Typical hero |
|---|---|
| `small` | One `stat` value, one large number `text`, or one `avatar` + short label |
| `medium` | Hero left or top + supporting detail opposite/below |
| `large` | Hero row + 2–4 supporting metrics or a content block |

Everything else is **supporting** — smaller, lighter color, fewer lines.

**Do not** give equal visual weight to five text lines. If everything is bold and 16 pt, nothing is important.

---

## Static vs dynamic bindings

Only `{{variable_name}}` becomes a **content field** (upload form, automation ingest, `bindings_required`).

| Use case | Template syntax | In derived schema? |
|---|---|---|
| Live data (username, KPI value, event title) | `"binding": "{{username}}"` | Yes |
| Fixed section label ("Profile views today") | `"binding": "Profile views today"` | No |
| Fixed metric name under a ring ("Revenue") | `"binding": "Revenue"` | No |
| Decorative brand icon (design constant) | `"binding": "https://…/icon.png"` on `image` | No |
| SF Symbol | `"binding": "bag.fill"` on `icon` | No |
| Progress-dependent caption | `"binding": "{{overall_goal_caption}}"` | Yes |

**Rule:** If the copy or asset never changes per refresh, use a **plain literal** — not `{{}}`. This keeps the upload flow clean and matches how the goldens are authored.

**Static images on device:** use **HTTPS PNG/JPEG** URLs. Local paths like `/brand-icons/…` only work in React preview.

---

## Golden reference library

Six device-approved examples live in `packages/sdk/goldens/`. They are the **quality bar** — adapt their structure to the user's data; never paste one verbatim with wrong bindings.

**Before designing:** call `list_golden_examples` (filter by `widget_size` or fetch one with `example_id`).

| ID | Size | Pattern | When to adapt |
|---|---|---|---|
| **s1-glance-kpi** | small | Gradient + username + 2 stacked KPI stats + static brand icon | Social/account KPIs, branded small metrics |
| **s2-glance-media** | small | White card: static section label → title → centered thumbnail → caption | Latest post/video/article thumbnails |
| **m1-split-strip** | medium | Left: static title stack · Right: hero `stat` | Single headline metric strips (monitoring, uptime) |
| **m2-multi-source** | medium | Left motion panel + right spend card + calendar event rows | Multi-integration dashboards (device + cloud) |
| **l1-app-performance** | large | Dark 2×2 KPI rings (`z-stack` + `circular_progress`) + quarterly `progress_bar` | Custom business metrics with goal progress |
| **l2-outfit-of-the-day** | large | Gradient + hero image + shoppable item rows (`href` + `icon`) | Creator commerce, product lists, playful layouts |

Language v2 references (same folder, `v2-` prefix). Load with `example_id`. Free users may use agenda. Pro+ goldens need `get_plan` family flags first.

| ID | Size | Plan | When to adapt |
|---|---|---|---|
| **v2-vocab-flip** | small | Pro+ views | In-place reveal — whole-card `toggle_flag` + `visibleFlag`, no `views` |
| **v2-today-agenda** | small | Free | Next few events as a list — `calendar` `agenda` + `event[]` |
| **v2-revenue-line** | medium | Pro+ charts | Today's total + cumulative hours — `chart` `line`, `showAxes: true` |
| **v2-weekday-bar** | medium | Pro+ charts | 7-day counts — `chart` `bar`, `showAxes`, `showAverage`, `colorScale` |
| **v2-share-pie** | small | Pro+ charts | Parts of a whole (≤ 8) — `chart` `pie` + `innerRadius` |
| **v2-activity-grid** | medium | Pro+ grid | Heat over days/weeks — `grid` `activity` + `colorScale` |
| **v2-standings-table** | medium | Pro+ table | Compact labeled numbers — `table` 3×3-ish, never 5 columns |
| **v2-mission-control** | large | Pro+ views + charts | Four-page hub — home summary + bottom nav `Home \| Dashboard \| Mail \| Calendar` |

### Golden techniques worth copying

- **S1:** `gradient` root; static caption literals above dynamic `stat` values; trailing brand `image` with static URL
- **S2:** explicit `spacer` gaps between title/image/caption; `maxLines` on all text; white `#FFFFFF` root background
- **M1:** horizontal split with `flex: 1` text column + trailing hero `stat` (`valueFontSize: 40`)
- **M2:** nested gray cards (`#F2F2F7`); color accent bars beside calendar rows; formatted strings in `text` not `stat`
- **L1:** ring container **82×82** with `circular_progress` **size 70, lineWidth 5** (prevents stroke clip); value text centered in `z-stack`; `overall_goal_caption` stays dynamic
- **L2:** `gradient` with `spacing` as gap; `fillContainer` hero image; `href` on shop tap targets; `sf-rounded` for playful headers
- **v2-vocab-flip:** whole-card `toggle_flag` + `visibleFlag`; prompt stays; answer appears on the same screen; no `views`; reload clears the flag
- **v2-revenue-line:** horizontal split, no divider; copy + insight + `relative_time` on the left; full-height `chart` `line` `showAxes: true` on the right
- **v2-weekday-bar:** same split on light `#F2F2F7`; copy + 7-day average on the left; full-height `chart` `bar` with axes, `showAverage`, and `colorScale` bands (red < 10, yellow < 20, green 20+)
- **v2-mission-control:** Notion monochrome (`#FFFFFF` / `#37352F` / `#9B9A97`). Home is greeting + KPIs + unread mail + agenda. Duplicate a 4-tab bottom nav on `tree` and every named view; selected tab is ink, the rest muted. Named views: `dashboard` (today's revenue — full-width cumulative line, hourly bars beside App / Webapp / B2B mix), `mail` (3 summaries), `calendar` (`columns` `days: 3`). Discover stays on home — home must read as a full widget.

---

## Size patterns (adapt — do not copy blindly)

Prefer picking a **golden reference** above, then adapt. These ASCII sketches are fallbacks when no golden fits:

### Small (170×170) — "one glance"

Best for: single KPI, countdown, status, one image thumbnail.

```
vertical container, padding 12, spacing 8
  → caption text (12pt, secondary, maxLines 1)     // label
  → stat OR large text (hero, 26–30pt)             // THE number/word
  → optional: badge OR relative_time (11pt)        // context
```

Avoid: horizontal rows of 3+ items, multiple stats, long paragraphs.

### Medium (364×170) — "headline strip"

Best for: integration dashboard, social snapshot, calendar next event.

**Pattern A — split row:**
```
vertical, padding 12
  → horizontal row, spacing 12, alignment center
      → left column (vertical): title + subtitle
      → right: stat OR circular_progress OR avatar/image
```

**Pattern B — title + detail row:**
```
vertical, padding 12, spacing 8
  → title text (15pt semibold, maxLines 1)
  → horizontal row: 2–3 compact stats OR image + text pair
```

Avoid: more than one horizontal band; cramming 4 columns.

### Large (364×382) — "dashboard card"

Best for: multi-metric boards, feed digests, rich integration views.

```
vertical, padding 12–16, spacing 12
  → header row (horizontal): title + optional badge
  → main content: 2–3 stats in a row OR 2×2 grid of images/metrics
  → spacer (flex 1)                                    // optional
  → footer: progress_bar OR relative_time OR caption   // optional
```

Use `divider` between header and body only when it clarifies — not by default.

---

## Component combinations that look polished

| Combo | When to use |
|---|---|
| `stat` + caption `text` above | KPI widgets (followers, revenue, streak) |
| `avatar` + vertical `text` stack in horizontal row | Social / account identity |
| `image` (cornerRadius 8) + `text` beside | Latest post, thumbnail + caption |
| `badge` (subtle bg `#E5E5EA`, text primary) | Status chips — "Live", "3 new" |
| `progress_bar` (height 6–8, muted track) | Goal completion — one per widget |
| `z-stack` + full-bleed `image` + `text` with light color | Event spotlight — use sparingly |
| `status_dot` + `text` | Health / server / pipeline status |
| `relative_time` or `date` in caption style | "Updated 2m ago" footer |
| `shape` circle + mapped `fillColor` | One number that should read as a state (score, health) |
| `calendar` agenda + caption | Today's events — do not rebuild event rows from `text` |
| `chart` line, `showAxes: false`, height 64–80 | Sparkline under a title on medium |
| `chart` pie + `innerRadius` 0.55 + caption | Donut KPI on small |
| `chart` bar, `showAxes: true`, `showAverage: true` | Category counts vs a typical day — dashed mean of `y` |
| `grid` 1×7 week strip | Habit / steps this week |
| `table` 3 cols × ≤ 4 rows | Standings, ranks, tiny scoreboard |
| Bottom nav `text` + `set_view` on every view | Mission Control — selected tab ink, others muted. Duplicate the bar; do not hide it. |
| Whole-card `toggle_flag` + `visibleFlag` on small | Vocab card — prompt stays, answer appears on the same screen |

**`stat` tips:** Use `valueFontSize` 26–32 for hero stats; `labelFontSize` 11; `suffix` for units (`K`, `%`, `°`). Prefer `ig_followers_fmt` style formatted strings in `text` when the integration provides them.

---

## Layout polish

- **Alignment:** `leading` for LTR text blocks; `center` for single hero in small; `trailing` for meta (time, badge) in header rows — but see reload button rule below.
- **Reload button:** Glance overlays a reload control in the **top-right** (~40×40 pt). Never put hero values or must-read text there; prefer leading clusters for top-band KPIs (label + value side-by-side).
- **Images:** Always set explicit `width` / `height`; `cornerRadius: 8–12` for photos; `contentMode: "fill"` for thumbnails.
- **Nested cards:** Inner `container` with `background: "#F2F2F7"`, `cornerRadius: 10`, `padding: 10` — sparingly, one level deep max.
- **Full bleed:** Only `gradient` root for dramatic widgets — and only when user wants flair or data suits it (event poster, media highlight).

---

## Anti-patterns — never ship these

| Anti-pattern | Why it fails |
|---|---|
| 5+ `text` nodes all 14 pt regular | No hierarchy — wallpaper of words |
| Rainbow hex on every element | Feels non-native, noisy |
| Horizontal row of 4 images on `small` | Guaranteed clip / crush |
| `stat` for currency (`$1,234`) or `%` strings | Type errors + ugly fallback |
| Root `padding: 0` or missing | Corner clip on home screen |
| Hero stat / spend in top-trailing corner | Hidden under reload button overlay |
| `gap`, `borderRadius`, `textAlign` style keys | Silently ignored — use correct keys from main skill |
| `{{}}` on fixed labels or decorative icons | Forces upload fields; use static literals instead |
| 8-char hex colors (`#RRGGBBAA`) | iOS ignores them — text falls back to black primary |
| `bar_chart` / `pie_chart` / `webview` / JS ternaries | Invalid. Use `type: "chart"` + `variant`, or a `stops` / `when` map |
| Chart or views on Free without checking `get_plan` | 403 at save. Offer agenda / v1 stand-in, or upgrade |
| Five equal tap targets on a small hub | No hero. One primary view, others supporting |
| Calendar rebuilt as `event_1_title` rows when they asked for a calendar | Use `calendar` + `event[]`. Indexed fields stay valid for v1 lists |
| Grid `rows`/`columns` as bindings | Those are **ints on the node**. `binding` is the `number[]` |
| Table `columns: 3` (a number) | Table `columns` must be `"{{headers}}"` (`string[]`) |
| Month calendar with event titles | Month is **dots only**. Use `agenda` or `columns` for titles |
| Discover / marketing tile that relies on `set_view` | Tiles stay on home. Views work on the subscriber Home Screen |

---

## Layout language v2 — exact authoring

v1 trees stay valid. Anything below sets `required_version: 2`. Do not invent types, CSS keys, or JavaScript in bindings.

**Call `get_plan` first.**

| Capability | Free | Pro+ |
|---|---|---|
| 19 v1 types, `shape`, mapping, `calendar` | Yes | Yes |
| `views` / `action` / `visibleFlag` (`family_views`) | No | Yes |
| `type: "chart"` (`family_charts`) | No | Yes |
| `type: "grid"` (`family_grid`) | No | Yes |
| `type: "table"` (`family_table`) | No | Yes |

`validate_template` never 403s — it returns `families_used`. `create_template` / `update_template` / `inline_ui` 403 `PREMIUM_FAMILY_REQUIRED` if a flag is false. Offer a Free stand-in (agenda, `stat`, or both sides of a card as text) or say they need Pro.

Power is **quotas**, not a third language. Do not variant-gate calendar.

### Mapping — closed functions of a number

Any node's `color` / `*Color` / `background` / `fillColor` / `opacity` / `visible` may be a **map object** instead of a hex or `{{binding}}`. No `{{n > 80 ? green : red}}`.

`from` must be the entire value `"{{number_field}}"`. Choose **exactly one** of `stops` or `when`.

**`stops`** — interpolate between points. Colors blend; numbers/opacity lerp. Never use `stops` on `visible`.

```json
"fillColor": {
  "from": "{{score}}",
  "stops": [
    { "at": 0, "value": "#FF3B30" },
    { "at": 20, "value": "#FFCC00" },
    { "at": 80, "value": "#34C759" }
  ]
}
```

**`when`** — first matching clause wins. One operator per clause: `lt` | `lte` | `gt` | `gte` | `eq`. Optional `else`.

```json
"visible": {
  "from": "{{count}}",
  "when": [{ "lt": 1, "value": false }],
  "else": true
}
```

`colorScale` on chart / grid / table is a map evaluated **per mark / cell** against that cell's number. Write `"from": "{{activity}}"` even though `activity` is a `number[]` — do not also bind `activity` as a scalar. Zero cells on a grid use `emptyColor`, not the scale.

Use mapping when the **look** should change with a number (tinted button, fading card, score ring). Prefer `when` for on/off and discrete bands; `stops` for a continuous wash. `from` must be a **number** field (`{{steps_today}}`, `{{score}}`) — never a formatted string (`{{steps_today_fmt}}`). Hex is 6-digit.

### `shape` — Free

`variant`: `circle` | `rectangle` | `capsule` | `line` | `triangle`. Optional `href` (or `action` on Pro+). No children.

| Style | Type | Control |
|---|---|---|
| `size` | number | Diameter / edge. **Wins over** `width` / `height` when set |
| `width` / `height` | number | Use when the shape is not square (`line`, wide capsule) |
| `fillColor` | hex, `{{color}}`, or map | Interior. **Ignored on `line`** |
| `strokeColor` | hex / map | Outline |
| `strokeWidth` | number | Outline thickness |
| `cornerRadius` | number | `rectangle` only |
| `opacity` | 0–1 or map | Whole shape |

Hero circle: `size` 64–80, centered, one caption. Status pip: `size` 10–14. Do not stack three shapes on small.

### `calendar` — Free

Consumes `event[]`. The node does **not** call EventKit itself. Bind `{{events}}` from `eventkit_calendar` (device, identity `field_mapping: {}`) or ingest. Google Calendar is still indexed strings — do not bind it to this node yet. `start` is ISO 8601; all-day may be `yyyy-MM-dd`. Omit `day` / `month` to use today / this month **on device**.

`variant`: `agenda` | `columns` | `month`.

| Variant | What it shows | When to pick |
|---|---|---|
| `agenda` | Start time (or "All day") + title. `end` is occupancy, not painted. | Default. Small/medium next-up |
| `columns` | Titles only in day columns. Node `days`: **1, 3, or 7** | Medium/large week strip |
| `month` | Month grid with **dots only** — no titles | Large "busy this month" |

| Style | Default intent |
|---|---|
| `width` / `height` | Fill remaining space; set `height` on medium (≈ 110) |
| `headerFontSize` / `headerColor` | Day / month chrome — caption scale, often `#8E8E93` or white on dark |
| `eventFontSize` / `eventColor` | Agenda / column titles |
| `dotColor` / `todayColor` / `gridColor` | Month marks and today |
| `maxEvents` | Agenda clip (e.g. 3 on small, 5 on medium) |
| `opacity` | Whole node |

Indexed `event_1_title` rows remain legal. Prefer `calendar` when they asked for a calendar.

### `chart` — Pro+ `family_charts`

`type` is always `"chart"`. **`bar_chart` and `pie_chart` are invalid.**

| `variant` | Required bindings | Optional | Cap |
|---|---|---|---|
| `bar` | `y` `number[]` | `x` `string[]` categories | 24 |
| `line` | `x` `number[]`, `y` `number[]` | — | 24 |
| `scatter` | `x` `number[]`, `y` `number[]` | `sizes` `number[]` | 24 |
| `candle` | `x`, `open`, `high`, `low`, `close` all `number[]` | — | 24 |
| `pie` | `y` `number[]`, `labels` `string[]` | — | **8** |

`x` on line / scatter / candle is numeric (unix, hour-of-day). ISO date **strings** in that array are accepted at ingest. Parallel arrays must be the same length (`SERIES_LENGTH_MISMATCH`).

| Style | Variants | Control |
|---|---|---|
| `width` / `height` | all | Medium sparkline height **64–80**. Set `size` on pie instead |
| `size` | pie | Diameter. Small donut ≈ 75 |
| `strokeColor` / `strokeWidth` | line, scatter | Accent stroke. Width 2 |
| `fillColor` | bar, area-ish line | Single series fill. Or `colorScale` per bar |
| `showAxes` | bar, line, scatter, candle | `false` = sparkline. `true` = plot plane (grid + Y ticks + X labels) so scale is readable |
| `showLabels` / `labelFontSize` / `labelColor` / `axisColor` | cartesian | X labels. Follows `showAxes` unless you set it. Keep both off on small |
| `orientation` | bar | `vertical` (default) or `horizontal` |
| `barGap` / `cornerRadius` | bar | Gap 3, radius 3 |
| `showValues` | bar | Rarely — clips on small |
| `colorScale` | bar | Map per bar value |
| `showAverage` / `averageColor` | bar | Dashed mean of the current `y` series. Default color `#636366`. Pair with `showAxes` |
| `showDots` / `dotSize` / `curve` | line | `curve`: `linear` \| `smooth` |
| `innerRadius` | pie | 0 = pie, `0.55` = donut |
| `colors` | pie | `string[]` of 6-digit hex. Default `#7B61FF` `#34C759` `#FF9500` `#FF3B30` `#007AFF` `#AF52DE` |
| `upColor` / `downColor` | candle | Default `#34C759` / `#FF3B30` |
| `opacity` | all | Whole mark |

**`showAverage` (bar only).** Set `"showAverage": true` when each bar should be judged against a typical day — weekday counts, new users, tickets. The renderer computes the arithmetic mean of the current `y` series and draws a dashed rule at that Y (or X if `orientation` is `"horizontal"`). It is not a second binding and not a second chart. Optional `"averageColor"` (default `#636366`). Pair with `showAxes: true` so the line sits on a readable scale. Line, pie, scatter, and candle ignore it. Do not fake this by stacking a `chart` `line` of constants on the bars — Y domains will not match. Web preview and iOS WidgetKit both paint it (Swift Charts `RuleMark` on device).

One chart is the hero. Do not put a chart and a large `stat` of equal weight on small. Candle / scatter belong on medium/large.

### `grid` — Pro+ `family_grid`

`variant` is `activity` (omit = activity). **`rows` and `columns` are positive ints on the node** — not bindings. `binding` is `number[]` of length `rows × columns`. Max **400** cells (7×52 fits; 7×53 does not). Row-major. No per-cell tap.

| Style | Default | Control |
|---|---|---|
| `width` / `height` | fill | Set `height` 72–96 on medium |
| `cellShape` | `square` | `square` \| `circle` \| `triangle` |
| `cellGap` | 2 | Keep 2. Larger gaps eat the canvas |
| `cellCornerRadius` | 2 | Squares only |
| `emptyColor` | `#EBEDF0` | Color for **0**. Dark themes: `#161B22` |
| `colorScale` | — | Map from the **same** series binding; each cell uses its own number |
| `opacity` | 1 | Whole grid |

Week strip: `"rows": 1, "columns": 7`. Year: `7 × 52`. GitHub-green stops are fine when the user wants that look; otherwise one accent hue.

### `table` — Pro+ `family_table`

| Field | Type | Required |
|---|---|---|
| `columns` | `{{binding}}` → `string[]` | Yes — headers |
| `cells` | `{{binding}}` → `string[]` | Yes — **row-major** |
| `rows` | `{{binding}}` → `string[]` | No — row headers |

`columns: 3` (a number) is a **grid** size, not a table. Hard cap **4 columns × 6 rows**. Numbers in `cells` coerce to string. Clip, no scroll.

Row count = `rows.length` if row headers exist, else `cells.length / columns.length` (must divide evenly).

| Style | Default | Control |
|---|---|---|
| `showColumnHeaders` | true | |
| `showRowHeaders` | true if `rows` bound | |
| `headerBackground` / `headerColor` | `#F3F4F6` / `#111827` | Chrome. Dark: `#1F2937` / `#F9FAFB` |
| `cellColor` / `cellFontSize` / `cellPadding` | `#111827` / 11 / 4 | Body type — caption scale |
| `gridColor` / `gridWidth` | `#E5E7EB` / 1 | Hairline only |
| `colorScale` | — | Heats a cell **if the string parses as a number** |
| `width` / `height` / `opacity` | fill | Clip inside the box |

3 columns × 3–4 rows on medium. Never five headers.

### Views and actions — Pro+ `family_views`

`family_views` is two patterns. Pick one per tap — do not mix them for the same interaction.

| Intent | Mechanism | Golden |
|---|---|---|
| Tap shows/hides content on the **same** screen | `toggle_flag` + `visibleFlag`. No `views` map. | **v2-vocab-flip** |
| Tap goes to **another** screen | `set_view` + `views` | **v2-mission-control** |

`tree` is **always home**. Optional sibling `views` is a map of slugs → trees. Max **4** named views. Slug: `^[a-z][a-z0-9_]{0,31}$`. Do not name a view `home`. Depth 8 / 80 nodes **per view**. 64 KiB for `{ tree, views }`.

**Screen swap**

```json
{
  "action": { "type": "set_view", "view": "dashboard" }
}
```

**In-place reveal** — flags default **false** (hidden). `visibleFlag` shows the node when that flag is true.

```json
{
  "action": { "type": "toggle_flag", "flag": "show_answer" }
}
```

```json
{
  "id": "answer",
  "type": "text",
  "binding": "{{answer}}",
  "visibleFlag": "show_answer"
}
```

**XOR:** a node may have `action` **or** `href`, never both (`ACTION_HREF_XOR`).

**Reload** (`RefreshWidgetIntent`) returns **home** and clears flags, with latest data. **Ingest keeps** the current view. Discover / marketing tiles stay on home — do not design a tile that only makes sense after a tap. Reveal goldens keep the prompt visible so Discover still reads.

In-place reveal is the small pattern: **v2-vocab-flip**. Prompt stays; answer appears on the same card. Named views on small feel cramped — prefer `toggle_flag`, or warn.

Hub pattern (large): **v2-mission-control**. Home (`tree`) is a summary — greeting, KPIs, unread mail, today's agenda — not an empty launchpad. Duplicate a 4-tab bottom nav (`Home` / `Dashboard` / `Mail` / `Calendar`) on home and every named view. Selected tab: ink `#37352F` semibold. Others: muted `#9B9A97`. Named views: `dashboard` (today's revenue: full-width cumulative line, then hourly bars + App / Webapp / B2B pie on one row), `mail` (fixed email rows — no `for_each`), `calendar` (`columns`, `days: 3`). `set_view` `"home"` returns home. Reload also returns home. Discover tiles stay on home.

### Series bindings in content

POST the arrays the tree asked for. Extra keys 400.

```json
{
  "prompt": "ventana",
  "answer": "window",
  "events": [{ "start": "2026-08-30T09:00:00", "title": "Standup" }],
  "hours": [9, 10, 11],
  "revenue": [12, 18, 15],
  "activity": [0, 1, 3, 0, 2, 4, 1],
  "headers": ["W", "L", "Pct"],
  "stats": ["12", "4", ".750"]
}
```

---

## Design process (before you write JSON)

1. **Clarify intent** — glance KPI? digest? status? media? trend? heat? reveal on the same screen? flip between screens?
2. **`get_plan`** — if they asked for charts / views / grid / table and the family is false, say so and offer a Free stand-in or upgrade. Do not emit the family.
3. **Pick `widget_size`** — smallest size that fits without clutter.
4. **Choose one hero** — what is the single takeaway? (Per view, if using views.)
5. **`list_golden_examples`** — S1–L2 for composition; `v2-*` for language nodes. Load with `example_id`.
6. **Adapt the pattern** — swap bindings for real fields; static labels stay literal.
7. **Assign typography** — hero / body / caption sizes from table.
8. **Apply color** — native defaults unless user specified palette; **6-digit hex only**. Maps and `colorScale` use the same hex rule.
9. **Run sizing math** — main skill algorithm; shrink before dropping the hero. Chart/grid/table need an explicit `height` or `size`.
10. **(Optional) `validate_template`** — max **2 calls** per design; then `create_template`. Structure must pass; design warnings do not block save. `families_used` is informational.
11. **Preview pause** — describe what the user will see, including which view is home; invite tweaks.

---

## Pre-submit checklist

Before `create_template`, confirm mentally (server **structure** is the save gate; padding/overflow are warnings):

- [ ] One clear hero element (per view)
- [ ] ≤ 3 font sizes, ≤ 2 active weights
- [ ] Root `padding` ≥ 12 (guideline — `ROOT_PADDING_LOW` will not block save)
- [ ] Labels use secondary color (`#8E8E93` or user-muted variant)
- [ ] At most one accent color (unless user asked for more)
- [ ] `maxLines` set on text that must not wrap
- [ ] Top-trailing corner clear of hero values (reload button overlay)
- [ ] Static labels/icons use plain literals (no `{{}}` unless value changes per refresh)
- [ ] All colors are 6-digit `#RRGGBB` (no alpha suffix)
- [ ] Layout suits the **data** — not a generic placeholder grid
- [ ] `get_plan` checked for any `chart` / `grid` / `table` / `views` / `action`
- [ ] No `bar_chart`, `pie_chart`, JS ternaries, or `action`+`href` on one node
- [ ] Chart series lengths match; pie ≤ 8; grid `rows*columns` = array length ≤ 400; table ≤ 4×6

---

## Talking to the user about design

- Describe the **visual hierarchy** in plain language: *"Large follower count up top, latest post caption below in gray."*
- Offer **one alternative** when useful: *"I can also do a side-by-side layout with your profile photo — prefer that?"*
- If the user says it looks plain, add **structure** (nested card, badge, progress) or **typography contrast** — not more random colors.
- For v2: name the **control**, not the type. *"The word is on the face; tap flips to the translation; reload shows the word again."* *"Home is three tiles; revenue is a sparkline; reload brings you back."*
