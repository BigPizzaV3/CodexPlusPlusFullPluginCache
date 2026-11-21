---
name: supersimple-apps
description: Build and publish Supersimple Apps inside explorations. Use for custom app blocks, visualizations and widgets, the Supersimple SDK, or supersimple app commands.
metadata:
  minimum-cli-version: "2.27.0"
---

# Supersimple Apps

A Supersimple App is client-side web code (usually a single HTML file) published into a
Supersimple workspace. It renders inside a sandboxed iframe as a "Custom app" block in explorations,
and accesses data through the **Supersimple SDK**, exposed as the global `sup` object.
The SDK uses the viewer's Supersimple session and permissions. Semantic-layer queries
apply the models' row-level access rules; raw SQL runs directly against warehouse tables.

The [Supersimple MCP server](https://docs.supersimple.io/integrations/mcp-server) lets your
coding agent inspect live explorations and App source. Use an existing MCP connection when available;
otherwise add `https://app.supersimple.io/mcp` to your coding
agent's MCP connections and authenticate. Use streamable HTTP and OAuth; see the guide for
client setup and API-token authentication. This connection is optional for CLI-based app
development, but required for the MCP workflows below.

## Before building

CLI steps require terminal access and separate CLI authentication; otherwise use available MCP tools or prepare files for the user to apply.

CLI authentication, the coding agent's Supersimple MCP connection, and the browser viewer's
session are separate. Confirm they point to the intended workspace; their permissions can differ.
If CLI credentials are missing, have the user run `supersimple login` with a token from
**Settings → Developers**, or use an existing `SUPERSIMPLE_TOKEN`. Never put that token in App code.

For an existing App, use its local source project if available. Otherwise read its source and
manifest with MCP `get_app` before editing; pass the block's `pinnedVersionId` as `versionId`
when present. Preserve its backend declarations and state keys. Decide whether the user wants
a change to this block or a published update affecting other blocks before publishing.

Choose the data path:

- Existing exploration output: use `sup.exploration.fetchBlock` and subscribe to invalidations.
- New analysis: inspect model fields and metrics, then use `sup.query`; do not invent model IDs
  or replace live data with hardcoded samples unless the user asks for a mockup.
- Raw warehouse SQL: read [raw SQL](references/raw-sql.md) for its permission and model-rule differences.
- External persistence or actions: read [connected backends](references/connected-backends.md).
  They require workspace registration and backend-side authorization, not just an SDK call.

## Workflow

```bash
supersimple app create my-app     # scaffold my-app/ (app.yaml + index.html)
cd my-app
supersimple app publish           # publish/update in the workspace (versions append)
```

Require CLI ≥2.27.0 (`supersimple --version`). Check `supersimple status` output, including the
account and host; it always exits 0, even on failure. `SUPERSIMPLE_HOST` optionally overrides
the API host. The account comes from the token.
Use `supersimple app <command> --help` for command options. If the CLI is missing, see
https://docs.supersimple.io/guides/managing-the-data-model/using-the-cli.

If product behavior differs from this skill, compare `supersimple --version` with the latest
released CLI and check for skill updates using the
[skill installation guide](https://docs.supersimple.io/guides/ai-coding-agents#installation).
The minimum CLI version above is not a freshness check. Update the complete skill folder,
including its references, preserving local edits, then retry the affected step. If the mismatch
remains, report the observed behavior rather than assuming the skill is correct.

CLI 2.27.0–2.27.1 scaffolds an `AGENTS.md` pointing to an older, CLI-embedded skill.
`supersimple app skill --install` in those versions overwrites this guide with that older copy;
update this separately installed skill through the installer you used to obtain it instead.

**The dev loop is publish + reload the page** in a test exploration, exercising the actual sandbox, CSP,
and upstream inputs. New apps are personal: only their author sees them in the picker, but other
viewers can use them through shared explorations after consent. `supersimple app promote <name>`
adds an app to the team library; `demote` removes it. These actions need the corresponding workspace
permissions (**Manage Apps** for publish/delete/promote/demote).

Choose a distinctive, namespaced manifest name. `supersimple app list` shows only team apps and
your own personal apps, so it cannot rule out name collisions. Publishing the same name
updates the existing app (including a team app or another author's app) and can restore a soft-deleted
one. Use a distinct name when developing a separate app. `publish --dir <directory>` selects the app
folder without changing directories. `supersimple app delete <name>` deletes an app; use only when
removal is explicitly requested.

MCP `draft_app` creates a source-only draft of an **existing** App; it cannot create a new App or
change its manifest. It returns an `appVersionId` but does not edit an exploration or attach the
draft to a block. Use it only with a workflow that can set the target block's `appVersionId`
(`app_version_id` in exploration YAML). Until then, the block still runs its previous version.

## app.yaml

```yaml
app:
  name: my-app        # unique per workspace; stable identifier (users see the title)
  title: My app       # human-readable; used as the default block title
  description: >-     # one line describing what the app does
    Ranks accounts by expansion potential.
  entry: index.html   # published as-is; keep the app self-contained in this one file
  tags: [ops]         # optional; the first one shows as a chip in the picker
```

The CLI validates the manifest when publishing; unknown keys are rejected.

## Supersimple SDK

Available through the global `sup` object only inside a Supersimple App iframe; no SDK import
is required. All methods are async. The examples below are API fragments, not a complete app.

```js
const ctx = await sup.context();     // { user: {id, email}, account: {id}, app: {id} }
const theme = await sup.theme();     // viewer appearance tokens, e.g. theme.brandMain, theme.textDefault, theme.background

// Query the semantic layer as the viewer. `pipeline` is an ARRAY of operations with
// camelCase parameter keys, not an exported YAML pipeline object. Empty array = base rows.
const result = await sup.query({
  baseModelId: '<model id>',
  pipeline: [],
  sort: [{ key: 'created_at', direction: 'DESC' }], // engine-side ordering — what a sortable header means
  first: 500,
});
// result: { rows: object[], fields: [{key, type, name}], hasMore: boolean, endCursor?: string }
// Grouped rows nest values under $children; see "Named metrics and grouped results" below.
// Page with the cursor: pass endCursor as `after` on the next call, keeping baseModelId,
// pipeline, sort, and variables identical between pages. Default page size: 100; max: 10,000.
// Aggregation property is an object, e.g. {type: "sum", key: "amount",
// property: {key: "total", name: "Total"}}. deriveField uses `fieldName`:
// { operation: 'deriveField', parameters: { key: 'year', fieldName: 'Year',
//   value: { expression: 'year(created_at)', version: '1' } } }

// Data-producing blocks in the surrounding exploration.
const blocks = await sup.exploration.getBlocks();
// [{ blockId, title, kind, properties: [{key, type, name}], aggregated }] — runs no queries.
// Match the columns this App needs. This chart example needs a numeric output.
// Aggregated blocks are valid chart inputs; exclude them only when you need per-record rows.
const usable = blocks.filter((b) => b.properties.some((p) => p.type === 'Number'));

// Fetch a block's output table. Use the user-requested block or a saved selection;
// auto-select only when exactly one block fits. Store block IDs, not titles or array indexes.
if (usable.length === 0) {
  // Show a setup message rather than dereferencing a missing block.
} else if (usable.length > 1) {
  // Show an input picker unless the requested/saved block already resolves.
} else {
  const upstream = await sup.exploration.fetchBlock(usable[0].blockId);
  // { rows, fields, hasMore }; hasMore means truncated, not a complete dataset.
}
const block = await sup.exploration.getBlock('known-block-id'); // metadata or null

// In the finished app, register this once before the initial fetch, then refetch on changes.
// Upstream changes do not reload the iframe.
await sup.exploration.onBlockInvalidated(({ blockId }) => {   // a fetched block changed underneath you
  if (blockId === myBlockId) refetchAndRender();        // (steps edited, or a variable feeding it moved)
});
await sup.exploration.onBlocksChange((blocks) => rebuildPicker(blocks));  // list changed: add/remove/rename

// Exploration variables: read, write (drives native blocks too), subscribe.
const vars = await sup.variables.get();
const declared = await sup.variables.list();            // [{ key, kind }] — find e.g. kind 'date_range'
// From a user action: await sup.variables.set('segment', 'enterprise');
await sup.variables.onChange((next) => render(next));
// Better than reading a variable's value: reference it in your pipeline and the engine
// resolves it exactly like a native filter (dynamic presets and timezone included):
//   { operation: 'filter', parameters: { key: 'created_at', operator: '==',
//     value: { expression: 'variable("range")', version: '1' } } }

// Persisted app state: part of the exploration's state, so it survives reload, travels in a
// shared link, and browser-back steps over it like any other exploration change.
const state = await sup.state.get();
await sup.state.onChange((next) => applyState(next));         // undo/redo, links, echoes of own writes
// From a user action: await sup.state.set({ x: 'mrr' });
```

Do not pass `variables` to `sup.query`: that array (`[{type,key,value}]`) replaces exploration
variables. Reference `variable("range")` in the pipeline instead.

Discover model IDs with `supersimple models list` and inspect fields with
`supersimple export --model-ids <id> --stdout` outside the sandbox. Prefer
`sup.exploration.fetchBlock(...)` over ad-hoc `sup.query` when the app is meant
to sit downstream of no-code steps — it keeps the data prep auditable. `fetchBlock` consumes the
block's output, which can be aggregated; it does not accept cursor/pagination parameters. Handle
`hasMore` as truncation and ask for a narrower upstream query when completeness matters. Subscribe
to invalidations to make the app reactive. For a direct `sup.query` that uses variables, subscribe
to variable changes and rerun it. Guard against older async responses overwriting newer results.

### Named metrics and grouped results

SDK parameter names use camelCase: a named-metric aggregation uses `metricId`.
CLI YAML uses `metric_id`. Keep user-defined field keys exactly as declared on the model.

```js
const revenueBySegment = await sup.query({
  baseModelId: '<model id>',
  pipeline: [{
    operation: 'groupAggregate',
    parameters: {
      groups: [{ key: 'segment' }],
      aggregations: [{
        type: 'metric',
        metricId: '<named metric id>',
        property: { key: 'revenue', name: 'Revenue' },
      }],
    },
  }],
  first: 100,
});
```

`sup.query` preserves the API's grouped row structure. Each grouping dimension adds a level:
its value is on the parent, and `$children` contains the next level or the aggregate values.
`$leaves` counts leaf result rows under that parent in the returned page, not source records
or a metric total. For example, `revenueBySegment.rows` can be:

```js
[
  { segment: 'enterprise', $leaves: 1, $children: [{ revenue: 12500 }] },
  { segment: 'self-serve', $leaves: 1, $children: [{ revenue: 800 }] },
]
```

Flatten recursively for a chart or table, carrying parent dimensions into every leaf:

```js
function flattenRows(rows, parent = {}) {
  return rows.flatMap(({ $children, $leaves, ...values }) => {
    const row = { ...parent, ...values };
    return Array.isArray($children) ? flattenRows($children, row) : [row];
  });
}
const revenueRows = flattenRows(revenueBySegment.rows);
// [{ segment: 'enterprise', revenue: 12500 }, { segment: 'self-serve', revenue: 800 }]
```

This handles multiple grouping dimensions and flat rows. Flatten each fetched page and append
its leaves; a group may span pages. Use `hasMore` and `endCursor` to determine completeness.
`sup.exploration.fetchBlock(...)` already flattens grouped output and returns flat rows.

Check the actual response before mapping it into a chart. A missing aggregate key is a shape
error; do not turn it into zero with `row.revenue ?? 0`. Preserve genuine zero and null values
and verify a known nonzero result against the source exploration.

## Appearance and charts

The iframe does **not** inherit the host's stylesheet or CSS variables. `sup.theme()` returns
color values; apply them to your own styles and chart-library options. It does not render charts,
legends, or a color picker. Do not assume additional SDK helpers exist.

```js
const theme = await sup.theme();
for (const [key, value] of Object.entries(theme)) {
  document.documentElement.style.setProperty(`--app-${key}`, value);
}
```

Use those locally defined variables, for example `color: var(--app-textDefault)` and
`background: var(--app-surface2)` on a chart panel, `textMuted` for secondary labels, `border`
for boundaries, and `surface1` for tooltips. Set body margins, font, and form-control colors
explicitly; browser defaults do not follow the viewer's Supersimple appearance. Theme changes
reload the iframe, so apply tokens again on startup. Test the exploration URL with
`?theme=light` and `?theme=dark`, regardless of the operating system's theme.

Unless the user asks otherwise, chart Apps should follow these product conventions:

- Use a compact chart panel and avoid repeating the host block's title inside it.
- Put a wrapping legend below the plot. Keep category colors stable across filtering and sorting;
  the native categorical sequence starts with `blue40`, `purple40`, `teal40`, `red40`, `orange40`,
  `green40` from `sup.theme()`. Use the same colors in marks, legend, and tooltips.
- Keep totals outside a pie, or inside a sufficiently large donut hole; never overlay them on
  colored slices. Format units and precision for readability, with exact values in tooltips.
- Give the plot a bounded height and responsive width; reserve space for labels and the legend.
  Check narrow blocks and long labels, not just a full-width view.

## Runtime constraints

- **Size to content, never to viewport.** The sandbox reports its content height and the block hugs
  it. Use intrinsic heights; avoid `100vh`/`100dvh` (causes sizing feedback). Users can also switch
  the block to "Fill available space". Natural height is clamped to 120–1600 px.
- **console.log works.** Sandbox console output and uncaught errors appear on the page's own
  console prefixed `[app:<app title>]` — use it to debug instead of guessing.
- **No secrets in app code.** Everything in the bundle is visible to every viewer. There is no
  server side. Use public/publishable keys and the viewer token from `sup.auth.getToken`
  for declared backends. Never use backend service-role credentials.
- **Dependencies:** import ESM from esm.sh (e.g. `import * as d3 from 'https://esm.sh/d3@7'`),
  or bundle locally into a self-contained HTML document. The CLI uploads only `entry` as text;
  it does not build code, upload sibling files, or wrap a bare JavaScript bundle in HTML.
  Pin tested dependency versions for reproducibility. `esm.sh` is permitted for scripts,
  not arbitrary fetches; other network calls need a declared, registered backend.
- **Sandbox:** scripts only; no localStorage/cookies, popups or new-tab links, form submissions,
  alert/confirm dialogs, remote images, or eval. Images must use `data:` or `blob:`. WASM is allowed.
  esm.sh is not allowed for stylesheets.
- **Versioning:** every publish appends a numbered version. Unpinned blocks follow the published
  version after a full page reload; the block menu’s "Reload app" only remounts the cached bundle.
  Blocks with `app_version_id` keep their pinned version.

## State: reproduce the user's view

`sup.state` stores this block's view configuration in the exploration, not private per-user
preferences. Restore meaningful choices on reload, shared links, and back/forward navigation.

| What the value represents | Where it belongs |
| --- | --- |
| Selected input block, metric, chart type, grouping, sort, or App-specific filter | `sup.state` |
| Selected record, tab, or drill-down that defines the view a shared link should open | `sup.state`; store stable IDs or keys |
| A parameter that should also drive native exploration blocks | `sup.variables`; use the existing variable definition |
| Hover, tooltip, loading/error status, request bookkeeping, or input the user has not applied | App memory |
| Fetched rows or values calculated from the data and current choices | App memory; refetch or recompute as needed |

Read saved state on startup and subscribe once to `sup.state.onChange`. Treat incoming state as
an instruction to restore the view, including undo/redo and returning to an earlier selection.
Use exploration variables directly when they own a setting; duplicating them in `sup.state`
creates competing values.

Write small patches from deliberate user interactions. A completed selection, applied filter,
or finished drag is a useful history step; keep in-progress typing and dragging local until
committed. Group related choices into one patch so undo restores a coherent view. Skip writes
when the persisted values are already the same.

Defaults and fallbacks are computed at render time. An empty saved state must render a useful
initial view without writing it back. If a saved block or column disappears, show a fallback or
setup message and preserve the saved choice until the user chooses a replacement. Rendering,
fetch completion, and `onChange` handlers must not save derived or repaired state. A Reset action
can explicitly save the default choices because the user requested it.

`set` shallow-merges a patch, replacing whole nested values; send the complete nested value you
intend to retain. The host coalesces writes over roughly 400 ms and caps serialized state at
8,192 characters. Store compact choices rather than data or whole block definitions. Catch
rejected `sup.state.set` promises and show the save error: the SDK updates its local state and
fires `onChange` before the host accepts the write. A fulfilled call acknowledges the host request;
the exploration update follows the host's debounce. Subscriptions have no unsubscribe handle.

## Debug data with Supersimple MCP

When an App's numbers disagree with an existing exploration, use the **Supersimple MCP server's**
tools below. If no Supersimple MCP connection is configured, ask the user to connect and authenticate it
using the setup guide above; installing this skill alone does not provide these tools.

1. `get_exploration` locates the App and its input blocks. `get_exploration_block` returns each
   block's definition and complete `dereferencedPipeline`; for an App block it also identifies
   the mounted App and persisted state. Use `get_app` to inspect its source, passing `versionId`
   for a pinned version.
2. `get_exploration_block_data` runs the source data block. Pass matching variable values in
   `params` (otherwise defaults apply), and use `limit`/`offset` for a small comparison sample.
   Match the account and user permissions as well as filters and date range.
3. Compare a known nonzero value with the App's result. A wrong source result points toward the
   model, pipeline, or inputs; a correct source result narrows the investigation to the App's
   query, result handling, or rendering.

MCP returns a formatted table for an existing data block. Inspect the actual `sup.query`
response in the running App to debug JavaScript, `$children` nesting, or a new SDK query.
Exploration reads require `data:read`; `get_app` requires `apps:read`; drafting and publishing
require `apps:write`. Publishing also needs **Manage Apps**. If a connection exists but a tool
is missing, check its granted scopes and user role before asking the user to reconnect.

## Review and verify

Test in the running Supersimple exploration. Local HTML preview and a successful publish do not
validate the `sup` bridge or sandbox. Exercise the interactions the App actually supports:

- Change an upstream filter or variable and verify a specific expected value, not just a redraw.
- Change an input or other saved choice; reload or reopen the link, then use back/undo and
  forward/redo. The controls and result must agree. Loading or restoring state must not add history.
- Check empty, error, and truncated results; light/dark appearance; and narrow block sizing.
  Inspect the parent console for `[app:<app title>]` errors.

## Using the published app

In any exploration: **Templates → Custom app** inserts a block; pick the app in the right sidebar
("Custom app" section). The sidebar has the app picker, "Fill available space", and "Show block
title". The block title defaults to the app title; reactivity is implemented with subscriptions.
