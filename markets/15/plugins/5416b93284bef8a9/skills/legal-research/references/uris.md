# Addressing documents

Every document tool takes a `uri` that starts with a scope. Prefer the form
that needs no extra call: a name or number goes straight into the content
tool.

## Accepted forms

| Form | Example | Notes |
| --- | --- | --- |
| Croatian title | `@hr/Zakon o radu` | Official Croatian title; English names fail |
| Croatian title on a date | `@hr/Zakon o radu@2015-01-01` | Picks the act valid that day |
| Croatian id | `@hr/regulation/{uuid}` | From `search`, `resolve`, publications |
| EU short name | `@eu/GDPR`, `@eu/NIS2` | Only the names listed below |
| CELEX | `@eu/32016R0679`, `@eu/regulation/32022L2555` | Resource word is always `regulation`, also for directives |
| French code | `@fr/code/Code civil` | Exact code title, including capitals |
| Decision | `@hr/decision/{uuid}` | Or pass the case number to `get_decision` |
| Publication | `NN 14/2019-268` | Directly to `get_publication` |

**Put the article in the `article` parameter.** After a free-form name the
rest of the string is read as part of the name, so
`@hr/Zakon o radu/article/112` and `@eu/GDPR/article/17` fail. Full canonical
URIs returned by the tools (`@hr/regulation/{uuid}/article/112`,
`@eu/regulation/32016R0679/article/17`) can be reused as they are.

`@eu/directive/...` and `@eu/celex/...` are not valid.

## EU short names

`resolve` on `@eu` and free-form `@eu/<name>` URIs know only these acts:

GDPR · AI Act · DORA · NIS2 · DSA · DMA · Data Act · Data Governance Act (DGA)
· Cyber Resilience Act (CRA) · Chips Act · eIDAS · CSRD · Whistleblower
Directive · CSDDD · PSD2 · MiFID II · MiFIR · MAR · Solvency II · CRR · CRD ·
SFDR · Taxonomy Regulation

`resolve` matches substrings and always reports `in_force: true` without
checking; "MAR" can return DMA first. For any other act (VAT Directive, MiCA,
AMLD, EMIR, CBAM …) find the CELEX with `search(scopes: ["@eu"])` and use it.

## Article references

- `@hr` — `112`, `Članak 112`, `112.a`. Paragraph parts (`st. 3`) are stripped
  and the whole article is returned; locate the paragraph in `text`.
- `@eu` — `17`, `Article 17`, `6a`, an article title, `Recital 61`,
  `Annex III`, `Chapter IV`. `Art. 17` and `17(1)` fail.
- `@fr` — `L225-102-1`, `Article L. 225-102-1`, `R. 431-16`, `1240`.

No scope addresses individual paragraphs.

## Version pins

URIs returned by `search` are pinned to the version that matched:
`@hr/.../article/112/version/{id}` and `@fr/.../article/1240/v/{LEGIARTI}`.
A pin wins silently over `as_of`. For text on another date, rebuild the URI
without the pin (`@hr/regulation/{uuid}`, `@fr/code/{code}`) and pass
`article` and `as_of`.

## Ambiguity

- `resolve` returns `matches[]`, `ambiguous` and `best_guess` (a URI).
- Document tools return `error_type: "ambiguous"` with `alternatives[]`
  (`regulation_id`, `title`, `in_force`); build `@hr/regulation/{id}` from the
  one the user chooses.
- `get_decision` returns `candidates[]` when several courts share a number.

Croatian same-title acts are usually settled by the server: it takes the act
in force (or valid on `as_of`) and explains the choice in `title_resolution`.
Read that field — its `warning` says when no act with that title is in force.
