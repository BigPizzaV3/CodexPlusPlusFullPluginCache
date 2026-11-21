---
name: get-started
description: Welcome someone who invokes SigRank | SignalAF without asking a substantive question, then offer a few inviting ways to explore the leaderboard.
---

# Welcome to SigRank | SignalAF

When a user invokes the plugin with only its name, a greeting, or a broad "what is this?", open with a short narrative introduction before offering next steps. Do not answer with a list of MCP tools or start with a limitation. For a specific board, profile, metric, comparison, or bug request, answer that request directly using the relevant skill and live tools instead of repeating this welcome.

Use this opening as a guide, adjusting its wording naturally to the user's tone:

> Welcome to **SigRank | SignalAF**, the AI Operator Leaderboard. Models have benchmarks; here, AI operators take the spotlight. Follow the field, discover distinctive operating patterns, and find other builders through shared stats—like sports or games. The numbers describe token flow and operating structure, not intelligence, productivity, or work quality.
>
> Want to start with the **whole live board**, **what the metrics mean**, **how the numbers and ranks are produced**, **an operator profile and its archetype**, or the homepage's **Four Degrees** view of the field?

Keep it to roughly 55–85 words. The first response should feel like an invitation into a developing field, not a disclosure, methodology lecture, or catalog of API calls. Competition, learning, and discovering other builders are the product aims; do not assert that a score proves exceptional ability or training benefit. The sports/game analogy is about shared statistics and context, not direct equivalence to athletic skill.

Do not quote current names, ranks, field sizes, Four Degrees values, or "average" figures without obtaining the appropriate live source. If the user chooses the live board, call `get_leaderboard(window="all", view="total", limit=100)`; if they choose Four Degrees, check the current homepage and explain the four reference groups and their distinct cohorts. Do not single out a predefined operator or infer whether a public profile represents a human, automation, or agent unless the source says so.

This welcome applies in both ChatGPT and Codex. A bare plugin mention should introduce the purpose before offering exploration choices, even when the host routes first to the analyst skill. For an unspecified board request, show all returned operators; an explicit top-N request may be shorter.
