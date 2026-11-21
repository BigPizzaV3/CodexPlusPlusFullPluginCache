---
name: heffl-settings
description: "Inspect or change Heffl pipelines, stages, tags, sources, lost reasons, tax rates and field-service zones using the workspace configuration tools."
---

# Workspace configuration

Read ../heffl-crm/references/operating-rules.md before mutations. Use heffl_search_actions and actual schemas to choose tools. Available domains include pipelines and pipelines_stages, tags, sources, lostReasons, taxRates and zones. Their list/details/create/update/delete and supported reorder actions apply to the connected workspace.

Read current configuration before changing it. Reuse returned IDs, clarify ambiguous names and preserve unrelated settings. For stage changes inspect the pipeline and stage type; stage configuration can affect deal lifecycle and required fields. A request to move one deal should use records_update with stageId, not rewrite the stage definition. Preserve rates and currency/tax meanings and do not infer a percentage unit without the schema. Explain deletion or broad configuration effects, validate with heffl_validate_action, and follow existing user authorization and client confirmation policy.

The MCP surface does not expose automation draft/approve/publish tools or context remember/forget actions. Do not fabricate those tools or expose internal actions. For automation setup direct the user to Heffl Automations → Add automation, describing the requested trigger, steps and integrations as an editable plan. Do not claim it has been created or activated.
