# Box Hubs

Box Hubs are curated collaborative spaces that organize files, folders, and links around a shared topic or project. Use a Hub to give a defined audience one place to browse content or ask Box AI questions across the collection.

## Access and eligibility

- Granting someone Hub access gives them Viewer access to every file and folder in it. External or Box links embedded in the Hub are exceptions.
- Before adding an item, compare its audience with the Hub's audience. Ask only when adding it would widen access beyond what the user authorized.
- Files and folders must be owned by the enterprise, and the acting user must be their Owner, Co-owner, or Editor.
- Titles and descriptions are visible to everyone with Hub access and may be used by AI as routing signals. Do not include sensitive details inappropriate for that audience.

## Questions and inventory

- Use `ai_qa_hub` for questions, summaries, or analysis across Hub content.
- Use `get_hub_items` for inventory or curation. It returns items added directly to the Hub, not descendants inside added folders; traverse those folders separately when the task requires them.

## Naming guide

Keep names scannable and unambiguous when an agent sees a flat list of hub names with no other context.

- Use [Domain] – [Scope] format: "Contracts – Enterprise Accounts" not "Sales Stuff".
- Avoid internal codenames or team jargon ("Project Falcon") unless the agent will also have access to a glossary.
- Disambiguate near-duplicates explicitly: "Legal – Active Matters" vs "Legal – Archived Matters".
- Skip filler words like "Hub," "Repository," "Center" — the type is already implied by context.

## Description guide (1–2 sentences max)

Format: [Content type] for [scope], [date range]. Use for [query type].

Optional third clause only if there's a common mix-up: Excludes [adjacent topic] — see [other hub].

Examples:

- Good: "Signed MSAs, SOWs, and pricing addenda for Enterprise accounts, 2022–present. Use for contract terms, pricing tiers, and renewal dates."
- Good: "Engineering design specs and architecture decision records for the Search platform, 2024–present. Use for technical implementation questions, not roadmap or planning."
- Good: "Customer support transcripts and resolved ticket summaries, last 12 months. Use for recurring issue patterns and product feedback themes. Excludes active/open tickets."
- Bad: "This is where the marketing team keeps their files." — no content types, no scope, no date range, nothing an agent can match against.
- Bad: "Important documents for Q3 planning." — vague noun ("documents"), vague scope ("Q3 planning" could be finance, product, hiring, anything).
