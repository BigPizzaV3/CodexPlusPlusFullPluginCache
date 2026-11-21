# Signal Six — OpenAI public plugin submission package

This package is prepared for the public-directory submission flow. It is not yet
fully ready for submission because the demo recording, reviewer-accessible demo
tenant/account, and supported dashboard category are still outstanding.

## Verified production integration

- MCP endpoint: https://signalsix.ai/api/mcp
- Transport: Streamable HTTP
- OAuth: authorization code + PKCE S256
- Protected-resource metadata: https://signalsix.ai/.well-known/oauth-protected-resource/api/mcp
- Authorization server: https://signalsix.ai/api/auth
- Authenticated requests are company-scoped.
- 20 tools total: 19 read-only and 1 write tool (`update_profile`).
- Every tool declares top-level OAuth `securitySchemes`.
- Production runtime returns HTTP 401 with the protected-resource `WWW-Authenticate`
  challenge for missing/invalid authentication.
- Tool-level authentication failures include `_meta["mcp/www_authenticate"]`.

## Listing URLs

- Website: https://signalsix.ai
- Support: https://signalsix.ai/support
- Privacy: https://signalsix.ai/privacy
- Terms: https://signalsix.ai/terms

## Remaining before final submission

1. Confirm the verified developer identity in the OpenAI submission portal.
2. Select the exact supported directory category shown by the portal (preferred:
   Business; fallback: Productivity if Business is unavailable).
3. Create a dedicated reviewer-safe demo tenant/account with sanitized sample data.
4. Run and verify the eight review cases against that demo environment.
5. Record and host the required ChatGPT demo video and add its reviewer-accessible URL
   to `extensions.com.openai.review.demo_recording_url`.
6. Supply reviewer credentials/instructions through the secure dashboard fields,
   never in this ZIP.
7. Complete any required portal attestations and publish only after approval.

## Review cases

The package includes five positive and three negative MCP cases under
`extensions.com.openai.review.test_cases`. They use the exact current production
tool names and avoid asserting unsupported capabilities.

## Icon

`assets/logo.png` is a 512x512 PNG using the existing draft geometric motif. It is
included to satisfy the package asset requirements; replace it with the canonical
Signal Six brand asset if one is preferred before final submission.


Category: Business & Operations

Capabilities:
- Competitive intelligence
- Competitor monitoring
- Pricing intelligence
- Competitive reports
- Market and competitor analysis
