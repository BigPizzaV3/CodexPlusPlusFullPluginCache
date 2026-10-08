# Cross-industry domains

Five domains that touch nearly every business regardless of sector. Each has **applicability
triggers** expressed against `exposure_flags` in the profile, so relevance is decided mechanically
rather than by impression.

Every instrument below was verified on **2026-09-09**: EU by resolving the CELEX deep link and
reading back the document title, UK by fetching the `legislation.gov.uk` page and reading back the
title, US CFR parts by confirming the part in the eCFR structure API. Controls were run — a fake
CELEX returns 404, a fake UK instrument returns 400, a fake CFR part is absent from the structure
API — so these are positive confirmations, not just links that happened to load.

## How to use this file — read this first

These are **baselines, not current state.** An instrument listed here is the anchor you cite for
scope and obligation, but its text may have been amended since 2026-09-09, and several of these
regimes have been actively amended in ways that change thresholds and dates.

So: **never state a threshold, date, or obligation from this file as current.** Use it to know what
to look for and what to cite, then confirm the operative text from the source registry and quote
that. This file tells you where to look; it is not itself a source for a finding.

---

## 1. `privacy_ai` — data protection and artificial intelligence

**Triggers.** Engaged if `personal_data` is anything other than `none`, or if `ai_systems` is
anything other than `none`. Escalations:

- `personal_data` includes `health`, `biometric`, or `children` → special-category and
  child-specific regimes engage; treat impact as `high` or above by default
- `ai_systems` includes `in_hiring` or `in_credit_decisions` → high-risk AI classification and
  automated-decision-making rules engage together
- `ai_systems` includes `in_product` **and** `consumer_facing` → transparency and labelling duties

**Key instruments**

| Jurisdiction | Instrument | Identifier | Link |
|---|---|---|---|
| EU | Regulation (EU) 2016/679 (GDPR) | CELEX `32016R0679` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679) |
| EU | Regulation (EU) 2024/1689 (AI Act) | CELEX `32024R1689` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) |
| UK | Data Protection Act 2018 | `ukpga/2018/12` | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2018/12) |
| UK | Data (Use and Access) Act 2025 | `ukpga/2025/18` | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2025/18) |
| US | HIPAA Security and Privacy, 45 CFR 164 | eCFR title 45 part 164 | via eCFR API |
| US | COPPA Rule, 16 CFR 312 | eCFR title 16 part 312 | via eCFR API |

The AI Act applies obligations in **stages** by risk class and actor role. Never cite a single "AI
Act deadline" — identify which obligation and which class, and quote the applicable provision.

**Watch.** EUR-Lex OJ L; EDPB; the EU AI Office page; ICO; FTC (`federal-trade-commission`) and HHS
(`health-and-human-services-department`) via the Federal Register API.

**US coverage.** Federal sources do not provide state coverage. If `coverage.us_states`
is nonempty, apply these domain topics through `sources-us-states.md` for each selected
state. Quote each state's own applicability rules; do not transfer thresholds across
jurisdictions. Otherwise identify state law as unsearched.

---

## 2. `employment` — labour, employment, and workplace safety

**Triggers.** Engaged whenever `headcount_by_jurisdiction` has any entry. Escalations:

- headcount in a jurisdiction crossing a statutory threshold → reporting duties (pay gap,
  pay transparency). **Thresholds change; always cite the current one with a quote.**
- `physical_sites` non-empty → health-and-safety duties in those jurisdictions
- `unionised_workforce: true` → collective consultation and information rights
- `ai_systems` includes `in_hiring` → overlaps domain 1; assess under both

**Key instruments**

| Jurisdiction | Instrument | Identifier | Link |
|---|---|---|---|
| EU | Directive (EU) 2023/970 (pay transparency) | CELEX `32023L0970` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L0970) |
| EU | Directive (EU) 2019/1937 (whistleblower protection) | CELEX `32019L1937` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L1937) |
| UK | Employment Rights Act 1996 | `ukpga/1996/18` | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/1996/18) |
| UK | Equality Act 2010 | `ukpga/2010/15` | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2010/15) |
| UK | Health and Safety at Work etc. Act 1974 | `ukpga/1974/37` | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/1974/37) |
| US | OSHA standards, 29 CFR 1910 | eCFR title 29 part 1910 | via eCFR API |

**EU directives bind through national law.** A directive sets what member states must achieve; the
obligation on a business comes from the transposing national measure, which varies in detail and
timing. Since `EU-<country>` coverage is out of v1 scope, an EU employment finding is a signal to
check national implementation — say that, rather than presenting the directive as the operative rule.

**Watch.** Federal Register slugs `labor-department`, `occupational-safety-and-health-administration`,
`equal-employment-opportunity-commission`, `national-labor-relations-board`; EUR-Lex; UK SI feeds
and HSE.

---

## 3. `esg` — sustainability reporting and due diligence

**Triggers.** Engaged if `public_company: true`, or `revenue_band` is large enough to cross a
reporting threshold, or `supply_chain_tiers_mapped >= 1`, or `physical_sites` is non-empty.
Escalations: `regulated_products` non-empty, or supply chains reaching commodity or
forced-labour-risk sectors.

**Key instruments**

| Jurisdiction | Instrument | Identifier | Link |
|---|---|---|---|
| EU | Directive (EU) 2022/2464 (CSRD) | CELEX `32022L2464` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2464) |
| EU | Directive (EU) 2024/1760 (corporate sustainability due diligence) | CELEX `32024L1760` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L1760) |
| EU | Regulation (EU) 2023/956 (carbon border adjustment mechanism) | CELEX `32023R0956` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R0956) |
| EU | Regulation (EU) 2023/1115 (deforestation-free products) | CELEX `32023R1115` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1115) |
| UK | Companies Act 2006 (reporting duties) | `ukpga/2006/46` | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2006/46) |
| UK | Modern Slavery Act 2015 | `ukpga/2015/30` | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2015/30) |

**Handle this domain with particular care.** The EU sustainability regime has been the subject of
active amendment and simplification, including changes to scope thresholds and application dates.
Anything you may recall about who is in scope and from when is **especially likely to be out of
date**. Do not state a CSRD or due-diligence wave, threshold, or first-reporting year without
quoting the currently operative provision. If you cannot reach it, report `undated` and a coverage
gap. A confidently wrong first-reporting year here would be directly relied on.

**Watch.** EUR-Lex OJ L for amendments; Have Your Say; SEC (`securities-and-exchange-commission`)
and EPA (`environmental-protection-agency`) via the Federal Register API.

---

## 4. `trade_sanctions` — sanctions, export controls, and import restrictions

**Triggers.** Engaged if `exports_controlled_items: true`, or `sanctioned_country_touchpoints` is
non-empty, or `legal_entities` span more than one jurisdiction, or `supply_chain_tiers_mapped >= 1`.

**Treat this domain as high-tempo and high-consequence.** Sanctions designations frequently take
effect **immediately on publication**, with no transition period, and breach can carry criminal
liability — which the rubric scores `critical` automatically. Timeline buckets are often `<30` or
already in force by the time of the scan.

**Key instruments**

| Jurisdiction | Instrument | Identifier | Link |
|---|---|---|---|
| UK | Sanctions and Anti-Money Laundering Act 2018 | `ukpga/2018/13` | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2018/13) |
| US | Export Administration Regulations — Commerce Control List, 15 CFR 774 | eCFR title 15 part 774 | via eCFR API |
| US | OFAC Reporting, Procedures and Penalties, 31 CFR 501 | eCFR title 31 part 501 | via eCFR API |
| EU | Restrictive measures — published as individual regulations in OJ L | per-measure CELEX | via OJ L feed |

EU sanctions are not one instrument: each measure is its own regulation or decision. Cite the
specific measure's CELEX, never a general reference.

**Watch.** OFAC recent actions; BIS Federal Register notices; Federal Register slugs
`foreign-assets-control-office`, `industry-and-security-bureau`, `u-s-customs-and-border-protection`;
EUR-Lex OJ L.

---

## 5. `consumer_protection` — consumer rights, digital markets, and marketing

**Triggers.** Engaged if `consumer_facing: true`. Escalations: `processes_payments: true` →
payments and billing rules; subscription or auto-renewal models → cancellation and renewal
disclosure rules; `ai_systems` includes `in_product` → overlaps domain 1.

**Key instruments**

| Jurisdiction | Instrument | Identifier | Link |
|---|---|---|---|
| EU | Directive 2011/83/EU (consumer rights) | CELEX `32011L0083` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32011L0083) |
| EU | Regulation (EU) 2022/2065 (Digital Services Act) | CELEX `32022R2065` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2065) |
| EU | Regulation (EU) 2022/1925 (Digital Markets Act) | CELEX `32022R1925` | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1925) |
| UK | Consumer Rights Act 2015 | `ukpga/2015/15` | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2015/15) |
| UK | Digital Markets, Competition and Consumers Act 2024 | `ukpga/2024/13` | [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2024/13) |

The DMA's core obligations bind **designated gatekeepers**, not every digital business. Unless the
profile indicates designation, DMA developments are `monitor_only` — and say why, so the reader can
see the reasoning rather than wondering why a major regulation was scored down.

The DMCCA 2024 commences in stages by appointed day. Check the commencement position for the
specific provision rather than treating the Act as wholly in force.

**Watch.** CMA Atom feed; gov.uk consultations; Federal Register slugs `federal-trade-commission`
and `consumer-financial-protection-bureau`; FTC press release RSS; EUR-Lex.

---

## Citation formatting notes

- **EU numbering changed in 2015.** Instruments from 2015 onward read
  "Regulation (EU) 2024/1689"; earlier ones read "Directive 2011/83/EU" — number before the suffix.
  Verified in the live text of both `32024R1689` and `32011L0083`. Use the form the instrument
  itself uses.
- **UK Acts** cite as name + year, with `ukpga/<year>/<number>` as the identifier. SIs cite as
  name + year with identifier `<year>/<number>`.
- **US CFR** cites as `<title> CFR <part>`. Note that eCFR's human-facing `/current/...` pages and
  `uscode.house.gov` are both bot-gated and returned interstitials rather than content on
  2026-09-09 — the eCFR **API** is the reliable route. Cite the Federal Register document
  (`html_url`) for a *change*, and the eCFR API for standing codified text.

## Overlaps

Several triggers fire in more than one domain — AI in hiring, supply chain across ESG and trade,
consumer-facing AI features. When a development engages more than one domain, report it **once**,
list every domain it touches, and score impact at the **highest** applicable level. Reporting the
same instrument several times across domain sections makes a scan look larger than it is and buries
the items that need attention.
