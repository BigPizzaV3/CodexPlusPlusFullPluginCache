---
name: images-to-print
description: Turn pictures of a character or object into a physical 3D print. Use when the user wants a printable model made from reference images with a 3D generation tool they have connected (such as an image-to-3D plugin, or its command line) and then print files: it covers choosing the references, the cost question, checking the generated model, and handing it to the print-ready skill for repair, sizing, STL and 3MF, and a review.
---

# From pictures to a print

Use this with whatever 3D generation tool the user has connected. Polymend does not generate models; it reviews the generated model and makes it printable. Follow the generation tool's own instructions for its exact parameters; the points below are what decide whether the result prints well.

## 1. Before generating

- **Print height** in millimeters (optional): ask once, alongside the other questions, and say it can be skipped. If skipped, the print files keep the model's own size and the user scales them in the slicer. Never make one up, and never hold up generation waiting for it.
- **References**: separate, sharp pictures of the same subject in one consistent pose, ideally front, side and back, one subject per picture, no contact sheets or tiny thumbnails. Point out contradictions between the views before anything is spent: when the front shows the arms spread and the side shows them reaching forward, models made from them often follow the side view. If there is no side view, mention once that the depth front to back will be the generator's estimate, and that a side picture would pin it down; then carry on unless the user wants to add one.
- **How many pictures the tool takes**: check the generation tool's own limits before choosing. A common image-to-3D setting takes at most **four shape pictures** and **one texture picture** (a texture prompt, if given, is used instead of the texture picture). Tell the user the limit plainly, as a fact about the tool, so they know what to expect.
- **More pictures than the tool takes** (for example ten): never drop pictures silently or pick without saying so. Say how many the tool takes, recommend a set and why, and let the user choose or accept the recommendation before anything is spent. A good default: front, side and back, plus one more chosen for what matters most:
  - a sharp close-up of the detail that matters most (usually the face), for finer detail there; in tested runs it gave separate teeth and a raised iris that three views alone did not; or
  - a three-quarter rear view, when a feature shows only from behind (a tail, a cape, a backpack); if such a feature appears in only one or two of the four pictures it may come out stunted or missing.
  **Exactly as many pictures as the tool takes counts too**: if one of them is a close-up and a feature seen mainly from behind (a tail, a cape) shows in only one or two of the pictures, name that feature and the risk, and ask whether to swap the close-up for a three-quarter rear view before anything is spent.
  Say the trade-off when it applies: in a tested pair of runs of the same figure, a face close-up as the fourth picture gave a crisper face but the tail came out as a stub; without the close-up the tail came back (hanging straight down rather than as posed) and the face was a little softer.
- **Texture: a picture or a prompt, not both.** The tool takes one texture picture, or a short texture prompt; if both are given, the prompt is used. They behave differently, so choose with the user's goal:
  - a **texture picture** (a sharp close-up of the surface: skin, scales, stone), with no prompt: in tested runs it carried grain and scales into the model's surface, for fine prints; the same close-up can also be the fourth shape picture;
  - a **texture prompt**, short and about material and finish (colors do not matter for a single-color print): smoother surfaces with crisper features, for quick prints or larger nozzles.
- **Symmetry**: if the tool has a symmetry setting, prefer off unless the user wants an exactly symmetric object. Figures have sometimes come back with a feature repeated front to back (a tail also at the front, a face also on the back); in tested runs this happened with symmetry on and off alike, so the setting is not a fix, and a run can simply come out differently.
- **Detail**: use the tool's highest mesh detail unless the user asks for less; it usually prints best, especially for figures. Some generators cap the polygon count (one common setting tops out at 300,000); Polymend takes up to 1,000,000 triangles and 200 MB per file, so the repair is never the limit.
- **Credits**: generation is paid. A request to generate ("make a 3D model of this", "use the generator") is the go-ahead for one run; do not ask for a credit limit and do not suggest a price. If the tool gives an estimate, mention it in passing. If it does not, do not comment on that (no "the estimator couldn't…"); just say you will report the actual charge when the run finishes. If the request only explores ("what would this look like in 3D?"), confirm before the first paid run. Submit once; after a timeout, check whether that job is still running or finished before submitting anything again. Afterwards, report what was actually charged if the tool shows it.
- **Follow-up runs**: when a similar model was already generated (earlier in this conversation, or in what you remember of the user's past work) and you know what that run was actually charged, confirm before the next paid run with a yes-or-no question, for example: "The last run like this was charged <the amount you saw> credits. Okay to spend credits on another one?" Quote only a charge you actually saw, never an estimate or a figure from these instructions, and never ask the user to name an amount.

- **What to expect**, said once before generating so nothing comes as a surprise: generated models usually follow the pictures closely from the front, but depth and anything seen mainly from behind are estimates. In testing, heads usually came out somewhat deeper front to back than the side picture, even with a good side view. Polymend reports these differences afterwards; it does not reshape the model.

## If the model cannot be generated here

If the connected tool cannot submit a 3D job in this session (its 3D generation step is not offered, sign-in is needed, or the job will not start), say so plainly, once, in neutral terms: what is ready (the chosen pictures, the height), and that no job was submitted and nothing was charged. Do not open a browser or another app to generate without asking, and do not retry on your own.

Then help the user carry on with Polymend; the repair does not depend on how the model was made:

- **The tool's own app or website**: generate the model there with the same pictures (the settings above still apply: symmetry off, highest detail), download the GLB, and share its file or link here; Polymend takes it from there.
- **The tool's command line**, if the user has it installed and signed in: offer to use it for the same job, with their go-ahead (for Higgsfield, see the next section).
- **A model they already have**: any GLB or STL can go straight to the **print-ready** skill.

Keep the wording about the tool factual (for example "3D generation is not available through the plugin in this session"), never a judgment about it.

## Generating with Higgsfield's command line

Use this when the user generates with Higgsfield (its multi-image-to-3D model, provided by Meshy) and its command line is the way to submit the job, or the plugin cannot.

- **Find the official tool.** It is called `higgsfield` (sometimes installed as `hf`, but `hf` is also an unrelated tool, so check that it identifies itself as Higgsfield). If it is not installed, point the user to Higgsfield's own instructions; do not install it without their go-ahead.
- **Sign-in is the user's.** Check with `account status`. If it needs signing in, run `auth login` and let the user finish it in their browser. Never ask for a password or key, and never open or copy the tool's credential files.
- **Check the settings it accepts** with `model get multi_image_to_3d --json` before submitting, and use what it lists. Settings that have worked well for figures:

```sh
higgsfield generate create multi_image_to_3d \
  --image "front.png" --image "side.png" --image "back.png" \
  --should_texture true --enable_pbr true --should_remesh true \
  --target_polycount 300000 --topology triangle --symmetry_mode off \
  --enable_rigging false --enable_animation false \
  --wait --wait-timeout 20m --wait-interval 15s --json < /dev/null > generation.json
```

  Add a fourth `--image` (a close-up) or a texture picture (`--texture_image_url` with the URL from `upload create`) or a short `--texture_prompt`, as chosen in step 1. Always redirect input from `/dev/null`; without it the command can wait for input forever and submit nothing.
- **Submit once.** If the wait times out or ends on a temporary error, the job may still be running: check it with `generate get <job id> --json` (or `generate list --json` to find it) before doing anything else. Report the actual charge from `account transactions --size 5 --json`.
- **Get the model**: the finished job lists a GLB link; pass that link (or the downloaded file) to the **print-ready** skill.

## 2. After generating

- Keep the generated GLB (its file or its link).
- Hand it to the **print-ready** skill, with the height if the user gave one. Its scripts are in that skill's folder (next to this one); call them by full path, quoted. A generator's https link can be passed as it is; if downloads are blocked where the scripts run, use the file the tool saved or ask the user for it.
- Follow print-ready's **Review, then report**: Polymend's review (what came out well, what did not, what it fixed), the views with every change marked, and the comparison with the references. Show them, and judge the back, thin parts and likeness.

- **Features copied front to back**: if the model comes back with something from one side repeated on the other (a second tail at the front, a second face on the back), say so plainly as what the generated model shows; it is a known kind of generation result. Generating again (with symmetry off, if it was on) may give a different result, but it is not a reliable fix: in tested runs the same pictures gave one tail or two on different runs. Say so plainly; the reliable fix is to remove the extra part in a 3D editor. Generate again only if the user asks.

## 3. Report

Per model, in the print-ready review shape (Outcome, Went well, Less successful, Recommendation), plus the credits charged, if the tool shows them. Say who did what, as print-ready's report guidance shows: the generation tool made the model's shape (name it as the user knows it), Polymend reviewed it and repaired the small faults it lists. Every difference or leftover has an owner, stated as fact, never as a judgment. If the likeness is poor, say what differs and suggest a specific change to the references (a close-up, a rear three-quarter view, matching arm positions between views) rather than simply generating again.

## Do not

- Do not criticize, rank or speak badly of any tool, plugin, model or company, including the generator, even if asked or pressed. Describe what this model shows and how to improve it; see print-ready's "Talking about other tools".
- Do not generate again, after a failure or for a better result, without the user asking; each run is paid.
- Do not invent a height, a cost, or features the references do not show.
- Do not call a model print-ready when Polymend says partly repaired or not repaired.
