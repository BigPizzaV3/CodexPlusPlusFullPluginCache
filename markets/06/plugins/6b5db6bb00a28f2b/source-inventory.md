# Source inventory: Cloudflare Data Security

## Source and access

- Source type: user-provided product request and research in this Codex task.
- User intent: create a Cloudflare security plugin focused on tenant/row isolation and strong security guidance across Cloudflare application infrastructure.
- Access status: prior assistant performed read-only Cloudflare documentation research and inspected account resource counts. No app source, database rows, secrets, or private application code are included as plugin source.
- No source GPT URL, export, user-provided GPT instruction text, or pre-existing plugin record was supplied.

## Verified platform facts carried into the package

- Cloudflare D1 is SQLite-based and exposes SQL through Worker bindings; D1 does not provide PostgreSQL-style native row-level security policies. D1 tenant/row authorization must be enforced in the application/Worker layer.
- PostgreSQL connected through Hyperdrive can use PostgreSQL RLS. Hyperdrive uses transaction pooling; session state must be established in the relevant query/transaction and must not be assumed to persist on a pooled connection.
- Identity verification and object/row authorization are distinct. Access/JWT validation does not by itself prove that an authenticated principal may access a requested row or object.
- Caching, R2 signed URLs, KV, Durable Objects, Vectorize/AI Search, bindings, secrets, and background jobs each require storage- and path-specific isolation checks.
- The prior account inventory found D1 databases and Workers but no R2 buckets or KV namespaces at that time. This is contextual, time-bound inventory, not a claim about all Cloudflare accounts or current state.

## Product assumptions

- Intended audience: developers, reviewers, and operators building multi-tenant Cloudflare applications.
- Product type: educational and code-review assistant; it does not itself enable a Cloudflare account setting, inspect arbitrary accounts, or deploy changes.
- “Maximum security” is interpreted as layered, fail-closed risk reduction; absolute or 100% security cannot be promised.
- For project-specific assessment, the assistant asks for relevant code/config/schema or clearly explains what evidence is missing.

## Unavailable source details

- No specific project identity provider, tenant model, privilege model, schema, deployment environments, threat model, compliance regime, or availability constraints were provided.
- No access to production source code or current live account inventory is included in this package.
