# Copy for GifGen - Sticker Maker

> **Everything below is MY DRAFT, not the owner's words.** It matches the
> voice of `../plugin-skills-only/COPY.md` so nothing is blank at
> submission time. Replace any line you would have written differently —
> once you do, that line is fixed and is not to be paraphrased again.

## Listing — as entered in the portal

| Field | Value |
|---|---|
| Name | `GifGen - Sticker Maker` |
| Package name | `gifgen-stickers` — LOCKED by the portal at first upload. The display name changed to Image Sets; this did not, and cannot. |
| Subtitle (27/30) | `Turn any idea into stickers` |
| Category | `Creativity` (form) · `creativity` (submission JSON — lowercase enum) |
| Developer name | `GifGen` |
| Website URL | `https://gifgen.ai` |
| Customer support URL | `https://gifgen.ai/help` |
| Privacy policy URL | `https://gifgen.ai/privacy` |
| Terms of Service URL | `https://gifgen.ai/terms` |
| Version | `2.0.0` |
| Capabilities | `Read` |
| Submission type | **Skills only** — no MCP server URL, no domain verification |

Icons: `assets/icon-512.png` (directory, needs ≥256) · `assets/icon-128.png`
(composer, needs ≥48). Transparent background — verified to read on both
ChatGPT light and dark. The opaque variant on the GifGen backdrop is at
`assets/opaque/` if the directory ever looks wrong without a plate.

### Description

```
Describe any idea or send any photo and GifGen makes a whole sticker set out of it in one go: nine takes on the same character, each a different reaction, cut apart into separate images you can download — on transparent backgrounds when you ask for it
```

### Directory prompts (max 3)

Three constraints, all deliberate: no "sticker" (it is the word that makes
the model draw a die-cut outline, and a directory prompt is the user's
first message), no photo or pet-of-my-own framing (a reviewer clicking the
prompt has nothing to upload), and one of the three asks for no background
so the transparency toggle gets exercised.

```
Make a meme pack of a grumpy toaster having a very bad morning
Make a set of a tiny wizard frog casting increasingly chaotic spells, no background
Make a reaction pack of a raccoon trying on deeply questionable disguises
```

## Output message (after every set)

```
🎬 Done with the set
🎞️ [Download the separate images](IMAGES_LINK)
📂 [Download the whole set](SET_LINK)
Let's continue!
💡 Any new ideas or changes?

by [gifgen.ai](https://gifgen.ai)
```

Live copy the skill reads: `skills/make-image-set/SKILL.md`.

## Auth

**None.** No sign-in, no server, nothing runs outside the chat — a reviewer
gets a working set with no credentials. Say this explicitly; the GIF
plugin's reviewers asked.

## A note on the word "sticker"

The product IS stickers and says so everywhere a person reads it — the
name, the subtitle, the description, the directory prompts, the skill's
trigger description.

It must never reach the **generation prompt**. Told "sticker", the image
model draws a die-cut white outline around every subject, baked into the
pixels and unrecoverable. So the prompt template says "image" throughout
and describes the *subject*, never the *format*. "die-cut", "vinyl",
"decal" and "badge" are banned with it.

Users will type "stickers" — the directory prompts above do too. That is
fine and expected. The skill's job is to give them stickers without
repeating the word to the model.

## Test cases (the portal wants 3–5)

1. Plain set request — *"Make me a set of nine dancing avocados."* →
   `make-image-set` → 9 distinct images, backgrounds kept.
2. Transparency asked for — *"Make a set of ghost images with no
   background."* → `make-image-set --transparent` → alpha present, corners
   fully transparent.
3. Asked for as stickers — *"I need WhatsApp stickers of a grumpy cat."* →
   `make-image-set --transparent` → cut out, 512×512, under 100KB, with
   `tray.png` and `contents.json`, and **no white outline** on the subjects.
4. From a photo — user attaches an image and asks for a set of it →
   `make-image-set` with the photo as the reference → same character,
   different reactions.
5. Green screen named on an existing image — *"Remove the green screen
   from this picture."* with an attachment → `remove-green` → transparent
   PNG; nothing is generated.

## Negative test cases (the portal wants EXACTLY 3)

1. **A GIF, not a set.** *"Make me a GIF of a fox jumping over a log."* →
   must not trigger; that is the `gifgen-local` plugin's job.
2. **One image, explicitly.** *"Make me a single picture of a sunset."* →
   must not trigger; nothing here is asked to vary.
3. **A question, not a request.** *"What size are WhatsApp stickers?"* →
   answer it; do not generate anything.
