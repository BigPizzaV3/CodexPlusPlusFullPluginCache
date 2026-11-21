---
name: get-started
description: Set up Postproxy after installing the plugin. Confirms the account is connected, shows which profile groups and social profiles are available, and helps connect a new social network. Use when the user has just installed Postproxy, asks what accounts are connected, or wants to connect another social account.
---

# Get started with Postproxy

Help the user confirm their Postproxy connection and make sure the social profiles they want to post to are connected.

## Steps

1. Call `auth_status` to confirm the connection works and to learn the workspace name. If it fails, tell the user to reconnect the Postproxy plugin and stop.
2. Call `profile_groups_list`. Profile groups are containers, usually one per brand or client.
3. Call `profiles_list` (once, without a filter) and group the results by `profile_group_id`.
4. Show a short overview: each group's name followed by its profiles (network and account name). Mark any profile whose status is not active, because posts to it will fail.
5. Ask which networks the user plans to post to. If a network is missing from the right group, offer to connect it (see below).
6. End with two or three example requests the user can try now, based on the profiles they actually have, such as "Schedule a LinkedIn post for tomorrow 9am" or "What happened on my accounts this week?".

## Connect a new social profile

1. Ask which profile group the profile belongs to, unless there is only one.
2. Call `profile_groups_initialize_connection` with `profile_group_id` and `platform`.
   - Bluesky needs `identifier` (handle) and `app_password`. Ask the user for an app password created at bsky.app/settings/app-passwords, never their main password.
   - Telegram needs `bot_token` from @BotFather.
   - WhatsApp accepts an optional `onboarding` value. Omit it unless the user has said whether the number stays in the WhatsApp Business app (`business_app`) or moves to the Cloud API (`api`).
3. Give the user the returned URL to open and finish the network's sign-in. Postproxy can't complete that step for them.
4. When the user says they are done, call `profiles_list` again and confirm the new profile appears.

## Notes

- Never invent profile IDs. Use IDs returned by `profiles_list`.
- Facebook pages, LinkedIn organizations, Pinterest boards, Telegram channels, Google Business locations, and WhatsApp numbers are placements under a profile. Call `profiles_placements` with the profile ID when the user needs to pick one.
