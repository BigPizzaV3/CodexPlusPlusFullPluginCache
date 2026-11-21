# Query conventions

- Namespaces and index requirements: `owl.data.show_dql_namespace`.
- Field and source discovery: select available tools such as `owl.field_schema.get`, `owl.log_index.list`, `owl.metric.list`, `owl.logging.list`, `owl.apm.list`, `owl.rum.list`, `owl.network.list`, `owl.profile.list`, or `owl.billing.list`.
- Events: call `owl.event.list`, then pass a returned document ID to `owl.event.get`.
- Catalog: call `owl.catalog.entity_type_query`, then `owl.catalog.entity_query`; use returned URNs for details or topology.
- Cross-workspace traces: discover accessible workspaces with `owl.account.workspace.same_org.list`, then use `owl.data.same_org_trace_query` with the requested scope and trace_id.
- Pass returned IDs, URNs, and workspace identifiers unchanged. Do not construct identifiers.
- For timeouts or rate limits, narrow the range, reduce fields, or adjust aggregation granularity. Follow server retry guidance and avoid unlimited retries.
- A 401 indicates an authentication gap; a 403 may involve permissions or an IP allowlist. Do not bypass restrictions through unauthorized workspaces.

These names are routing hints, not a fixed API inventory. Runtime discovery determines actual availability, parameters, and permissions.
