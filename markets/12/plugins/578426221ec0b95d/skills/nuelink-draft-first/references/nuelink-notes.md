# Nuelink notes

- nuelink_create_post defaults to DRAFT; pass DRAFT explicitly for this workflow. The supplied schema permits captions up to 3000 characters, but individual platform limits may differ.
- Creation returns status and data containing id and message, not the full post. Verify the exact ID with nuelink_list_posts.
- New posts use the collection's destinations. Do not change collection channels as a shortcut for one post.

Resource requests are documented at 30 per minute per user, within a route limit of 60 per minute. Honor retry delays; reconcile uncertain writes before retrying.
