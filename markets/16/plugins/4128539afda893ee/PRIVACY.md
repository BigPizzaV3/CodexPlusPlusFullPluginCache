# J-Express AI plugin privacy policy

Last updated: 7 November 2026

This policy describes J-Express, a scientific data analysis product operated by **Bjarte Dysvik**, an individual developer in Norway using **Resonalis** as the project and brand name. Resonalis is not currently a separately registered company. The policy applies to ChatGPT and Claude integrations using the MCP server at `https://jexpress.resonalis.com/jexpress2026/mcp`. The public version is at https://resonalis.com/privacy/. For privacy or user-rights inquiries contact **contact@resonalis.com**.

## Categories, purposes and recipients of data

J-Express is intended for **non-personal, non-clinical research datasets**. We do not require an account or ask you to submit payment information, patient records, passwords, or personal identity documents. Service operation nevertheless involves some technical information that may constitute personal data.

| Information | Purpose | Recipient / location |
| --- | --- | --- |
| Browser datasets, annotations, analyses and local preferences | Perform research analysis and restore local work | Your own browser storage; not routinely uploaded to a permanent J-Express dataset repository |
| Random browser session ID, connection secret, OAuth client details and permissions, hashed access/refresh tokens | Authenticate users, protect tools and relay approved requests | Cloudflare Durable Objects; not shared with arbitrary AI clients |
| Short technical dataset summary (type, shape and numeric analysis parameters) | Identify the connected workspace before authorizing tools | Cloudflare session relay |
| Authorized MCP results (selected matrix values, labels, annotations, research metadata, plots) | Answer the precise AI tool request | Temporarily via Cloudflare relay, then the specific AI client/provider you authorized (such as OpenAI or Anthropic) |
| IP-derived anti-abuse rate-limit keys and ordinary hosting request metadata | Protect client registration, delivery and security | Cloudflare infrastructure |
| Optional predefined usage event/analysis categories and count | Understand usage and reliability | Cloudflare Analytics Engine; no dataset values or persistent user ID in the application event |
| Email address and content you voluntarily send to support | Respond to your inquiry | Our email-service provider; do not email private datasets or credentials |

External annotation and enrichment services may receive gene identifiers or background lists when you explicitly invoke such a feature. The AI provider may independently retain tool results in chats or logs under its terms and controls. We do not sell research dataset content or use it for advertising.

## Application-level retention

An inactive browser AI session expires after approximately **30 minutes**, an OAuth access token after **15 minutes**, a refresh token after at most **30 days**, dynamic OAuth client registration after **30 days of inactivity**, an OAuth pairing request after **5 minutes**, and an authorization code after approximately **1 minute**. Uncollected tool results become eligible for cleanup after approximately **60 seconds**. A session revocation marker with no dataset contents persists for up to **31 days** to prevent old tokens being reactivated. IP-derived registration rate-limit keys expire after approximately **one hour**.

Disconnect/Revoke are designed to delete that session's access/refresh records and queued tool results promptly. Expiry and actual deletion are not identical; cleanup, Cloudflare logs/backups and data already received by an AI provider have their own retention mechanisms and are not guaranteed to disappear immediately. The browser workspace may persist until you delete it. Support correspondence is retained as needed to resolve the request and meet applicable recordkeeping obligations.

## Choices and controls

You can analyze data without AI, refuse/decline MCP approval, approve only selected scopes, disconnect the AI session, turn off optional telemetry in the app (or by using `?telemetry=off`), and clear the browser workspace/site storage. For information handled by an independent AI provider, use that provider's data controls. Contact **contact@resonalis.com** for questions or applicable access, correction, deletion and other data-rights requests.

## Browser workspace and data flows

J-Express runs in your browser. Your loaded datasets, annotations, selections and analyses are processed in the J-Express workspace. The plugin package provides connection information and scientific workflow guidance; it does not install local executable software.

When you authorize an AI client and it invokes a J-Express MCP tool, the request passes through the J-Express server to your connected browser session. The result returns through that server to the requesting AI client. Depending on the tool and permissions granted, results **may include raw numeric matrix values, dataset identifiers, row/column names, sample annotations, quality metrics, analysis results and exported plot images**. Such information is disclosed to the AI provider when returned to its client.

## Connection records and temporary processing

The J-Express server uses Cloudflare Durable Objects for connection/session state, OAuth client registration and token records. A browser connection sends an allowlisted technical context (dataset type/size and selected numeric analysis metadata) to the relay before any AI client is approved; matrix values and identifiers are not included in this initial context. A connected browser renews its session, which otherwise expires after about 30 minutes. Access tokens expire after 15 minutes; refresh tokens have a maximum 30-day validity. The OAuth registry stores hashes of tokens, not the bearer or refresh-token strings. Dynamic client registrations expire after 30 days of inactivity; pending requests expire in 5 minutes and authorization codes in about 1 minute.

The relay may temporarily store a queued MCP request and its response, including the returned scientific data, while passing it between your browser and the approved AI client. Results are deleted when collected and otherwise become eligible for cleanup after about 60 seconds. Expiration is checked when records are used, while actual deletion can be delayed by periodic cleanup, provider retention or backups. This is not a permanent server-side dataset repository.

**Disconnect and revoke:** the live relay denies MCP access as soon as browser sharing is inactive. The production Worker deployed on 7 November 2026 is designed to delete associated access/refresh records on an authenticated Disconnect/Revoke, purge queued requests and results, and keep a session-ID-only revocation marker for up to 31 days to prevent credential reactivation. Source-level tests and deployment succeeded. Independent-client integration testing and verification of Cloudflare provider-side storage and deletion remain outstanding; data already received by an AI provider cannot be withdrawn.

For OAuth dynamic client-registration abuse prevention, J-Express temporarily stores a rate-limit key derived from the caller's IP address (IPv6 grouped to a /64 prefix), with approximately one-hour expiry. This technical network information is separate from optional anonymous usage counts.

## Your controls

You choose whether to connect an AI client, review its requested permissions, and may disconnect the workspace. Permissions may include reading data, creating derived analyses or datasets, modifying data through authorized tools, and capturing plots. Datasets are locked against matrix edits by default; supported edit operations are designed to preserve source data by creating derived datasets. Review each requested action and permission carefully.

## AI providers and third parties

Information sent to ChatGPT is governed by OpenAI's applicable terms and privacy practices; information sent to Claude is governed by Anthropic's applicable terms and privacy practices. Resonalis does not control how these independent providers handle information you choose to share with them.

J-Express infrastructure is hosted using Cloudflare services. Optional J-Express usage statistics (enabled by default, disable in the app or with `?telemetry=off`) send only allowlisted event/analysis categories and a count to Cloudflare Analytics Engine; they contain no matrix values, names or persistent user IDs. This does **not** mean the host is unable to see IP addresses, timestamps or request metadata.

A read-only inspection of the production Worker on 6 November 2026 found `logpush: false` and no Tail Worker consumers. This does not establish that Cloudflare account-wide security/diagnostic logs, analytics retention or backups are absent; their exact retention has not been independently verified. The plugin does not intentionally sell dataset content or use it for advertising. No guarantee is made here about a third-party AI provider's model-training practices.

## Contact

Bjarte Dysvik (Resonalis project) — contact@resonalis.com.

This notice describes documented application behavior and selected live infrastructure settings, not external security, privacy or clinical certification. We cannot guarantee deletion of third-party provider logs or copies already received by a connected AI client.
