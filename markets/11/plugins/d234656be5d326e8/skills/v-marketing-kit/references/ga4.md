# GA4 source specifics

## GA4 (`mk_ga4_*`)

- Counts all sources, not only ads. For ads filter by the
  source or by the user property `af_media_source`.
- Data settles within 24–48 hours; realtime covers only the last 30 minutes.
- With small samples thresholds and sampling are possible — the answer marks them.

# Ready-made checks

1. **Event semantics.** Compare by day in `mk_ga4_report` pairs of events
   that must not match (trial start and payment, opening the purchase screen and
   cancelling). A full match or "the effect is bigger than the cause" is a reason to check
   the logging.
