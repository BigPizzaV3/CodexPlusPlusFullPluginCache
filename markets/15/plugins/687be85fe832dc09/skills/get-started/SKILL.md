---
name: get-started
description: Use when the person wants to write a post for their own Facebook groups with MultiGroupPoster, save it as a draft, publish it to a saved group list after confirming, or check where a post went out.
---

# Posting to your Facebook groups with MultiGroupPoster

1. Call `get_started` first. It says whether the MultiGroupPoster extension is connected and what to do next.
2. Call `list_group_lists` to see the person's saved group lists. Only these groups can be used. If the person names groups that are not in a list, ask which saved list to use.
3. Write the post text with the person. For photos or video, use `open_post_composer` (a card in the chat) or `get_upload_link`, then `list_uploaded_media`.
4. Save the post with `create_post` as a draft by default.
5. Publish now only after showing a short summary (text, list, number of groups) and getting a clear yes. Then call `create_post` with `confirmed: true`.
6. Follow the post with `get_post_status` and give the links group by group. If a post seems to have failed, check `list_recent_posts` before creating it again, so nothing is posted twice.
