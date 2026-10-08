# License and account screens
Current evidence includes both legacy License-Key activation and account-aware entitlement flows. Always ask which VeTayStudio version and screen the customer sees.
Common statuses include `ACTIVE`, `INVALID`, `BLOCKED`, `EXPIRED`, `DEVICE_MISMATCH`, `DEVICE_LIMIT_REACHED`, `ACCOUNT_LOGIN_REQUIRED`, and `ACTIVATION_REQUIRED`.
Customer-safe handling:
- `INVALID`: recheck the exact key entered; do not generate or alter a key.
- `BLOCKED` or `EXPIRED`: escalate to official support.
- `DEVICE_MISMATCH` or `DEVICE_LIMIT_REACHED`: do not advise fingerprint bypass or database edits; escalate with the exact message.
- `ACCOUNT_LOGIN_REQUIRED`: ask the customer to use the account sign-in flow shown by their installed version.
- Network/protocol/storage messages: capture the exact text, verify connectivity, restart once, then escalate if persistent.
Never request passwords, activation tokens, signing keys, database access, or payment evidence in a public chat. Mask License keys in screenshots when possible.
