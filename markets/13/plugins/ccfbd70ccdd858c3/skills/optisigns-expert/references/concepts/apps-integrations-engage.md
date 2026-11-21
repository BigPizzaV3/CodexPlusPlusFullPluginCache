# Apps, integrations and Engage

## Five ways to show outside content

The deciding question: **does the source need a login, and can the screen sign in by itself?**

| Source | Use | Login | Plan |
|---|---|---|---|
| Public web page | **Website** or **Embed** app | None | Standard |
| Common service (weather, calendars, social, Power BI, news) | A **native app** (100+) | Handled by the app | Varies; most Standard |
| Site with a simple login on a desktop-class player | Website, signed in once on the device | Saved on the device | Standard |
| Site with a login, no person at the screen | **Web Scripting** (a recorded login the player replays) | Recorded | Pro Plus |
| Login with two-factor codes, a mixed fleet, or a slow report | **Secured Dashboard** (runs on a server, sends a screenshot) | On the server | Pro Plus |
| Your own data (Sheets, POS, REST APIs) shown in your design | **OptiSync** data sources into Designer | Stored keys | Pro Plus |

- **Prefer a native app** when one exists. It handles sign-in and refresh, and survives changes to the
  source site better than a recorded login.
- **Login pages don't render** through the plain Website or Embed app.
- **Embed only works** if the source site allows being framed.
- **Cookie banners aren't dismissed** automatically; the site shows them like any browser would.
- **Recorded logins break** when the site changes its sign-in flow; re-record it.
- **Two-factor codes:** Web Scripting can generate fresh codes on Android and OptiStick players when
  given the secret key. Fire OS can't. Secured Dashboard covers the rest.
- **Samsung and LG signage TVs** often can't render modern dashboards like Power BI. Use an OptiSigns
  player.
- **Power BI** connects through Microsoft's official API. An Azure admin approves OptiSigns once.
  The same report can be filtered per screen with a screen attribute (for example `Location`).
- **Menu boards with live prices** from a POS work through OptiSync:
  https://support.optisigns.com/hc/en-us/articles/31860170199955

## Engage: interactive screens

Engage turns a one-way display into a two-way one. It's available as the Engage plan (every screen)
or as the **Engage add-on** on chosen screens of a Standard or Pro Plus account.

| Feature | What it does |
|---|---|
| Kiosk Designer Pro | Touch apps built in Designer: tap an element to open content or a page |
| Kiosk Lite | Simple kiosk: play content, launch an app, idle attract screen |
| AI Camera | Detects viewers (gender, expression) to tailor content and gather analytics. Age isn't supported |
| Check-in + SMS | Visitor form on an iPad or Android tablet, SMS follow-ups, review requests. Includes an SMS allowance per screen |
| Touchless QR | Viewers scan a QR code to trigger content; no touch screen needed |
| IoT / RS-232 sensors | Lift and Learn: picking up a product changes the content |
| Live TV with ads | Promotions overlaid on a live TV feed |

Common Engage questions:
- **Interactive content won't assign:** check the plan, or whether this screen has an Engage add-on.
- **Engage disappeared after the trial ended:** a trial includes Engage on one screen; a paid Pro Plus
  plan doesn't. Add Engage to the screens that need it.
- **Engage tab missing:** turning on "Remove OptiSigns Branding" hides it for the whole account.
  Users with SSO or custom roles may also not see it; that's a permissions setting.

Engage FAQ: https://support.optisigns.com/hc/en-us/articles/23565267463315
