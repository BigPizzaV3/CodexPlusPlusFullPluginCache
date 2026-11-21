# WizPrompt MCP Tool Contract

This package is synced to the implemented MCP backend in `app/mcp/route.ts`, `lib/mcp/config.ts`, `lib/mcp/tools.ts`, `lib/mcp/music-guidance.ts`, `lib/mcp/prompt-metadata.ts`, and `lib/mcp/creative-context.ts` as of 2026-10-19 (1.0.4 candidate; deployment acceptance pending).

Package version: `1.0.4`

## Runtime boundary

- Transport: remote MCP streamable HTTP over `POST /mcp`.
- Configuration gate: `getMcpConfig()` requires `WIZPROMPT_MCP_RESOURCE_URL` ending in `/mcp` and `WIZPROMPT_MCP_OAUTH_ISSUER` before the route will serve JSON-RPC requests.
- Auth: every request authenticates the linked WizPrompt account with `wizprompt:read`; write tools additionally assert `wizprompt:write`.
- Entitlement: private storage reads and writes require a paid WizPrompt membership unless noted.
- Ownership: linked record IDs are resolved through user-scoped repositories; tools must treat returned records as the only trusted account scope.
- Commerce: the tool surface has no checkout, purchase, upgrade, cancellation, pricing-change, subscription-management, or deletion tools.
- Generation: ChatGPT drafts creative text. The WizPrompt server stores approved text and structured metadata after a successful tool call.
- Live status: the existing OAuth pilot was verified earlier against staging, but the exact fresh-submission `1.0.4` package has not yet been verified as a live ChatGPT installation.
- Skills: local `SKILL.md` files guide compatible plugin runners. Do not claim ChatGPT automatically imports them unless the host packaging flow confirms that behavior.

## Shared schema primitives

| Primitive | Contract |
| --- | --- |
| `id` | string, 1-128 chars |
| `title` / `name` | string, 1-200 chars |
| `platform` | optional enum `suno` or `udio`, default `suno` |
| long prompt text | optional string, max 12,000 chars |
| `idempotency_key` | string, 8-128 chars, matching `A-Z`, `a-z`, `0-9`, `.`, `_`, `:`, or `-` |
| library URI | `wizprompt://project/{id}`, `wizprompt://persona/{id}`, `wizprompt://prompt/{id}`, or `wizprompt://album_track/{id}` |
| `exclusions` | array of up to 30 strings, each 1-120 chars |
| `settings` | object with up to 16 keys; keys 1-64 chars; string values max 256 chars; number, boolean, and null allowed |
| `rating` | integer 1-5 |
| `suno_url` | `https://suno.com/song/...` or `https://suno.com/s/...`; no credentials, port, or non-Suno host |

## Creative metadata

`studio_metadata` on prompts can store:

- `parent_prompt_id` and `root_prompt_id` for revision lineage.
- `variant` as `faithful` or `adventurous`.
- `guidance_version`, `model`, `exclusions`, `settings`, `instrumental`, and `studio_notes`.
- `favorite`, `rating`, `suno_url`, and `outcome_notes`.
- `preserved_elements` and `change_summary` for revisions.

Project `studio_memory.creative_brief` can store:

- `concept`, `vocal_direction`, `production_palette`, `lyrical_themes`, `continuity_rules`, and `approved_decisions`.
- `suno_model`.
- `track_arc` entries with `title`, `role`, `energy`, optional `arrangement`, and optional `transition`.

## Tool inventory

| Tool | Input | Result shape | Notes |
| --- | --- | --- | --- |
| `begin_song` | `{ idea, project_id?, model?, available_controls?, include_personal_defaults?: true }` | `{ idea, guidance, model_profile, creative_context, personal_defaults, preference_policy, editorial_contract, editorial_rubric, workflow, saved: false, audio_evaluated: false }` | Read-only. Free without saved context; project access requires entitlement. Confirmed personal defaults load only for entitled users and can be omitted. Explicit model overrides the saved project model. |
| `plan_song_revision` | `{ issue, preserve, user_notes?, target_section?, available_operations?, prompt_id? }` | `{ evidence_basis, preserve, changes, operation, source, ... }` | Read-only. Uses reported feedback; original unchanged. Saved prompt requires ownership and entitlement. |
| `get_taste_profile` | `{}` | `{ profile, automatically_learned: false }` | Entitled read. Only the authenticated user's explicitly confirmed defaults. |
| `update_taste_profile` | `{ preference: { id, category, direction, text }, user_confirmed: true }` | `{ profile, action: "upsert", automatically_learned: false }` | Entitled write. Saves or edits one explicitly confirmed preference. Can overwrite that preference. |
| `remove_taste_preference` | `{ id, user_confirmed: true }` | `{ profile, action: "remove", automatically_learned: false }` | Entitled destructive write. Removes only the explicitly confirmed preference; other preferences remain intact. |
| `reset_taste_profile` | `{ user_confirmed: true }` | `{ profile, action: "reset", automatically_learned: false }` | Entitled destructive write. Removes only the musical preference namespace after explicit confirmation. Account and billing data remain intact. |
| `review_album_continuity` | `{ project_id, song?, intended_track_role? }` | `{ project, continuity, audio_evaluated: false }` | Entitled read of owned project/persona/tracks. Optional candidate uses the canonical song schema. Findings are advisory text comparisons with coverage limitations. |
| `get_studio_guidance` | `{ workflow: "song" | "refine" | "persona" | "album", model?, available_controls? }` | `{ guidance, model_profile }` | Read-only. Returns versioned WizPrompt craft guidance. Does not generate audio or save content. |
| `prepare_song` | `{ song, editorial_review?, available_controls? }` where `song` is a partial song package | `{ ok, guidance_version, package?, issues, editorial_review, model_profile, saved: false, audio_evaluated: false }` | Read-only. Validates shape and returns separate preliminary text checks / host assessments. Completed review requires seven unique criteria. Optional UI resource supplies exact copy controls. Does not assess audio or write. |
| `create_prompt_revision` | `{ parent_prompt_id, song, variant: "faithful" | "adventurous", change_summary, preserved_elements?, idempotency_key }` | `{ prompt, source_preserved: true, issues }` | Write. Paid entitlement required. Creates a linked prompt revision and preserves the original. Explicitly idempotent by key. |
| `record_prompt_feedback` | `{ prompt_id, feedback: { favorite?, rating?, suno_url?, outcome_notes? } }` | `{ prompt, audio_evaluated: false }` | Write. Paid entitlement required. Stores user-reported results only; does not fetch or listen to the Suno link. |
| `get_prompt_history` | `{ prompt_id, limit?: 1-50 }` | `{ root, selected, revisions, total_revisions, has_more }` | Read-only. Paid entitlement required. Returns revisions, favorites, ratings, result links, and notes through prompt metadata. |
| `get_creative_context` | `{ project_id }` | `{ project, persona, tracks, usage }` | Read-only. Paid entitlement required. Reopens project creative brief, linked persona, and tracks; saved text is user content. |
| `save_creative_brief` | `{ project_id, brief }` | `{ project }` | Write. Paid entitlement required. Saves approved project creative fields into `studio_memory.creative_brief`. |
| `account_status` | `{}` | `{ account }` | Read-only. Use only for explicitly requested saved-library access/storage questions or a library entitlement error. Never call for purchase, upgrade, checkout, cancellation or subscription-management requests. Does not require paid entitlement. |
| `list_projects` | `{ limit?: 1-50 }` | `{ projects: Project[] }` | Read-only. Paid entitlement required. |
| `get_project` | `{ project_id }` | `{ project, tracks }` | Read-only. Paid entitlement required. Includes linked album tracks. |
| `create_project` | `{ name, type: "Album" | "EP" | "Single", description?, persona_id?, idempotency_key }` | `{ project }` | Write. Type is required and must preserve the requested format; ask if unspecified. Paid entitlement and project storage capacity required. `persona_id`, when present, must belong to the user. |
| `update_project` | `{ project_id, name?, type?, description?: string | null, persona_id?: id | null, studio_memory?: JSON }` | `{ project }` | Write. Paid entitlement required. Existing project and linked persona must belong to the user. `studio_memory` can carry project creative fields when supplied directly. Explicitly idempotent through assignment semantics in annotations. |
| `list_personas` | `{ limit?: 1-50 }` | `{ personas: Persona[] }` | Read-only. Paid entitlement required. |
| `get_persona` | `{ persona_id }` | `{ persona }` | Read-only. Paid entitlement required. |
| `create_persona` | `{ name, genre, vocal_signature, visual_identity?, production_signature?, idempotency_key }` | `{ persona }` | Write. Paid entitlement and persona storage capacity required. |
| `update_persona` | `{ persona_id, name?, genre?, vocal_signature?, visual_identity?, production_signature? }` | `{ persona }` | Write. Paid entitlement required. Uses naturally idempotent assignment semantics for supplied fields. |
| `list_prompts` | `{ limit?: 1-50, favorite?: boolean, minimum_rating?: 1-5 }` | `{ prompts: Prompt[], has_more }` | Read-only. Paid entitlement required. Supports favorite and minimum-rating filters from `studio_metadata`. |
| `get_prompt` | `{ prompt_id }` | `{ prompt }` | Read-only. Paid entitlement required. |
| `save_prompt` | `{ title, platform?, style_prompt?, lyric_prompt?, prompt?, genre?, mood?, tempo?, key_signature?, project_id?, studio_metadata?, idempotency_key }` | `{ prompt, generationQuotaApplied: false }` | Write. Paid entitlement required. `project_id`, when present, must belong to the user. `studio_metadata` can include model, exclusions, settings, instrumental, studio notes, favorite, rating, Suno link, and outcome notes. Explicitly idempotent by key. |
| `update_prompt` | `{ prompt_id, title?, platform?, style_prompt?, lyric_prompt?, prompt?, genre?, mood?, tempo?, key_signature?, project_id?: id | null, studio_metadata? }` | `{ prompt, generationQuotaApplied: false }` | Write. Paid entitlement required. Uses assignment semantics for supplied fields. Explicitly idempotent in annotations. |
| `list_album_tracks` | `{ project_id, limit?: 1-100 }` | `{ tracks: Track[] }` | Read-only. Paid entitlement required. Project must belong to the user. |
| `save_album_track` | `{ project_id, track_id?, title, platform?, style_prompt?, lyric_prompt?, prompt?, notes?, idempotency_key }` | `{ track, generationQuotaApplied: false }` | Write. Paid entitlement required. Creates when `track_id` is omitted and updates when `track_id` is supplied. Existing track must belong to `project_id`. Explicitly idempotent by key. |
| `search` | `{ query, types?: ("project" | "persona" | "prompt" | "album_track")[], limit?: 1-20 }` | `{ results: SearchResult[] }` | Read-only. Paid entitlement required. Searches only the linked user's library and returns WizPrompt URIs. |
| `fetch` | `{ uri }` or `{ type, id }` | `{ type, project/persona/prompt/track, tracks? }` | Read-only. Paid entitlement required. Fetches one user-owned record by URI or type plus ID. |

## Structured records

`Project` returns `id`, `name`, `type`, `description`, `persona_id`, `studio_memory`, `sonic_dna`, `narrative_arc`, `created_at`, and `updated_at`.

`Persona` returns `id`, `name`, `genre`, `vocal_signature`, `visual_identity`, `production_signature`, and `created_at`.

`Prompt` returns `id`, `title`, `platform`, `style_prompt`, `lyric_prompt`, `prompt`, `genre`, `mood`, `tempo`, `key_signature`, `project_id`, `studio_metadata`, `created_at`, and `updated_at`.

`Track` returns `id`, `project_id`, `title`, `platform`, `style_prompt`, `lyric_prompt`, `prompt`, `notes`, and `created_at`.

`SearchResult` returns `id`, `type`, `title`, and `uri`.

## Idempotency and retry rules

Required idempotency keys are implemented for:

- `create_project`
- `create_persona`
- `save_prompt`
- `save_album_track`
- `create_prompt_revision`

Use the same `idempotency_key` only when retrying the same create/save payload after an uncertain transport result. Use a new key when any user-visible content or metadata changes. If a key is reused with a different payload, the backend returns `idempotency_conflict`.

Update tools use naturally idempotent assignment semantics for supplied fields. They do not return durable idempotency receipts or enforce revision locking.

## Tool annotations

All registered tools set `openWorldHint: false`. The candidate marks `update_taste_profile`, `remove_taste_preference`, `reset_taste_profile`, `record_prompt_feedback`, `save_creative_brief`, `update_project`, `update_persona`, `update_prompt`, `save_album_track` with `destructiveHint: true` because they can replace existing user data or remove preferences. Other tools set it false. These annotations describe the candidate registry; verify the production tool scan before submission.

Read tools set `readOnlyHint: true`, use OAuth scope `wizprompt:read`, and currently get `idempotentHint: true` through the shared registration helper.

Write tools set `readOnlyHint: false` and use OAuth scopes `wizprompt:read` and `wizprompt:write`. Write tools set `idempotentHint: false` by default unless the registration explicitly marks them idempotent.

Write tools explicitly marked `idempotentHint: true`:

- `create_prompt_revision`
- `create_project`
- `update_project`
- `create_persona`
- `update_persona`
- `save_prompt`
- `update_prompt`
- `save_album_track`

Write tools currently using the default `idempotentHint: false`:

- `record_prompt_feedback`
- `save_creative_brief`
- `update_taste_profile`
- `remove_taste_preference`
- `reset_taste_profile`

## Error handling

Tool errors return `isError: true`, text content, and structured `{ error, code }`.

Known codes include:

- `membership_required` for missing paid WizPrompt entitlement.
- `idempotency_conflict` for conflicting idempotent retries.
- `insufficient_scope` for missing write scope; write-scope failures include an MCP `WWW-Authenticate` challenge in `_meta["mcp/www_authenticate"]`.
- `bad_request` for malformed fetch targets or mismatched linked records.
- `mcp_tool_error` for unexpected server-side failures.

A ChatGPT response may say a record is saved, updated, or synced only after the corresponding tool returns success and a stable record ID.

## Personal preference storage and concurrency

Preference tools share the existing Clerk private-metadata store with a 12-preference and 3KB namespace limit. Personal defaults are separate from `studio_memory.creative_brief`. Current explicit instructions and approved project choices take precedence. Clerk deep merge preserves unrelated metadata; null removes only the selected preference or taste namespace. Stored malformed data produces a controlled reset-needed error, and reset can recover it. Preference writes are not a transaction or revision-locking mechanism: simultaneous edits to the same preference use provider last-write behavior, and count/size prechecks cannot enforce a strict global limit under concurrent writes.

## UI resource

`prepare_song` declares `_meta.ui.resourceUri` and the compatibility `openai/outputTemplate`. Resource `ui://wizprompt/song-package/v1.html` uses `text/html;profile=mcp-app`, content-level restrictive CSP metadata, the MCP Apps initialize/notification bridge and optional `window.openai` compatibility. The panel has no external network dependencies. Authenticated ChatGPT rendering and its actual clipboard policy remain separate acceptance checks from local simulated-host tests.
