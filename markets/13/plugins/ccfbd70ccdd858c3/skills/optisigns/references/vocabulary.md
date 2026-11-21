# OptiSigns vocabulary

Use the customer-visible name in replies. When a phrase could mean two things, ask one short question.

## Core terms

| Term | Meaning |
|---|---|
| Screen | A display running the OptiSigns player, paired to the account. It is the device plus its license, not the physical panel. |
| Asset | One piece of content: image, video, document (PDF, PowerPoint), website, or app. |
| Playlist | An ordered list of assets, each with a duration, that loops on the screen (also "content rotation"). |
| Schedule | Time rules for which asset or playlist plays when: by day, hour, recurring or one-off. |
| Default content | What plays when nothing is scheduled. |
| Team | A workspace inside an account. Content and screens belong to a team. |
| Folder | Organizes screens, assets, playlists and schedules; also a permission boundary. |
| App | A built-in content type set up with a form: weather, clock, news, RSS, Google Slides, social feeds, dashboards, QR codes and many more. |
| Assign / push | Set what a screen shows now (an asset, playlist or schedule), or schedule a future go-live. |
| Pairing code | The short code a new screen shows; entering it in the portal links that screen to the account. |
| Offline playback | A screen keeps playing cached content when the network drops; changes apply when it reconnects. |
| Split Screen | Several content zones on one screen, such as main content plus a ticker or a logo. |
| Takeover / flash message | A time-boxed override of normal content, for alerts or specials. |
| Operational schedule | Turns the display on and off on a timer. This is power, not content. |

## Customer says X, means Y

**Devices**
- "my TV / monitor / display / the sign" → a screen. "The board" may be a menu board.
- "the player / the box" → the device running the player app. Which platform matters.
- "the stick" → could be an OptiStick, an Amazon Fire TV Stick, or another Android dongle. Ask; fixes differ.
- "Firestick" → Amazon Fire TV, not an OptiStick.
- "Pro Player / ProMax" → OptiSigns' own high-end players.

**Content**
- "pic / photo / image" → image asset. "vid / clip / movie" → video asset.
- "slideshow / loop / rotation" → playlist. "It loops wrong" usually means playlist order or durations.
- "slides" → an asset, a playlist, or the Google Slides app. Ask if unclear.
- "menu board" → a menu design; may pull live prices from a POS or spreadsheet.
- "design / template / Canva" → the Designer or a template; "Canva" may mean the Canva integration.
- "push / deploy / send it to the TV" → assign content to a screen.
- "takeover / override" → a temporary takeover, not a permanent change.

**Scheduling**
- "calendar / timetable" → a schedule, or the Google / Microsoft calendar app. Ask.
- "daypart / breakfast menu in the morning" → a recurring schedule by time of day.
- "turn the TV on and off on a timer" → operational schedule, not content scheduling. Depends on the device.
- "what plays when nothing's scheduled" → default content.

**"Not working"**
- "it's offline / down" → screen offline: network, power, the app not running, or an operational schedule. Diagnose, don't assume.
- "TV won't turn on" → offline, scheduled power-off, or hardware. Ask what they see.
- "black screen every morning / goes dark overnight" → check for an operational schedule first; a repeat at the same time is a schedule, not a fault.
- "stuck on old content / not updating" → content not syncing yet; check that the screen is online.
- "it just shows a login page" → the site needs a sign-in or blocks embedding; a secured dashboard or web scripting app fits better than a plain website app.

**Account and access**
- "workspace / group" → a team, or a folder. Confirm.
- "admin" → an administrator role; not the same as the account owner.
- "give them access" → invite a member and pick a role.
- "SSO" → SAML single sign-on. "2FA / MFA" → multi-factor sign-in.

**Plans and billing** (route actions to the portal or support)
- "my plan / subscription" → the plan tier: Free, Standard, Pro Plus, Engage or Enterprise. "Pro" alone is an older tier some existing accounts still have.
- "pause / on hold" → put screens on hold; content is kept.
- "cancel" often means pause for the season; mention On Hold.
- "refund / overcharged / invoice / PO" → billing; route to support.

**Apps and integrations**
- "widget" → app. "weather / clock / news / RSS" → the named app.
- "show my dashboard / Power BI / Tableau" → a dashboard app; sign-in-protected ones need the secured dashboard path.
- "embed a website" → Website app, or Scrolling Website.
- "Google Sheet / Excel as data" → OptiSync, live data into a design.
- "API / webhook" → the OptiSigns API or API Gateway.
- "cast / screen share / present" → AeriCast wireless presentation.

**Remote management and interactive**
- "restart it remotely / take a screenshot of the screen" → remote commands (plan- and device-dependent).
- "kiosk / touch screen / interactive" → Engage or Kiosk Designer Pro (Engage plan).
- "QR code" → a QR Code app or overlay. "Check-in screen" → Check-in app (Engage).

## Opti* names people mix up

- **OptiSync**: live data into content. **OptiSound**: background music add-on. **OptiStick**: OptiSigns' HDMI stick player (Android, not Fire OS). **OptiKiosk**: touch kiosk hardware. **AeriCast**: wireless presentation.

## Plan-gated features (attribute to the plan)

- Brand Kit, Web Scripting, Proof of Play, Sync Play, custom domain: Pro Plus and up.
- Kiosk Designer Pro, AI camera, Check-in, touchless QR, IoT/sensor triggers: Engage.
- Remote commands: depend on plan and device.

## Industry terms

| Term | Meaning |
|---|---|
| Digital signage | Centrally managed displays showing scheduled content. |
| DOOH | Digital out-of-home: digital ads and signage in public venues. An ad network is a different business from a signage CMS. |
| CMS | The cloud platform managing content and screens (OptiSigns). |
| Content loop | The sequence a screen cycles through; a playlist. |
| Dayparting | Different content by time of day. |
| Zone / region | Part of a screen with its own content (split screen). |
| Ticker / crawl | A scrolling text band along an edge. |
| Lower third | An overlay in the bottom part of the frame. |
| Video wall | Several panels from one player, as one canvas or separate content per panel. |
| Menu board | A restaurant display of items and prices, often synced to a POS. |
| Wayfinding | Directional signage in lobbies, campuses and hospitals. |
| Kiosk / interactive | A touch or QR-driven self-service display. |
| Attract loop | Idle content that draws people to a kiosk. |
| Dwell time | How long a viewer stays in front of a screen. |
| Captive audience | Viewers in a fixed setting: waiting room, elevator, queue. |
| Aspect ratio / orientation | Width to height (16:9, 9:16); landscape or portrait. |
| Commercial display | A panel rated for 24/7 use, unlike a consumer TV. |
| SoC display | A display with a built-in player (Samsung Tizen, LG webOS). |
| Fleet / endpoint | All screens on an account / one screen in it. |
| Provisioning / mass deployment | Preparing and pairing many devices at scale. |
| Proof of play | A log showing content actually played. "POP" in OptiSigns means proof of play, not point of purchase. |
| Sync play | Frame-synchronized playback across screens. |
| Failover | What plays when scheduled content or the network fails. |
| Data-driven content | Content filled live from a data source. |
| Brand compliance | Keeping content on-brand (fonts, colors, logos). |
