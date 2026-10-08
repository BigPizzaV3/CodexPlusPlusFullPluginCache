# E-Worker WebMCP plugin

E-Worker is a skills-only plugin for the universal ChatGPT and Codex Plugins Directory. It contains
workflow instructions and brand assets, but no MCP server, registered MCP application, local broker,
background service, credentials, or server-side AI transport.

The plugin opens one of the five focused E-Worker editors in the built-in browser:

- Documents: `https://eworker.ca/apps/documents/`
- Workbook: `https://eworker.ca/apps/workbooks/`
- Slides: `https://eworker.ca/apps/slides/`
- Notes: `https://eworker.ca/apps/notes/`
- Project Plan: `https://eworker.ca/apps/project-plan/`

Public support is available at `https://eworker.ca/support/`.

Each live page registers its own bounded semantic tools through `document.modelContext`. ChatGPT Work
or Codex discovers only the tools belonging to that page and executes them in the user's visible,
signed-in editor session. The handlers reuse the editor's existing owners, permissions, preview,
approval, history, recovery, and save behavior.

Complete new-artifact workflows open a fresh editor page with the exact
`#eworker-webmcp-compose` fragment. The App Host treats that fragment only as a startup policy: it
defers recovery restore and stale cloud-result handoff in the composition page while retaining every
recovery snapshot for a later normal launch. Existing-artifact workflows and ordinary user launches
do not use the fragment and retain normal recovery behavior. The fragment is not authorization and
does not contain a secret.

## Calling E-Worker

In Codex, invoke the bundled workflow with `$eworker`. ChatGPT uses `@eworker` for explicit skill
invocation. Matching plain-language requests may also activate the skill.

```text
$eworker create an image-led product presentation in E-Worker Slides.
$eworker build a monthly operating budget in E-Worker Workbook.
$eworker revise the introduction in the open E-Worker document.
```

The workflow requires the built-in browser and WebMCP site-tool support. It does not fall back to an
MCP connection, shell, raw filesystem access, or mouse/keyboard editing when site tools are absent.

The public plugin uses only the production `https://eworker.ca` origin. It does not open or use
E-Worker page tools from any other origin.

## Build and verify

From the repository root:

```text
npm run build:e-worker-plugin
npm run verify:e-worker-plugin
```

The local marketplace distributable is emitted to `Build/E-Worker-Plugin/eworker`. Reviewer-ready
submission materials are emitted to `Build/E-Worker-Plugin/OpenAI-Submission`, including the
uploadable `eworker-plugin.zip`, listing copy, reviewer tests, logo, and checksums. The ZIP contains
the complete skills-only plugin root, including `.codex-plugin/plugin.json` and
`skills/eworker/SKILL.md`.
