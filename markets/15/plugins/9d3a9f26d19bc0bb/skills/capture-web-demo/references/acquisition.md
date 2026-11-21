# Acquisition commands

`wandeo` denotes the plugin launcher. Each result is `{ok,result}`; check failures before using IDs.

```text
wandeo project init --project <work> --title "Product film"
wandeo source add --project <work> --input <website-or-GitHub-URL-or-local-repository>
wandeo source search --project <work> --query "demo" --source <source-id>
wandeo source read --project <work> --source <source-id> --path README.md --offset 0 --limit 12000
wandeo source fetch --project <work> --source <source-id> --url <direct-media-URL>
wandeo runtime prepare --name node --version 24.21.0
```

For a different portable runtime, supply a JSON descriptor with `name`, exact `version`, public HTTPS `packageUrl`, `sha256`, `archive` (`zip` or `tar.gz`) and relative `binDirectories`. Node metadata is resolved automatically. Missing database or OS services are reported, not fabricated.

Write execution requests to files and pass `--request` to preserve argument boundaries:

```json
{
  "sourceId": "source-ID_FROM_IMPORT",
  "command": "node",
  "args": ["server.mjs"],
  "cwd": ".",
  "runtimeId": "ID_FROM_RUNTIME_PREPARE",
  "requestKey": "start-web-demo"
}
```

`exec start` returns an ID and the execution copy. Use `exec status`, `exec logs` (with optional `--offset`/`--limit`), and `exec stop --id <id>`. Installation may use an absolute runtime Node with its npm CLI, or the appropriate project launcher. Explicit environment variables may be passed in `env`; application credentials are not inherited automatically. The execution copy is not an OS security sandbox.

```text
wandeo browser open --project <work> --url http://127.0.0.1:4173 --width 1440 --height 900 --dpr 2
wandeo browser record-start --project <work> --source <source-id> --no-cursor
wandeo browser act --project <work> --request <actions.json>
wandeo browser record-stop --project <work>
wandeo browser close --project <work>
```

Actions can be a JSON array, for example:

```json
[
  {"type":"click","selector":"button[data-action=run]","resultSelector":"[data-state=complete]"},
  {"type":"wait","selector":"[data-state=complete]"},
  {"type":"scroll","deltaY":400},
  {"type":"wait","seconds":1}
]
```

Other actions: `click` with viewport `x/y`, `move` with `x/y`, `type` with `selector/text/clear`, and `press` with a Puppeteer key name. The worker preserves the page across calls and returns a fresh screenshot. Only operate authorized pages and handle external actions according to the host's permissions.

`--dpr` accepts 1 or 2; a new browser defaults to normal pixel density. Density is fixed for that browser session because Chromium screencast uses its native surface. Choose it before collecting footage; if a browser is already open at another density, close it and reopen at the intended URL with the desired `--dpr`. The physical frame must stay below 16 megapixels. Check the imported recording's probed dimensions before authoring a close-up. `--no-cursor` is optional; without it a pointer is embedded in the recording.

Each recorded action stores its time and visible target region, plus the result region when `resultSelector` is provided. Entered input values are not stored in the action metadata. Regions use normalized viewport coordinates, so they also work with higher-density capture. `media interactions --asset <id> [--offset --limit]` reads the sidecar; `media focus --asset <id> --start <source-start> --end <source-end>` offers camera candidates. The recorder's startup timing uncertainty is included; inspect frames near the action before precise editing.
