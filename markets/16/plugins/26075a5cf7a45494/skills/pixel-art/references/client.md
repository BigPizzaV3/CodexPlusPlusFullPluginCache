# Bundled client usage

This page describes the plugin's optional Python client. Sprite Fusion's documented operations, prompts, parameters, and retry guidance are in the other references.

The client uses Python 3.9+ and the standard library. Resolve `CLIENT` to `scripts/sprite_fusion.py` relative to this skill directory.

```bash
python3 "$CLIENT" credits
python3 "$CLIENT" assets --limit 20
python3 "$CLIENT" assets --limit 20 --cursor 'opaque-nextCursor-value'
python3 "$CLIENT" asset 'saved-asset-id'
python3 "$CLIENT" asset 'saved-asset-id' --output ./assets/recovered
python3 "$CLIENT" generate --request ./request.json --output ./assets/generated
```

`request.json` contains a request using the fields and examples in [Generate and Transform Sprites](generate-and-transform-images.md) and [API Reference](api-reference.md). The client's `generate` command sends any of the five documented operations to `POST /generate`.

Authentication uses `SPRITE_FUSION_API_KEY`. The client can also receive an already supplied key as one line of standard input with the global `--key-stdin` option before the command. `--request` takes a file path independently of standard input.

`assets` retrieves one page per call. `asset --output` downloads an existing saved asset. `generate --output` creates a run directory, prints that directory to stderr, and writes `result.json`. The record contains request information, source descriptors, returned asset metadata, and local file paths. The client downloads the returned asset files and, when supplied, animation source images and spritesheets. Partial records remain available after an interrupted stream.

Commands print JSON to stdout and progress to stderr. Exit codes are `0` for success with downloads saved, `1` for a request or completion failure, and `2` for a successful generation or retrieval with a download failure. The client makes one generation submission per invocation. Apply the retry guidance in [Streaming, Errors, and Credits](streaming-errors-and-credits.md) to the returned outcome.
