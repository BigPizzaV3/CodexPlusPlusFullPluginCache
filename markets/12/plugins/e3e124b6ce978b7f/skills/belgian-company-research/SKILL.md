---
name: belgian-company-research
description: Answer questions about Belgian companies (how a company is doing, its figures over the years, its health, administrators, Staatsblad publications, or which companies in a sector and place) from their filed annual accounts with the bedrijfscijfers tools.
---

Use the bedrijfscijfers tools whenever the person asks about a Belgian company or a group of Belgian companies.

1. **Find the company first.** With a name, call `find_company` and pick the right candidate by name, place and activity; ask when two candidates fit equally well. With an enterprise number (ten digits, "0400.378.485" or "BE0400378485"), go straight to the other tools.
2. **One call per company where you can.** `get_company` gives the profile, latest figures, health score and sector rank. Add `include` (financials, health, publications, network) to get more in the same call instead of calling several tools about the same company.
3. **Several years:** `get_financials`. **The ratios behind the health score:** `get_health`. **Staatsblad publications:** `get_publications`. **Administrators and shareholders:** `get_network`.
4. **Groups of companies:** find the sector code with `lookup_sector`, then `search_companies` with the sector, a place or province and size ranges. It lists up to 20, the largest first, with the total number that match.

When you answer:

- Figures are in euro, as filed. Small companies file an abridged model without turnover; then gross margin is the size measure, so say which one you use.
- Name the financial year the figures are from.
- Link every company you name to its `url`.
- The health score is an indication based on the filed accounts, not a credit rating. Say so when you use it in a judgement.
- When a tool says a daily limit is reached or a plan is needed, tell the person what it says; don't retry.
