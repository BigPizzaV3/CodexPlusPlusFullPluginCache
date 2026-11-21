---
name: facebook-research
description: Read public Facebook pages for businesses, brands, creators and public figures with HasData. Use for page information and counters, not personal dossiers, private accounts, groups or a separate comments API.
---

# Read public Facebook page information

Read `../hasdata-research/SKILL.md` and the Social and video section of `../hasdata-research/references/tool-catalog.md`.

Use `hasdata_facebook_profile_getFacebookProfile` with a genuine handle or returned page ID for the requested public business, brand, creator or public-figure page. Do not derive an ID from a display name or use a personal profile.php?id= URL to investigate a private individual. Ask for the public page URL/handle if the intended page is ambiguous.

Return requested public description, category, links, counters or content only where present. Preserve the returned wording of localized counters rather than inventing exact numbers. The catalog has a profile tool, not a separate Facebook comments or posts tool; do not guess one.

No groups or private personal-account access, login cookies, messages or edits. A failed/missing public response is not permission for an automatic paid generic-scraping fallback. State the limitation and preserve source context.
