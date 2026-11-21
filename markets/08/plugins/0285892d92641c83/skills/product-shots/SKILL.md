---
name: product-shots
description: Use this when someone has photographs of a real product and wants a consistent set of images out of them, such as product photos, catalogue shots, packshots, marketplace listing images, an Amazon main image, A+ content, an infographic, a white background set, a hero banner, lifestyle scenes or a seasonal refresh. Do not use it when there is no source photograph of the product, and do not use it for video.
---

# Product shots

Take the photographs a person already has and return a set that looks like it came from one shoot.

## When to trigger

Trigger on "product photos", "product shots", "packshots", "listing photos", "listing images", "Amazon listing", "main image", "A+ content", "infographic", "hero banner", "carousel set", "catalogue set", "on white", "lifestyle shots of my product", "make these look professional", or on someone sharing product photographs and asking for more.

Do not trigger for a video of the product (use make-a-video or the product demo route in run-a-preset), and do not trigger when the product does not exist yet.

## Ask for this first

Ask once, bundled:

1. A link to the photographs, or confirmation that they are already in their NOLGIA library. Up to four references can ride along on a single image.
2. The product name and anything that must read correctly, such as label text or a finish.
3. The set they want: plain white, a surface and a prop, a lifestyle scene, or all three.
4. The shape: square for a listing, vertical for a feed, wide for a banner.
5. How many.

The server needs a link it can open. If the person attaches a file to the chat rather than giving a link, tell them plainly that you need either a link or an image already saved in their NOLGIA library, and offer to work from the library.

## Steps

Presets first. Call `nolgia_list_presets` once (reuse the result if it is already in the conversation). If the catalog carries `product-photos` (hero shot on white, lifestyle, closeup with hands, hero banner, carousel directions) or `marketplace-listing-images` (main image, infographic, multi-angle, detail shot, lifestyle, what's in the box), open the one that fits with `nolgia_get_preset`, pick the direction that matches their words, bind the photographs to its reference field and run it with `nolgia_run_preset`. Only when neither is in the catalog do the direct steps below apply.

1. If the images are already theirs, call `nolgia_list_assets` filtered to images, then `nolgia_get_asset` on the ones they mean to get fresh links.
2. Call `nolgia_list_models` and pick an image model that accepts the number of references you plan to send. Several models take only one reference.
3. Call `nolgia_image_to_image` once per shot in the set. Pass the product photograph as `image_url`, and additional references as `image_urls` only on a model that accepts them. Set `aspect_ratio` from their answer. In the prompt, name the product exactly as it appears in the reference and require that it match the reference exactly, with no redesign, restyle, recolor or reinterpretation. Describe only the set, the light and the angle.
4. Look at every result before you deliver it. If the label, the shape, the color or the finish drifted from the reference, re-run that shot alone. Do not deliver a drifted product.
5. Call `nolgia_create_project` for the set, then `nolgia_add_project_assets`, then `nolgia_update_asset_tags` with something the person will recognise later, such as the product name.

## What to return

The set, grouped, with one line saying what each shot is for. Say which reference each came from. Offer one more angle or one more background.

Never name a model and never discuss what anything cost.

## When to stop or decline

- No usable source photograph: stop and ask for one.
- The photographs show a person's face and the person is not the account holder's own model: say you will keep the product in frame and crop or replace the person rather than reproducing them.
- The product carries another company's branding and the request is to pass it off as the person's own: decline.
