---
name: goalz-manager
description: Use the Goalz MCP connection to read and manage the signed-in manager's football club, fixtures, training, transfers, messages, community, youth, and team crest. Use when the user asks about their Goalz account or a Goalz action.
---

# Goalz Manager

Help the user manage their own Goalz football manager account through the connected Goalz MCP server.

## Connection and account

- Use the Goalz MCP server already connected by the host. The OAuth connection identifies the Goalz manager. Keep every request on that identity and use only the currently visible tools.
- Ask the user to connect or reconnect through the provider's browser sign-in and consent flow when the connection is missing or a required permission is absent. Never ask them to paste a Goalz password, email confirmation code, access token, refresh token, or client secret into chat.
- Do not call password, registration, confirmation-code, autonomous-token, or connection-token tools. These flows are not part of the marketplace connection.
- Use only the scopes the provider actually granted and the tools the server exposes. A read-only grant supports only its visible read tools. If a requested action needs more permission, explain the missing scope and reconnect only through a provider-supported flow that explicitly requests it; do not promise incremental authorization or try another account, token, endpoint, or hidden tool.
- `manager:read` is required for Goalz OAuth calls. Read tools may also require `club:read`; for example, training changes require `club:manage`, while Wappen generation requires `club:manage` and `transfers:write`. Follow the exact scope requirements exposed for the selected tool; this list is guidance, not a replacement for tool metadata or server enforcement.
- The host may not support every Goalz capability. A tool's absence is not permission to simulate or claim that the action succeeded.

## Read and change game data

- Read the current state before recommending or changing it. Use `get_training` before proposing a training change, `get_kader` for the active squad, and `get_manager_onboarding` for the manager's checklist.
- Use current `tools/list` schemas and the chosen active team. Do not guess IDs, dates, budgets, roster members, offers, or match results. Ask a short question when a required selection is ambiguous.
- For a direct, clear request, perform the requested reversible game action only when its tool is visible and the grant permits it. For public messages, transfers, irreversible actions, or changes with material cost, show the exact target and content or amount and get the user's approval before submitting unless the user already gave that exact approval.
- Report the result returned by Goalz. Distinguish a preview, pending action, accepted action, completed action, and failure. Do not claim an asynchronous offer or preview is complete before Goalz reports completion.
- Public forum, talk, and guestbook posts are visible to other players. Confirm the destination and final text before posting. Do not copy private account or mailbox data into public messages.

## Multiple clubs and concurrent requests

- Read `whoami` for the current `team_context` and `list_teams` when club selection matters. Never infer a club ID from a name or silently switch clubs. Every club-context mutation requires `expected_verein_id` for the intended active club; this also applies to offer-refresh tools such as `get_sponsor` and `get_trainer`. For Wappen writes (`generate_wappen`, `accept_wappen`, `discard_wappen`, and `upload_wappen`), set `verein_id` to the same club ID. Follow the current tool schema and do not use `verein_id` as a substitute for `expected_verein_id`. For club-dependent reads, include `expected_verein_id` whenever the schema exposes it.
- Check the returned `team_context` after a club action. If the server reports `TEAM_CONTEXT_CHANGED`, a target mismatch, or stale team data, do not retry with a different ID. Read `whoami` and the relevant club data again, then confirm that the original intent still applies.
- Change the active club only when the user clearly asks for that transition. For `set_active_team`, use the current active club as `expected_verein_id` (0 if none is active), the destination as `verein_id`, and repeat that destination in `confirm_verein_id`. Then verify with `whoami`, discard old decision data, and reload what is needed before the next club action.
- For `leave_club`, identify the membership to leave with `verein_id`, set `confirm_leave=true`, and repeat that ID in `confirm_verein_id`. For `takeover_club` with a replacement, set `team_option="ersetzen"`, identify the owned club with `zu_ersetzende_vereins_id`, and pass the same ID in `confirm_replace_verein_id` plus its exact current name in `confirm_replace_team_name`. A manager-wide `apply_for_club` request does not switch the active club; when it specifies `zu_ersetzende_vereins_id`, require the same ID/name confirmation fields and report the returned application status.
- Calls on the same OAuth connection share one active-club selection. Do not race a club switch against club reads or writes. After a context conflict, re-read and reassess rather than blindly repeating the action. An idempotency replay can return the original result; use `whoami` for the live active club.
- Responses may include `stale_after_team_switch` and `reload_hint`; discard the old decision data and reload before deciding or writing. A snapshot or a return to the same club does not establish that old data is fresh.

## Wappen generation

- Wappen generation is available through `generate_wappen`, `get_wappen_generation`, and `get_wappen_preview` when the connected account and effective scopes allow it.
- `get_wappen_preview` retrieves preview data, which may be PNG/Base64; the tool result alone does not prove the host displayed an inline image. Say the preview is shown in chat only if it is visibly present there. To view an existing preview on the Goalz site, build the affected club's link from its returned club ID (`https://www.goalz.de/vereinsprofil.php?vereinsid=<club_id>`) and direct the owner to “Wappen verwalten”; the owner may need to sign in. Never put tokens or passwords in links. Do not generate or activate a Wappen just to display an existing preview.
- `generate_wappen` starts a quota-limited operation that may incur cost. Explain this before generating and proceed only after the user clearly asks for generation with that cost understood.
- If the user requests a new Wappen while forbidding quota use, any cost, or sending its prompt or image references to a provider, do not call `generate_wappen`: those restrictions conflict with a new generation. Explain the conflict and link to <https://www.goalz.de/agenten.php#datenschutz>. If an existing preview is available, identify it clearly as already existing; do not start another generation or activate it.
- A generated result is a private preview; generation does not activate the crest. Check the status and show the preview. Use `accept_wappen` only after the user separately asks to activate that preview; use `discard_wappen` only when the user asks to discard it.
- Goalz's privacy information describes which cleaned team details and image references can be sent to image providers for generation. Link to <https://www.goalz.de/agenten.php#datenschutz> when the user asks how it works. Do not invent retention or provider guarantees.

## Privacy and reporting

- Use only information relevant to the requested task. The provider processes the conversation and tool results under its own service terms and privacy policy; Goalz's current information is at <https://www.goalz.de/agenten.php#datenschutz>.
- Link setup and support questions to <https://www.goalz.de/agenten.php#einrichten> and <https://www.goalz.de/agenten.php#support>. Link use terms to <https://www.goalz.de/agenten.php#nutzung> and the operator contact to <https://www.goalz.de/impressum.php>.
- Never claim that a permission was granted, a write succeeded, a post was published, or a Wappen was activated unless the tool response confirms it.

## Example requests

German:

- “Wie sieht mein Kader aus?” Read the active squad with `get_kader` and summarize the returned players.
- “Welche Trainingsschwerpunkte habe ich diese Woche?” Read `get_training`; do not change anything.
- “Stell Montag auf Pressing.” Read the current plan, verify the user has an active team and write permission, then use `set_training` for Monday only.
- “Mach mir ein neues Vereinswappen. Ich weiß, dass dafür die quota-limitierte Generierung startet.” Start `generate_wappen`, check status, and show the private preview. Do not accept it automatically.
- “Schreib diesen Text in den Gästebucheintrag meines Gegners.” Confirm the destination and exact text before using a visible posting tool.

English:

- “Show my squad.” Use `get_kader` for the signed-in manager's active team.
- “Set Monday's training to pressing.” Read the plan first and use `set_training` only when that tool is visible and the active grant permits the write.
- “Create a new crest preview; I understand the quota and cost.” Use the Wappen generation workflow and leave the result as a private preview until the user separately accepts it.
