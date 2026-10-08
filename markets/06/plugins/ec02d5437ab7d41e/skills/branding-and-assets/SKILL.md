---
name: branding-and-assets
description: Create unique plugin logos, composer icons, favicons, and supporting brand assets.
---

Generate a distinct square PNG for every converted plugin unless the user explicitly requests supplied branding. Never reuse a previous plugin's logo or composer icon by filename, copy, or visual design. Derive a new asset identity from the plugin name and purpose, record its SHA-256 hashes in the build manifest, and verify that logo and composer-icon hashes differ from the previous plugin's assets.

Ensure the asset is usable at directory and composer sizes, has no accidental text or third-party marks, and is referenced by both `interface.logo` and `interface.composerIcon`. Create favicon or alternate-size assets only when useful. Check dimensions, file format, square geometry, transparency, and hashes before packaging. If image generation or local asset writing needs permission, request it once and resume from the branding checkpoint.
