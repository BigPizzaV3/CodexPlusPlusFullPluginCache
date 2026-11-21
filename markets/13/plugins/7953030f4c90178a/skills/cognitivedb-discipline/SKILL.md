---
name: cognitivedb-discipline
description: >-
  Resolve the connection and Space in each conversation for CognitiveDB operations
  that require Space context.
metadata:
  version: "dev-1.0.1-chatgpt.1"
---

# CognitiveDB Discipline

Keep the selected connection, Space ID, Space name, and organization in the
conversation context. Resume the user's task once the target is resolved.

## Core Instructions

For an own-profile or Space-list-only request, use `cognitivedb_user_current_get`
or `cognitivedb_space_list` through the intended connection without selecting a
Space. Apply the following Space-selection rules only to dependent operations
whose live Tool contract requires Space context.

1. For a Space-scoped task, honor an explicit user target; otherwise reuse this
   conversation's selected Space. When unresolved, call `cognitivedb_space_list`
   through the intended connection.
   Use the returned `project_id` as `space_id`.

2. When user selection is needed, present the candidates through GenUI.
   Highlight each Space's organization alongside its name; group candidates by
   organization when useful. Bind each selection to the actual Space ID and send
   that ID in the next user message. Match the reply to the current connection's
   candidates before continuing. Require selection even for a single candidate.
   A list-only request finishes with the list.

3. Use the selected Space for dependent operations. Resolve again when the user
   changes the target or connection, then resolve Catalogs, Computes, and other
   resources within that Space.

4. Supply an explicit `space_id` and connection whenever assigning Space-related
   work to a child conversation or Agent. The parent conversation resolves the
   target and manages the children. Children use the supplied target; if missing,
   request it from the parent.

5. After each Space-related task, report the Space name, Space ID, and organization.
