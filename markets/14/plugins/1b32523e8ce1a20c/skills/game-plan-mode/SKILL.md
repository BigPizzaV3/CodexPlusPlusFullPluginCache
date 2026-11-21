---
name: "game-plan-mode"
description: "game plan mode: Prepare planning questions for a complex game idea. Preserve existing context and make one bounded next step."
---

# Game Plan Mode

Ask at most three high-value questions about the goal, player actions and success/failure, then provide a small proposed scope with labeled defaults. Write an English planning prompt for the user's existing builder. Suggest selecting Plan mode manually when available; no tool here activates it. Fictional example: Before building our original garden puzzle, clarify 1) which three symbols the player arranges 2) whether six failed moves ends the round 3) whether mobile touch input is required. Plan ONLY one level; explain acceptance tests before adding features. Do not create a fresh project or build link unless requested. Once the user wants a build, prepare the full eleven-section brief, call check_game_brief, revise once if below 80, display Game brief score: X/100, then call create_game_build_link. Never claim planning decisions were confirmed when they were only proposed.

Reply in the user's language; copyable builder prompts stay English. Refuse real-money gambling, adult sexual content, illegal activity and exact copyrighted-IP clones; offer original alternatives. No credentials or invented progress. Preserve working behavior and user facts. A builder may need iteration; test in preview, fix one issue at a time and add features incrementally. If a link is explicitly requested, use only its returned URL, copy_text, truncation warning, disclosure and next_steps; never construct links or claim a game exists.
