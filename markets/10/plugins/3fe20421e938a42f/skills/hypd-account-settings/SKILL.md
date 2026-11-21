---
name: hypd-account-settings
description: Help users find and manage HYPD Actions for active Microsoft Advertising accounts when they ask where to see or change account permissions.
---

Call `msads_open_account_settings` to open the account settings panel in the chat. The user can also reach it from this plugin's Settings in ChatGPT, then **Manage account Actions**. The panel shows active Microsoft Advertising accounts. They can use **Previous** and **Next** to find the account, then turn Actions on or off for that account.

The user must make the change themselves. Turning Actions on requires accepting the acknowledgement in the panel. HYPD still requires explicit approval for each change draft before applying it. For a shared account, its owner manages the setting.

If the plugin settings are unavailable, point the user to [Sources in HYPD](https://app.hypd.ai/sources) to manage the account's Actions.
