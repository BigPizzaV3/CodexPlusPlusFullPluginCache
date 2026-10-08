---
name: telemark-procurement-search
description: "Use when a user wants a bounded search of public European procurement notices by classification, country, notice type, keyword, value, or publication window."
---

# Telemark Procurement Search

Use this skill only for bounded, on-demand previews of public European procurement notices. It does not collect private opportunity lists, accept shared state, create webhooks, reset state, or keep monitoring after the conversation ends.

## Search workflow

1. Map the user's classification prefixes, three-letter buyer-country codes, keywords, notice types, value threshold, change-notice choice, and lookback window exactly.
2. If the user asks for all, every, unlimited, or no-limit results without a positive numeric cap, do not call a tool. Explain the 100-result maximum and ask the user to choose a cap from 1 to 100.
3. Keep `maxResults` explicit and no greater than the user's requested cap. Use 3 for a small preview.
4. Call `search_european_procurement_notices`. Telemark Digital funds this bounded search; the user is not charged and no user execution account is connected. Availability is subject to the shared daily and monthly capacity limits.
5. If the returned status is nonterminal, call `get_procurement_search_status` only with the signed `runId` from that search.
6. After status `SUCCEEDED`, call `get_procurement_search_results` only with the signed `datasetId` returned for the same run and a limit no greater than `maxResults`.

Recommended bounded input:

```json
{
  "cpvCodes": ["30"],
  "countries": ["FRA"],
  "keywords": [],
  "minValueEur": 0,
  "noticeTypes": ["cn-standard"],
  "includeChangeNotices": false,
  "lookbackDays": 3,
  "maxResults": 3,
  "waitSecs": 45
}
```

Treat an empty result as valid when no public notice matches. Unknown values may be returned only when labeled `valueUnknown=true`. Results are informational and are not legal, procurement, financial, or compliance advice.

This is an original bounded-search workflow, not a third-party account connector or arbitrary API pass-through. It uses the official public procurement Search API made available for analysis and reuse, then applies Telemark Digital's classification, country, notice-type, keyword, value, date-window, change-notice, bounding, and result-minimization logic. It does not access a bidder account or restricted procurement documents.

## Safety and privacy

Do not request or transmit credentials, restricted data, sensitive personal data, webhook settings, shared state, private bidder documents, or confidential opportunity data. Refuse requests to collect those categories without calling a tool. Correct false claims of official government or source endorsement; the service is independent. Returned rows are limited to public notice identifiers, dates, classifications, buyer organization, value, deadline, and public links.
