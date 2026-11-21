# Supported clients and recovery

Official sources checked 2026-10-05: [Site tools](https://learn.chatgpt.com/docs/webmcp), [packaging](https://developers.openai.com/plugins/build/plugins), [submission](https://developers.openai.com/plugins/deploy/submission). Recheck them before local acceptance or submission.

Live WebMCP requires the latest ChatGPT desktop app's built-in browser, ChatGPT Work or Codex, an open top-level Scribe editor page, enabled Site tools, allowed workspace policy and rollout availability. Enterprise admins must permit it; Edu is excluded by the current documentation. The docs explicitly name GPT-5.6 Sol and GPT-6 Sol; they do not establish GPT-6.1 Sol compatibility. This cloud implementation uses the requested GPT-6.1 Sol; verify its actual tool availability during local acceptance and do not silently change models. Tools registered inside iframes and declarative HTML form tools are unsupported. Closing/navigating the page can remove tools.

The package is skills-only. WebMCP is the live page's `document.modelContext` surface, not an HTTPS MCP server. No remote server, credential, connector, hook or account setting is installed by this package. Offline JSON authoring can work in any client that loads the skill; running validation also needs Node 22/24 and filesystem execution. That does not establish live browser support in web chat, mobile, ordinary Chrome, CLI or cloud Codex.

| State | Recovery |
|---|---|
| No Scribe page tools | Check the supported built-in browser, top-level editor URL, Site tools panel and policy. Ask the user to open/enable where appropriate. Offer AI JSON plus offline validation and manual Import AI JSON instructions. |
| Capability missing or unavailable | Search by task, get current contracts, inspect reasons. Use another supported owner only when it performs the authorized outcome. Otherwise mark the operation NOT_RUN. |
| Schema/version differs from this package | Retrieve current schema; use supported fields for live calls. For changed AI JSON ingress, obtain a compatible package or run the app's validator and treat offline compatibility as unverified. Never relabel schemaVersion to suppress an error. |
| Permission denied or confirmation cancelled | Stop that action, preserve state, report the reason. Do not retry under a different API or use page scripts/DOM/store writes to bypass it. Continue independent authorized work. |
| Stale project/revision, restore conflict | Re-read editor context and current object IDs. Resolve project identity with the user when ambiguous; never replay a stale mutation blindly. |
| Partial batch, error or uncertain result | Read back affected state, use ordinary Undo for an observed unwanted change, and repair through the canonical owner. Do not claim rollback without evidence. |
| Import warning or red missing-asset marker | Inspect skipped/adjusted fields and dependencies. Replace invented/unavailable assets with supported self-contained units, revalidate, preview and save/reopen. |

Use only discovered actual tool names. Typical stable controls are `scribe_get_editor_context`, `scribe_search_capabilities`, `scribe_get_capability`, `scribe_execute_capability`, `scribe_execute_batch`, and history tools. Search → get → execute is sufficient; activation changes logical preferences and is not a prerequisite that makes missing tools exist. Returned structured errors and permission checks remain authoritative.
