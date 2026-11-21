---
name: oac-content-discovery
description: Discover and inspect Oracle Analytics Cloud content and data sources using the OAC MCP tools. Use when a user wants to find workbooks, folders, datasets, connections, subject areas, analyses, reports, dashboards, or scripts; determine which OAC data source can answer a natural-language question; or inspect tables and columns for a known dataset or subject area. Keep discovery read-only, return only tool-supported metadata, and use search, source matching, and metadata inspection in the smallest sequence needed to answer the request.
---

# Oracle Analytics Cloud Content Discovery

## Configured instance

Use only the Oracle Analytics MCP connection attached to the selected configured instance. Ground requests in that instance's live tools, metadata, identifiers, and permissions. Do not fall back to the template example URL, a remembered demo account or catalog path, or another instance's connection. If no instance is configured, explain that a workspace administrator must configure one before this workflow can run.

Use this skill to help users locate OAC content and understand available analytical data before querying or modifying anything. Use the runtime MCP schema as the source of truth for arguments and response fields.

## Choose the discovery path

1. For a named or described catalog object, call `oracle_analytics-search_catalog`.
   - Search the user's stated criteria without inventing catalog paths or object names.
   - The documented searchable object types include workbooks, folders, datasets, connections, subject areas, analyses, reports, dashboards, and scripts.
   - Return enough tool-provided context to distinguish similar matches.

2. For a business question where the user does not know the source, call `oracle_analytics-find_matching_datasources`.
   - Preserve the analytical intent of the user's question.
   - Explain source relevance only from information returned by the tool.
   - Do not infer unavailable measures, dimensions, relationships, or permissions.

3. For a known subject area or dataset, call `oracle_analytics-describe_data`.
   - Retrieve table and column metadata needed to understand its structure.
   - Do not fabricate columns, data types, joins, relationships, or business definitions.

4. Chain tools only when useful.
   - Search -> describe when the user first needs an object located and then wants its structure.
   - Match source -> describe when a natural-language question needs a suitable source and then schema grounding.
   - Stop once the user's discovery question is answered; do not execute SQL unless the request also asks for analysis.

## MCP tools

- `oracle_analytics-search_catalog`: Search catalog objects. This tool is experimental.
- `oracle_analytics-find_matching_datasources`: Match a natural-language question to relevant OAC data sources.
- `oracle_analytics-describe_data`: Retrieve table and column metadata for subject areas or datasets.

## Result handling

- Prefer a short ranked-by-relevance presentation only when the tool itself provides relevance information; otherwise present matches without inventing a ranking.
- Clearly distinguish exact matches from partial or ambiguous matches when the returned metadata supports that distinction.
- If no match is returned, say that no matching item was found under the supplied criteria. Do not manufacture a fallback object.
- Do not expose metadata that the MCP tool did not return.

## Boundaries

- Treat all discovery operations as read-only.
- Do not invoke catalog mutation, export, query execution, or ACL update tools unless the user's request extends beyond discovery and another applicable workflow governs the action.
- Do not invent MCP parameters. Use the host's live tool schema.
- `oracle_analytics-search_catalog` is experimental in the Oracle documentation, and the OAC MCP integration is in Preview.

## Example requests

- "Find the workforce planning workbook."
- "Which dataset should I use to answer a question about renewal revenue?"
- "What columns are available in the Sales subject area?"
- "Show me dashboards related to pipeline."
