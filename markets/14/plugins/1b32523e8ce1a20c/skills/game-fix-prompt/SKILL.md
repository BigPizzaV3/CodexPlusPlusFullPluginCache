---
name: "game-fix-prompt"
description: "game fix prompt: Write a focused repair prompt for an existing game. Preserve existing context and make one bounded next step."
---

# Game Fix Prompt

Ask for the existing game context, one expected-versus-actual behavior and exact error text if available. Never invent console output or replace missing context with a new project. Produce one copyable English repair prompt; no fresh build link unless explicitly requested. Template: When I [action], I expected [X] but [Y] happens. Please fix only this. Preserve [working behavior]. Done when [specific test]. Fictional example: When I press Jump on mobile, I expected the player to jump 140 px but nothing happens. Fix only the touch Jump binding; preserve desktop controls. Done when tapping Jump clears the first 100 px gap. For a feature request, define one incremental addition and its regression checks. Do not claim the repair ran. check_game_brief evaluates full build briefs, not repair success; use it only if the user separately requests a complete revised brief.

Reply in the user's language; copyable builder prompts stay English. Refuse real-money gambling, adult sexual content, illegal activity and exact copyrighted-IP clones; offer original alternatives. No credentials or invented progress. Preserve working behavior and user facts. A builder may need iteration; test in preview, fix one issue at a time and add features incrementally. If a link is explicitly requested, use only its returned URL, copy_text, truncation warning, disclosure and next_steps; never construct links or claim a game exists.
