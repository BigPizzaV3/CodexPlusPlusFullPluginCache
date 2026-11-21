# Voico plugin v0.3.0 — change log and publishing checklist

## Updated
- Version: `0.2.0` → `0.3.0`.
- Icon: replaced `assets/voico-icon.png` with the user-supplied 140×140 Voico favicon. Both logo and composerIcon point to it.
- Website: `https://www.voico.ai/`.
- Support contact: `support@voico.ai`.
- Support URL: `https://www.voico.ai/impressum` (public company contact page; publisher should confirm acceptance).
- Privacy: `https://www.voico.ai/datenschutz` (unchanged).
- Terms: `https://www.voico.ai/agb` (unchanged).
- MCP: `https://mcp.voico.ai/mcp` (unchanged).

## Findings in supplied screenshot
1. Website URL required — now populated.
2. Support URL required — now populated with public contact page; confirm portal accepts it.
3. Remove pricing/subscription/temporary promotion language from listing description — reviewed: current long description contains none of these offers; references to subscription-dependent availability are factual eligibility disclosures, not an offer. Portal may still flag them; if so revise wording in consultation with reviewer.
4. Privacy-policy automated assessment incomplete — not fixable from ZIP alone; publisher must review whether policy explicitly covers MCP/ChatGPT data handling and seek manual review or publish addendum.
5. MCP configuration incomplete — requires portal-side server connection, authentication, domain verification, tool scanning.
6. Review information needs attention — requires actual reviewer test account, credentials supplied securely in portal, and any requested recording.

## Publisher action required
- Upload new version ZIP, then check parsed website/support fields and icon preview.
- Verify MCP endpoint and authentication in the portal; never put access tokens in ZIP.
- Provide review test account, opt-in test call number, sample data and recording if required.
- Confirm website/support links, privacy and terms satisfy publication review.
- Re-run portal findings and only submit when blockers are cleared.

## Validation scope
JSON parsing, ZIP integrity, relative icon references and PNG readability checked locally. This does not certify OpenAI schema acceptance, live MCP availability, or approval.
