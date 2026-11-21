---
name: furnish-room
description: Furnish one named room of a Simple House Planner plan with items from the catalog, against its walls and with clearances. Use when someone asks to furnish or rearrange a room.
---

# Furnish a room

Tools: `list_projects`, `describe_plan`, `search_furniture`, `edit_project`, `open_editor`.

1. Find the plan with `list_projects` if the person did not name one in this chat, call `describe_plan` and find the room, its doors, its windows and its size.
2. Find items with `search_furniture`, for example "bed", "sofa" or "w:1200 table".
3. Place items with `plan.against(wall, offset, item, room)` so that their back, or a bed's head, stands against a wall. Keep 900 mm free in front of beds, sofas and counters, and keep door swings and windows free.
4. Free-standing items such as tables use `plan.furniture(floor, item, at, rotation)`.
5. Fitted furniture such as kitchen counters, wall cabinets, a pantry, closets, shelves, a bench seat or a desk uses `plan.alongWall(wall, start, end, style, room)`, from one offset along the wall to another; put a sink or hob from the catalog on a counter with `plan.against`.
6. Read the warnings in the result and fix every one before you finish: overlaps, door swings, furniture in the way through a door, cupboards, appliances and toilets without 600 mm free in front, tall furniture in front of windows, and a room that furniture cuts in two. Then call `open_editor`, unless the editor already shows the plan.
