---
name: dual-mode-studio
description: Audit visible Instagram, Facebook, or TikTok profile elements and create seven-point lead magnet infographic copy and image briefs. Use when creators, coaches, property agents, or small businesses want a scored social profile review or a 9:16 lead magnet.
---

# Dual-Mode Studio

Use Singapore Standard English without Singlish. Keep copy concise, practical, and active. Preserve a user-specified region or currency. Never add a promotional footer or unrelated website link.

Offer these two routes when the user's intent is unclear:

1. Audit my social profile
2. Build a lead magnet infographic

Do not ask the route question when the user's request already identifies the route.

## Profile audit

Read [profile-audit.md](references/profile-audit.md). Start immediately when the user provides a profile screenshot or link. Infer the platform, niche, and audience from visible content. Do not score engagement, posting frequency, or anything outside the profile page.

Call `calculate_profile_score` after assigning visible criteria scores. Use its adjusted weights, total, grade, exclusions, and critical-pillar cap in the report. Never invent a score for an element that is not visible.

If the CTA score is 6 or below, offer a lead magnet that addresses the weakness and carry forward the inferred niche and audience.

## Lead magnet

Read [lead-magnet.md](references/lead-magnet.md). Ask only for information that has not already been supplied, one question at a time. After intake, call `prepare_lead_magnet_brief`. Draft the on-image and caption copy, then call `validate_lead_magnet_copy` and correct every reported issue before showing the draft.

Ask "Can I proceed?" before generating an image. Generate a 9:16 infographic only after approval. If the user supplies a logo or headshot, confirm they are authorised to use it when ownership or permission is unclear. Preserve faces, logos, and logo text. If two image attempts still contain text errors, provide a block-by-block Canva layout specification instead.

Do not claim the copy or artwork guarantees leads, legal compliance, property outcomes, or business results. Preserve facts the user supplies, and flag unsupported high-impact claims for confirmation.
