---
name: clash-royale-merge-tactics
description: Open the RoyaleTools Merge Tactics team builder or a public player's Merge Tactics stats and help interpret results visible in its partner embed. Use specifically for Merge Tactics tasks, not ordinary Clash Royale eight-card deck building.
---

# Merge Tactics

Read [the website contract](../royaletools-navigator/references/website.md).

For team building, open `/merge-tactics/builder`. For player stats, open `/player/{tag}` and choose the visible Merge Tactics tab. Use the site's resulting URL for a direct stats link instead of assuming a fragment or tab query. The builder and stats are provided through a MergeTactics.gg iframe with partner credit.

The embed makes a browser request to MergeTactics.gg. A player stats request includes the public Player Tag. Open it only for the user's requested Merge Tactics task, not when inspecting an unrelated player profile. Do not preload other players or parallel partner sessions.

Inspect whether the available browser exposes the iframe's actual controls and results. If it does, operate ordinary selectors relevant to the requested team and verify the result. Do not assume browser support, rewrite iframe URLs, call partner endpoints directly, or copy hidden payloads. If the embed is inaccessible, taking too long, or not supported by the host, explain that visible condition and hand off the RoyaleTools page or the partner link offered on the page.

Use a builder-generated share link when available. Preserve opaque build parameters produced by the builder; do not invent or decode them to infer a team. Do not report a team, rank, or statistic that you have not observed.

Return the requested visible result with the partner attribution and relevant RoyaleTools page link. Skills do not establish redistribution rights or grant access to partner data beyond supported website use.
