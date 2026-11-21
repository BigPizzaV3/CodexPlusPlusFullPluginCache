# Rivet local plugin candidate

This plugin uses local stdio MCP and Rivet runtime 0.30.1. It is not marketplace-approved. Node 22.16+ in 22.x or Node 24+ must be available to the desktop host. OpenAI includes the runtime file closure traced from its locked production dependencies, with runtime assets and dependency notices at their original paths. Its manifest runs the bundled runtime directly.

## Account and data flow

Rivet requires a Rivet account and browser sign-in. The runtime reads its own access and refresh session from ~/.rivet/config.json, so an existing Rivet sign-in can be reused. The access token authenticates requests to the Rivet proxy. The refresh token is sent to the Rivet proxy's /api/auth/refresh endpoint to renew that Rivet session. These are Rivet credentials, separate from a coding provider's account.

The selected runtime defaults to proxy https://rivet-proxy.onrender.com and telemetry https://rivet-proxy.onrender.com/ingest. The proxy supports authentication, profile, reference, and evidence operations. Explicit prototype publishing sends its artifact to https://rivet-prototype-host.onrender.com/publish. Environment and application configuration can override service destinations. Local stdio describes the host-to-MCP connection; model prompts, project or reference context, and images can leave the machine for hosted processing. Request content is separate from the credential in an Authorization header.

Worker execution launches an installed, authenticated supported coding CLI and consumes that provider account's usage. Each provider CLI manages its own authentication. Rivet does not directly extract provider keychain files; launched workers can inherit environment variables. Plugin sessions send approved product event categories, outcomes, counts, timings, and runtime version to Rivet's configured telemetry endpoint. Signed-in events use the Rivet account ID, with email set as an analytics profile property rather than an event property. Anonymous use has a persistent random installation identifier. The plugin does not alias installation IDs, emails, or accounts. Raw log forwarding, exception payloads, Sentry, session replay, console recording, and automatic interaction capture are disabled in plugin mode. Functional feature-flag lookups use only the installation identifier, disable geo-IP enrichment, and emit no flag analytics. Model and account service requests remain separate.

To disable optional telemetry, persist RIVET_TELEMETRY_DISABLED=1 in the desktop host's environment so both MCP and pinned CLI processes inherit it. Alternatively add --no-telemetry to the MCP launch arguments and each pinned CLI invocation. Restart the plugin and editor/coordinator after changing launch configuration. Existing processes with a different or unverified telemetry policy are rejected until explicitly stopped. These controls affect future collection; they do not delete previously hosted records or disable required service requests.

## Review and migration



Use the Rivet skill to open an editor and the MCP tools for status, sign-in, and variants. Startup does not install global skills, agents, rules, or permissions. Before enabling this plugin alongside an existing Rivet CLI integration, inspect and back up the host MCP, skill, and worker configuration. Disable the duplicate integration only after confirming ownership; this plugin does not remove user configuration.

The npm runtime remains GPL-3.0-or-later. Dependency notices remain in node_modules, and Rivet's license is copied into notices. Integration source remains UNLICENSED. Authentication, model usage, worker fidelity, Dock launch, and Cowork require separate verification before submission.

## Support

Contact [support@rivet.design](mailto:support@rivet.design) for help. Read the [documentation](https://docs.rivet.design), [privacy policy](https://rivet.design/privacy), and [terms of service](https://rivet.design/terms).
