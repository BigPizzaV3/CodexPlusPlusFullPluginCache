---
name: voyager-3d-vork
description: "Cloud: render 3D videos and stills with Vork, Voyager's open-source GPU renderer, on a Voyager cloud machine: scene, previs preview, estimate from the measured speed, final render, multi-GPU split."
---

# Vork on a Voyager cloud machine

Load `voyager-3d` first for leasing, files, jobs, cost and release.
Vork (https://github.com/voyager-so/vork) is Voyager's open-source headless
3D renderer for agents. It is installed on every machine as `vork` and needs a
ray-tracing GPU: use `render` or `render-lite` (or `render-2x` / `render-4x`
for a long render), never `compute`. Make a video (MP4) unless the user asks
for a still. `load_guide` with topic `vork` returns this guide from the server.

## Estimate first

Call `estimate_render` with the `frames` (or `seconds` and `fps`),
`resolution` and `profile` (`std/final` for the finished render) and tell the
user the GPU and the rough time and cost it returns for the whole job. It also
lists the same job on the other presets the workspace runs and recommends a
multi-GPU preset when it saves real time. Before a scene has a preview its
numbers are rough, since scenes vary about tenfold.

**Long renders go on one multi-GPU machine.** More than about 2 minutes of
single-GPU time, or a final render over about 100 frames, goes on ONE
`render-2x` or `render-4x` machine with the split recipe below, not on several
single-GPU machines.

## The loop

1. Once per machine: `run_command` with `vork setup` (seconds on the default
   image). Run vork from `/project`, the default working directory.
2. `vork help` explains the scene format; example scenes are in the
   repository's `examples/` folder. `vork --version` gives the installed
   version: a scene written for an older Vork may need porting
   (`vork help upgrade`).
3. Write the scene, upload it with `upload_files`, and render a quick check
   with the `std/previs` profile: a few frames or a low-resolution pass of the
   video.
4. `download_files` the output folder and show the user the result: a PNG
   preview appears in the chat; for a video, give the link and also render
   one still so they see a frame. Revise and repeat.
5. After the first preview of THIS scene, call `estimate_render` again with
   `from_job` set to that render's job id: it scales this scene's own measured
   speed to the final frames, resolution and profile (basis `this_scene`).
   Tell the user if the time or cost changed a lot.
6. Render the final once with `std/final` (or `std/path` for interiors and
   glass) as a job (`run_command` with `wait` off), follow `job_logs` (Vork
   prints frame N/M), and re-estimate the finish from the measured seconds per
   frame once the first frames are done.
7. Download the final and give the user its link before you release the
   machine (`voyager-3d`, "Getting the files to the user").

Library assets, HDRIs and character motions go into Vork scenes too: see
`voyager-3d-assets`. `motions_compose` returns a Vork scene fragment for
a certified sequence of mannequin motions.

## Split frames across GPUs

On `render-2x` or `render-4x`, render a separate frame range on each GPU at
the same time, then join the parts. Upload this as `render.sh` and run it as a
job (`sh render.sh` with `wait` off):

```sh
vork setup
N=$(nvidia-smi -L | wc -l); F=240           # GPUs; total frames (0..F-1)
per=$(( (F + N - 1) / N ))
run=$(mkdir -p shot-parts && mktemp -d shot-parts/run.XXXXXX); pids=
: > $run/parts.txt
for g in $(seq 0 $((N-1))); do
  a=$((g*per)); b=$((a+per-1)); [ $b -ge $F ] && b=$((F-1)); [ $a -gt $b ] && continue
  mkdir -p $run/$g
  vork render shot.json --gpu $g --frame-start $a --frame-end $b --out $run/$g/shot.mp4 &
  pids="$pids $!"; echo "file '$g/shot.mp4'" >> $run/parts.txt
done
failed=0; for p in $pids; do wait $p || failed=1; done
[ $failed = 0 ] || { echo "a part failed; see its log" >&2; exit 1; }
ffmpeg -f concat -safe 0 -i $run/parts.txt -c copy $run/shot.mp4 && echo "joined: $run/shot.mp4"
```

Each GPU's part goes in its own folder, since Vork locks a render's output
folder. Select GPUs with `--gpu`, never with `CUDA_VISIBLE_DEVICES`.

## Rules

- Estimate and confirm before leasing; re-estimate after the first preview.
- Previews with `std/previs`; the final render once.
- Run every long render as a job, never as `nohup … &` in a short command.
- If the machine is lost mid-render (`MACHINE_RESTARTED`), tell the user,
  re-upload what is missing and re-run the render.
