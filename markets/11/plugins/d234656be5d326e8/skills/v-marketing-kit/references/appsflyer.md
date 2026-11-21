# AppsFlyer: source specifics

- An install = the first launch with the AppsFlyer SDK. Users of old versions without
  the SDK are not visible in AppsFlyer at all.
- Installs from the web on iOS are not always linked to the click — part of them go to
  organic. On Android linking through the Install Referrer is almost complete.
- In-app events are attributed to the install source, not to the last click.
- `mk_appsflyer_raw` is available only with the Raw Data module in the plan.

## Ready-made checks

1. **Attribution leak web → store.** Meta insights on clicks to the store (window
   1 day after the click) against `mk_appsflyer_aggregate` for the needed `media_source`
   (for example, `meta_web2app`) for the same period: a large gap on iOS is
   expected, on Android it is a reason to look for a broken OneLink.
2. **Silence after a release.** Meta events and `mk_appsflyer_aggregate` for the last 2 days:
   an event that used to be there has disappeared — check the mapping in the new version.
