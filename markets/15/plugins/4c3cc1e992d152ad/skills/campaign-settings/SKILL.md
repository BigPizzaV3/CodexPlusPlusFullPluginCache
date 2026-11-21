---
name: campaign-settings
description: Use for renaming campaigns, configuring sharing and player permissions, choosing screen settings, or inviting a member.
---

# Campaign settings

To start a new campaign, check `list_campaigns` for an existing match. Use `create_campaign` with its name. Creation requires Maintain as the connection default and an available campaign slot under the user’s subscription. If the limit is reached, share the returned allowance and subscription link.

Use `get_campaign` to check the selected campaign. With Maintain and the appropriate campaign role, use `update_campaign` and send just the requested fields. Owners can rename the campaign, allow joining by URL, enable automatic approval of join requests, and decide whether players may claim or create characters.

Use `allow_join_by_url` for a shareable join link and `auto_approve_join_requests` for automatic acceptance. To let players claim existing characters without opening character creation, enable `allow_claiming_player_characters` and leave `allow_players_to_create_player_characters` as configured.

Use `allow_players_to_manage_status_conditions` for condition definitions and `allow_players_to_manage_others_status_conditions` for assignments to other characters. `allow_players_to_activate_reveal` allows players to display their own reveals. `allow_game_screen_management` delegates screen management, including pan and zoom on the visible active map. Screen settings include the active map or URL, map visibility, automatic screen activation, character-list position, character placement and component rotations.

To invite an existing dm-screen.com account, call `invite_campaign_member` with the campaign ID and email. Use the role from the invitation request. The default role is `player`. Use `owner` only when requested. Report the status returned. A new invitation is pending and an existing membership keeps its role. For someone without an account, the owner can share the join link from the web app when link joining is enabled. Personal preferences, account details and billing live in the web app.
