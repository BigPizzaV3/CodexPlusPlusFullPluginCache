---
name: prompt-tracking
description: Select buyer questions worth tracking in Cituna using Search Console and existing evidence, and add, enable, disable, remove or replace tracked prompts when the user asks.
---

# Select and manage tracked prompts

Read [connection and evidence rules](../../references/connection-and-evidence.md).

## Recommend prompts

1. Resolve the brand with `list_brands`. Its brand `prompts` configuration, when
   returned, is the current set of `{text, enabled}` entries. Read `get_visibility`
   separately for questions measured in the latest saved scan and their engine
   results. That scan can predate configuration changes and is not the current
   prompt editor. Check `whoami` for workspace-wide prompt capacity. If current
   configuration is missing, say it is unavailable rather than assuming it empty.
2. When GSC is connected, use `gsc_query`, `gsc_query_mix` or
   `gsc_striking_distance` to identify observed buyer demand. `gsc_ai_searches`
   can supply conversational-query candidates, but its classifications do not
   prove AI-origin traffic. Respect history coverage and reporting lag.
3. Propose a small set aligned with the brand's actual offering, market and
   language. Include category discovery, relevant use cases, comparisons and
   buyer concerns where the evidence supports them. Avoid leading premises or
   questions designed solely to force a brand mention.
4. Show each proposed prompt, its supporting query/evidence, buyer intent and
   reason to track. Label rewrites or inferred questions as suggestions, never
   literal GSC queries. If GSC is unavailable, use the user's supplied topics and
   clearly disclose that demand is unverified.
5. Deduplicate against the current configured prompts and show the proposed additions and
   capacity implications. A request for recommendations alone does not authorize
   editing the tracked set. If the user asks to add/track specified prompts, apply
   that instruction without an extra approval loop.

## Apply changes

Use `set_prompts` with the real brand ID/domain and the exact requested text:

| User intent | Argument | Effect |
| --- | --- | --- |
| Track additional questions | `add` | Preserves current questions; duplicates ignored |
| Resume questions | `enable` | Re-enables existing questions |
| Stop tracking for now | `disable` | Stops checks while retaining the question |
| Delete specified questions | `remove` | Removes them; destructive |
| Explicitly replace the whole set | `replace` | Deletes questions omitted from the replacement |

Prefer `disable` for pausing. Use `remove` only for an explicit deletion request.
Use `replace` only when the user explicitly requests a complete replacement and
the exact final set is established. Never combine `replace` with other actions.
An empty replacement is refused by this MCP; to pause everything, use `disable`
with the existing exact questions. Explain which questions will leave tracking
before deletion when the user has not already been told. A prompt-config update
does not prove that stored historical scans were deleted. Never silently remove
existing questions to fit a capacity limit. Adding an already-present disabled
prompt does not resume it; use `enable` for that.

Inspect the returned `counts`, `added`, `removed`, `notFound`, and final `prompts`
list. An `ok: true` response can still include unmatched questions in `notFound`;
report those as unapplied rather than claiming every requested edit succeeded.
Read `list_brands` again and compare the target brand's saved `prompts` text and
enabled flags. If that read does not expose the configuration, distinguish the
tool's write receipt from an independent verification and point to the app's
prompt settings. Do not repeat a write just to verify it.

Use `get_visibility` to check measurements only. New or resumed prompts may not
have answers until the next scan; changed configuration does not rewrite the
previous scan. Do not report citations before measurements exist or trigger a
paid scan simply to fill the new grid.

## Relevant tools

`whoami`, `list_brands`, `get_visibility`, `get_engine_answers`, `set_prompts`,
`gsc_status`, `gsc_query`, `gsc_query_mix`, `gsc_striking_distance`,
`gsc_ai_searches`.
