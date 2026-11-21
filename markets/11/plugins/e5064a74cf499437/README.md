# Spline plugin

The package we submit to the ChatGPT/Codex plugin directory, and the source
of the public repository that Cursor and Claude Code install the plugin from:
one skill plus the hosted MCP server (`packages/mcp-remote`, at
`https://mcp.spline.design/mcp`), and for ChatGPT/Codex the authoring guides. How the relay works:
[`packages/mcp-remote/README.md`](../../packages/mcp-remote/README.md).

```
plugin.json                      Agent Plugins manifest; OpenAI listing under extensions.com.openai.interface,
                                 review cases under extensions.com.openai.review
mcp.json                         the hosted server, for ChatGPT and Codex
skills/spline/SKILL.md           the skill for ChatGPT/Codex: the editor opens in the Spline panel
public/skills/spline/SKILL.md    the skill for everyone else (published as skills/): the editor opens from a link
.claude-plugin/plugin.json       Claude Code manifest
.claude-plugin/marketplace.json  makes the public repo its own Claude Code marketplace
.mcp.json                        the hosted server, for Claude Code
.cursor-plugin/plugin.json       Cursor manifest
.cursor-plugin/mcp.json          the hosted server, for Cursor (published as mcp.json)
public/                          the public repo's README.md, LICENSE and skills/
agents/openai.yaml               ChatGPT/Codex interface metadata: the monochrome small icon, as Figma's plugin declares it
assets/                          listing-logo.png (the listing icon), logo.png (the composer icon),
                                 spline-icon-mono-{dark,light}.svg/.png (the monochrome mark, see Icons)
```

Both skills are judgment only: when to use Spline, how to start, the
build–look–refine loop. They name tools but never copy the authoring guides.
Tool mechanics live in the tool descriptions; on any conflict the server wins.
The two differ only in how the editor gets on screen (ChatGPT's panel vs. a
link to the web editor, plus the local bridge's create tools); the export
fails if their names or the build–look–refine section drift apart.

The ChatGPT/Codex package also carries the editors' authoring guides, so
everything that steers the model can be read inside it: the upload script
below adds `skills/spline-3d-use/`, the `3d_run_code` skill laid out like
Figma's figma-use (the authoring contract, the DSL reference and a typed DSL
API, `dsl-api.d.ts`, under references/), one `skills/spline-3d-<name>/` skill
per other 3D guide (OpenAI's scan flagged them bundled as one skill) and
`skills/spline-2d/`, an index plus one `references/<name>.md` per guide, all
generated from the same modules `*_load_skill` serves. They are not committed here: a guide change reaches
`*_load_skill` with the next server deploy, and the package with the next
upload.

Every manifest carries the same `name` and `version`; the export below fails
when they drift, or when the three MCP configs point at different servers.

## Cursor and Claude Code: the public repo

Both install plugins from a public git repository, so
`scripts/export-agent-plugin.mjs` builds one from this folder (a single plugin
at the repo root, readable by both; the ChatGPT/Codex `plugin.json` is left
out) and `.github/workflows/sync-agent-plugin.yml` pushes it on every release
merge to `main`. Pull requests that touch this folder run the export as a
check. Edit here, never in the public repo: the next sync overwrites it.

```bash
node scripts/export-agent-plugin.mjs /tmp/spline-plugin
```

Writes the public repo's contents (without a directory, to a temporary one: a
validation-only run). Check the result with `claude plugin validate
/tmp/spline-plugin`. Users then install with `/plugin marketplace add
<owner>/<repo>` and `/plugin install spline@spline` in Claude Code, or from the
Cursor Marketplace once it's listed there.

## Upload (ChatGPT/Codex)

Build the ZIP and upload it at `https://platform.openai.com/plugins`; that
takes an organization owner or a member with Apps Management Write, in a
verified organization. Build it from the commit the relay is deployed from,
so the bundled guides match what `*_load_skill` serves.

```bash
npm run package-plugin --workspace=@splinetool/mcp-remote
```

Writes `plugins/spline-plugin.zip`: this folder's contents without the other
hosts' files (`.cursor-plugin/`, `public/`, `.claude-plugin/marketplace.json`),
plus the generated guide skills. Add `-- --dir /tmp/spline-plugin` to also keep
the unzipped package for a look.

## Icons

- `logo` (`assets/listing-logo.png`) and `composerIcon` (`assets/logo.png`):
  the colour sphere, for the directory listing and the composer, as every
  published plugin keeps them in colour.
- `assets/spline-icon-mono-{dark,light}.svg`: the monochrome mark, the
  logo's colour zones as opacity steps of one colour. Named for the glyph's
  colour: `-dark` is black, for light backgrounds; `-light` is white, for
  dark ones. The `.png` next to each is the same at 1024 px.
- `agents/openai.yaml`'s `icon_small` (`assets/spline-icon-mono-dark.svg`):
  Figma's plugin declares its single-tone glyph the same way; no
  `plugin.json` field takes one.
- ChatGPT's apps menu draws each app as a single-tone glyph (Canva's shows
  white, although its package ships only colour icons), so that icon looks
  to be set with the app in the portal rather than read from the package:
  upload `assets/spline-icon-mono-dark.png` there, or
  `spline-icon-mono-light.png` where a field wants the dark-mode version.

## Before submission

- The relay's `EDITOR_ORIGIN` set to `https://app.spline.design`, with the
  editor changes deployed there.
- Reviewer access, entered in the dashboard form (the package may not carry
  credentials): a demo account with sample files whose login works without an
  emailed code or other second step.
- `supportURL` points at the MCP docs page until Spline has a support page.
- Optional: `screenshots`, `brandColor`.
