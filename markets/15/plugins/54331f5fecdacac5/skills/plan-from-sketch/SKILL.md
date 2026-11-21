---
name: plan-from-sketch
description: Turn a photo of a hand sketch, an existing floor plan or a plot into a Simple House Planner plan. Use when someone shares a sketch, a plan image, or photos of a property.
---

# Plan from a sketch

Tools: `create_project`, `open_editor`, `edit_project`, `describe_plan`.

1. Look at the image. Say which rooms you read in it, and ask for one known length, such as the width of the house or of one room, to set the scale. Do not guess the scale.
2. Call `create_project` with a short title and `open_editor` with its `project_id`.
3. Work out the outer outline and the inner walls in millimeters from that length, snapped to whole 50 mm steps, with `y` pointing up.
4. Build with one `edit_project` call: `plan.walls(0, outline, {closed: true, thickness: 240})`, `plan.wall(0, from, to, {thickness: 120})` for inner walls, `plan.marker(0, name, point)` in each room, and `plan.door` and `plan.window` where the image shows them.
5. Call `describe_plan`, compare the rooms and their areas with the image, and fix what differs.
6. Tell the person which parts you were unsure of. Ask them to check them beside the image and to correct them by hand or in words.

## A plot with its land and buildings

When the image shows a plot, a site sketch or a photo of a property:

1. Take the lengths and the levels that the sketch states. Build the boundary with `plan.plot` and the slope with `plan.spot` heights along each contour line.
2. Model each building that stays as one `plan.shape`, from its size in the sketch and its look in the photo. It stands on the sloping ground by itself, so leave its `elevation` out.
3. Place trees with `plan.furniture`, and drives, paths and the street with `plan.surface`. They follow the ground.
4. Build the new house where the sketch shows it, with a terrace by `plan.platform` where the ground falls away.
5. Say what you took from the images and what you assumed.

A sketch is rarely to scale, so the result is a starting point, not a survey.
