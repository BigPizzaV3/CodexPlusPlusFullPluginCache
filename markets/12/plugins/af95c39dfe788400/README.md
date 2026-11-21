# VibeDoctor plugin

The listing package for the ChatGPT/Codex plugin directory and the Claude Code plugin. Both point at the signed-in MCP endpoint `https://agent.vibedoctor.io/mcp` (engine `src/agent/`).

| File | Used by |
|---|---|
| `plugin.json`, `mcp.json` | OpenAI (Agent Plugins format, settings under `extensions.com.openai`) |
| `.claude-plugin/plugin.json`, `.mcp.json` | Claude Code |
| `skills/`, `assets/` | Both |

## OpenAI ZIP

Only the OpenAI files go in the ZIP:

```powershell
Compress-Archive -Path plugin.json, mcp.json, skills, assets -DestinationPath vibedoctor-openai.zip -Force
```

Before uploading at platform.openai.com/plugins:

- Add `review.demo_recording_url` (a reachable video of the sign-in and the five positive test cases).
- Set `developerName` to the verified individual or business name.
- Enter the reviewer account's email and password in Review details, never in the ZIP.
- Bump `version` for every resubmission.

## Checks

```bash
claude plugin validate ./vibedoctor-plugin --strict
```
