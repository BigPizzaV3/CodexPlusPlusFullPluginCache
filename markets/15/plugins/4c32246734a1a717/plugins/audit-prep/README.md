# ISMS Copilot Audit prep (beta)

An ISO 27001 audit-prep reviewer for Claude Code. It reads your ISMS files, has ISMS Copilot challenge its findings (the audit-prep job, think mode), checks every returned point in your files, and gives you a verified change list. It never edits your files.

**Beta.** Tested on 9 real ISO 27001 audit-prep cases on 2026-11-03: with this method and ISMS Copilot, Claude found 72 to 99 true points against 46 to 73 without it (two blind judges). About a third of the final points came first from ISMS Copilot.

## Install

1. In ISMS Copilot, open Settings, Connected apps, Create token (scope: conversations), and set it in your shell: `export ISMSCOPILOT_TOKEN=pat-isms-...`
2. In Claude Code: `/plugin marketplace add better-isms/ismscopilot-plugin`, then `/plugin install ismscopilot-audit-prep@ismscopilot`.
3. Ask: "Prepare our Stage 1 audit: check the SoA and the risk register."

Each check uses your ISMS Copilot plan, like any other conversation. When you reach your limit, the reviewer tells you when it resets, gives the upgrade link when ISMS Copilot provides one, and finishes without the check.

## What is sent

Over your token, the plugin sends ISMS Copilot its draft findings, the text under review, short excerpts of related records, the review instructions and its follow-up questions, with secrets and unneeded personal data removed. It sends no other files. Claude Code itself still processes your files through its model provider, as for any task. ISMS Copilot privacy policy: https://trust.ismscopilot.com/en/privacy-policy
