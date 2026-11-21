---
name: voyager-3d-blender
description: "Cloud: render with Blender on a Voyager cloud GPU machine: build or open a scene with a Python script, render stills, turntables and animations with Cycles on the GPU, and encode MP4."
---

# Blender on a Voyager cloud machine

Load `voyager-3d` first for leasing, files, jobs, cost and release. Every
machine has Blender (`blender`, the LTS release, and `blender-5.3`), ffmpeg
and Python. Blender runs headless (`-b`): there is no window, so the scene is
built or changed with a Python script and every result is a file you download.

Cycles renders on the GPU by default (OptiX, then CUDA), saved scenes
included; nothing needs enabling. A CPU render is only for a deliberate reason
and is far slower. EEVEE works too on `render`, `render-lite` and the
multi-GPU presets; never use Blender on `compute`, whose GPU has no graphics.
`blender --version` says which release a machine has.

## Plan the scene

1. Ask what the user wants to see: the subject, the look, the shot (still,
   turntable or animation), length and resolution.
2. Find the parts in the Voyager asset library before modelling anything
   (`voyager-3d-assets`): models, PBR materials and HDRIs, at real scale.
   `assets_guide` with `renderer` `blender` gives lighting rigs, camera
   lenses, material values and the draft, preview and final render settings,
   plus whole scene templates (product on a sweep, tabletop food, interior
   room, night street, outdoor nature, space) that build in one command on the
   machine.
3. The user's own model (GLB, glTF, FBX, OBJ, USD or STL) goes on the machine
   with `upload_files`; a `.blend` file works too.

## Build and render

Write the scene as one Python script, upload it with `upload_files` (as
`text`), and run it with `run_command`:

```sh
blender -b -P build_scene.py
```

A minimal script: clear the default scene, import the model, frame it, light
it, and render.

```python
import bpy, math
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath="/project/model.glb")
scene = bpy.context.scene
scene.render.engine = "CYCLES"
scene.cycles.samples = 64            # draft 16, preview 32, final 64-256
scene.cycles.use_denoising = True
scene.render.resolution_x, scene.render.resolution_y = 1920, 1080
scene.view_settings.view_transform = "AgX"
world = bpy.data.worlds.new("World"); scene.world = world
world.use_nodes = True              # an HDRI from the library lights it best
cam = bpy.data.objects.new("Camera", bpy.data.cameras.new("Camera"))
scene.collection.objects.link(cam); scene.camera = cam
cam.location = (0, -3, 1.2); cam.rotation_euler = (math.radians(75), 0, 0)
scene.render.filepath = "/project/out/still.png"
bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath="/project/scene.blend")
```

Save the `.blend` beside the render: the next change opens it
(`blender -b scene.blend -P change.py`) instead of rebuilding.

- **Still:** render one frame at preview settings, `download_files` the PNG and
  show it. Adjust, then render the final once and hand it over (`voyager-3d`,
  "Getting the files to the user").
- **Turntable:** parent the camera to an empty at the subject's centre and key
  the empty's Z rotation from 0 to 360 degrees over the frame range, with
  linear interpolation so the loop has no ease.
- **Animation:** set `scene.frame_start` and `scene.frame_end`, set
  `scene.render.filepath` to a folder with a frame pattern such as
  `/project/out/frames/f_####`, and render with `bpy.ops.render.render(animation=True)`.

Run any render longer than a few frames as a job (`run_command` with `wait`
off), follow `job_logs` (Blender prints each frame as it finishes), and tell
the user the frame rate you measure and the expected finish.

## Make the video

Encode the frames to an MP4 with ffmpeg on the machine:

```sh
ffmpeg -y -framerate 24 -i out/frames/f_%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 out/render.mp4
```

Then `download_files` the MP4 (it comes back as a download link) and one
frame as a PNG, so the user sees a still in the chat and can play the video.

## Quality and time

- Draft (about 480 px wide, 16 samples) for framing, preview (960 px, 32
  samples) for lighting, final (1920 px, 64 or more samples) once the user
  approves. `assets_guide` lists the exact values per tier.
- Time a preview frame before estimating a final: seconds per frame times the
  frame count, and say it is rough. Long animations go on `render-2x` or
  `render-4x`, one Blender process per GPU on its own frame range
  (`-s` start and `-e` end frames with `-a`), then one ffmpeg join.
- Real scale, AgX colour, light the scene instead of pushing exposure.
- A render that runs out of GPU memory can lose the machine
  (`MACHINE_RESTARTED`): lower the texture size or sample count, or use
  `render` (96 GB) instead of `render-lite` (24 GB).

## Deliver

Download what the user asked for: the MP4 or PNGs, and the `.blend` or an
exported GLB when they want to keep editing, and hand them over with the links
`download_files` returns (`voyager-3d`, "Getting the files to the user"; one zip
when they want it all).
List the credit lines of any library assets used (`voyager-3d-assets`). Then
release the machine as `voyager-3d` describes.
