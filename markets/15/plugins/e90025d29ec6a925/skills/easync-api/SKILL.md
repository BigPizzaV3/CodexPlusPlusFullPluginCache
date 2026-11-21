---
name: easync-api
description: Work with an easync account through the easync User API - create eBay listings from Amazon/AliExpress/Walmart product IDs, review and publish drafts, track listing batches, read orders and update order notes. Use when the user asks to list products, check listing progress, approve or reject drafts, or look up easync orders.
---

# easync User API

easync lists products from source marketplaces (Amazon, AliExpress, Walmart) on the seller's
eBay (or Shopify/WooCommerce) stores, reprices them and fulfils orders. This API gives access
to one easync account.

- Base URL: `https://my.easync.io/api/v1`
- Auth header: `Authorization: Bearer <token>`. The token starts with `es_` and is created by
  the user in easync: Account → Preferences → API & MCP. Read it from an environment variable
  (e.g. `EASYNC_API_TOKEN`); never print it or store it in files.
- Full reference (all fields and schemas): `https://my.easync.io/openapi/easync-user-api-v1.yaml`.
- MCP: if the `easync` MCP server is connected (`https://my.easync.io/api/mcp`, with the same
  token in the `Authorization` header or through the OAuth sign-in that clients such as ChatGPT
  and Claude start automatically), prefer its tools - they map 1:1 to the endpoints below
  (`list_stores`, `create_listings`, `get_listing_batch`, `list_listing_batch_items`,
  `approve_listing_items`, `approve_listing_batch`, `reject_listing_items`, `list_orders`,
  `search_orders`, `get_order`, `update_order_notes`, ...) and follow the same rules.
- Start with `GET /me` to see which scopes the token has. A missing scope returns
  `403 insufficient_scope`; the user must create a new token with that scope (scopes cannot be
  added to an existing token).

## Conventions

- JSON responses: `{"data": ...}`, lists add `nextCursor` (pass it as `cursor`; `null` = last page).
- Errors: `{"error": {"code": "...", "message": "..."}}`.
- Prices are decimals in the given currency (`{"amount": 8.49, "currency": "USD"}`); dates are ISO 8601 UTC.
- Rate limit: 120 requests/minute per token. On `429` wait `Retry-After` seconds.

## Creating listings (scopes `listings:read`, `listings:write`)

1. `GET /stores` - pick the store. Check `active`, `activeListings`, `plan` (account listings
   limit/usage) and `ebaySellingLimits` (remaining eBay quantity/amount). Do not submit to a
   store with `active: false`.
2. `POST /stores/{storeId}/listing-requests`:
   ```json
   {"source": "amazon_us", "mode": "draft", "productIds": ["B09KLZNXRH"], "addVariants": false, "name": "optional batch name"}
   ```
   - `source`: `amazon_us|uk|de|fr|it|es|ca|au` (ASINs, 10 chars), `aliexpress_us|uk`,
     `walmart_us` (numeric IDs). Send IDs, never URLs.
   - `mode`: `publish` = easync publishes automatically after parsing (items with problems
     stay as drafts); `draft` = everything stops as a draft for review.
   - Up to 500 IDs per request, 5000 accepted IDs per account per UTC day.
   - Response `202`: `batchId`, `accepted`, `acceptedProductIds`, `skipped[{productId, reason}]`.
     `200` with `batchId: null` means every ID was skipped.
3. Track: `GET /listing-batches/{batchId}` returns `counts` by status. Poll every few minutes;
   parsing takes minutes. Done when `processing` and `publishing` are 0.
4. Review: `GET /listing-batches/{batchId}/items?status=draft` - each item has `title`,
   `price`, `profit`, `quantity`, `errors[]`.
5. Act on drafts:
   - `POST /listing-batches/{batchId}/approve` - publish all ready drafts of the batch;
   - `POST /listing-requests/approve` `{"ids": [...]}` - publish selected items (max 500);
   - `POST /listing-requests/reject` `{"ids": [...]}` - discard selected drafts.
   The response lists `approved`/`rejected` IDs and `skipped[{id, reason}]`.

Item statuses: `processing` (parsing / pricing / about to auto-publish), `draft` (waits for
approve or reject; `errors` explain a failed publish attempt), `publishing`, `published`
(`target.productId` = eBay item ID), `failed` (product could not be parsed, nothing to approve),
`rejected`.

Skip reasons on submit: `invalid_product_id`, `duplicate_in_request`, `already_listed` (an
active listing of this product exists in this store, or in another eBay store of the account),
`already_in_progress` (submitted to this store within 7 days and not finished). Skipped IDs do
not count towards the daily limit. Do not resubmit them; `failed` and `rejected` products may
be submitted again later.

Skip reasons on approve: `not_ready` (price or variation data missing - fix in the app or
reject), `not_draft`, `already_publishing`, `already_published`, `already_rejected`, `failed`,
`store_disabled`, `plan_limit_reached`, `not_found`.

### Rules

- Confirm with the user before `mode: publish`, `approve` or `reject` on more than a handful of
  items: these create or discard real eBay listings.
- Pace submissions per store (e.g. a fixed number per day) instead of sending everything at
  once; new eBay accounts have low selling limits and listings above them fail at publish time.
- Errors `plan_limit_reached` (403), `store_inactive` / `store_disabled` (400) need user action
  in easync; report them instead of retrying. `daily_limit_reached` (429) resets at 00:00 UTC.

## Orders (scopes `orders:read`, `orders.source:read`, `orders.notes:write`)

- `GET /orders?store=&status=&autoOrderState=&soldAfter=&soldBefore=&limit=&cursor=` - newest first.
- `GET /orders/search?ebayOrderId=23-15210-10870` or `?sourceOrderId=113-7921422-2976214`.
- `GET /orders/{id}`, `GET /orders/{id}/source-orders` (needs `orders.source:read`).
- `PUT /orders/{id}/notes` `{"text": "...", "mode": "append"}` (`append` default, or `replace`;
  text up to 2000 chars, notes up to 10000).

## Example

```bash
curl -s -X POST -H "Authorization: Bearer $EASYNC_API_TOKEN" -H "Content-Type: application/json" \
  -d '{"source":"amazon_us","mode":"draft","productIds":["B09KLZNXRH","B0FXBH3HN5"]}' \
  https://my.easync.io/api/v1/stores/<storeId>/listing-requests
```
