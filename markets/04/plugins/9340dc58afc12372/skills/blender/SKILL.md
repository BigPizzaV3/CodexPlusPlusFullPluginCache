---
name: blender
description: Build or edit Blender scenes using ImagineArt reference images and textures — objects, materials, lighting, cameras, keyframes and verified renders. Use for editable .blend projects, product turntables, 3D scenes and material work. Requires Blender app access, a supported integration, or a local Blender executable.
---

# Blender Studio

Deliver an editable `.blend` project and the requested render or export. ImagineArt can
supply reference images, texture artwork and backgrounds; build geometry and animation
in Blender. An image or video that looks three-dimensional is not an editable 3D asset.

Read `references/blender-workflow.md` before operating Blender, and
`references/qa.md` before delivery.

## Tokens

`/blender` `/blend` `/turntable` `/material` `/3d-scene`

Use this skill when the user wants to work in Blender or receive an editable 3D scene.
For only a generated product image, use Product Studio; for a rendered logo video without
an editable scene, Brand Studio already covers the task.

## Check access and inspect the project

1. Inspect available integrations for actual Blender operations. Do not assume a Blender
   MCP server, extension, or add-on is installed because this skill is present.
2. Otherwise use an available local Blender executable with Python scripting, or desktop
   controls. Follow the host's access and execution permissions. Check the installed version.
3. Inspect the existing file, active scene, object names, collections, materials, cameras,
   render engine, frame range, frame rate and output dimensions before editing.
4. If Blender access is unavailable, state that limitation. Offer a scene-building script
   or asset handoff, clearly marked unexecuted. Do not claim a `.blend` exists or spend
   generation credits on an alternative deliverable without the user's agreement.

## Establish the deliverable

Use the user's existing scene and settings for edits. For a new scene, establish subject,
scale, still versus animation, output dimensions and duration. Choose reasonable defaults
for unspecified visual details and state them. Ask about real-world dimensions when they
affect the task; do not infer accurate product geometry from a single photo.

Separate the editable project from any interchange export. If GLB, FBX or another format
is requested, inspect the installed exporter's support and verify that output separately;
modifiers, procedural materials and rigs may need format-specific preparation.

## Generate only missing assets

- Use existing user assets first. A change to camera, material color, text or keyframe
  timing normally needs no new ImagineArt call.
- Use `generate_image` for reference boards, background plates or texture artwork.
  Consult the current tool schema for valid model, resolution and aspect-ratio values.
- Use `request_image_upload` when ImagineArt needs a user-supplied image and the host
  requires its upload widget. Local Blender-only edits do not require uploading the scene.
- Resolve the ImagineArt organization as directed by the tool; use returned IDs rather
  than inventing them. For pending generations, follow the widget's polling flow or the
  current `fetch_status` tool contract on a host without widgets.
- Download completed outputs through available authorized file tools to stable project
  paths before using them in Blender. Never treat a remote URL as an imported local image.
- Request flat, evenly lit texture artwork where appropriate. Check tiling seams; a prompt
  asking for seamless output is not proof that it tiles. Do not represent an ordinary RGB
  image as a calibrated normal, roughness, displacement map, or HDR lighting environment.

## Build or edit

1. Save a working copy when modifying an existing project. Keep the source recoverable.
2. Build named objects in a task collection; retain editable text, modifiers and material
   nodes unless the requested output requires conversion. Never clear the whole scene as
   a routine setup step in an existing project.
3. Assign materials and image textures deliberately. Check UV placement, texture scale,
   image color-space role and missing-file indicators.
4. Place a camera, set its framing and focus, and light the subject. Use real lights or an
   appropriate environment for illumination; a generated background plate need not light
   the scene accurately.
5. For animation, keyframe only the requested objects or camera. Preserve existing actions.
   For a turntable, keep lighting stable unless the brief calls for moving lights, and
   check the loop boundary for a duplicate hold frame or a jump.
6. Render a small preview and inspect it before committing to the full render. Check
   framing, clipping, materials, readable text, shadows and animation at representative frames.
7. Save the `.blend`, bundle required resources, render/export, and reopen the saved project
   to verify the requested result. A successful script exit or a queued render is insufficient.

## Follow-up edits

Locate the existing object, material or action by name. Change only the requested property.
For "make the bottle blue," edit that material; preserve geometry, camera, lighting,
animation and other materials. Check whether the material is shared before altering it.
Do not rebuild the scene to make a local edit.

## Failure handling

Distinguish unsupported capabilities, missing files, render failures and ImagineArt refusals.
Stop on safety/content refusals; never switch models to bypass them. If the reason is
unclear, stop and clarify. Disclose model or output-setting changes used for a confirmed
capability limitation. Retry technical failures at most twice; do not duplicate pending
generation jobs or restart a full animation render blindly.

## Delivery

Provide paths to the `.blend`, bundled resources and final outputs. State what was actually
reopened, rendered and inspected, plus any missing dependencies or unverified outputs.
Never describe a script, viewport screenshot or reference image as a completed 3D project.
