# Nuelink notes

- nuelink_list_brands returns timezone and queueStatus. nuelink_list_collections includes assigned channels, queues, status, and timezone; use nuelink_list_channels for the full connected-channel inventory.
- Collection channels are defaults. Post reads return effective channels: explicit post targets when set, otherwise the collection's assigned channels. Use the exact post's channels for its current audience; if the field is missing or inconsistent, obtain confirmation. The channel list alone does not establish whether a post inherits defaults when moving it.
- nuelink_get_schedule returns collectionStatus inside each schedule[day][] entry.

Resource requests are documented at 30 per minute per user, within a route limit of 60 per minute. Honor retry delays; reconcile uncertain writes before retrying.
