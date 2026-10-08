# Source registry — United Kingdom

Verification labels below are original author notes, not results of the Codex compatibility
review. Recheck every endpoint and claim at run time. HTTP status alone does not verify
content. Runtime behavior is governed by `runtime-safety.md`.


Every URL here was fetched and confirmed live on **2026-09-09**. A source that fails at scan time is
a named coverage gap.

---

## 1. legislation.gov.uk Atom feeds — `primary`, the anchor source

The official publisher of UK legislation. Feeds are free, need no key, and carry structured metadata.

| Feed | URL | Notes |
|---|---|---|
| All new legislation | `https://www.legislation.gov.uk/new/data.feed` | Verified 200. Most recent items across all types. |
| New on a given date | `https://www.legislation.gov.uk/new/uk/2026-09-08` | Verified 200. Date-addressable — use for a window. |
| UK SIs by year | `https://www.legislation.gov.uk/uksi/2026/data.feed` | Verified 200. |
| UK public general Acts by year | `https://www.legislation.gov.uk/ukpga/2026/data.feed` | Verified 200. |

### Entry metadata

Each Atom entry carries a `ukm:` namespace block, verified live:

- `ukm:DocumentMainType` — observed values in the live feed: `UnitedKingdomStatutoryInstrument`,
  `UnitedKingdomDraftStatutoryInstrument`, `ScottishStatutoryInstrument`, `WelshStatutoryInstrument`
- `ukm:Year`, `ukm:Number` — together the `official_id`, formatted `2026/912`
- `ukm:CreationDate` — the date the instrument was **made**, which is not the date it bites
- `ukm:Subject` — subject categorisation, useful for domain routing
- `ukm:ISBN`, plus `title`, `summary`, `published`, `updated`, and links to `data.xml`, `data.pdf`,
  `data.rdf`, and HTML

`source_url` ← the entry's HTML link (e.g. `https://www.legislation.gov.uk/uksi/2026/912`).

### Two traps worth taking seriously

**"Draft" is not law.** `UnitedKingdomDraftStatutoryInstrument` means laid before Parliament and not
yet made. Lifecycle stage is `proposed`. It may be amended or never made. Never report a draft SI as
though it were in force, and never diarise its indicative dates as obligations.

**"Made" is not "in force."** `ukm:CreationDate` is the making date. Commencement is set by the
instrument's own commencement provision, which may be a fixed date, a staged set of dates, or
"such day as the Secretary of State may by regulations appoint" — meaning **no date exists yet**.
You must open the instrument and quote the commencement article. If commencement is by appointed
day and no day is appointed, the correct output is `undated` with that fact stated. This is the
single most common UK error, and an invented commencement date is exactly the harm the citation
rules exist to prevent.

## 2. Consultations and policy — `primary` / `regulator`

| Source | URL | Notes |
|---|---|---|
| gov.uk open consultations (Atom) | `https://www.gov.uk/search/policy-papers-and-consultations.atom?content_store_document_type=open_consultations` | Verified 200. Machine-readable, covers all departments. |
| CMA (Atom) | `https://www.gov.uk/government/organisations/competition-and-markets-authority.atom` | Verified 200. Competition and consumer enforcement. |

The gov.uk Atom pattern generalises: append `.atom` to a department or organisation page for a feed.
Verify any new feed URL by fetching it before relying on it.

## 3. Regulators — `regulator`

| Body | URL | Domain |
|---|---|---|
| ICO news and blogs | `https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/` | data protection, AI |
| FCA news (RSS) | `https://www.fca.org.uk/news/rss.xml` | financial services |
| HSE news | `https://www.hse.gov.uk/news/index.htm` | health and safety |

All verified 200 on 2026-09-09. ICO and FCA guidance is not law; label it `regulator` tier and
describe it as supervisory expectation, not obligation — while noting that in practice it drives
enforcement.

## 4. Devolved legislation

`ScottishStatutoryInstrument` and `WelshStatutoryInstrument` appear in the main
`/new/data.feed` (verified). Northern Ireland instruments publish similarly.

Only report devolved instruments when the profile includes `UK-SCT`, `UK-WLS`, or `UK-NIR`, or when
the business has `physical_sites` or headcount there. If the profile has bare `UK` and a devolved
instrument looks materially relevant, surface it as a question about the profile rather than
assuming the footprint — employment and health-and-safety duties in particular turn on where people
actually work.

---

## Retained EU law

Post-Brexit, some UK obligations still derive from assimilated (formerly retained) EU law, which is
subject to its own programme of revocation and reform. When a finding touches an area with EU
origins, check whether the UK instrument amends or revokes assimilated law and cite the amending
instrument specifically. Do not reason from the EU version of a rule to its current UK content —
they have diverged, and citing the EU text for a UK obligation would be a sourcing error even though
the link resolves.
