# nDot Physics Research

Public-upload preparation, 14 October 2026. Package ndot-physics-research, version 1.0.0.

## Connection

The package connects directly to https://physics.ndot.io/mcp with explicit auth.type="none" from the initial upload. It contains no private App binding, credentials or OAuth client configuration. The direct research endpoint is hosted by the publisher at Hostinger. The separate Sites presentation website remains the listing website.

The existing original public draft is retained for support case 17180668. The earlier ndot-physics-noauth-check test draft was deleted by the publisher. This package is intended for a new public draft, not a replacement of the original saved connection.

## Included

English default listing, German and Hungarian translations, nDot monogram icon, three starter prompts, five positive and three negative review cases, existing demo recording, publisher and support details, and country targeting without restrictions. The research tools remain read-only and do not execute retrieved code. The demo demonstrates the research workflows; it predates migration of the MCP hosting endpoint.

## Independent verification

Anonymous modern discovery, 16-tool listing, listTopics, listCode, reference document and equation retrieval passed. A 209214-byte output file was read completely in three parts. Legacy initialization, notification, tool listing, listTopics and session deletion also passed. The live tools match OpenAPI 1.5.0 input schemas and annotations. These HTTP checks do not replace the portal's tool scan or ChatGPT review-case tests. Details are in development-checks.json.

Code-file pagination ends when next_offset is null. The truncated flag may remain true on the last part because that response still represents only part of the original file. Code-version arguments are strings such as v1; derive them from the supplied code links where a listing gives the numeric component 1.

## Remaining preparation and portal steps

1. Publish the supplied updated English, German and Hungarian legal Markdown at the existing physics.ndot.io/plugin/support, /plugin/privacy and /plugin/terms pages and their existing translated routes. The current canonical privacy page still describes the old infrastructure. The new notice discloses Hostinger hosting, short-lived hashed rate counters and legacy session metadata. Exact infrastructure-log contents and retention remain unverified by the publisher.
2. Upload this ZIP as a new draft under the verified publisher. Confirm the name nDot Physics Research, imported metadata and No authentication mode.
3. Obtain the domain-verification token for physics.ndot.io from that draft and have the backend serve its exact text at /.well-known/openai-apps-challenge. Do not reuse the old Sites token.
4. Run the portal scan, connection flow and all eight saved-version review cases. Their current status is Not run. The publisher must complete the portal attestations before requesting review.

This archive has not been uploaded, submitted for review or published. Successful protocol checks do not guarantee portal acceptance or review approval. Existing business verification must be selected and confirmed in the portal.
