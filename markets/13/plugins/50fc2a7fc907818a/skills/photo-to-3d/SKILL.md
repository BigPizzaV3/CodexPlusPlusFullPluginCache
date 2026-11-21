---
name: photo-to-3d
description: Turn a product photo or a technical drawing into a 3D model (GLB and STL) with TechDraw AI. Use when the user wants a 3D model, an AR preview, a 3D print of a real object, or an asset for Blender or a web viewer.
---

# Photo or drawing to 3D model

## Steps

1. Ask for a photo of one object, ideally on a plain background at a three-quarter angle. A TechDraw AI drawing works too.
2. Tell the user it costs 80 credits and needs the Studio plan, and call `get_credits` if they are unsure of their balance.
3. Call `photo_to_3d` for a photo, or `drawing_to_3d` for a technical drawing.
4. The card shows progress and offers GLB and STL downloads when the model is ready, usually in 2 to 4 minutes. If it does not update, call `check_job` with the `job_id` every 15 seconds.

## Tips

- Crop out other objects; the model is built from the whole image.
- Set `textured: false` when the user only needs clean geometry for printing.
