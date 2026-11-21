# Bajaj Finserv ChatGPT MCP Plugin

## Package contents

- `plugin.json` — listing, review and publication metadata.
- `mcp.json` — production Streamable HTTP MCP endpoint.
- `assets/logo.png` — 1024×1024 square listing logo supplied by the publisher.
- `assets/composer-icon.png` — 192×192 square composer icon/favicon supplied by the publisher.

## Logo mapping

The two supplied brand assets are intentionally used for the two separate listing fields:

- `extensions.com.openai.interface.logo` → `./assets/logo.png`
- `extensions.com.openai.interface.composerIcon` → `./assets/composer-icon.png`

Both are PNG files and exceed the minimum dimensions required for their respective roles.

## Before public submission

1. Verify the four public listing URLs in the submission portal:
   - websiteURL
   - supportURL
   - privacyPolicyURL
   - termsOfServiceURL
2. Add the reviewer-accessible demo recording URL to
   `extensions.com.openai.review.demo_recording_url` after the actual recording is hosted and verified.
3. Enter reviewer credentials/access instructions only in the secure submission portal, never in this ZIP.
4. Validate the production MCP authentication/authorization flow in the portal.
5. Run the five positive and three negative review cases against the saved submission.
6. Confirm the verified developer identity and the portal's accepted category values before submission.

No credentials or secrets are included in this package.

## Step to login 

We have a dedicated test account for reviewers. No SMS or real phone is needed:
1. connect the Bajaj Finance connector.
2. You’ll be redirected to the Bajaj Finance login page.
3. Enter mobile number 9838383839 and click Get OTP, Enter OTP 838383. or Enter Email id = "mcp-review@theaicompany.org"
4. Approve consent and return to Chat with the connector connected.

- The account has mock customer data covering loan status, upcoming EMIs, a Flexi loan and the EMI Network Card.

- Sample prompts:

Show my active loans with Bajaj Finance.
When is my next EMI due and how much is it?
Show my Flexi loan details and available limit.
Show my EMI Network Card details.