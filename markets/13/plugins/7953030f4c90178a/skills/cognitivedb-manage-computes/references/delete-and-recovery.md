# Compute Deletion and Recovery

Use this reference before deleting or after any ambiguous Compute mutation.

## Delete

Resolve one immutable ID and obtain an authoritative current snapshot. Use list
for discovery or ambiguity and describe when an immutable ID is supplied or list
evidence is incomplete. Before confirmation, show resource type, exact name and
ID, current Space, state, configuration, visible
dependencies, and declared cascade behavior. State any dependency or cascade
information that the live tools cannot inspect. Confirm the exact target,
delete once, then list and verify that exact ID is absent.

## Ambiguous Outcomes

After a timeout, transport error, or lost response, inspect the exact ID before
retrying. Never repeat create, update, set-default, start, stop, suspend, or
delete until evidence proves the first request did not take effect. If mutation
and read-back evidence conflict, report an uncertain outcome and correlation
information instead of claiming success or broadening the target.
