# Built-in OptiSigns apps

Check this list before designing anything. A built-in app updates itself, needs no hosting and no
redesign when the data changes. If one fits, recommend it and say why in one line; design a slide or
page only when the user still wants their own look or the app can't show what they need.

## How to create one

1. `optisigns_app_manifest(appType)` → the fields the app needs. Never guess fields.
2. Ask the user for whatever is required and missing (location, feed URL, account to connect).
3. Show the plan (app, settings, name, which screen) and get the user's OK. Only then call
   `optisigns_asset_create{appType, appData, name}` (a web page: `{url, name}` only). The server does
   not ask for confirmation on a create, so this OK is the only one.
4. Hand off to `optisigns-operate` to assign or schedule it.

Some apps need the user to connect an account (Google, Microsoft, Instagram, Power BI) in the OptiSigns
portal first; the manifest shows those fields. If the connection can't be made from chat, say so and
point to the portal.

## The apps

| Need | App | appType | Prefer it when |
|---|---|---|---|
| Current weather / forecast | Weather | `weatherForm` | Any "today's weather" sign. Needs a location (city + latitude/longitude). |
| Time of day | Clock | `simpleClock` | A clock on its own or in a zone. Never build a JavaScript clock page for this. World clocks: ask `optisigns_app_manifest` for the type. |
| Headlines, blog, news | RSS / news feed | ask `optisigns_app_manifest` for the type | The source has an RSS feed and the user wants it always current. |
| A deck the team already edits in Google | Google Slides | ask `optisigns_app_manifest` for the type | The slides live in Google and change often; edits show up without re-uploading. |
| Meetings, room bookings, events | Google / Microsoft calendar | ask `optisigns_app_manifest` for the type | A room or lobby schedule from a real calendar. A one-off "this week's events" slide is fine as a design. |
| Business dashboard | Power BI | `powerBi` | The report already exists in Power BI. Don't rebuild it as a page. |
| Video from a channel or playlist | YouTube | ask `optisigns_app_manifest` for the type | The video is on YouTube and should stay there. A video file they own is uploaded instead. |
| Social posts | Instagram (business) | `instagramBusiness` | Show the account's latest posts. Other networks: ask `optisigns_app_manifest` for the type. |
| A live web page or web dashboard | Website | `website` (or just pass `url`) | The page exists, is public, and fits one screen without scrolling. |
| A project built on OptiDev | OptiDev project | `optidev` (a `*.optidev.ai` URL is detected) | The user built an app on OptiDev; `name` defaults to the project name. |

## Common requests that are an app, not a slide

| Request | Use |
|---|---|
| Room schedules, building or school events kept in a calendar | Calendar app |
| Live KPIs, sales numbers, production counts, OEE | Power BI, or a dashboard web page |
| Company news, a blog, a chat channel that changes daily | RSS / feed app, or a web page |
| Reviews, Instagram, social proof | Social feed app |
| Weather, local news, transit, flight times | Weather / news apps |
| A daily menu or bell schedule already kept in a spreadsheet | Live Google Sheets or a web page |
| Health or safety tips that rotate weekly | Feed app, or a short deck |

## When a design still wins

- The message is static (an announcement, a promo, a menu that changes weekly) → slides.
- The user wants their brand look on weather, news or calendar data and the app's themes don't fit →
  a web page (`references/web-app.md`).
- A Website app shows blank because the site refuses to load inside other pages → suggest the native app
  for that data, or a slide or file.

## Help Center

- Clock styles: https://support.optisigns.com/hc/en-us/articles/360042950593
- World clocks: https://support.optisigns.com/hc/en-us/articles/360042450514
- Google and Microsoft calendars together: https://support.optisigns.com/hc/en-us/articles/4408052949139
- iCloud calendar: https://support.optisigns.com/hc/en-us/articles/27356288211859
- Curated feeds: https://support.optisigns.com/hc/en-us/articles/24338756617747

For any other app, search with `optisigns_kb_search` ("<app name> app").
