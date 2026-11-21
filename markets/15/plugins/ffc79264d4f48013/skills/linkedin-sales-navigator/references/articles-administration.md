# Administration article references

Reviewed 2026-11-05. Notes are paraphrases. Verify current availability and procedures before acting. Review status distinguishes complete article text from supplementary media.

## Contents

- [a105137 — Add users by email](#a105137)
- [a133029 — Add users via CSV](#a133029)
- [a766076 — Admin activity log](#a766076)
- [a107088 — Admin Center overview](#a107088)
- [a10268730 — Admin guide](#a10268730)
- [a158015 — Admin Home](#a158015)
- [a106094 — Admin permissions](#a106094)
- [a108077 — Admin permissions matrix](#a108077)
- [a108015 — Admin settings](#a108015)
- [a147282 — Bulk email-domain updates](#a147282)
- [a106037 — Coach FAQ](#a106037)
- [a105143 — Create groups](#a105143)
- [a106098 — CSV import troubleshooting](#a106098)
- [a7462804 — Duplicate-profile CSV errors](#a7462804)
- [a7738286 — Email an admin group](#a7738286)
- [a108115 — Enable ROI reporting](#a108115)
- [a106038 — Export usage report](#a106038)
- [a186605 — Manage group membership](#a186605)
- [a193618 — Manage licenses](#a193618)
- [a124415 — Metric definitions](#a124415)
- [a105139 — Older ROI FAQ](#a105139)
- [a102028 — Online Advanced license quantities](#a102028)
- [a108110 — Open Admin Center](#a108110)
- [a408026 — Remove groups](#a408026)
- [a186744 — Remove users](#a186744)
- [a8340043 — Representative-only usage metrics](#a8340043)
- [a106031 — Sales Navigator Coach](#a106031)
- [a7762565 — Sales Navigator CSV field schema](#a7762565)
- [a103027 — Usage reports](#a103027)
- [a186668 — User/group action index](#a186668)

<a id="a105137"></a>
## a105137 — Add users by email
Source: https://www.linkedin.com/help/sales-navigator/answer/a105137
Reviewed: full article.
Users → Add new users → Add users by email; choose license (Advanced/Plus/TeamLink Extend/No License), permission (User/Full/Subadmin), optional group, up to50 addresses. Invalid/duplicate/overlimit entries error. Add users assigns access and automatically sends welcome. Use CSV for larger sets; inspect summary and authorization before submission.

<a id="a133029"></a>
## a133029 — Add users via CSV
Source: https://www.linkedin.com/help/sales-navigator/answer/a133029
Reviewed: full article.
Add users by CSV → Get started → Download template → Add users only. Populate invited_email_address, preferred_first_name, preferred_last_name, sales_license_current_status=active; optional comma-separated groups. employee_user_id must be unique: duplicates can cause data loss. Upload CSV, review errors, reconcile results. Welcome emails send automatically; Invited becomes Activated only after user accepts/onboards.

<a id="a766076"></a>
## a766076 — Admin activity log
Source: https://www.linkedin.com/help/sales-navigator/answer/a766076
Reviewed: full article.
Read-only Admin Center Activity log records invitations, license changes, permission changes and activation. It explicitly excludes user removals and adding users to groups. Do not present it as a complete audit trail.

<a id="a107088"></a>
## a107088 — Admin Center overview
Source: https://www.linkedin.com/help/sales-navigator/answer/a107088
Review: full article.
Advanced/Plus admins, no Core user/license management. Users, Groups, Admins, Settings, Reporting, ActivityLog; settings include SSO,CRM,SCIM,OAuth,SFTP. Multiple-product admins may see dashboard switcher. Role, license and billing permissions differ.

<a id="a10268730"></a>
## a10268730 — Admin guide
Source: https://www.linkedin.com/help/sales-navigator/answer/a10268730
Reviewed: full guide and tables; no collapsed sections or tabs.
Plan license roles, admin-only access, SSO/SCIM, user activation and training. Encourage existing LinkedIn accounts and work-email association. Optional CSV employee IDs must be unique; duplicates can overwrite users. Universal links only activate users already assigned access. Standardize shared products, configure CRM and Teams, monitor usage and ROI, and manage billing through the right purchase channel. Data transfers overwrite destination data instead of merging. Admin-only users do not consume selling licenses. The guide links detailed procedures; reading the guide alone does not constitute reading those linked documents.

<a id="a158015"></a>
## a158015 — Admin Home
Source: https://www.linkedin.com/help/sales-navigator/answer/a158015
Review: full article and FAQs.
Four surfaces: AdminHome onboarding objectives; UsageReporting; AdminSettings for CRM/messaging/TeamLink/SmartLinks/AI; AdminCenter for users/groups/SSO. Contract/license updates reflected within24hours. Connecting CRM and syncing individual licenses are separate. CRM onboarding tasks optional; Coach optional. Do not impose integrations solely because dashboard suggests them.
Supplementary media: image URLs returned HTTP 403; do not claim visual review.

<a id="a106094"></a>
## a106094 — Admin permissions
Source: https://www.linkedin.com/help/sales-navigator/answer/a106094
Reviewed: full article and all four expanded methods.
Desktop Admin Center supports User (seller), Sub admin (reporting), Full admin. Queue, quick Manage license & permission, Admins → More → Manage permissions, or CSV are alternatives. No License creates admin-only roles. CSV Permissions: Admin, Reporting, blank for no admin grant; inspect current template semantics. Other admins can restore accidentally removed privileges; sole-admin lockout requires support. Online purchaser admin cannot simply be removed; replacement may require a new subscription/data transfer. Treat permission expansion as security-sensitive, not an incidental edit.

<a id="a108077"></a>
## a108077 — Admin permissions matrix
Source: https://www.linkedin.com/help/sales-navigator/answer/a108077
Review: full article and table; image repeats matrix.
Full admin without seller license can manage users/groups/settings and reports; seller functionality still needs license. Subadmin without license can view reporting; with license can also use SalesNav. User requires license. Billing administration/additional-seat purchase requires appropriate billing permissions, not automatic for every product admin.

<a id="a108015"></a>
## a108015 — Admin settings
Source: https://www.linkedin.com/help/sales-navigator/answer/a108015
Reviewed: full article and settings table; no collapsed sections or tabs.
Admin → Admin Settings covers contract summary; CRM connections, imports, exports, field mapping and sandbox; ROI; messaging/disclosures; TeamLink; Smart Links; AI; shared products; seat transfer; Office 365; SSO and referrals. Separate account-wide feature configuration from Admin Center's billing and license management. Availability depends on plan and role.

<a id="a147282"></a>
## a147282 — Bulk email-domain updates
Source: https://www.linkedin.com/help/sales-navigator/answer/a147282
Reviewed: full article.
Use Update company email domain template: existing_email_address old address, invited_email_address corresponding new-domain address (same username), domain_name_change=TRUE. Upload applies automatically; verify exported CSV/enterprise profiles. Does not change personal LinkedIn email, resend invitations or require reonboarding for existing activated users. Pending users still need activation; duplicate-profile errors require reconciliation.

<a id="a106037"></a>
## a106037 — Coach FAQ
Source: https://www.linkedin.com/help/sales-navigator/answer/a106037
Review: every FAQ.
Homepage/profile menu access. Actual feature actions earn credit, watching videos/tip sheets does not. Recent engagement data may omit old activity; brief latency/refresh may help. Ad blockers can prevent tracking; don't weaken browser safeguards merely for score. Levels do not expire/decrease according to FAQ. Disabled messaging removes that required action; admins see usage, public sharing unavailable.

<a id="a105143"></a>
## a105143 — Create groups
Source: https://www.linkedin.com/help/sales-navigator/answer/a105143
Reviewed: full article and four expanded methods.
Groups → Create new group → name/members → Create; queue/users Manage Groups can create unmatched name. CSV groups lists complete intended memberships, creating listed groups and dropping omitted ones. Prefer incremental columns when preserving existing groups. Above2,000 users use CSV/segmentation.

<a id="a106098"></a>
## a106098 — CSV import troubleshooting
Source: https://www.linkedin.com/help/sales-navigator/answer/a106098
Reviewed: complete article and every error-code accordion.
Use CSV, not XLS/PDF. Distinguish partial row errors, wholly failed imports and interrupted batch imports; download error CSV, inspect top critical error and Messages column, reconcile successful batches, correct/reimport failed or unprocessed rows. Processing stops after1,000 errors.
LSSCSV: 001 nonexistent seat/result;103 removal would eliminate admins (use Admin Center, retain one);104 license assigned but invitation failed (resend);105 malformed email;109 purchaser seat cannot be removed;110 cannot force Pending to Active (recipient must onboard);111 capacity reached (article's copied message is inconsistent, explanation says free/buy seats);112 email matches multiple active seats (resolve duplicate/support).
EIS_UPLOAD: DUPLICATE_HEADER_COLUMN remove repeated header; INTERNAL_ERROR retry/support; PRIMARY_EMAIL_ADDRESS_HEADER_COLUMN_IS_REQUIRED add header/values; UNSUPPORTED_FILE_TYPE use CSV. EIS_UPLOAD_ROW: FIELD_PRIMARY_EMAIL_DUPLICATED deduplicate; FIELD_PRIMARY_EMAIL_MISSING supply email; HAS_MISSING_FIELDS restore comma-delimited fields even when empty; UNRECOGNIZED_GROUP_FIELD_VALUE legacy0 remove/1 add/blank unchanged; UNRECOGNIZED_LICENSE_STATUS_FIELD_VALUE active/inactive/pending, not blank; CREATE_FAILED/UPDATE_FAILED retry/support; PRIMARY_EMAIL_VALIDATION_ERROR correct format. UPLOAD_MISSING_MEDIA_ID indicates file access error; retry/support. UPLOAD_ROW_EMAIL_HANDLE_CREATION_ERROR: reimport affected row. Use current template over legacy schema assumptions.

<a id="a7462804"></a>
## a7462804 — Duplicate-profile CSV errors
Source: https://www.linkedin.com/help/sales-navigator/answer/a7462804
Review: full article.
AdminCenter detects duplicate email aliases against licensed users and blocks high-duplicate imports. Review flagged entries, correct intended identities and reupload; for small changes edit existing profile instead. Adding new users by email may invite them and assign roles. Do not delete real user accounts to bypass validation. Escalate persistent duplicates to relevant product support.

<a id="a7738286"></a>
## a7738286 — Email an admin group
Source: https://www.linkedin.com/help/sales-navigator/answer/a7738286
Review: full article.
Desktop AdminCenter > Groups > select group > email icon opens default email client; maximum50recipients. Verify recipients, draft and send only under explicit messaging authorization. Mobile has no admin functionality.

<a id="a108115"></a>
## a108115 — Enable ROI reporting
Source: https://www.linkedin.com/help/sales-navigator/answer/a108115
Reviewed: full article.
Advanced Plus only; all four supported CRMs, Sync and opportunity access. Production → Imported from CRM → ROI toggle → opportunity-value field → optional totals/currency. Requests go to representative. Includes searches, notes and lists activity beyond basic message metrics.

<a id="a106038"></a>
## a106038 — Export usage report
Source: https://www.linkedin.com/help/sales-navigator/answer/a106038
Reviewed: full article.
Admin → Usage Reporting → Export CSV; set date range, groups/users, include inactive and SSI options. Article says groups aren't included in exported CSV, conflicting with metrics dictionary's Groups field. Verify actual export schema; filtering by a group does not guarantee group column export.

<a id="a186605"></a>
## a186605 — Manage group membership
Source: https://www.linkedin.com/help/sales-navigator/answer/a186605
Reviewed: full article, all four expanded methods.
Desktop Admin Center Users queue/quick actions → Manage Groups; Groups tab Add members or remove individual. For over2,000 users use CSV or smaller groups. CSV groups is complete replacement and removes omitted memberships; add_to_groups/remove_from_groups are incremental alternatives. Upload applies automatically, so preview intended changes first.

<a id="a193618"></a>
## a193618 — Manage licenses
Source: https://www.linkedin.com/help/sales-navigator/answer/a193618
Reviewed: full article and six expanded sections.
Advanced/Plus admins use queue, quick actions, Users More, enterprise Licenses or exported CSV. License and permission are separate. No License preserves user membership; user removal is distinct. Reassignment limits depend on purchased capacity and reset first of month; UI displays remaining allowance. Reversing assignment requires available license and may transfer original/current assignee data back; examine data implications before action. Billing admins can purchase capacity separately.

<a id="a124415"></a>
## a124415 — Metric definitions
Source: https://www.linkedin.com/help/sales-navigator/answer/a124415
Reviewed: full article and all metric tables.
Purchased, Invited, Activated seats are different counts; Coach uses binary actions at latest selected date. InMail acceptance=accepted/sent within30days, refreshed daily; Top5 requires≥10 sent. CSV employee/seat IDs, invitation email, seat/license status, invited/activated/removed dates and groups are described as near-real-time; usage/SSI metrics24h delay. SSI sums brand/find people/engage/build relationships.
Dictionary has copy errors: search definition describes profile views; saved lead/account table mixes cumulative and period counts while CSV explicitly says period-only. Follow actual export column names and a103027 distinction between period saves and total saved. Groups export claim conflicts with a106038; verify schema. CSV Unique Connections is per-user first-degree, unlike aggregate team-network view.

<a id="a105139"></a>
## a105139 — Older ROI FAQ
Source: https://www.linkedin.com/help/sales-navigator/answer/a105139
Reviewed: full article and every expanded FAQ.
ROI uses CRM Sync data; aggregate closed-won metrics include connections/profile/account views, saves, InMail, public engagements, notes/searches/lists and associated lead/contact owners. Older FAQ says reps only see revenue percentage and small sample deals; newer a16641001 describes optional aggregate revenue totals and no deal-level access. Do not promise older privacy claims universally. Disable via ROI settings; member opt-out controls LinkedIn activity separately. Linked security whitepaper is a separate dependency.

<a id="a102028"></a>
## a102028 — Online Advanced license quantities
Source: https://www.linkedin.com/help/sales-navigator/answer/a102028
Reviewed: full article and troubleshooting table; no collapsed sections or tabs.
Only original purchaser admin: Admin Center → Purchases → Active subscription → Purchase additional licenses or Return Purchases. Returns are limited to unclaimed/unused licenses and take effect immediately with prorated refund; additions are prorated. Quantity changes may apply current pricing and alter billing. This differs from simply unassigning a user's license. Core must upgrade to add users; sales-representative contracts use their admin purchase routes.

<a id="a108110"></a>
## a108110 — Open Admin Center
Source: https://www.linkedin.com/help/sales-navigator/answer/a108110
Review: full article.
Advanced/Plus admin: SalesNav > Admin > AdminCenter. User/license management depends on admin role, not merely possession of a subscription.

<a id="a408026"></a>
## a408026 — Remove groups
Source: https://www.linkedin.com/help/sales-navigator/answer/a408026
Reviewed: full article and three expanded methods.
Groups tab select → Remove groups, or group-info More → Delete group, then confirmation. Remove from this group changes membership only. Distinguish deleting group, removing member and unassigning license.

<a id="a186744"></a>
## a186744 — Remove users
Source: https://www.linkedin.com/help/sales-navigator/answer/a186744
Reviewed: full article and both methods.
Users queue or quick actions → Remove Users → Save. Removed users lose Sales Navigator and removed admins lose Admin Center access, but historical usage stays in reports. Unassigning licenses is a separate alternative that preserves account membership.

<a id="a8340043"></a>
## a8340043 — Representative-only usage metrics
Source: https://www.linkedin.com/help/sales-navigator/answer/a8340043
Reviewed: full article and all tables; page stated updated six hours ago at review.
Sales-assisted Advanced/Plus admins request reports from representative; not self-service exports. Includes per-user last login/days active and AccountIQ/LeadIQ impressions in Sales Navigator versus embedded surfaces. Additional aggregate integration/maps metrics may be available. Categories: fundamental usage, finding people, engagement, conversation preparation and effectiveness.
Best-practice thresholds generally90days: Book of Business ≥25 saved accounts over2years; Focus top accounts ≥40 prioritization actions; Right buyers ≥25 Director+ decision-makers contacted/connected/saved; Warm paths ≥5 relevant lead interactions; Buyer readiness ≥5 intent dashboard/column/alert/filter actions; Personalize ≥10 relevant outbound engagements/messages; Stay updated ≥10 alert engagements or profile views within7days of alert; Discover insights ≥90 saved-entity research interactions. Warm paths include first/second degree, TeamLink, job changes, same former employer/school, past customers. Positive alert interaction includes message/save/share/view/profile view or opening More.
Multi-threading requires ≥3 relevant connections or saved leads for at least half of qualifying saved accounts, with both account and lead saved where applicable; two-year save window, connections may be older. Table labels appear reversed relative to definitions (saved-leads heading describes connections and vice versa); retain definitions and verify report field labels. LinkedIn activity opt-out reduces blended data.

<a id="a106031"></a>
## a106031 — Sales Navigator Coach
Source: https://www.linkedin.com/help/sales-navigator/answer/a106031
Review: full article.
Suggested actions, feature links and short videos; levels beginner/intermediate/proficient/advanced/expert. Admins can see activity metrics, network sharing of progression unavailable. Completion is engagement, not proof of selling expertise.

<a id="a7762565"></a>
## a7762565 — Sales Navigator CSV field schema
Source: https://www.linkedin.com/help/sales-navigator/answer/a7762565
Review: full schema and considerations.
Required invited_email_address; optional names, unique employee_id/unique_user_id, immutable seat_id, sales_license_current_status, teamlink_extend_license_current_status, admin_permission, groups/add_to_groups/remove_from_groups. Domain changes need existing_email_address and domain_name_change TRUE/FALSE. groups replaces memberships; incremental columns preserve other memberships. No row limit stated; IDs must be unique to prevent loss. Table uses lowercase active/inactive but prose calls Active/Inactive case-sensitive: genuine contradiction, use downloaded current template or support before bulk write. Active invites new users; Inactive revokes licenses. admin_permission values admin/reporting/blank. Test narrowly before bulk application, never reuse generic IDs.

<a id="a103027"></a>
## a103027 — Usage reports
Source: https://www.linkedin.com/help/sales-navigator/answer/a103027
Reviewed: full article, both expanded metric sections and message matrix.
Advanced/Plus full/subadmins: Admin → Usage Reporting. Overview, Usage, Effectiveness; default last30days, history up to2years, daily refresh with different metric refresh times. Beyond30days dates round to full weeks. Group changes may take24h. Data begins at completed onboarding; inactive/unonboarded names may appear in CSV without activity. Filter by own/default personas, not other people's custom personas.
Days active combines LinkedIn/Sales Navigator desktop, mobile, email and CRM embedded interactions. Searches count new search/filter changes, excluding typeahead and paging. Profile views include hovers. Leads/accounts saved include CRM autosaves in period; total saved counts are distinct stock measures in CSV/BI. Lists/SmartLinks created and SmartLinks views are separate metrics. LinkedIn activity opt-out affects blended measures.
InMail sent includes Sales Navigator Open Profile and nonconnection initial messages; excludes LinkedIn.com InMail and invitations. First-degree messages and post-accepted-InMail replies count Messages Sent, not initial InMail. Acceptance rate measures acceptance within30days; Top5 rank may show absolute accepted messages. Unique connections aggregate onboarded seats plus TeamLink Extend/groups, excluding opt-outs. Representatives supply additional contract-specific metrics.

<a id="a186668"></a>
## a186668 — User/group action index
Source: https://www.linkedin.com/help/sales-navigator/answer/a186668
Review: full article and action links.
AdminCenter routes to licenses, permissions, groups, invitations, group email and removal. Each has distinct scope/effects; managing users does not automatically authorize emailing everyone.
