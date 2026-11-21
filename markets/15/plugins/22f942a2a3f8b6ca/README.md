# MemoryRouter ChatGPT plugin

This directory contains the current local plugin package, manual Developer mode instructions, signed-out contract checks, and public submission assets for MemoryRouter.

## Truthful status

- Manual ChatGPT Developer mode connection is supported by the current published host contract and MemoryRouter signed-out discovery metadata.
- A real ChatGPT account has not been used in this build to test app creation, OAuth, vault selection, tool invocation, reconnect, or revocation.
- The public plugin has not been submitted, approved, published, or listed.
- `submission/readiness.v1.json` intentionally keeps `submission_ready` false until every external gate is complete.
- No file in this directory is proof of OpenAI approval or publication.

## Manual connection on ChatGPT web

Current official OpenAI documentation lists Pro, Plus, Business, Enterprise, and Education accounts on web. Workspace policy can still block Developer mode.

1. In ChatGPT, open **Settings → Security and login**.
2. Enable **Developer mode**.
3. Open [ChatGPT Plugins](https://chatgpt.com/plugins).
4. Select the plus button.
5. Create a developer-mode app using `https://mcp.memoryrouter.ai/mcp` as the public MCP endpoint.
6. Review the five discovered tools and their permissions. The standard package requests only `memories:read` and `memories:write`; whole-vault deletion remains separately authorized.
7. Complete MemoryRouter OAuth and select exactly one vault.
8. Start a new conversation, choose **Developer mode** from the plus menu, and add MemoryRouter.

Start with the first suggested action: **“Transfer what ChatGPT remembers about me.”**

ChatGPT inspects only saved memory and durable context actually available to the current chat. It organizes response instructions, personal details, projects, goals, recurring topics, tools, languages, frameworks, preferences, and corrections into one exact structured preview. It preserves the user's wording where possible, flags likely sensitive entries, excludes credentials and secrets, and lets the user edit, remove, or add entries.

No write occurs until the user explicitly approves the exact final preview in a later turn. The plugin then makes at most 12 sequential `store_memory` calls, reports the actual receipt for every entry, and identifies partial failures without inventing success. It finishes with this Claude handoff prompt:

> Use MemoryRouter to show what ChatGPT already knows about me and continue from there.

Claude connector review: https://claude.ai/settings/connectors?mcpUrl=https%3A%2F%2Fmcp.memoryrouter.ai%2Fmcp

This flow cannot read unseen private chats, does not prove completeness for the whole ChatGPT account, does not import previous conversations, and does not passively sync messages. Tool use is model-directed.

## Tools and scopes

| Tool | Scope | Behavior |
| --- | --- | --- |
| `search_memories` | `memories:read` | Recall shared memory from the selected vault. |
| `store_memory` | `memories:write` | Save useful details from the conversation; the host can ask the user to confirm each save. |
| `memory_status` | `memories:read` | Show opaque vault binding, counts, and scopes. |
| `forget_all_memories` | `memories:delete` | Permanently delete the selected vault after the exact phrase and host confirmation. |
| `search` | `memories:read` | Legacy compatibility alias. Not Company Knowledge or directory search. |

The standard package requests `memories:read` and `memories:write`; it omits `memories:delete`. Whole-vault deletion requires a separate grant, a permanent whole-vault warning that says item deletion is unavailable, the exact phrase `DELETE ALL MEMORIES` in a later turn, and destructive host confirmation. Ambiguous requests such as “forget that” never call the delete tool.

MemoryRouter does not expose `fetch`. Current OpenAI documentation requires standard `search` and `fetch` only for Company Knowledge eligibility, not for ordinary Developer mode or plugin submission.

## Package layout

- `.codex-plugin/plugin.json`: current OpenAI plugin manifest.
- `.mcp.json`: remote HTTP MCP configuration.
- `.app.example.json`: non-packaged shape only. A real OpenAI technical app ID must never be fabricated.
- `skills/memoryrouter/SKILL.md`: model guidance and behavioral boundaries.
- `submission/`: listing, test cases, annotation justifications, recording plan, and hard readiness gates.
- `scripts/`: deterministic package, validation, probe, checksum, and secret-scan tooling.
- `artifacts/`: generated deterministic ZIP and checksum only.

The installable ZIP intentionally omits `.app.json`. If a host workflow requires a registered ChatGPT app reference, create the app in a real account, use the OpenAI-generated technical ID in an ephemeral local test copy, and do not commit it without an explicit product decision. The current package instead declares the remote MCP directly through `.mcp.json`.

## Local validation

```bash
cd integrations/chatgpt
npm run validate
npm test
npm run package
npm run package:verify
npm run secrets
```

Run the safe signed-out probe to a temporary path:

```bash
npm run probe:live -- --output /tmp/memoryrouter-chatgpt-probe.json
```

The probe only performs unauthenticated initialization, tool listing, OAuth metadata discovery, a blocked signed-out tool call, and public URL checks. It does not register a client, log in, exchange tokens, or touch a vault.

## Build artifact

```bash
npm run package
```

Output:

- `artifacts/memoryrouter-chatgpt-plugin-1.3.0.zip`
- `artifacts/memoryrouter-chatgpt-plugin-1.3.0.zip.sha256`

The builder uses sorted entries, fixed timestamps, normalized file modes, and a fixed compression mode. Two builds from identical source must be byte-identical.

## Local install and remove boundary

OpenAI's current plugin documentation describes validation through the Plugin Creator plugin and installation from a local marketplace. It does not provide a host-neutral command that this repository can safely invent.

Before claiming a complete ChatGPT package install:

1. Validate the final source tree with the current Plugin Creator workflow in an authorized account.
2. Register or select the real MCP app if ChatGPT requests an app technical ID.
3. Install the package from a local marketplace.
4. Run the manual acceptance suite in `submission/manual-real-account-checks.md`.
5. Remove the test plugin from the local marketplace and delete or disconnect the draft app in ChatGPT Plugins.
6. Revoke MemoryRouter authorization separately if ChatGPT disconnect does not revoke it.

Manual URL connection remains the only currently documented and truthfully usable path in this repository without an account-generated app ID.

## Public submission boundary

The intended public path is a new **With MCP** draft in the OpenAI plugin submission portal using the universal endpoint `https://mcp.memoryrouter.ai/mcp`. The portal scans the live server directly. See:

- `submission/CURRENT-SUBMISSION-GATES.md`
- `submission/review-checklist.md`
- `submission/readiness.v1.json`
- `../../docs/connectors/chatgpt-connector-design-2026-08-05.md`

Do not submit, publish, deploy, register, or log in from automated validation.

## Remove or disconnect

For a manual Developer mode draft, open ChatGPT Plugins, remove the draft or disconnect it, then verify whether MemoryRouter authorization was revoked. Disconnecting does not delete vault data.

For a published plugin, unpublish or delete it through the OpenAI plugin submission portal. Those actions are account-gated and are not performed by repository scripts.

## Official references

Accessed 2026-08-05:

- https://developers.openai.com/api/docs/guides/developer-mode
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/build/mcp-server
- https://developers.openai.com/plugins/build/auth
- https://developers.openai.com/plugins/deploy/connect-chatgpt
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors
- https://developers.openai.com/plugins/deploy/app-review
- https://developers.openai.com/plugins/reference

Transfer pattern sources, accessed 2026-08-05:

- https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude
- https://claude.com/import-memory

The primary ChatGPT action adapts Anthropic's official migration categories and completeness check to ChatGPT's actual host boundary. It does not imply that ChatGPT exposes Claude's memory system or unseen private history.
