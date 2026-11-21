# Workflow authoring

## Discover and choose the entry point

Use list_node_types for configurationSchema, defaults, branchesAtDefaults, providedContext, lineAssignable and node requires. Use list_templates and list_connections when relevant. The available contracts determine the actual configuration; examples below are not substitutes for discovery.

| Trigger | Intended entry point |
| --- | --- |
| MANUAL | Explicit run of an enabled saved workflow. |
| CRON | Scheduled execution; confirm the intended timezone and validate the expression. |
| WEBHOOK | Incoming webhook; configure its protected URL and secret in Chatigram. |
| HTTP_ENDPOINT | Incoming HTTP request; use supported response nodes for the response. Manage endpoint authentication in Chatigram. |
| DATABASE_OPERATION | Selected record operations on the actual database/table and column schema. |
| CONVERSATION_CREATED | Creation of a conversation on an eligible Line. |
| CONVERSATION_START | New chat or configured target-text match; enable a supported condition. |
| NEW_EXTERNAL_TEXT_CHAT_MESSAGE | Matching inbound text. |
| CONVERSATION_STATUS_CHANGE | A conversation status transition; resolve the actual status ID. |
| NODE_TYPE_START | Entry point for a reusable Node Type definition only. |

A conversation node requires conversation context; do not put it under an incompatible trigger. Event-triggered workflows need their real event. Do not invent a scheduled event or webhook payload to call execute_workflow.

## Draft, preview and save

Use begin_draft with a fresh UUID draftId and one source: workflowId to edit, duplicateWorkflowId to copy within the organization, a supported portable document, templateId or a new name. Retain the returned draft ID and revision. Drafts expire after 24 hours. New workflows are disabled.

Use add_node, configure_node, rename_node, connect_branch, remove_node, rename_workflow and update_settings as supported. Send the latest revision on each mutation. Changing a trigger starts from that trigger's defaults. For protected connection fields, select a real connection and use bind_connection; do not put credentials into configuration. Preserve protected fields and bindings unless the user explicitly requests a supported change.

Use set_goto with parentId, branchIndex and toNodeId to loop or converge to an existing node. Omit parentId for the trigger; omit toNodeId to return to Start. remove_goto clears the source link. These links do not move their target nodes. Keep branches free of conflicting edges or links.

preview_draft provides configured variableNames, validation, changes and setup requirements. Review the same revision before save_draft. Honor the requested disabled/assignment state. After a timeout, inspect_draft with the same ID before retrying. On a revision conflict, read the current resource and reconcile rather than replaying old edits blindly. Use list_history and restore_draft for an authorized restore, followed by preview and save.

Only use set_activation or execute_workflow when the user requests the corresponding effect. Direct execution supports enabled MANUAL workflows. Use a fresh requestId for each intended run; reuse it with the same savedRevision after timeout. Confirm the actual returned runId through execution_status. cancel_execution stops the selected run, not the workflow or conversation; completed external effects cannot be undone. node_diagnostics provides safe failure details. Report fixed errors without exposing raw service responses or secrets.

Use run_scheduled_once only for an explicitly requested run of a saved enabled CRON workflow after inspecting its downstream effects. It preserves the saved trigger, schedule, activation and revision. It does not fabricate conversation, database, webhook or HTTP event context. Keep its exact requestId/revision after an uncertain response.

Before changing a trigger, resource schema, output contract, node name/removal or Property, use workflow_dependencies and inspect the exact affected paths. Structured Variable.name and StringComparison.variable references are checked, including protected fields without disclosing values. Node rename updates structured references atomically. Trigger conversion can supply variableRemapping from removed names to valid existing inputs; never replace missing event values with empty strings or invented events. Literal/provider-specific templates are not covered by this analysis. Review those separately before claiming completeness.

Readable configuration is classified by field. Redacted fields, omitted values, null and empty values are distinct. Preserve opaque account references by editing the owned draft narrowly. HTTP/Signed API request patches preserve signing and protected headers. Only classified public headers and non-secret fields are editable. Existing destination edits stay on the same static origin; dynamic destinations, credential-bearing fields and changes of origin require secure setup. Never reconstruct a whole request from a partial read.

Use execution_status for recorded terminal reason and step count; unavailable historical telemetry is not evidence of a guessed timeout. The current engine has a 1000-step guard per execution segment; it is not a documented wall-clock timeout. Use finite loop budgets and advance independent stages when a budget is exhausted. execution_outputs requires explicit selected keys and returns only classified bounded outputs; provider bodies remain unavailable. HTTP failures retain existing error branches and strings while adding classified status, known error codes and bounded validation paths. A generic 409 or missing local receipt does not prove rejection: reconcile before replay or replacement.

## Expressions and portable workflows

Read actual variable names from read_workflow or preview_draft. A constant expression uses [{"$tag":"Constant","value":"Example"}]; a variable expression uses [{"$tag":"Variable","name":"actual.variable.name"}]. Do not invent output names.

For imports, use a complete chatigram-workflow version 1 document. Keep metadata, workflow settings, trigger, properties, nodes and gotos. Each node needs a unique UUID, name, parentId, branchIndex, type and data matching its discovered contract. A null parent attaches to the trigger. Review destination resource IDs and connections explicitly. Do not rebuild a protected copy from redacted read_workflow output; use duplicateWorkflowId instead.

## Properties and reusable Node Types

Use read_properties on a draft or the corresponding saved read tool for Property IDs, labels, help, required flags, values and canonical references. Properties are public TEXT inputs and must not contain credentials. Use add_property, update_property, remove_property and reorder_properties with the latest draft revision. Use the exact workflow.PROPERTY_UUID reference returned by read/preview. Referenced Properties cannot be removed without resolving their uses. Ordinary Set Variable output references use NodeName.default.

For a requested reusable Node Type, resolve the owned definition with list_custom_node_types/read_custom_node_type and use begin_node_type_draft. Definition Properties are per-instance text inputs with empty definition values; nesting is unsupported. Reuse graph, Property, preview and save tools, review affectedInstances/saveAllowed and preserve existing consumers. After saving, refresh list_node_types and use the returned type, input IDs and output references; do not invent them or silently rewrite consumers.
