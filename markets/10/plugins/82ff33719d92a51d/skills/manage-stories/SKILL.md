---
name: manage-stories
description: >
  Prepare, edit or schedule an unpublished PostQuickAI story. Use for story
  drafts, turning a post or video into a story, or changing a future story.
---

# Manage Stories

1. Identify the existing content group and use `listAccounts` to check connected destinations. Story destinations are Instagram, Facebook and TikTok; do not offer unsupported platforms.
2. For an existing story, use `listStories` and `getStory`; reuse known IDs rather than guessing. Read content and status before editing.
3. For new media supplied as a file, use `createUploadLink` and wait for `getUploadLink` to report uploaded. Use `createStory` for a public media URL or `convertToStory` for an existing post/video. Both create drafts.
4. `updateStory` changes only provided fields on an unpublished story. Confirm changes to scheduled public content. A type change must include the appropriate media URL. Already published or active publishing work cannot be edited.
5. Before `scheduleStory`, show the media, caption, connected destinations, date, time and timezone and obtain approval. Use the returned saved schedule as evidence of success.
6. For cancellation, read the saved item and show what will be cancelled before `cancelSchedule`. Cancellation does not recall published content or accepted publishing work.

Immediate story publishing and deletion are unavailable through this connector. Redirect those requests to the PostQuickAI dashboard. Do not blindly retry a write with an unknown outcome.
