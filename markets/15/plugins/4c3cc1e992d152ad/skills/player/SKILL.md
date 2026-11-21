---
name: player
description: Use when a player claims a character, places or moves its token on the shared map, or attaches a spell area to it.
---

# Player actions

Find the player character with `list_characters`. When claiming is enabled, `claim_character` links it to the signed-in player’s accepted membership. If the campaign allows player creation, `create_character` links the new player character automatically. A Read grant lets the player inspect a claimed token. Claiming, placing and moving need Write or Maintain.

Read `get_game_screen` for the visible active map, then `get_map_token_positions` with that map ID and the claimed character ID. It returns grid size, pixel offsets, token layer IDs, their columns and rows, and a snapshot. Owners inspect full artwork and fog. Use the character-specific lookup for player moves.

For “move my character 30 feet right,” select the matching token. On the 5-foot grid add six to `gridColumn` and keep `gridRow`. Call `edit_map_layer` with `action: update`, the token’s layer ID, the snapshot and the changed column. If there are two tokens for the same character, use their positions to clarify which one to move. If there’s no token, `action: create` accepts `type: character`, the character’s `placeableId`, and the requested grid cell on an enabled grid. Reread the positions to verify the move. Layer editing is beta.

For a 10-foot aura, create an `area-effect` with `effectType: radius`, `radiusFeet: 10` and `parentId` set to the token’s layer ID. A linked effect moves with the token. Cubes take `sideFeet`, cones take `lengthFeet` and `directionDegrees`, and lines also take `widthFeet`. Use 5-foot steps from 5 through 120. Keep the effect’s returned layer ID for later edits. Removing its parent token removes the linked effects.
