# ArabyVoice plugin

Version 1.0.8. Prepare Arabic scripts, choose from live dialects and voices, view your balance, and generate voiceovers using your existing ArabyVoice account.

Voice browsing shows ten preview-ready voices per page when available: five male and five female, alternating male then female. Always offer more voices and wait for the user to choose a voice before generation, unless they explicitly request a random voice. The audio player is the only place to listen and download: audio URLs go to the player through widget-only metadata, and the reply never repeats what the player shows (voice lists, links, voice name, dialect, duration). After a generation the reply gives the remaining balance and suggests emotions that fit the script for a new take. The player's download icon starts the host download/link action without a preceding network check; the signed download endpoint still enforces subscription and expiry. Deploy the web changes as well as uploading this package to activate the updated server and player. The companion web fix restores the working 1.0.5 template URI (`ui://arabyvoice/audio-player-v2.html`) and serves both v3 and the original unversioned URI as aliases to the same updated player. Deploy that web fix to restore cached ChatGPT connections; uploading or downgrading the ZIP alone cannot restore a missing server resource.

This package updates the connected plugin exported in `plugin.zip`. Its internal name is `app-6abb615537b881919ba481779cacf5ca`, matching the existing directory plugin; its display name is ArabyVoice.

The MCP server is declared only in `mcp.json`; the package has no `.app.json` app reference, because directory submissions reject them. Finish the MCP connection setup in the plugin dashboard. Account credentials are managed by the client and are not included in this package.

Connect ArabyVoice in your client. Sign in and approve access on ArabyVoice. The plugin never needs your password or API key in chat.

Included skill: `arabic-voiceover`.

The remote MCP endpoint is `https://arabyvoice.com/api/mcp`, with four tools:

- `list_dialects`: live dialect names and voice counts.
- `list_voices`: voices for a selected dialect, with pagination and listen-only previews in the player.
- `get_balance`: wallet balance, available generation seconds, and subscription expiry.
- `generate_voiceover`: the player with playback and protected download, actual duration, and remaining balance.

Generation uses the same ArabyVoice account and billing rules as the website. Audio links expire; saved generations are in https://arabyvoice.com/generations. Manage access at https://arabyvoice.com/account/connections.

Service activation requires deploying the companion ArabyVoice web changes and enabling the project's Supabase OAuth server. The package alone does not deploy or enable those services. See `plugins/SETUP.md` in the ArabyVoice source repository for deployment instructions.
