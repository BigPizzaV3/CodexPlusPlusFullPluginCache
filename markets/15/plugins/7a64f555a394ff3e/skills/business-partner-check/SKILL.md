---
name: business-partner-check
description: Run a quick business partner check on a company - status, insolvency proceedings, sanctions list entries, crisis alerts, recent register changes and VAT ID validation. Use for "check this supplier", "KYB", "due diligence", "is the company insolvent", "sanctions", "Geschäftspartner prüfen", "UID prüfen", "Insolvenz".
---

Use this skill when the user wants to know whether a company is a sound, legitimate business partner.

## Workflow

1. Resolve the company with `search_company` (ask when several results fit).
2. Call `get_company` with `sections: ["overview", "alerts", "insolvency", "sanctions", "changes"]`. For `changes`, limit to the last 12 months with `changes_since` unless the user asks otherwise.
3. If the user provides a VAT ID or UID number, or the profile contains one, call `validate_vat` to confirm it is currently registered and compare the returned name and address with the profile.
4. Summarize as a short checklist:
   - Status (active, in liquidation, dissolved).
   - Insolvency proceedings on record.
   - Sanctions list entries (name, list, date) or "no entry on record".
   - Crisis alert yes or no.
   - Notable changes in the last 12 months (management, address, shareholders, capital).
   - VAT ID result, if checked.
5. End with the facts only. Say that the check reflects the data on record and is not legal advice.

## Boundaries

- A missing sanctions or insolvency entry means "none on record", not a guarantee.
- Do not make accusations beyond the recorded facts.
- Answer in the user's language. Explicit user instructions take priority over this skill.
