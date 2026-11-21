# Secure Access for Joomla — PUBLIC SUBMISSION DRAFT v1.0.0

This is a separate, portable draft created from the original miniOrange Joomla store-data submission workflow. It is NOT the original private workspace plugin and does not modify or replace it.

## Contents

This is an MCP-only public upload; no skills are bundled.

- `plugin.json`: public listing, 5 positive and 3 negative review cases, demo link, release notes, country targeting
- `mcp.json`: declared miniOrange MCP endpoint

## Remaining steps before public submission

1. **Official miniOrange logo included.** `assets/miniorange-logo.png` is bundled and referenced as both listing and composer icons.
2. **MCP transport/authentication NOT verified in this environment.** The draft config uses streamable HTTP for `https://joomla.mcp.miniorange.ai/mcp` URL. the developer must check that the real server supports this transport and that OAuth works from the submission portal. Do not submit with an incorrect transport.
3. **No reviewer credentials are bundled.** Use the secure portal reviewer-access fields for the independently accessible Joomla administrator sign-in URL and a rotated test account password.
4. **Demo playback URL** is included in `plugin.json` as provided. External viewing and any OAuth-code redaction have not been independently confirmed.
5. **Website URL** is the miniOrange homepage as requested. The portal may require the dedicated public plugin page `https://plugins.miniorange.com/joomla-ai-assistant` instead; confirm before finalizing.
6. **Trademark/title:** Open Source Matters Joomla trademark guidance should be reviewed for the OpenAI listing before publishing.
7. **Category** is Business & Operations as configured in the public portal.
8. **MCP tool annotations** `readOnlyHint`, `destructiveHint`, `idempotentHint`, and `openWorldHint` must be verified server-side.
9. Run all review cases against the exact saved public draft, resolve scans/attestations, and submit only after approval of listing content.

## Security

This package contains no OAuth tokens, passwords, private app IDs, or reviewer login instructions. It is not payment-enabled and does not claim permission for destructive operations or marketing email campaigns.
