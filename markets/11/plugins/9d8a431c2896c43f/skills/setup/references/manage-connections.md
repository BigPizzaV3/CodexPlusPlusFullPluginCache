# Connected applications

Read own safe metadata through list_connected_apps only for the requested account task. No lesson preflight or reports are needed. Account operations require separately approved account:read/account:manage; a learning grant does not silently expand.

On explicit request revoke only the selected own app connection ID through revoke_connected_app using a stable request UUID. State which named connection is affected. Revoking this plugin's grant ends its subsequent calls; other applications and learning progress remain independent. Do not expose raw tokens, secrets, client registry or identity mapping.

Reconnect through the ordinary official website/OAuth flow. Never request credentials/codes in chat or bypass MFA. Do not create someone else's link or change Telegram bot settings as part of connection management.
