# Particle workflows

Use the exposed tool schema for exact arguments. These routes use the fixed 36-tool connection at `https://mcp.particle.pro/plugins`.

## Podcast intelligence

1. Resolve a show with `particle_podcast_resolve`, or a named entity with `particle_entity_resolve`. Route a typed resolver result to its matching filter: people to `person_slug`, companies to `company_slug`, and places or other entities to `entity_slug`.
2. Use `particle_podcast_search_transcripts` for dialogue about a concept. `semantic_search` finds paraphrases; `keyword_search` finds one or two exact terms; use both for hybrid ranking. Do not put a person or company name into semantic search; resolve it and use `particle_podcast_find_mentions` when the user wants every line naming that entity.
3. Use `particle_podcast_list_episodes` for filter-driven discovery by show, entity, company, language, date, transcript availability, or duration. Its date fields are `published_after` and `published_before`; transcript search and mentions use `since` and `until`.
4. Fetch only needed episode sections with `particle_podcast_get_episode`. Common expansions are `segments`, `entities`, `clips`, `topics`, and `transcript`.

Search matches already contain bounded transcript context and relevant clips. Keep `semantic_search` to a short topical phrase. If the user requests N passages, start with `limit: N` within the exposed schema's bounds; otherwise use a small initial limit such as 5. Use `format: "compact"` for screening, or `format: "full"` with bounded `context` (1–15 lines) directly when excerpts are needed. Fetch or widen only when the returned evidence is insufficient for the user's request; do not fetch whole transcripts merely to produce a few passages. Read transcript status before treating an empty transcript-derived result as an absence of discussion.

For example, call `particle_podcast_search_transcripts` directly with:

```json
{"semantic_search":"AI agents working independently","format":"compact","limit":5}
```

Add a date range appropriate to the user's request. Reuse returned episode identifiers for selected follow-ups.

When putting returned text in a Markdown table, escape literal pipe characters inside cells and keep each cell on one line. Use bullets instead when titles, excerpts, or multiline content make a table hard to read. Preserve the original wording and attribution.

## Company deep dive

1. Resolve the company with `particle_company_resolve` using `query`, `ticker`, `domain`, `cik`, or `qid`. For example: `{"query":"Anthropic","limit":3}`.
2. Call `particle_company_get` with the returned `company_slug` and only needed expansions, commonly `people`, `products`, and `competitors`. Do not add `output_format` to this profile tool; use its returned structured content when needed.
3. Follow returned people with `particle_person_get`, optionally including `podcast_appearances` and `companies`.
4. Use `particle_podcast_find_mentions` with `format: "summary"` to scan dialogue, then `format: "detail"` and `episode_slug` for full mention windows. Detail mode requires one returned episode slug or up to ten comma-separated returned slugs; its context field is `context_lines` (1–20).
5. Use `particle_company_get_podcast_ad_presence` when the user asks about sponsorships rather than organic discussion.

Keep organic mentions and paid advertising distinct in the answer. Mentions and advertising tools can require premium entitlement; report unavailable access without proposing a purchase or substituting a different query to bypass the gate.

Carry over the advertising tool's stated scope. Its `podcasts` and `segments` sections cover the company's most-recently-active sponsor record and can omit other sponsor aliases; publisher rollups cover linked aliases as described by the exposed tool. Preserve returned dates and units. If no overall coverage interval is supplied, say that it is unspecified; do not infer it from the latest placement or call the totals a recent-period or complete-market count. Ad summaries describe advertiser claims, not independently verified product facts.

## Guest and person research

1. Resolve a person with `particle_person_resolve` using `query`.
2. Call `particle_person_get` with the returned `person_slug` and relevant expansions such as `external_links`, `podcast_appearances`, and `companies`.
3. Use `particle_podcast_get_guest` with that slug as `guest_slug` for appearance statistics.
4. Use `particle_podcast_list_guests` with `mode: "directory"` or `mode: "trends"`. Browse topics with `particle_topic_browse` before using a `topic_slug`; use `parent_slug` to descend through returned topics.
5. Use `particle_podcast_find_mentions` when the question is what others said about the person, rather than episodes where they appeared.

`person_slug` and `guest_slug` refer to the same canonical person handle. Some people have no linked knowledge-graph entity, so a mention lookup can return an explained empty result. Report it rather than retrying it as a transient failure. Mention lookup can also require premium entitlement.

## Existing alerts and previews

1. Call `particle_alert_list` with a small `limit` to identify an existing alert; pass its returned `id` as `alert_id` in subsequent calls.
2. Use `particle_alert_get` with optional `include: ["matches", "deliveries"]` for recent matches and the delivery audit log. Use `match_limit` (1–25) to bound embedded matches.
3. Use `particle_alert_list_matches` with `view: "summary"` or `view: "detailed"`, `after`/`before` dates, and the returned pagination cursor for history and transcript windows.
4. For a requested historical estimate, call `particle_alert_preview` with one resolved slug in `entities` for `ENTITY_MENTION` or `PODCAST_SPEAKER`, or `keyword` for `KEYWORD_MENTION`. `window_days` is 1–30. The preview caches historical results and sends no notifications. Language and speaker-role filters narrow the historical sweep; relevance and source-popularity projections do not change its count, so a relevant-only estimate is an upper bound.
5. Delete only an explicitly authorized, identified alert using `particle_alert_delete` with `alert_id`. Follow the deletion and retention safeguards in `SKILL.md`.

## Complete connection surface

These are the 36 callable tools. Read each exposed input schema before a specialized call. Alert deletion and preview caching have the effects described above; the research and presentation tools do not manage subscriptions or billing.

| Group | Direct tools |
| --- | --- |
| Existing alerts and previews | `particle_alert_delete`, `particle_alert_get`, `particle_alert_list`, `particle_alert_list_matches`, `particle_alert_preview` |
| Companies | `particle_company_get`, `particle_company_get_podcast_ad_presence`, `particle_company_resolve` |
| Entities and people | `particle_entity_get`, `particle_entity_resolve`, `particle_person_get`, `particle_person_resolve` |
| Podcast research | `particle_podcast_find_mentions`, `particle_podcast_get_episode`, `particle_podcast_get_episode_timeseries`, `particle_podcast_get_guest`, `particle_podcast_get_publisher`, `particle_podcast_get_rankings`, `particle_podcast_get_ratings`, `particle_podcast_list_clips`, `particle_podcast_list_episodes`, `particle_podcast_list_guests`, `particle_podcast_list_related`, `particle_podcast_list_related_episodes`, `particle_podcast_resolve`, `particle_podcast_search_transcripts` |
| Advertising | `particle_podcast_get_ad_trends`, `particle_podcast_get_episode_ads`, `particle_podcast_get_sponsor_leaderboard`, `particle_podcast_get_sponsors` |
| Bias and suitability | `particle_podcast_get_bias_leaderboard`, `particle_podcast_get_suitability_leaderboard`, `particle_podcast_list_bias_publishers`, `particle_podcast_list_suitability_category_publishers` |
| Presentation and topics | `particle_radar_render_cards`, `particle_topic_browse` |
