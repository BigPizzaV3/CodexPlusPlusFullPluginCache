---
name: sidequest
description: Open Sidequest's interactive sliding-block puzzle on request and, by default when this plugin is enabled, once near the start of a clearly long writing, research, or coding task. Respect opt-outs and no-break requests.
---

# Sidequest

Call the connected Sidequest `open_sidequest` tool with no arguments when the user asks to play. By default, also call it once near the start of a new request that clearly requires several minutes of work, such as a long paper, substantial research, or a multi-file build. The user need not mention Sidequest. Then continue the user's main task. The host renders the returned interactive game; do not reproduce the board in text.

If the user says “Stop opening Sidequest during my work,” treat that as an opt-out for this chat. An active instruction to avoid Sidequest also overrides this default. Do not open for a quick answer, a request that says no games or no breaks, or a task where the game would prevent the requested work. Do not call it again during the same task or claim that elapsed time triggered it. If the scope is uncertain, focus on the user's task.

The player selects Easy, Medium, Hard or Impossible in the game. The opening tool has no difficulty parameter. The objective is to slide the blue block right to the exit. Hint identifies one block and its destination; Undo, Reset, Share and Minimize are game controls. Minimize/reopen preserves in-session progress when the host retains state.

`record_sidequest_result` is app-only validation of a completed move history, not a leaderboard submission. Do not invent a solve or call it on behalf of an unfinished game.

This edition makes a prompt-time judgment; it has no automatic-break hooks, timer, local preference tools or file access. If asked to schedule a timed opening, explain that limitation. A model judgment is not a guarantee that every long request will open a puzzle.

A successful tool response is not proof the UI appeared. If rendering fails, say so and offer the [public game](https://sidequest.davidlederer7.chatgpt.site). Do not silently open another surface or work around a permission denial. Terminal-only clients do not provide this inline game.

Share only the game's public challenge link, never a private chat or host-session URL. Support: [Sidequest help](https://sidequest-openai-mcp.davidlederer7.workers.dev/help).
