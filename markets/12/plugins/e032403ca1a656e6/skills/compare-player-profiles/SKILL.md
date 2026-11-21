---
name: compare-player-profiles
description: Compare Cricket Explorer player biographies, reported roles, and batting or bowling styles when the user asks how selected players differ or wants a profile comparison. Use successful model-visible player details; do not use for career-statistics rankings, recent form, fantasy selection, or deciding who is the better performer.
---

# Compare Player Profiles

Build a comparison that helps the user understand the players' reported backgrounds and playing styles.

## Inputs and retrieval

1. Identify the players the user wants to compare. Resolve their identities from supplied IDs, returned player rows, or the latest `widgetState.modelContent.selectedPlayer`; confirm ambiguous names through a widget selection.
2. Reuse successful `structuredContent.selectedPlayer` detail responses already present in the conversation. For each missing profile with a known ID, call `open-cricket-explorer` with `reason`, `initialPanel: "players"`, and `playerId`.
3. Check each returned profile against the requested identity. Treat null selections and failed lookups as unresolved; do not substitute an unrelated list entry or interpret an opaque ID as proof of identity.
4. If an ID is unknown, open the Players panel with `reason` and `initialPanel: "players"`, then ask the user to select that player. Read the next model-visible selection. A name is not a supported search argument.
5. Retain the returned profiles and their IDs in the conversation as selections change. Widget state carries one selected player, not a history or a comparison collection. Do not claim access to the widget's local cache or call its app-only `get-cricket-data` tool.

## Compare the evidence

1. Align the reported fields: `country`, `role`, `battingStyle`, `bowlingStyle`, `dateOfBirth`, and `placeOfBirth`. Show unavailable values as unknown, including normalized text such as `Unknown country` or `Unknown player`.
2. Describe the differences in roles and styles using the reported labels. Explain unfamiliar labels briefly when useful, without turning a style into a claim about skill, tactics, success, or current team selection.
3. Keep country, birthplace, and nationality distinct. Do not fill missing country or role values from a name, flag, birthplace, or personal recollection.
4. Preserve source dates. Calculate ages only if requested and the birth dates and comparison date are trustworthy; include that comparison date.
5. State that the app supplies no career totals, averages, rankings, recent performances, or head-to-head statistics. Avoid declaring a better player from biographical fields.

## Deliverable

Provide a compact comparison table followed by the most useful supported similarities and differences. Distinguish missing fields from actual differences, and name any player whose lookup remains unresolved.

Describe the profiles as reported by CricketData and potentially cached for up to 24 hours. Keep any user-supplied facts separate from app-returned fields.
