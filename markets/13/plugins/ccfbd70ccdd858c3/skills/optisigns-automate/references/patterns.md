# Automation patterns

Seven ready-made boards. For each: check whether a self-updating option fits first (SKILL.md §1). Every
template plugs into the full template in [host-scheduled-tasks.md](host-scheduled-tasks.md); fill the
`<…>` parts with the user's answers and the ids from the first run.

| Pattern | Source | Cadence | Output | Default method |
|---|---|---|---|---|
| Weekly team update | email or chat channel | Monday morning | 1 slide, 3–5 items | file swap in playlist |
| Release highlights | releases channel or changelog | weekly | 1 slide per notable release (max 3) | file swap |
| Calendar board | team or room calendar | daily | today's or this week's events | live page / web swap |
| KPI board | spreadsheet or dashboard | hourly–daily | big-number board | live page first |
| Menu change | menu sheet or doc | when it changes / daily check | menu board slide(s) | file swap or schedule item |
| Event countdown | event name + date | daily | "N days to …" slide | web swap or file swap |
| Social digest | company social accounts | weekly | 2–3 post slides | built-in social app first |

## 1. Weekly team update

- Source: a chat channel or email label, last 7 days.
- Output: 1 landscape slide; title "This week", 3–5 bullets ≤ 8 words, date range in the footer.

```
Keep "Weekly Update" current. Every Monday 7:00 am <timezone>.
Source: <#team-news> messages and <"Announcements" email label> from the last 7 days.
Summarize: 3–5 items people on the floor should know (launches, wins, deadlines, welcomes); ≤ 8 words each;
skip chatter, links and anything marked internal-only.
Output: 1 slide 1920×1080 PNG, same template as last week, footer "Week of <date>".
Target: team <teamId>, playlist <playlistId>, slot "Weekly Update – current".
Update method: file swap in playlist. If nothing new: no change. Approval: <ASK|STANDING …>.
```

## 2. Release highlights

- Source: a releases channel, changelog page or release notes feed.
- Output: one slide per notable customer-facing release, max 3; feature name + one benefit line.

```
Keep "Release Highlights" current. Every Friday 4:00 pm <timezone>.
Source: <#releases / changelog URL>, items from the last 7 days.
Pick up to 3 customer-facing releases; skip fixes and internal changes.
Output: one 1920×1080 PNG per release: feature name (large), one benefit line, release date.
Target: team <teamId>, playlist <playlistId>; replace last week's release slides in their positions,
remove extras if fewer this week. If nothing shipped: no change. Approval: <ASK|STANDING …>.
```

## 3. Calendar board

- Prefer a live calendar view or built-in calendar app (no job needed). Otherwise generate a page.
- Output: today's events with times and rooms, or a week grid.

```
Keep "Today at <Office>" current. Every weekday 6:30 am <timezone>.
Source: <calendar name>, events today between 8:00 and 18:00; public titles only, skip private events.
Output: a web page (or 1920×1080 PNG) listing time, title, room; max 8 rows; "No events today" is fine.
Target: team <teamId>, asset <assetId> ("Calendar – current").
Update method: <web URL swap | file swap in playlist <playlistId>>. Approval: <ASK|STANDING …>.
```

## 4. KPI board

- Prefer a dashboard page or built-in BI app that refreshes itself (publish once, done).
- Otherwise regenerate a big-number slide from the sheet.

```
Keep "Lobby KPIs" current. Every day 7:00 am <timezone> (or hourly 8:00–18:00 on weekdays).
Source: <spreadsheet / tab / cells>; metrics: <names>, with change vs <yesterday / last week>.
Output: 1920×1080 PNG or web page, 3–4 big numbers with labels and up/down arrows, "Updated <time>".
If the numbers are unchanged since the last run: no change.
Target: team <teamId>, <asset <assetId> | playlist <playlistId>>.
Update method: <web URL swap | file swap>. Approval: <ASK|STANDING …>.
```

## 5. Menu change

- Source: the menu sheet or doc (items, prices, sold-out marks).
- For breakfast/lunch/dinner times, build the daypart schedule once (operate skill) and swap each part's
  content.

```
Keep the "<Store> menu" current. Every day 5:30 am <timezone> (check for changes).
Source: <menu sheet>, tab <name>; columns item, price, available.
Output: <1 portrait 1080×1920 PNG per daypart>, same template; hide unavailable items; prices exactly as
in the sheet.
If the sheet hasn't changed since the last run: no change.
Target: team <teamId>, schedule <scheduleId> items <breakfast itemId, lunch itemId…> or playlist <id>.
Update method: <file swap in playlist | schedule item update scope ALL>. Approval: <ASK|STANDING …>.
```

## 6. Event countdown

- Source: event name and date from the user (or a calendar event).
- Output: "12 days to <Event>" slide; on the day: "Today: <Event>"; after it: stop.

```
Keep the "<Event> countdown" current. Every day 6:00 am <timezone> until <event date>.
Output: 1920×1080 PNG: "<N> days to <Event>", event date and place, same template every day.
On the event day show "Today: <Event>". The day after, change nothing and tell me the countdown is done
so I can turn this task off.
Target: team <teamId>, playlist <playlistId>, slot "<Event> countdown – current".
Update method: file swap in playlist. Approval: <ASK|STANDING …>.
```

## 7. Social digest

- Prefer the built-in social media apps (they refresh themselves); check `optisigns_app_manifest` for the
  platform.
- Otherwise build slides from the week's top posts.

```
Keep "Social Highlights" current. Every Monday 8:00 am <timezone>.
Source: <company accounts>, posts from the last 7 days; pick the 2–3 with the most engagement.
Output: one 1920×1080 PNG per post: image, first line of the caption (≤ 12 words), handle, date.
Use only the company's own posts; no customer photos without the user's OK.
Target: team <teamId>, playlist <playlistId>; replace last week's social slides in place.
If no new posts: no change. Approval: <ASK|STANDING …>.
```

## Tips

- Keep text large and short; the `signage-design` skill has sizes and contrast rules.
- One board per task; separate tasks for separate screens' content.
- After the first unattended run, check the report with the user once.
