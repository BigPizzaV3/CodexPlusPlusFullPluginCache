---
name: irisx-analytics-sql
description: Orientation and query procedure for the IrisX Analytics data lake (Databricks Unity Catalog, catalog `irisx`). Use this when the user writes, reviews, debugs or explains SQL against irisx.* data; asks to query the data lake, Databricks, or the irisx catalog; or wants historical, aggregated, metric, trend, or cross-fleet analysis such as fuel usage, idle hours, engine hours, fault codes, or utilisation — even if no table is named. Do not use this for current lookups of an asset, site, depot, customer, group, or other entity details — GraphQL is the primary interface for live metadata, associations, maps, and Manager links. Trigger this BEFORE running any analytics SQL, because picking the wrong catalog or the wrong time-grain view is the most common failure and cannot be recovered after the fact.
---

# IrisX Data Lake

This skill gets you oriented and tells you how to look things up. It deliberately does **not** describe what individual tables and columns mean — that lives in the Unity Catalog comments, which are authoritative. Read them.

## Current entities belong on GraphQL

A question about an asset, site, depot, customer, or group as it exists now is a GraphQL lookup. GraphQL returns live metadata, associations, maps, and Manager links. This skill is for the data lake — SQL, history, aggregation, metrics, trends, and cross-fleet analysis. Do not start here for a current-entity question; the orientation below will not help, and it only adds latency.

## Start in the right catalog

Trackunit-provided fleet and telematics data lives in **`irisx`**. Always start there.

Other catalogs may be named similarly to the customer account slug. Those hold tables the *customer* uploaded themselves — not Trackunit data. Never infer a catalog name from the account slug. Only leave `irisx` if the user explicitly asks about their own uploaded tables.

## The catalog describes itself — read it before guessing

Every catalog object carries a table comment, and core-schema columns carry column comments. These are the source of truth for business meaning. Blind-guessing table names is the single most common failure mode here, and it is entirely avoidable:

```sql
DESCRIBE TABLE EXTENDED irisx.<schema>.<table>;
```

Do this before explaining, joining, or filtering a table you have not already looked up in this session. If a comment is missing or contradicts what the name implies, **trust the comment and say the name is misleading** — several are.

If a table or column has no comment and you cannot determine its meaning from the catalog, say so plainly and ask. Do not infer meaning from the name. A wrong confident answer about fleet data is worse than an admitted gap, because the user cannot tell the difference without re-doing your work.

## Orientation

`asset.asset` is the hub. Nearly every other schema hangs off `asset_id`. When unsure how two tables relate, check whether both carry `asset_id` before looking for anything cleverer.

| Domain | Schema(s) |
|---|---|
| Accounts & customers | `account` |
| Users & groups | `user`, `group` |
| Asset (hub) | `asset` |
| Devices & device state | `telematics_device` |
| Raw device telemetry | `telematics_device_telemetry` |
| Computed metrics | `insight` |
| OEM / custom sensors | `advanced_sensor` |
| Faults & CAN errors | `event` |
| Sites & access keys | `site`, `access_management` |
| Maintenance | `service_plan` |
| Platform / billing / calendar | `irisx`, `usage`, `dimension` |

## Finding the right metric — do not enumerate

The `insight` schema ships many metric families, each with five grains: base, `_2min`, `_hour`, `_day`, `_latest`. Never list them all, and never guess a metric name. Search:

```sql
SELECT table_name, comment
FROM irisx.information_schema.tables
WHERE table_schema = 'insight'
  AND table_name LIKE '%fuel%'          -- keyword from the user's question
ORDER BY table_name;
```

Try a couple of keyword spellings before concluding a metric does not exist — names are compressed and unpunctuated (e.g. `acaveragefrequency`). If several families plausibly match, show the user the candidates and ask which they mean rather than picking one. Choosing the wrong metric produces a confident, plausible, wrong number.

The same search works on any schema. Use it whenever you are reaching for a table name you have not verified exists.

## Query rules

1. **Always fully qualify:** `irisx.<schema>.<table>`. Unqualified names resolve unpredictably.

2. **Always apply the table's stated filter column.** Each table comment names one (`account_id`, `asset_id`, `date_utc`, `timestamp_utc`, `site_id`, or a pair). These views scan wide without it, and unfiltered fleet-scale queries are the main source of slow and timed-out queries. Read the filter hint from the comment rather than assuming which column it is — it varies within a schema.

3. **Pick the smallest sufficient grain.** `insight` and `telematics_device_telemetry` ship multiple grains per metric. A question about a month of data wants `_day`, not the base view. Defaulting to raw is the second-biggest performance mistake. Use `_latest` for "right now" questions — it is one row per asset and far cheaper than ordering the full history.

4. **Check freshness before answering "now" questions.** `irisx.irisx.data_updated` holds the refresh watermark per table:
   ```sql
   SELECT * FROM irisx.irisx.data_updated
   WHERE schema_name = 'insight' AND table_name = '<view>';
   ```
   Cadences differ by family (hourly for master data, every 4 hours for events and insights, ~8 minutes for raw telemetry). If the user asks for live data, tell them the actual staleness rather than implying the number is current.

5. **Never mix event time and receipt time.** Several views carry both. `timestamp_utc` is when the reading happened on the machine; `received_timestamp_utc` and `stream_timestamp_utc` are when the platform got it. Machines go offline and backfill, so these diverge by hours or days. Filter and aggregate on event time unless the user is specifically asking about ingestion lag.

6. **Aggregated grain views carry a window, not an instant.** `_2min` / `_hour` / `_day` views expose `start_time_utc` and `end_time_utc` alongside `timestamp_utc`. Use the window bounds for interval logic; do not treat the row as a point measurement.

7. **Everything is a view.** Catalog objects are Unity Catalog views with no declared primary or foreign keys. Nothing enforces referential integrity, so joins can silently drop or fan out rows. Sanity-check row counts on multi-table joins before reporting a number.

## Two names that mislead

These trip up nearly everyone, cross schema boundaries, and so have no single comment to live in:

- **`account` is not `customer`.** An account is the Trackunit tenant (a rental company, say). A customer is that tenant's own end-customer, who rents machines from them. `account.customer` is therefore one level *below* `account.account`, not a synonym. Getting these backwards inverts the whole fleet-ownership picture.
- **`insight` is not `telematics_device_telemetry`.** `insight` holds computed, business-level metrics. `telematics_device_telemetry` holds raw device signals — including device health rather than the machine measurement you probably want. When the user asks a fleet question, reach for `insight` first.

## Handling personal data

`user.user`, `account.customer` and `account.customer_contacts` contain names, emails, phone numbers and addresses. `access_management.key` contains operator identity.

Do not surface these in anything shared, exported, published, or written to a file. Aggregate or redact instead. If the user explicitly wants identifiable rows, confirm the destination before producing them — and never place them in an artifact or HTML output, where personal and customer data must not be posted.

## Reporting results

State the grain, the time window, and the freshness alongside any number you report — a fleet figure without those three is not interpretable, and the user cannot spot a grain mistake without them. If you fell back to a metric family you were not certain about, say which one you used and why.
