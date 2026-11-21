# App filters

Use semicolons to combine country/category values, matching the dashboard request. `country` is required; select markets relevant to the current conversation rather than assuming worldwide coverage. These are configured dashboard filter values, not guarantees that every product/category has observations in every market.

Categories (exact English values): `Popular`, `Electronics`, `Home & Garden`, `Health & Beauty`, `Apparel & Accessories`, `Tools`, `Baby & Toddler`. When omitted, search uses all seven, matching the dashboard's initial category selection.

Dashboard country choices include `DZ`, `TN`, `MA`, `LY`, `EG`; grouped Gulf `SA;QA;EA;OM;BH;KW`; Europe `GB;IE;FR;BE;LU;CH;DE;AT;ES;IT;NL;PT`; and Africa `NG;CI;SN;KE`. The dashboard's existing Gulf group spells the UAE entry `EA`, while its flag map contains `AE`; this inconsistency is preserved, not repaired by the plugin. Do not claim UAE coverage on the basis of that group value alone. Actual data completeness remains a separate question.

`weeks` defaults to 12, matching the dashboard request. The existing backend clamps its effective raw request to 1–200. Window/batch semantics follow the app; requesting a larger window does not manufacture older data.

`v` defaults to the shared dashboard request version. It affects the existing outer cache key. Normally omit it. Do not change it to bypass usage limits; it has no effect on plugin quota identity.

The MCP adapter supplies `priceFrom: -1`, `priceTo: -1` and `transformation: "market-reaction"` through the same shared request builder as the dashboard. It does not select the separate advanced-analysis branch or run another reasoning model.
