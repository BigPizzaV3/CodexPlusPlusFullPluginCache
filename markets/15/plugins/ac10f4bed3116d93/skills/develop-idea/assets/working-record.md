# Working record and checkpoint guide

Use this as coverage, not mandatory headings. A concise brief can be the record. Avoid duplicate summaries, empty fields or a full configuration panel on every response.

- **Objective and hard constraints:** retain the user's actual outcome, exclusions and changes.
- **Settings:** active profile, role overrides, mode/depth/challenge, pause cadence, and documentation/diagram on/off plus cadence. Distinguish defaults from explicit overrides so a profile switch does not erase custom choices.
- **Basis:** user-supplied facts, checked evidence with actual references, assumptions and unknowns.
- **Decisions:** stable IDs when helpful; choice, status, rationale, alternative and unresolved objection. Status is proposed, user-selected, deferred or rejected. Record supersession instead of silently overwriting the prior selected choice.
- **Current scope and next action:** preserve rejected work outside the implementation scope. State the next unfinished stage and material unanswered choice, not an invented background job.
- **Artifacts:** last issued document/diagram revision, what decision state each reflects, and current or stale status. An output never produced is “not produced,” not a fictitious R0/G0 file.

A compact visible checkpoint could read: `Paused after engineering. D2 remains proposed. R2 current; G1 stale after the offline scope change. Next: compare the conflict-policy options.` Include only fields the session actually needs. It must not claim approval, storage, background execution or completed checks.

A one-time “export session” request produces a self-contained text record containing relevant settings, evidence boundaries, current decisions, unresolved matters, artifact status and next step. Include the current document and diagram content when requested and available, or clearly label a stale artifact. Exported text can be pasted into another chat. Do not promise that another chat already has the original history.

## Diagram discipline

Keep diagram node IDs stable across revisions when the same concept survives. Label proposed versus selected choices in words, not only colors. If a change removes a feature, remove it from the active implementation path; an alternatives diagram may retain it only as rejected or deferred. Identify unreviewed dependencies and unknowns explicitly. The document and diagram must describe the same scope and status.

Unless the host is known to render Mermaid, supply a readable outline/table representing the same relationships. If a native document or canvas tool is available and authorized, use it only when it benefits the requested output and report whether the update succeeded. A failed or unavailable artifact action does not block providing the complete current text in chat.

For MCP-enabled checked records and exports, follow the [stateless backend guide](backend-guide.md). Use actual returned labels, state, `state_hash` and capsule JSON; retain the server graph's meaning, in which `choice` and `replaced by` edges are not implementation sequence or dependency. A chat-only fallback remains an unchecked draft. The service receives bounded fields and returns them without storing a session.
