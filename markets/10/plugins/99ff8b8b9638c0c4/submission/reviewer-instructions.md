# LystBot reviewer instructions

1. Open the LystBot connection supplied for review. For an authorized private
   test, open ChatGPT Plugins, select the plus button and **Add custom MCP
   server**. Enter the name LystBot and MCP URL `https://lystbot.com/api/v1/mcp`.
   Configure OAuth authentication, review the notice and create the plugin.
   Check the discovered tools, install it and select LystBot with `@` in a new
   conversation. Account/workspace policies must allow custom connections.
2. Select Connect to start LystBot's OAuth approval flow.
3. On the LystBot page, enter `<REVIEW_CODE>` exactly, including its `review-`
   prefix. Select **Verbinden** (Connect). No LystBot email, password, app
   installation or MFA step is required for this review device.
4. Return to ChatGPT and ask “Show my LystBot lists.” The prepared demo device
   should contain **Movie Night**, **Weekly Groceries** and **Weekend Trip**.
5. Run the eight scenarios in `test-prompts.md`. All testers share this demo
   device's content, but each completed connection has its own grant. Reuse the
   review code for reconnection while it remains valid.
6. To disconnect, use ChatGPT's connection management to disconnect LystBot.
   Alternatively, use **Settings → ChatGPT → Disconnect** in the LystBot app
   for the paired device. Backend token revocation or device disconnection
   revokes all ChatGPT grants for that device, including other reviewers.
   Disconnecting does not delete lists or previous chat messages. There is no
   disconnect MCP tool; a chat request alone cannot revoke access.

## Operator prerequisites, before providing these instructions

This checkout creates neither a demo device nor the named demo lists. TARS must
prepare those synthetic lists on one dedicated device with no memberships in
other devices' lists and no other members in its own lists. Do not assign real
user data or a push token to the demo. Then apply migration 033 and run:

```sh
php backend/bin/create-chatgpt-pairing-code.php <DEMO_DEVICE_UUID> --mark-demo
php backend/bin/create-chatgpt-pairing-code.php <DEMO_DEVICE_UUID> --review --ttl-days 90
php backend/bin/create-chatgpt-pairing-code.php <DEMO_DEVICE_UUID> --revoke-review
```

Insert the issued value in the private reviewer field in place of
`<REVIEW_CODE>`; never commit it. Default validity is 90 days, maximum 180.
A new review code replaces the previous one. Code revocation/expiry stops new
connections; separately disconnect to revoke grants already issued. After review,
revoke the code, disconnect the demo, and remove synthetic data as appropriate.
Production setup and submission require separate approval.

Evidence: `AlexaPairingService.php`, `OAuthAuthorizationService.php`,
`create-chatgpt-pairing-code.php`, migration 033 and `McpController.php`.
ChatGPT connection flow: [official OpenAI documentation](https://developers.openai.com/plugins/deploy/connect-chatgpt).
