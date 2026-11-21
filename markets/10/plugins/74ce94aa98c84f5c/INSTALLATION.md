# Pawn Break public plugin

**UI Bakery** is Pawn Break's publisher. The public edition connects to a hosted HTTPS MCP. End users need no local server, build tools or hook setup. Once installed and enabled, its skill directs Codex to open a chess board at the start of every task, including short questions, without a separate request or opt-in. Opening and completion are model-mediated rather than lifecycle hooks, so the host must load and follow the skill. An automatic board shows **Getting back to the chat…** for 1.5 seconds after completion, then requests closure; an explicit opening stays open.

## Availability, install and open

The current code is a **0.4.3** release candidate; the hosted service is **0.4.3**, deployed for local testing on October 9, 2026. The official Platform draft remains **0.4.0**, Not submitted / Not published; no public directory installation is available yet. Its previously verified domain/metadata/skill/MCP checks apply to that draft. Updated package scans, native acceptance and a demonstration recording remain pending.

Install Pawn Break from its approved directory listing when published and enable its connection. The next Codex task should open it automatically. “Open Pawn Break” also opens it explicitly and resumes automatic opening after a request to stop in the current chat. This repository's current release candidate is a development package; official registration, host checks, scans and approval are tracked separately.

For local developer testing, import the generated public package from a local source through your host's supported plugin workflow. Its internal package name is `pawn-break-public`, displayed as Pawn Break. This package is separate from the repository's existing local hook installation. The package declares its HTTPS MCP URL directly; OpenAI Platform completes official MCP setup and scans separately. Do not replace the existing local installation with the draft.

Official submission currently rejects `.app.json` app references and lifecycle hooks. The public ZIP uses `.mcp.json` and contains neither. A personal custom-MCP registration is useful for development testing but does not replace Platform's submission checks.

## Play and progress

Hint and Retry help on the current puzzle. Next puzzle advances or skips. Five clean solves increase rating by 100, capped at 2500; an assisted solve or skip resets the clean streak. Clear the host’s local/site data to remove saved progress. The public storage namespace is separate from the older local plugin.

Hosts may block, partition or clear local storage. Progress has no account, cross-chat or cross-device guarantee. It does not upload solve outcomes or local assignment IDs. Removing a plugin may leave local widget storage; use the host's site-data cleanup to remove it.

## Update, disable and remove

Use your host's plugin controls to update, disable the connection or uninstall Pawn Break. Ask Codex to stop opening Pawn Break in the current chat, then explicitly ask “Open Pawn Break” to resume. Disable the plugin to stop automatic opening across chats.

Closing or switching chats does not save a pause. MCP Apps teardown carries no closing reason and can happen during routine resource disposal, so the widget cannot reliably infer user dismissal from it. Version 0.4.2 ignores obsolete pause flags and never closes itself because of a stored pause. Puzzle progress keeps its existing storage namespace. The board has only its existing chess and progress controls.

If a request for the next puzzle fails, the current board remains available: retry Next puzzle after connectivity returns. Cached or bundled puzzles help when the external puzzle source is unavailable; they cannot replace a wholly unavailable MCP server.

Support and current privacy/terms are linked from the plugin listing and public website. UI Bakery operates the service independently of OpenAI and Lichess. See [support](https://pawn-break.uibakery-6k0ore.app.compartment.run/support), [privacy](https://pawn-break.uibakery-6k0ore.app.compartment.run/privacy), [terms](https://pawn-break.uibakery-6k0ore.app.compartment.run/terms) and the [issue tracker](https://github.com/KostyaDanovsky/pawn-break/issues).

## Automatic completion

The assistant sends completion immediately before its final answer for completed work, using only the token returned by the current automatic opening. Required-input or approval questions and progress updates do not signal completion. Starting a new automatic opening or explicitly continuing play cancels an older pending close. An interrupted task, missing token, server restart, expired token or unavailable host closure can leave the board open; use the host panel controls to close it manually. Completion does not pause later automatic openings.
