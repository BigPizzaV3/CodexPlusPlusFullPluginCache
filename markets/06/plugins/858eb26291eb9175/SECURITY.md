# Media2URL plugin security

The plugin is an instruction and metadata package, not an authorization layer. The future connected Media2URL App and backend must enforce account connection, workspace ownership, file validation, abuse controls, rate limits, plan entitlements, quota, retention, and every destructive action server-side.

## Boundaries

- Do not place OAuth tokens, refresh tokens, storage keys, presigned upload credentials, deletion secrets, database keys, private content, or sensitive asset metadata in skills or responses.
- A user-provided public URL does not prove ownership and does not authorize copying, importing, modifying, or deleting the remote asset.
- Private assets stay private unless the user explicitly requests an allowed publication action and the connected App confirms authorization.
- A binary attachment must not be treated as available to the App unless the current supported App upload flow actually receives its bytes.
- Anonymous ChatGPT storage and publishing are not offered. The App must require account connection before creating storage, publishing content, importing media, or issuing an upload destination.
- The Free account tier is capped at 90 uploads per month, roughly 3 per day. A paid plan is required for higher quotas and advanced controls; the App/backend must enforce each limit before creating a write capability.
- Delete is destructive and must remain a distinct write action subject to App authorization and ChatGPT confirmation behavior.
- Skills must report only structured results returned by the App; they must not invent URLs, expiration, access controls, version history, or diagnostic facts.

## Trust and support

Use the actual Media2URL resources for policy and support questions:

- [Privacy Policy](https://media2url.com/privacy)
- [Terms of Service](https://media2url.com/terms)
- [Security](https://media2url.com/security)
- [Contact and support](https://media2url.com/contact)
- [Report abuse](https://media2url.com/report-abuse)

Analytics attribution belongs in the App/backend and must use controlled sources such as `chatgpt_plugin`, `chatgpt_app`, and `codex_plugin`. Skill text must not add arbitrary tracking parameters or log private user content.
