# Nuelink notes

- Documented nuelink_create_automation defaults are addPostsAsDraft false and loadOldPosts false. This workflow sets them explicitly to true and false respectively.
- Documented refreshRate intervals are hours: 1, 6, 12, or 24. Use a documented interval only after approval and check live constraints.
- Creation and list responses expose addPostsAsDraft and refreshRate. Compare observed values with the approval; if required fields are missing or inconsistent, use the dashboard fallback before activation. Sending a flag alone does not verify it.
- loadOldPosts controls the initial history import and is not returned. Do not claim that history import was disabled merely because false was requested.
- Status updates accept PAUSED or INACTIVE for pausing and return INACTIVE. Verify that returned state; do not treat the wording difference as proof of a failed pause.
- Post channels show the current effective audience, not whether it is inherited or explicitly targeted. Before moving posts, resolve that distinction or confirm the future destinations with the user.

Resource requests are documented at 30 per minute per user, within a route limit of 60 per minute. Honor retry delays; reconcile uncertain writes before retrying.
