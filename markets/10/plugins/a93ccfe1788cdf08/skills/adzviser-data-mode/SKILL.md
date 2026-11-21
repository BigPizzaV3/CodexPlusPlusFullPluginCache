---
name: adzviser-data-mode
description: Retrieve and analyze reporting from the user's connected Meta Ads accounts with Adzviser. Use for Facebook and Instagram advertising spend, clicks, purchases, campaign comparisons, trends, raw rows and Data Mode. Do not use for an interactive report preview, current account settings, account edits, connection permissions, change receipts, or public competitor Ad Library searches.
---

# Meta Ads Data Mode

Use `retrieve_reporting_data` for questions about numbers. Use the preview skill
only for an explicitly requested interactive report. Do not open a widget merely
to display a report already retrieved for analysis.

## Reporting workflow

1. Call `list_workspace` and select the user's named workspace. If access is
   unavailable, explain the problem instead of substituting another workspace.
   If no workspace was named and multiple suitable choices exist, ask which to use.
2. Call `list_metrics_and_breakdowns_fb_ads` with the selected `workspace_name`.
   Use exact returned labels, including workspace-specific custom conversions
   when relevant. Request only the fields needed to answer the question.
3. Resolve inclusive YYYY-MM-DD date pairs using the current date. Last month
   means the previous complete calendar month; last week means the previous
   complete Monday-Sunday week unless the user specifies otherwise. Dates use
   the advertising account's reporting timezone.
4. Send `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.fb_ads_request` containing `metrics`
   and optional `breakdowns`. Include both periods in one comparison request.
5. Read all tables, headers, rows and relevant `note_of_assumption` values under
   `structuredContent.reportingData.FacebookAds`. The `data` object can contain
   a table keyed by an empty string or by a breakdown such as PublisherPlatform.
   Do not assume a fixed table key or flatten headers into data rows.
6. Answer from the returned rows, with the workspace, exact dates, units and
   relevant limitations. Reuse successful results instead of repeating queries.

Never send conversation history, the raw user prompt, unrelated context,
credentials, email addresses or session tokens as report inputs. Use only
structured fields needed for the report. `reporting_mode=data` selects this
workflow; it is not a tool argument. Do not send `client_id`, `reporting_mode`
or `_widget_action`. `set_reporting_mode` is an app-only preference control.

## Interpret Meta Ads data

- Include Account Currency for monetary reports. Preserve the reported currency
  and keep different currencies separate. Do not assume USD or convert units.
- Include Campaign ID with Campaign Name when distinguishing campaigns. Names
  need not be unique. Use equivalent IDs for ad sets and ads when needed.
- A request for conversions may mean purchases, leads or a custom event. Use
  the event specified by the user; clarify an ambiguous conversion definition.
  Website Purchases counts attributed purchase events, not unique customers.
  Do not substitute Actions or a different conversion event for purchases.
- Spend, Impressions, Link Clicks and Website Purchases are examples; confirm
  current field labels through discovery. Link Clicks and Clicks (All) differ.
- Publisher Platform can include Facebook, Instagram, Audience Network, Threads
  or other returned values. Preserve actual groups rather than forcing every
  row into Facebook or Instagram.
- Calculate rates from their matching numerators and denominators, with N/A for
  a zero denominator. Do not average percentages, frequencies or ROAS across
  groups. Do not sum reach as though it were a deduplicated audience.
- Use `time_granularity` for Date, Week, Month or Quarter instead of inventing
  time breakdowns. Daily dates can be returned in a Date Range column.
- Keep full returned precision for calculations and round only displayed money.
  A zero comparison baseline has no finite percentage change. Missing rows are
  not proof of zero activity; explain header-only or empty results honestly.
- Configured ad-set targeting describes settings. Demographic performance
  describes aggregate delivery; neither reveals individual audience members.

Only `fb_ads_request` is supported for reporting here. Do not use
`meta_ad_library_request` for connected-account reporting or claim this plugin
can search public competitor ads or disclose individual people who saw an ad.

Reporting tools do not change advertising accounts. Use
`adzviser-account-management` for current settings, campaign or ad set renames
and pauses, connection permissions, and change receipts. Its resource discovery
uses `source=fb_ads`; reporting still uses `assorted_requests.fb_ads_request`.

When analysis leads to a requested edit, preserve the workspace, advertiser
account, campaign or ad set identity, and any returned `evidence_ref`. Discover
current resource references and action schemas before previewing the edit.
A report or recommendation alone does not authorize preparing or applying a
change. Account edits require their own saved preview and exact user
confirmation before apply.

Do not invent arbitrary filters, URLs, sorting, limits or query-text inputs.
For unsupported fields, refresh discovery, correct the request once and retry.
Explain authentication or access errors without claiming the report succeeded.
