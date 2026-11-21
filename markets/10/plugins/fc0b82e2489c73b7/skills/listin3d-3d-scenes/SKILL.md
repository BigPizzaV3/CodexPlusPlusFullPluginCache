---
name: listin3d-3d-scenes
description: Prepare a GLB model or a Three.js/HTML 3D scene for a Listin3D product listing and send it with the Listin3D connector. Use when a seller wants a 3D model, 3D scene or Three.js view of their product on Listin3D, or asks to upload, import, send or attach a .glb or .html 3D file to a listing.
---

# Send 3D to a Listin3D listing

Listin3D lists products with interactive 3D. A seller can attach one private 3D proposal to each of their listings: a self-contained GLB model or a single-file HTML scene such as Three.js. Listin3D staff review it, place it in a scene and publish it with the listing. Nothing you send is public until then.

## 1. Check requirements and the listing

For example scenes before creating a listing, call `list_3d_experiences`. These are conceptual demonstrations, not published product offers.

1. Call `get_3d_requirements`. If `seller_uploads_enabled` is false, tell the seller 3D uploads are paused and stop.
2. Call `list_my_submissions` and ask which listing the 3D is for. If the seller has none, help create one with `get_listing_requirements` and `create_listing_draft`. Never invent product details.
3. A listing's `scene_proposal` shows any existing proposal. Sending a new valid file replaces it.

## 2. Prepare the file

Choose the format from what the seller has or wants:

- **Product model** (furniture, a device, a vehicle): a GLB. Listin3D places it in a studio, home or street environment.
- **Complete experience** (a room, a building walkthrough, a configurator, custom lighting): a single-file HTML scene.

GLB rules:

- One binary glTF 2.0 file with embedded buffers and textures. No external `.bin` or image files.
- Real-world size in meters, +Y up, with the model resting at its true scale. Listin3D never rescales a model.
- Up to 50 MB; aim for 5 to 15 MB for phones. Draco, Meshopt and KTX2 compression are supported.
- In a code sandbox, export with Three.js `GLTFExporter` (`binary: true`), Blender (`export_format='GLB'`) or trimesh, then check the file as described below.

HTML scene rules:

- Start from `references/threejs-scene-template.html`. It already has the required readiness snippet, visibility pause, resize handling and orbit controls.
- One UTF-8 document, up to 5 MB (1,000,000 characters to send as text). Load libraries only from absolute HTTPS URLs that allow CORS, such as `cdn.jsdelivr.net`, or inline them. Local side files are not uploaded.
- Compile React or TypeScript to plain HTML first. The scene must create its own renderer, camera, lights, floor and controls.
- It runs in an isolated sandbox without same-origin access, cookies, storage of the parent page, popups, forms or top navigation. Don't rely on those.
- It must post `{ type: "LISTIN3D_READY" }` to its parent. Without that, staff cannot preview it, and Listin3D rejects it.

Before sending a file you created in a sandbox or on the user's computer, run the checker. Replace `ACTUAL_SKILL_FOLDER` with the local directory containing this `SKILL.md`, using the location provided by the skill loader:

```bash
python3 "ACTUAL_SKILL_FOLDER/scripts/check_3d_file.py" path/to/file.glb
```

The checker needs only Python 3 and reports problems plus the transfer method to use. Fix every reported problem before sending. If the host does not expose a local skill folder or code execution, use the supported MCP transfer or website flow and explain that the local checker could not run.

## 3. Confirm with the seller

Before sending, ask the seller to confirm both:

- They have the right to share and use this file in the listing.
- It replaces any earlier 3D proposal for that listing.

Pass `rights_confirmed: true` only after they confirm. Use a new UUID as `request_id` for each distinct file, and reuse it only to retry the same file.

## 4. Send it

Pick the first method that fits:

| Situation                                                              | Tool                                                                                         |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| You wrote or hold the HTML scene text                                  | `submit_3d_scene_html` with the full document as `html`                                      |
| The user attached the file in ChatGPT, or it is at a public HTTPS link | `import_3d_file` (`file.download_url`, `file.file_id`)                                       |
| The file exists only in your code sandbox or on the user's computer    | `create_3d_upload_link`, then run the returned `command` once                                |
| None of the above works                                                | Give the seller the `website_url` from `get_3d_requirements` to upload it in their dashboard |

Notes for `create_3d_upload_link`:

- Pass the exact `size_bytes`, up to 30 MB; a larger GLB (up to 50 MB) needs `import_3d_file` from a public HTTPS link or the website. The link works once and expires after 15 minutes. Don't show it to anyone else.
- A code sandbox needs outbound network access to `listin3d.com`. If the upload fails with a network or DNS error, explain that the user can allow that domain for code execution in their assistant's settings, or download the file and upload it on the website.
- For GLB models you may pass an optional `suggestion` with an environment (`studio`, `home`, `street`), navigation (`orbit`, `fps`) and placement. Staff make the final choice.

## 5. Report the result

- Success returns `scene_proposal.status: "ready_for_review"` and `proposal_published: false`. Say the file was received for team review. Never say it is published or approved.
- For a draft or revision listing, use `get_my_listing` to read its version. The seller can add selected photos or plans with `import_listing_files`, then explicitly approve `submit_listing_for_review`; use the account skill for this workflow. Also share `listing_url` for the web editor.
- If a tool returns an error, follow its instruction. Don't retry a validation error with the same file.
- Check progress later with `list_my_submissions`.
