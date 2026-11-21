# General Legal

Connect your General Legal account to submit contracts for attorney review, manage legal matters, exchange messages with attorneys, and download reviewed documents.

## Connect

This plugin connects to **https://mcp.general.legal/mcp**, the same remote MCP endpoint used by the General Legal Claude connector. Sign in through your client's OAuth flow and select your General Legal organization. An existing portal account with access to that organization is required.

Authentication is handled by Clerk. Never paste passwords, access tokens, or API keys into chat or tool arguments. If access expires, use your client's reconnect action.

## Work with legal matters

The bundled `legal-matters` skill explains these workflows, including transfer
confirmation, safe retries, and finding released versions in completed matters.

- Ask to see your matters or documents and their review status.
- Open a matter with a legal question, or submit a document for review.
- Complete the file transfer through the upload link before confirming review.
- Read attorney messages and send a reply when you want to respond.
- Download a released document when review is complete.

Starting a matter, confirming an upload, and replying to a thread can initiate work or notify the legal team. Reviews involve AI and a human attorney, so results are not instantaneous. Legal services remain subject to your engagement terms and applicable fees.

This package connects only to the OAuth matters service. It does not include programmatic signup, API-key issuance or recovery, or incorporation workflows.

## Support and policies

- [Contact General Legal](https://general.legal/contact) or email support@general.legal.
- [Privacy policy](https://general.legal/privacy-policy)
- [Terms of service](https://general.legal/terms-of-service)

The icon assets come from the [General Legal press kit](https://general.legal/press-kit). Their original vector shapes and colors are preserved; intrinsic dimensions are set to 128 by 128 pixels for plugin listings.
