# Setting up Voicedot

## New account

- **In the browser:** the person starts at https://app.voicedot.ai/onboarding,
  enters the exact site address and installs the widget themselves, e-mails
  the snippet to a developer, chooses "Let my agent install it" (instructions
  valid until first use, at most 24 hours) or books a 15-minute install call. Installation is detected
  automatically; then they send a first comment.
- **Through a coding agent that can run commands (setup CLI v2):** the client is
  `/static/voicedot/agent-setup/v2/client.py` (checksum in `v2/facts.json`).
  For an existing owner's installation delegation, follow the copied v2 bootstrap,
  then its returned `nextStep` commands; `next` resumes from the same private state.
  `config` returns the canonical snippet and installation instructions. Python is
  needed in the agent environment, not in the website repository. This installation
  grant cannot register accounts, issue login links, read feedback or change billing.
  Owner installation redemption lasts at most 24 hours; registration installation
  redemption below lasts 15 minutes. Execution lasts 60 minutes after exchange.
  Commands print `stage` and `nextStep` (`--json`); failures add `code`,
  `retryAfter`, `expiresAt`. Secrets go via stdin; use one mode-0600 `--state`
  file per request, outside the repository.
  1. `register` (stdin JSON: `email`, exact `siteOrigin`, optional
     `addProject`); give the person the checkpoint link with its `#` fragment
     (30 minutes).
  2. They verify the e-mail in that same browser (15 minutes).
  3. `redeem`, `config`, `status`: install; the person opens the exact origin
     in a browser; wait for `freshAcceptedPing=true`.
  4. `handoff`: the sign-in link (one use, 15 minutes) is only for the person;
     they send the first message. Connect MCP as printed.
  5. `next` shows the current step; `withdraw` cancels.
  Only the person accepts the Terms, verifies, signs in and sends feedback;
  never bypass a CAPTCHA.

## Existing account, through MCP

1. With the "Set up projects and addresses" permission and a plan that allows
   another project, `create_project` adds a project for the exact HTTPS
   address the human gave. If the plan allows one project, the human uses the
   existing project. `add_project_address` adds another exact address the
   human asked for.
   A Team member also needs the owner's "Can create projects" permission to
   create another project. Every active Team member can work with addresses
   of existing workspace projects; the connection's own write permission
   is still required.
2. Install the returned snippet; the human opens the exact address in a
   browser; confirm `readyForFeedback` with `get_project_installation_status`.
3. The human opens that address and sends the first message with the widget;
   the agent never sends it.
4. The human finishes setup at `dashboardSetupUrl`; the project becomes active.

Address rules are in `plans`.
