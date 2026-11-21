# Reading responses: warnings and errors

Several fields change what an answer may claim. Check them on every response.

## Warning fields

| Field | Where | What to do |
| --- | --- | --- |
| `text_available: false`, `content_warning` | `get_article` | No wording was retrieved. Say so; never reconstruct it. |
| `found: false` + `available_sections` | `@eu` `get_article` | Not an error envelope. Retry with a listed section or use `get_structure` (the list shows only 20). |
| `title_resolution` | `@hr` title URIs | The server chose one of several same-titled acts. Name the act you used; if it has `warning` / `in_force_until`, the act is no longer in force and a successor may be missing from the corpus. |
| `version_fallback` | `@hr` `get_full_document`, `get_structure`, `list_articles` | Act is repealed; the last version was served. Report its validity dates. |
| `version_note`, `base_celex` | `@eu` | A consolidated text was served instead of the original act. Cite the version you read. |
| `consolidation_warnings` | `@hr` `get_article`, `get_chapter` | The server repaired the consolidated text (misplaced points, duplicated paragraph); `excluded_text` shows what it removed. Mention it when quoting the affected paragraph. |
| `is_current_version`, `regulation_in_force` | `@hr` `get_article` | `in_force` describes the version, not the act. A future-only act may be served with `in_force: false` and no note. |
| `status_note` | `@hr` `get_status` `at_date` | `version.status` is the version's status today, not on that date. |
| `low_relevance_filtered`, `scope_errors`, `scope_status.degraded` | `search` | Some scopes returned nothing confident or failed. Report it as a coverage gap. |
| `profile_note`, `mode_coerced` | `search`, `get_status` | The fast profile changed the request; mention it if it matters. |
| `applicable: false` | `eu_transposition` | The act is a regulation or decision; nothing is transposed. |
| `available: false` | `eurostat_query` | No data; see `attempted_filters`. Not an error envelope. |
| `chronology_warning` | `get_decision` related decisions | The link between decisions may be wrong. |

## Error envelope

Errors look like `{error, error_type, scope, retryable, details}`.

| `error_type` | Meaning | Recovery |
| --- | --- | --- |
| `not_found` | No such act, article or version. The message is generic. | `@hr`: use the official Croatian title, or `resolve`. Repealed act with `get_article` / `get_chapter`: pass `as_of` within its validity. `@eu`: find the CELEX with `search`. |
| `ambiguous` | Several acts or decisions match. | Show `alternatives[]` / `candidates[]` and ask, or pass `as_of` when the date decides it. |
| `unsupported_capability` | The scope lacks this tool or parameter. | Expected. Use another tool or scope from [scopes.md](scopes.md), or state the limit. |
| `validation` | Bad parameter (date format, missing `as_of`, wrong country). | Read `details` (`candidates`, `accepted_codes`, `available_chapters`) and fix. |
| `upstream_timeout`, `upstream_5xx` | Backend slow or down; `retryable: true`. | Retry once. Then report the failure — do not infer that nothing exists. |
| `upstream_4xx` | Backend rejected the request (for example `limit` too high, `date_from` not before `date_to`). | Fix the parameter; do not retry unchanged. |
| `scope_unknown` | The scope is not connected to this server: a misspelling, or a real jurisdiction code (for example `@de`, `@si`) that is not wired yet. | Use a scope from `list_scopes`. Say which jurisdiction is unavailable; never substitute another country's law for it. |

## Quota

A quota message ("MCP quota exceeded: N tool calls/day on the … plan. Resets
at 00:00 UTC.") ends retrieval for the day. Tell the user, mention that a
higher plan raises the limit, and do not continue from memory as if you had
retrieved the law.

## Known data limits

- Croatian consolidated texts can still show a paragraph that a later
  amendment deleted ("briše se"). When the answer turns on whether a specific
  paragraph still applies, check `get_status` history for the amending act,
  or `get_full_document`, which includes the editorial notes.
- Point-in-time lookups resolve version boundaries by calendar day (Croatian
  time), so keep the requested date. Entry-into-force dates are taken from the
  gazette and can be wrong for an individual version; when the answer turns on
  the date, confirm it in the amending act via `get_publication`.
- EU text is English only. Translate if asked and say it is a translation.
