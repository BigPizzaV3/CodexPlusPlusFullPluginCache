# Casually

Prepare marketing campaigns with your team's saved projects and brand context.
Use Casually to save landing page and email drafts, reuse existing images and forms,
request human review, and read actual campaign results.

## What you can do

- Read and update shared project context and saved brand references.
- Save LP drafts from your own copy, or generate LP layout and email text using existing account credits.
- Revise a saved LP, reuse project images, and configure saved forms.
- Request human review. Publish or queue email only after an authorized person has approved the exact saved version and audience in Casually.
- Read measured project results and save campaign reports with an explicit reporting period.

This directory integration does not generate AI images, video or audio, execute arbitrary API operations,
approve on a person's behalf, or offer subscription/credit purchases. Do not install the full marketplace
edition alongside this edition in the same chat: use one Casually connection for the intended task.

## Connect

When available in your AI client's directory, install Casually and choose Connect or Authenticate.
For prerelease review, add the HTTPS endpoint below as a custom remote MCP connector in ChatGPT or Claude.
For plugin-bundle review, select repository clyr-inc/casually-plugins and path directory/casually.
Public directory approval is separate from this GitHub release.
Sign in through the Casually browser page and approve the requested access.
The client receives and manages OAuth tokens. Never paste passwords, API keys or tokens into chat.

The fixed HTTPS endpoint is https://api.casually.marketing/api/v2/mcp/directory.
It is a limited surface of the same protected OAuth resource at /api/v2/mcp.
No executable, shell hook or local MCP process is bundled. The package contains five skills:
setup, project, campaign, landing-page and report. Chat, desktop and coding clients may expose different
installation controls; follow the client's native connection flow.

## Requirements and effects

You need a Casually account and permission to access the chosen project. Availability and quotas follow
your plan. AI campaign generation and LP revision require an explicit maximum credit budget;
charges are settled by actual usage within that budget. Confirm the available balance before generating. Client/model fees are separate.
Connection checks and project reads do not generate paid assets. Content creation and edits persist in
Casually. Registering a reference website fetches its public content. Human review requests may notify
approvers; launch publishes the approved page and queues email to the fixed reviewed audience.
A queued email is not proof of inbox delivery.

## Data sent, read and saved

### Reference website registration

`register_project_service_site` calls Casually's fixed `POST /api/creatives/projects/:id/service-site`
operation. Its arguments are projectId, the selected public website URL, a unique requestKey and
the project's latest baseUpdatedAt. It fetches that website to save typography, colors, copy,
screenshots and existing image references in the authorized project. It cannot accept an arbitrary
API path, HTTP method or request body, and does not authenticate to the source website, change DNS,
publish a page or send email. Use a public website you are authorized to reference.

### Tool data and retention

The AI client sends only the arguments of the Casually tools it calls: selected IDs, a task brief,
user-supplied copy, requested edits, selected website URLs, form settings, and any explicitly supplied
audience. Casually uses the authenticated member and organization for permission checks. It reads and
saves requested project/workflow/form/page data, performs the requested operation, and returns relevant
results and links. Tool execution input summaries and results older than 30 days are cleared periodically.
Saved artifacts and operational metadata (date, operation, outcome and usage) are retained separately;
revoking a connection does not delete them. Use service deletion controls or contact support to request deletion. The plugin does not request the full
conversation, inspect local files, or send credentials from your machine.

For AI text/layout generation Casually uses its configured generation providers on the server. Public
reference-site registration can fetch that site and save brand-reference assets. Launch can send the
approved campaign through the organization's configured mail provider. No provider keys are requested
by this package. Review the service privacy policy before connecting.

## Disconnect and support

Revoke access in Casually's /dashboard/plugins connection guide, or disconnect in your AI client.
A failed or revoked connection requires native OAuth again; do not fall back to another endpoint or an API key.

- Website: https://casually.marketing
- Setup documentation: https://github.com/clyr-inc/casually-plugins/tree/main/directory/casually
- Support: https://github.com/clyr-inc/casually-plugins/issues
- Support email: contact@clyr.co.jp
- Privacy policy: https://casually.marketing/legal/privacy-policy
- Terms: https://casually.marketing/legal/terms

Do not post customer data, reviewer credentials, tokens or private preview links in public issues.
This package uses the Casually Plugin License in LICENSE; CLYR株式会社 retains ownership.

## Review recordings and verification

The [0.4.0 review release](https://github.com/clyr-inc/casually-plugins/releases/tag/directory-v0.4.0) includes actual ChatGPT and Claude walkthroughs, chapter indexes and submission ZIPs. [Verification notes](./VERIFICATION.md) distinguish actual client results, supplemental protocol checks and untested delivery paths. These artifacts do not indicate directory approval. Reviewer credentials are provided privately and never included in this repository.
