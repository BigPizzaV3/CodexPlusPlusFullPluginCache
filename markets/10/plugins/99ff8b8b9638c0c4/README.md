# LystBot connection

Generate a six-digit code in the LystBot app under **Settings → ChatGPT**
(**Settings → Alexa** in older app versions). Select Connect in ChatGPT,
enter the code on the LystBot authorization page and approve access.
App-generated codes expire after 10 minutes and can be used once.
OAuth 2.1 uses PKCE; no API key or client secret belongs in this package.
Tokens are bound to the paired device. Access covers its list memberships,
including shared lists, and its reminders.

| Tool | Required OAuth scope |
| --- | --- |
| list_lists | lists:read |
| get_list | lists:read |
| list_reminders | reminders:read |
| create_list | lists:write |
| add_items | lists:write |
| update_item | lists:write |
| create_reminder | reminders:write |

There are no delete or sharing tools. Disconnect under Settings → ChatGPT
in the app or disconnect in ChatGPT; OAuth token revocation also withdraws access.
Disconnecting does not delete list data or previously returned ChatGPT messages.

Production MCP: https://lystbot.com/lystbot/api/v1/mcp
Staging MCP (separate staging test, not a second package connection):
https://daffy.touraround.io/lystbot/api/v1/mcp
Discovery is provided through the server's `.well-known` OAuth metadata.

Support: https://lystbot.com/legal/imprint-en.html (Contact)
Privacy: https://lystbot.com/legal/privacy-en.html
German privacy: https://lystbot.com/legal/privacy-de.html
Terms: https://lystbot.com/legal/terms-en.html
German terms: https://lystbot.com/legal/terms-de.html

Build: `php backend/bin/build-chatgpt-package.php /tmp/lystbot.zip`
Verify: `php backend/tests/chatgpt-package-test.php`
The build contains only this README, the two manifests and the existing app logo.
