---
name: company-check
description: Check a company registered in Denmark with SelskabsInfo. Resolve the name to a CVR number, fetch only the owners, management, accounts, risk or cases the user asks about, and report them with the register's caveats.
---

Use this skill when the user asks about a company registered in Denmark: who owns
or runs it, how it is doing, whether it is risky to deal with, or for a due
diligence or KYC summary. The user's own instructions take priority over these
steps.

1. If the user gives an 8-digit CVR number, use it. Otherwise call
   `search_companies` with the name. When several companies match, show the
   closest few (name, CVR number, city, company form) and ask which one is
   meant. Prefer an active company, status NORMAL, unless the user asks about a
   dissolved one.
2. Call `get_company` with only the sections the question needs; one call with
   several sections costs less than several section tools. For "who is behind
   it", call `get_ultimate_owners`.
3. Report what the tools returned:
   - Ownership percentages are bands, as the register reports them (for
     example 50-66.67 %). Never present them as exact figures.
   - Relay a "forbehold" field when a response has one.
   - A "warnings" entry means a section is not included in the user's
     SelskabsInfo account: say which section was left out. Do not name plans
     or prices, and do not suggest an upgrade.
   - A key ending in "_truncated" names the full count; quote that number.
   - Amounts are in DKK unless the response says otherwise. Give the fiscal
     year each figure belongs to.
4. Do not fill gaps from memory. If a tool returns no data for something, say
   that the register has none rather than guessing. People appear only in
   their registered company roles; do not look for private addresses or phone
   numbers.
