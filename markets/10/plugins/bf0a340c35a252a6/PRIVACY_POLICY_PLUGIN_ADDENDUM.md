# Suggested Privacy Policy Addendum For Pretture ERP ChatGPT Plugin

Use this as source text for the public Pretture privacy policy page or a dedicated plugin privacy page.

## Pretture ERP ChatGPT Plugin

The Pretture ERP ChatGPT plugin lets authorized users connect ChatGPT to their Pretture ERP account through Pretture's hosted MCP service. The plugin is used to run read-only, backend-calculated ERP sales analytics and return relevant metrics to the user.

### Data We Collect Or Process

When you use the plugin, we may process:

- Account and authorization data needed to connect your Pretture ERP account.
- OAuth session records, client identifiers, access-token hashes, refresh-token hashes, and revocation records.
- Encrypted ERP credentials or tokens needed to perform authorized ERP requests.
- ERP report parameters submitted through ChatGPT, such as date ranges, filters, grouping, and return-handling choices.
- ERP report responses returned by the configured Pretture ERP sales analytics endpoint.
- Operational logs, including request identifiers, timestamps, connection status, tool names, endpoint names, HTTP status, latency, and sanitized query parameters.
- Administrator account and audit data for managing access, credentials, configured backend endpoints, and activity.

We do not intentionally store raw OAuth access tokens, raw refresh tokens, or raw ERP credentials in logs. Credentials are encrypted at rest, and activity logs are designed to exclude passwords, tokens, cookies, and authorization headers.

### How We Use Data

We use this data to:

- Authenticate and authorize access to the plugin.
- Connect ChatGPT to the user's authorized Pretture ERP account.
- Execute reviewed sales analytics tools through the Pretture MCP server.
- Return ERP analytics and operational results requested by the user.
- Maintain security, rate limiting, fraud prevention, troubleshooting, and auditability.
- Allow administrators to manage users, credentials, configured backend endpoints, and activity.

### Recipients And Processors

Data may be processed by:

- KAVworks Technologies Private Limited, which operates Pretture.
- Hosting, database, security, monitoring, and infrastructure providers used to operate the Pretture ERP and MCP services.
- OpenAI, when users choose to use the plugin through ChatGPT, subject to OpenAI's applicable terms and privacy practices.
- Legal, regulatory, or security recipients when disclosure is required by law or needed to protect the service.

We do not sell plugin data.

### Retention

We retain plugin data only as long as reasonably necessary to provide the service, maintain security, meet legal obligations, resolve disputes, and support audits. Encrypted credentials and OAuth records are retained while the user's connection remains active or as needed for security and audit purposes. Activity and audit logs are retained for operational, security, and compliance needs and then deleted or anonymized according to Pretture's retention practices.

### User Controls

Users may disconnect or revoke plugin access through ChatGPT or by contacting Pretture. Administrators may disable, reset, or revoke user access and connection credentials from the Pretture admin portal. To request access, correction, deletion, or more information about personal data, contact `contact@pretture.com`.

### Contact

For privacy questions about the Pretture ERP ChatGPT plugin, contact `contact@pretture.com`.
