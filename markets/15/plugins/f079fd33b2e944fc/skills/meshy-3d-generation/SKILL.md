---
name: meshy-3d-generation
description: "Generates and edits digital 3D assets with Meshy: text-to-3D and image-to-3D models, reference images, texturing, remeshing and LODs, UV unwrapping, format conversion (GLB, FBX, OBJ, USDZ, STL, 3MF, Blender), rigging, animation and motion clips from text. Uses Meshy's hosted tools first and the Meshy CLI for what they do not do. Use when the user asks to make, texture, rig, animate, convert, find or download a 3D model or game asset. For physical 3D printing use meshy-3d-printing."
license: MIT
compatibility: "Hosted tools: a host connected to Meshy's MCP server, nothing to install. CLI steps: a terminal with network access, Node.js 22.12+ and the Meshy CLI 0.8.x, 0.8.5 or later (npm install -g meshy-cli@0.8.5)."
---

# Meshy 3D Generation

Turn the user's request into a delivered asset. Completion means the requested files in the
requested location, or their download links where the host has no file system, and an available
preview inspected. Login or task submission alone is not completion. Choose the shortest
suitable pipeline and reuse existing assets for follow-ups.

## How to run it

Meshy is reached two ways: its hosted tools, and the Meshy CLI. **Use the hosted tools first;
the CLI is for what they do not do.** See which this session has before anything else.

| This session has | Run |
|---|---|
| Meshy's hosted tools (`image_to_3d`, `text_to_3d_preview`, `get_task`, `download_model`, `get_balance`; a host may list them with a prefix, as in `meshy_3d_image_to_3d`) | Generation, reference pictures, texturing, lookups, downloads and the balance through the tools: [Tools](references/tools.md) |
| The tools and a terminal | The same, plus the CLI for what the tools do not do: rigging, animation, motion, remeshing and LODs, UV unwrapping, multi-image-to-3d, conversion, resizing, and steps on a local model file. When the `meshy` command is missing, install it; that is the normal first run, not a reason to decline |
| The tools and no terminal | The tools only. For a step they do not do, say that it is not available in this environment |
| A terminal and no Meshy tools | Everything through the CLI: the CLI sections below and their references |

**The tools not offering a step never means Meshy cannot do it.** With a terminal, a step the
tools lack is a CLI step: run `meshy --version`, install the CLI when it is missing, and check
`auth status`, all as *CLI: first use and authorization* says. Do this before telling the user
that anything is unavailable.

The CLI counts as not working only after that was tried: the install was refused and the
temporary package failed too, or the terminal cannot reach Meshy (a sandbox without network
access, for one). Then say which of these happened, and that the step is not available in this
environment.

Choose the path when you plan the job, and say in the plan which it is:

- **The tools cover every step** (make, texture, find, show, download): the tools.
- **The request already names a CLI step** (a character to rig, an LOD chain, several photos of
  one object): set the CLI up first, then run the whole job on it. Its recipes set options at creation
  that the tools do not have, such as the pose of a character to rig, and its steps chain by
  task ID.
- **A CLI step comes up later**, on a model the tools made: the CLI continues from that model's
  task ID. Tools, *Continuing on the CLI*, says how, and how to check first that both are signed
  in to the same account.

## Read what this request needs

| Need | Reference |
|---|---|
| The hosted tools: routes, credits and consent, progress, delivery, continuing on the CLI | [Tools](references/tools.md) |
| CLI runner, credentials, or output location | [Setup](references/setup.md) |
| CLI generation and the models to pair for a project, texturing, remeshing, conversion, scale, or 2D images | [Pipelines](references/pipelines.md) |
| Rigging, animation, or generated motion (CLI) | [Animation](references/animation.md) |
| CLI cost, waiting, preview, delivery, or finding a previous model | [Delivery](references/delivery.md) |
| Failed or uncertain CLI operation | [Troubleshooting](references/troubleshooting.md) |

Read the relevant section when needed; recipes are examples to adapt to the requested result,
not a requirement to execute every stage. An untextured model skips texture generation; an
existing GLB needs no extra format conversion. Use command help when parameters are uncertain.

## Before any paid create

These hold on the tools and on the CLI alike.

- Know what the model is for before the first paid create: a game asset, a character to rig, a
  render, a 3D print. If the user hasn't said, ask once; the answer picks the route and the
  models. A game asset or a face-count budget means smart topology, not a standard model
  remeshed down.
- Without a usable photo, recommend making a reference image first and building the model
  from it; text-to-3d is the quicker alternative.
- Continue work within the user's approved scope and budget. Propose additional paid stages
  or reruns before spending.
- Submit a create once and follow that task to its end. A timeout or an unknown submission does
  not authorize another paid create.

## CLI: first use and authorization

In DeepSeek Harness with the Meshy plugin (`DSH_MESHY_CLI` is set) run every command as
`"$DSH_MESHY_NODE" "$DSH_MESHY_CLI" …`, never a `meshy` on PATH, install nothing, and sign in with
the `meshy_sign_in` tool. Everywhere else run `meshy --version` before the first command, without
asking; when it is missing or older than 0.8.5, install it with `npm install -g meshy-cli@0.8.5`
and say so in one line ([Setup](references/setup.md), section 1).

**Keep the CLI current.** An older CLI lacks commands these references use. A version older than
0.8.5 is upgraded before anything else, not worked around; say which version it replaced. Once
per conversation, unless you installed it just now, also look for a newer 0.8 release
(`npm view meshy-cli@0.8 version --json`; the last entry is the newest). When there is one,
recommend it to the user in one line with its command, `npm install -g meshy-cli@VERSION`, and
run that when they agree. Do not hold the job for the answer.

Reuse a verified session. If login is needed, run `auth login --device` (with `--region cn` for a
user in mainland China) as Setup, section 3 describes: show its URL and user code in
**commentary/progress, not a final answer**, wait on that same command in this turn, verify
`auth status`, then continue the original request. Browser approval stays with the user;
credentials never belong in chat, and only the CLI touches its config directory.

## CLI: execution boundaries

- Run API, upload, download and mesh operations through the CLI. Local inputs have a 50 MiB
  limit, and a local model must be GLB or glTF (rigging, UV unwrap and multicolor: GLB); use the supported
  URL input route for anything else.
- Use `--format json --no-update-check` on every command: stdout is one `meshy.cli/v1` envelope,
  auth included. Resolve `WORKSPACE` from the user's output
  path and pass it to writes.
- The route and the models for a purpose are in [Pipelines](references/pipelines.md), with
  *Start from an image* for a request without a photo.
- Submit once with `create --async`, retain the owning resource and ID, then `wait` on that
  task. Keep the agent turn active while awaiting a running command. Follow Troubleshooting
  on timeout or unknown submission.
- Delivery specifies estimates and balance checks.

## Deliver

Download only needed assets. Inspect and show a preview when available; a missing preview
must not prevent delivery or be described as inspected. On the CLI, Delivery covers
earlier-stage preview lookup and actual charges. Report the result and any concrete
limitation; a rendered image does not establish topology quality or provide a 3D viewer.
