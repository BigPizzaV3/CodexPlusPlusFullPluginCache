# VisionBoard plugin

This repo-local plugin connects Codex, ChatGPT Work, Claude Code, and Claude Desktop to the production VisionBoard OAuth MCP server at `https://visionboard.si/api/mcp`.

It bundles the complete provider-neutral VisionBoard working rules and MCP contract: approved Direction and exact reads, governed Notes, Goals, Documents and source files, Brand Kits, Products, Images, Boards, review comments, approval packets, human-authorized Vision creation, provenance, and long-running Goal Runs. The Goal Run protocol extends the existing tools; it does not replace or narrow them.

## One plugin, several hosts

There is one MCP server definition (`.mcp.json`), one skill tree (`skills/`), and one icon. Each host only adds its own metadata file, and every one of those is generated from `plugin.manifest.json`:

| File | Read by | Generated |
|---|---|---|
| `plugin.manifest.json` | nothing — the only file you edit | source |
| `.mcp.json` | every host | shared, hand-maintained |
| `skills/visionboard/` | every host | shared, hand-maintained |
| `.codex-plugin/plugin.json` | Codex, ChatGPT Work | yes |
| `.claude-plugin/plugin.json` | Claude Code, Claude Desktop | yes |
| `/.agents/plugins/marketplace.json` | Codex marketplace (from a checkout) | yes |
| `/.claude-plugin/marketplace.json` | Claude Code marketplace (from a checkout) | yes |
| `/public/plugin/marketplace.json` + `visionboard.zip` | anyone installing from visionboard.si | yes, at build |
| `pyrabit-com/visionboard` (public repo) | anyone installing by name, and the community catalog | yes, via `tools/publish-plugin-repo.mjs` |

Run `npm run plugin:release` after editing the source: it regenerates the host manifests and rebuilds the published archive and its descriptor. `npm run plugin:manifests:check` fails the test suite if a committed manifest was edited directly or left stale, and the release artifacts are rebuilt on every `npm run build`, so no host can drift apart from the others.

## Install

There are three entry points. All three reach the same server, the same OAuth consent, and the same tools; they differ only in how much of the working-rules skill comes with them.

**1. Plugin — Claude Code.**

```bash
claude plugin marketplace add pyrabit-com/visionboard
claude plugin install visionboard@visionboard
```

Three routes reach the same plugin, and all three are generated from this directory: the public repository `pyrabit-com/visionboard`, which the community catalog pins a commit from; `https://visionboard.si/plugin/marketplace.json`, which serves the archive built by `npm run plugin:release` with its hash; and `claude plugin marketplace add ./` from a checkout for development. Run `node tools/publish-plugin-repo.mjs <clone>` to refresh the public repository — never edit it directly.

This is the fullest path: the MCP server *and* the bundled skill, so the model knows when to consult VisionBoard and how to close a strategic loop. Codex installs the same directory through its own marketplace at `.agents/plugins/marketplace.json`.

**2. Connector — claude.ai and Claude Desktop.** In VisionBoard, AI Connectors → pick **Claude** → **Copy and open Claude** puts the address on the clipboard and opens `https://claude.ai/customize/connectors` (Team and Enterprise owners add it once at `https://claude.ai/admin-settings/connectors`, then members press Connect). There, `+` → Add custom connector → paste:

```
https://visionboard.si/api/mcp
```

Claude has no link that pre-fills a connector address, so copying and landing on the exact page is the shortest honest path; the three steps are spelled out on the card rather than left to a help article. The server advertises protected-resource metadata, dynamic client registration, and PKCE, so Claude registers itself and opens the ordinary VisionBoard consent screen. This gives the complete tool contract without the bundled skill; paste the Direction reminder from AI Connectors into the project or custom instructions to get the same recall behavior.

**3. Plain MCP — anything else.** Any MCP-capable client adds the same address as a remote server. AI Connectors carries the same one-action treatment for ChatGPT (which has a settings page but no documented direct link, so the menu path is spelled out) and for Codex (which has no page at all, so it gets a runnable `codex mcp add visionboard --url …` command instead of a link that would not exist). Its `Any other AI tool` disclosure explains the manual path for everything else: paste the address where the tool asks for a remote or custom MCP server, let it sign itself in, and fall back to a developer key only when a tool cannot complete sign-in.

Connector hosts normally call this server from their own infrastructure without an `Origin` header. When one does forward its published browser origin, `MCP_TRUSTED_CLIENT_ORIGINS` in `lib/domain/ai-access/mcp-transport.mjs` keeps the connection working; every other cross-origin caller is still refused.

## What the connection does

Hosts that render a native conversation workspace also receive a compact card for Direction, Goals, the exact Library inventory, Board previews, and durable Goal work. This is not a second VisionBoard frontend or a shadow copy of its data: the card holds identifiers only and reads or acts through the same OAuth scopes, canonical tools, revisions, coverage manifest, and human decision boundaries as the web product. `Open full view` is progressive disclosure for spatial editing and dense administration, not a mandatory extra step for routine work.

Hosts that render tool results as text, such as coding agents, lose no capability. The skill carries the same single outcome in a written summary with the exact identifiers, state, and scoped VisionBoard link, and it reads the connected tool list rather than assuming which kind of host it is running in.

The plugin deliberately closes strategically relevant work with one clear moment, not a stream of cards: a quiet current-Direction check after comparing the conversation with approved truth, one exact Approval Bundle when a Review is ready, one focused Goal Run question, or an explicit **not saved** disclosure when a strategic update still needs to be recorded. Saved changes identify the object and distinguish additions from edits. These paths are mutually exclusive for the same work result, so the user never has to approve the same thing twice.

At project-task start, the skill checks a saved project/Vision association or searches the permitted Vision directory with pagination. Ambiguous matches require a person to choose; no matching accessible Vision leads to a creation proposal, never automatic creation. A user-authorized `.visionboard/project.json` or host project instruction stores identifiers only, not credentials or copied strategy. The skill reads that file directly and stops at the repository root, so it never inherits another project's association. See [project continuity](./skills/visionboard/references/project-continuity.md).

Repository changes do not update installed plugin caches or other worktrees automatically. Release the matching MCP server before distributing this candidate, then verify a fresh task with the updated plugin in each host you support. Older servers lack the `update_needed` card and paginated directory; the skill must disclose that limitation rather than claim the Vision is missing or synchronized.

Installation makes VisionBoard available to supported tasks and gives the model clear rules for when strategic work should consult it. It does not send every prompt to VisionBoard and it does not keep a model running in the background. A recurring scheduled task supplies wake-ups for a human-activated Goal Run; each wake performs one bounded cycle and exits.

VisionBoard's cloud state does not depend on an open browser tab. The browser is
only a human control and review surface. Local agents still need the local
computer and its scheduled-task host to be available; cloud-hosted work can
wake remotely. A missed local wake remains safely waiting in VisionBoard and
continues from the durable run version when the host returns.

Installation grants nothing by itself. The first real use opens VisionBoard's OAuth consent, where a person chooses exact capabilities and Vision access. Existing grants never gain new permissions silently, and approval, Vision creation, Goal activation, and Goal completion retain their human decision boundaries.

The plugin is validation-ready for local and team testing. The repository root
contains a review-facing ChatGPT App submission candidate generated from the
actual public tool inventory. Publishing to any host directory remains a
separate product-release action: first deploy and verify the hardened source,
configure the portal-provided domain challenge token, supply dedicated reviewer
credentials, run the live tool scan, and obtain explicit owner confirmation
immediately before submitting for review.
