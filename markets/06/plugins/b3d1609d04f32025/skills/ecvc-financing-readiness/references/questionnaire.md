# Interactive questionnaire and branching rules

Use this question bank to cover document readiness without turning the assessment into a financing-round questionnaire.

## Response-state ledger

Maintain one state for every question asked:

| State | Use |
|---|---|
| Answered | The user supplied a responsive answer or confirmed extracted context. |
| Unknown | The user expressly says they do not know. |
| Explicitly skipped | The user says to skip or defer it. |
| Not applicable | The user confirms it does not apply; record the reason. |
| Pending | Asked but not answered, including an omitted part of a multi-question batch. |

Pending and Explicitly skipped items must appear under `Still to answer` in the next assessment turn and in the final open-items list. Unknown items also appear in the final open-items list. Never silently convert a missing response to Unknown, Not applicable, or no.

## Document-led sequence

Use documents first when the user chooses document review or uploads files:

1. Extract apparent facts and records.
2. Label pitch-deck facts `deck-derived—confirmation needed`.
3. Ask the user to confirm material extracted context.
4. Ask only questions needed to fill gaps or resolve inconsistencies.
5. Update the ledger and scoring statuses.

Never require an upload. Do not ask about financing type, round structure, amount, valuation, timing, use of proceeds, or investor count as part of the readiness assessment.

## Step 1 of 7 — Company, sector, and footprint

Cover these items in batches of no more than three:

- Company name, entity type, formation jurisdiction, and primary sector or activity.
- Every location where the company operates, including leased or owned offices, labs, warehouses, facilities, or other real estate; capture city, state or province, country, and lease/ownership status.
- Other jurisdictions indicated by employees, contractors, inventory, or material operations.
- Preferred guided, document-first, or combined path.
- Optional pitch-deck upload to prefill company, product, sector, geography, team, IP, and regulatory context.

Consolidate the footprint into `jurisdictions for qualification/registration review`. Explain that counsel must determine whether foreign qualification, licensing, permitting, tax registration, or other filings are required.

## Step 2 of 7 — Organization, governance, and registrations

Ask about:

- Formation and current entity records; governing documents and amendments.
- Current directors and officers; board and owner approvals and records.
- Existing foreign qualifications, assumed-name registrations, business licenses, permits, and registrations in the footprint jurisdictions.
- Leases, deeds, or other records for each leased or owned location.

## Step 3 of 7 — Capitalization and securities

Ask about:

- Current capitalization table and its as-of date.
- Shares, options, warrants, SAFEs, notes, or similar outstanding rights.
- Ownership ledger, approvals, grant agreements, valuation records, and equity-plan records, when applicable.

Do not request contemplated-round financing terms or draft financing documents.

## Step 4 of 7 — People, IP, and digital assets

Ask about:

- Current founder, employee, and contractor roster and agreement coverage.
- Confidentiality and invention/IP-assignment coverage for every relevant person, including founders and pre-formation contributors.
- Pending or registered patents, trademarks, and copyrights, including applicant or owner and jurisdiction.
- Domains, source repositories, app-store accounts, social accounts, cloud accounts, and other key digital assets; identify any held personally by founders or others rather than in the company's name.
- Whether a freedom-to-operate, trademark-clearance, or similar search has been considered or performed where the technology, product, or sector makes it relevant.

Do not conduct or interpret freedom-to-operate or clearance work. Put unresolved ownership and clearance issues in `Questions for counsel`.

## Step 5 of 7 — Commercial, privacy, and sector regulation

Ask about:

- Material customer, vendor, partner, license, and real-estate agreements.
- Website, app, user, customer, or subscription terms, when applicable.
- Privacy notices, cookie practices, data processing, information-security policies, and handling of sensitive or regulated data.
- Permits, licenses, registrations, insurance, and compliance work relevant to the stated sector and activities.

Apply conditional prompts when relevant, including healthcare and life sciences; defense, government contracting, and export controls; financial services; regulated consumer products; environmental activities; or other licensed operations. The report must recommend appropriate counsel review of sector-specific permitting, licensing, registration, privacy, and other requirements without making a compliance determination.

## Step 6 of 7 — Financial, tax, disputes, and investigations

Ask about:

- Current financial statements, budget, burn, runway, tax filings, debt, bank arrangements, and other financial obligations.
- Pending or threatened litigation, claims, demand letters, employment disputes, IP disputes, or similar proceedings.
- Government or regulatory inquiries, audits, subpoenas, or investigations.

Request only a high-level inventory. Do not ask for privileged legal analysis or unnecessary personal details, and do not assess merits or exposure.

## Step 7 of 7 — Diligence organization and output

Ask about:

- Diligence owner and contributors.
- Existing file index, naming convention, version control, and access controls.
- Known gaps, missing signatures, inconsistent versions, or other exceptions.
- Preferred output: dashboard, readiness workbook, concise report, data-room index/action plan, or questions for counsel.

The pitch deck remains an optional intake source. Do not include a contemplated-round financing-materials category or folder in scoring, the report, or the data-room index.
