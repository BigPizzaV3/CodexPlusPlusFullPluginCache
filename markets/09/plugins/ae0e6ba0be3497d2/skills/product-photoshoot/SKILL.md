---
name: product-photoshoot
description: Make product photos of the user's real product, from clean packshots to lifestyle scenes. Use when the user asks for a product photoshoot, product photos or packshots, their product on a white or plain background, in a lifestyle scene, in a flat lay or held by a person, or images for a store or marketplace listing.
---

# Product photoshoot

Use this skill to turn a product into a set of finished photos that show the real packaging. Explicit instructions from
the user always take priority over this skill, including the scenes, sizes, number of shots and style they
name.

## The product
1. Call `list_product_photos`. These are the brand's saved product photos: use them, and never ask the user to
   upload one again.
2. If none is saved, ask for a photo of the product (a link, or a file the user shares). `upload_file` turns a file
   into a link. Then call `set_product_image` with it: it checks that the photo clearly shows the product and saves
   it as the brand's product. If it is rejected, say why and ask for a clearer shot.

## The shoot
1. Agree the shots: how many, the setting for each (studio white, a kitchen counter, outdoors, on a model, a flat
   lay), and the size (1:1 for a store listing, 4:5 for a feed post, 9:16 for a story). Say how many images you
   will make before you start, because each one uses credits.
2. Call `generate_image` once per shot, with a prompt that names the product, the setting, the light and the
   framing, and the `aspectRatio`. The saved product photo is used automatically, so the real packaging appears.
3. To change one detail of a finished photo (the background, the light, a prop), call `edit_image` with the image
   and a plain instruction. Everything else in the photo stays as it is.

## Output
Show the photos (the Hermoso card displays them) with one line each. They are in the user's Hermoso Library;
`save_to_drive` saves copies to Google Drive when the user asks and Drive is connected.

## Credits
Each image uses credits from the user's Hermoso account, and the tool reply says how many. If the balance is too
low, say so; credits are managed in the user's Hermoso account. Never start a purchase.

## Do not
- Do not invent product details, labels, claims or prices that are not on the real product.
- Do not change the product's shape, colour or packaging unless the user asks.
