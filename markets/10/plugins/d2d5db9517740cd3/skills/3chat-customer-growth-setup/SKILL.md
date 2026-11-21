---
name: 3chat-customer-growth-setup
description: Guide first use of 3Chat Customer Growth or a user-requested setup review. Read the current workspace's historical Agent-publication and channel-connection milestones, then guide only the missing steps.
---

# Set Up 3Chat Customer Growth

When the host starts this onboarding workflow, call `get_3chat_workspace_readiness` once for the authenticated workspace. It only reads milestones; it cannot publish an Agent or connect a channel.

Read [startup-readiness.md](../3chat-customer-growth/references/startup-readiness.md) for the response rules and [guidance-links.md](../3chat-customer-growth/references/guidance-links.md) before presenting setup links.

- `READY`: briefly confirm that initial milestones were completed and suggest a concrete first customer task. Do not claim current availability.
- Both milestones missing: include the capability introduction and setup rationale, three text steps with a prominent named link below each applicable step, and a suggestion to improve the Agent later.
- One missing: show only that step and its applicable action link.
- Error: follow structured errors, not the missing-milestone guidance.

Use the exact URL from the matching action object. Present links for the user to choose; do not automatically navigate, claim a button/card was rendered, or change configuration. Rechecks, result reuse, and postponing setup follow the shared startup reference; never duplicate checks in the same assistant turn.
