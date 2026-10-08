---
name: empire-settings
description: Configure, inspect, or remove Empire LLM credentials and project budget settings without exposing secret values. Use when the user asks to set up Empire, enter OpenRouter or Artificial Analysis credentials, check Empire credentials, change the review budget, or sign out.
---

# Empire Settings

Manage Empire locally. Never ask the user to paste an API key into chat, a prompt, a project file, or a shell command.

The shared router keeps JSON as its default automation contract and accepts
`--view compact|detailed` before or after a command for native-Codex Markdown.
Use the compact view for ordinary redacted status and budget summaries, and the
detailed view for diagnosis or reconciliation. A view must never reveal fields
that the underlying redacted result omits.

## Exposed-secret guard

If a user includes a credential-looking value in chat, never echo it, quote it, forward it to a tool, store it, test it, or treat it as usable configuration. Tell the user to revoke it and create a replacement. Resume setup only after the replacement is entered through the hidden terminal prompt. This guard applies even when the user explicitly asks Codex to store the pasted value.

Codex does not provide a native secret-field schema for skill-only plugins. Do not imitate a settings form in chat. Do not add an MCP app merely to collect credentials. Use the local hidden prompt and system keyring on every supported platform.

## Credential settings

1. Resolve the sibling `../empire-review` directory from this `SKILL.md` as `EMPIRE_REVIEW_ROOT`.
2. Run the redacted credential doctor before any setup prompt:

   ```bash
   python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" doctor
   ```

   Treat its states as a finite-state contract:

   - `present: true` — use the credential; never prompt again.
   - `present: false`, `action: setup` — absence is verified; setup may be offered.
   - `present: null`, `action: retry_with_keyring_access` — the operating-system keyring is inaccessible from the current sandbox. Retry this same redacted doctor command with narrowly scoped Keychain/keyring access. Do not run setup and do not ask the user for the key again.
   - `present: null`, `action: install_secure_keyring` — no supported secure store is available. On Linux, install `secret-tool` and a compatible Secret Service; use environment variables only for CI/headless operation.

3. For verified initial setup or an explicitly requested replacement, instruct the user to run this interactively in their local terminal, or open an interactive terminal session in which the user—not Codex—types the secret:

   ```bash
   python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" setup
   ```

   The prompts use `getpass`, so entered characters are not echoed. OpenRouter is required and Artificial Analysis is optional; pressing Enter at the optional prompt preserves an existing Artificial Analysis credential. Store credentials under `empire-codex-router` in macOS Keychain, Windows Credential Manager, or Linux Secret Service. Secret values must never appear in output.
   Setup reads each saved key back before reporting `configured`. A successful write whose readback is sandbox-blocked reports `configured_unverified`; rerun `doctor` with narrowly scoped keyring access instead of prompting again. A successful write followed by a verified missing result is an error.
4. To inspect configuration, run `doctor`. Report only `present`, `source`, and `action`; never report a value.
5. To remove credentials, run `logout` and preserve its confirmation prompt.

OpenRouter is the default inference provider. Artificial Analysis supplies optional benchmark evidence and does not execute reviews.

Use environment variables only for CI or headless systems. On Linux, if Secret Service is unavailable, explain that the user must install `secret-tool` and a compatible keyring service; never create a plaintext fallback.

## Public web research

The web skill in 1.7.2 uses native Codex web tools and needs no provider key.
The legacy external web adapter is retired. Do not run its old setup, doctor,
upload, or browser commands. Existing web-provider credentials are left untouched;
this release does not inspect, migrate, or delete them.

## User-owned provider

Empire also supports one user-selected OpenAI-compatible HTTPS chat-completions provider. Gather only non-secret values in chat: provider slug, endpoint, native model ID, corresponding OpenRouter catalog model ID when available, input/output USD per million tokens, and context size. Then run:

```bash
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" provider setup \
  --name PROVIDER_SLUG \
  --endpoint "HTTPS_CHAT_COMPLETIONS_ENDPOINT" \
  --model "NATIVE_MODEL_ID" \
  --catalog-model "OPENROUTER_CATALOG_MODEL_ID" \
  --input-cost-per-mtok "INPUT_USD" \
  --output-cost-per-mtok "OUTPUT_USD" \
  --context-tokens CONTEXT_TOKENS
```

The API key is entered only at the hidden prompt and stored in the system keyring. The non-secret settings file is mode `0600` where supported. Never infer direct-provider prices from OpenRouter; ask the user to obtain prices from their provider account.

Use `provider status` for redacted status, `provider select openrouter|direct` to choose the default route, and `provider remove` to delete the direct credential and metadata. A single review can override the saved route with `review --provider openrouter|direct`.

## Project budget

Set or inspect a repository-local logical budget through the same router:

```bash
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" budget status --repo .
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" budget set --repo . --limit-usd "5.00"
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" budget pending --repo .
```

Changing a budget is allowed only when the user requests the new limit. Never perform a paid live review merely to test settings.

An ambiguous provider outcome remains reserved. Reconcile it from provider
billing evidence with `budget reconcile --reservation ID
--observed-cost-usd USD`. Use `budget release-pending` only when the provider
proves no billable request exists; it requires `--yes` and a recorded reason.
