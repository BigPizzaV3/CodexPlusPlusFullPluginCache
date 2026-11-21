# Setup and rollout

Use this in consultant mode: ask, recommend, then give a rollout plan the user can follow.

## 1. Discovery questions

Ask the few that matter for the request (three to five, not all of them):

- **Goal:** what should the screens do? Sell, inform staff, guide visitors, show live data, take input?
- **Audience and setting:** customers or staff? Retail floor, lobby, break room, factory, classroom?
- **Scale:** how many screens now, how many locations, growth in the next year?
- **Hours:** business hours only, or always on?
- **Hardware:** buying new, or reusing smart TVs, sticks or PCs?
- **People:** who creates content, who approves it, who looks after the screens on site?
- **Content sources:** files, a menu or price list, dashboards, calendars, social, internal sites?
- **IT:** corporate network (802.1X Wi-Fi, proxy, firewall)? Single sign-on? Security review?

## 2. Account structure

| Need | Use | Plan |
|---|---|---|
| One business, a handful of editors | One account, folders by location or purpose | Standard |
| Locations or departments that must not see each other's content | **Teams** (separate workspaces in one account; screen licenses can be split per team) | Pro Plus |
| Shared brand content from HQ, local content per site | Teams + **folder permissions** (HQ shares master folders down) | Pro Plus |
| Staff who suggest changes and a manager who signs off | **Content approval** (proposer and approver roles) | Pro Plus |
| Franchises or clients with their own billing and owners | **Sub-accounts** under a parent account | Ask support |
| Company sign-in | **SSO (SAML)** with Google Workspace, Microsoft Entra ID, Okta, OneLogin | Pro Plus |

Notes:
- Built-in roles: Owner, Super Admin, Admin, User, Content Proposal, Content Approval, Read Only.
  Custom roles are Pro Plus.
- Turning on custom roles or folder-level security **can't be undone**. Plan the structure first.
- SSO: "authentication only" (roles set by hand in the portal) suits small teams. "Full
  authorization" (identity-provider groups map to roles and teams on every sign-in) suits larger
  organizations. Always keep one backup admin who can sign in without SSO.
- There's no "move an asset to another team"; share the folder instead.

Help Center: multi-location chains
https://support.optisigns.com/hc/en-us/articles/43657735780627, teams and roles
https://support.optisigns.com/hc/en-us/articles/360034883113, folder permissions
https://support.optisigns.com/hc/en-us/articles/360044600474, approval workflow
https://support.optisigns.com/hc/en-us/articles/360063693093, SSO strategy
https://support.optisigns.com/hc/en-us/articles/4407128433299.

## 3. Device picks by setting

Short version (detail in [devices.md](devices.md)):

- Marketing screens in stores, restaurants, offices: **OptiStick**.
- Always-on, 24/7, or enterprise IT: **Pro Player**. Video walls, 8K, heavy animation: **ProMax**.
- Touch kiosks: **OptiKiosk** or a tablet.
- Existing smart TVs, Rokus, Fire Sticks: keep them, state the limits, add an OptiStick over HDMI
  where autostart matters.
- Never recommend a Fire Stick for a new purchase.

## 4. Naming convention

Agree on names before pairing. Rename later is slow at scale.

- Screens: `<location>-<area>-<number>`, for example `DAL-03-Lobby-01`, `NYC-Kitchen-Menu-02`.
- Use **tags** for groups that cut across locations (`menu-board`, `lobby`, `drive-thru`). Tags let
  you assign content, run remote commands and filter playlist items for a whole group at once.
- Folders mirror the structure: by region or location for screens; by campaign or purpose for content.
- Keep a sheet that maps each screen name to its physical spot and player serial.

Tags: https://support.optisigns.com/hc/en-us/articles/38062664690195.

## 5. Pairing and provisioning

- **A few screens:** install or plug in the player, it shows a pair code, enter it in the portal
  under Add Screen. Pair while in the right team so the screen lands there. Each screen uses one
  license; with none free it lands in the OnHold folder.
- **Many screens:** mass provisioning sets up many devices at once without typing codes (Enterprise).
  OptiSigns players can also ship preconfigured to pair themselves on first boot.
  https://support.optisigns.com/hc/en-us/articles/4416542923667
- **Raspberry Pi fleets:** https://support.optisigns.com/hc/en-us/articles/360063098753
- **Corporate networks:** open the OptiSigns domains on port 443 first, including the software update
  domains, or screens won't pair or update.
  https://support.optisigns.com/hc/en-us/articles/360047275934

First screen walkthrough: https://support.optisigns.com/hc/en-us/articles/18823504383891.

## 6. Rollout checklist

1. **Pilot:** one location, two or three screens, the real network. Confirm pairing, autostart after
   a power cut, and that content plays offline.
2. **Structure:** teams, folders, roles, SSO and naming agreed and set up before more screens join.
3. **Content plan:** a base playlist per screen type, a schedule for dayparts, and **default content**
   so a screen is never black between scheduled items.
4. **Set each screen's time zone.** Schedules run on the screen's local clock.
5. **Power and hours:** an operational schedule turns TVs on and off (HDMI-CEC or RS-232) on capable
   players.
6. **Monitoring:** offline email alerts for the screens that matter (Pro Plus); know who on site can
   power-cycle a player.
7. **Wave rollout:** location by location, reusing the pilot's playlists and schedules.
8. **Hand-off:** a one-page guide for site staff: what normal looks like, who to call.

## 7. Getting more value

- **Keep it fresh:** content that never changes stops being noticed. Rotate weekly; schedule by daypart.
- **Automate:** live data (menus, prices, KPIs, calendars, social) keeps screens current with no
  manual work. The `optisigns-automate` skill sets this up.
- **Measure:** proof-of-play reports show what played where (Pro Plus); Engage adds audience analytics.
- **Reuse:** one schedule works across time zones because each screen uses its own clock.
- **Interactive where it pays:** a few kiosk or QR-interactive screens via the Engage add-on.
- **Remote fixes first:** refresh, reboot and screenshot from the portal save a site visit.
