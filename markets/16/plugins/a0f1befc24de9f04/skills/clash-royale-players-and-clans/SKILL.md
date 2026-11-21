---
name: clash-royale-players-and-clans
description: Read public Clash Royale player profiles, battle history, clan activity, and Daily Plan through RoyaleTools. Use for public player or clan analysis and daily priorities, not account login or player ownership verification.
---

# Players, clans, and Daily Plan

Read [the website contract](../royaletools-navigator/references/website.md).

- **Player Lookup:** use `/?playerTag={tag}#player-tag`, then follow the visible player result or open `/player/{tag}`. Inspect the requested profile tab, recent decks, battlelog, clan, or collection. Explain patterns from the displayed battles without treating that window as the player's full history. Shared deck links encode cards, not a historical profile snapshot.
- **Daily Plan:** use `/daily-brief?tag={tag}`. Read the loaded plan for deck, upgrade, and War priorities. Change comparisons depend on a previous snapshot available in this browser. Do not claim day-over-day changes without the displayed comparison, and do not use demo query modes as real player results.
- **Clan Activity:** open `/clan`, enter the public `Clan Tag`, and choose `Open Clan Activity`. The result uses `/clan/{tag}`. Inspect the relevant overview, roster, activity, or War tab and its snapshot date. Distinguish unknown activity from inactivity. Open a member's public profile only when needed to answer the question.
- **Clan search or joining:** for finding a clan, use `/clan-discovery` and the community skill. RoyaleTools can show public join policy; it cannot join a clan inside the game for the user.

Ask for a public Player Tag or Clan Tag when the intended record is unknown. Name search covers an approved creator/pro directory, not every Clash Royale player. Do not select a similarly named person without confirming the match.

Return the relevant public facts, the limited observation window, and a direct profile, clan, or Daily Plan link. Never ask for a game password, Supercell login, session token, or proof of ownership for a public lookup.
