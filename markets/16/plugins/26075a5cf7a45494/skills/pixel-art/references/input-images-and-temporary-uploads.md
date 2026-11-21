---
title: Input Images
description: Supply owned assets, small inline images, or private staged images to the Sprite Fusion API.
---

Image inputs can be passed in three ways:

```json
{"asset_id":"owned_sprite_id"}
```

```json
{"data_url":"data:image/png;base64,..."}
```

```json
{"upload_id":"upl_..."}
```

## Input counts and ordering

- `generate`: no inputs
- `edit`: 1–9 inputs; the first image is the primary sprite and later images are supporting visual sources
- `style-reference`: 1–20 inputs
- `direction-set`: exactly 1 input
- `animate`: exactly 1 input

## Inline limits

Use a data URL for small sprites that keep the whole JSON request comfortably below the platform limit.

- Sprite Fusion JSON request limit: 4,000,000 UTF-8 bytes
- Underlying request-body ceiling: 4.5 MB
- Decoded inline image: 1,000,000 bytes each
- Decoded inline images: 2,500,000 bytes total
- Accepted formats after decoding: still PNG, JPEG, and WebP
- Maximum dimension: 4,096 pixels
- Maximum pixels: 12,000,000 per image and across all inputs

SVG, GIF, animated WebP, HEIC, malformed base64, decompression bombs, and zero-sized images are rejected.

## Stage a larger input

Use a private temporary upload for a large file that would make the JSON request too large. Each staged object may be up to 20 MiB; all inputs may total up to 40 MiB.

Calculate the exact byte length and SHA-256 digest:

```bash
FILE="reference.png"
SIZE_BYTES=$(wc -c < "$FILE" | tr -d ' ')
SHA256=$(shasum -a 256 "$FILE" | awk '{print $1}')
```

Request an upload URL:

```bash
curl -sS https://www.spritefusion.com/api/v1/uploads \
  -H "Authorization: Bearer $SPRITE_FUSION_API_KEY" \
  -H "Content-Type: application/json" \
  --data "{\"content_type\":\"image/png\",\"size_bytes\":$SIZE_BYTES,\"sha256\":\"$SHA256\"}" \
  > upload.json
```

The response includes `upload_id`, `upload_url`, `upload_url_expires_at`, `upload_id_expires_at`, and the exact required headers. The upload URL expires after five minutes; the upload ID can be used for about one day.

Upload the raw bytes directly using every returned header:

```bash
UPLOAD_URL=$(jq -r .upload_url upload.json)
curl --fail-with-body -X PUT "$UPLOAD_URL" \
  -H "Content-Type: image/png" \
  --data-binary @"$FILE"
```

Then reference the signed descriptor in generation:

```bash
UPLOAD_ID=$(jq -r .upload_id upload.json)
curl -N https://www.spritefusion.com/api/v1/generate \
  -H "Authorization: Bearer $SPRITE_FUSION_API_KEY" \
  -H "Content-Type: application/json" \
  --data "{\"operation\":\"edit\",\"prompt\":\"Use the armor from the reference image\",\"inputs\":[{\"upload_id\":\"$UPLOAD_ID\"}]}"
```

The direct `PUT` is only an upload; it does not start generation or create a library asset.

Pre-signed URLs are short-lived bearer credentials. Do not log `upload_url` or `upload_id`. Temporary inputs are private and have no download URL.

## JavaScript Example

```js
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";

const bytes = await readFile("reference.png");
const descriptor = await fetch("https://www.spritefusion.com/api/v1/uploads", {
  method: "POST",
  headers: {
    authorization: `Bearer ${process.env.SPRITE_FUSION_API_KEY}`,
    "content-type": "application/json",
  },
  body: JSON.stringify({
    content_type: "image/png",
    size_bytes: bytes.byteLength,
    sha256: createHash("sha256").update(bytes).digest("hex"),
  }),
}).then((response) => response.json());

const uploaded = await fetch(descriptor.upload_url, {
  method: "PUT",
  headers: descriptor.headers,
  body: bytes,
});
if (!uploaded.ok) throw new Error(`Upload failed: ${uploaded.status}`);
```
