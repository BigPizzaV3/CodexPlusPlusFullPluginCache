---
name: draft-epk
description: "Get an audience-specific EPK outline (booking, press, brand, festival, or general) from the Artispreneur get_epk_outline tool when connected, then draft from artist-supplied facts only; otherwise use the create-an-epk skill. Use when an artist needs a press kit structure."
metadata:
  author: Artispreneur
  version: "2.0.0"
  website: https://www.artispreneur.com
---

# Draft an EPK Outline

1. Confirm the audience: general, booking, partnerships, festival, or release campaign.
2. If `get_epk_outline` is available, call it with that audience and walk through the section order, required content, call to action, storyline beats, and bio word targets. Otherwise run `create-an-epk`.
3. Fill the scaffold with only facts the artist supplies. Keep `[CONFIRM]` placeholders where facts are missing; ask rather than invent.
4. Never invent shows, draw numbers, press quotes, or partnerships. For the full build and claim check, run `create-an-epk`.

## Quality checks (run before handing over)

- [ ] Only the target `audience` enum (`general`, `booking`, `partnerships`, `festival`, or `release_campaign`) was sent to `get_epk_outline`.
- [ ] Every section uses only user-supplied facts or `[CONFIRM]` placeholders.
- [ ] Zero shows, press quotes, streaming numbers, or partnerships were invented.

## Guardrails

- Send only the `audience` field to `get_epk_outline`. Never send personal data, credentials, full chat history, or location data.
- `get_epk_outline` is strictly read-only (`readOnlyHint: true`, `destructiveHint: false`, `openWorldHint: false`) and operates independently without invoking external plugins.
- Never invent shows, draw numbers, press quotes, or partnerships. Mark missing facts `[CONFIRM]`.
- Never collect, solicit, or process Restricted Data (PCI DSS payment cards, PHI, government IDs such as SSN/ITIN/EIN, or passwords/API keys/MFA codes) or precise location data (street addresses or GPS coordinates).

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
