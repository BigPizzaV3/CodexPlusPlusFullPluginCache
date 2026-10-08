# Delivery checks

- Reopen the saved `.blend`; confirm the active scene and camera are correct.
- Check for missing textures, linked libraries, fonts and caches. Verify the handoff's
  resource layout rather than relying on files elsewhere on the authoring machine.
- Confirm requested geometry, materials, text and animation remain editable.
- Inspect a rendered image for framing, clipping, seams, unintended transparency and lighting.
- For animation, inspect representative frames and playback; verify frame range, frame rate,
  duration and loop continuity where requested.
- Verify the actual exported file separately from the `.blend`, including expected geometry,
  materials and animation supported by that format.
- Check that unrelated objects, shared materials, actions and render settings were preserved.
- Report each unavailable check. Never report a preview as a final render.

## Follow-up checks

| Request | Expected behavior |
|---|---|
| Make only the product blue | Change its material; preserve other objects sharing the old material |
| Move the camera closer | Adjust the existing camera; preserve geometry and lighting |
| Shorten the turntable | Adjust timing/frame range, inspect the loop; do not regenerate textures |
| Export an existing scene | Inspect and export; no ImagineArt generation is needed |
| Build a scene without Blender access | Explain the dependency and offer a clearly labeled script/handoff |
