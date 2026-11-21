# Error catalog

Known failures, what they mean, and the fix. Check here before retrying anything — most of these
fail identically on retry.

## Call-shape errors

**"Tool not found" for a name you're sure exists**
This connector is flat — every tool is called by its own name, there are no routers and no
`action`/`list_tools` step. Check the exact spelling against your tool list (the platform is in the
name, e.g. `list_meta_campaigns` or `list_tiktok_campaigns`, not `list_campaigns`). If it genuinely
isn't listed, the host may show a reduced set; call the closest listed tool and read the error.

**A write returns a preview instead of running**
Spend-affecting or irreversible changes (creates with a budget, budget or bid edits,
resume/enable, duplicates, deletes) need `confirm: true`. Show the user the preview, get their yes,
then call the same tool again with the same arguments plus `confirm: true`. Don't set it
pre-emptively.

**A parameter was rejected ("field required", "unknown field", bad enum value)**
Don't guess the fix. Call `get_tool_schema` with the tool name — it returns the exact parameter
names, types, which are required, and the allowed values — then rebuild the call. `get_tool_schema`
is free, so read it before any write and before any read you haven't run before.

**`get_tool_schema` is not in your tool list**
Some clients show a reduced tool set. If it's missing, call the tool you want directly; if a
parameter is rejected, the error names the field — fix it from that. Never stop just because
`get_tool_schema` is missing.

## Account errors

**400, `multi_account`**
The user has two or more active accounts on that platform and none was named. The error lists the
accounts and the exact parameter to pass. Ask the user which one, then resend with
`ad_account_id` (Meta) or `advertiser_id` (TikTok).

**403 on an account id you passed**
That account is not connected, or was deactivated. Adspirer will *not* silently fall back to
another account, because that would report the wrong account's numbers. Do not retry without the
id. Call `get_connections_status`, show the user what is actually connected, and let them pick or
reconnect at `https://adspirer.ai/connections`.

**"No account found" / "connect your account"**
Nothing is connected for that platform, or the token expired. Point the user at
`https://adspirer.ai/connections`. Don't attempt the operation.

## Budget errors

**Meta campaign booked at 100× the intended budget**
You sent cents where the tool expects the account's own currency as a decimal. `daily_budget` and
`lifetime_budget` take the plain currency amount: `$50/day` is `50`, `$20/day` is `20`. The tool
converts to Meta's internal unit for you, so a value you meant as cents gets multiplied again —
sending `2000` for an intended `$20/day` books **`$2,000/day`**. Send the currency amount, never
cents, and never multiply by 100.

**TikTok: "Your budget setting must not be less than X"**
Below TikTok's per-currency daily floor. USD 20, EUR 20, GBP 15, CAD 25, AUD 30, SGD 25, BRL 100,
HKD 150, MXN 350, ZAR 500, TWD 600, PHP 1000, INR 1500, JPY 2500. Lifetime floor is roughly 7× the
daily floor. See `adspirer-tiktok-ads/references/validity-matrix.md`.

## TikTok

**Error 40002 on a single-image in-feed ad**
TikTok does not support single-image in-feed ads. Use a video ad or a Spark Ad
(`tiktok_item_id`). For a carousel, build it in TikTok Ads Manager, then boost that post here as a
Spark Ad.

**`pixel_id` rejected — `PIXEL_ID_NOT_ALLOWED_FOR_OBJECTIVE`**
An ad-group `pixel_id` is only valid for `CONVERSIONS`, `WEB_CONVERSIONS`, `PRODUCT_SALES`, and
`SHOP_PURCHASES`. For every other objective the pixel goes on the **ad** as `tracking_pixel_id`.
This is the most frequent TikTok error. When you do set an ad-group `pixel_id`,
`optimization_event` becomes required.

**`video_id` comes back as the string `"None"`**
The upload silently failed. The value is literally `"None"`, not null. Re-upload the video; do not
create the ad with it.

**CTA rejected**
`LEARN`, `VISIT`, and `GO` are not valid. Use `LEARN_MORE`, `SHOP_NOW`, `DOWNLOAD_NOW`, `SIGN_UP`,
`GET_QUOTE`, `BOOK_NOW`, or `INSTALL_NOW`.

## Meta

**Ad creation rejected — missing page**
Meta requires a Facebook `page_id` and an `http(s)` landing URL on every ad. Run
`list_meta_pages` first if you don't have one.

**Objective rejected**
Meta uses ODAX objectives: `OUTCOME_AWARENESS`, `OUTCOME_TRAFFIC`, `OUTCOME_ENGAGEMENT`,
`OUTCOME_LEADS`, `OUTCOME_APP_PROMOTION`, `OUTCOME_SALES`. Legacy names (`CONVERSIONS`,
`LINK_CLICKS`, `LEAD_GENERATION`) are auto-mapped, but prefer the ODAX name.

**Write blocked / rate limited**
Meta campaign creation is rate-guarded per user (100/hr, 300/day). Updates and pauses are not
limited. If a write is blocked, stop — do not retry in a loop.

## Quota

**Quota exceeded**
Tell the user they've reached their limit for this period and when it resets. Do not route around
it, do not switch to another tool to get the same data, and never fabricate the numbers.
`get_tool_schema`, `get_usage_status`, and `get_connections_status` remain free.
