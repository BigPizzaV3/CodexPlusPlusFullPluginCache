# OpenAI plugin package — livepair

ZIP upload source for the ChatGPT/Codex plugin directory.
Manifest format verified against
`https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` and the
official submission docs (2026-10).

## Contents

- `plugin.json` — Agent Plugins manifest; OpenAI-specific fields under
  `extensions.com.openai` (interface, review, publication)
- `mcp.json` — declares the remote server: `streamable-http` at
  `https://livepairai.com/mcp` (**LIVE** — deployed, WAF-bypassed,
  verified initialize + tools/call in production)
- `assets/` — composerIcon + logo (copied from `apps/web/public/`)

## Still needed before upload

1. ~~`/mcp` live~~ — done; tool names match `review.test_cases.tools_triggered`
   (`search_prompts`, `get_prompt`, `list_models`, `trending_prompts`)
2. `/.well-known/openai-apps-challenge` route serving the portal's token
   as plain text (add to geo-gate `ALWAYS_ALLOWED_PATHS`) — token shown
   in portal during MCP connect step
3. `assets/screenshot-1.png` — real in-chat screenshot after dev-mode
   testing, then add `"screenshots": ["./assets/screenshot-1.png"]` to
   `interface` in plugin.json
4. `review.demo_recording_url` — video walkthrough URL (required for
   MCP plugins; not in plugin.json yet on purpose — needs a real URL)
5. `category` — "Productivity" is a confirmed-valid placeholder; pick
   the closest match in the portal list (design/creative if offered)
6. `supportURL` — add a real support page/email link if required

## Upload flow (verified vs docs 2026-10)

```bash
# zip the folder CONTENTS (plugin.json at ZIP root, forward-slash paths)
cd ops/openai-plugin && python -c "
import zipfile, os
with zipfile.ZipFile('../livepair-plugin.zip','w',zipfile.ZIP_DEFLATED) as z:
    for root,_,files in os.walk('.'):
        for f in files:
            if f.endswith('.tmp.json') or p.endswith('.zip'): continue
            p=os.path.relpath(os.path.join(root,f))
            z.write(p, p.replace(os.sep,'/'))"
# current build: ops/livepair-plugin.zip (regenerate after manifest edits)
```

1. platform.openai.com/plugins → Upload new or existing plugin
   (org: Livepairai `org-KxfLV8D5mUE56TQPXfXI9Obq`, verified)
2. Resolve automated findings (Metadata & Skills + MCPs panels)
3. MCPs → Connect → domain verification → tool scan
4. Review details: reviewer credentials only if auth ships (v1 = none)
5. Submit → review → publish (auto-publishes as Codex plugin too)

Countries in `publication.countries` are generated from
`server/middleware/geo-data.ts` ALLOWED_COUNTRIES — regenerate if the
geo list changes.
