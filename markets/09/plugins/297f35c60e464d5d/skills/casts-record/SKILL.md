---
name: casts-record
version: 1.0.2
description: Use Record to discover, compare, and research entertainment-technology companies and profiles. Prefer the MCP tools for live index data and identify when authentication is required.
---
Use the Record MCP server for requests involving entertainment-technology companies, company profiles, comparisons, market landscapes, integrations, comparable public-sector awards, and related research.

When presenting company information, distinguish sourced facts returned by Record from analysis. Use the tool that matches the request: company discovery and shortlists use check_record; named-company presence uses lookup_company; full profiles use get_company; market-wide counts use market_landscape; named integrations or customers use works_with; public award evidence uses comparable_awards; index coverage uses index_stats.

If the MCP server requests authentication, direct the user through the service's normal OAuth/login flow rather than asking them to provide credentials in chat.
