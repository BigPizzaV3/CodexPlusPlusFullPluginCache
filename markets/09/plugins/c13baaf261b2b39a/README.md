# WallKiwi

Package version **1.4.0** adds the public-plugin privacy boundary. This is an
adult-facing integration using anonymous or synthetic teaching inputs only.
Never transmit personal information about children under 13 to OpenAI. Pupil
names/ids, rosters, photographs, scripts, individual answers/results and named
seat assignments stay outside this integration. Give the exact native link
for the adult to complete sensitive steps independently; never open, capture
or read those private records back through a browser or another connector.
Prior 1.3.1 dashboard checks do not approve these changed 1.4.0 contracts.

Plan, measure and prepare classroom displays with 26 quick, non-AI utilities and all 14 existing printables. The same native calculations run on the website and through the hosted MCP. Preview anonymously; a linked free account can save, reopen, revise, duplicate and download a planning PDF without an upgrade, download allowance or AI credits. Native saved-item capacity and rate limits apply.

The practical catalogue covers board area and borders, backing paper, columns and rows, grid fitting, centred positions, even gaps, mounts and heading zones; cutting yield, pouch fitting, print quantities and costs, scaling and resolution; print bleed and printer margins, and multi-board materials budgets; plus fixing positions and cord length. These are calculation records and diagrams, not templates or artwork replacing the paid display maker.

Existing display users can browse current examples, read owned packs, create and build custom walls, lettering, bunting or decorations, edit versioned manifests and export permitted PDFs or ZIPs. Designing, building and rebuilding use the connected account’s existing credits and native feature access. Read the live balance and server prices before spending; ownership and output rules apply. An insufficient balance is a restriction to report neutrally. No purchase, subscription or token-sale actions are exposed.

## Connection

Remote MCP: https://wallkiwi.com/mcp

Public discovery, exact settings and real previews need no account. Saved calculations and downloads use WallKiwi OAuth with tools:read/tools:write. Custom display operations use displays:read/displays:write. Sign-in is supplied by the shared Planit account issuer at https://planitteachers.ai; tokens are bound to the WallKiwi resource. Planit utility names and saved classroom resources are separate.

Both MCP import files explicitly declare server-level `extensions["com.openai"].auth` with `type:mixed`, `client.mode:dcr`, exact `resource:https://wallkiwi.com/mcp` and `defaultScopes:[]`. Anonymous tools remain public; protected tools request their actual scopes through native consent. The package includes no client id/secret or token, and leaves authorization, token and registration URLs to the live discovery documents. Planit's shared sign-in is expected; the WallKiwi audience remains separate. Empty host defaults avoid a blanket scope request; the server's minimal read-only fallback and per-tool step-up still apply.

[OpenAI's package documentation](https://developers.openai.com/plugins/build/plugins#configure-mcp-authentication) specifies this auth extension. The published Agent Plugins base schema currently rejects all server extensions, so only the transport projection passes that schema; the documented OpenAI auth contract is checked separately. Full base-schema compatibility of the vendor extension is not claimed.

Read get_wallkiwi_catalog before choosing tools. Each row supplies exact detailTool, previewTool and exportTool names that are individually exposed in tools/list. Read that detailTool before setting values, then call its previewTool with the actual inputs. Do not construct operation names or pass a tool_slug selector to preview/export. Keep the complete returned snapshot and string seed for saving and exporting. Do not send pupil details, images or credentials in utility arguments. For uploaded photos or sensitive existing content, give the exact native editor link and hand the step to the adult without opening or reading it back. Only anonymous/synthetic examples may be inspected through this integration.

## Build and verify

- python3 scripts/build-wallkiwi-plugin.py creates dist/wallkiwi-plugin.zip.
- python3 scripts/build-wallkiwi-plugin.py --check validates both package manifests, five skills, MCP configuration, current-site icon provenance and five positive/three negative review cases.
- python3 -m unittest discover -s plugins/planit-teachers/scripts -p test_plugin_mcp_auth.py checks both brands' explicit mixed/DCR auth, audience isolation, scope defaults, credential exclusion and portable/Codex parity; both builders also enforce it.
- python3 plugins/planit-teachers/scripts/plugin_mcp_auth.py --live-discovery reads both public OAuth metadata chains and verifies resource/issuer, DCR, S256 and public-client exchange support without registering clients or exchanging credentials.
- python3 plugins/wallkiwi/scripts/public-mcp-acceptance.py checks the complete individually exposed operation set, each real tool preview, retired-executor refusals, current sources and anonymous/invalid-token account recovery without paid generation.
- python3 plugins/planit-teachers/scripts/validate-operation-snapshots.py checks both brands' local per-slug contract metadata, source hashes and operation bindings. Add --archive dist/wallkiwi-plugin.zip to verify the runtime archive excludes development snapshots/scripts. --refresh regenerates local metadata only, without a production capture or deployment.

Normal deployments regenerate registered tool definitions and page discovery. Published example content is read live. The shared utility catalogue has generated copies in each standalone build, guarded against drift. The checked source contracts contain 40 utility entries, each with separate detail, preview and PDF export operations; this source count is not evidence of deployment. Published pages, FAQs and catalogue metadata are data. Each utility's executable operations are separately exposed upfront with fixed bindings and closed schemas. A new utility or changed executable schema requires deployment, a refreshed scan and review of its operation definitions. A catalogue update cannot enable an unexposed operation.

Version 1.2 adds three guided `projectWorkflows` to the existing catalogue: mounted layout and pouch checks, print size/resolution/sheet costs, and materials for several boards. Recipes use current registry settings, exact numeric result keys and explicit units, including centimetre-to-millimetre mappings. They describe existing operations rather than executing jobs. New calculation connections require a checked recipe; a new tool still appears through normal catalogue discovery.

Version 1.3 applies the remediation for Planit Teachers' 16 October 2026 dynamic-tools rejection to WallKiwi too. The directory endpoint removes generic utility executors from discovery and rejects direct calls. For example, `get_display_mount_size_calculator`, `preview_display_mount_size_calculator` and `export_display_mount_size_calculator` each describe one fixed utility, with per-operation annotations and authentication. Guided recipe steps name those separate operations; saving a snapshot stores data without executing it. Refresh and inspect all definitions in the publisher dashboard after deployment and before submission. See `docs/plugin-operation-review/` for the rejection, decisions and verification requirements.

Question search now ranks authored help answers, tool FAQs and page summaries, preserving original titles and source URLs. Full guide files read the native publication index beyond the first browsing page. Bounded work, memory or failed sources produce explicit partial-read notices and links to individual pages. See `docs/plugin-useful-workflows/verification.md` for this version's local evidence; the existing walkthrough shows the earlier release.

## Public-plugin privacy and maintenance boundaries

All five skills prohibit transmitting under-13 personal information to OpenAI
and require anonymous or synthetic inputs. Pupil names/ids, photos, rosters,
medical details, scripts and individual results cannot travel through utility
arguments, saved snapshots, display manifests, exports or browser readback.
Do not read an existing record merely to decide whether to redact it; hand
uncertain private content to the adult at the exact native link.

The native saved-tool gateway validates the generated safe utility/input
contracts and rejects browser/private slugs and unsafe legacy snapshots.
Normal ownership, capacity and account-only download rules remain in force.
`get_display_access` and `get_wallkiwi_tool_download_access` may refresh native
allowance/access mirrors and correctly advertise `readOnlyHint:false`; neither
check generates artwork, initiates a purchase or authorises spending.

## Review

Prepared listing and reviewer cases are in plugin.json. Both 256-square PNG icons are mechanical exports of the core site's scissors mascot at `packages/app/public/images/wallkiwi/kiwi-mascot.webp`, each 9,866 bytes. Transparent corners, opaque artwork and source/export hashes are verified; the complete mascot stays below 10 KB. Earlier-release walkthrough: https://wallkiwi.com/plugin-review/walkthrough. It does not establish the v1.4.0 privacy contracts. A new film needs fresh post-deployment production captures and acceptance evidence; it has not been recorded or rendered for this revision.

The owner has requested public-directory submission in bjameseastwood@gmail.com. The browser must be connected to that account. Supply reviewer credentials only with specific owner permission; the owner confirms the final legal attestations. Acceptance and search traffic cannot be guaranteed. See docs/wallkiwi-free-rollout/verification.md for the tested release evidence.
