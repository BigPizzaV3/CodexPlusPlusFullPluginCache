# MCP policy and domain verification

No OAuth, account, API key or privileged credentials are required. The MCP path reads anonymous published device rows and bundled published English guides. It does not write records, use R2, persist query bodies or fetch external evidence URLs. Tool arguments are processed by Cloudflare and, for device reads, public Supabase REST. Provider operational/security logs may exist; no fixed retention claim is made. Results return to the AI host under its own privacy terms. Avoid sensitive information in arguments.

Privacy and terms additions are factual supplements to the existing pages, dated 2026-11-05 in source. Existing legal review language remains. This is engineering documentation, not a claim of completed legal review.

## Exact portal challenge procedure (owner action, not executed)

1. After an authorized draft upload, open MCPs → lensden-explorer → Connect. Obtain the exact challenge token AND the HTTPS challenge URL displayed by the portal.
2. The documented path is /.well-known/openai-apps-challenge on the portal-selected eligible origin, normally https://lensden.net/.well-known/openai-apps-challenge. Use the displayed URL, not a guessed token or an alternate path.
3. With separate authorization, host only the exact token as a plain-text response at that URL (no JSON, labels, token list or invented placeholder). Do not overwrite another plugin's challenge. If it is occupied, follow the portal's eligible parent-origin/distinct-host options or contact support; do not create new infrastructure automatically.
4. The present artifact deliberately has no invented challenge file. If serving the real token needs a source/artifact change, prepare that single file and new hash under separate authorization before release; never mutate the pinned artifact. No DNS or production change is performed by this procedure.
5. After authorized hosting, perform one exact challenge read/portal verification, then connect and inspect the automated scan. Fix concrete findings only; submission remains separately authorized.

Source: https://developers.openai.com/plugins/deploy/submission#domain-verification-details
