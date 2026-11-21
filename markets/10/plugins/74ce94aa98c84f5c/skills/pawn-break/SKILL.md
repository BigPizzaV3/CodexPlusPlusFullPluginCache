---
name: pawn-break
description: Use at the start of every Codex task or user request while this plugin is installed and enabled, including development, debugging, research, explanations and short questions. Also use for explicit Pawn Break requests and existing board controls.
---

# Pawn Break

## Automatic opening

An installed and enabled Pawn Break plugin opens automatically. No separate permission, chess request, opt-in or "permanent use" mode is required.

At the beginning of every new task or user request, before substantive work or other tools, call the installed Pawn Break `show_chess_puzzle` tool once with `{"trigger":"automatic"}`, then immediately continue the user's task. The explicit-opening, existing-board control, pause and disabled cases below take precedence. Apply automatic opening to short questions as well as development, debugging and research. Do not decide the task is too short, unrelated to chess, or unlikely to require waiting. Do not wait for the user to solve a puzzle or replace the task with chess instructions.

Save the `board_token` returned by an automatic opening for this task. Immediately before the final answer that completes the task, call `finish_pawn_break` once with `{"board_token":"<this task's returned token>"}`. Finish the newest automatic opening only; never reuse a token from an earlier task or another chat, invent one, or send a chat/turn identifier. The board shows **Getting back to the chat…** for 1.5 seconds, then requests closure. Continue with the final answer without waiting for the panel to close. A failed or unavailable completion tool must not block the answer.

Do not send completion while work is unfinished, waiting for required input/approval, or merely posting a progress update. An explicit opening stays open: it returns no `board_token`, so do not call `finish_pawn_break` for it. Any explicit opening or request to keep playing cancels pending automatic completion for this task; discard its saved board token. An older server that returns no token keeps the board open; do not fabricate a token or replace it with a new opening just to close it.

If the user explicitly asks to open Pawn Break, call it once with `{"trigger":"explicit"}` instead. This resumes automatic opening for subsequent tasks in the current chat. A question about the plugin is not an explicit request to reopen it.

If the user asks to stop opening Pawn Break, continue their work without opening it again in this chat until they explicitly ask to open it. If the plugin is disabled, do not open it. An opening failure must not block the user's task.

Closing or switching away from a chat can produce host teardown without a user dismissal. Teardown alone must not be treated as a request to stop automatic opening. The widget ignores obsolete local pause flags and does not close itself because of them. Stopping in a chat is an assistant instruction, not a stored widget preference. To stop automatic opening across chats, use the host's plugin disable controls. Its puzzle text also works in hosts without an interactive board.

On an existing board, puzzle advancement and progress are widget controls:

| Request | Action |
| --- | --- |
| Next puzzle | Point to **Next puzzle** on the current board. |
| Hint, retry, skip | Use the board's Hint, Retry and Next puzzle controls. |

`get_pawn_break_puzzle` and `get_pawn_break_completion` are app-only. The assistant opening tool cannot reset local progress or advance the current widget. Keep the existing board for these control requests.

Progress belongs to the host's local widget storage, with no cross-chat or cross-device guarantee. Opening and completion are model-mediated; Pawn Break uses no lifecycle hooks. If the task is interrupted or the host does not honor closure, the user can close the panel manually. Automatic closure must not pause future openings.
