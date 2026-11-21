# WooCommerce Operations — OpenAI public plugin package

**Plugin display name:** WooCommerce Operations  
**Publisher:** Zactra Technologies Inc  
**Technical MCP server ID:** `zactra_woocommerce` (unchanged)

**This ZIP is for uploading in the OpenAI Plugins portal. It is not a WordPress plugin and not a replacement for the hosted Python MCP server.**

Includes portable `plugin.json`, `mcp.json`, onboarding/operations skills, and non-secret listing images.

Hosted MCP endpoint: `https://commerce-mcp.zactra.com/mcp` (confirm the public hostname still resolves to the deployed 37-tool server at submission).

Before final **Submit for review**, the publisher must:

1. Verify the business identity, MCP domain, and working OAuth discovery/authorization in the portal.
2. Confirm **all 37 tools** are visible in the portal's MCP scan (older ChatGPT connections previously showed 30). Correct annotations and any automated tool findings.
3. Create a **dedicated disposable reviewer account** and staging WooCommerce store with product/order test data and test login. Enter reviewer credentials **only in the secure review form**, never in this ZIP.
4. Record and upload a reviewer-accessible demonstration video. Add its URL in Review Details; `review.demo_recording_url` is intentionally absent because no recording was supplied.
5. Execute the 5 positive and 3 negative cases against the reviewer account and fix discrepancies.
6. Review the company's privacy and terms pages to ensure they specifically cover WooCommerce account/store/order/customer data, data retention, and connected-store permissions.
7. Confirm secure public merchant onboarding is functional; do not assume production self-registration is enabled.

The server is hosted and maintained separately, and submission approval depends on automated scans and OpenAI review.

## Optional merchant self-registration

The remote OAuth server can show a Create account tab when ALLOW_SELF_REGISTRATION=true and the corresponding backend update is installed. This supports email/password sign-up without email verification as an operator-selected policy. The public plugin ZIP intentionally contains no backend configuration or credentials.
