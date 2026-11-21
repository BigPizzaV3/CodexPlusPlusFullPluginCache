---
name: service-business-assessment
description: Assess a local service business from its domain, select 3–5 regional competitors, and produce a concise client brief plus a sourced interactive report and agent-readable data. Use for digital presence, website conversion, local SEO, advertising and inquiry follow-up audits; distinguish public evidence from account data and controlled tests.
---

## Website and start

Use the business website already supplied, or ask for it. The optional Overtime start page is https://grader.overtime.work/start/?tool=digital-presence . Explain that pressing Start sends Overtime the website and selected tool, then returns the user to ChatGPT; no email or Overtime login is needed. If the conversation already includes an Overtime submission receipt, do not ask the user to submit again. Never claim the website was captured or a notification sent without a server receipt. Do not silently send conversation content or contact information to Overtime. If the user declines the form, still help with the skill; capture only actual submissions.


# Service Business Assessment

## ChatGPT assessment workflow

Use the hosted grader evidence when its status/report links are provided in the handoff, then research and explain the findings in ChatGPT using available tools and the bundled references. No Overtime MCP connection or account is required. Give the owner 3–5 prioritized, specific recommendations with linked evidence. Preserve incomplete provider data, estimates versus actuals and unknown versus zero. Local collection scripts are optional helpers when an execution environment is available; they are not a prerequisite for the public baseline. Explicit user instructions take precedence.

Run an evidence-backed assessment, not a generic agency checklist. The domain is enough to begin. Infer the business, services and service area from the site, then review those inferences before selecting competitors. Ask only for information that cannot be inferred, and keep collecting independent public evidence while access questions are pending.

## Deliverables

Create one canonical `report.json`, a client brief of no more than five pages, an expanded interactive webpage when requested, and Markdown/JSON/query access for agents. Keep raw crawl files and private account exports outside the published bundle. Use the user's voice and brand where supplied; use the user's requested writing style. Use available document, PDF and website capabilities when producing those artifacts.

The default reader is the business owner. Verify the owner’s name from the company site when available, then open with a short paragraph addressed to that person about the possibilities for the business. Frame the entire assessment around focus areas and opportunities available to the business, never as a proposal, a personal recommendation from the author, or a list of work an agency would perform. Avoid “I’d,” “we’ll,” “our work,” provider staffing and engagement language. Address the owner directly and lead with how customers find the business, request estimates and become booked work. Explain findings through their business implications and the decision or action they support. Keep collection procedures, exporter instructions, agent APIs, workflow design and assessment-tool comparisons out of the main client narrative; retain them in supporting evidence or operator documentation. Do not mistake a clarification of the intended reader for authorization to make the report publicly accessible.

## Workflow

1. **Discover.** Read the homepage, services, about and contact pages. Record actual service area, main buyer, booking/inquiry type, and service lines. Use `scripts/collect.py DOMAIN --out WORKDIR/collection/subject` for a bounded, robots-aware public crawl. Render the conversion path before claiming a form is missing. Review redirects, robots restrictions and truncation in the output.
2. **Choose peers.** Search the web for the core service plus the actual city/region. Select 3–5 businesses with overlapping geography and services. Verify each on its own site; record the reason for inclusion and material differences (wholesale versus installation, franchise versus local, broad regional footprint). Exclude directories and national lead brokers unless explicitly relevant. Do not call them market leaders without evidence.
3. **Collect comparable evidence.** Crawl peers with the same limit and categorize sitemap URLs. Read [collection protocol](references/collection-protocol.md) for website, performance, SEO, ads and email checks. Record sources, dates, query filters, device and measurement units alongside results. Prefer account APIs/exports when available; use public browser evidence for ad libraries and rendered flows. Never bypass access controls or infer unavailable account metrics.
4. **Add account data.** Use available account access to collect same-date, same-country Ahrefs Overview, Top Pages and Organic Keywords for every domain. Request exports only when needed. Normalize CSVs with `scripts/import_ahrefs.py`; review and merge with `scripts/merge_ahrefs.py`. When using a signed-in browser, follow the SEO collection protocol for filters, pagination, screenshots and provider notices. Preserve estimates versus actuals and unknown versus zero. Owner Search Console/analytics/ad access can verify actual results; Ahrefs access is useful but not a prerequisite for the public baseline.
5. **Verify follow-up.** Ask early for an authorized test inbox and permission for one real inquiry if that permission is not already in the conversation. Until supplied, inspect without submission. The test must separately verify on-page success, owner delivery, customer confirmation and successful conversion recording. Redact private details and avoid repeated submissions.
6. **Assess.** Write observations, their implications and an executable recommendation. Use [assessment rules](references/assessment-rules.md). Rank a small number of opportunities by evidence, likely business impact, effort and prerequisites. Do not produce a composite maturity score by default. Explain what missing evidence prevents us from deciding.
7. **Package.** Follow `references/report-contract.md`. Validate with `scripts/validate_report.py REPORT_JSON`; generate the readable evidence companion with `scripts/export_markdown.py REPORT_JSON --out REPORT_MD`. Build the short brief and interactive view from the same canonical facts. Put screenshots next to the finding they support, with capture date and linked source. Make model inputs editable and clearly hypothetical until real inputs exist.
8. **Check and deliver.** Verify source references, entity identity, missing-data semantics, page count, PDF renders and endpoint behavior. Create and deliver artifacts using the capabilities available in this conversation; publish only within the user’s requested scope. Do not email or message the client without explicit authorization. Return the brief, report link, and the specific data still needed.

## Reusable tools

- `scripts/collect.py`: bounded public crawl; no forms submitted, no browser-only claims.
- `scripts/init_report.py`: create a schema-compatible starting bundle from reviewed business/peer configuration and crawl folders; all account measurements start unknown.
- `scripts/import_ahrefs.py`: normalize CSV/TSV exports with date, country, domain and provider provenance.
- `scripts/merge_ahrefs.py`: merge a reviewed normalized export into an existing bundle without changing unrelated findings.
- `scripts/validate_report.py`: schema, reference integrity, entity and unknown-state checks.
- `scripts/export_markdown.py`: complete readable companion from the canonical bundle.
- `scripts/render_brief.py`: five-page PDF renderer for reviewed `brief.pages` content, with overflow failure and linked citations.
- `scripts/test_workflow.py`: meaningful regression checks for collection, import and validation boundaries.

Install `scripts/requirements.txt` into an isolated Python 3.9+ environment. Browser and account access remain agent-managed, not hidden in scripts. Never put credentials in the report, skill or source repository.

## Format evolution

Test additional business categories before claiming the product is broadly validated. Preserve dated snapshots and distinguish public evidence from authorized account research.

## Hosted grader

The Start form starts the hosted grader and adds job/status/report URLs to the ChatGPT handoff. When those URLs are supplied, check status and use the report JSON as dated source evidence; preserve unavailable providers and gaps. Do not start another scan merely because a report is partial. If the hosted scan did not start, offer the hosted grader retry and continue useful public research with available tools. Do not claim a container scan or hosted report ran without evidence.
