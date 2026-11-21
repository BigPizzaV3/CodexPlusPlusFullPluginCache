---
name: setup
description: Set up an installed Veora plugin, identify its authorized Veorik, and explain how to use it. Use for onboarding or connection troubleshooting, not to submit work automatically.
---

# Connect Veora

Help the user connect this installed plugin to their own Veora account. Installation, an OAuth grant, and successful answer delivery are distinct states.

1. Use ChatGPT's native account-linking flow if this connection needs authorization. The user signs in to Veora and explicitly chooses the workspace, Veorik and permissions in the consent screen. Do not ask for passwords, tokens, OAuth parameters, runtime addresses or a task key in chat. Do not bypass a denied connection or grant access yourself.
2. Call this connection's `find_agents` read-only tool to identify the consented workspace and Veorik. It exposes only that binding; it is not a picker for other customers' agents. Explain the returned identity naturally. An authentication or eligibility error means setup is not confirmed.
3. For automatic answers to unfinished work, check the host's native plugin Events capability and whether this plugin advertises `task.updated`. Events are not a sixth callable Veora tool. The documented test surfaces are ChatGPT Work on web and Work with Cloud selected on desktop. Do not create a subscription during setup, substitute a timer monitor, or claim delivery is verified just because discovery succeeds.
4. Suggest a harmless first request: “Ask Veora which OpenClaw version it is using and how it verified it.” Do not submit that request until the user asks. Updates to an explicitly requested task are part of returning that task's answer, subject to host permissions and OAuth scopes; they are not blanket authorization for ongoing monitoring.

If the user wants another Veorik, explain how to connect an additional account/profile where supported or revoke and reconnect through the native flow. Existing tasks stay with their original grant. Revocation stops future access and updates but does not cancel running tasks.

Use the bundled [ask-veora workflow](../ask-veora/SKILL.md) when the user actually delegates bounded work. A successful `find_agents` call confirms the authorized binding, not that background delivery works. Report the concrete remaining step instead of displaying diagnostic identifiers or declaring every capability ready.
