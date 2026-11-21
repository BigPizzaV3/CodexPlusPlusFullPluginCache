# Lifterly plugin for ChatGPT and Codex

The plugin people install from the ChatGPT plugin directory: skills that
guide the model through recognizable training goals, on top of the Lifterly
MCP server (`apps/mcp`, `https://mcp.lifterly.com/mcp`) for live data, writes
and the cards it shows.

Approved by OpenAI and listed since 2026-11-04:
<https://chatgpt.com/plugins/plugin_asdk_app_6ad9d853a2208191a3c9243320a58e1b>
(`CHATGPT_PLUGIN_URL` in `apps/web/src/lib/stores.ts`, which the website links
to).

## Package

An [Agent Plugins](https://agent-plugins.org) package, the format ChatGPT and
Codex share:

| Path | What |
| --- | --- |
| `plugin.json` | Identity, plus `extensions.com.openai`: the directory listing (`interface`), the review cases (`review`) and the release notes and the listing text in French, Spanish, German and Brazilian Portuguese (`publication`) |
| `.app.json` | The same server as registered in ChatGPT (`asdk_app_6ad9bf432344819190c7be247ef34114`, the "Lifterly" custom MCP server of the developer's ChatGPT account), referenced by `extensions.com.openai.apps`. ChatGPT's Work mode runs chats on its servers, which only reach MCP servers registered in ChatGPT: without it a local install gets the skills but no tools. Local and workspace installs only |
| `mcp.json` | The production MCP server, for the submission and for Codex, which starts it on the user's machine. No `auth` block: ChatGPT discovers OAuth from the server's protected-resource metadata (scopes `training:read`, `training:write`) and the API's authorization server (CIMD, with DCR as fallback) |
| `assets/` | `logo.png` (512 px) and `icon.png` (192 px), copies of `apps/web/public/brand/lifterly-{512,192}.png` |
| `skills/` | The skills below, each with `agents/openai.yaml` (its name in ChatGPT and its dependency on the `lifterly` MCP server) |

The listing makes no mention of pricing or Pro: plugins may not promote a
subscription. There is no lifecycle hook either, and the submission ZIP leaves
`.app.json` out: packages with them cannot be submitted.

Validate after a change, against the published schemas
(`https://agent-plugins.org/schemas/1.0.0/{plugin,mcp}.schema.json`) and the
submission limits: `displayName` and `shortDescription` (and each translated
`subtitle`) at most 30 characters, at most three `defaultPrompt`s of 128,
five positive and three negative review cases.

## Skills

| Skill | When |
| --- | --- |
| `plan-training` | Plan the next days, a week, a month or a program (in blocks of up to four weeks), around what is planned |
| `build-workout` | One session, shown as a proposal card, added once the user agrees |
| `review-training-progress` | How training is going: consistency, records, plateaus, next steps |
| `log-past-workout` | Record a workout done without the app |
| `swap-exercise` | Replace an exercise in a planned session, optionally ban it |

Each skill folder stands alone (the importer allows five skills), so
`references/programming.md`, Lifterly's own programming rules (ported from
the coach's planner prompt, `apps/mastra/src/mastra/prompts/planner.ts`), is
copied into the two skills that plan sessions: keep both copies in step.

The website also publishes them for any agent, each folder as a `.tar.gz`
listed in `https://lifterly.com/.well-known/agent-skills/index.json`
(`apps/web/src/lib/agent-skills.ts`): deploy the website after changing a
skill.

## Install it locally

`.agents/plugins/marketplace.json`, at the repository root, lists this folder
as the `lifterly-local` marketplace.

- **ChatGPT desktop app** (Work mode or Codex): restart the app, open the
  Plugins Directory, choose "Lifterly (local)" and install Lifterly; it asks
  to sign in to Lifterly on install. Work mode reaches the tools through the
  server registered in ChatGPT (`.app.json`): an account without that
  registration adds it from chatgpt.com/plugins (**+**, **Add custom MCP
  server**, `https://mcp.lifterly.com/mcp` with OAuth, **Create as a
  plugin**) and puts the `asdk_app_…` part of the page's
  `plugin_asdk_app_…` id in `.app.json`, locally.
- **Codex CLI**:

  ```bash
  codex plugin marketplace add /path/to/lifterly
  codex plugin add lifterly@lifterly-local
  ```

Restart the app after changing the package so the local install picks it up.
To try the staging server, point `mcp.json` at
`https://mcp-staging.lifterly.com/mcp` locally; never commit it.

## Submit it

Zip this folder, its contents at the archive's root and without `.app.json`
and the manifest's `apps` field (`scripts/zip-chatgpt-plugin.mjs`), into
`lifterly-plugin.zip` at the repository root:

```bash
npm run plugin:zip
```

On [Plugins](https://platform.openai.com/plugins), select **Upload new or
existing plugin**, choose the verified developer identity (MissionMind) and
upload the ZIP. The listing, review cases and translations fill in from
`plugin.json`, and the MCP server from `mcp.json`, whose tools the dashboard
scans from the live server. Still to give in the dashboard: the reviewers'
demo account (an email account with training history and no MFA, in the
secure form, never in the package) and the demo recording
(`review.demo_recording_url`, which can also go in `plugin.json` once
recorded).

Changes to the MCP server's tools go live after automated checks, without a
new ZIP; changes to the listing or the skills need one, with a higher
`version` and new `publication.release_notes`.
