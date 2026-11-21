# Movitera plugin

Portable Agent Plugins package connecting ChatGPT and Codex to the existing Movitera remote MCP server.

## Connection

- Endpoint: https://api.movitera.com/mcp
- Transport: Streamable HTTP
- Authentication and workspace selection use Movitera OAuth.
- Available tools and data follow the connected account, enabled modules, connection scopes and permissions. Write operations additionally require authorization for that connection.

## Package

`plugin.json` contains identity, listing metadata, review scenarios and release notes. `mcp.json` retains the existing remote server configuration. The original official 512 × 512 Movitera PNG is included at `assets/logo.png` and used for the logo and composer icon. Source: https://movitera.com/icons/icon-512-v2.png (declared in the official web manifest).

## Review scenarios

The manifest contains five positive and three negative scenarios. They are expected behaviors, not assertions of passed tests. Prepare the stated synthetic fixtures before execution. In particular, the activity must be due on the real execution date in the workspace time zone; write cases require the write scope and authorization for the reviewer connection. Replace the issue-ID placeholder with the real ID returned by the preceding create case.

## Submission preparation

This archive is a preparation artifact, not a submitted or approved release. Missing or unverified listing, recording, commerce or publication information is deliberately not invented. The website, support/documentation page and current service/MCP privacy policy were verified publicly on 1 October 2026. The publisher-designated terms-of-service URL is https://movitera.com/terms-of-use. The root URL redirected to /pt-BR/terms-of-use and returned HTTP 404 when checked on 1 October 2026 and remains pending publication and content validation. The reviewer demo walkthrough recording is declared in `plugin.json` (`review.demo_recording_url`). Confirm intended publisher identity, country availability and commerce declarations before calling the submission ready. The inherited author/developer label Movitera does not attest verified publisher status.

Keep credentials and reviewer login instructions exclusively in secure review-access fields, never in this package. Verify the production tool catalog, annotations, OAuth/reviewer access and review-case results for the exact version under review. A partial recording does not establish complete test coverage.

A portal ZIP reupload replaces the bundle and resets attestations. Review the saved draft and field import behavior before any authorized replacement. Uploading a draft, submitting for review and publishing are separate actions.
