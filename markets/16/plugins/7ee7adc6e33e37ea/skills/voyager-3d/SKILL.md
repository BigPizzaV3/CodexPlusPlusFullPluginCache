---
name: voyager-3d
description: "Cloud: render 3D scenes, models and videos with Blender or Vork on a Voyager cloud GPU machine, and generate 3D models from a prompt or an image: estimate, lease, upload, render, show results, release. Load this first."
---

# Voyager 3D

A Voyager cloud machine is a Linux computer with an NVIDIA GPU, leased from the
user's Voyager workspace. Blender (Cycles on the GPU), Vork, ffmpeg and Python
are already installed, and the Voyager asset library is one search away. The
machine bills per second from when it is ready until it is paused or released,
so every step below keeps the GPU busy and releases it when the work is done.

Load the companion skill for the job: `voyager-3d-blender` for Blender
scenes, models and turntables, `voyager-3d-vork` for Vork renders,
`voyager-3d-assets` to find ready-made models, materials, HDRIs and
character motions, or to bring in the user's own files, and
`voyager-3d-models` to generate a 3D model from a prompt or an image and
render it. Without the plugin's skills,
`load_guide` returns the same guidance from the server (topics `machines`,
`vork`, `blender`, `assets` and `models`).

## Generated 3D models

`generate_3d_from_text` and `generate_3d_from_image` make a 3D model with the
user's credits, without a machine; `retexture_3d`, `remesh_3d`, `rig_3d` and
`animate_3d` work on a finished one. Each has an estimate tool that takes the
same arguments: estimate first and wait for the user's OK, run the tool once,
and poll `get_3d_job` until the job ends; never run it again to resolve a slow
job. `place_3d_model` copies the finished model onto a machine for Blender or
Vork, and the job's links download it. See `voyager-3d-models`.

## Who can use it

A Voyager workspace that is allowed to run the job and has enough balance. If a
call is refused with `PLAN_REQUIRED`, `VERIFICATION_REQUIRED` or
`INSUFFICIENT_CREDITS`, tell the user what the error says, give them the link
it includes, and stop. Never retry a refused create.

## Presets

| Preset | GPU | Use it for |
| --- | --- | --- |
| `render` (default) | RTX PRO 6000, 96 GB | Blender and Vork renders |
| `render-lite` | L4, 24 GB | Cheaper drafts and previews |
| `render-2x` / `render-4x` | 2 or 4 RTX PRO 6000 | Long renders split across GPUs (where the workspace allows it) |
| `compute` | H100, 80 GB | CUDA and ML work. No ray tracing: it cannot run Vork |

`list_presets` returns each preset's live cost and whether the user's workspace
runs it (`available`, `reason`, `required_plan`). If it can't, show the reason
instead of leasing it. Never quote a cost from memory: read it from
`list_presets`, `estimate_render` or the machine itself.

## Before you lease: estimate and confirm

1. `list_machines` first: if the user already has a ready or paused machine,
   reuse it instead of leasing another.
2. Estimate. For Vork, `estimate_render` with the frames (or `seconds` and
   `fps`), resolution and profile returns a time and cost range and, for long
   jobs, a multi-GPU recommendation. For Blender, read the preset's cost from
   `list_presets` and give a rough time from the scene size, saying it is rough
   until a preview has been timed.
3. Tell the user the GPU, the rough time and the rough total cost, and wait for
   their OK unless they already approved it. Offer `budget_usd` on
   `create_machine` as a hard spend cap when the user names a limit: the
   machine stops when it is reached.

## The loop

1. **Lease once.** `create_machine` with the preset (keep the `request_key` it
   returns: reusing it retries the same create safely after a timeout). Then
   `get_machine` with `wait_seconds` 50 until `status` is `ready` (usually under
   a minute). Keep this one machine for the whole conversation; don't lease one
   per step, and don't release it after a preview, since the user usually wants
   changes.
2. **Put inputs on it.** `upload_files` writes files under `/project`: `text`
   for scripts and scene files, `content_base64` for small binaries (a few MiB
   per call in all), or `url` for anything the server can fetch over https (up
   to 200 MiB per call). Unchanged files are skipped. `complete_upload` belongs
   to the direct-upload form, which needs a shell on the user's side; in a chat,
   use `text`, `content_base64` or `url`. Library assets are placed on the
   machine with a command instead (see `voyager-3d-assets`), and a generated
   3D model with `place_3d_model` (see `voyager-3d-models`).
3. **Run.** `run_command` with `wait` on returns the output and `exit_code`
   within about a minute. Run anything longer (renders, encodes) with `wait`
   off: it returns a `job_id` at once; follow it with `job_logs` and `get_job`
   (`wait_seconds` 50) until it ends, and tell the user how far it has got.
   `cancel_job` stops a job the user no longer wants. A non-zero `exit_code`
   means the command failed: read its output before retrying.
4. **Show results.** `download_files` with files or folders. Every file comes
   back with a download link, and PNG, JPEG and WebP images up to 4 MiB also
   appear in the chat. Render a still beside a video so the user sees a frame,
   show every preview before moving on, and hand the files over as "Getting the
   files to the user" says.
5. **Finish.** When the user says the work is done, download the final outputs
   and give the user their links (see below), then `release_machine`, and tell
   the user how long it ran and what it cost (it returns both). Releasing
   deletes the disk, so download or snapshot first.

## Getting the files to the user

The user's files are on the machine until you release it, so hand them over
first:

- Give the user the link `download_files` returns for every deliverable (the
  final PNGs, the MP4, the GLB, the `.blend`), not only a preview in the chat.
  Never claim a link that was not returned.
- To give everything from the session in one step, zip the outputs on the
  machine (`python3 -m zipfile -c outputs.zip out/`), `download_files` that one
  zip and give its link.
- Links open in any browser, with no sign-in, save under the file's own name
  (an image, MP4 or WebM opens in the browser) and last 2 hours, also after the
  machine is released. Releasing deletes its disk, so give the links before
  you release and tell the user they expire.
- A generated model's links last 10 minutes; `get_3d_job` returns fresh ones.
- Never print, decode or paste a base64 result or a large file's content;
  use its link.

## Pausing, snapshots and ports

- A machine with no command, file transfer or busy GPU (above 10%) pauses by
  itself after its idle timeout (15 minutes unless `idle_timeout_seconds` says
  otherwise). Work started in the background keeps the machine while it keeps a
  GPU busy; CPU-only work does not, so run it as a command or raise the timeout.
  `pause_machine` pauses it now. A paused machine does not bill for compute and
  keeps its disk.
- A paused machine stays paused: `run_command`, `upload_files` and
  `download_files` answer `MACHINE_PAUSED`. Resuming bills again, so ask the
  user, then `resume_machine`, wait with `get_machine` until ready, and retry.
- `snapshot_machine` saves the disk; `create_machine` with `from_snapshot`
  starts a new machine from it later, scene and assets in place.
- `open_port` serves a web viewer or preview running on the machine at a
  private https link. Anyone with the link can open it while the machine runs,
  so share it only with the user.

## When a machine is lost

If `get_machine` shows error `MACHINE_RESTARTED`, the machine was lost (for
example, a render ran out of memory) and restarted on a new one. Tell the user
plainly what happened and what was lost or restored (the message says), check
`/project`, re-upload or re-run what is missing, and only then continue. Act on
each loss once: the error stays until the machine's next resume. A job with
error `MACHINE_LOST` died with its machine: say so and re-run that step.

## Rules

- Confirm the GPU and a rough cost before leasing; report the real time and
  cost at release.
- One machine per conversation. Never leave a machine running without telling
  the user it is still running and using credits.
- Previews first, final quality once: a few frames or a low resolution to check
  framing and lighting, then the full render after the user approves it.
- Run long commands as jobs (`wait` off), never as `nohup … &` inside a short
  command: only jobs are tracked, so a process that dies in the background is
  never reported.
- Never put secrets in a command line; pass them in `env`.
- Everything happens on the machine: paths are machine paths under `/project`,
  and results reach the user only through `download_files`.
