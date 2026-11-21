# MCP tool review - latest supplied export

Status: supplied-metadata review PASSED. This supersedes the previous findings.

Source: tools(2).json supplied by the creator, 20 tool descriptors.

- All tools set readOnlyHint, destructiveHint and openWorldHint to explicit booleans.
- Read-only operations set destructiveHint=false.
- Paid website creation sets destructiveHint=true, readOnlyHint=false, idempotentHint=false.
- Public-content upload, move and delete operations set openWorldHint=true and destructiveHint=true.
- Directory creation remains additive and idempotent.
- One-time download-URL issuance is declared non-read-only, non-destructive, non-idempotent.
- create_website_database sets readOnlyHint=false, destructiveHint=true, idempotentHint=true; it can rewrite its managed config file.
- create_website_database and get_website_database output schemas no longer declare a password property.
- The database creation description explains server-side credentials in /database.php, outside /httpdocs, and shows PHP loading that config.
- run_database_query retains write/destructive/non-idempotent classification.

Bounded account operations can retain openWorldHint=false when they do not publish public content or address arbitrary external entities.

Verification limits:
- This review covers supplied tool descriptors and schemas, not server source or all actual responses.
- Do not read /database.php into the model to test its contents. Check credential-file access protection in the server implementation. The creator reports fixes; runtime enforcement is not established by this JSON.
- Refresh/reconnect the private connection and scan the live official MCP endpoint in the submission portal. Confirm the imported annotations and schemas match this export.
- Live regression checks of the revised database-configuration workflow remain to be completed on a disposable reviewer website.

Guidance: https://developers.openai.com/plugins/plugin-guidelines
