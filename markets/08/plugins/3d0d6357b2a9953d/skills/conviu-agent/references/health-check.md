# Health check — is everything running?

For "is my account OK?", "check my e-shops", "did anything break overnight?", or an agency asking you
to sweep every organization they manage. This is a **read-only** sweep: gather, summarise, then offer
to fix — never fix across the board on your own.

## Start with the modules — it's the fastest signal

`get_organization_modules` (`organizationUid`, optional `locale`) returns the status of **every**
Conviu module the organization uses — product import/export, pricing calculator, bidding, competition
monitoring, marketplaces, PPC advertisement — the same overview the Conviu dashboard shows. Per
module you get:

- `code` — internal module id; `title` — the human name (localised)
- `status` — **`error` | `warning` | `success` | `info`** (lowercase)
- `statusMessage` — a short human explanation
- `lastUpdatedAt` — when the module's state was last refreshed
- `dataObjectDefinitionType` — which data kind it concerns
- `primaryMessages` — actionable alerts, each with `message` and `type`

Pass `locale` (format `xx-xx`, e.g. `cs-cz`) so the titles and messages come back in the user's
language — **`whoami` returns their locale**. One call answers "how is my organization doing?"; only
drill deeper into what it flags.

## Single organization

1. **`get_organization_modules`** — anything with `status` `error` or `warning` is your shortlist.
2. **Drill into what it flagged**, not everything:
   - import/export trouble → `list_data_sources` / `list_data_writer_jobs`, then `diagnose.md`
   - feed rejected by a platform → `validation.md`
3. **`get_organization`** if the question is commercial rather than technical — it carries
   `active`, `hasOverdueInvoice`, `subscriptionEndDate`, `daysBeforeSubscriptionEndDate` and item
   limits. An expiring subscription or an overdue invoice explains a lot of "it stopped working".
4. **Summarise in plain words**, worst first, then offer the fix.

## Many organizations (agencies)

**`whoami` tells you if this is an agency account** — it returns `agencyAccount` alongside `email`,
`name`, `locale` and `timezone`. When it's true, sweeping several organizations is a natural offer.

1. **`whoami`** → agency? which locale?
2. **`list_organizations`** — supports `search`, `sort` (`name` / `createdAt` / `active`), and
   `offset` / `limit`. Returns each organization's `uid`, `smallUid`, `name`, `active`, plus
   `totalCount`. **Check `totalCount`** — if it exceeds what you fetched, say so rather than
   implying you covered everything.
3. **Per organization: `get_organization_modules`.** This is the sweep. One call per organization
   gives you every module's status.
4. **Report a compact table**, problems first: organization → which module → what's wrong. Do not
   dump raw JSON or a per-module list for healthy organizations — "9 of 12 are fine" is the useful
   sentence.
5. **Offer to drill into the worst one.** Fix one thing at a time, with consent each time.

### Keep the sweep proportionate

A sweep is one call per organization — with 30 organizations that's 30 calls and a lot of output. So:

- **Ask first if the list is long.** "You have 34 organizations — sweep all of them, or the ones you
  care about most?" Beats burning the context on everything.
- **Narrow with the tools you have** — `list_organizations`'s `search` for a subset, `limit` for a
  first pass, and FQL `filter` on the list tools (e.g. `active:"false"`) when you drill down. See
  `fql.md`.
- **Skip inactive organizations** unless asked — an organization with `active:"false"` isn't running
  anything and isn't news.
- **Say what you didn't check.** Silently covering 20 of 34 and reporting "all good" is worse than
  useless.

## What "unhealthy" looks like

| Signal | Where | Means |
|---|---|---|
| `status: "error"` | module | Something is actively broken — start here. |
| `status: "warning"` | module | Degraded or needs attention soon. |
| `active: false` | import / export / org | It never runs. A very common "why is my feed old?". |
| `lastWrittenAt` / `lastImportedAt` far in the past | export / import | Stale — compare against today's date from context. |
| `itemCount: 0` | export | Empty or blocked feed → `diagnose.md`. |
| `hasOverdueInvoice: true`, subscription expiring | organization | Commercial cause behind technical symptoms. |

## Rules for the sweep

- **Read-only by default.** Gathering status changes nothing; fixing does. Never fire `trigger_*`,
  `set_*_active` or an update across organizations off your own bat — propose per item, act on consent.
- **Don't infer fields you weren't given.** If a tool didn't return it, you don't know it.
- **Translate, don't dump.** Status codes and timestamps become "your pricing module has been failing
  since yesterday morning". No raw JSON, no code names.
