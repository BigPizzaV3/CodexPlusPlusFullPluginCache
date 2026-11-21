# ProjectBase plugin submission draft

Based on the supplied chatgpt-app-submission.json and the current portable Agent Plugins format.

Before submission:

- The MCP endpoint is configured as https://mcp.projectbase.io/mcp. Confirm the deployed server supports Streamable HTTP and authenticated workspace access.
- Replace the four placeholder listing URLs in plugin.json with the product website, support page, privacy policy, and terms of service.
- Confirm developerName matches your verified publisher identity and choose the appropriate dashboard category (Productivity is the draft category).
- Include your actual square brand icon in assets/ and set extensions.com.openai.interface.logo and composerIcon to its ./assets/ path. No invented brand asset is included.
- Add extensions.com.openai.review.demo_recording_url with an accessible video walkthrough.
- Run the five positive and three negative review cases with a dedicated test account. Enter reviewer credentials separately in the dashboard, not in this folder.
- Publish the tool annotations and justifications from the original submission on the MCP server. They are server metadata and are not embedded in mcp.json or plugin.json.
- ZIP the contents of this folder with plugin.json and mcp.json at the archive root after replacing the placeholders and adding assets.

JSON syntax has been checked. This draft has not been tested against a live MCP server or the submission portal.

Official references:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
