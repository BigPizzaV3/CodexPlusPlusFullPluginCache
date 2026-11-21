---
name: eu-to-national-law
description: Trace an EU directive to the national measures a member state reported as implementing it and its available transposition deadline, including NIS2, CSRD and the Whistleblower Directive. Open national text where supported. Distinguish a notification from complete, correct and timely implementation; EU regulations are not transposed.
license: Proprietary — see https://eulex.ai/legal
metadata:
  compatibility: Requires the EULEX.AI MCP connector (https://mcp.eulex.ai/mcp) to be connected and authorised. Without it none of the retrieval steps can run.
  author: Augment Ltd
  version: "1.3.14"
---

# From EU directive to national implementation

A directive binds member states as to the result; what a business must follow
is the national measure. Answering with the directive alone misses the
operative rule.

Use the tools of the EULEX.AI connection (`https://mcp.eulex.ai/mcp`) with
the exact names the host shows. If it is unavailable, say retrieval needs it.

## 1. Get the reported measures — one call

`eu_transposition(celex: "NIS2", member_state: "HR")`

- `celex` accepts a CELEX (`32022L2555`), `Directive (EU) 2022/2555`,
  `Directive 95/46/EC`, or the short names NIS2, CSRD, CSDDD, PSD2, MiFID2,
  Solvency2, CRD and Whistleblower Directive. Any other name returns
  `validation` with `details.candidates`; find the CELEX with
  `search(query: ..., scopes: ["@eu"])` and call again.
- `member_state` accepts `HR`, `HRV`, `Croatia`; Greece is `EL` or `GR`.
  Only the 27 member states. Omit it for all 27 — a large response, so pass a
  country whenever the user named one.
- The first call takes 1–10 s and is then cached. `upstream_timeout` is
  retryable once; after that report the failure — never conclude that no
  measures exist.

**A regulation is not transposed.** For a regulation or decision the
response has `applicable: false` and a `note`: the act applies directly. Say
that, and look for national provisions on supervision or penalties with
`search` with the requested supported national scope instead.

## 2. Read the result honestly

- `deadline` is the earliest transposition date only. Some directives have
  staged deadlines; `get_status(uri: "@eu/<CELEX>", mode: "history")` lists
  every `TRANSPOSITION_DEADLINE` event when the timeline exists.
- Per country: `status` (`reported_measures_found` /
  `no_reported_measures_found`), `nim_count`, and `national_measures[]` with
  `title`, `notification_date` and sometimes `nn_reference`.
- `predates_directive: true` marks an older law re-notified for this
  directive; it is part of the picture, not a new measure.
- Compare `notification_date` with `deadline` to say whether reporting was
  on time. Notification date is not the law's entry-into-force date.

## 3. Open the national law, where the corpus has it

- **Croatia (`@hr`).** Address the act by the title in the measure, without
  the gazette part: `get_article(uri: "@hr/Zakon o kibernetičkoj sigurnosti",
  article: ...)` or `get_structure`. If that fails, open the gazette issue
  with `get_publication(uri: <nn_reference>)` and take the matching item's
  `regulations[].uri`. Then `get_status` — implementing acts are often
  amended after transposition.
- **Germany, Slovenia, Netherlands (`@de`, `@si`, `@nl`).** Use `resolve` on
  the reported title or a verified abbreviation, select the matching canonical
  act, then retrieve its operative article and recorded status. Do not treat a
  title similarity as proof of implementation.
- **France (`@fr`).** Only codified provisions are available; match the
  measure to a code and article if you can, otherwise give the reported
  reference.
- **Any other member state.** Report the measures and their references, and
  say clearly that the connector does not hold that country's legislation.

## 4. Compare only retrieved texts

Saying that national law goes further than the directive (gold-plating)
compares two provisions, so fetch both: the directive's article with
`get_article` on `@eu` (English text) and the national article on its scope.
If you could not retrieve both, say the comparison was not possible.

## Data limits to disclose

Transposition data is what member states reported to the Commission. It can
lag, list superseded measures, or miss some. Present it as the reported
position, not as proof of complete or correct transposition — and never as a
compliance assessment. Some directives are missing from the EU text corpus
(`get_article` returns `not_found`) although `eu_transposition` still works;
say so if that happens.

## Output

- The directive: CELEX, title and deadline.
- The reported national measures for the requested member state(s), with
  notification dates and timeliness.
- For Croatia, the implementing provision quoted and cited, with status.
- Coverage limits, where a country is outside the corpus.

## Do not

- Do not present the directive's article as the rule a business must follow.
- Do not treat an empty result as proof that a state failed to transpose.
- Do not call this legal or compliance advice.
