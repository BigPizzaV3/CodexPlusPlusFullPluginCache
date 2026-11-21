---
name: setup
description: Onboarding workflow. Connect the user's Nida OS workspace, verify the connection, and orient them to their live data.
---

Guide the user through connecting their Nida OS workspace:

1. Ask the user to authorize the Nida OS connection if they have not already done so. The plugin handles the OAuth flow automatically.
2. Once connected, call `workspace:state` to confirm the connection is working and retrieve their workspace summary.
3. Show them a brief summary: business name, number of contacts, active websites, open leads, and any pending calendar bookings.
4. Ask what they would like to accomplish first.

If the connection fails or returns an error:
- Confirm they have a Nida OS account at nida-os.com
- Ask them to try disconnecting and reconnecting from their ChatGPT plugin settings
- Direct them to help@nida-os.com for support
