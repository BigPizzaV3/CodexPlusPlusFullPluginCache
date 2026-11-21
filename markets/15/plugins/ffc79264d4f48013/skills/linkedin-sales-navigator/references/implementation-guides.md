# Linked implementation guides

## Contents

- SSO administrator guide
- Microsoft Dynamics installation
- Dynamics sync and activity writeback
- Dynamics validation
- Dynamics security
- HubSpot sync
- EDI and SSO privacy/security whitepaper
- LinkedIn Admin Center illustrated guide
- Microsoft Entra SAML SSO

## SSO administrator guide
Source: https://content.linkedin.com/content/dam/help/en-us/sales-navigator/SSO_Admin-Guide.pdf
Review: all 8 pages of extracted text; visual screenshots and diagrams reviewed. May2020 historical version.
AccountCenter Settings > SSO. Exchange LinkedIn SP metadata with IdP and IdP metadata with LinkedIn, via XML upload or manual fields. IdP issuer/entityID, redirect endpoint, optional subject attribute (otherwise NameID), public X.509 certificate; multiple certs supported. Save both sides. Optional settings include signing, algorithm, binding, authentication-context and custom mappings. Historical defaults unsigned AuthnRequest/SHA1/HTTPRedirect are not current security recommendations. Test/IdP-only mode enforces IdP flow while normal LinkedIn/SP sign-in remains possible; enable only after successful test and recovery planning. Use current admin UI and modern organization-approved algorithm/policy; public certificate is distinct from private key.

## Microsoft Dynamics installation
Source: https://learn.microsoft.com/en-us/dynamics365/sales/linkedin/install-sales-navigator
Review: complete article, prerequisites through troubleshooting and related links.
Requires Dynamics SystemAdministrator, CustomerEngagement environment (not standaloneDataverse/on-premises), licensed Dynamics and LinkedIn components. Open LinkedInIntegration from SalesHub AppSettings or AdvancedSettings, or official Marketplace. Select correct environment, inspect terms, install, verify three solutions: LinkedInSalesNavigatorControlsForUnifiedClient, LinkedIn, msdyn_LinkedInSalesNavigatorAnchor. Enable integration and desired photo/employment updates separately; CRM Sync remains separate. Missing tab: verify toggle, controls and anchorversion3.0.1.1060+. Inactive: solutions installed, sync enabled, actual LinkedIn seat active. Stuck install: environment permissions/status/dependencies. Preinstalled solutions do not themselves enable transfers. Microsoft's older Advanced references conflict with LinkedIn's explicit Plus-only2025widget policy; verify product bundle entitlements.

## Dynamics sync and activity writeback
Source: https://delivery-p143253-e1476319.adobeaemcloud.com/adobe/assets/urn:aaid:aem:ee74c282-ff85-4426-a84d-fd410bd0eb8e/original/as/original.pdf
Review: full 14-page text, all sections and field table; visual screenshots and diagrams reviewed.
OnlineDynamics2016/365v8.2+, dedicated integration identity with required read scope, Plus+admin and seller seat for testing. Guided flow chooses production/sandbox, checks permissions, connects, configures autosave/import/export/creation/validation and optional ROI value/currency. Refresh/close restarts incomplete flow. Initial ingestion days/week; NotSure stage includes open opportunities. Writeback requires each user OAuth and appropriate Task/Note/Call write scope; mobile-originated calls only. User can correct matching before logging, confirm destination record then perform only authorized activity. Subject prefixes distinguish standard Tasks; reporting creator identifies actor. Approximately90day reauthentication per guide, verify actual policy. Historical Salesforce/Dynamics-only statement and create-leads description are obsolete/copy errors, not universal platform limits.

## Dynamics validation
Source: https://delivery-p143253-e1476319.adobeaemcloud.com/adobe/assets/urn:aaid:aem:a4a9a343-a6a0-4271-a55e-13876d0259d1/original/as/original.pdf
Review: all 5 pages text, complete lines0–64; visual screenshots and diagrams reviewed.
Requires app+sync+Plus. Dynamics integration settings permit LinkedIn updates; SalesNav AdminSettings > Production > Exported > ValidateCRMData. Initiates within48hours, daily thereafter. NotAtCompany flag populated for mismatch, null otherwise. Eligible contacts owned by syncing users or related to their accounts/opportunities. Four optional systemviews: all/my opportunities-at-risk and all/my departed contacts; CRM permissions control access. This is original flag validation, distinct from newer CRM badge validation.

## Dynamics security
Source: https://delivery-p143253-e1476319.adobeaemcloud.com/adobe/assets/urn:aaid:aem:500a6795-5ab7-40d0-902f-6bf91ba1980d/original/as/original.pdf
Review: full 12-page text including complete object/field appendices; visual screenshots and diagrams reviewed.
OAuth admin/user layers, TLS, encrypted stored imports, record-level access restrictions. Imports every12hours, matched badges visible contract-wide, onebest match, manual corrections shared, no automatic unsave on ownership change. Activities append instantly; accounts accept notes, mobilecalls only. Disconnect/purge removes imported data within30days. Imported ActivityPointer/Account/Contact/Lead/Opportunity/SystemUser/Position/Teams include identity, contact,address,ownership,revenue,status,timestamp and hierarchy fields; custom mappings supported. Integration identity also needs WhoAmI and RetrieveUserPrivilegeByPrivilegeName read permissions. Writeback uses activity timestamps/subject/owner/recordlink/body/status; notes subject/object/notetext; SmartLinks adds URL/location. Legacy SafeHarbor and SOCTypeI wording requires current TrustCenter verification; old app requirement conflicts with newer writeback guide, use current installation flow.

## HubSpot sync
Source: https://delivery-p143253-e1476319.adobeaemcloud.com/adobe/assets/urn:aaid:aem:1f5890bf-6a3b-4a23-92fc-5499cb13b414/original/as/original.pdf
Review: full 12-page text including tables and troubleshooting; visual screenshots and diagrams reviewed.
Plus, HubSpot SalesHubPro+, admin on both. Per-user embedded app separate from admin LinkedInCRMSync package. Connect in HubSpot integrations, choose correct SalesNav contract and production/sandbox, inspect consent and return to HubSpot to finish. BusinessManager existing connection requires planned disconnect/reconnect around SalesNav connection; shared-source consequences matter. Users individually authorize writeback; select LinkedIn in activity timeline filters. Contacts→leads, companies→accounts, deals→opportunities, owners→ownership. New contacts need email and account association where configured; do not create duplicates merely because match failed. Contact updates require actual write permissions. Broad lead-creation/Advanced-widget wording in PDF is inherited boilerplate: HubSpot supports contacts and current embedded eligibility is Plus. Verify actor, match and resulting activity rather than assuming success.

## EDI and SSO privacy/security whitepaper
Source: https://content.linkedin.com/content/dam/me/business/en-us/sales-solutions/resources/pdfs/privacy-and-security-whitepaper.pdf
Review: complete 11-page extracted text; December 2016 historical version; binding diagram visually reviewed: first SSO login branches through binding; subsequent logins enter application.
EDI uploads employee CSV through UI, SFTP/public keys or HTTPS/token, encrypted in transit/storage. Minimum recommended identity fields are stable ID, primary email and names; may upload only relevant employees. SAML 2 SSO is optional. Binding grants application-specific read permissions to personal profile/network; personal writes require separate authentication. Employer must deactivate leavers; removal from all applications unbinds identity. Employees can request support unbinding, company can request purge. The guide warns all uploaded employee fields are visible to EDI identities. Do not treat historic product list, account-creation guidance, or no-SOC statement as current policy; use modern dedicated articles and Trust Center.

## LinkedIn Admin Center illustrated guide
Source: https://business.linkedin.com/content/dam/me/business/en-us/talent-solutions/resources/pdfs/admin-center-2023-v2.pdf
Review: both pages, complete text and screenshots. 2023 guide.
Contracts & Orders opens contract terms, dates, contacts, billing and downloadable order forms. Transactions downloads invoices. Payment-method default applies future purchases, not existing contracts; edit contract billing to change its method. Contract Admins controls invitations/removal. Older illustrated guide says request frequency/payment changes through support; newer help articles expose more self-service fields. Hire/Learn cover label is historical; current Sales Navigator billing articles establish applicability.

## Microsoft Entra SAML SSO
Source: https://learn.microsoft.com/en-us/entra/identity/saas-apps/linkedinsalesnavigator-tutorial
Review: complete article including prerequisite, mapping, SP/IdP test sections; screenshots described in text.
Use an SSO-enabled Sales Navigator subscription and appropriate Entra application-admin role. Gallery application supports SP/IdP flows, JIT provisioning and automated provisioning, but these are distinct settings. Fixed identifier limits one instance per tenant according to guide. Exchange Entity ID/ACS with LinkedIn, use actual tenant-specific sign-in URL, map email/name/department and unique identifier consistently, upload federation metadata. Assign a test user and test both required entry paths before enforcing. JIT auto-license assignment consumes available licenses and does not eliminate initial personal-account linking. Historical Account Center labels may differ from current Admin Center. Use current LinkedIn test mode and certificate-rotation guidance to avoid lockout.
