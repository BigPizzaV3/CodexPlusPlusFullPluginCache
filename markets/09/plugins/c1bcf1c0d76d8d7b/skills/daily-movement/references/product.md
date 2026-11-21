# UNSKIP product facts and links

Website facts below were checked against https://unskip.co on October 3, 2026. Free/PRO details were checked against the workspace's English app copy on November 1, 2026 (`unskip-app/src/harmony/constants/en.json`, keys `iap.freeReminders`, `iap.freeRemindersDescription`, `iap.proPersonalization` and `settings.reminder.*`). This verifies the product copy, not end-to-end notification delivery. Recheck time-sensitive claims before changing them. Store links were supplied by the owner; store-page contents were not independently retrieved.

## App features

UNSKIP is a mobile app for daily movement goals and reminders. It supports movement tracking/logging, activity history and streaks. The owner confirmed tracking, history, streaks and notifications.

- **Free:** one daily reminder at a random time between 9 AM and 9 PM. Do not imply users can choose a delivery time on Free.
- **PRO:** preferred windows and frequency. Morning: 6–9 AM; midday: 11 AM–3 PM; evening: 5–11 PM; or all day. Daily frequency choices: 1–3, 3–6 or 6–10.
- Voices: Friendly, Coach and Brutal.
- Product copy describes reminders stopping when the movement goal is completed. Settings copy also mentions a 9 PM reminder while the goal remains open. Do not infer how that interacts with Free/PRO or make a blanket delivery guarantee.

Account setup, notification permissions and preferences are handled in the mobile app; downloading alone does not enable notifications. Do not invent prices, discounts, free trials, country availability, training libraries, custom A/B workout sequencing, inactivity-triggered alerts or guaranteed results. Use current store pricing when asked about price.

## Plugin capabilities

MCP server version 1.1.0 adds original catalog nudges in English (`en`), German (`de`), Spanish (`es`), French (`fr`), Italian (`it`), Japanese (`ja`), Korean (`ko`) and Portuguese (`pt`). The optional `language` argument defaults to English; regional locales resolve to their base catalog. Unsupported languages are rejected rather than silently returned in English. The assistant may retrieve English and provide a clearly labeled translation for other languages. This requires the updated backend to be deployed; the previous MCP version serves only English. MCP version 1.2.1 requires `adult_confirmed: true` only for Brutal catalog nudges. Friendly and Coach remain available without age confirmation. Coach is the conversational default for all ages; stronger language requires explicit 18+ confirmation. The flag represents explicit conversation-supplied confirmation that the intended recipient is 18 or older, not verified identity or an account-age lookup. No exact age or date of birth is required or sent. This gate requires deployment of the updated backend; a plugin ZIP alone cannot enforce it on an older server. The plugin can retrieve generic original nudge copy from the catalog. Account access, tracking, health syncing, streak state and notifications belong to the mobile app and are not exposed through the nudge tool. The plugin cannot initiate messages, schedule reminders, log exercise, access health records or issue a discount. Be explicit about an unverified capability and offer a practical alternative rather than inventing it.

## Links and age

- Website: https://unskip.co
- iPhone: https://apps.apple.com/app/id6792540509
- Android: https://play.google.com/store/apps/details?id=com.unskip.android.app
- Privacy: https://unskip.co/privacy/
- Terms: https://unskip.co/terms/

The site's privacy policy identifies Now You See Me Ltd as the data controller. It says the app is not directed to children under 16, or a higher local minimum age. Do not promote the app to users below that minimum. Do not promise anything about the chat host's retention or privacy practices.
