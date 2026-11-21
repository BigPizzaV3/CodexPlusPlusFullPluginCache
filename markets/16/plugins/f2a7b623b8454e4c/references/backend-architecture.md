# Backend and data design

- Model entities, ownership, multi-tenancy, API contracts, authorization and migrations before selecting vendors. Existing backend is authoritative for extension requests.
- Strong defaults: typed validated inputs, server-side authZ, pagination, idempotency, transaction boundaries, request limits, timeouts, error handling, structured logging without sensitive fields.
- For uploads: size/type limits, storage permissions and malware risks. For payments: use approved processors and verified webhooks; never store raw payment details.
- Data stores: choose relational, document, embedded/local or external service based on query/consistency/offline requirements; avoid unnecessary layers.
- Client should never hold privileged API/database secrets. Keep user tokens and credential lifecycle scoped and documented.
- Performance and accessibility are functional quality: practical loading states, local caching only when safe, retries with backoff, user-visible failure handling.
- Tests: schema changes, auth scopes, happy/negative paths, read/write integrity, network failure and concurrency.
