# Identity article references

Reviewed 2026-11-05. Notes are paraphrases. Verify current availability and procedures before acting. Review status distinguishes complete article text from supplementary media.

## Contents

- [a157566 — Admin Home onboarding](#a157566)
- [a1381088 — Configure two-factor authentication](#a1381088)
- [a10221077 — Connecting LinkedIn and Sales Navigator accounts](#a10221077)
- [a528092 — EDI and SSO privacy overview](#a528092)
- [a1450539 — EDI and SSO security guide launcher](#a1450539)
- [a149084 — EDI/SSO security whitepaper launcher](#a149084)
- [a1658198 — Employer-provided activation](#a1658198)
- [a1347782 — Enterprise association blocks account closure](#a1347782)
- [a150068 — Enterprise profiles](#a150068)
- [a182007 — Google authentication for admins](#a182007)
- [a1342692 — Identity verification for account recovery](#a1342692)
- [a1504599 — License activation troubleshooting](#a1504599)
- [a1338223 — LinkedIn signup](#a1338223)
- [a519904 — Manage email addresses](#a519904)
- [a144127 — Microsoft Entra SCIM setup](#a144127)
- [a1337273 — New-location notification](#a1337273)
- [a105078 — New-user onboarding](#a105078)
- [a1377116 — No access to account email](#a1377116)
- [a10239009 — Okta SCIM setup](#a10239009)
- [a1382101 — Password recovery](#a1382101)
- [a1377054 — Recruiter sign-in troubleshooting](#a1377054)
- [a1376109 — Repeated sign-in prompts](#a1376109)
- [a148043 — Sales Navigator SSO overview](#a148043)
- [a7140521 — Sales Navigator two-factor FAQ](#a7140521)
- [a10215127 — SCIM entity mapping](#a10215127)
- [a1657264 — SCIM setup and FAQ](#a1657264)
- [a10986009 — SCIM-managed updates](#a10986009)
- [a521796 — Second email benefits](#a521796)
- [a105136 — SSO admin guide launcher](#a105136)
- [a134025 — SSO certificate renewal](#a134025)
- [a1358878 — Two-factor overview](#a1358878)
- [a162746 — User email mismatch](#a162746)

<a id="a157566"></a>
## a157566 — Admin Home onboarding
Source: https://www.linkedin.com/help/sales-navigator/answer/a157566
Reviewed: full article.
Admin Home → Usage Reporting Overview → Coach level distribution; export CSV, sort Coach Level to identify Beginner/Intermediate users and plan targeted training. Sending training emails is a separate authorized action, not part of read-only assessment.

<a id="a1381088"></a>
## a1381088 — Configure two-factor authentication
Source: https://www.linkedin.com/help/sales-navigator/answer/a1381088
Reviewed: full Desktop/Mobile tabs and authentication sections.
LinkedIn Settings & Privacy → Sign in & security → Two-factor authentication. SMS or authenticator options; setup verifies identity and six-digit code. Authenticator secret is a credential and must remain under user's control. Existing mobile session/push may offer sign-in security prompt. Disabling2FA blocks Sales Navigator access subject to specific SSO exception documented separately. Do not disable it as troubleshooting shortcut; credential setup/change belongs to user handoff under applicable tools policy.

<a id="a10221077"></a>
## a10221077 — Connecting LinkedIn and Sales Navigator accounts
Source: https://www.linkedin.com/help/sales-navigator/answer/a10221077
Reviewed: full article; no collapsed sections or tabs.
Activation must link a LinkedIn account. Use the existing professional profile with the relevant network; LinkedIn allows one personal account. A gradual activation experiment can recommend a more established profile but allows continuation. The linked identity determines messages, recommendations and network paths. Employer admins can receive usage data; users can opt out of LinkedIn.com activity reporting. Contact support to change the linked account.

<a id="a528092"></a>
## a528092 — EDI and SSO privacy overview
Source: https://www.linkedin.com/help/sales-navigator/answer/a528092
Reviewed: complete public article text, including all returned FAQ and platform sections, 2026-11-05.
EDI imports HRIS employee identities for authentication and license management; SSO is optional. Employee identities and personal LinkedIn identities remain distinct. The old phased-rollout wording is historical. See linked EDI privacy guide.

<a id="a1450539"></a>
## a1450539 — EDI and SSO security guide launcher
Source: https://www.linkedin.com/help/sales-navigator/answer/a1450539
Reviewed: complete public article text, including all returned FAQ and platform sections, 2026-11-05.
Links to the December 2016 privacy/security whitepaper. The replacement content.linkedin.com PDF works; the old help.linkedin.com attachment URL does not. Full guide reviewed in implementation-guides.md.

<a id="a149084"></a>
## a149084 — EDI/SSO security whitepaper launcher
Source: https://www.linkedin.com/help/sales-navigator/answer/a149084
Reviewed: full article. Old attachment is broken; current a1450539 links to same titled EDI/SSO whitepaper, all 11 pages and binding diagram reviewed.
Account Center admin privacy/security dependency for employee database and SSO integration.

<a id="a1658198"></a>
## a1658198 — Employer-provided activation
Source: https://www.linkedin.com/help/sales-navigator/answer/a1658198
Reviewed: full article; no collapsed sections or tabs.
Admin must assign a license. Find the activation invitation in work email, including spam; request a resend if expired. Sign into the existing LinkedIn identity, connect it, and begin setup. A gradual personalized setup asks goal, product/service, buyer persona and target accounts. Product website analysis suggests a description/category that must be reviewed. Admins can restrict product editing. Personas require at least one function/seniority/title/geography filter. Save at least three target accounts, choose an existing list, upload an eligible CSV, or use the lead-saving alternative. Preferences remain editable after setup. Authentication and agreement acceptance follow the active tool policy.

<a id="a1347782"></a>
## a1347782 — Enterprise association blocks account closure
Source: https://www.linkedin.com/help/sales-navigator/answer/a1347782
Reviewed: complete public article text, including all returned FAQ and platform sections, 2026-11-05.
Current or former employer enterprise association can block closing LinkedIn account. Administrator must remove the enterprise association first; contact support if unknown or still blocked. Retry closure only after resolving association and with explicit deletion authorization.

<a id="a150068"></a>
## a150068 — Enterprise profiles
Source: https://www.linkedin.com/help/sales-navigator/answer/a150068
Reviewed: full article and five expanded sections.
Users → user name opens enterprise snapshot with LinkedIn profile, email action, employee details, groups, licenses and permissions, subject to admin rights. Employee Info Edit updates corporate contact details; personal LinkedIn name changes must be made by the member. Groups add/remove; Licenses Manage license; Permissions Edit. Admin-only uses No License with appropriate permission.

<a id="a182007"></a>
## a182007 — Google authentication for admins
Source: https://www.linkedin.com/help/sales-navigator/answer/a182007
Reviewed: full article and expanded setup.
Google OAuth2/OpenID Connect can act as IdP instead of SAML. Hosted company domains must be allowed; member needs work email on LinkedIn. CSV/invites should use matching domain or Google ID as external ID. Corporate authentication precedes LinkedIn verification; cached authentication may last up to12h. JIT provisioning discontinued: use SCIM. Admin Center Settings → SSO → Authenticate with Google → hosted domains → Save/Yes → enable SSO. This is security configuration, requiring appropriate authorization and verified domain scope.

<a id="a1342692"></a>
## a1342692 — Identity verification for account recovery
Source: https://www.linkedin.com/help/sales-navigator/answer/a1342692
Reviewed: complete public article text, including all returned FAQ and platform sections, 2026-11-05.
Follow official recovery prompts; Persona may require valid government ID and selfie via smartphone. LinkedIn receives consented verification result, name, birth year, locality, ID type/issuer and redacted portrait/name image, not biometric data or ID number/dates. Vendor says recovery data generally deleted within 14 days, with nonidentifying fraud data potentially retained. Canada/EU/UK alternative: notarized affidavit attached to support case. User must complete identity, camera and consent steps personally. Review covered full text; examples describe clear, valid, unobstructed ID, not verification bypass.

<a id="a1504599"></a>
## a1504599 — License activation troubleshooting
Source: https://www.linkedin.com/help/sales-navigator/answer/a1504599
Review: full text; duplicate-profile screenshot is illustrative.
Sign into intended LinkedIn account before activation. Already-active seats use direct SalesNav sign-in. Suspected duplicate profile: support re-associates subscription; do not delete/merge impulsively. Invitations expire14days, admin resends. Verified email may require Use for sign in/reset password toggle. Cache/incognito/browser checks are troubleshooting options; clearing cookies or changing security settings has separate consequences.

<a id="a1338223"></a>
## a1338223 — LinkedIn signup
Source: https://www.linkedin.com/help/sales-navigator/answer/a1338223
Reviewed: complete public article text and returned platform/FAQ sections, 2026-11-05.
Use true personal name, personal work/private email, one profile; no shared role addresses or duplicate profiles. Google/Apple sign-in optional. Existing Sales Navigator users should link established LinkedIn profile, not create a new one to bypass account restrictions.

<a id="a519904"></a>
## a519904 — Manage email addresses
Source: https://www.linkedin.com/help/sales-navigator/answer/a519904
Reviewed: complete public article text, including all returned FAQ and platform sections, 2026-11-05.
Desktop/mobile/mobile-web: Settings > Sign in & security > Email addresses. Add email, complete security check/password and verify in mailbox; only verified email can become primary. Additional verified emails can sign in. If license activation requires a toggle beside confirmed email, enable that specific address; this does not reset password. Remove only requested address and preserve recovery access.

<a id="a144127"></a>
## a144127 — Microsoft Entra SCIM setup
Source: https://www.linkedin.com/help/sales-navigator/answer/a144127
Reviewed: full public article text, all sections/tables, 2026-11-05.
Create Sales Navigator enterprise application from Entra gallery, assign users/groups with User role, create LinkedIn Admin Center SCIM configuration with selected license, generate token. In Entra Provisioning > New configuration > secret token > Test > Create. Check both user/group mappings and scope before Start Provisioning; initial sync then incremental changes/deactivations. Provision on demand can test subset. Confirm enterprise-profile email matches IdP and inspect Entra provisioning logs. Guide asks Global Administrator; use current Microsoft documented least sufficient role. SCIM provisioning remains distinct from SAML SSO and personal account activation. Full text read; illustrated controls require live UI verification.

<a id="a1337273"></a>
## a1337273 — New-location notification
Source: https://www.linkedin.com/help/sales-navigator/answer/a1337273
Reviewed: full article.
Unusual locations may trigger reauthentication and warning email. Recognized access needs no action; unrecognized access warrants official account security recovery/password change by user. Never treat warning email alone as evidence of compromise or follow unverified embedded links.

<a id="a105078"></a>
## a105078 — New-user onboarding
Source: https://www.linkedin.com/help/sales-navigator/answer/a105078
Reviewed: full article; no collapsed sections or tabs.
Start from the individual purchase-confirmation email or employer license invitation. Personalized questions are gradually available, so missing setup screens are not necessarily an error. Follow the guided onboarding checklist after activation; use the activation troubleshooting guide for failures and the homepage/navigation reference for orientation.

<a id="a1377116"></a>
## a1377116 — No access to account email
Source: https://www.linkedin.com/help/sales-navigator/answer/a1377116
Reviewed: full article; no collapsed sections or tabs.
Use an already-added alternate email or phone where possible. Otherwise the Forgot password flow offers unavailable-email/other-recovery choices, a desktop QR step, a new contact email and official identity verification. Recovery can require government ID. Keep sensitive documents within the official recovery flow; do not collect them into this skill. Recommend recovery methods and two-factor authentication after recovery. Follow the browser's credential-change and identity-verification rules.

<a id="a10239009"></a>
## a10239009 — Okta SCIM setup
Source: https://www.linkedin.com/help/sales-navigator/answer/a10239009
Reviewed: full public article text, all sections/tables, 2026-11-05.
Advanced/Plus, Okta and LinkedIn admin rights. Admin Center > Settings > SCIM > Add configuration; name, choose auto-license assignment/license and generate token. Okta catalog Sales Navigator with SCIM > Add > Provisioning > API Integration > token > Test > Save. Enable create/update/deactivate in To App and assign scoped users. Group Push only syncs group members already assigned to application. Initial names must be unique in both systems. Push Now cannot reconcile manually added LinkedIn membership; manage pushed groups in Okta. Unlink pushed group to remove group. Tokens are secrets; do not print/store in notes. Full text read; UI images unavailable, confirm exact options in current admin UI.

<a id="a1382101"></a>
## a1382101 — Password recovery
Source: https://www.linkedin.com/help/sales-navigator/answer/a1382101
Reviewed: full article and email/phone sections.
Official Forgot password → linked email/phone → verification via email/SMS/call → password reset. Additional2FA/security checks may apply; codes expire. Successful reset generates email confirmation. No code delivery: troubleshoot email or support. User must enter new credentials; never store passwords/recovery codes in skill.

<a id="a1377054"></a>
## a1377054 — Recruiter sign-in troubleshooting
Source: https://www.linkedin.com/help/sales-navigator/answer/a1377054
Reviewed: full article linked in Sales Navigator Account Access.
Check duplicate accounts, exact email spelling/domain/whitespace and verified primary LinkedIn email. Recruiter-specific title is not a Sales Navigator entitlement rule. Do not merge/delete accounts without explicit authorized recovery plan.

<a id="a1376109"></a>
## a1376109 — Repeated sign-in prompts
Source: https://www.linkedin.com/help/sales-navigator/answer/a1376109
Reviewed: full article.
Check device date/time, scoped cache/cookie issue, LinkedIn trust settings and corporate security controls; support if persistent. Do not disable broad firewall/browser protections.

<a id="a148043"></a>
## a148043 — Sales Navigator SSO overview
Source: https://www.linkedin.com/help/sales-navigator/answer/a148043
Review: full article.
Advanced/Plus, SAML2.0; corporate authentication plus initial personal LinkedIn verification. Article describes up-to12hour cached session subject to browser/IdP, no OAuth2/OpenID for this SSO setup. SSO optional. Do not confuse SAML product sign-in with OAuth CRM integrations.

<a id="a7140521"></a>
## a7140521 — Sales Navigator two-factor FAQ
Source: https://www.linkedin.com/help/sales-navigator/answer/a7140521
Reviewed: full article and every FAQ.
Required desktop/mobile since mid-April2025 for Core/Advanced/Plus, generally14days after initial activation. Existing LinkedIn2FA applies. FAQ exempts detected corporate SSO/MFA and says embedded profiles/experiences do not currently require it; verify integration-specific configuration. Each member enables individually, not bulk admin. SMS/authenticator; triggered for unrecognized devices/browser/VPN rather than every sign-in. Compatible with SCIM. Lack of2FA blocks product access but not notification emails.

<a id="a10215127"></a>
## a10215127 — SCIM entity mapping
Source: https://www.linkedin.com/help/sales-navigator/answer/a10215127
Reviewed: full public article text, all sections/tables, 2026-11-05.
Keep IdP authoritative for mapped identities. SCIM externalId maps stable user ID; username maps email; name.givenName/familyName map names; title maps business title; enterprise User extension department/manager map those fields. displayName stored in profile; work address locality stored under office addresses but not shown in UI; work-email value stored among email addresses, primary shown. Verify mapping and uniqueness before provision; map user and group separately.

<a id="a1657264"></a>
## a1657264 — SCIM setup and FAQ
Source: https://www.linkedin.com/help/sales-navigator/answer/a1657264
Review: full article and every expanded FAQ.
Advanced/Plus, Okta/OneLogin/Entra. AdminCenter Settings > GlobalSettings > SCIM; token valid2years. One-way IdP provisioning separate from SSO, user activation still required. IdP-tagged users/licenses/groups updated in IdP; roles remain AdminCenter. Manual groups/non-IdP users independently manageable; SCIM can take over formerly manual licenses. Same identifiers required across Learning and SalesNav. Existing identical group names conflict instead of overwrite. Sync within/hour. Over-capacity provisioning errors after available seats assigned; do not rely on incidental order to prioritize users. TeamLinkExtend needs separate application/token. Attributes include names, department,title,email,employeeID. IdP group changes may affect other apps. Linked Entra/Okta guides are reviewed as a144127 and a10239009; SAML guide is in implementation-guides.md.

<a id="a10986009"></a>
## a10986009 — SCIM-managed updates
Source: https://www.linkedin.com/help/sales-navigator/answer/a10986009
Review: full article.
IdP owns synchronized identity, license and group membership; AdminCenter shows IdP tags and updates within one hour. Admin role assignment remains local. Non-identity business title/phone/department/manager and membership in manually created reporting groups can be managed locally per this article. Manual groups support CSV. Distinguish these exceptions from blanket older statements that nothing is editable. Never modify IdP groups without assessing cross-application scope.

<a id="a521796"></a>
## a521796 — Second email benefits
Source: https://www.linkedin.com/help/sales-navigator/answer/a521796
Reviewed: complete public article text, including all returned FAQ and platform sections, 2026-11-05.
Verified personal plus work email improves recovery, colleague discovery and continued access after job changes. Password reset goes only to confirmed addresses. Backup may receive notifications if primary fails. Matching email can also personalize ads subject to preferences. Adding requires email verification; avoid duplicate profile creation.

<a id="a105136"></a>
## a105136 — SSO admin guide launcher
Source: https://www.linkedin.com/help/sales-navigator/answer/a105136
Reviewed: full article. Full eight-page SSO PDF and screenshots reviewed.
EDI integrates HRIS employee data; optional SSO configuration.

<a id="a134025"></a>
## a134025 — SSO certificate renewal
Source: https://www.linkedin.com/help/sales-navigator/answer/a134025
Reviewed: full article and eight expanded sections.
This is a historical March 2020 certificate rollover notice, describing a ten-year replacement certificate. ADFS and custom signed-request configurations need IT review and the current vendor certificate installed in the IdP signature list. Standard Entra ID, Okta and OneLogin setups may not use this certificate unless customized. LinkedIn cannot renew the customer's configuration. The article also suggests disabling AuthnRequest signing or temporary IdP-initiated access; do not apply a security-weakening workaround automatically. Verify current SSO documentation and involve the authorized IT owner.

<a id="a1358878"></a>
## a1358878 — Two-factor overview
Source: https://www.linkedin.com/help/sales-navigator/answer/a1358878
Reviewed: full article; linked recovery questions separate.
Password plus SMS/authenticator on unrecognized device; existing mobile session may get approval prompt. LinkedIn prefers authenticator. General all-SalesNavigator requirement has specific corporateSSO exception in a7140521; use both. New-device/email/code-limit/device-loss recovery handled through official workflow, never bypass checks.

<a id="a162746"></a>
## a162746 — User email mismatch
Source: https://www.linkedin.com/help/sales-navigator/answer/a162746
Reviewed: full article; no tabs or collapsed sections.
Desktop Admin Center → user enterprise profile → Employee Info → edit email to match CRM. The documented remediation then removes/reassigns the license, sends a new invitation and requires onboarding before CRM enablement. The article also describes instant rematching after email updates. Check the least disruptive current route first; license removal is a consequential access change, not a harmless refresh.
