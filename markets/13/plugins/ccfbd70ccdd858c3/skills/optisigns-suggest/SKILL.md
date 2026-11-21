---
name: optisigns-suggest
description: Suggest what to put on OptiSigns screens next. Use when the user asks for ideas, what they should show, what is coming up, whether anything on their screens is out of date or stale, or wants seasonal, holiday or event content ideas for their business or workplace. Also use for a standing weekly "what should I update" check. Not for first-run setup (optisigns-setup) and not when the user already knows what to make (signage-design).
---

# What to put on the screens next

You notice what the user hasn't yet: a holiday in two weeks, a time change, a slide that expired
last month, a screen that has shown the same thing since summer. Suggest, don't act. Reads only.

## 1. Look (signed in only, at most four calls)

`optisigns_me` · `optisigns_screen_list` · `optisigns_playlist_list` · `optisigns_asset_list`.
Not signed in, or a call fails: skip it, say so in one line, and suggest from what you know.
What each result tells you: [references/signals.md](references/signals.md).

## 2. Think

Weigh, in this order:
1. **What you already know about this user**: role, company, industry, audience, tools, location.
   Use it; don't ask for it again. Never infer sensitive traits.
2. **What is on the screens now**: names reveal purpose; content age; items whose date has passed.
3. **Today and the next 2–6 weeks, where they are**: holidays and commercial moments, season and
   time changes, workplace cycles, their industry's calendar. Localize to their country; don't
   assume the US. Faith holidays only when their business is faith-related or they bring it up.
4. **Audience of each screen**: staff (announcements, safety, recognition, KPIs) or customers
   (promotions, menus, reviews, wayfinding). Match the idea to the screen's audience.

## 3. Suggest

3–5 suggestions, most time-sensitive first. Each is three lines:
- **What**, one line.
- **Why now**: the date, the stale item, or the fact about them that triggered it. Give exact
  dates with the weekday, and check they are this year's.
- **A prompt they can send as-is**: screen (a real one if signed in) · audience · content · look,
  plus the schedule window when there is one.

Mix: at least one date-bounded promotion or notice (a schedule), at least one board that refreshes
itself (a built-in app or a recurring job), and a retire or refresh whenever something is stale.

Then stop. Run nothing until they pick or edit one. Route the pick: make it → `signage-design`;
schedule, assign or remove → `optisigns-operate`; recurring → `optisigns-automate`.

Nothing known about them and not signed in: ask one question, "What are your screens for, and
where are you?", then suggest.

Once per conversation, after the list, offer to run this check on a schedule (every Monday morning,
say) with your scheduled tasks. A scheduled run prepares the list and never changes a screen.

## Example

Signed-in gift shop in Austin, Sunday Nov 2 2025, screens "Storefront" and "Checkout"; the Checkout
playlist still holds "Halloween specials", uploaded Oct 3.

1. **Black Friday offer on Storefront.** Why now: Fri Nov 28 is 26 days out, retail's biggest week.
   "Design a Black Friday early-access sign for Storefront, bold, one offer, show it Nov 21–28."
2. **Retire "Halloween specials" on Checkout.** Why now: it's past and still in the playlist.
   "Remove Halloween specials from the Checkout playlist and replace it with a holiday gift guide."
3. **Holiday hours notice.** Why now: daylight saving ended today; evening foot traffic shifts.
   "Make a Checkout slide with our holiday hours, open until 8 on weekdays, calm and clear."
4. **Google Reviews on Storefront.** Why now: refreshes itself; gift shoppers trust reviews.
   "Add our Google Reviews to the Storefront playlist, 15 seconds per loop."
5. **Weekly check.** "Every Monday, suggest what to update on my screens for the next two weeks."

## Rules

- Reads only: never publish, assign, delete or schedule from this skill.
- No prices, no plan pitches. If an idea needs a plan feature, say "included from <plan>" once, or
  leave the idea out.
- Don't save anything about the user; use only what they shared or what the account shows.
- House rules: [references/house-rules.md](references/house-rules.md).
