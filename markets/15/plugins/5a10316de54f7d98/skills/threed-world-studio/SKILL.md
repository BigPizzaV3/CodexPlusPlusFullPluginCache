---
name: threed-world-studio
description: "Use when the user wants to create, open or stage a CinAI 3D World: characters, props, cameras, lights, environment and camera moves."
---

# 3D World Studio

1. Find or create.
   - `list_3d_worlds` lists the user's 3D World projects with their links.
   - `open_3d_world` returns one world's scene summary and its `https://cinai.tv/3d-world/<world_id>` link.
   - `create_3d_world` makes a new world. Set `title`, `ratio` and `duration` (5 to 60 seconds) from the request.
2. Stage the scene. Call `update_3d_scene` with `world_id` and `commands` such as `add_character`, `add_crowd`, `add_prop`, `add_camera`, `add_light`, `set_environment`, `set_aspect`, `set_duration`, `animate_character` and `animate_camera`. To stage a 3D node on a Canvas, also pass its `node_id`.
3. Ask before replacing. If a change would remove or replace parts of a scene the user already built, describe it and wait for a yes.
4. Share the link from the tool result so the user can open the scene, preview it and render shots on cinai.tv.

Prefer explicit `commands` you can describe to the user. A free-text `prompt` (on create) or `pending_prompt` (on update) is carried out by the CinAI 3D Director only when the user opens the world on cinai.tv; say so when you use one.
