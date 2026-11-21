---
name: portrait-studio
description: Restyle portrait backgrounds with Portrait Studio. Use for the studio media workflow.
---

Use `portrait_studio_generate` for the requested edit or design. Pass actual attachments or supplied reference URLs; never invent attachment IDs. Portrait Studio requires a real portrait reference. Banner Studio produces wide 16:9 concepts.

Wait for synchronous completion and show the actual inline result card. If the user wants to compare or refine in the workspace, use `portrait_studio_open`, passing their actual reference image when available. The workspace has controls specific to this studio, image comparison, Download and Use in chat. Existing outputs can be reopened with `portrait_studio_preview` using their actual saved ID or returned URL.

Do not automatically retry uncertain generation or fabricate output. Report unavailable tools and failures accurately. Firemoon and its media provider process inputs and save link-accessible outputs. Inspect generated details before use; do not guarantee exact likeness or lettering.
