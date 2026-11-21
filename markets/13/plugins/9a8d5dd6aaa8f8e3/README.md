# PropETL ChatGPT/Codex plugin package

Portable **Agent Plugins** package for submission to OpenAI's universal plugin
directory (shared by ChatGPT and Codex). This folder is the source of truth for
the ZIP uploaded at https://chatgpt.com/plugins (portal → Upload new or existing
plugin).

## Layout

```
chatgpt-plugin/
├── plugin.json          # portable manifest (agent-plugins.org schema 1.0.0)
│                        #   + extensions.com.openai: interface, review, publication
├── mcp.json             # the ONE bundled MCP server: https://mcp.propetl.com/mcp
│                        #   streamable-http, OAuth (CIMD preferred, DCR fallback),
│                        #   baseScopes ["etl"] — declared in mcp.json, NOT plugin.json
└── assets/              # icon.png / logo.png (512px, white+gold brand)
```

Rules enforced by the portal (verified against developers.openai.com Oct 2026):

- No `apps`/`.app.json` references and **no lifecycle hooks** — either one makes
  the package ineligible for public submission.
- No secrets, demo credentials, `test_credentials` or `reviewer_instructions` in
  the ZIP — reviewer access goes in the secure dashboard form only.
- Server `headers` must be empty on public submission.
- Review requires **exactly 5 positive + 3 negative test cases** and a
  **`demo_recording_url`** under `extensions.com.openai.review` *in the ZIP*
  (dashboard-editing the recording URL is no longer accepted — a missing URL
  blocks Submit with "No video walkthrough URL provided").
- Listing copy must not mention pricing, free trials or promotions.

## Re-building the ZIP after edits

Bump `version` in `plugin.json`, then zip with **forward-slash** entries
(PowerShell `Compress-Archive` writes spec-illegal backslash entries):

```bash
python - <<'EOF'
import zipfile, os
os.chdir("chatgpt-plugin")
with zipfile.ZipFile("../propetl-plugin-<version>.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk("."):
        for f in files:
            p = os.path.join(root, f)
            z.write(p, p.replace(os.sep, "/").lstrip("./"))
EOF
```

## Submission flow (manual, from the founder's PERSONAL OpenAI account)

1. Upload ZIP → automated metadata checks → resolve findings.
2. **MCPs** tab → Connect `propetl` server → pass domain verification by hosting
   the portal's challenge token at
   `https://mcp.propetl.com/.well-known/openai-apps-challenge` (served by
   `src/auth/` from the `OPENAI_APPS_CHALLENGE_TOKEN` Railway env var — set the
   var to the token the portal shows, redeploy, retry).
3. Complete the OAuth connect (consent page = license sign-in / inline trial).
4. Automated tool scan → resolve findings → Rescan.
5. Review details form → reviewer credentials (demo@propetl.com + demo license
   key, no 2FA) — entered in the DASHBOARD, never in the ZIP.
6. Submit for review. Post-approval: MCP server tool changes are re-scanned
   daily and go live without a new ZIP; metadata/skill changes need a new ZIP.

## Local testing

Personal marketplace entry in `~/.agents/plugins/marketplace.json` pointing at a
copy of this folder (`source.path` relative to the marketplace root, `./`-prefixed),
then restart the ChatGPT desktop app and install from the local source.
