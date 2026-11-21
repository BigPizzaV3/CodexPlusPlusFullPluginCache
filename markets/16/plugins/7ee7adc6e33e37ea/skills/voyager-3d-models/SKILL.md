---
name: voyager-3d-models
description: "Cloud: generate a 3D model from a prompt or an image with one of Voyager's 3D models, then put it on a cloud GPU machine and render it in Blender or Vork, or give the user its download links."
---

# Generate a 3D model

Voyager's 3D models make a textured mesh from a prompt or one image, and
retexture, rig, animate or remesh a mesh they made. The result is a GLB with
other formats beside it, ready to render on a Voyager cloud machine. Load
`voyager-3d` first when the model goes on a machine. `load_guide` with topic
`models` returns this guide from the server.

These tools make 3D models only: no image, video or audio generation.

## Pick the model

`list_3d_models` with no arguments gives Voyager's recommended 3D models, one
marked default (Meshy 7.1); omitting `model` uses it. When the user
names a model, find it with `query` (for example `tripo`, `rodin`, `hunyuan`
or `trellis`) and use exactly that one; if it is not listed, ask the user
rather than substituting another. `get_3d_model` returns one model's 3D tasks:
for each, the tool that runs it, its estimate tool, the settings it accepts
and its credit rates.

## One tool per task

Each task has its own tool and an estimate tool that takes the same arguments:

| Task | Tool | Estimate with | Starts from |
| --- | --- | --- | --- |
| A model from a prompt | `generate_3d_from_text` | `estimate_3d_from_text` | `prompt`, up to 600 characters |
| A model from an image | `generate_3d_from_image` | `estimate_3d_from_image` | `image_ids`: one image, or two to four views of the same object |
| A new texture | `retexture_3d` | `estimate_3d_retexture` | `source_job_id` and a `prompt` for the new look |
| A new mesh at a face count | `remesh_3d` | `estimate_3d_remesh` | `source_job_id` |
| A skeleton for a character | `rig_3d` | `estimate_3d_rig` | `source_job_id` |
| Animations on a rigged character | `animate_3d` | `estimate_3d_animation` | `rig_job_id` and `action_ids` |

Models from a prompt: `Meshy 7.1`, `Tripo H3.1`,
`Rodin 2.5`, `Hunyuan3D 3`. Models from an image:
`Meshy 7.1`, `Tripo P2`, `TRELLIS 2`,
`Idol`. Retexture, remesh, rig and animate run on
Meshy 7.1 and take a finished 3D job of its own.

The two generation tools take a few optional settings, each a named argument:
`polycount` (target face count), `quads` (a quad mesh), `pbr` (PBR maps, from
an image), `pose` (`a-pose` or `t-pose` for a character) and `seed`. A model
takes only the ones `get_3d_model` lists for it; another is refused with
nothing charged. Leave them out unless the user asked.

A character to animate: generate it with `pose` `t-pose` and `polycount`
100000 (rigging takes at most 380,000 triangles; `remesh_3d` with `polycount`
100000 fixes a larger mesh), then `rig_3d`, then `animate_3d` with the rig
job.
`action_ids` are ids from the model's animation library: use the ones
the user gives, and ask for them rather than guessing.

## An image to start from

`import_3d_image` with an https link imports one image and returns its
`file_…` id; pass it in `image_ids`. The link can be a public image the user
gave, or the download link `download_files` returns for an image on a cloud
machine (an image rendered or made there). Only images are accepted.

## Estimate, confirm, run once

1. Call the task's estimate tool with the arguments you will run it with.
   Tell the user the model and the credits it estimates, and wait for their OK
   unless they already approved it. If it says the workspace cannot run it,
   tell the user what it says and stop.
2. Call the task's tool once with the same arguments, and a `client_key` so a
   retry after a timeout returns the same job instead of a second one. It
   waits about 20 seconds and returns the job.
3. Poll `get_3d_job` with `wait_seconds` 25 until the state is `succeeded` or
   `failed`; most models take one to a few minutes. Tell the user it is still
   working. Never run the tool again to resolve a slow or `unknown` job:
   report it and check the same job later.
4. When it succeeds, show the user the preview and the download links (GLB and
   the other formats; links last 10 minutes, `get_3d_job` gives fresh ones).
   The charge it reports can differ from the estimate.

## Put it on a machine and render

1. Lease or reuse a machine as `voyager-3d` describes.
2. `place_3d_model` with the machine, the job and a `format` (`glb` by
   default; the job lists the others) copies the model onto the machine at
   `models/<file name>` under `/project`, or at the `path` you give.
3. Render it: in Blender, import it with `bpy.ops.import_scene.gltf` in a
   build script (`voyager-3d-blender`); in Vork, use it as a mesh in the scene
   (`voyager-3d-vork`). Light it with a library HDRI and add a ground or a set
   from the library (`voyager-3d-assets`).
4. Show the preview, revise, render the final, give the user the render's link
   and the model's links (fresh from `get_3d_job`), and release the machine
   when the user is done.

A change to the model itself (new texture, mesh, rig, animation) is another
job, made by that task's tool from the finished one; estimate and confirm it
like the first.

## Rules

- Estimate and get the user's OK before every tool that spends.
- One run per request; poll the job, never resubmit it.
- Only the models `list_3d_models` lists, and exactly the one the user named.
- Give the user the download links for anything they want to keep, before you
  release the machine. A model's links last 10 minutes; `get_3d_job` gives
  fresh ones.
