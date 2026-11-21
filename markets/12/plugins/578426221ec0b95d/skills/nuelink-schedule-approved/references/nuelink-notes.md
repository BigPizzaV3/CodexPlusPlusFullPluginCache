# Nuelink notes

- scheduledAt is brand-local YYYY-MM-DD HH:mm:ss and must be at least ten minutes in the future. Returned postDate is UTC; compare after timezone conversion.
- nuelink_create_post uses the collection's channels and returns an ID and message, not a full post. Verify that ID in SCHEDULED or QUEUE view. Creation supports SCHEDULE with scheduledAt or QUEUE, but has no queuePosition input.
- nuelink_update_post returns the full post. Its advertised inputs allow caption and lifecycle changes for unpublished non-POLL posts, not media/platform options; publishMode has DRAFT, SCHEDULE, and QUEUE, without IMMEDIATE.
- Post reads and update responses expose effective channels: explicit post targets when set, otherwise collection defaults. Preview and verify the exact post's returned channels. Use user or dashboard confirmation only when destinations are missing or inconsistent; never substitute collection defaults for an unknown audience.
- nuelink_get_schedule includes collectionStatus in each schedule[day][] entry. FRONT queue placement does not guarantee an immediate send.

Resource requests are documented at 30 per minute per user, within a route limit of 60 per minute. Honor retry delays; reconcile uncertain writes before retrying.
