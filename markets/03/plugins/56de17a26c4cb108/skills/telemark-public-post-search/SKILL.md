---
name: telemark-public-post-search
description: "Use when a user wants a bounded keyword search of recent public posts on a decentralized social network."
---

# Telemark Public Post Search

Use this skill only for bounded, on-demand keyword searches of recent public posts. It does not access private posts, search by private identity, create webhooks, reset state, or keep monitoring after the conversation ends.

## Search workflow

1. Require at least one complete keyword or phrase. Keep each quoted multi-word phrase in one `keywords` array item; never split its words. Multiple array items use OR semantics.
2. Map the user's language filters and exclusions exactly.
3. If the user asks for all, every, unlimited, or no-limit results without a positive numeric cap, do not call a tool. Explain the 100-result maximum and ask the user to choose a cap from 1 to 100.
4. Keep `maxResults` explicit and no greater than the user's requested cap. Use 3 for a small preview.
5. Call `search_public_social_posts`. Telemark Digital funds this bounded search; the user is not charged and no user execution account is connected. Availability is subject to the shared daily and monthly capacity limits.
6. If the returned status is nonterminal, call `get_public_post_search_status` only with the signed `runId` from that search.
7. After status `SUCCEEDED`, call `get_public_post_search_results` only with the signed `datasetId` returned for the same run and a limit no greater than `maxResults`.

Recommended bounded input:

```json
{
  "keywords": ["technology"],
  "excludeTerms": [],
  "langs": ["en"],
  "maxResults": 3,
  "sort": "latest",
  "waitSecs": 45
}
```

Treat an empty result as valid when no public post matches. When a language filter is requested, return only posts that carry a matching declared language label; exclude unlabeled posts. Never invent posts or claim background monitoring.

This is an original bounded-search workflow, not a third-party account connector or arbitrary API pass-through. It uses a source-provided unauthenticated public-web API, then applies Telemark Digital's keyword, phrase, exclusion, declared-language, sorting, bounding, and result-minimization logic. It does not authenticate as a source user or perform likes, follows, replies, messages, or other source-account actions.

## Safety and privacy

Do not request private posts or attempt to bypass access controls. Do not request or transmit credentials, restricted data, sensitive personal data, webhook settings, or confidential source data. Returned rows are limited to the public post URL, text, publication time, language labels, and matched terms.
