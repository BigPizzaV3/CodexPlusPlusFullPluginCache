---
name: tl-create-workflow
description: Turn a sponsorship sourcing or outreach goal into ordered stages, entry criteria, and ThoughtLeaders data sources. Use to design a workflow, pipeline, acquisition funnel, or channel-sourcing stages.
---

# Workflow planning (MCP)

The current MCP tools do not create or update workflows. This skill can design a grounded plan, but must never claim it saved one in the ThoughtLeaders account.

## Workflow

1. Call tl_whoami, then tl_skill_track with skill="tl-create-workflow" and stage="started"; retain its run_id. Clarify the target brand or campaign, audience, geography, channel constraints, and desired outcome. Resolve a named brand with tl_brands_find.
2. Call tl_whoami and read tl://guide/tools to select suitable recommendation and search tools. Ground the entry stage using relevant recommender tools or bounded tl_db_es/tl_db_pg queries. Estimate cost before broad queries.
3. Propose an ordered funnel, for example Sourced → Qualified → Fit reviewed → Outreach ready. For every stage specify purpose, entry and exit rules, evidence required, and which available MCP operation can populate or inspect it.
4. Mark manual stages and unsupported account operations. The MCP cannot move channels between stages, create a workflow record, or send outreach.
5. Present the plan for the user to implement in the product or CLI. If asked to create it, explain that a workflow write tool is not available.

Before the final response, call tl_skill_track with skill="tl-create-workflow", stage="completed", the retained run_id, and outcome="completed", "no_results", "failed", or "cancelled". Never include user content, queries, or results in that tracking call.

