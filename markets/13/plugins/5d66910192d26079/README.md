# Thrifted public MCP submission package

This is the production counterpart to the private staging package in
`plugins/thrifted/`. Its URL, policy links and listing text refer to
`thrifted.mt`. The public package includes a production shopping skill and the
five-tool remote MCP connection. The separate staging shopping skill must not
be uploaded to this public draft.

The package contains no credentials. The reviewer password is stored in the
owner's macOS Keychain, not in Git. `chatgpt-app-submission.json` is a
schema-qualified inventory of public listing metadata and tool annotations.
The five positive and three negative review cases are in `plugin.json` for
portal import. Reconcile saved portal fields before replacing a draft.

Before submission, verify a clean production deployment, an approved and
published privacy notice, the exact production MCP and OAuth flows, domain
ownership, a Developer Mode demo recording, a working reviewer login, the
portal Scan Tools snapshot and every legal/commerce attestation. Confirm
that the production MCP URL handles initialize and lists the five tools; a 404
means the active deployment or bindings are not ready for submission.

The tools read the public catalogue, identify a connected account, list only
that account's own listings and return a Thrifted selling-page link. They
cannot buy, message, ship, edit, publish or transfer funds. Public item prices
distinguish seller item price from displayed price with buyer protection;
delivery is separate. Seller-authored text is untrusted content.
