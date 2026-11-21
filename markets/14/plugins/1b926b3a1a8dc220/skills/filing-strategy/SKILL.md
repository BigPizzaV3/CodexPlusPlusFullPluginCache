---
name: filing-strategy
description: Use when a user wants to protect a trademark, patent or design in several countries - choosing between national filings, Madrid, Hague, PCT and regional systems, using the priority period, and laying out a country-by-country plan with deadlines. Uses the IPRwise connector.
---

# International filing plan

This skill gives the method for turning "we want protection in these countries" into a filing plan. The IPRwise connector supplies treaty memberships and country rules with their sources; this skill says how to combine them.

## If the connector is not connected

If the IPRwise tools (`filing_routes`, `country_ip_facts`, `nice_2027_check`, `ip_news`) are not available, ask the user to connect IPRwise in the app's settings and sign in with an IPRwise account. Without it, mark every membership and rule in the plan as unverified.

## Workflow

1. **Collect the facts.** The right; the first filing (country, date, number) or the home registration; the target countries; for trademarks the classes and specification; the business timeline; budget limits. Ask only for what is missing.
2. **Routes in one call.** Call `filing_routes` once with all target countries and the home country. Build a table: country, Paris, Madrid / Hague / PCT, regional option, note. A Madrid or Hague filing also needs the applicant to be connected to a member: a national of, domiciled in, or with an establishment in a contracting party (often the home country).
3. **Priority.** From the first filing date, calculate the Paris Convention priority deadline (Art. 4C): 12 months for patents and utility models, 6 months for trademarks and industrial designs. Show the calculation. If the deadline has passed, say so: later filings stand on their own dates.
4. **Choose the route for each country and give the reason.**
   - Trademarks: Madrid where both the applicant's office and the target are members; a national filing where the target is not a Madrid member or needs a local strategy; one EU trade mark for all 27 EU states; OAPI as the only route for its member states. Under Madrid the international registration depends on the basic mark for five years (Madrid Protocol Art. 6(3)): mention this when the basic mark is still exposed to refusal or opposition.
   - Patents: PCT to keep many countries open and defer costs; the EPO for Europe, including extension and validation states; EAPO for its member states; ARIPO (Harare Protocol) for its members. National phase deadlines differ by office: confirm each one.
   - Designs: Hague where the target is a member; otherwise a national or regional filing (EU design, OAPI).
5. **Country rules.** Call `country_ip_facts` for each target country. Flag early: a required local agent, power of attorney formalities (legalisation can take weeks), the filing language and translations, opposition periods.
6. **Classification.** For trademark specifications filed on or after 1 January 2027, run the terms through `nice_2027_check` and propose the new wording where a term was reworded, deleted or moved.
7. **Recent changes.** Call `ip_news` for the main target offices and WIPO. Mention items that affect the plan, such as fee changes or treaty accessions, with their effective dates.
8. **Deliver the plan.** A table with country, route, priority deadline, local agent needed, power of attorney formality, key note and source links; then a dated timeline and next steps. To instruct local attorneys, use the foreign-associate skill and `find_attorneys`.

## Rules

- Do not quote fees: the tools do not return them. Ask the local attorneys for estimates.
- Every country rule in the plan cites the source link `country_ip_facts` returned. No rule from memory.
- Membership dates matter: a country whose accession is "not yet in force" cannot be designated before that date.
- This is reference information, not legal advice; the user confirms the plan with counsel before filing.
