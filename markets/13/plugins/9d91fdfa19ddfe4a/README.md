# Yigri 0.2.2 Healthcare and OAuth draft package

Prepared October 19, 2026. This package is usable for creating or updating a submission draft. It is not approval to submit for review or publish.

## Connection and scope

The portable MCP configuration connects to https://mcp.yigri.com/mcp. The server exposes eight read-only tools for existing running data, stored analysis, fitness trends, key findings and weekly context. Each AI connection requires OAuth approval. Revoking a connection stops future reads; it does not erase information or answers already received by the AI app.

Supported sources are Garmin and COROS through Stridee, and Apple Health, subject to source and recipient eligibility. Accounts with a current Strava connection cannot use the integration. Previously imported Strava history, dependent analysis and information with unverified provenance remain excluded. Results can be partial or unavailable.

Published policies are linked in the listing metadata. The approved October 16 Privacy and consent disclosures describe shared information, recipients and revocation limits. This package makes no new retention promises or legal eligibility declarations.

## Existing OAuth client and callback check

This draft declares the existing pre-registered Yigri Beta plugin client using OAuth client mode provided, token endpoint authentication method none, and the existing openid/offline_access scopes. Its actual client ID, method, allowed scopes, MCP audience and registered callback were checked read-only against the provider. This public client does not require a client secret. OAuth endpoints remain discoverable from the live server.

Compatibility between that registered callback and the current submission draft is UNVERIFIED. This package stages the existing client configuration so the saved connection can be inspected. Before OAuth consent, inspect the saved draft's imported client ID and method and compare its actual production redirect URI with the client's registered callback. Stop if they differ. No client, credential, redirect allowlist or grant was created or changed during packaging. The authenticated submission-portal flow has not been validated.

The listing category is Healthcare, selected by the owner and confirmed against the current directory heading. The copy describes existing running data and stored training insights. Future portal classification and review outcomes remain unverified.

## Review materials and evidence status

The manifest contains five positive and three negative case definitions and the protected demo URL https://mcp.yigri.com/mcp/review. The page hosts a 4:03 guided training-workflow clip and a 2:38 instructed capability-explanation clip. Existing synthetic reviewer sign-in, playback, midpoint seeking, private byte-range responses and local sign-out were verified on the hosted page. After sign-out, fresh media requests were denied.

The guided training demonstrations do not establish that every original unqualified manifest prompt passed. The fifth positive case has separate empty-account SDK evidence; its native natural-language prompt has not been run. The three original negative prompts have not been run. The recorded no-tool capability explanations are not proof of spontaneous negative-test behavior.

Full decoding and sampled visual checks passed. Continuous whole-clip visual privacy review remains incomplete. Keep the recordings protected until that review is complete. Acceptance of password-protected video hosting in the actual submission portal remains unverified.

Use only the existing dedicated synthetic reviewer accounts. Supply credentials and login instructions through secure reviewer-access fields, outside this package. This ZIP contains a public OAuth client identifier, with no client secret, access token, password or reviewer account details. It creates no account or OAuth grant.

## Country targeting

The owner approved global availability where eligible, skipping countries requiring additional work for now. The exact eligible-country list has not been verified.

The unverified legacy US-only value is omitted from this separate draft-upload package. The manifest does not include publication.countries. Omission preserves existing targeting and leaves the field editable in supported dashboards; an empty list would deliberately remove restrictions. This package does not use an empty list or select new countries. Verify and set the correct country list in the saved draft before review. Do not assume omission changes a draft's existing targeting.

## Draft setup and final review

Use Upload new version on the existing owned Yigri draft. First inspect the imported OAuth client and actual redirect URI before consent. Then check metadata, country targeting, reviewer access, actual saved-version test results, and required scans. Publisher verification, owner attestations and explicit final submission approval remain separate from this local package. No portal validation, upload, submission or public availability change is claimed here.

The archive contains only plugin.json, mcp.json, this README and assets/icon.png. Recordings and internal evidence stay outside the author-upload bundle. Private development app bindings are preserved separately and are not included.

## Validation note

The current published Agent Plugins 1.0 portable MCP schema rejects the server-level extensions field. OpenAI's current authentication documentation explicitly requires that field for OAuth configuration. This package follows the documented OpenAI mapping. Its portable transport fields and documented OAuth configuration are checked separately. The full MCP file does not pass the unextended portable baseline schema. Confirm acceptance and imported settings in the saved submission draft before connecting.
