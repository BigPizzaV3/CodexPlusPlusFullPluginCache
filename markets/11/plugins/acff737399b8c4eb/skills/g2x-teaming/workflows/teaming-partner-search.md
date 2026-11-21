# Teaming partner search

Goal: a defensible partner shortlist for one pursuit or NAICS, with what supports each name and what is still unknown.

## Steps

1. Calibrate with `g2x_calibrate_session`. Exclude the user's own UEI from every partner search.
2. Find candidates. Call `g2x_teaming_partners` with the opportunity NAICS code, for example `{"naics_code": "541611", "excluded_ueis": ["<your company UEI>"]}`. Raise `min_past_performance` when the pursuit needs proven volume. Page for more partners with the same NAICS and exclusions.
3. Resolve each finalist. Call `g2x_search_companies` and keep same-name entities separate by UEI. Then call `g2x_company_contract_history` for recent relevant work and `g2x_socioeconomic_status` for certifications such as 8(a) or SDVOSB.
4. Check relationships carefully. Call `g2x_get_graph_neighborhood` for public one-hop links. A graph neighbor, a shared NAICS or a similar name does not prove a teaming relationship. Say what the link actually is.
5. Back specific claims. Call `g2x_company_evidence` with the claim to test, for example past performance at the target agency. Keep every citation with the claim it supports.
6. Add public context only when it helps. `g2x_company_signals` and `g2x_company_web_profile` each spend a metered lookup. Treat posts and news as claims to verify, not facts.
7. Save only on request. If asked, create or update CRM records with `g2x_crm_find` first, then `g2x_crm_save_account`. Research does not authorize outreach or CRM writes.

## What to tell the user

Give the shortlist with UEI, certifications, relevant awards, the evidence behind each pick and the open questions before contact. Name who you excluded and why. The people directory is not available yet; use people named in returned source documents, with citations. Never invent contact details.
