# Data format

## Geo panel (design, readout, profile)

One row per geo and day, long format:

```csv
date,geo,conversions,spend,revenue
2026-01-05,Madrid,312,4120.50,18450.00
2026-01-05,Barcelona,288,3890.10,17020.00
```

| Column | Required | Notes |
|---|---|---|
| date | yes | ISO dates. Daily is strongly preferred; weekly works with lower power |
| geo | yes | The unit that will be targeted on and off: region, province, state, DMA, city, postcode group |
| KPI | yes | The business outcome: orders, leads, sign-ups, subscriptions. Recognized names: conversions, orders, leads, signups, sales, purchases, transactions, kpi |
| spend | no | Spend of the channel being tested, by geo. Needed for cost, iCPA and iROAS |
| value | no | Revenue or conversion value. Needed for iROAS |

The script recognizes common column names and accepts explicit `--date-col`, `--geo-col`, `--kpi-col`, `--spend-col`, `--value-col`.

History: at least 8 weeks before the test, ideally 12 months. The longer the history, the more placebo windows and the more honest the interval.

## Single series (prepost, switchback)

```csv
date,conversions,spend,control
2026-01-05,1840,9200,620
```

`control` is optional: a series the change did not affect, such as the same KPI in another country, organic-only sign-ups, or a product line with no ads.

## Where the data usually lives

| KPI source | How to get it by geo and day |
|---|---|
| Shopify | Orders export with shipping region, or the Shopify analytics "Sales by billing region" report by day |
| GA4 | Exploration: dimensions Date and Region (or City), metric Key events or Transactions; or BigQuery export with `geo.region` |
| CRM (HubSpot, Salesforce) | Leads or deals created by day with the contact's region or postcode |
| App | Installs or subscriptions by day and country or region from the analytics tool or the backend |
| Google Ads (spend) | Report with Day and the "user location" geo dimension (matches targeting), or the campaign's geo report |
| Meta Ads (spend) | Ads Reporting with breakdown by Region and Day |

Use the backend as the KPI source. Platform-reported conversions are attributed by the same platform being tested: in geos where ads are off they drop to zero by construction and say nothing about organic or direct conversions that replaced them.

Geo granularity: the geo in the data must match a unit the ad platform can target. Postcodes from the CRM can be grouped into the regions used for targeting.
