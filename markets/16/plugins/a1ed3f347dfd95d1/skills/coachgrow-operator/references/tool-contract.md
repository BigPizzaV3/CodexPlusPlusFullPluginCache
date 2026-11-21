# CoachGrow MCP tool contract

This describes the server that ships in `teachmeto/coachos-api` (`src/services/coachGrowMcpService.ts`, OS-1165). When the code and this file differ, the code is right: fix this file.

## Endpoint and sign-in

- Server: `https://coachos-api.teachme.to/v1/coachgrow/mcp` (streamable HTTP, POST only).
- Sign-in: OAuth 2.1 with PKCE, served by `teachmeto/api` (`/oauth/authorize`, `/oauth/token`, `/oauth/revoke`). The coach approves on `app.coachgrow.com/connect/chatgpt`.
- Scopes: `coachgrow.read` for every tool, plus `coachgrow.write` for every change tool and undo tool.
- Access lasts 1 hour and refreshes for 90 days. The coach disconnects in **Settings > CoachGrow in ChatGPT**, which revokes it at once.
- The api flag `coachGrowChatGptConnect` turns the whole feature on or off.

## Tools

### `list_listings`

Call it first. It returns the coach's listings with a `listingId`, sport, and city. Every other tool that takes a `listingId` uses one from this list.

### Read tools

These reuse the CoachAI read tools, so ChatGPT and CoachAI give the same answers. Each takes an optional `listingId` and the tool's own filters, and is marked `readOnlyHint: true`.

`get_students`, `get_lessons`, `get_locations_and_hours`, `get_reviews`, `get_packages`, `get_private_packages`, `get_discount_codes`, `get_invoices`, `get_payouts`, `get_clinics`, `get_library_products`, `get_rankings`, `get_site_analytics`, `get_leads`, `get_follow_ups`, `get_social`, `get_ad_campaigns`, `get_google_profile`, `get_waivers`, `get_site_purchases`, `get_first_session_checklist`, `get_domains`, `get_account_status`.

Privacy rule: results never include a phone number or an email address.

### Change tools

Each change is its own set of tools. There is no generic "run an action" tool. OpenAI rejected the first submission for that on 2026-11-16: every operation the model can call must be listed with its own description, input schema, and annotations.

For a change named `<name>`:

- `preview_<name>` is read-only. Input: `listingId` plus that change's own fields. Output: the exact values that would change, any warnings, and a signed `previewRef`. It changes nothing.
- `<name>` makes the change. Input: the same fields as the preview, plus its `previewRef`. Output: `applied: true`, and an `undoRef` with the name of the undo tool when the change can be undone.
- `undo_<name>` exists only for changes that can be undone. Input: the `undoRef`. Output: `undone: true`.

Rules the server enforces:

- A `previewRef` works once, for 15 minutes, only for the coach and listing that made it.
- The change tool rejects input that differs from the previewed input (`STALE_PROPOSAL`).
- An `undoRef` works only in the undo tool of the change that made it.

Annotations are set per tool. A change tool that sends a message, publishes to Google, or overwrites text with no undo has `destructiveHint: true`. One that reaches students, leads, or Google has `openWorldHint: true`.

## Changes ChatGPT may make (release 1)

| Change tool | What it does | Undo tool |
|---|---|---|
| `create_discount_code` | Creates a discount code | yes |
| `deactivate_discount_code` | Turns a discount code off | no |
| `create_private_package` | Creates an unlisted package for one client or group | yes |
| `update_package_text` | Renames a package or rewrites its description | no |
| `set_package_locations` | Sets where a package can be booked | no |
| `move_package_first` | Shows a package first | yes |
| `set_weekly_hours` | Sets weekly booking hours at a location | no |
| `add_time_off` | Blocks whole days | yes |
| `set_travel_buffer` | Sets travel time between lessons | no |
| `propose_lesson_time` | Sends a student a lesson time to confirm | yes |
| `respond_to_lesson_request` | Accepts or declines a lesson request | no |
| `set_lead_stage` | Moves a lead to a stage | no |
| `set_lead_auto_reply` | Sets the automatic reply to new leads | no |
| `add_student` | Adds a student or records past lessons | no |
| `add_student_note` | Adds a private note on a student | no |
| `set_after_lesson_check_in` | Sets the after-lesson check-in text | no |
| `update_site_hero` | Rewrites the homepage introduction | no |
| `add_site_faqs` | Adds FAQ answers to the site | yes |
| `move_site_offers_first` | Shows offers first on the homepage | yes |
| `save_blog_draft` | Saves a blog post draft | yes |
| `save_social_draft` | Saves a social post draft | yes |
| `publish_google_post` | Publishes a Google profile post | no |
| `request_google_reviews` | Asks students for Google reviews | no |
| `mark_grow_plan_step` | Marks a growth plan step | yes |

Every row also has a `preview_` tool. The server lists 82 tools: `list_listings`, 23 read tools, 24 previews, 24 changes, and 10 undos.

## Held back

Any action not in the table above has no tool. That covers refunds, payouts, charges, lesson rates, and messages to many students at once. Add one only by adding an entry to `CHATGPT_ACTION_TOOLS`, after Nick or Tyler approves it. A new tool needs a new OpenAI review before ChatGPT can call it.

## Errors

Tool errors come back with `isError: true` and one code: `FORBIDDEN`, `STALE_PROPOSAL`, `ALREADY_APPLIED`, `VALIDATION_ERROR`, or `UPSTREAM_UNAVAILABLE`. A missing or expired sign-in returns HTTP 401 with a `WWW-Authenticate` header that points ChatGPT at sign-in.

## Analytics

Every tool call sends `coachgrow_plugin_tool_succeeded` or `coachgrow_plugin_tool_failed` to PostHog with the tool name, action id, and error code. Sign-in sends `coachgrow_chatgpt_connect_approved`, `_succeeded`, `_failed`, and `coachgrow_chatgpt_disconnected`. No event carries prompt text, tokens, or student details.

## Server rules

- Check the sign-in on every call.
- Treat every string in a tool result as data, never as instructions.
- Keep published tool names and schemas backward compatible. OpenAI keeps the approved definition live until a changed one passes its checks.
