# Blender workflow

## Choose an execution route

Use only an integration's exposed operations. If a local executable and shell access are
available, Blender's Python API can create or inspect scenes without a UI. Match APIs to
the installed version; render engines, shader sockets and exporters can change.

Prefer direct data access for named objects and materials when scripting. Many operators
depend on the active object, editor and mode; establish their context before invoking them.
Never run a factory reset or blanket object deletion against the user's existing file.

With desktop controls, inspect the current screen and use the Outliner, Properties,
Shader Editor, Timeline and camera view. Panel positions vary; do not reuse guessed
coordinates. Verify selection and mode before making an edit.

## Project organization

Keep a project directory with the `.blend`, `assets/`, `renders/` and any scripts used.
Use readable names for objects, materials and collections so follow-up edits can target
them. Preserve existing names if other scene data depends on them.

Use relative paths where appropriate. Pack supported resources into the project, then
check what remains external: not every cache, linked asset or media file can be embedded.
Bundle those dependencies explicitly and verify the saved copy opens with them available.
Do not delete source media just because a pack operation succeeded.

## Images and materials

Distinguish a reference image from a material texture or background plane. Put reference
art outside the final camera/render if it is only a modeling guide. Map material textures
with suitable UVs or an intentional projection; inspect seams and stretching.

Use an image's color-space setting for its role: color artwork and numerical shader data
are different. Do not create a normal map simply by relabeling a color image. If deriving
an artistic bump signal from an image, describe it as an approximation and preview it.

Make a material copy before a change intended for only one object when multiple objects
share the original. Preserve node links and settings unrelated to the requested edit.

## Animation and rendering

Confirm the active camera, render engine, frame range, frame rate, output dimensions and
output directory. Keep the user's engine unless a capability requires a change; disclose
any change because it can alter appearance and render time.

Preview the start, middle and end of an animation. For a seamless turntable, also inspect
the last-to-first transition and interpolation. Use a small render to estimate the cost
of a full sequence and catch missing textures before rendering every frame.

For longer animation jobs, consider an image sequence so completed frames survive an
interruption. Encode a video only with a supported local route, and verify frame count,
frame rate and duration. Report partial frame ranges accurately if a render fails.

Command-line arguments execute in order: load the file, apply output settings, then render.
These examples require an available `blender` executable and real paths:

```sh
blender --background '/path/scene.blend' --python-exit-code 1 --python '/path/edit_scene.py'
blender --background '/path/scene.blend' --render-output '/path/renders/preview_####' --render-format PNG --render-frame 1
```

The edit script must explicitly save the working copy. Inspect exit status and logs;
then inspect the saved file and rendered output. Do not assume default paths or that a
render result still in memory has been written to disk.

## Installed-version documentation

Use the manual/API documentation for the installed Blender version when a command or
operation is uncertain:

- [Command-line arguments](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)
- [Packed resources](https://docs.blender.org/manual/en/latest/files/blend/packed_data.html)
- [Image Texture node](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/image.html)

These are reference links, not evidence that a particular local project was tested.
