---
name: banner-studio
description: Design wide banner concepts with Banner Studio. Use for the studio media workflow.
---

Use `banner_studio_generate` for the requested edit or design. Pass actual attachments or supplied reference URLs; never invent attachment IDs. Portrait Studio requires a real portrait reference. Banner Studio produces wide 16:9 concepts.

Wait for synchronous completion and show the actual inline result card. If the user wants to compare or refine in the workspace, use `banner_studio_open`, passing their actual reference image when available. The workspace has controls specific to this studio, image comparison, Download and Use in chat. Existing outputs can be reopened with `banner_studio_preview` using their actual saved ID or returned URL.

Do not automatically retry uncertain generation or fabricate output. Report unavailable tools and failures accurately. Firemoon and its media provider process inputs and save link-accessible outputs. Inspect generated details before use; do not guarantee exact likeness or lettering.

## Guest access and optional account linking

Start by calling the workflow tools directly. Do not request account linking before using the anonymous daily image/video allowance. Guests share 100 image/video outputs per host guest identity per UTC day; each image variation counts separately. Only offer account linking when the tool returns an authentication challenge or the user explicitly wants to use account credits. Never invent a guest identifier or bypass a quota response. Preserve existing attachment requirements and uncertain-job retry safeguards. Account linking accesses existing account entitlements. Do not list plans or credit packs, promote digital upgrades, or create checkout links in the plugin.
