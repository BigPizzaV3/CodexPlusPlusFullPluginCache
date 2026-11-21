---
title: Streaming, Errors, and Credits
description: Consume Sprite Fusion SSE events, handle failures safely, and check credit balances.
---

Every accepted generation returns `text/event-stream`. Each event is one JSON object on a `data:` line. Comment heartbeats such as `: keep-alive` contain no JSON and should be ignored.

One request can return multiple assets. Collect every `output` until `completed`, then check the collected count against `output_count`.

## Event sequence

`started` appears exactly once after the 15-credit reservation succeeds:

```json
{"type":"started","request_id":"req_...","operation":"edit","credits":{"reserved":15,"remaining":285}}
```

`progress` reports that generation is underway:

```json
{"type":"progress","message":"Generating sprites"}
```

`output` appears once for every persisted asset, as soon as it is ready:

```json
{"type":"output","index":0,"asset":{"id":"...","type":"image","assetUrl":"https://media.spritefusion.com/...","contentType":"image/png","width":32,"height":32}}
```

`completed` is the final JSON event:

```json
{"type":"completed","status":"succeeded","output_count":9,"credits":{"remaining":285}}
```

`status` is `succeeded` or `failed`. A request succeeds publicly once at least one usable output is saved. A failed completion includes a safe `error` object.

## JavaScript Example

```js
const response = await fetch("https://www.spritefusion.com/api/v1/generate", {
  method: "POST",
  headers: {
    authorization: `Bearer ${process.env.SPRITE_FUSION_API_KEY}`,
    "content-type": "application/json",
  },
  body: JSON.stringify({ operation: "generate", prompt: "A tiny observatory", size: 32 }),
});
if (!response.ok) throw new Error(await response.text());

const reader = response.body.getReader();
const decoder = new TextDecoder();
let buffer = "";
let completed = false;

while (true) {
  const { value, done } = await reader.read();
  if (done) break;
  buffer += decoder.decode(value, { stream: true }).replaceAll("\r\n", "\n");
  for (let boundary = buffer.indexOf("\n\n"); boundary >= 0; boundary = buffer.indexOf("\n\n")) {
    const block = buffer.slice(0, boundary);
    buffer = buffer.slice(boundary + 2);
    const json = block.split("\n").filter((line) => line.startsWith("data:")).map((line) => line.slice(5).trimStart()).join("\n");
    if (!json) continue;
    const event = JSON.parse(json);
    if (event.type === "output") console.log(event.asset.assetUrl);
    if (event.type === "completed") completed = true;
  }
}
if (!completed) throw new Error("stream_interrupted");
```

## Python Example

```python
import json, os, requests

response = requests.post(
    "https://www.spritefusion.com/api/v1/generate",
    headers={"Authorization": f"Bearer {os.environ['SPRITE_FUSION_API_KEY']}"},
    json={"operation": "generate", "prompt": "A tiny observatory", "size": 32},
    stream=True,
)
response.raise_for_status()
completed = False
for line in response.iter_lines(decode_unicode=True):
    if not line or line.startswith(":") or not line.startswith("data:"):
        continue
    event = json.loads(line[5:].lstrip())
    if event["type"] == "output":
        print(event["asset"]["assetUrl"])
    if event["type"] == "completed":
        completed = True
if not completed:
    raise RuntimeError("stream_interrupted")
```

Use `curl -N` to disable output buffering in shell examples.

## Interruption and retry behavior

EOF before `completed` means `stream_interrupted`. Do not automatically retry the generation POST: an output may already have been persisted and charged. Website history can recover persisted outputs.

If no output is persisted, Sprite Fusion refunds the reservation.

## Pre-stream errors

Validation and authentication failures are ordinary JSON:

```json
{"error":{"code":"invalid_request","message":"At least one input image is required."}}
```

- `400`: malformed JSON or invalid operation, prompt, parameter, or input
- `401`: missing, invalid, or revoked authentication
- `402`: access gate or insufficient credits
- `404`: owned asset or temporary input not found
- `413`: request, image, byte, dimension, or pixel limit exceeded
- `429`: account rate limit or temporary credit contention; honor `Retry-After`
- `500`: unexpected application failure
- `502` or `503`: service temporarily unavailable before streaming, where applicable

## Credits

Check the balance without modifying it:

```bash
curl -sS https://www.spritefusion.com/api/v1/credits \
  -H "Authorization: Bearer $SPRITE_FUSION_API_KEY"
```

Session requests and all API keys belonging to the same account share account-level generation and upload-URL rate limits.
