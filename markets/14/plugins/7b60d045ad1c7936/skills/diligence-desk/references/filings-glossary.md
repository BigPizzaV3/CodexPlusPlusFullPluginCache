# Filings and registers glossary

What the common records mean, so the memo can explain them in one line.

## US SEC (EDGAR)

| Form | Meaning |
|---|---|
| D | Notice of exempt offering (Regulation D). Private companies file it within 15 days of the first sale to accredited investors. Shows issuer name and address, year of incorporation, entity type, related persons (officers, directors, promoters), offering amount, amount sold, number of investors, and the exemption claimed (Rule 506(b) or 506(c)). Amendments are marked D/A. This is the public funding history of a US startup. |
| 10-K | Annual report with audited financials for domestic registrants. |
| 10-Q | Quarterly report, unaudited. |
| 8-K | Current report of a material event. Item 1.01 material agreement, 2.02 results, 4.01 auditor change, 4.02 non-reliance on prior financials, 5.02 officer or director changes, 8.01 other events. |
| 20-F / 6-K | Annual and interim reports for foreign private issuers. |
| S-1 / F-1 | Registration statement for an IPO. |
| 13D / 13G | Beneficial ownership above 5 percent of a registrant. |
| DEF 14A | Proxy statement; executive compensation and governance. |
| NT 10-K / NT 10-Q | Notification of late filing. |

XBRL concepts worth reading from the company-concept endpoint: `Revenues` (or `RevenueFromContractWithCustomerExcludingAssessedTax`), `NetIncomeLoss`, `Assets`, `Liabilities`, `StockholdersEquity`, `CashAndCashEquivalentsAtCarryingValue`, `OperatingIncomeLoss`. Values are in USD; `fy` is the fiscal year, `fp` the period (FY, Q1, Q2, Q3), `form` the filing it came from. Only SEC registrants have XBRL facts; Form D filers do not.

CIK numbers are up to ten digits and are zero-padded to ten digits in URLs (CIK0000320193 for Apple). The submissions endpoint returns the most recent filings in parallel arrays: index i of `form`, `filingDate` and `accessionNumber` describe the same filing. The full-text search returns `display_names` and `ciks` for each hit; use the CIK with the submissions endpoint.

## GLEIF (Legal Entity Identifier register)

An LEI is a 20-character identifier issued to legal entities that take part in financial transactions. The record carries the legal name, other names, legal and headquarters addresses, jurisdiction, legal form, entity status (ACTIVE or INACTIVE), creation date where known, and the registration authority (`registeredAt.id`, a code such as RA000665 for the Delaware Division of Corporations) with the entity's number there (`registeredAs`). The registration block shows when the LEI was issued, last updated, its status (ISSUED, LAPSED, RETIRED) and next renewal date. Parent relationships are reported by the entity itself when it has an accounting consolidating parent.

Who has one: public companies, funds and their general partners, banks, and private companies that have issued securities to institutions or done regulated transactions. Many early-stage US startups do not.

## SAM.gov (System for Award Management)

Every business that wants to receive US federal contracts or grants registers here. Public fields: legal business name, DBA name, Unique Entity ID (UEI, 12 characters), CAGE code, registration status and dates (registration, activation, expiration), physical address, entity structure (corporation, LLC, partnership), state and country of incorporation, entity start date, fiscal year end, business types (small business, women-owned, and so on), and the purpose of registration. Absence means only that the company does not do business with the federal government. Not connected as a tool in this plugin: check sam.gov by hand when the UEI or registration status matters. Federal awards themselves come from USAspending (api.usaspending.gov), which needs no registration to read.

## USAspending recipient profiles

USAspending.gov (US Treasury) publishes every federal award and a profile for each recipient, built from SAM.gov registrations: legal name, alternate names, UEI, parent company and parent UEI, business types (for example `small_business`, `corporate_entity_not_tax_exempt`, `us_owned_business`, `manufacturer_of_goods`), location, and total transactions. Profiles exist at three levels: parent (P), child (C, one registered entity) and recipient (R, no parent link). A company that won awards through several entities appears several times. Business types are self-certified at registration; a `small_business` flag is set per size standard and contract, so a large company can carry it for some awards.

## Domain registry (RDAP)

Events: `registration` (first registered), `expiration`, `last changed`. Status values: `client transfer prohibited` is normal for a managed corporate domain; `pending delete` or `redemption period` means the domain is lapsing. The registrar appears under entities with role `registrar`; the registrant organisation is often redacted for privacy.

## What does not exist as an open source

Delaware, California, New York and most other states do not publish their corporate registers through a free API, and there is no federal register of private companies. For a US private company the public record is: Form D (if it raised), USAspending (if it has won federal awards), GLEIF (if it has an LEI), the domain registry and GitHub. The memo must say which of these were checked and which had no record.
