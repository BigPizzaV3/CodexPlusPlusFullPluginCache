# Nuelink notes

- Post dates in returned records are UTC. scheduledAt inputs are brand-local; recurring queue slots use the brand timezone.
- nuelink_list_published_posts defaults status to PUBLISHED when omitted. Query FAILED explicitly for failures; query RETRYING, SKIPPED, and SENT when relevant to incomplete delivery. Never assume an unfiltered call covers every status. Delivery records are per destination; preserve distinct record IDs for the same post.
- nuelink_get_schedule puts collectionStatus inside schedule[day][] entries. For delivery, show only statuses and engagement fields actually returned.

Resource requests are documented at 30 per minute per user, within a route limit of 60 per minute. Honor retry delays; reconcile uncertain writes before retrying.
