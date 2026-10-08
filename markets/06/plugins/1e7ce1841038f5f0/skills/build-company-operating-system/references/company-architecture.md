# Adaptive company architecture

## Core modules

| Folder | Purpose | Typical contents |
|---|---|---|
| `00_START_HERE` | Current truth and navigation | Beginner guide, company profile, workspace map, setup register, open decisions, risks, document register |
| `01_STRATEGY_RESEARCH` | Direction and evidence | Thesis, market, customers, competitors, business model, assumptions, goals, roadmap |
| `02_GOVERNANCE_LEGAL` | Entity and decision controls | Formation evidence, ownership, resolutions, contracts register, legal review, licenses |
| `03_FINANCE_TAX` | Financial control | Model, budget, cash, pricing, invoicing, accounting handoff, tax records, insurance |
| `04_BRAND_POSITIONING` | Coherent identity | Positioning, messaging, voice, visual system, naming, asset rules |
| `05_PRODUCTS_SERVICES` | What is sold | Catalog, specifications, roadmap, quality criteria, pricing, change history |
| `06_CUSTOMER_ACCESS` | Model-specific acquisition and conversion | Self-service journey and intent routing, sales pipeline, marketplace sides, partners, community or local intake—only the artifacts justified by the selected motion |
| `07_MARKETING_GROWTH` | Discovery and demand | Search/SEO, public tools and pages, content, social, paid demand capture, referral, campaigns, partnerships, experiments, attribution, analytics |
| `08_DELIVERY_CUSTOMER_SUCCESS` | Fulfillment and retention | Onboarding, delivery, support, SLAs, feedback, renewals, incidents |
| `09_OPERATIONS_SOPS` | Repeatable execution | Process map, SOP index, checklists, QA, vendors, procurement, continuity |
| `10_PEOPLE_ORGANIZATION` | Roles and work | Org design, role cards, RACI, hiring, onboarding, performance, training |
| `11_TECH_DATA_AI` | Systems and information | Architecture, tool register, data map, environments, AI governance, integrations |
| `12_SECURITY_PRIVACY_RISK` | Protection and assurance | Access, secrets, backups, incidents, privacy, retention, threat/risk registers |
| `13_ANALYTICS_REPORTING` | Measurement | KPI dictionary, dashboards, operating reviews, experiments, source lineage |
| `14_ASSETS_TEMPLATES` | Reusable artifacts | Document, spreadsheet, proposal, briefing, meeting, design, and communication templates |
| `15_ARCHIVE_HISTORY` | Controlled history | Superseded material, exports, releases, migrations, dated snapshots |
| `16_AI_ROLES_PROMPTS` | Controlled AI work | Role map, chat architecture, approved prompts, input/output rules, review and privacy controls |
| `17_OPERATING_WORKSPACE` | Daily execution | Inbox, active work, review/approval, released records, results, and lessons |

## Conditional modules

Add only when justified:

- `INVESTORS_BOARD` for fundraising, cap table, data room, and board reporting.
- `REGULATORY_QUALITY` for regulated products, certifications, validation, audits, and quality management.
- `INVENTORY_SUPPLY_CHAIN` for physical goods, sourcing, logistics, stock, and recalls.
- `FRANCHISE_LOCATIONS` for multi-site or franchise operations.
- `CUSTOMER_WORKSPACES` when per-client segregation is required.
- `ENGINEERING_PRODUCT` when software development needs repositories, architecture decisions, releases, and incident operations beyond the core tech module.

## Architecture improvements over a generic folder tree

1. Put a source-of-truth `START_HERE` area first and write it for an inexperienced operator.
2. Separate evidence, decisions, assumptions, and drafts.
3. Attach owner, status, review date, and sensitivity to critical documents.
4. Use registers for external state instead of pretending accounts or registrations exist.
5. Keep templates separate from completed records.
6. Keep superseded work in a controlled archive rather than mixing it with current truth.
7. Adapt modules to company stage and risk instead of creating every possible department.
8. Split content by operating purpose; keep one navigation source rather than one giant handbook.
9. Separate reusable prompts/templates from approved company records and live work.
10. Do not make a sales department universal. A broad self-service or product-led platform needs intent discovery, activation, conversion, lifecycle and support controls; a sales-led business needs account and pipeline controls; hybrid models need explicit routing and ownership.
