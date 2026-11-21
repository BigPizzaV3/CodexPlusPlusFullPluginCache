---
name: point-in-time-law
description: Research the wording and available amendment history of a provision at the time of an event, contract, dispute or tax period. Use for questions such as what the law said in 2015 or what changed between versions. Dated text is available for Croatia, France, Slovenia and the Netherlands where indexed; EU timelines and German snapshots have distinct limits. Do not replace unavailable historical text with current wording.
license: Proprietary — see https://eulex.ai/legal
metadata:
  compatibility: Requires the EULEX.AI MCP connector (https://mcp.eulex.ai/mcp) to be connected and authorised. Without it none of the retrieval steps can run.
  author: Augment Ltd
  version: "1.3.14"
---

# Reading a provision as it stood on a date

Disputes are decided under the law in force at the time, not today's text.
Today's wording is usually plausible, so returning it for a past date is a
confident error that nobody notices.

Use the tools of the EULEX.AI connection (`https://mcp.eulex.ai/mcp`) with
the exact names the host shows. If the connection is unavailable, say that
retrieval needs it; never answer a historical question from memory.

## First: fix the date and check support

Use the date of the legally relevant event (contract, damage, dismissal, tax
period), not the date of a later judgment. Ask only if the date is unclear and
would change the answer.

| Scope | Text on a date | Timeline |
| --- | --- | --- |
| `@hr` Croatia | Yes — `as_of` or `version_id` | Yes — `get_status` |
| `@fr` France | Yes — `as_of` | Only the returned version's own window |
| `@si` Slovenia / `@nl` Netherlands | Available versions with `as_of` or `version_id` | Recorded versions via `get_status` |
| `@de` Germany | Snapshot ID only; no arbitrary historical date | Recorded snapshots, not validity history |
| `@eu` EUR-Lex | **No** — `unsupported_capability` | Events and consolidated versions |

## Croatian law

1. **Get the text on the date** in one call:
   `get_article(uri: "@hr/Zakon o radu", article: "112", as_of: "2015-01-01")`.
   With `as_of`, a title shared by several acts resolves to the one valid on
   that day (see `title_resolution`). Keep the returned
   `regulation_version_id` and `citation` (the gazette chain) for the label.
2. **Decide whether it changed** — compare texts, never infer it from a
   version count. Fetch the current article (`get_article` without `as_of`)
   and compare it with the step-1 text; the two `regulation_version_id`
   values tell you whether the act was amended in between, the text
   comparison tells you whether *this article* changed (an amendment may have
   touched other articles only). `get_status(uri, mode: "in_range",
   date_from, date_to)` is auxiliary history: it lists versions active on at
   least one day of `[date_from, date_to)` — `date_to` itself is **not
   included**, so pass the day after the last date you care about. One
   version in the range means no new version started inside it; it proves
   nothing about `date_to`. If `regulation_in_force` is false, the act was
   later replaced: today's rule is in a successor act with the same or a new
   title, so compare with that act instead.
3. **Name the amendment.** `get_status(uri, mode: "history")` lists every
   version with the Narodne novine item that produced it
   (`publication.nn_reference`). `get_publication` on that reference shows the
   amending act. When the law was re-enacted under the same title (Zakon o
   radu 1995, 2009, 2014), add `consolidate: true` for the whole lineage.

Pitfalls:

- Do not combine a pinned `/version/{id}` URI with a different `as_of`. Rebuild
  `@hr/regulation/{uuid}` and pass `article` and `as_of`.
- `get_article` on a repealed act without a date returns `not_found`; pass an
  `as_of` inside its validity.
- `as_of` before the first version returns `not_found`: the act did not yet
  exist in that form.
- `get_status` `at_date` reports `version.status` as of today; read
  `status_note`. `in_range` needs `date_from` earlier than `date_to`.
- Version boundaries are resolved by calendar day (Croatian time): on the
  day a version entered into force, that version is returned. Keep the
  requested date. If the returned `citation` or `regulation_version_id`
  disagrees with `get_status` history, report the discrepancy; do not try a
  neighbouring date as a substitute.
- A consolidated version can still show a paragraph that the amendment
  deleted ("briše se"). If the question turns on one paragraph, confirm with
  the amending act via `get_publication`.

## French codes

`get_article(uri: "@fr/code/Code civil", article: "1240", as_of: "YYYY-MM-DD")`
returns the version with `date_debut ≤ as_of < date_fin`. Report that window
— it states from when to when this wording applied (`2999-01-01` means still
open). For a comparison, fetch again without `as_of` and compare. A search URI
ending in `/v/{LEGIARTI}` pins a specific version. Conflicting selectors are rejected;
remove the version suffix before querying another date. There is no list of all versions,
so do not claim a full amendment history.

## EU law: the tool refuses historical text, and that is correct

`get_article` and `get_structure` on `@eu` reject `as_of` and `version_id`.
Do not work around it or quote today's text as past text. Give what the
corpus can establish:

- `get_status(uri, mode: "history")` — dated events: entry into force,
  application dates, transposition deadline, end of validity. If it returns
  `not_found`, the timeline is missing for that act; use `mode: "current"`.
- `get_status(uri)` — `consolidated_versions[]` with `version_date` and
  `in_force`; tell the user which consolidated CELEX covers the event date so
  they can open it on EUR-Lex.
- `get_related(uri, relation_type: "amendments")` — the amending acts. Pass
  the base CELEX, not a consolidated one.

You may say that no amendment is recorded in the corpus after the date; do not
say the text is unchanged.

## Slovenian and Dutch law

Use `get_article` with the canonical act or abbreviation and `as_of`. Preserve
`version.version_key`, `valid_from`, `valid_to` and the official source URL.
Use `version_id` to reproduce that exact retrieved version. Compare actual texts;
a new version of the act need not change the requested article. Missing intervals
or rejected dates are limitations, never permission to substitute current text.

## German federal law

`get_status(mode: "history")` lists available consolidation snapshots. Retrieve
one by `version_id`; label it as a snapshot and retain its source Stand note.
The connector rejects `as_of` because snapshot dates do not prove legal validity
on the user's historical date. State that limit instead of asserting past law.

## Inspect the retrieved historical source

Use `view_source` with the returned version-qualified `sources[].id` to open the
wording. Do not combine a pinned URI with `as_of`; the returned ID already fixes
the version. Context mode must retain that version. A viewer status such as
"Not recorded as in force" may describe the version today, not the requested
past date: explain the validity dates and `get_status.status_note` separately.
France remains article-only. Keep ordinary citations if the host cannot render.

## Output

- The wording that applied on the date, quoted and labelled with the date and
  version (gazette chain, LEGI window, or EU consolidated CELEX).
- Whether it differs from today's wording, based on a real comparison of the
  two retrieved texts.
- The amending instrument, when the user asks what changed it.
- For `@eu`, the timeline plus an explicit statement of the limit.

## Do not

- Do not present current text as historical text.
- Do not infer past wording from an amendment's title or description.
- Do not treat the `@eu` refusal as an error to route around.
