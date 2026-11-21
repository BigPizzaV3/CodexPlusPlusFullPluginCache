# Public sources and official fee-schedule workflow

Reference links checked for design on 2026-10-01. Recheck current pages and applicability during each user's analysis. This file contains no rate table, code catalog, or CPT descriptors.

## Sources by question

- Population: [Census ACS](https://www.census.gov/programs-surveys/acs/data.html). Align year, geography, denominator, and margin of error. A demographic count is not an obtainable patient count.
- Medicare context: [CMS data](https://data.cms.gov/). Choose enrollment data matching geography and period. Separate Original Medicare and Medicare Advantage; contracts determine the latter's modeled payment.
- Facility alternatives: [CMS provider data](https://data.cms.gov/provider-data/), state directories, and organizations' own sites. Verify services, payer participation, geography, and availability. Directory absence does not prove no competition.
- Wages: [BLS OEWS](https://www.bls.gov/oes/) and [methodology](https://www.bls.gov/oes/methods_25.pdf). Employment wage estimates omit benefits and do not measure local recruiting availability. Obtain local quotes when hiring determines feasibility.
- Payment research: [CMS PFS overview](https://www.cms.gov/medicare/physician-fee-schedule/search/overview), the official search linked there, and the applicable MAC. Other settings/services may require a different payment system; do not force everything through PFS.
- Coverage research: [Medicare Coverage Database](https://www.cms.gov/medicare-coverage-database/). Check applicable policies and effective dates separately from prices.

Do not bulk scrape directories, automate restricted services, or bypass access controls. Use available authorized browsing for public methodological/context pages. If an interface requires agreement to terms, let the user complete that step. Never claim terms have been accepted for the user.

## Payment assumptions without a bundled code database

1. Establish service year, state/locality, payer, clinician type, and facility/nonfacility setting. Identify whether PFS is the relevant payment system; bundled facility payments and product reimbursement may be different.
2. Direct the user or their billing specialist to the official CMS lookup from the overview above. They select the appropriate code(s), year, locality, and payment fields in that resource under its applicable terms. This plugin does not choose or validate CPT codes, reproduce descriptors, import code catalogs, or automate the licensed lookup.
3. Ask for the resulting numerical allowed amount under an original plain-language service label, plus source link/reference, retrieval date, year, locality, provider, setting, and whether adjustments are already included. Do not ask for a downloaded code table. Code values are unnecessary in the model input and its rate template.
4. Treat the supplied amount as user-reported until independently corroborated through a permitted source. Never convert a pasted number into a verified rate merely because it names CMS. If only a hypothetical amount is available, use it for a labeled sensitivity analysis.
5. Distinguish allowed amount, applicable provider adjustments, claim-payment probability, payer/secondary/patient collections, and collection timing. Apply each once. In the calculator, `allowed_amount` is already adjusted to the stated provider/setting; do not apply provider adjustments again. `payer_share` is a scenario input, not a universal Medicare rule.
6. Verify coverage, medical necessity, bundling, frequency limits, authorization, and billing eligibility through the user's qualified reviewer and current applicable sources. A price alone resolves none of those questions. MAC-priced and some nonpayable services may not appear in the lookup; missing is not zero.
7. Keep proposed policies separate from finalized/effective inputs. For a future year without final data, show an explicit provisional scenario and identify the refresh needed. Do not present yesterday's cache as a current lookup.

Use [payment-assumptions.csv](../assets/payment-assumptions.csv) to capture amounts and provenance. Actual private payer contracts may be summarized by the user as permitted; do not request credentials or complete confidential agreements when a numerical assumption suffices.

## Rights distinction

Linking to an official fee-schedule resource does not confer rights to redistribute the CPT content displayed there. CMS's [AMA exhibit](https://www.cms.gov/outreach-and-education/medicare-learning-network-mln/mlnedwebguide/downloads/ama-exhibit-8.pdf) concerns specified CMS displays, not blanket third-party reuse. Refer licensing questions to the [AMA licensing FAQ](https://www.ama-assn.org/practice-management/cpt/cpt-licensing-frequently-asked-questions-faqs). Do not promise that this architecture establishes a legal exemption. Use original service labels, numerical planning assumptions, and source links; no CPT descriptors, crosswalks, searchable catalog, or licensed data is distributed in this package.
