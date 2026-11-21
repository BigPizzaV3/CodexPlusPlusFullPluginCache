# Agentic Atlas — companion plugin for Claude Code

[Agentic Atlas](https://agentic-atlas.dev/) is a collection of field-tested
patterns for designing agent systems, readable by people and consultable by
agents over MCP. This companion plugin supplies three skills for the three
design moments — auditing an artifact you have, designing a system you don't
have yet, and applying one pattern you just read — over two strictly
read-only agents. Version `0.8.0` uses the five `atlas_*` tools on the hosted
MCP endpoint (`.mcp.json` → Streamable HTTP at
`https://agentic-atlas.dev/mcp/`). It runs unchanged against the live v6
server Release and the coordinated agent-projection/v7 Release.
The plugin installs no SDK, CLI, local server, or content bundle.

There is no bundled client, downloaded artifact, pinned release, or rollback
path in the plugin. The endpoint serves one active Release, and a promotion
replaces it wholesale. Every response identifies that Release so a
consultation can refuse to cross a promotion silently.

## Security boundary

Artifact contents stay local. The audit agent reads only the local paths the
user selected and treats their contents as untrusted data; embedded
instructions, links, and tool requests cannot expand the audit. The hosted MCP
receives only generic design vocabulary, canonical Atlas ids and addresses,
and required grammar fields such as revisions or cursors — never source code,
file paths, user concerns, secrets, or fetched references. Its responses are
reference data, not code or operational instructions. A full plugin install
stops if one of its local control files is missing. A standalone skills-CLI
install instead runs the self-contained inline method in its local `SKILL.md`;
neither mode downloads replacement instructions.

## Layout

- `plugin.json` — the portable manifest, conforming to
  [Agent Plugins 1.0.0](https://agent-plugins.org/specification).
- `mcp.json` — the portable MCP configuration: one `streamable-http`
  server at the hosted endpoint.
- `LICENSE.md` — the Agentic Atlas source-available license, including the
  companion plugin. The public distribution ships this file unchanged.
- `.claude-plugin/plugin.json` — Claude Code's manifest, stating the same
  identity in its own dialect. `.claude-plugin/icon.svg` packages the site's
  brand mark for the Claude directory listing.
- `.mcp.json` — Claude Code's MCP configuration, registering the same
  hosted public consultation endpoint (which it spells `http`). Claude
  Code connects to an endpoint once, from its highest-precedence
  definition: if you also registered this endpoint yourself at project or
  user scope under another name, the plugin's server is skipped, the two
  agents' `tools:` scope has nothing to bind, and every consultation runs
  through the skills' inline method instead — disclosed, not hidden. The
  skills see it coming: each surface check resolves the name the session
  serves the atlas under and compares it with the agent's `tools:` line,
  so a dispatch that cannot bind is not made. To let the agents bind,
  remove the by-hand registration (`claude mcp remove <name>`, at the
  scope `claude mcp get <name>` reports) and the plugin's own server
  connects in its place.
- `contracts/return-shapes.md` — the one normative statement of every
  skill↔agent seam: the three return shapes, the shared status vocabulary,
  the citation form, the corpus traversal rules, and the uniform
  degradation rules. Skills paste the relevant shape and the traversal
  rules into each dispatch and validate returns against the shape's
  receiver checks; nothing restates a shape anywhere else.
- `skills/reviewing-agent-designs/` — audit an existing skill, agent,
  plugin, or workflow against the patterns; cited, checkable findings.
- `skills/designing-agent-systems/` — inline interview, one consolidated
  corpus consultation, a proposed decomposition with every structural
  choice cited. Also the home of cheap inline lookups.
- `skills/applying-a-pattern/` — verify one named pattern against the live
  Release, get a cited edit plan, execute it in the main context.
- `agents/pattern-librarian.md` — pure corpus traversal
  (ConsultationReturn); serves designing-agent-systems.
- `agents/design-auditor.md` — reads the user's artifact read-only and
  consults the corpus; audit mode (AuditReturn) serves
  reviewing-agent-designs, apply mode (EditPlanReturn) serves
  applying-a-pattern. It never edits.
- `evals/` — behavioral evals for the `claude plugin eval` harness:
  trigger accuracy (positive and negative), return-shape recovery, and
  honest degradation when the Atlas is absent from the parent or from a
  dispatched child only.
  See `evals/README.md` for the tool grants and deliberate gaps.

Harness authors can read the consultation contract as copyable documentation
at [agentic-atlas.dev/consult.md](https://agentic-atlas.dev/consult.md), but
the plugin never uses that remote page as replacement control instructions.

This directory contains only the public companion components. Corpus files,
publisher tooling, a local client, and a fallback server are not part of the
plugin.
