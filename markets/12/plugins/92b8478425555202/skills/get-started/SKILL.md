---
name: get-started
description: Set up DevKit Code, pair a Mac, check its connection, or guide a first coding task by project name. Use for DevKit onboarding and connection help.
---

# Set up DevKit Code

Help the user reach a connected Mac and a useful first task. Use the DevKit Code tools available in the current chat; do not substitute another repository, account or execution provider.

When the user asks for setup or connection help, read `devkit_status` silently if available. Explain only the next missing setup step. Ignore revoked devices when deciding whether a usable Mac is paired; do not lead with internal QA device names, IDs, status tables or a five-step checklist. An offline or revoked device does not prove that the helper is missing from the current Mac.

## First reply: one useful next step

The verified public guide is **https://devkit.run/docs#local-tools**. The published plugin is **https://chatgpt.com/plugins/plugin_asdk_app_6ad50cf4ff4c8191808e92261b5defc4**. These are actual release URLs, not placeholders. The Mac helper is installed with the Homebrew formula at **https://devkit.run/downloads/devkit.rb**; it is not a graphical installer or an App Store download.

If no usable Mac is connected and installation is unknown, start with: “First, install DevKit’s Mac helper. Open [Install DevKit on your Mac](https://devkit.run/docs#local-tools). On your Mac, press Command + Space, type Terminal, and press Return.” Then give only the install instructions below, with their success check. If the user says it is already installed, skip installation and help connect or start that same Mac. If the Mac is already ready, skip setup and ask what project they want to work on.

Do not say “use the official listing for the installer,” “use the command supplied by the release,” or “I couldn’t verify a public installer link” when these supplied release URLs are available. If a live fetch actually fails, name that specific failure; do not infer that the installer was never published. Do not send someone who already installed and connected the published plugin through manual MCP creation or OAuth scope editing again.

Use one stage at a time: install, pair, prepare Codex, start, then check readiness. State where to act, the exact command or link, and what success looks like. Wait for that stage’s result before supplying the next one. Never ask for the entire diagnostic log; if a step fails, ask only for the non-secret error line. Do not run installation, pairing or permission changes on the user’s behalf merely because they asked for guidance.

## Mac setup

The initial agent supports Apple Silicon macOS (M1 or newer). Homebrew installs Node 24+ as a dependency; do not make users install Node separately. The user needs a normal local Codex ChatGPT login with available included Codex quota. This beta is free from DevKit; no API account or API key is required and checkout is disabled. Never invent a domain, download link, native-client ID or pairing code.

For a first installation on a Mac with Homebrew, give this complete block:

```sh
brew tap-new devkit/local
curl -fL https://devkit.run/downloads/devkit.rb -o "$(brew --repository devkit/local)/Formula/devkit.rb"
brew install devkit/local/devkit
```

Then verify with `devkit --help`. Success is the DevKit command list. If the local tap already exists, skip the first line. If `brew` is missing, direct the user to https://brew.sh/ and continue only after Homebrew is available. If installation fails, stop that stage and help with the actual error. Do not give `devkit setup codex` until the helper is installed.

After installation, pair the Mac using the complete public production command:

```sh
devkit login --backend https://code.devkit.run --auth0-issuer https://dev-3kfazan344cjsvi3.eu.auth0.com/ --client-id h95fohE9xJsjs0nJsT8UkDjt7U5SkfuK
```

The user opens the sign-in URL printed in Terminal, signs in to the same DevKit account connected in ChatGPT, compares the device code, and confirms pairing. Success is a paired confirmation in Terminal. Preserve an existing pairing instead of logging out or replacing it. Do not request passwords, access/refresh tokens, MFA codes or Keychain contents in chat.

DevKit uses the normal local Codex ChatGPT login and its included subscription quota. Run `devkit setup codex`, enable the requested folder access while stopped, then run `devkit model login` to reuse the existing sign-in or complete Codex sign-in. `devkit model setup` selects an existing login and migrates an older API-key profile; `devkit model status` reports readiness. No API key is required. Do not request or copy Codex auth caches, tokens, passwords or API keys. Quota exhaustion stops coding; never suggest buying credits or falling back to API billing without explicit user authorization.

While their agent is stopped, the user can explicitly enable task-selected folder access with `devkit folders enable`. After successful model setup, recommend accepting the one-time automatic startup prompt. Never opt in on their behalf without authorization. Noninteractive setup uses `--autostart` or `--no-autostart`; without a flag it never prompts or installs. Existing users can opt in later with `devkit service install` without pairing again. Use `devkit start` for an enabled service, `devkit stop` to stop until next login, and `devkit service disable` to stop and disable login startup. Terminal can close after opting in; keep the Mac awake and online. Foreground `devkit run` is an advanced fallback. Preserve existing pairings and permission choices. These commands are available in the published Mac helper 0.4.3_6 or newer. Check `devkit --version` and `devkit service status` before directing an older helper to use them. For an already ready Mac, do not prompt for reinstallation or pairing.

For ChatGPT, open the DevKit Code listing, connect or reconnect the account, and review the actual sharing and identity consent. Use the same DevKit account as the paired Mac. Select DevKit in a new Chat conversation, choose GPT-6 with Extra High reasoning for this verified beta, and keep it active while the task runs. Work is optional for longer tasks and depends on the account's available Work usage; choose Cloud if the desktop app asks where to run it. A compact task card shows automatic progress, the computer and any permission/input wait, then Done. View changes opens the owned saved patch and Cancel stops unfinished work. Select the intended DevKit app with @ for each task, follow-up and cancellation. Give old test connections distinct names; if ChatGPT loses the connection while the Mac is ready, reselect the intended app and continue the owned task instead of starting it over. Refresh tools once for an existing older connection. Account linking and folder access are separate grants.

## First task and review

Ask for the intended project name and desired result only if they are not already clear. Users can say "Fix the checkout total in Demo Shop and run its tests." Do not require an absolute path, project registration, a picker or a separate investigation command. Resolve the single ready Mac and relevant folder names using DevKit's tools; ask in the conversation when a match is ambiguous.

Git tasks run in an isolated working copy. Report the actual saved result and test outcome. Use the card’s View changes control or ask “Show me the changes” to inspect the saved patch. Reviewing a patch does not apply it to the original checkout. Continue the owned task in the same thread/worktree for a natural follow-up, unless the user asks for separate work.

After starting or replying to a task, let the component track progress and resume the conversation with the saved result. Give the final answer once; do not repeat the card as a table or ask the user to poll. If a read-only continuation is needed, use `codex_job_wait` for the same owned task until it becomes terminal or needs input. A bounded wait with unchanged progress is normal. Never start a duplicate task to retrieve a result. While awaiting Mac approval, explain the local action once and keep monitoring before and after that external decision. For input questions, ask the saved questions and resume the same task when the user answers.

Explain that “Cancel that task” stops unfinished work but can retain earlier changes or partial output. Native Mac permission decisions stay on the Mac: read the requested command and use **Approve** or **Deny** there. A denial ends that request. Never approve through public tools, retry a denied command, or weaken sandbox protections to complete setup.

If the Mac is disconnected, report that state. Do not claim execution or replay an old request when it reconnects. Use `devkit doctor` for local readiness details and the listing's support contact for unresolved setup problems.

## Release evidence

For dated review results and the exact video/runtime boundaries, see [0.4.3 QA evidence](references/release-evidence.md). These recorded checks do not establish current readiness or OpenAI directory approval.
