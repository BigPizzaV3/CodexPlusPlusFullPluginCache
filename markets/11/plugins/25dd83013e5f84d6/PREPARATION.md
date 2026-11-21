# Jetopia public plugin v2.0.1 preparation

## Package status

- Public MCP URL: `https://mcp.jetopia.kr/mcp`
- Plugin connection authentication: `none` (the separate MCP server has no user login).
- The MCP server calls the Jetopia Sites bridge with a shared secret stored only in hosting environment variables.
- The Sites bridge executes the existing six Sites MCP tool implementations. Pricing continues through the existing `/api/tours/quote` path and booking requests retain the `chatgpt_app` source.
- The package keeps the v1.0.5 metadata, icons, and reviewer test guide. It does not include `.app.json`.
- OpenAI portal upload and submission have not been performed.

## Deployment gate

The endpoint is not live until the owner deploys `jetopia-mcp-vercel.zip` to Vercel, adds the Vercel domain `mcp.jetopia.kr`, configures the matching `JETOPIA_MCP_SHARED_KEY`, and supplies the portal challenge token as `OPENAI_APPS_CHALLENGE`. Then verify `/health`, `/.well-known/openai-apps-challenge`, and `POST /mcp` with an MCP client before connecting or scanning tools in the portal.

## Site publication

The Site-side bridge is published as Sites version v861. It uses `/api/mcp/{tours,vehicles,quote,booking-requests,booking-status,staff-requests}`. Missing or incorrect shared secrets receive HTTP 401. Bridge errors return safe error codes only. No visual pages were changed.
