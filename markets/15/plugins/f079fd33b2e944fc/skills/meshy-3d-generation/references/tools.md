# Meshy's hosted tools

Shared by the generation and print workflows. This file applies when the session lists Meshy's
hosted tools: `image_to_3d`, `text_to_3d_preview`, `get_task`, `download_model`, `get_balance`
and the others below. A host may list them with a prefix, as in `meshy_3d_image_to_3d`; they are
the same tools. They run on Meshy's servers under the Meshy account the user connected in
the host. Nothing is installed, and the CLI's login is not involved.

Each tool's own description and parameters are the contract: what it takes, the `request_id`
rules, the models to pair by project, what a refusal means. Read them there. This file adds what
they do not say: which tool a request needs, when to ask before spending, what to show, and how
the CLI continues from a model the tools made.

The local Meshy MCP server is something else: a separate package the user installed and gave an
API key. Its tools follow that server's own instructions, not this file.

Contents: what the tools do · pick the route · credits and consent · while it runs · show and
deliver · continuing on the CLI · when a tool refuses.

## What the tools do, and what they leave to the CLI

| The tools do | Tool |
|---|---|
| A model from a description | `text_to_3d_preview` (untextured), then `text_to_3d_refine` to texture it |
| A model from one picture | `image_to_3d` |
| A reference picture from a description | `text_to_image` |
| A new picture from a picture and a prompt | `image_to_image` |
| Texture an untextured model, or a model file the user has | `texture_model` |
| Send a file from the user's computer to Meshy | `create_upload`, where the host cannot attach the file itself |
| Find the user's models and pictures | `list_tasks`, `get_task` |
| Show a model or picture; open Meshy 3D | `show_model`, `open_meshy_studio`, where the host offers them |
| A download link as GLB, FBX, OBJ, USDZ or STL | `download_model` |
| The credit balance and what a create costs | `get_balance` |

The tools do not rig, animate or generate motion, remesh a model that exists, unwrap UVs, build
one model from several photos, convert to other formats (3MF, Blender) or convert a local file,
resize, check or repair printability, split a model into parts, make multicolor 3MF files, run
Creative Lab products, or open a slicer. Those are CLI steps:

- **With a terminal:** follow the skill's CLI route for them, as its *How to run it* says. When
  the `meshy` command is missing, the skill installs it; a missing command is not a reason to
  call the step unavailable.
- **Without a terminal, or once the CLI could not be installed or could not reach Meshy:** say
  that the step is not available in this environment. Never describe a model as rigged,
  remeshed, repaired or printable when no step did that. For a print, the STL download is the
  handoff; suggest checking it in the user's slicer.

## Pick the route

| The user has | Route |
|---|---|
| A picture attached in the host | `image_to_3d` with `image_file`, where the tool lists that parameter |
| A picture at a public link | `image_to_3d` with `image_url` |
| A picture on their computer, in a host that cannot attach it | `create_upload`, send the file as its description says, then `image_to_3d` with `image_upload_id` |
| A description and no picture | Recommend a reference picture first: `text_to_image`, show it, and once the user accepts it `image_to_3d` from that picture. The quicker alternative, with nothing to review, is `text_to_3d_preview` and then `text_to_3d_refine` when color is wanted |
| A sketch, silhouette, line drawing or logo | `image_to_image` into a shaded picture of the object, show it, then `image_to_3d` from the accepted picture |
| A reference picture that is close but not right | `image_to_image` from that picture, until the user accepts one: a new picture costs less than a new model |
| One of their untextured models (`texturable` is true) | `texture_model` with its `task_id` |
| A model file on their computer to texture | `create_upload`, then `texture_model` with `model_upload_id` |
| "My models", "the last one", "that fox" | `list_tasks`, then `get_task` |

- Know what the model is for before the first paid create, as the skill says. The tool
  descriptions carry the guide that pairs a geometry model and a texture model by project;
  follow it. A game asset or a face budget means a smart topology model with a polygon target,
  where the tool lists those models.
- A prompt describes one object: what it is, its shape, material and style, in plain words.
  Turn a vague request into such a prompt and say what you sent. For a reference picture,
  describe the object whole and unobstructed on a plain background.
- `image_to_3d` textures by default; pass `should_texture: false` when only the shape is wanted.
- Use only the parameters a tool lists. Never put a user's file on another host to get a link
  for it.

## Credits and consent

- `get_balance` returns the balance and `prices`. A call the list does not cover costs an amount
  that is not listed: say so instead of quoting a default price or guessing.
- The generation the user asked for proceeds. Before a paid step they did not ask for
  (texturing a preview they asked for untextured, another variant, a higher resolution, a
  rerun), say what it is and its price, and wait for their yes.
- When the balance is below the price, say so and do not start.
- When the plan also has CLI steps, give one price for the whole job: the tools' prices and the
  CLI steps' estimate ([Delivery](delivery.md), *Cost*) together, before the first paid create.
- A create is sent once. One answered `CREATING` or `RESULT_UNKNOWN` may still complete: resolve
  it with `get_task`, or by repeating the same call with the same `request_id`, as the tool's
  description says. Never start it again with a new `request_id` unless the user agrees to pay
  twice.

## While it runs

- Right after a create, call `show_model` with the `task_id` it returned, where the host offers
  that tool. Where it shows Meshy's card, the card follows the progress by itself; where it does
  not, report the progress in text.
- Call `get_task` when you need the result to continue, for example before `text_to_3d_refine`
  or before turning a picture into a model. A model usually takes one to a few minutes; check at
  a calm pace, not in a tight loop.
- `FAILED`: give its `error`. Trying again is a new paid create, so ask first.

## Show and deliver

- `show_model` presents a finished model or picture. `open_meshy_studio` opens Meshy 3D with the
  user's balance and newest models. When the host offers neither tool, or a result says
  `ui_enabled` is false, describe the task in text instead.
- A succeeded model's `formats` lists what `download_model` can make of it. Without `formats`
  there is nothing to download for that model here; say so, and do not guess the reason.
- Choose formats by use: game engines GLB or FBX; Apple AR USDZ; 3D printing STL; anything else
  GLB or OBJ. Download only what the user wants: a download counts toward the monthly allowance
  on plans that have one.
- A download link expires. With a terminal, save the file from the link to the path the user
  named (`curl -fL -o PATH URL`) and report where it is; without one, give the link. Thumbnail
  and picture links expire too; `get_task` signs fresh ones.
- Hand over the file or link, the task ID, and what was shown. The next request ("texture it",
  "now as FBX") continues from that task; generating again is a second charge.

## Continuing on the CLI

A model the tools made is a Meshy task like any other, and the CLI takes it by task ID
(`--input-task-id`). Do not download it and upload it again: some CLI steps, splitting into
parts for one, accept a Meshy task only and refuse a model file.

1. **Check the account before the first CLI step.** The CLI signs in separately from the host's
   connection, possibly to another account or to the China site, and the tools do not say which
   account they use. Read the task with the CLI; it is free:

   ```bash
   meshy image-to-3d get TASK_ID --format json --no-update-check
   ```

   The resource follows the task's `task_type`: `image-to-3d`; `text-to-3d` for a preview or a
   refine; `retexture` for a `texture_model` result. A task that is found means the same
   account: continue. `not_found` means the CLI is signed in somewhere else: ask the user to
   sign the CLI in to the account this host is connected to ([Setup](setup.md), section 3). Do
   not continue on another account's credits, and do not generate the model again there.
2. **Pass a task the step accepts.** The CLI reference for the step says which tasks it takes;
   read it before you choose. Some steps want the generation task, not a later texture result,
   and some refuse smart topology models.
3. **Then follow the CLI route** for that step: its reference, its cost estimate, its delivery.

## When a tool refuses

Tell the user what the tool's text means, in their language. A refused create made no model and
spent nothing.

- Never suggest upgrading, name a plan, or give a purchase or pricing link, even when a tool's
  text does. Say what is not available on their current plan and stop there.
- Give a price only when `get_balance` lists the exact price for this call.
- When the connection is no longer authorized, ask the user to reconnect Meshy in the host's
  settings, then repeat the call. Do not switch to the CLI to get around a refusal.
- For a queue limit or a temporary failure, wait and try again, with a new `request_id` for a
  create.
