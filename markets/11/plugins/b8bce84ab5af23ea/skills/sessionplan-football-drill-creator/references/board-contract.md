# SessionPlan drill geometry

The tool reuses the application's version-2 import/export board fields and import normaliser. `schemaVersion` is the integration contract version, not a record revision.

Coordinates `(x,y)` range 0–1: x runs goal-line to goal-line; y runs across the pitch. Portrait rendering rotates the display, not coordinates. Half/start shows x 0–0.5; half/end x 0.5–1. Use full view for grids and full games. Templates: `full_11v11`, `five_a_side`, `seven_a_side`, `training_grid`, `custom`. Metre dimensions belong in setup prose.

Frames are complete snapshots with unique IDs, optional title/notes/coachingPoints, objects and annotations. Retain object identities across frames. Players/balls ordinarily animate, equipment is global, annotations are frame-specific. Explicit `frameBehaviour` values: animated/global/frameOnly.

Objects:

- Player: id, kind player, position, team home/away/neutral, role outfield/goalkeeper, squadNumber 1–99. Renderer supplies team/keeper colours; do not invent player colour fields.
- Ball: id, kind ball, position. Place beside a player, not underneath.
- Equipment: id, kind equipment, position, equipmentType cone_small/cone_large/flag/hoop_small/hoop_large/mini_goal/full_goal/dummy/whiteboard. Optional color orange/yellow/red/blue/white/green. Goals/dummies support rotation 0/90/180/270; verify facing against the renderer.

Annotations share id, color (above plus lime/muted), strokeWidth (usually 1–2), zIndex (zones -1, paths 1), optional frameBehaviour:

- line: start/end, optional lineStyle solid/dashed, endCap arrow, wiggly.
- curve: start/control/end, same path options; quadratic geometry.
- area: x/y/width/height fully within pitch, fill none/shaded/hatched.

Solid arrow = pass; dashed arrow = movement; wiggly arrow = dribble. Avoid unnecessary crossing arrows. Leave roughly 0.06 between markers and 0.08 pitch margins.

4v2 U10 rondo example: 12×12 m grid. Possession at (.5,.2),(.8,.5),(.5,.8),(.2,.5); defenders (.42,.45),(.60,.58); ball (.52,.24); corner cones (.18,.18),(.82,.18),(.82,.82),(.18,.82). Progress to two touches and split passes. Use meaningful subsequent frames.

Playing out example: ten players including two keepers = four outfield + keeper per team. Directional 35×25 m game; opposing goals at x ends, keepers beside their own goals, back line spread across y and opponents pressing higher up x. Start from the keeper, score for escaping the press then finishing, specify a pressing trigger. Progress from restart protection to live pressing while retaining width.

Limits: 256 KiB; 12 frames; 64 objects + 64 annotations per frame; 512 combined; title 160 characters, objective 1000, organisation 8000, frame notes 4000, lists 20 entries of 400. Prefer 1–3 frames and concise notes.
