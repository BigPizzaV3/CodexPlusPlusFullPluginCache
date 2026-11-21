---
name: instagram-research
description: Read a public Instagram profile, its recent posts or comments on a supplied public post or Reel with HasData. Use for Instagram handles and public content, not private-account access, posting or messaging.
---

# Research public Instagram content

Read `../hasdata-research/SKILL.md` and the Social and video section of `../hasdata-research/references/tool-catalog.md`.

For a profile, call `hasdata_instagram_profile_getInstagramProfile` with handle without @. For recent posts, use `hasdata_instagram_posts_getInstagramPosts` with that handle and only the requested bounded limit. For post/Reel comments, use `hasdata_instagram_comments_getInstagramComments` with the actual supplied or returned public post URL, not the profile handle.

Read the requested operation only; profile, posts and comments are separate requests. Extract a handle from a clear public profile URL without an unnecessary search. Do not invent a post ID or bypass a private profile.

Keep returned counters, dates, post URLs and sample size. Missing metrics are unknown, not zero. One profile snapshot cannot establish follower growth or historical engagement. For comments, quote briefly and omit unnecessary commenter identifiers or sensitive inferences. Pagination uses actual returned nextPageToken values within the agreed scope. No follows, DMs or edits.
