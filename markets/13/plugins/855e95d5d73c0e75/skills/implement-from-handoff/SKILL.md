---
name: implement-from-handoff
description: Implement a feature in the open repository from a published Rivora handoff. Use when the user names a Rivora feature, product, handoff id, or version pin, or asks to build from Rivora.
---

# Implement from a Rivora handoff

Rivora is the source of the approved feature pack. The open repository is the code to change. Read the handoff through the Rivora MCP server, then implement only what that pinned version says.

## Before changing code

1. Resolve one handoff.
   - If the user gives a handoff id or version pin, call `get_handoff`.
   - Otherwise call `find_handoffs` with the feature name and, when known, the product name. Use the single latest match. If several matches remain, ask which one to use.
2. Read the sections this change needs with `get_handoff_section`. Prefer, in this order, the ones that exist on the handoff:
   - `cursor_coding_agent_handoff`
   - `implementation_handoff`
   - `frontend_ux_specification`
   - `backend_platform_specification`
   - `data_and_memory_specification`
   - `jira_delivery_mapping`
   - `current_product_impact_map`
   - `architecture_module_impact_map`
   - `feature_intent_and_problem_framing`
   - `executive_summary`
3. Call `list_handoff_open_questions`. Treat unresolved questions as scope you must not invent past.
4. Call `list_handoff_citations` when a requirement needs its source. Use `search_handoff_evidence` only to search evidence frozen in that same handoff.
5. Tell the user the `version_pin` and `content_hash` from `get_handoff` before editing files.

## While implementing

- Follow the pinned handoff. A later change in the live Feature Pack is a different version.
- Keep draft or unapproved material out of the implementation. The published handoff is the approved bundle.
- Stay inside the open repository. Do not edit Rivora Product OS, its approved sections, or another product's code.
- When an open question blocks a decision, stop and ask the user. Do not fill the gap with a guess.

## Sending a proposal back

Call `propose_handoff_changes` only when the user explicitly asks to send a proposal to Rivora. If their Rivora sign-in did not include proposal access, the tool returns a permission error. Stop there and tell them Rivora did not grant proposal submission for this login. A successful call records a proposal for a person to review. It does not change the approved handoff.
