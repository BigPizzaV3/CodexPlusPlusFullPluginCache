# Planit Teachers plugin

Package version **1.4.0** adds the public-plugin privacy boundary. This is an
adult-facing integration using anonymous or synthetic teaching inputs only.
Never transmit personal information about children under 13 to OpenAI. Pupil
names/ids, rosters, photographs, scripts, individual answers/results and named
seat assignments stay outside this integration. Give the exact native link
for the adult to complete sensitive steps independently; never open, capture
or read those private records back through a browser or another connector.
Prior 1.3.1 dashboard checks do not approve these changed 1.4.0 contracts.

An installable plugin for teachers using Planit's classroom tools and existing
Planit accounts. It includes five skills, portable and Codex manifests, brand
assets, and a remote MCP connection at:

`https://planitteachers.ai/mcp/teachers`

The app and API host the endpoint; the ZIP carries the skills and connection
settings. Package creation, private connection, review submission and directory
publication are separate steps. Current release evidence is maintained in
`docs/planit-teachers-plugin/verification.md` in the source repository.

## What teachers can do

| Workflow | Support |
| --- | --- |
| Every registered classroom tool | Live catalogue, exact URL, formats, presets, instructions and FAQs; direct pure generators plus native interactive tools |
| Printable-tool settings | Real controls/defaults/seeds; preview and account-only PDF/CSV export |
| Connected preparation | Guided vocabulary and maths packs, printing estimates and mounted pupil-work layouts; numeric results and explicit unit mappings |
| Teaching knowledge and FAQs | Entire published collection index, source Markdown, paginated LLM documents and existing specialist searches |
| Lessons | Quote, create, poll, read, AI edit, generate another output, export |
| Worksheets and homework | Anonymous teaching content: quote, create, list, read, AI edit and PDF export; known child-personalised worksheets require adult native handoff |
| Saved classroom tools | Save, read, update and duplicate; exact reopening URL and seed preservation |
| Classes | Owned class-level metadata/counts and requested metadata changes; pupil names/ids and roster inputs are excluded |
| Class seating | Deterministic simple layouts from an owned class internally; summaries omit pupil identities and desk assignments; named inspection/changes/exports are an independent adult native workflow |
| Worksheet header settings | Read and update requested text/position while preserving other fields, existing logo, watermark and native access rules |
| School workspace | Active membership, colleague/shared-library/activity summaries and owner-only requested name/colour changes; native authorisation and private-content boundaries |
| Learning walls, lettering, bunting and decorations | Owned packs and published examples; quoted/confirmed create, choose, build, direct manifest edits, clone, retry and guarded PDF/ZIP exports |
| Marking summaries and generic schemes | Owned session-level progress and aggregate numeric analysis; checked generic schemes and requested settings; no raw answers, individual results or pupil-specific corrections |
| Marking capture and exports | Adult handoff to private native capture/upload, scan inspection, individual results, closing and exports; no agent browser readback |
| Units | Save teacher-approved 2–12-lesson outlines, read actual progress and manage owned lesson/resource links; no hidden outline/brief AI fallback |
| Display photos and natural-language redesign | Adult native-editor handoff where no individually exposed operation is available; private pupil content is never read back |
| Account access | Existing account, live credit balance, native quotes, allowance refresh and feature/download guards |

All classroom tools can be discovered and used through their native controls.
The plugin distinguishes this from direct remote execution. It never claims
that browsing a catalogue or saving a snapshot has rendered a file.

## Access and directory rules

Browsing public resources and building classroom tools are free. Saving needs
a Planit account. AI creation/editing uses the connected account's existing
credits and feature entitlements. Free tool download/print/copy requires a
linked FREE account only, with no upgrade or upsell. Other resource downloads
retain their existing access rules. The API and browser enforce the same rule.

This is the public-directory version selected for this project. It does not
promote upgrades, display subscription offers, sell digital tokens/credits,
initiate subscriptions or link checkout pages. Native access errors are
reported as restrictions, with any allowance refresh information. Existing
paid accounts can use included features. ChatGPT access and Planit access are
separate.

The isolated endpoint filters `start_subscription` from both discovery and
calls. The API rejects that operation for tokens issued to the plugin's
resource, even if a client requests billing permission. The older `/mcp`
integration remains a separate surface. OAuth uses PKCE, scoped consent and
short-lived delegated REST tokens; client tokens are never passed through.
CIMD negotiates the mutually supported public method from ChatGPT's advertised
capabilities. Private-key-only clients and unsupported client assertions are
rejected; DCR remains available.

Both `mcp.json` and `.mcp.json` explicitly declare server-level
`extensions["com.openai"].auth` as `mixed`, with `client.mode:dcr` and the exact
resource `https://planitteachers.ai/mcp/teachers`. Public tools stay anonymous;
protected operations request their disclosed scopes through OAuth. The empty
`defaultScopes` array avoids importing a broad connection-wide scope default;
per-tool step-up and the native minimal read-only fallback remain authoritative.
The package contains no client id, client secret, bearer token or endpoint
copies. Resource metadata discovers the shared Planit issuer and its current
authorization, token and registration endpoints. The packaged connection
selects DCR; server-side CIMD support remains available to other clients.

## Install and package

The repository marketplace is `.agents/plugins/marketplace.json`. Refresh the
local marketplace in Codex, find **Planit Teachers**, and install it for local
testing. The portable root manifest also works with hosts supporting Agent
Plugins. The compatibility manifest remains available for Codex.

Run from the repository root:

```sh
python3 scripts/build-planit-plugin.py --check
python3 scripts/build-planit-plugin.py
python3 -m unittest discover -s plugins/planit-teachers/scripts -p test_plugin_mcp_auth.py
python3 plugins/planit-teachers/scripts/plugin_mcp_auth.py --live-discovery
```

The second command creates `dist/planit-teachers-plugin.zip`. It contains the
manifest, MCP configuration, skills and assets at the ZIP root. The reference
archive is development evidence and is excluded from the distributable ZIP.

Package builders also reject missing auth, incompatible portable/Codex
settings, incorrect resource audiences, bundled credentials and broad scope
defaults. OpenAI documents the server auth extension in
[Package your plugin](https://developers.openai.com/plugins/build/plugins#configure-mcp-authentication).
The currently published Agent Plugins base schema forbids server extensions,
so it rejects even that documented field. Base transport validation therefore
checks a projection without the known vendor extension; the OpenAI auth shape
is checked separately against the documented contract. This discrepancy is
recorded as a limitation rather than a full base-schema pass.

The earlier-release narrated production walkthrough is available at
[the review player](https://planitteachers.ai/plugin-review/walkthrough), with
captions and a transcript. It shows genuine MCP Inspector and native editor
screens, not a ChatGPT conversation. It does not establish the v1.4.0 privacy
contracts. A new film requires fresh post-deployment production captures and
acceptance evidence; it has not been recorded or rendered for this revision.

## Connect and submit

1. Deploy the frontend and backend changes using the project's normal release
   workflow. Verify `/mcp/teachers`, the individual operation definitions and
   its OAuth metadata in production. Check that retired generic executors are
   absent and refused, then run the public acceptance script against production.
2. In ChatGPT developer mode, register that HTTPS MCP endpoint, using Planit's
   OAuth flow. This is a remote endpoint; no local server, pasted secret or
   browser cookie export is needed.
3. Test a real free account and a real paid account, including an exhausted
   credit balance and a denied export. Use sample teaching data and no real
   pupil records for review.
4. Refresh and scan the MCP definitions in the existing draft. Each native
   printable exposes separate detail, preview and export operations with a
   fixed tool binding, closed schema, description and annotations. Confirm that
   these definitions are visible before submitting the remote endpoint through
   **With MCP** in OpenAI's plugin
   submission flow and upload the bundled skills/package as supported. The
   registered technical app id and publisher verification are provided by
   OpenAI during that process; this repository does not invent them.
5. Provide accurate contact/privacy/terms details, an authorised demo account
   with sample resources, and review evidence. Publish only after review and
   approval. A local marketplace entry is not a public listing.

## Source snapshot and freshness

Runtime catalogue and knowledge reads use the application's existing
registries and Markdown renderers. Published pages, FAQs and source resources
can grow as data without adding executable operations. Static App Router pages are indexed during
ordinary Next builds; published data collections use live family reads. Public
Markdown reading uses the site's shared public-page rules, including future
page roots. A tool added to a pure generator registry receives separate
model-callable detail, preview and export definitions in the server release.
Deploy, refresh, scan and submit those new or changed operation definitions
for review before directory use. A catalogue read cannot add a hidden builder.
New interactive
tools automatically appear with their native URL, settings, formats and FAQs.
Content-only catalogue updates do not need a plugin ZIP update. Changed skills
or MCP operation definitions require the corresponding package/connection
refresh and review. `reference-snapshot/` holds a historical development
snapshot of the full tool catalogue and LLM documents, plus the knowledge page
index and any degraded collections at export time.

`reference-snapshot/classroom-tools.json` is local generated-contract metadata,
with its timestamp, exact source path and SHA-256, explicitly marked as a
working-tree snapshot rather than a production capture. It omits live FAQs,
starting snapshots, account access and workflow state. Older knowledge-index
and LLM documents remain historical evidence with their original provenance;
the runtime package excludes the whole reference directory. Runtime sources
and failures must be checked through the connected server.

The checked source contracts contain 336 individually described
native tools: 236 have deterministic previews, 234 also have PDF/CSV export
operations, and 100 use native editors for execution. The two preview-only
interactive worksheet tools retain their native output controls. These are
checked source counts for this candidate, not evidence of live deployment;
runtime discovery reads the deployed registries and sources. Absence/consent
letters, social stories and token boards remain discoverable with exact native
links, but their pupil-specific execution stays in the adult native editor.
Anonymous books, blank interactive worksheets and teacher-authored crosswords
remain supported; the public author, private-asset and solving-progress fields
are empty-only.

Run `python3 plugins/planit-teachers/scripts/validate-operation-snapshots.py`
to detect stale local contract metadata and incorrect per-slug operation
bindings for both brands. Its `--refresh` option regenerates only that local
metadata; `--archive dist/planit-teachers-plugin.zip` additionally verifies
that snapshots and development scripts are excluded from the distributable.
This does not deploy, register or approve operations.

Version 1.2 adds ranked question search over authored help answers and tool FAQs,
retaining page titles and source URLs. Catalogues include guided recipes under
`projectWorkflows`; these describe calls to existing operations and do not run
jobs themselves. Each prepared practical utility returns exact numeric result
rows alongside its printable preview. Recipes resolve current tool settings at
runtime. New mathematical connections need a checked recipe; they are not
inferred automatically from newly added tools.

Guide corpus files enumerate the native publication index rather than the first
browsing page. Reads have bounded concurrency, work and memory. Every constrained
or failed read reports partial status and directs the assistant to individual
published pages. The full searchable guide index remains available separately.
The limits and local verification for this version are recorded in
`docs/plugin-useful-workflows/verification.md`. The older walkthrough demonstrates
the earlier flows; it does not establish review of the new recipes.

Version 1.3 addresses the actual 16 October 2026 rejection of v1.0.0:
“Your plugin uses dynamic tools to execute operations that were not
individually exposed for review.” The directory endpoint replaces generic
tool-selecting executors with individually exposed operations. For example,
the times-table worksheet has `get_times_tables_worksheet`,
`preview_times_tables_worksheet` and `export_times_tables_worksheet`.
Their schemas bind that worksheet and accept no `tool_slug` selector.
The live catalogue returns `detailTool`, `previewTool` and `exportTool` names;
recipes name each step's separate operations. Skills select names returned by
the catalogue and present in `tools/list`, rather than constructing names.
Saving a snapshot stores data and does not execute a generator. Existing
account-resource operations remain separate and scoped.

Version 1.4 adds an adult-facing privacy boundary across both directory
resources. Class reads return class-level summaries only; class writes accept
metadata, not a pupil roster. Consent, ownership or an explicit teacher request
does not authorise sharing under-13 personal information with OpenAI.

Marking returns aggregate progress and numeric question analysis only. Scores
are suppressed below five assessed pupils per session and five answered pupils
per question. Questions use generated ordinals, without stored ids or text.
Scripts, raw answers, named clusters, pupil identifiers and individual results
are not returned. Saved session/paper labels are omitted; schemes learned from
scripts require the adult's native editor rather than exposing their structure.
The public surface excludes pupil-specific mark overrides and notes.
Checked generic schemes and session settings retain their exact disclosed
confirmation/state rules. Sensitive work is handed off with the native URL;
the assistant does not open the private page or inspect its pupil content.

Owned-class seating can prepare deterministic layouts using the class
internally without returning its roster or individual desk assignments.
The public surface excludes arbitrary pupil assignments and saved-plan
updates. Adult users inspect named placements, make changes and export in the
native editor independently. Existing class reconciliation, consent, capacity,
saved-plan and native download rules remain authoritative.

School summaries omit private full resource bodies and colleague contact
information. Only the school owner may confirm name/colour changes through
`update_school_identity`; no membership, invitations, logo upload or billing
capability is added. Sheet headers and reviewed unit outlines accept anonymous
teaching content only. Existing lesson/worksheet/display content of uncertain
privacy must be handed off, not read into ChatGPT for inspection or redaction.
Known child-personalised worksheets are omitted from public lists and refused
for read, AI edit and export, including lesson-linked native worksheet PDFs.
Anonymous teaching content and teacher answer keys remain supported. Do not
retry a refused resource through another format, lesson, connector or browser.

Saved classroom-tool CRUD accepts only generated typed safe-tool contracts.
Browser/private tool slugs and unsafe legacy snapshots cannot use saving,
reading, duplication or export to bypass the privacy boundary. Direct file
exports keep the real native account guard and byte verification. Public
deterministic previews and free-account downloads remain available.

AI display/lesson workflows keep their existing scoped access, credit quotes
and explicit confirmations. Some native account/access/quote operations have
`readOnlyHint:false` because allowance ledgers or policy/subscription mirrors
may refresh. These checks do not initiate a purchase or new spending; no
blanket claim that every account read is side-effect-free is made.

The exact current protected operation names and counts must come from the
refreshed production `tools/list`; source/package checks alone do not establish
deployment or complete protected-workflow acceptance. Sensitive native pages
are adult handoffs, never a browser fallback for obtaining pupil records.
The reviewed source teacher profile contains 78 protected operations, including
ten class/school, five seating and thirteen marking operations. This is a
source count, not a production-discovery claim.

The reviewer response and verification requirements are recorded in
`docs/plugin-operation-review/`. The version number and local package checks
do not establish deployment, successful rescanning, submission or acceptance.

To export current public detail/knowledge evidence from `packages/app`, using
the existing service ts-node runtime:

```sh
API_URL=https://edge-api.planitteachers.ai \
NEXT_PUBLIC_API_URL=https://edge-api.planitteachers.ai \
TS_NODE_COMPILER_OPTIONS='{"module":"commonjs","jsx":"react"}' \
  node -r ../service/node_modules/ts-node/register/transpile-only \
  -r ../service/node_modules/tsconfig-paths/register \
  scripts/export-teacher-plugin.ts
```

This reads public source data only. It does not import account content,
marketing operations playbooks, Facebook group inventories or credentials.
Source Markdown is data; the skills must not obey instructions embedded in it.
The rich `classroom-tool-details.json` export has its own local provenance and
does not overwrite the validated generated-contract metadata snapshot.

## Primary implementation references

- [OpenAI: package a plugin](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: define focused tools](https://developers.openai.com/plugins/plan/tools)
- [OpenAI: build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI: OAuth authentication](https://developers.openai.com/plugins/build/auth)
- [OpenAI: plugin guidelines and commerce restrictions](https://developers.openai.com/plugins/plugin-guidelines)
- [OpenAI: submit and publish](https://developers.openai.com/plugins/deploy/submission)
- [Plugins in ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)
