# Meta Ads (`mk_meta_*`) — source specifics

- Installs and conversions follow Meta's attribution window (by default 7 days after
  the click and 1 day after the view). To reconcile with AppsFlyer request 1 day
  after the click (`action_attribution_windows: ["1d_click"]`) or state explicitly
  the window applied, taken from the answer.
- Data for the last 1–3 days is still being filled in — do not treat it as final.
- Custom app events in Insights reports may land in
  `app_custom_event.other`; by name they are visible in `mk_meta_events`.
- iOS: part of the conversions arrives through SKAN with a delay of up to several days
  and without a breakdown below the campaign.
- The attribution windows `7d_view`/`28d_view` return no data since 12 January 2026 —
  the tool removes them from the request itself and reports it in
  `action_attribution_windows.dropped` of the `mk_meta_insights` answer.
- `mk_meta_events` gives counters without a source (the owner's decision): the count
  of each event for the period is known (from `insights.actions` and the pixel
  stats), but where it came from — the app's SDK, the Conversions API or a partner
  integration — is not available programmatically and is not given in the answer.

## Ready-made checks

1. **Double counting of events in Meta.** `mk_meta_events`: one event (for example,
   StartTrial) arrives both from the SDK and from the AppsFlyer partner — double counting.
   Reconcile with the counter of the same event in AppsFlyer for the same period (call
   the `mk_appsflyer_*` tools).
2. **Attribution leak web → store.** `mk_meta_insights` (clicks to the store, window
   1 day after the click) against AppsFlyer by the source `meta_web2app` for the same
   period: a large gap on iOS is expected, on Android it is a reason to look for a
   broken OneLink.
3. **Silence after a release.** `mk_meta_events` for the last 2 days: an event that
   used to be there has disappeared — check the mapping in the new version (the pixel
   or a custom conversion may have stopped matching).
