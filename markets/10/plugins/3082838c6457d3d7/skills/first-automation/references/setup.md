# Setup reference

Verified against the public product documentation on 2026-10-08. Prefer live tool schemas and observed app state if they differ.

Current server: https://superlog.sh/api/mcp (Streamable HTTP). An unauthenticated initialize request returns an OAuth challenge with resource metadata at https://superlog.sh/.well-known/oauth-protected-resource/api/mcp. Authentication is per user; no credentials belong in the plugin package. The documentation also describes workspace API keys for compatible clients; never collect them in conversation.

Documented management tools include get_workspace, list_integrations, refresh_integrations, list_automations, get_automation, create_automation, update_automation, list_automation_runs, start_automation_run, get_automation_run, cancel_automation_run, and send_automation_run_message. Discover their current schemas before use. No first-run step requires listing secrets, revoking API keys, or changing model credentials.

Creation uses name, description, enabled, and configuration. Configuration includes prompt, repositoryIds, triggers, and optional contextAccountIds. Slack triggers use kind=slack, integrationAccountId, channelIds, and eventMode. Current source distinguishes every_message, mentions, and both. IDs come from integration discovery, not names or guessed identifiers. Preserve selected repositories and integrations when editing an existing automation; inspect whether the current update schema replaces configuration before sending a partial object. Omitted model settings use defaults where supported.

The website editor can connect missing tools inline. The first save activates an automation. Test and Run now execute real work and require an active automation in the documented UI. Do not describe them as a dry run. The Active switch pauses future triggers; separately inspect already-running work before claiming all work has stopped.

Other paths: Sentry new issues/regressions; scheduled hourly/daily/weekly reviews; Slack questions or mentions; Discord commands. Recheck available triggers before presenting options. Repositories, models, integration authorization, and output destinations must be valid for the chosen path.

Sources:
- https://docs.superlog.sh/api-reference/mcp
- https://docs.superlog.sh/api-reference/automations/create-an-automation
- https://docs.superlog.sh/automations/overview
- https://docs.superlog.sh/automations/triggers
- https://docs.superlog.sh/automations/templates

Some older documentation still describes the prior telemetry product. Do not mix its project-scoped APIs or Slack notification settings with the current workspace automation editor.

## Plans

Superlog has free and paid usage plans, purchased and managed on its website. Explain usage and link to https://docs.superlog.sh/settings/billing or https://superlog.sh/pricing when asked; verify current pricing rather than hardcoding prices. Sandbox compute counts toward usage even when users supply their own inference access. Do not imply connecting this plugin includes unlimited runs, and do not purchase or upgrade a plan as part of setup.

## Legacy connection handoff

Current application source maps the integrations page to https://superlog.sh/settings. Integration cards without connected accounts use the Add action; existing connections use Manage. Guide only the required provider for the current step, then refresh and verify on return before asking for a channel or repository. Provider consent screens can vary; do not invent their labels. An empty workspace should receive guided onboarding, not a missing-connections report.

## Connections from chat

Discover list_available_integrations and start_integration_connection in the live schema before use. The start tool accepts a provider and returns connectionType, status, url, expiresAt, and instructions. OAuth consent links are bound to the authenticated Superlog user/workspace and expire in ten minutes. Reissuing a link replaces that pending flow. Supported direct consent providers in the prepared backend change are Slack, GitHub, Sentry, Discord, Vercel, Linear, Google Cloud, Axiom, and PostHog. Additional-configuration providers return secure_setup instead; credentials stay out of chat. Use live discovery rather than assuming this backend version is deployed. Verify completion through list_integrations, using refresh_integrations for Slack/GitHub resources when needed.

The optional inline connection card uses handoffUrl to open consent with a host-supplied conversation return address. It checks list_integrations and requests a follow-up after verification. Automatic return requires host support; never promise it for a plain link or invent the current conversation URL. Otherwise the user sees a focused completion page and can return manually. A connection follow-up is not authorization to activate an automation; retain the agreed setup scope.
