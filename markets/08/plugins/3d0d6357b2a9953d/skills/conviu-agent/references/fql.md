# FQL — filter & condition syntax

**FQL** (Feed Query Language) is the small query string Conviu uses to select items. It is **not
SQL** — `SELECT`, `WHERE`, `LIKE` and bare `=` do not exist, and `%` is **not** a wildcard (the
wildcard is `*`; in an export rule's `conditions` a `%name%` token is a Conviu variable, see below).
You write FQL wherever a tool takes:

- a `filter` — on list tools: `list_items`, `list_data_sources`, `list_data_writer_jobs`
- `conditions` — on export rules

## Discover the fields first

A term addresses a **field** (column). Never guess field names — they depend on the data. Get the
real ones from actual data: call `list_items` (no filter, small limit) and read the keys of the
returned item `data`, plus `customData` and `variables`. Common product fields include `title`,
`brand`, `salePrice`, `inStock`; two special paths are always available: `dataSource.uid` (which
import an item came from) and `approval` (its approval status). Field paths may be nested with a dot
(`dataSource.uid`).

## Values: quoting, escaping, case

- Every value is wrapped in **double quotes**: `brand:"Nike"` — even numbers and booleans
  (`salePrice:["100" TO *]`, `inStock:"true"`).
- Escape an inner double quote as `\"` (and a literal backslash as `\\`).
- Matching is **case-insensitive by default**. Append **`#s`** for a case-sensitive comparison. The
  flag attaches to the value part and works on equality, the text matches, and sets:
  `brand:"Nike"#s`, `title:"*shoe*"#s`, `brand:("Nike;Adidas"#s)`.

## Operators

`field` is the column. Each row shows the exact FQL the operator produces.

### Equality

| Intent | FQL |
|---|---|
| Equals | `field:"value"` |
| Not equals | `NOT field:"value"` |

### Text match (TEXT / ARRAY fields)

| Intent | FQL |
|---|---|
| Contains | `field:"*value*"` |
| Not contains | `NOT field:"*value*"` |
| Starts with | `field:"value*"` |
| Ends with | `field:"*value"` |
| Not starts / not ends | `NOT field:"value*"` / `NOT field:"*value"` |

### Set — value in a list (OR within one field)

Values are separated by **semicolons** (`;`), inside quotes and parentheses:

| Intent | FQL |
|---|---|
| In a set | `field:("a;b;c")` |
| Not in a set | `NOT field:("a;b;c")` |

### Regular expression (TEXT / ARRAY fields)

The pattern is wrapped in tildes inside the quotes:

| Intent | FQL |
|---|---|
| Matches regex | `field:"~pattern~"` |
| Doesn't match | `NOT field:"~pattern~"` |

### Numeric / date comparisons (open-ended ranges)

The meaningful bracket sits on the **value** side: `[` / `]` inclusive, `{` / `}` exclusive; `*` is
the open end.

| Intent | FQL |
|---|---|
| ≥ x | `field:["x" TO *]` |
| ≤ x | `field:[* TO "x"]` |
| > x | `field:{"x" TO *]` |
| < x | `field:[* TO "x"}` |

### Between two bounds

| Intent | FQL |
|---|---|
| a ≤ v ≤ b (inclusive) | `field:["a" TO "b"]` |
| a < v < b (exclusive) | `field:{"a" TO "b"}` |
| a ≤ v < b | `field:["a" TO "b"}` |
| a < v ≤ b | `field:{"a" TO "b"]` |

### Advanced: length modifier `#L`

Compares the value's **character length** rather than the value itself, via a trailing `#L`:
`field:"5"#L` (length equals 5), `field:{"5" TO *]#L` (length greater than 5),
`field:[* TO "5"}#L` (length shorter than 5). Use it only when you specifically need to filter by
how long a text field is.

## Combining terms

Join conditions with **`AND`** and **`OR`**; negate a single term by prefixing its field with
**`NOT`** (`NOT brand:"Nike"`). The canonical shape — what Conviu's own filter builder emits — is:
OR-alternatives grouped in parentheses, **every group** wrapped and joined by `AND`:

```
(brand:"Nike" OR brand:"Adidas") AND (salePrice:["100" TO "500"]) AND (inStock:"true")
```

The rules Conviu's builder follows:
- **A lone condition stays bare** — no parentheses needed: `brand:"Nike"`.
- **Combining two or more? Wrap each group in `(...)`** and join with ` AND ` (or ` OR `) — including
  groups that hold just one condition. That's why `(inStock:"true")` above is parenthesized.
- `AND` binds groups of `OR` alternatives — put one field's OR options together inside one set of
  parentheses.

Filters without the per-group parentheses still parse, but emit the canonical form above: it stays
unambiguous as conditions get added.

## Worked examples

Combined filters use the canonical per-group parentheses; single-condition filters stay bare.

- Nike or Adidas, priced 100–500, in stock:
  `(brand:"Nike" OR brand:"Adidas") AND (salePrice:["100" TO "500"]) AND (inStock:"true")`
- More expensive than 1000 (strictly greater), in stock:
  `(salePrice:{"1000" TO *]) AND (inStock:"true")`
- Strictly between 100 and 500, brand exactly "Nike" (case-sensitive):
  `(salePrice:{"100" TO "500"}) AND (brand:"Nike"#s)`
- From one specific import, awaiting review:
  `(dataSource.uid:"<uid32>") AND (approval:"pending")`
- Title mentions "sleva" but is NOT clearance:
  `(title:"*sleva*") AND (NOT title:"*výprodej*")`
- Title longer than 70 characters — `filter` only, see the note on `#L` below (single condition, no
  parentheses): `title:{"70" TO *]#L`
- SKU matching an exact pattern (regex), case-sensitive:
  `sku:"~^AB[0-9]{4}$~"#s`
- One of several ids:
  `id:("101;102;103")`

## Fields inside an export rule's `conditions`

A rule's `conditions` are FQL too, but the **field** is written differently than in a `filter`, and
there are exactly two valid forms. Anything else is accepted by the server, stored happily, and then
**never matches a single item** — the rule looks fine and silently does nothing.

| Form | Reads | Where the exact spelling comes from |
|---|---|---|
| `%variable%` | the item's **source** data | `variables` in `get_data_writer_job` / `get_data_writer_job_rule` — copy `name` verbatim, percent signs included |
| `'Full > path'` | the **rendered output element**, i.e. after mapping into the format and after every rule with a lower `position` | `fields` in `get_data_writer_job` — an exact map key, in single quotes, never shortened to its last segment |

Prefer `%variable%`: it reads the source data, so it does not depend on the output format or on the
order rules run in. Reach for `'Full > path'` only when the question really is about the finished
feed, or when no variable fits.

```
(%price-vat%:{"250" TO *]) AND (%productname%:"*protein*")
'item > g:title':"*Akce*"
```

A bare name (`price-vat`, `title`) is the mistake to watch for — it is neither form, so it resolves
to nothing. `list_data_queries` does not return either catalogue; `get_data_writer_job` does.

Three further limits apply to rule `conditions` and not to `filter`:

- **No closed ranges.** Write `["500" TO *]` and `[* TO "1000"}` as two separate terms instead of
  `["500" TO "1000"]`.
- **`#L` and `#W` are ignored.** They work in a `filter`, but a rule's condition evaluator reads
  only the `#s` flag.
- **Keep the canonical shape.** Wrap every AND-group in parentheses, even a single one, and keep the
  spacing exactly as shown above — Conviu's visual rule editor can only display a condition it can
  re-encode character for character, and quietly drops any term it cannot.

## Common mistakes to avoid

- **SQL habits.** `LIKE`, `WHERE` and bare `=` don't exist — use `field:"value"` and the wildcards
  above. `%` is not a wildcard either; the only meaning of `%` in FQL is a `%variable%` token inside
  an export rule's `conditions`.
- **Missing quotes.** Every value is double-quoted, including numbers and booleans.
- **Guessing field names.** Verify against real items first — a filter over a non-existent field matches nothing.
- **Wrong range bracket.** `>` needs the exclusive `{`; `≥` needs the inclusive `[`. Mixing them shifts the boundary by one.
- **Commas in a set.** The set separator is `;`, not `,`.
- **`#s` in the wrong place.** For a set it goes inside the parentheses (`field:("a;b"#s)`); elsewhere it trails the closing quote (`field:"value"#s`).

## Sorting (alongside filters)

List tools also accept a `sort`, separate from the FQL filter. For `list_data_sources` and
`list_data_writer_jobs` it's a single object `{ field, order }`; for `list_items` it's an array of
such objects. `order` is `"ASC"` or `"DESC"`, e.g. `{ "field": "lastImportedAt", "order": "DESC" }`.
The filter selects; the sort orders.
