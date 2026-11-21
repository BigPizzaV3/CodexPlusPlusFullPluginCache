# Concepts, glossary & identifiers

Understand the setup before you change anything. This file is the mental model behind every
other reference.

## The data flow

```
[E-SHOP / SUPPLIER]  →  IMPORT  →  items in Conviu  →  EXPORT  →  [Platform / channel]
```

An **import** brings data in; an **export** sends data out. They are independent objects, each
with its **own schedule and its own run history**. Most "my feed is wrong" problems come down to
figuring out whether the import or the export is at fault — establish that first.

## Glossary (internal name → what to call it with users)

| Internal name (in tools/data) | Talk to users about it as | What it is |
|---|---|---|
| Data source | **Import** | A configured feed that pulls products/orders INTO Conviu on a schedule. |
| Data writer job | **Export** | A job that writes items OUT in a chosen format for one platform. |
| Item | **Product** (or order) | A single record living in Conviu after an import runs. |
| Data query | **Product selection / source** | A saved selection of items. Every import has one; an export draws from one or more. |
| Data writer job rule | **Export rule** | A transformation/condition applied to items within an export. |
| Format | **Feed format** | The platform-specific shape of a feed (Zboží.cz, Heureka, Google, a Custom format…). |
| Reader | **Connection** | How an import fetches data: URL download, FTP/SFTP, Google Sheet, file upload, web service, marketplace API. |
| Writer | **Destination** | Where an export delivers: Conviu internal storage (the default) or FTP / a connector. |

Use the human words with users. Reserve the internal names for tool arguments and for reasoning.

## Object type: product vs order

Almost everything is scoped to an **object type**, usually `product` or `order`. Price-comparison
and marketplace feeds (Zboží.cz, Heureka, Google, Glami, Favi…) are **product** feeds. Infer the
type from context; ask only when genuinely ambiguous.

## Identifiers — never invent them

- **UID32** — a 32-character id used for most entities (organizations, imports, exports, rules, and
  an item's `dataSourceUid`). Parameters named `uid`, `organizationUid`, `dataSourceUid`,
  `dataWriterJobUid`, etc. expect a UID32. Note: a Conviu uid is 32 lowercase alphanumerics with at
  least one digit — it is **not** hex, so don't validate it as `[a-f0-9]{32}`.
- **smallUid / UID10** — a 10-character id. Used for organizations in URLs and for feed formats
  (`formatSmallUid`).

Always discover real ids first (`whoami`, `get_organization`, `list_data_sources`,
`get_data_source_formats`, …) and copy them verbatim. Never guess or hand-build an id.

## Discovery-first for restricted values

These parameters only accept specific server-side values — fetch them, then use a returned value
exactly:

| Parameter | Discover with |
|---|---|
| `formatSmallUid` | `get_data_source_formats` (or `detect_feed_format` when you have a feed URL) |
| `readerType` | `get_data_source_readers` |
| `writerType` | `get_data_source_writers` |
| `connectorAccountUid` | `list_data_connector_accounts` |
| `objectDefinitionType` | the object kind, typically `product` or `order` |

The import `configuration` JSON is shaped per the chosen reader — its exact keys come back as a
`configurationSchema` on each `get_data_source_readers` entry (note which are required, defaulted,
or sensitive). Some types take no configuration (pass `{}`).

## Finding the right account and item

Start from the caller and drill down — never assume which org or item is meant:

```
whoami
  → get_organization / list_organizations      (which organization?)
      → list_data_sources        (imports)   ─┐
      → list_data_writer_jobs    (exports)    ├─ match the one the user means BY NAME
      → list_data_queries        (sources)    │
          → get_data_source / get_data_writer_job / get_data_writer_job_rule   (detail)
```

If the user is already looking at a specific item and its id is in context, use it — don't re-list.
If several could match, ask one short question offering the candidates by name.

## The data you need may already be in Conviu

Before reaching for anything external, check what's already imported: `list_items` (with an FQL
`filter`) shows the real products and their fields; `get_data_source` /
`get_module_jobs_by_data_source` show how an import feeds downstream exports. The answer to
"which products are affected" is usually one `list_items` call away.

## Help documentation (how-to / conceptual questions)

For "how do I…", "what does X mean", or troubleshooting questions about **using Conviu** (features,
settings, step-by-step guides), call `search_documentation` with the user's question and answer
from the returned passages — cite the page by its public URL, and use `get_documentation_page`
for the full text when needed. This is general product knowledge; keep using the data tools for the
caller's own imports, exports, and items.
