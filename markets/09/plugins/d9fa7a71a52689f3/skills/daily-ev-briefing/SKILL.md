---
name: daily-ev-briefing
description: Create a dated trading-card Daily EV briefing for selected games or sets, showing box/display EV, observed sealed prices, coverage and model exclusions without account linking.
---

Use The Expected Value's `query_daily_ev` for a free briefing. Respect the user's
chosen game, sets, currency and scope; a request for a briefing does not authorize
portfolio access or changes.

- Query the requested game/set and follow `page.nextPage` when a complete list
  is requested. State which filters and pages were covered; a first page is not
  the whole market. Keep booster packs inside their box/display context.
- Check snapshot `freshness` and every record's `evFreshness`. State the source
  observation dates. A fresh wrapper does not repair old EV. Unavailable or stale
  values cannot support a current ranking; missing prices are never zero.
- Present a compact table with product, marketplace low sealed price, opened EV
  and its singles basis, currency, coverage and source link. Keep marketplace
  names independent of the chosen singles basis. Do not compare USD with EUR.
- Include relevant chase exclusions from the supplied provenance. Preserve the
  baseline model; do not add serialized cards or excluded chase outcomes. Sift
  and user filters apply after complete contents are drawn and do not backfill.
- EV is gross unless explicitly fee-adjusted. Prices are dated observations,
  not proof of stock or landed cost. Link the public Daily EV page and explain
  any partial model coverage that affects the answer.

If the public dataset fails, report that limit. Do not substitute premium data
or request credentials. For an explicitly requested fee/break-even comparison,
use `compare_sealed_products` with eligible pricing access and user-selected
fees; keep the free briefing usable without linking an account.
