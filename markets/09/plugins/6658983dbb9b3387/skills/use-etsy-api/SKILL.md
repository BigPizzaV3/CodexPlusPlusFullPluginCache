---
name: use-etsy-api
description: Discover and use MakeBox direct Etsy API tools with exact schemas, seller-owned identity, file transport, precise authorization and authoritative readback; avoid guessed endpoints and duplicate uncertain writes.
---

# Direct Etsy API

Read [transport contract](../../references/direct-etsy-api-guide.md) and [operation recipes](../../references/etsy-operation-recipes.md). Search the [105-operation index](../../references/etsy-operation-index.md) for the task, then inspect the live tool schema. The bundled [schemas](../../references/etsy-tool-schemas.json) are a dated fallback/reference, not authority to call unavailable tools.

## Operating contract

1. No MCP: do not invent a tool or demand connection for copy work. Produce manual fields/settings with the appropriate skill. Only external execution waits for connection.
2. Connected: `list_shops`/`get_account_status` establish selected MakeBox workspace/access, `etsy_get_me` Etsy identity. Private shop/user IDs are server-bound; public calls may expose shop IDs. Etsy listing IDs differ from MakeBox row IDs.
3. Read current resource; collect missing facts. Inspect required params/body/enums and media input. Do not infer an API limitation from a narrower convenience tool.
4. Prepare exact changes and show affected scope/consequence. Reuse prior explicit authorization for that same scope. Only an authorized write gets `confirm:true`; deletion also needs the current `expected_title` where required.
5. Use direct tools for chat-authored approved payloads; no internal model or AI allowance needed to transport them. Plans, scopes and Etsy fees can still apply. Optional generation/research workflows have separate costs/quotas.
6. Follow returned readback hint or matching authoritative read. Acceptance with `verified:false` is not completed state. On timeout/mismatch read first; never automatically replay.

Body fields belong inside `body`; path/query params at top level. Preserve omission, false, zero and permitted clears. Use native enum values: direct `download` is not convenience `digital`. Binary fields take tenant-owned asset references, not arbitrary server/local paths. See recipes for examples validated against the server snapshot.

Full inventory and personalization writes replace complete sets: preserve untouched values and convert GET-only structures to the writable schema. Shared profile edits can affect many listings. Public research does not authorize private competitor access.

Report target IDs, source/capture time, accepted/verified status and the real unresolved error. Never expose tokens or imply API supports every website feature, general buyer messaging, purchases, ad changes or refund initiation.
