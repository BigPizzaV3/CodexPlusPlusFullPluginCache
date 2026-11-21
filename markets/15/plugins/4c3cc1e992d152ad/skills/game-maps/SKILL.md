---
name: game-maps
description: Use for activating battle maps, uncovering rooms, inspecting Konva layers, or placing rectangles, character tokens and spell areas on a grid.
---

# Game maps and fog

Owners find maps with `list_maps`, add an imported image or video using `create_map`, and select the game-view source with `update_map` and `activate: true`. The Konva editor stores artwork, ordered shapes and fog strokes separately. `get_map_canvas` provides the owner with one page of saved layer bounds, grid settings and a snapshot. Follow `next_page` for more. Both the full canvas and unfogged `get_map_preview` are owner-only.

For “activate the map and uncover the first room,” use a named entrance layer or inspect the still artwork. Convert preview coordinates to original image pixels using the returned original width and height. For example, if a 1000-pixel-wide preview represents a 4000-pixel-wide map, multiply horizontal distances by four. Use known bounds for a video map and clarify an ambiguous entrance. Activate the requested map and call `set_map_fog` with `action: uncover`, `x`, `y`, `width`, `height` and the fresh snapshot. Fit each rectangle inside the room. Use returned snapshots for subsequent edits. The browser editor also supports freehand fog.

**Map layer editing is beta.** Use `edit_map_layer` for a rectangle, token or spell area. Rectangles use image pixels. Tokens use `gridColumn` and `gridRow`. One cell is 5 feet. Pixel X is the grid's X offset plus column times cell size. Pixel Y is the Y offset plus row times cell size. A 30-foot move right adds six columns regardless of screen zoom. The full canvas is for the DM. `get_map_token_positions` supplies the grid and narrowly scoped token positions for a character the member may place.

Read the saved position after a write. If another editor changes the map, reread the current snapshot and target before retrying. For overlapping shapes or an uncertain visual placement, use the Konva editor to check the result. The Player skill covers linked spell areas and relative token moves.
