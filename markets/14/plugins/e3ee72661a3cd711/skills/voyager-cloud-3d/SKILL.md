---
name: voyager-cloud-3d
description: "Cloud: generate 3D models with Voyager from a text description or a reference image, and retexture them."
---

# 3D models

Follow `voyager-cloud` (read it with `load_skill` if it isn't loaded) for account,
models, costs and jobs.

## Generate

1. Choose the model as `voyager-cloud` describes. The default makes a model from
   text, and from a reference image it makes one from the image. For another
   operation pass its `mode` (retexture, rigging, remesh, animations and more,
   all listed by `list_models` with `operation` 3d) and omit `model`.
2. For a specific object, import a clean reference image (one object, plain
   background, the whole object in view) with `import_reference` and pass its
   asset ID in `reference_ids`. To retexture, pass the finished 3D job as
   `source_job_id`. For a concept,
   describe shape, materials, style and intended use (game asset, product shot,
   print) in the prompt.
3. Call `generate_3d` and poll `get_job`. 3D jobs take several
   minutes.
4. Present the preview image and the downloadable formats the job returns (for
   example GLB). Say which format suits the user's tool; don't promise rigging,
   animation or formats the job did not return.
5. For an object or a person cut out of a photo, make its masks first with
   `generate_segmentation` (`voyager-cloud-image`, "Select objects"), then run
   `generate_3d(model="sam-3", mode="image-to-3d")` with `image` and `masks`
   in `parameters` (`image-to-3d-body` takes one person's `mask`).
