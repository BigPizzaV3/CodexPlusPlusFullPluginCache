---
name: ella-readonly
description: Retrieve data from a connected Ella account to inspect sustainability records and draft evidence-backed ESG and carbon reports.
---

Use the available Ella MCP tools to identify supported read-only operations and retrieve user-authorized ESG and sustainability information. Do not assume tool names or schemas; discover available tools from the host. If Ella authentication is needed, ask the user to complete the supported connection flow. Never ask the user to paste access tokens. Do not invent companies, assessments, report results, or other records. Only report data returned by the server. Until explicit write operations are supported and approved, do not imply records can be created, changed, or deleted.


Start a connected account review by retrieving its company profile. Treat returned company data as existing state: a first plugin conversation does not mean a new or empty company. Do not hardcode a company name or use sample-company records as defaults. Use the configured reporting period when supported; if it is missing or a financial year differs from a calendar year, clarify the requested period before presenting annual totals. Report connection failures separately from empty data. This plugin cannot create accounts, companies, or onboarding records; direct unsupported setup actions to the Ella application.

## Build ESG and carbon report drafts

Use this workflow when the user asks to build, draft, or prepare an ESG, sustainability, or carbon report from Ella data. Retrieve the underlying records before writing factual report content. Draft the report in the conversation unless the user requests a file and a suitable document tool is available. This skill does not save reports into Ella.

1. Retrieve the company profile and establish the company, reporting period, currency, and requested audience. Use the configured period when it matches the request. The current carbon tools accept calendar years: do not label their results as a non-calendar financial year. Clarify a period mismatch and explain any unsupported date range.
2. Discover the tools exposed by the connected Ella server. Where available, use `get_emissions_summary` for annual totals and scope breakdowns, `list_emission_sources` for contributing sources, and `search_activities` for supporting quantities, units, emission factors, and provenance. Pass the same explicit year to related calls. Use only arguments supported by the discovered schemas.
3. Treat the emissions summary as the aggregate source. Activity searches are limited result sets: do not sum a sample and present it as the complete inventory. Preserve returned units and label any unit conversions. Avoid adding totals to their own breakdowns. Compare periods only when both periods were retrieved and boundaries and units are comparable; identify derived calculations.
4. For a carbon report, include company and period, available inventory boundaries, total CO2e, returned scope breakdowns, principal emission sources, available calculation methods and factor provenance, and data gaps. Explain the evidence behind material figures using returned record identifiers or source references where available. Never invent links or methodology.
5. For a broader ESG report, retrieve environmental, social, and governance records only through tools actually available. Include supported findings and an explicit list of unavailable topics. Carbon data alone cannot establish social or governance performance. Do not invent policies, targets, certifications, assessments, or compliance claims.
6. Distinguish recorded facts, calculated comparisons, and suggested next steps. Mark missing data as unavailable rather than zero, and disclose incomplete coverage, failed retrievals, and unknown assurance status. Do not describe a draft as audited, certified, or compliant with a reporting standard without evidence.

Finish with a usable report draft and a short evidence-and-gaps section. If the requested format requires information Ella cannot expose, produce the supported sections and identify the exact missing inputs. Never claim to have submitted, published, or saved a report unless a supported authorized operation actually succeeded.

