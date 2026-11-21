---
title: API Reference
description: Endpoint, request, response, and event reference for the Sprite Fusion API.
---

Base URL:

```text
https://www.spritefusion.com/api/v1
```

Authenticate every API request with your API key:

```http
Authorization: Bearer $SPRITE_FUSION_API_KEY
```

## GET /credits

Returns the credits currently available to the account.

```bash
curl -sS https://www.spritefusion.com/api/v1/credits \
  -H "Authorization: Bearer $SPRITE_FUSION_API_KEY"
```

```json
{"credits":285}
```

## GET /assets

Lists your saved assets from the editor, API, and integrations, newest first. Both asset endpoints require authentication and consume no credits.

```bash
curl -sS 'https://www.spritefusion.com/api/v1/assets?limit=10' \
  -H "Authorization: Bearer $SPRITE_FUSION_API_KEY"
```

`limit` is optional: 1–100 assets, default 20. Batch members count individually, retain their batch metadata, and may span pages.

Returns `assets`, `hasMore`, and `nextCursor`. Start without a `cursor`. For the next page, pass `nextCursor` unchanged as the URL-encoded `cursor` query parameter. Stop when `nextCursor` is `null` (`hasMore: false`).

Each asset matches `output.asset`: ID, type, prompt, dimensions, timestamps, and `assetUrl`. Animations also include `sourceImageUrl`, `spritesheetUrl`, `frameCount`, and optional `fps`.

## GET `/assets/{assetId}`

Returns `{"asset": {...}}` for an asset you own, with the same fields as the list endpoint.

Returned file URLs are public and can be downloaded directly. Reuse an image asset's `id` as an `asset_id` input for generation requests.

## POST /uploads

Creates a short-lived upload URL for an input image. Send JSON with these fields:

| Field | Type | Description |
| --- | --- | --- |
| `content_type` | string | `image/png`, `image/jpeg`, or `image/webp` |
| `size_bytes` | integer | Exact file size, up to 20 MiB |
| `sha256` | string | Lowercase SHA-256 digest of the file |

```json
{
  "content_type": "image/png",
  "size_bytes": 12480,
  "sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
}
```

The response contains the signed `upload_id`, upload URL, their separate expiry times, and headers to use for the upload:

```json
{
  "upload_id": "upl_...",
  "upload_url": "https://...",
  "upload_url_expires_at": "2026-08-28T12:05:00.000Z",
  "upload_id_expires_at": "2026-08-29T12:00:00.000Z",
  "headers": {"Content-Type":"image/png"}
}
```

See [Input Images](https://www.spritefusion.com/docs/pixel-art-generator/api/input-images-and-temporary-uploads) for the complete upload flow.

## POST /generate

Starts any generation or transformation operation. Send `Content-Type: application/json`. A successful request returns a `text/event-stream` response.

| Operation | Required fields | Optional fields |
| --- | --- | --- |
| `generate` | `prompt`, `size` | — |
| `edit` | `prompt`, `inputs` (1–9) | `size` |
| `style-reference` | `prompt`, `inputs` (1–20) | `size` |
| `direction-set` | `inputs` (exactly 1) | `size` |
| `animate` | `prompt`, `inputs` (exactly 1) | `output_frames`, `colors` |

Image `size` may be `16`, `32`, or `64`. Animation `output_frames` must be an even number from 2 to 16, and `colors` must be an integer from 2 to 256.

```json
{
  "operation": "edit",
  "prompt": "Give this character a blue cape",
  "inputs": [{"asset_id":"asset_..."}],
  "size": 32
}
```

Each item in `inputs` uses one of the following forms:

```json
{"asset_id":"asset_..."}
```

```json
{"data_url":"data:image/png;base64,..."}
```

```json
{"upload_id":"upl_..."}
```

See [Generate and Transform Sprites](https://www.spritefusion.com/docs/pixel-art-generator/api/generate-and-transform-images) for an example of every operation.

## Stream events

Each JSON event is sent on an SSE `data:` line.

See the [Agent Guide for tracking results and revisions](https://www.spritefusion.com/docs/pixel-art-generator/api/agent-guide#keep-results-available-for-follow-up-work).

| Event | Description |
| --- | --- |
| `started` | The request started and credits were reserved |
| `progress` | Generation is underway |
| `output` | Emitted once per saved asset, with its index and asset details |
| `completed` | Final event with `succeeded` or `failed` and the total `output_count` |

```text
data: {"type":"started","request_id":"req_...","operation":"edit","credits":{"reserved":15,"remaining":285}}

data: {"type":"progress","message":"Generating sprites"}

data: {"type":"output","index":0,"asset":{"id":"asset_1","type":"image","assetUrl":"https://media.spritefusion.com/example-1.png"}}

data: {"type":"output","index":1,"asset":{"id":"asset_2","type":"image","assetUrl":"https://media.spritefusion.com/example-2.png"}}

data: {"type":"completed","status":"succeeded","output_count":2,"credits":{"remaining":285}}
```

See [Streaming, Errors, and Credits](https://www.spritefusion.com/docs/pixel-art-generator/api/streaming-errors-and-credits) for complete readers and interruption handling.

## Errors

Errors returned before streaming use JSON:

```json
{"error":{"code":"invalid_request","message":"At least one input image is required."}}
```

| Status | Meaning |
| --- | --- |
| `400` | Invalid request or image |
| `401` | Missing, invalid, or revoked authentication |
| `402` | Subscription or credit requirement not met |
| `404` | Asset or input image not found |
| `413` | Request or image limit exceeded |
| `429` | Rate limit or temporary credit contention |
| `500` | Unexpected application failure |

When a `429` response includes `Retry-After`, wait that many seconds before trying again.
