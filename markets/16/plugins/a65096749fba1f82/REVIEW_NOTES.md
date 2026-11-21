# MailBridge - reviewer handoff notes

MCP URL: https://mailbridge.bhristov.eu/mcp
OAuth client ID: chatgpt (public client, PKCE, authorization code, refresh token)
OAuth login: user signs in with a dedicated VSID. Do not put a live VSID in this archive.
Privacy: https://mailbridge.bhristov.eu/privacy.html
Terms: https://mailbridge.bhristov.eu/terms.html
Support: https://mailbridge.bhristov.eu/contact
Demo video: https://drive.google.com/file/d/1izYrchs7QEugoOfM0FYiyJTklkASW90t/view

For portal submission select With MCP and Universal URL. Enter reviewer VSID only in the secure reviewer credentials section. Five positive and three negative test cases are embedded in plugin.json under extensions.com.openai.review.test_cases. Verify domain ownership when prompted. Run Scan Tools and review all 23 tool annotations (readOnlyHint, openWorldHint, destructiveHint) against actual behavior before submitting. The public listing requires a verified developer/business identity and a production logo.

This package contains no credentials, tokens, or source code. It has not passed OpenAI's portal checks yet.

Version 1.0.1: added official MailBridge icon, support URL, and shortened subtitle.
