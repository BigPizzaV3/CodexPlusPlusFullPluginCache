# Sales Navigator workflow reference

Review snapshot: 2026-11-05. Use the detailed article notes for exceptions and current official sources before consequential action. See source-status.md for source replacements, retired features and unavailable supplementary material. This collection is generic across companies and industries.

## Contents

- Plans and availability
- Lead and account search
- Personas, saved searches, lists and alerts
- Research and relationships
- Outreach and messaging
- Exporting lead and account data
- Admin and implementation workflow
- Practical troubleshooting routes

## Plans and availability

LinkedIn's plan comparison describes Core as individual prospecting with advanced search, custom lists, alerts, account and lead pages, Relationship Maps, and InMail. It lists 50 InMail credits per month and 10,000 saved leads and accounts per user. Advanced adds shared lists and saved searches, TeamLink, Smart Links, buyer intent and CSV upload of a book of business. Advanced Plus adds CRM synchronization, embedded workflows, CRM information exchange and other administration/reporting features. Some features depend on configuration, language, rollout and access. [Plan types and features](https://www.linkedin.com/help/sales-navigator/answer/a104003)

Account IQ and Lead IQ are documented for Core, Advanced and Advanced Plus, but may be unavailable for particular companies or profiles. Lead IQ is documented as desktop-only and currently requires English language settings and sufficient public information. Account IQ combines LinkedIn and public information; its summaries can contain errors or sources may be stale. Verify claims before using them. Product and service personalization is rolling out to some Core users, so check the account; it can tailor generated insights and message drafts. [Lead IQ](https://www.linkedin.com/help/sales-navigator/answer/a6841315); [Account IQ](https://www.linkedin.com/help/sales-navigator/answer/a1655021); [Account IQ sources](https://www.linkedin.com/help/sales-navigator/answer/a6844057); [product personalization](https://www.linkedin.com/help/sales-navigator/answer/a7141991).

## Lead and account search

For an execution request to discover or rank prospects, first follow [the prospecting workflow](prospecting-workflow.md) and retain its evidence record. The sections here describe product behavior; the workflow adds explicitly labeled agent execution requirements. Exact-name lookups verify supplied targets but do not establish that the strongest matches were discovered.

Lead filters documented by LinkedIn include current and past company, company size and type, headquarters, function, current and past title, seniority, tenure, geography, industry, profile language, experience, groups and school. Other filters include relationship and shared experiences, previous interactions, saved lead and account lists, recent job changes and recent posting. Some buyer-intent and CRM filters depend on a higher plan. Person location and company headquarters location are separate filters.

Account search can filter on headquarters, industry, employee headcount, growth, annual revenue, department headcount and growth, jobs, activity, connections, and saved account lists. Criteria can include or exclude values. Results update as filters change. A pinned control is not necessarily an active value, and suggested options are not user-selected filters. Lead-search terms may include related variations; LinkedIn may show close matches when the original filter combination yields no results, so check whether it adjusted the search. [Filter definitions](https://www.linkedin.com/help/sales-navigator/answer/a1452817); [search behavior](https://www.linkedin.com/help/sales-navigator/answer/a106027); [search steps](https://www.linkedin.com/help/sales-navigator/answer/a735730).

LinkedIn documents a display maximum of 2,500 lead results across 100 pages and 1,000 account results across 40 pages per search. Refine or partition queries and check for overlap. [Search result limits](https://www.linkedin.com/help/sales-navigator/answer/a106030).

## Personas, saved searches, lists and alerts

Personas describe target buyers using function, seniority, title and geography. They can be used in search and account-related discovery; they are not the same as pinned filters or saved searches. The homepage persona section relates to saved accounts. Persona changes may take time to propagate. [Persona FAQ](https://www.linkedin.com/help/sales-navigator/answer/a1422192); [create a persona](https://www.linkedin.com/help/sales-navigator/answer/a1420199).

Saved searches preserve criteria, not a static result list, and trigger weekly new-match alerts. LinkedIn documents a limit of 50 saved lead searches and 50 saved account searches. To change search criteria, update an existing search and save a new search; renaming alone does not change its criteria. [Save searches](https://www.linkedin.com/help/sales-navigator/answer/a102024); [edit searches](https://www.linkedin.com/help/sales-navigator/answer/a106018).

Save leads and companies to return to them and receive relevant alerts. Custom lists organize them. LinkedIn's onboarding article says saving a lead also saves its associated account and links the lead to the relationship map. New-job and account updates may offer context for outreach, but do not by themselves prove active intent. [Find and save leads](https://www.linkedin.com/help/sales-navigator/answer/a10710125); [alerts](https://www.linkedin.com/help/sales-navigator/answer/a105133).

## Research and relationships

Lead pages and panels surface profile, role, relevant activity and relationship signals. Account pages can show company overview, employees, growth, relevant people, and Account IQ when available. Cross-check details; do not describe AI-generated suggestions as established facts. Search for mutual connections and shared experiences to identify a warm path. TeamLink depends on plan and colleagues' participation. [Lead pages](https://www.linkedin.com/help/sales-navigator/answer/a106049); [account pages](https://www.linkedin.com/help/sales-navigator/answer/a106045).

Relationship Maps exist across all plans and let users manually organize saved and suggested leads by hierarchy and buying role. LinkedIn documents up to 10 maps per account and 30 leads per map, with roles including decision maker, champion, evaluator, procurement and influencer. Maps can use placeholder cards for unidentified people. Map sharing depends on plan; bulk CRM updates require Advanced Plus and enabled CRM settings. Relationship Maps are not available in the mobile app per the reviewed FAQ. [Relationship Maps](https://www.linkedin.com/help/sales-navigator/answer/a456397); [FAQ](https://www.linkedin.com/help/sales-navigator/answer/a5938467).

## Outreach and messaging

LinkedIn describes messages to first-degree connections or Open Profiles as free InMail, subject to applicable limits. InMail to other eligible members consumes a credit; a response within 90 days returns a credit. Sales Navigator and LinkedIn have separate inbox behavior. Check current credit count, eligibility and restrictions before planning an outreach sequence. Never send without explicit user authorization. [Message types](https://www.linkedin.com/help/sales-navigator/answer/a1451572); [send InMail](https://www.linkedin.com/help/sales-navigator/answer/a107018).

## Exporting lead and account data

LinkedIn states that Sales Navigator does not directly export lead or account information to CSV or XLS. Advanced Plus CRM Sync, supported embedded profiles and CRM lead creation provide other workflows subject to setup and permissions; do not promise direct spreadsheet export. Source reviewed in cloud browser on 2026-11-05: https://www.linkedin.com/help/sales-navigator/answer/a102031.

## Admin and implementation workflow

Select the correct contract, purchase channel and administrative role before making changes. For identity, follow the SCIM/SSO references and distinguish provisioned user, assigned license, personal account link and actual activation. For CRM, use the current resource hub, then the vendor-specific setup, security, seller and troubleshooting guide. Establish authentication, match correctness and permission scope before enabling or testing writeback. Record success from the destination record; a connected badge alone does not validate every feature.

For subscription changes, determine whether the source is personal, corporate or online multi-user and whether the destination is eligible. Read the transferable-data matrix and transfer route. Confirm retention/overwrite behavior and completed transfer before canceling; do not assume repurchase restores old data. Purchaser, billing and product-administration permissions are different.

For reporting, choose metrics that match the business question, then inspect the export definitions and observation period. Usage and ROI attribution are not controlled evidence of causality. Privacy opt-outs and permissions can affect what an administrator sees.

## Practical troubleshooting routes

| Symptom | First references to retrieve |
| --- | --- |
| Search is unexpectedly narrow/broad | Filter definitions, Boolean syntax, search behavior, actual active values |
| Missing leads or accounts | Saved/list distinction, autosave rules, search limits, correct contract |
| Missing message or reply | Inbox routing, response filters, recipient status, credits |
| Smart Link views look incomplete | Analytics FAQ, viewer identity/privacy, access FAQ |
| A feature/button is missing | Plan matrix, role, rollout, language/device and admin toggle |
| CRM widget is present but sync absent | Embedded vs Sync guide, admin connection and per-user authentication |
| CRM record exists but cannot update | Match identity, CRM object/field write permissions, required fields |
| Provisioned user cannot activate | SCIM authority, license capacity, email association and activation |
| Teams app installed but no alerts | Tenant approval, individual sign-in, Exchange Online, region and persona settings |
| Cannot change plan | Purchaser authority, purchase channel, billing cycle, pending cancellation |
| Billing method update has no effect | Default-wallet method versus existing-contract assignment |

Retrieve exact notes using the bundled lookup rather than inventing an interface path from memory. Prefer evidence and the smallest relevant fix. Never run installation, outreach or data deletion merely as part of reading documentation.
