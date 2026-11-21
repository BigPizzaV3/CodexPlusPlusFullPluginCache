---
name: voyager-3d-assets
description: "Cloud: find ready-to-render 3D models, PBR materials, HDRIs and character motions in the Voyager asset library and place them on a cloud machine, or bring the user's own files; keep versions and credits."
---

# Assets for 3D scenes

Load `voyager-3d` first for the machine itself. The Voyager asset library
holds ready-to-render models, PBR materials and HDRIs (CC0, real size in
metres, with previews) and motion clips for a humanoid mannequin. A library
asset is placed in seconds where modelling or generating one takes far
longer, so search before building anything.

## Find and place assets

1. `assets_search` with a short description, and `kind` (`model`, `material`
   or `hdri`) when you know it. Filters narrow it: `category`, `licence`,
   `max_tris`, `min_size_m` and `max_size_m`, `res`, and `kit` (a model kit is
   several separate pieces in one layout). Show the user the preview images
   and sizes of the best few hits. Each hit has a relevance `score`;
   `good_matches` says how many reach `min_score`. Zero means the library has
   nothing that really matches, whatever the list shows: say so rather than
   forcing a poor match. A hit's `variants` are other looks of the same shape.
2. `assets_show` for one hit's files, licence and credit.
3. `assets_resolve` pins exact versions (id@version) for a set of assets.
4. Place each one on the machine with the add command its search hit carries,
   run with `run_command` in `/project`. It puts the files under
   `assets/<id>@<version>/` and records them in the project's asset lock file
   (`voyager-assets.lock.json`); keep that file with the project, since it
   restores the same versions later.
5. Before delivery, run `voyager-cloud assets credits` on the machine and give
   the user the credit lines of every asset used.

`assets_guide` gives lighting rigs, camera lenses, material values, render
tiers for Blender and Vork, and scene templates built from library assets.
Call it before building a scene from scratch.

## Character motion

`motions_search` finds motion clips for the humanoid mannequin by what they
do (`intent`, such as idle, look, turn, sit, gesture or walk), `loop` and
`max_seconds`. Each hit states its `distribution`: an `open` or
`open_sharealike` clip has files its add command places on the machine; a
`composer_only` clip has none and cannot be downloaded. `motions_show` gives
one clip's timing, licence and credit. `motions_compose` turns a short
sequence of motions into a certified plan and, when every clip may be
redistributed, a Vork scene fragment. Keep each clip's credit and licence
with the work that uses it.

## The user's own files

Hosted chats reach the machine only through `upload_files`:

- Small files the user shares in the chat: `content_base64` (binary) or
  `text`, a few MiB per call in all.
- Anything at an https address: `url`. The server fetches it, up to 200 MiB
  per call. Any file with a download link goes on the machine this way; a 3D
  model generated here goes on with `place_3d_model` (`voyager-3d-models`).
- Large files without a link: ask the user for one (a shared storage link) or
  to make the file smaller.

Then import it in the scene: a GLB, glTF, FBX, OBJ, USD or STL model in
Blender, or as a mesh in a Vork scene.

## Rules

- Search the library first; generate (`voyager-3d-models`) or model only
  what it does not have (the user's own product, characters, stylised
  objects).
- Show previews and sizes before placing assets, and keep the lock file.
- Always deliver the credit lines with the render.
- A library asset's files stay on the machine. When the user wants them, zip
  the asset's folder, `download_files` the zip and give the link it returns
  (`voyager-3d`, "Getting the files to the user").
