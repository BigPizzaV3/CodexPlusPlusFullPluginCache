---
name: turrior-manage-candidate
description: Change a candidate's hiring status, add a note, or add a talent to the Turrior shortlist.
---

Use this skill when the user asks to move, reject, hire, hold, shortlist, or add a note to a candidate.

1. If the candidate was provided by name, resolve and confirm them first using the candidate-resolution workflow.
2. Use IDs according to their exact meaning:
   - funnel change → application/interaction ID
   - candidate note → interaction ID
   - shortlist → `talent.id`
3. Do not use raw invitations with `change-candidates-status` or `add-candidate-note`.
4. For status changes, call `change-candidates-status` with the resolved application IDs and requested target status.
5. Check the result for partial transition failures and report them clearly.
6. For notes, call `add-candidate-note`.
7. For shortlist requests, call `add-to-shortlist`.
8. Never report an action as completed unless the corresponding MCP action succeeded.
