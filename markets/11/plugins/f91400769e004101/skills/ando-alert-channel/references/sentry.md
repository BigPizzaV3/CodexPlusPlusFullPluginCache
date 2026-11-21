# Sentry alerts in Ando

Refresh [the Sentry guide](https://docs.ando.so/docs/connecting-apps-to-ando/sentry), live connection schemas, and the installation UI before executing. These notes describe the inspected source and are not proof of deployment or account availability.

## Resolve the user's intent

Distinguish a new-issue feed from issue-alert rules and metric-alert rules. Ask which organization/projects, destination audience, severity or conditions, and follow-up behavior they want. Do not assume “Sentry alerts” means every issue in every project.

## Native setup

The documented admin path is Studio → Apps → Sentry → Issues in Ando → Set up. The person approves the Sentry installation and returns to Ando to complete the channel setup. Inspect existing installation state before repeating setup.

The inspected native implementation provisions a public #sentry feed (with a fallback name when needed). Confirm that audience fits the request before using it for sensitive events; do not promise an arbitrary private destination through this path. Inspect current supported routing if another destination is needed.

The native installation implementation includes an app connection for agents and a feed, while a standalone Sentry OAuth connection does not create the feed. Check the actual resulting agent access and delivery independently.

Issue events become native issue cards. The inspected source also handles event_alert and metric_alert deliveries; metric alert state changes are threaded. For rule-based alerts, the Sentry rule must select “Send a notification via Ando” as an action. Installing the integration or subscribing to issue webhooks alone does not configure those rules. Verify the currently exposed action and organization permissions in Sentry.

## Optional investigation and triage

Verify the agent can read a known issue in the intended organization/project. Discover current tools and account grants; do not assume resolve, assign, or snooze actions exist. A miniapp can offer only declared operations available to its installer/viewer. Separate local acknowledgment from resolving an issue in Sentry.

If agent follow-up is requested, establish its runtime and participation/trigger rules. Route investigation results to the issue thread and define when new information warrants another reply. Do not create issues, resolve real incidents, or alter production alert thresholds merely to demonstrate the setup.

## Evidence required

Record installation/readback, rule action where applicable, a representative delivery, the rendered card/source link, and later state behavior if tested. Test the miniapp or agent separately if included. When consent, provider permissions, or an unavailable feature prevents completion, identify the exact step; a mocked preview is presentation evidence only.
