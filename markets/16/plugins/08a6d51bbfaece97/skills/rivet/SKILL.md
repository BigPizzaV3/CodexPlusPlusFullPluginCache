---
name: rivet
description: Explore design directions for a local web app with Rivet, compare them in its editor, and implement the user's chosen direction.
---

Use this plugin's Rivet MCP tools to inspect explorations, sign in, explore designs and retrieve chosen directions, and manage design context. Use an explicit absolute project path. If sign-in is required, use the login tool and let the user finish in their browser.

Open or attach the editor with this plugin's pinned CLI. Replace the project path below. Use `--user-port` when an app dev server already runs.

```sh
RIVET_PLUGIN_NAME=rivet NODE_ENV=production RIVET_AUTO_UPDATE_DISABLED=1 node "${PLUGIN_ROOT}/node_modules/rivet-design/bin/rivet.js" open --project /absolute/project --no-browser --caller-agent codex
```

Open and share the returned editorUrl. For an existing app, resolve saved instructions before authoring a short runLabel and distinct briefs for variants start. For a fresh empty project, use fresh mode with the same host-authored runLabel and distinct briefs. Include the user's design references unchanged.

Read autonomy from rivet_get_design_context before selecting saved references. When autonomy is off, use saved references only when the user asks, and pass profile: "auto" for that request. When autonomy is on, you may search and select relevant saved references for the request. Do not change the user's autonomous-references setting. A disabled profile stays off.

rivet_find_references ranks saved references by meaning with zero model calls. It may start the coordinator and installed local search engine; it never rebuilds, downloads, imports, or makes external requests. Read status, searchMode, and coverage before interpreting an empty result. If search is unavailable, report the status and continue without invented references.

Inspect promising keys with rivet_get_design_context. Pass 1–3 distinct keys and concise reasons to rivet_explore_designs as referencePicks: {profileId, picks: [{key, reason}]}. Reasons are at most 500 characters. With autonomy off, explicit profile: "auto" is required; profile: "off" drops picks. Rivet attaches valid picks as removable reference chips and records their delivery without a selection model call. Delivery does not prove the generated design used them.


When a tool returns complete_host_variant_work, follow each server-authored workerPrompt verbatim and use the returned worker agent type. Each worker completes its own assigned work promptly. Otherwise Rivet owns execution; inspect status until terminal. Poll during start_in_flight. Cancel only when the user asks. When the user chooses a direction, retrieve it with rivet_get_exploration using project, sessionId, and variantId, then implement and verify it in the user's project. Rivet retains prototype artifacts and context.

Do not run a global install, updater, or permission configurator. Updating this plugin is separate from running a design request. Existing CLI integrations may duplicate this plugin's tools and workers; inspect the migration guidance before changing user configuration.

Plugin sessions collect approved product metadata: action categories, outcomes, counts, timings, and runtime version. Signed-in events use the Rivet account ID and email is set as a profile property; anonymous use has a persistent installation identifier. Email is excluded from event properties, and installations are not aliased to accounts. Plugins do not upload raw logs, exception contents, prompts, source, local paths, replay, or console recordings. Model and account requests remain separate. Functional feature-flag lookups remain enabled with the installation identifier and flag analytics disabled, including when optional telemetry is off.

Honor a user's telemetry preference on every launch. Set `RIVET_TELEMETRY_DISABLED=1` in the host environment to disable optional telemetry across MCP and pinned CLI processes. A persistent MCP configuration can also add `--no-telemetry` to its server arguments; include that flag on pinned CLI commands too. Restart the plugin and its editor/coordinator after changing launch configuration. A telemetry-policy mismatch requires finishing existing work and explicitly stopping the mismatched runtime before reopening; do not stop it automatically.
