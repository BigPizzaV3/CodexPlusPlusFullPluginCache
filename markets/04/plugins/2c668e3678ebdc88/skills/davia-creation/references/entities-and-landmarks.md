# Entities and landmarks

Entities are named actors that may move and act. Landmarks are named fixed
places. Choose the subject from its behavior in the game, not merely its name:
a mobile army is an entity; a fortress is a landmark; a province is a cell.

## Entities

Each entity object exposes:

- canonical `slug` after creation;
- editable `name` and `description`;
- editable `is_featured`;
- editable `placement`;
- editable stat overrides.

Descriptions should state who or what the entity is, its present position,
relationships, resources, constraints, and opening pressure. Do not address
the player as “you,” prescribe a future plot, or store engine instructions in
the description.

Every entity can become a playable role. Keep abstract concepts and generic
professions out of the cast unless an existing record intentionally represents
a specific organization or collective actor.

## Landmarks

Each landmark exposes a canonical `slug`, editable `name`, editable
`placement`, and editable stat overrides. The current virtual file does not
expose landmark descriptions or asset assignments.

A landmark should make sense at the board's scale. A capital can be useful on
a continental map; a private office usually belongs in context rather than as
a world-scale point.

## Placement

Placement has one of two complete shapes:

```json
{
  "starts_on_map": true,
  "cell_id": 42,
  "lng": 4.83,
  "lat": 45.76
}
```

```json
{
  "starts_on_map": false,
  "cell_id": null,
  "lng": null,
  "lat": null
}
```

For on-map placement, supply the existing containing `cell_id` and deliberate
longitude/latitude coordinates. Longitude is between -180 and 180; latitude is
between -90 and 90. Do not derive a point from a cell slug, array position, or
generic center when a real or deliberately authored location is known.

Coordinates are authoritative. If the point is inside the selected cell, Davia
stores that exact longitude and latitude. If it is outside, Davia moves it into
the selected cell. Choose the real or intentionally authored point first, then
use its containing cell; do not substitute the cell centroid.

Off-map placement is supported for entities and for existing landmarks. A new
entity may be created off-map. A new landmark must start on-map with a complete
`cell_id`, `lng`, and `lat`, because fixed places need an initial map position.
After creation, a landmark may be moved off-map intentionally.

## Create and delete

Before creating either kind, use `grep` and the current `entities.json` and
`landmarks.json` to check for an equivalent existing actor or place. Compare
meaning as well as exact spelling. Reuse and edit the existing object when it
already represents the requested subject.

To create, append one complete object with every exposed field. Use a
kebab-case placeholder `slug` derived from the name. The server creates the
record through the Creation Hub, derives its canonical slug from `name`, and
may add a numeric suffix on collision. Reread the file immediately so later
edits use the canonical slug.

To delete, remove the complete object from its array. This removes it from the
game rather than merely hiding it from the map; use an off-map placement when
the creator wants to keep an entity or existing landmark without displaying
it.

## 3D assets

The bundled catalog can recommend an existing `mapAssetKey`, but the current
virtual files do not expose that field. Do not claim to assign or change an
asset. If the creator requests it, give the exact recommendation and identify
asset assignment as a remaining Creation Hub action.
