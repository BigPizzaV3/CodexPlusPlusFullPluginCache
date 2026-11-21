# MemberSpace public plugin draft — 0.1.0

Status: package prepared; NOT ready for public submission. No portal upload, review submission, publication, or installation performed. The internal plugin is unchanged.

## Verified

- User supplied the production MCP endpoint and confirmed customers use their own accounts through OAuth.
- Endpoint rejects unauthenticated MCP initialization with 401 and advertises OAuth protected-resource metadata.
- OAuth discovery advertises authorization code, refresh tokens, and S256 PKCE. Read scopes: plans, members, memberships, memberEvents, contentViews, coupons.
- Existing icon reused: 256 x 256 PNG, 3,107 bytes. No alternate dark-mode asset or brand-color overrides added.
- Tools and review cases based on the ten currently exposed internal-plugin tool schemas. Full authenticated tools/list and tool annotation inspection remain unverified.
- Package contains no internal app binding, credentials, customer records, or tokens.

## Next: listing and publication decisions

1. Confirmed intended publisher: MemberSpace. Written to author.name and developerName; actual portal developer verification remains pending.
2. Confirmed: all supported countries. publication.countries is explicitly [] to remove country restrictions.
3. Confirmed: Growth Plan or higher is required, enforced by the API. Written to the listing and commerce_description. Confirmed: customers purchase or upgrade through MemberSpace, outside ChatGPT. Final commerce classification remains pending the target portal field requirements.
4. Provide a public page describing this plugin. The MemberSpace homepage is live but does not establish a plugin-specific description.
5. Confirm published support, privacy, and terms pages cover this integration. Candidate existing pages inspected: https://help.memberspace.com/ ; https://www.memberspace.com/privacy-policy/ ; https://www.memberspace.com/terms-and-conditions/ . They are not yet declared as verified plugin-specific listing URLs.
6. Optional: retain the current icon for both themes, or supply dark-mode assets and/or brand colors.
7. Choose the category supported in the target directory dashboard.

## Review cases

Five positive and three negative cases are embedded in plugin.json. All are NOT RUN. They cover site discovery, plan filters, bounded membership counts, multi-step coupon resolution, and login counts, plus unsupported cancellation, refunds, and email sending. Use a dedicated Growth Plan-or-higher test account. Prepare REVIEW10 and sample redemptions before running the coupon case. Also test a below-Growth account: an entitlement error must be explained accurately without claiming successful retrieval or attempting to bypass the restriction. This additional authorization check is NOT RUN. No production customer data was queried for these materials.

Verify live MCP tool annotations include boolean readOnlyHint, destructiveHint, and openWorldHint matching actual behavior. These cannot be established from the exposed wrapper schemas. Check tenant isolation and OAuth sign-in, refresh, and revocation with the intended public client. OAuth client registration/credentials and redirect URIs still need portal setup; discovery success does not prove customer connection success.

## Demo recording plan

Use the existing development installation with a dedicated sample account. Start your screen recorder, show MemberSpace connected, then run: (1) Which MemberSpace sites can I access? (2) List my enabled subscription plans. (3) Who was the last member to use coupon REVIEW10? (4) Refund every payment from yesterday. Show real responses and the unsupported-action explanation. Keep each response readable; avoid showing credentials or unrelated customer information. Stop the recording, review playback, and host it at a reviewer-accessible link of your choice. The recording and verified URL are still missing; this script is not a demo recording. A visible walkthrough can be assisted through computer controls if desired, with a separate screen recorder when video capture is unavailable.

## Final portal work, after preparation

Upload only when requested. Connect the production MCP server through OAuth, verify imported metadata, and run review cases against the saved version. Provide dedicated reviewer credentials only in secure dashboard fields, never in this ZIP or chat. Developer/domain verification, required scans, and legal attestations remain separate. Submission for review and publishing an approved release are separate actions.

## Maintenance

Keep package name memberspace stable for future releases, increment the semantic version, and preserve finalized portal-generated bindings in their owning release. This author-supplied public upload intentionally has only portable mcp.json. Server deployment and package release are separate.


## Confirmed data handling — October 1, 2026

The MCP server is stateless. MemberSpace keeps normal application access logs for up to one month. POST request bodies and responses are not logged; tool arguments and returned member data are not retained in those logs. This describes MemberSpace MCP/access logging only, not ChatGPT data retention or the underlying MemberSpace account records.

Customers can contact MemberSpace support to request deletion of their OAuth connections. ChatGPT-side disconnect behavior and whether it revokes MemberSpace authorization remain unverified; do not promise server-side revocation through ChatGPT until tested.

These facts are ready to inform the integration documentation and privacy-policy review. Existing policy coverage has not yet been confirmed, and no policy updates have been published.


## Existing legal URLs reviewed — October 1, 2026

The user supplied the existing terms and privacy-policy URLs. Both are publicly accessible and identify MemberSpace; both are now included in the manifest. URL verification does not establish legal sufficiency or directory approval.

Terms section 10 already addresses customer-authorized third-party sharing. Section 7 has broad automated-access and data-copying restrictions; consider clarifying that officially supported API/MCP integrations are permitted. Privacy section 3 includes consent-based sharing and a specific Pop Site integration disclosure, but the inspected text does not explain the ChatGPT/MCP integration. Recommended focused addition: authorized data categories and purpose of transfer to ChatGPT, applicable third-party handling, confirmed access-log practices, and support-assisted revocation. Have the legal reviewer confirm final coverage; no policy changes have been published.


## Listing feedback addressed — October 1, 2026

Removed the Growth Plan eligibility statement from the public listing description. Public descriptions now focus on membership analytics and reporting, with no prices, subscription offers, or temporary promotions. Eligibility remains accurately documented in reviewer/commerce metadata and test setup.

No category was present in the source manifest. The category selected in the submission portal and its available category choices are unknown. Obtain those choices before setting interface.category; do not treat category validation as resolved. The intended main purpose is membership analytics and reporting for business owners and teams.


## Category and support update — October 2, 2026

Set interface.category to Data & Analytics, an exact supported category from the official submission-error reference. The listing focuses on membership analytics and reporting.

Set interface.supportURL to the user-supplied https://help.memberspace.com/article/512-chatgpt-ai-insights . Article content/access verification remains incomplete: the web retrieval tool could not access it and the execution environment network proxy was unavailable. This does not establish that the page is broken. The websiteURL field still awaits a verified public plugin page.


## Website URL added — October 2, 2026

Set interface.websiteURL to https://www.memberspace.com/ at the user’s request. The homepage was previously verified as publicly accessible and identifying MemberSpace; plugin-specific page content remains a separate listing review consideration.
