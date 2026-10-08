---
name: prompt-refinement
description: Diagnose and improve an existing prompt without changing its purpose.
---

# Prompt Refinement

Apply when the user supplies a prompt to improve or troubleshoot.

1. Preserve the user's task, audience, voice, constraints, and required output unless asked to change them.
2. Identify ambiguity, conflicting instructions, missing context, excessive scope, untestable goals, and unsupported capability assumptions.
3. Produce the revised prompt. Summarize material edits and explain any unresolved trade-off.
4. If examples or failures are supplied, tie each proposed change to the observed issue; do not claim a root cause beyond the evidence.
5. Prefer minimal, testable changes over wholesale rewrites. Offer an alternate version only when there is a genuine design choice.

Do not add hidden persuasion, impersonation, coercion, undisclosed data collection, jailbreaks, or instructions to override applicable safeguards. Do not reproduce proprietary prompts obtained without authorization.
