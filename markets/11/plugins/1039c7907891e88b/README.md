# Clipto

Read an individual shared Clipto transcript or every transcript in a selected shared collection, then create source-grounded summaries, answers, comparisons, and work outputs. Supports full share URLs and Clipto short links. This integration does not browse an entire private library, transcribe recordings, or modify or delete source content.

## Connection and authorization

The MCP endpoint remains `https://mcp.clipto.com/mcp`. The connection declares no authentication. Public transcript and collection share links can be read through Clipto tools without Clipto sign-in or OAuth. The skill follows actual tool and host access errors and does not bypass restrictions. This ZIP does not deploy the server, reset existing host connections, or grant access to private library content. No credentials are included.

## Tool workflow

- `get_shared_content`: pass a short link unchanged; inspect the response for transcript content or `shared_transcript_urls`.
- `get_shared_collection`: list members of a full collection share URL.
- `get_shared_transcript`: read a full individual share URL, including every distinct member returned by a collection.

A collection listing is not full transcript content. Retrieve every member, keep citations per recording, and disclose failures, truncation, and incomplete coverage. Follow continuation metadata only where the actual tools support it.

## Collection verification

During preparation, `https://www.clipto.com/s/x2sjak3D` returned three transcript URLs via `get_shared_content`. Each was successfully read with `get_shared_transcript`, returning 42, 70, and 185 sentence items respectively. This verifies the live resolution and member-retrieval path, not an end-to-end run of the newly packaged skill or the submission portal review cases. Collection membership may change.

## Package contents

- `plugin.json`: version 0.1.3, listing metadata, five positive and three negative review cases, existing demo URL, and release notes.
- `mcp.json`: existing endpoint and explicit no-authentication configuration.
- `skills/shared-transcript-workflows/SKILL.md`: authorization, short-link routing, complete collection reading, source attribution, and recovery rules.
- `assets/clipto-icon.png`: original icon.

## Submission checks still needed

Run review cases against the exact saved portal version without Clipto sign-in or OAuth. The existing demo URL is retained; its coverage of this updated access policy and collection reading has not been reverified. These public-share cases do not require reviewer account credentials. Server tool annotations must truthfully declare read-only, destructive, and open-world behavior for every tool; this ZIP cannot change hosted tool metadata. Existing installed plugins may retain older skills or connection metadata, so verify the published update in a new conversation. No backend or portal changes are made by this package.
