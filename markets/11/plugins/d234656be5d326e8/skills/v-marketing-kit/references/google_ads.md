# Google Ads: source specifics

- Conversions are by the click date, not by the conversion date; the window is set in the
  conversion action.
- The cost in `cost_micros` is to be divided by 1 000 000. `mk_google_ads_report`
  returns a ready field without the `_micros` suffix next to the original one — already
  divided, no need to recalculate by hand.
