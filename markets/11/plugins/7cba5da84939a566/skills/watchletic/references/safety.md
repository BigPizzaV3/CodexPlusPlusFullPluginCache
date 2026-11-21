# Safety and account changes

Full access is selected by default during MCP authorization. Users can choose Read-only instead. A Full access connection is required for mutations.

For every settings, activity, structured-workout, route, layout, device, readiness, training-load, analytics, integration, deletion, or bulk-export change:

1. Call the focused preview tool with the exact proposed action.
2. Show the returned action summary, before-and-after diff, and warnings.
3. Ask for explicit confirmation immediately after showing that preview.
4. Only after an unambiguous confirmation, call the matching apply tool with the unchanged action and confirmation token.

Never apply after an ambiguous reply or after changing the payload. Preview again instead. Previews have no time limit, but apply still requires the same authorized session and checks current revisions. Do not seek alternate credentials when a Read-only connection blocks an apply action.

The plugin cannot purchase or upgrade Watchletic Club. Existing subscriptions are managed in the Watchletic app through the applicable platform store.
