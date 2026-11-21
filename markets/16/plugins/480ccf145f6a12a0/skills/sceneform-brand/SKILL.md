---
name: sceneform-brand
description: Read, build, and edit Sceneform BrandKits and their products, and create or edit Personas, reusable AI characters or influencers made from a description or photos. Use when the user mentions their brand, website, products, colors, voice, a saved character, or wants content in their style. NOT for one-off media (sceneform-generate), ads (sceneform-ad-studio), or posting (sceneform-publish).
license: MIT
metadata:
  author: sceneform
  version: "0.11.0"
---

# BrandKits and Personas

A BrandKit is a brand's saved identity: name, website, summary, audience,
voice, colors, logo, and products. A Persona is a saved, reusable character
with a portrait and an optional default voice. Both exist so every
generation reads as the same brand and the same person. Read a reference
file by calling `load_skill` with this skill's name and the file's `path`,
or open it when this skill is installed locally.

## Read

All reads are free.

- `list_brand_kits`: every kit with `brand_kit_ref`, `name`, `status`,
  `summary`, `audience_summary`, `voice`, `voice_exemplars`, `colors`, and
  `products` (each with a `product_ref`, `name`, and `status`: `importing`
  while its page is read, then `ready` or `failed`).
- `get_brand_kit`: one kit, with `status` `building`, `ready`, or `failed`,
  and once ready its `logo_url`. `get_persona` reads one Persona the same
  way. Both take `timeout_seconds` (at most 40) to wait for one still being
  made. Reads never show a card. When the user wants to review a Persona
  and a BrandKit together, call `show_card` with just those two refs.
- `list_personas`: every Persona with `persona_ref`, `name`, `status`,
  `has_portrait`, and `has_voice`. Only a `ready` one goes into a
  generation.
- `list_elements`: saved Elements (reusable characters, locations, and
  props) with `element_ref`, `name`, `category`, `description`, and
  `image_count`. Pass `category` to list one kind.

## Use a brand in a generation

1. Read the kit before writing a prompt or concept for that brand. Turn its
   `summary`, `audience_summary`, `voice`, and `colors` into plain words in
   the prompt ("deep forest green and cream, calm and plain-spoken"), and
   quote a `voice_exemplars` line when writing copy.
2. Facts come from the kit or the user: claims, prices, label text, colors.
   A field the kit leaves empty stays out of the prompt.
3. A Persona, product, or Element goes into an image or video through
   `reference_refs` (`generate_image`, `generate_video`, `reshoot_video`,
   standalone ads). A Persona
   also works as `start_frame_ref` to animate its portrait, or as an
   avatar's `image_ref`.
4. Refs stay inside tool arguments. In prose, use the brand, product, and
   Persona names.

## Build and edit a BrandKit

These writes are free and save at once.

- `build_brand_kit_from_source` builds a kit from the brand's website or a
  social handle; prefer it whenever the user names one. A bare domain or
  "my brand" is a brand source. A product page link (`/products/...`) is a
  product: `add_product` into the brand's kit, and when there is no kit yet,
  build one from that site's domain first, then add the product to it. When
  the user gives only a brand name, ask for the link rather than guessing a
  domain.
- The build returns status `building`. When the request goes on to use the
  kit (an ad, a carousel, on-brand media, a report of what it learned), or
  no card follows it, wait in the same turn: `get_brand_kit` with
  `timeout_seconds: 40`, up to three calls in a row while it is `building`,
  then carry on. If it is still `building` after those, say it is on its
  way. When the kit is all the user asked for and a card
  (`card_offered: true`) follows it, say it is on its way and stop. Content
  made before the kit is `ready` ignores it. A `failed` kit can be built
  again from the same source.
- `create_brand_kit` makes a kit from an identity the user spells out:
  `name`, `website` (or null), `brand_summary`, and optionally the audience,
  voice, `voice_lines`, colors, and a logo `logo_ref`.
- `update_brand_kit` changes only the fields you pass; null clears a field.
  Logos, documents, and competitors stay on the BrandKits page.
- `add_product` imports a product from its page: `brand_kit_ref`, `url`,
  and `kind` `"app"` for software. It returns a `product_ref` with status
  `importing`; `get_brand_kit` lists it as `ready` once its name and images
  are read, or `failed`. Use a product only once it is `ready`. Adding the
  same page again re-imports it.
- Creating a second BrandKit needs an active subscription; relay that error
  as returned.

## Create a Persona

Create one only when the user asks for a persona, character, or AI
influencer they will reuse; a single image of a person does not need one.

`generate_persona` takes a written description (`prompt`) or 1 to 5 photos
of a real person (`source_image_refs`, never both), with an optional `name`
and default `voice_ref`. Write the description with
[references/personas.md](references/personas.md). Pass photos only after the
user confirms they have permission to use every face in them; photos come
from `search_library`, `import_media`, `open_upload`, or `attachments`.

It starts at once and returns a receipt with the credits charged; the price
depends on the number of photos. Pass `quote_only: true` when the user asks
what it costs or asked you to check before spending. Give a quote's summary
and credits and call `confirm_actions` after the user says yes; with
`card_offered: true` the host was also given a card with its buttons. The Persona finishes in the
background: `list_personas` shows it as `generating`, then `ready` or
`failed`. When the request goes on to use the Persona (a video ad with
them in it), wait in the same turn: `get_persona` with
`timeout_seconds: 40`, up to three calls in a row while it is `generating`,
then carry on. If it is still `generating` after those, say it is on its
way. A failed Persona's charge is refunded. Only a `generate_persona`
receipt that comes back `failed` names the amount, as `refunded_credits`;
`list_personas` and `get_persona` show just the status.

`update_persona` renames a Persona or sets its default `voice_ref` (null
removes it). It does not regenerate the portrait.

## Rules

- Use only refs the tools returned; never invent or edit one.
- When the user names a Persona that is not in the list, ask which one they
  mean, offer `generate_persona` for a reusable one, or make a one-off
  character with sceneform-generate.
- Relay errors as returned.

```sh
sceneform brand-kits
sceneform personas
sceneform elements --category location
sceneform persona --prompt "An outdoor cooking creator with curly hair" --name Alex
sceneform persona --photo front.jpg --photo side.jpg --name Alex
sceneform persona-edit tq1gwy1tsqrtzgkz3qaxr68jeyfk2dne --name Sam
sceneform brand-kit create --name Acme --website acme.com --summary "…"
sceneform brand-kit update 3nqab2wxtqwmvq8s4ejvsdsg44cp64sn --primary "#1D4ED8"
sceneform add-product 3nqab2wxtqwmvq8s4ejvsdsg44cp64sn https://acme.com/products/drill
```

The refs above are examples; use the ones `sceneform personas` and
`sceneform brand-kits` print. To check with the user first from the CLI, add
`--max-credits <n>` without `--yes`: the CLI prints the quote and exits with
code 2.
