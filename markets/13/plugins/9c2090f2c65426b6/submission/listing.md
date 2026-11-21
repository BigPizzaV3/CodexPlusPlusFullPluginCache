# Submission listing draft

This draft assumes submission by the Singapore Department of Statistics or an authorized representative who can verify the SingStat domain and publisher identity.

- Plugin name: SingStat
- Category: Data
- Short description: Explore official Singapore statistics.
- Long description: Find SingStat data tables, inspect their metadata, and retrieve current official Singapore economic and social statistics. The plugin helps users select the right table and series, apply time filters, preserve units and footnotes, and clearly separate official values from AI-generated calculations or interpretation.
- Website: https://www.singstat.gov.sg/data-tools-services/singstat-mcp
- Support: https://www.singstat.gov.sg/who-we-are/contact-us-statistical-enquiries
- Privacy policy: https://www.singstat.gov.sg/data-tools-services/singstat-mcp/privacy-policy
- Terms: https://www.singstat.gov.sg/terms-of-use
- MCP URL type: Universal
- MCP URL: https://chatwithsandra.singstat.gov.sg/mcp
- Authentication: None
- Suggested availability: Select only countries and regions supported by the publisher's legal and support processes.

## Expected tool annotations

| Tool | `readOnlyHint` | `openWorldHint` | `destructiveHint` |
| --- | --- | --- | --- |
| `get_relevant_table_names` | `true` | `true` | `false` |
| `get_table_metadata` | `true` | `true` | `false` |
| `get_table_data` | `true` | `true` | `false` |
