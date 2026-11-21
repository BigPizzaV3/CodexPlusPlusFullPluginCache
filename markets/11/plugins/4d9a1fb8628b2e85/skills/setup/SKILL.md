---
name: setup
description: Connect PlaylistAI to Spotify after installation or when the user asks to repair a connection.
---

Check Spotify with `getUsersPlaylists` (limit 1, offset 0). This check does not change the library.

If authentication is needed, let the host present its connection screen. Spotify shows PlaylistAI consent followed by Spotify sign-in.

After linking, retry the read once. Confirm connection only when the authenticated request succeeds; an empty library is successful. If it fails, report the returned error and stop retrying. Never ask for passwords, OAuth tokens, client secrets, signing keys, or encryption keys in chat. Do not create or change playlists to test a connection.
