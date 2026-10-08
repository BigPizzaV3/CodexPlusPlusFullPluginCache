# Plans and access

Use this reference for questions about Floose plans, onboarding, connection
problems, and feature restrictions. These are product rules, not the current
user's billing status. Treat explicit server eligibility results as authoritative.

## Plugin eligibility

| Capability | Free | Writer | Advanced |
| --- | --- | --- | --- |
| Connect and use Floose MCP | No | Yes | Yes |
| Notes, saved links and addresses, cloud files, Canvas via MCP | No | Yes | Yes |
| Floose Code via MCP, including Code cards and Code file sharing | No | No | Yes |
| Vault content via MCP | No | No | No |

This table describes MCP access, not all capabilities of the standalone Floose
app. For example, lack of Free MCP access does not mean Free users cannot take
notes in the app. Feature access can also depend on server-granted entitlements;
never infer the user's purchased plan from one successful operation.

There is no billing-status, checkout, or plan-upgrade tool in this MCP catalog.
Do not invent one, claim an upgrade succeeded, or deliberately try writes to
probe eligibility. A successful login alone does not prove access to every tool.

Subscriptions are managed in the Floose app, not purchased by this skill or MCP.
Account registration itself does not activate a paid subscription. Explain this
neutrally when asked or when a relevant feature is denied; do not insert upsells
into unrelated work. Do not invent prices, discounts, renewal dates, credit
balances, or subscription status. For current prices or billing details, refer
the user to the information shown in their Floose app.

## Connect or register

For an existing account, start the Floose connection from the host's plugin
settings, sign in on Floose's hosted page, and authorize the requested access.
The MCP endpoint is `https://note.floose.app/mcp`.

The login route `https://note.floose.app/oauth/login` requires a dynamically
generated OAuth `login_challenge`; do not offer the bare route as a standalone
working login link or construct a challenge yourself.

For a new account, the login page offers **Crea account**. Registration requires
email verification. Continue in the Floose app using the same account, then
return to the host to connect after the account has the required entitlement.
Do not promise that installing the app transfers the browser session or logs
the user in automatically. The app download page is
https://note.floose.app/download; do not promise platform availability beyond
what that page actually offers.

## Diagnose the message, not the plan

| Observed situation | Appropriate next step |
| --- | --- |
| Floose is not connected or no Floose tools are available | Explain how to connect it in the host. General help is still possible; do not simulate private results. |
| Login, expired-session, or missing-scope error | Ask the user to complete or renew the hosted connection. Do not ask for credentials in chat or change the app's security settings. |
| Explicit Writer/Advanced requirement | Explain the named requirement and which requested action is unavailable; do not assume every authentication failure is a plan restriction. |
| Code action denied while other tools work | Explain that Floose Code requires Advanced. Do not store the same artifact in another resource type to bypass that restriction. |
| Timeout, service unavailable, or connection failure | Report a connectivity/service problem without asserting the user needs a different plan. Avoid automatic repeated writes. |
| Resource not found or empty search | Clarify the target or check the appropriate resource type. Do not infer a plan failure or assert the whole account is empty. |
| User says the required plan is already active | Suggest checking the signed-in account and entitlement status in the app, then reconnecting; if unresolved, use Floose support. Do not recommend purchasing again. |

Support: https://note.floose.app/support/

Never grant access, disable MFA, or change billing to fix a connection. When
asked about costs, distinguish Floose's required plan from the host's own plan
and usage terms. Floose's entitlement checks may initialize or update billing
records and initial credits; they do not purchase a subscription or charge a
payment method. This is not a promise that every service is free or unlimited.
