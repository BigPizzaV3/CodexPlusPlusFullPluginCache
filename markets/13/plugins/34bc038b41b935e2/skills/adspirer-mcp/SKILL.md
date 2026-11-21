---
name: adspirer-mcp
description: How to call the Adspirer Social Ads connector correctly — it exposes every Meta (Facebook/Instagram) and TikTok operation as its own top-level tool (no routers, no two-step). Covers get_tool_schema as the way to read a tool's exact parameters before calling it, the confirm-preview rule for spend-affecting changes, per-platform account IDs, quota rules, and the budget unit (the account's own currency as a decimal — never cents). Load this before making any Adspirer tool call.
---

# Calling the Adspirer Social Ads connector

Adspirer Social Ads is a **flat connector** for **Meta Ads (Facebook + Instagram)** and
**TikTok Ads**: every ad operation is its own top-level tool, called by its own name. There are
**no routers** and there is **no `list_tools` / `action` / two-step** — if a tool is in your tool
list, call it directly. Read this before your first tool call.

## The shape of the surface

There are about **100 tools**, named for exactly what they do and which platform they touch:
`list_meta_campaigns`, `search_meta_targeting`, `analyze_meta_wasted_spend`,
`update_meta_campaign`, `get_tiktok_campaign_performance`, `create_tiktok_video_campaign`,
`add_tiktok_ad_group`, and so on. Meta tools have `meta` in the name, TikTok tools have `tiktok`,
so a tool only ever acts on the platform it names. You call the tool directly:

```json
{
  "name": "list_tiktok_campaigns",
  "arguments": { "advertiser_id": "7012345678901234567" }
}
```

Read-only tools (reports, lists, analysis, targeting research) are marked read-only; tools that
create, update, pause, resume or delete are marked as changing data.

A few tools are platform-neutral and the ones to reach for first:

| Tool | Use it for |
|---|---|
| `get_tool_schema` | The exact parameters for any tool, before you call it. Free. |
| `get_connections_status` | Which Meta and TikTok accounts are connected, and their health. Free. |
| `get_usage_status` | Tool calls used and left this period, and when it resets. Free. |
| `activate_ad_accounts` | Change which account is active. Only when the user asks. |
| `get_meta_campaign_performance` | Meta (Facebook/Instagram) performance dashboard. |
| `get_tiktok_campaign_performance` | TikTok campaign performance. |
| `competitor_ads_research` | A competitor's live ads, by website domain (ask for the domain; never guess it). |

## get_tool_schema — the one habit that keeps calls correct

The tools carry real, specific parameters, and the fastest way to get a call right the first time
is to read the schema before you send it. `get_tool_schema` returns a tool's exact parameter
names, types, which are required, and the allowed values — and it is **free and instant**.

**Use it like this:**

- **Before any write, and before any read you haven't called before**, pass the tool name(s) to
  `get_tool_schema` and build the arguments from what it returns. Don't guess a parameter name or
  an enum value.
- **Batch it.** `get_tool_schema` takes one name or a list (`{"tool_names": ["…", "…"]}`), so when
  a task spans several tools (create a campaign, add an ad set, add an ad), ask for all of them in
  one call and read them together before you start.
- **It is free.** It never counts against the user's quota, so there is never a reason to skip it
  to save calls or to guess instead.
- **If it isn't in your tool list**, some hosts show a reduced set; call the tool you want directly
  and, if a parameter is rejected, read the error — it names the field. Never stop because
  `get_tool_schema` is missing.

If you don't know *which* tool does a job, the names are descriptive — scan your tool list for the
platform + verb (`create_…`, `list_…`, `analyze_…`, `update_…`, `pause_…`). When in doubt,
`get_tool_schema` the closest-looking candidates and compare.

### The flow

1. Know the task and the platform.
2. `get_tool_schema` the tool (or tools) you intend to call — read the required params and enums.
3. Call the tool directly by name with arguments that match the schema.
4. For a write, read the object back (a `list_…` or `get_…` tool) and confirm it landed.

## Changes that spend or can't be undone: preview, then `confirm: true`

Spend-affecting or irreversible changes — creates with a budget, budget or bid edits, resuming or
enabling, duplicates, and deletes — take a `confirm` flag. Called without it, the tool returns a
**preview and does not run**. Show the user the preview, get their clear yes, then call the **same
tool again** with the same arguments plus `confirm: true`. Don't set it pre-emptively.

Pausing is reversible and runs immediately. Deletes (`delete_tiktok_campaign`,
`delete_tiktok_ad_group`, `delete_tiktok_ad`) cascade and cannot be undone — confirm the exact
object first. Most create tools create campaigns paused; if a tool creates something active, tell
the user.

## Budgets: the unit is the same everywhere, and it is NOT cents

This is the single most common and most expensive error. **Read this before you send a budget.**

| Platform | Unit | `$50/day` becomes |
|---|---|---|
| Meta Ads | account currency (decimal) | `50.0` |
| TikTok Ads | account currency (decimal) | `50.0` |

**Both platforms take the budget in the account's own currency as a plain decimal — never cents,
never multiplied by anything.** For `$20/day` send `20`, for `$50/day` send `50`. The tools convert
to each platform's internal unit for you; if you send `2000` meaning `$20` you will book
**`$2,000/day`** — a 100× overspend. Never convert the user's currency to USD; send the number in
the account's own currency, and read the created campaign back to confirm it.

## Accounts

One connected account is selected automatically. With two or more *active* accounts you must name
one — the call fails with a `multi_account` error that lists them.

The parameter name differs per platform:

| Platform | Parameter |
|---|---|
| Meta Ads | `ad_account_id` |
| TikTok Ads | `advertiser_id` |

Send IDs as **strings**, not numbers. Naming an account the user has not connected returns a 403 —
it never quietly falls back to another account, so do not treat 403 as "try again without the id."
Use `get_connections_status` to see what is connected.

## Quota

Most tool calls count toward the user's monthly allowance of tool calls.

**Free, call these as much as you need:** `get_tool_schema`, `get_connections_status`, and
`get_usage_status`.

Because reading a schema is free, there is never a reason to guess a tool name or a parameter to
save calls.

If a call is refused because the user's allowance is used up, tell the user plainly that they've
reached their limit for this period and when it resets (`get_usage_status` shows both). Don't work
around it, don't switch to another tool to get the same data, and never invent the numbers.

## Platforms the user hasn't connected

The Meta and TikTok tools are listed even before the user connects that platform. Calling one for
a platform that isn't connected returns a message asking the user to connect it. Relay that and
point them at `https://adspirer.ai/connections`; don't treat it as an error to retry.

## Out of scope

Only Meta and TikTok. Other ad platforms, SEO and domain-authority data, and financial or
investment advice are out of scope — say so; don't call a tool or make up an answer.

## When something fails

Read `references/error-catalog.md` for the known error codes and their fixes before retrying
anything. Retrying an invalid call unchanged will fail the same way — read the error (it usually
names the field), or `get_tool_schema` the tool, then fix the call.
