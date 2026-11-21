---
name: encounter-planning
description: Prepare, revise, save or export Dungeons & Dragons combat encounters with Encounter Workbench using the supported SRD 5.2.1 revised 2024 rules. Use when a DM asks to build an encounter, select monsters, calculate a combat budget, or reopen their saved encounter.
---

Use tools for calculations, catalog data and persistence. The supported ruleset is `srd-5.2.1` (revised 2024). Do not substitute 2014 encounter multipliers or paid book content.

1. Read `workbench_list` to find saved parties/encounters and their current revisions. Ask for missing party counts/levels only when the brief cannot establish them.
2. Use `monster_search` to select actual catalog IDs. Treat returned stat blocks as source data; never invent their CR, XP or mechanics. If the request names unsupported content, explain the catalog boundary and offer licensed alternatives.
3. Compose objective, terrain, complications and useful DM notes from the user's brief. Label these as creative suggestions. Call `encounter_calculate` to inspect a roster without saving. Budget/difficulty comes from the server result, not mental arithmetic. A short or tense encounter is a design goal, not a promised number of rounds.
4. For app Build requests, compose an original unsaved preview with the exact supplied ID, party and brief through `encounter_preview`. Do not save it; the app waits for this response and the user reviews then clicks Save.
5. Save a requested party with `party_save`. For a new encounter use a unique ID and revision 0. When an app Build request supplies an encounter/request ID, preserve that exact ID, party and brief so the waiting app can display the result. Include full party, roster, brief, notes, title and ruleset through `encounter_save`. For edits fetch the current saved snapshot/revision and apply only the intended change. Do not overwrite a conflict: reopen current state and reconcile with the user.
6. Call `encounter_open` with the saved ID to display the authoritative encounter. Explain the difficulty estimate and any relevant returned warning briefly. For AI Build requests, write original narrative and use search, calculate and preview; never substitute `encounter_generate`. The latter is only a local heuristic quick draft when explicitly requested.
7. Duplicate, move to trash, restore or export only when requested. Deletion is recoverable; restoration needs the trash revision. `encounter_export` returns a sourced Markdown sheet with attribution. Do not claim that exporting, installing or publishing occurred without evidence.

Never accept account identity from the conversation. The server scopes saved records to verified credentials. Do not advertise subscriptions, plans, upgrades or digital checkout. Initiative tracking, tactical simulation, maps and multiplayer are outside the initial release.
