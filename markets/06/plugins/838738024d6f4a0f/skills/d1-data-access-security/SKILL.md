---
name: d1-data-access-security
description: Review D1 query safety, API exposure, authentication, tenant isolation, and data lifecycle controls.
---

# D1 and Data Access Security

Review D1 access paths, Worker bindings, HTTP/API exposure, SQL construction, query parameterization, input validation, authorization checks, migrations, backups/restore practices, and sensitive-data handling. Use prepared statements and bound values for user-controlled data; validate types, lengths, formats, and allowed values. Trace authorization from verified identity to every row/object operation, checking tenant ownership and preventing insecure direct object reference/BOLA patterns. Do not assume a user-supplied ID or client-side filter is authorization.

D1 is SQLite-compatible managed SQL; do not claim PostgreSQL RLS semantics or native row policies. Authorization must be enforced by application code and query design. The account audit should inspect metadata/config only by default, not read table data. If the user explicitly requests data-level review, minimize fields/rows and avoid exposing personal or secret values in the report. Distinguish static query review from tested runtime enforcement.
