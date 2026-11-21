---
name: oac-analytics-qa
description: Answer business and analytical questions with Oracle Analytics Cloud using the OAC MCP tools. Use when a user asks for totals, trends, comparisons, breakdowns, KPIs, filtering, aggregation, or other data questions that require discovering an OAC data source, inspecting metadata, executing Oracle Analytics Logical SQL, and explaining the returned results. Keep this workflow read-only and use Logical SQL as the default query path when the analytical context requires it.
---

# Oracle Analytics Cloud Analytics Q&A

## Configured instance

Use only the Oracle Analytics MCP connection attached to the selected configured instance. Ground requests in that instance's live tools, metadata, identifiers, and permissions. Do not fall back to the template example URL, a remembered demo account or catalog path, or another instance's connection. If no instance is configured, explain that a workspace administrator must configure one before this workflow can run.

Use the Oracle Analytics Cloud MCP server as the execution layer. Use the runtime-exposed tool schema as the source of truth for arguments, required fields, and return values. Raw MCP tool names are listed below; the host may normalize their identifiers.

## Workflow

1. Interpret the analytical question.
   - Preserve the user's requested measures, dimensions, filters, date range, comparison period, and level of detail.
   - Do not add business definitions or filters that the user did not request or that OAC metadata does not establish.

2. Resolve the data source.
   - If the relevant subject area or dataset is already known from current conversation context, reuse it.
   - Otherwise call `oracle_analytics-find_matching_datasources` with the user's analytical intent.
   - If multiple candidates are returned, use metadata to distinguish them when possible. Ask the user only when the available tools cannot resolve a material ambiguity.

3. Ground the query in metadata.
   - Call `oracle_analytics-describe_data` before composing a query when table or column structure is not already established by current OAC tool output.
   - Use only returned table, column, subject-area, dataset, and related metadata. Never fabricate names, relationships, data types, or business meanings.

4. Choose the query tool.
   - Use `oracle_analytics-execute_logical_sql` for standard analytical queries or when the user explicitly requests Oracle Analytics Logical SQL or when the requested analysis depends on Logical SQL semantics established by the available context.
   - Do not silently substitute one query language for the other when the distinction matters.
   
5. Execute the query.
   - Match the aggregation and grain to the user's question.
   - Avoid unnecessary detail or unbounded row retrieval when an aggregate answer satisfies the request.
   - If the query fails, revise it only from returned metadata or tool error information. Do not guess at schema changes.

6. Present the answer.
   - State the result clearly and concisely.
   - Identify material filters, date ranges, grouping, or assumptions that came from the request or tool output.
   - Distinguish returned data from interpretation. Do not present an interpretation as a field returned by OAC.
   - Report units and scale only when source metadata or an authoritative data dictionary explicitly establishes them. A column name containing "Rate" or "Ratio" does not establish a percentage. If units or scale are unknown, preserve the returned numeric value and state the limitation; do not append `%`, rescale the value, or use inferred units in charts or follow-ups.
   - If the data is incomplete or ambiguous, explain the limitation rather than filling gaps.

## MCP tools

- `oracle_analytics-find_matching_datasources`: Match a natural-language analytical question to relevant OAC data sources.
- `oracle_analytics-describe_data`: Retrieve table and column metadata for subject areas or datasets.
- `oracle_analytics-execute_oac_ansi_sql`: Execute OAC ANSI SQL when explicitly requested and supported by the live tool schema; otherwise use Logical SQL as the default.
- `oracle_analytics-execute_logical_sql`: Execute Oracle Analytics Logical SQL and return query results.

## Boundaries

- Keep this skill read-only. Do not invoke catalog mutation or permission-management tools as part of an analytical Q&A request.
- Do not claim a query succeeded until the MCP tool returns a successful result.
- Do not invent MCP parameters. Follow the live runtime schema.
- The Oracle Analytics Cloud MCP integration is in Preview; avoid promising behavior beyond the currently exposed tools.

## Example requests

- "Show revenue by region for Q2."
- "Which product categories grew the most year over year?"
- "Use Logical SQL to return monthly bookings by sales organization."
- "What is the average order value for enterprise customers this quarter?"
