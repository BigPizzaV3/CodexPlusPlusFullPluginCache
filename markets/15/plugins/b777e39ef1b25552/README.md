# Voico — public plugin package candidate (v0.3.0)

**Publisher:** Voico GmbH (based on Voico's published Impressum; must match verified OpenAI publisher identity)

**Purpose:** ChatGPT plugin for each authorized Voico customer to read call/agent analytics and perform explicitly authorized operations through Voico MCP.

**Connection:** `https://mcp.voico.ai/mcp` (user-supplied endpoint, Streamable HTTP assumed; not independently reachable for live validation here).

## Inventory

- `plugin.json` — public identity, descriptions, three default prompts, icon, privacy and terms, submission review cases and release notes.
- `mcp.json` — remote Voico MCP server declaration; no embedded tokens/secrets.
- `assets/voico-icon.png` — user-provided Voico favicon (140 x 140 PNG); confirm branding rights and legibility in portal preview.
- `skills/voico/SKILL.md` — reusable top-level behavior and safety rules.
- `skills/voico/references/*` — detailed catalog and workflows for all 15 observed operations, privacy rules, user prompts.

## Why this ZIP has no code implementing 15 methods

In the MCP architecture, operations are implemented by **the remote Voico MCP server**, not copied into a plugin ZIP. On connection ChatGPT discovers tool names and JSON schemas exposed by that server for the connected account. The ZIP supplies connector configuration, human-readable product metadata, policies, instructions and review materials. Hardcoding guessed tool implementations, OAuth URLs or credentials in this ZIP would be incorrect and unsafe.

## Release blockers — do not submit as a finished public plugin yet

1. Confirm that the production endpoint actually supports Streamable HTTP and lists the expected 15 operations when reached by a new customer in a clean session; cross-check each server tool's JSON schema and `readOnlyHint`/`openWorldHint`/`destructiveHint` annotations.
2. Confirm which per-user authentication scheme the endpoint supports; implement/configure required OAuth discovery, redirects, token audience/scope, consent and revocation. If a verified OAuth client mode is available, add correct `extensions.com.openai.auth` settings to `mcp.json` or configure the connection in the submission portal. Do not put client secrets in this ZIP.
3. Verify object-level tenant permissions for calls, transcripts, agents, partner clients, phone numbers, and every write operation. Ensure authorized users only see their own workspaces.
4. Website URL set to https://www.voico.ai/ and support URL set to https://www.voico.ai/impressum (public contact page), with support@voico.ai as email. Confirm the submission portal accepts this support page; ideally publish a dedicated support page if required.
5. Have Voico legal/privacy confirm existing `https://www.voico.ai/datenschutz` and `https://www.voico.ai/agb` cover the ChatGPT plugin's actual data flows, retention, consent and support arrangements, and publish an addendum if needed.
6. Confirm the supplied favicon is approved for public branding, and verify developer identity in the OpenAI submission portal.
7. Record an **actual** reviewer-accessible demo using a clean review test account with dummy data; insert the verified `review.demo_recording_url`. A script is not a recording.
8. Create reviewer test workspace containing test agent, completed transcribed calls, assigned number, credits, and an opt-in test number. Provide credentials and login details **only** in secure portal fields, never in this archive.
9. Run actual positive and negative review cases, record evidence, verify API errors and safe approval gates, and finish country targeting, commerce declarations (if applicable), policies, scans and attestations in portal.

## Public review

There are eight positive and three negative draft cases in `plugin.json` → `extensions.com.openai.review.test_cases`. They are **drafts, not executed tests**. Their descriptions define the necessary reviewer fixture data and pass conditions. A human reviewer and product owner should verify the real server can satisfy them.

## Recommended demo walkthrough

1. Connect reviewer Voico workspace with approved auth; don't show credentials.
2. Ask weekly call totals and daily breakdown. Show actual statistics with dates.
3. Inspect the last transcribed finished call. Show real (dummy) call outcome/summary.
4. List configured agents and phone-number assignments.
5. Ask to modify a test agent's prompt; show the preview and explicit confirmation before applying. If the environment supports it, approve one safe test change.
6. Prepare an outbound call to the reviewer-controlled number; demonstrate the consent/approval boundary. Place it only if the reviewer has authorized safe test telephony.
7. Ask for unsupported deletion or another company's data and show proper handling.

## File safety

No real customer IDs, tokens, passwords, payment details or production phone numbers are included. The sample calls and date ranges in skill files are illustrative, not production data.
