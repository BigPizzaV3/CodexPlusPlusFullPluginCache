# Existing tool annotations and submission justifications

All three tools remain unchanged in the supplied MCP 0.1.1 source. Copy the justifications into the portal's tool-review fields after its live scan; this document does not modify the server.

| Tool | readOnlyHint | destructiveHint | openWorldHint | idempotentHint | Justification |
|---|---|---|---|---|---|
| search_public_collections | true | false | true | true | Reads genuinely published Curavo search results; cannot change records. Returns public website links and may encounter untrusted public content. Repeating a query changes no user content. |
| get_public_collection | true | false | true | true | Retrieves an existing public guide and allowlisted entries/links. No private access or destructive operation. Repeated reads can increment operational aggregate counters, but do not change user content. |
| get_collection_link | true | false | true | true | Verifies public availability and returns a canonical website link. Does not create a share permission or modify records. Verification can increment an aggregate read counter. |

Content_notice labels collection text as untrusted user-generated content, not instructions. No endpoint accepts a caller-supplied arbitrary upstream URL; IDs, query length, categories and result limits are validated. Empty/unavailable responses must not be replaced with invented recommendations. Public read-only tools require no OAuth reviewer credentials.
