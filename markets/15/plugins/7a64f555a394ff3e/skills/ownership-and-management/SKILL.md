---
name: ownership-and-management
description: Show who runs and who owns a company - managing directors, board, shareholders, ultimate beneficial owners, group structure and related companies. Use for "who owns", "shareholders", "UBO", "group structure", "managing director", "Geschäftsführer", "Gesellschafter", "wirtschaftlich Berechtigte", "Konzern".
---

Use this skill when the user asks about management, ownership, beneficial owners or the network of a company.

## Workflow

1. Resolve the company with `search_company` (ask when several results fit).
2. Choose sections by question:
   - Managing directors, board, historical roles: `management`.
   - Direct owners with ownership percentage: `shareholders`.
   - Beneficial owners and multi-level structure: `ownership_tree` (`ownership_depth` 1 to 5, default 3).
   - Related companies and people: `network` (`network_depth` 1 to 3, default 1).
3. Present people with name, role and start date as recorded. Present owners with ownership percentage when on record. For trees, show the chain from the company up to the beneficial owners.
4. Report the returned relationship types and dates. Label entries explicitly marked `ai_generated: true` as AI-generated; do not infer official-register status or request internal source/confidence fields that the tools do not expose.

## Personal data

- Show people only in their role at the company, as recorded in the register.
- Do not search for, combine or infer private information about individuals such as home addresses, private phone numbers, family relations, health or financial situation. Decline such requests and offer the company-related information instead.

## Boundaries

- Do not invent owners, percentages or roles. If the data is `not_present` or `not_loaded`, say so.
- Answer in the user's language. Explicit user instructions take priority over this skill.
