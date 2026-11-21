# Tool annotation review — 5 November 2026

The rejection email identifies annotations inconsistent with behaviour but does not name a tool. Code inspection identified the persistent public schematic as incorrectly marked read-only. All four hints were already explicit booleans; this release corrects their semantics.

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint | Justification |
|---|---|---|---|---|---|
| search_railtours | true | false | true | true | Retrieves indexed public railway sources; no user data changes. Public-source corpus is open-world despite local caching. |
| read_source | true | false | true | true | Retrieves approved public HTML/PDF sources, with internal retrieval caching; no edits to source or user records. Repeated reads have no additional user-facing side effects. |
| view_source_image | true | false | true | true | Downloads a public source image and computes an in-memory preview; does not publish an artifact. |
| find_reference_sources | true | false | true | true | Retrieves public publisher catalogues and links, with internal caching; no user-facing writes. |
| draw_route_schematic | false | true | false | true | Persists a publicly accessible PNG. os.replace can overwrite an existing artifact, so destructiveHint is conservatively true. Source refresh can change the content hash and create another URL for the same arguments, so idempotentHint is false. Reads public sources and publishes a public URL. |
| research_guidance | true | false | true | false | Reads bundled method text, a fixed source directory and local coverage counts. Does not fetch linked websites or publish artifacts. |

Internal source caches support retrieval and are not user-created artifacts. Guidance's returned external links do not themselves access the internet.

Reference: https://developers.openai.com/plugins/plugin-guidelines
The current guidelines say justifications are no longer required, but this document supplies them because the rejection explicitly requested them.

Resubmission: upload version 1.0.2, rescan the live MCP tools, check the four boolean hints against this table, and include this explanation in the review notes. Approval remains a reviewer decision.
