# More than one product

## Small requests: up to 4 images

For up to 4 images in total (for example two products with one colour each), do not ask how to approve and do not use the per-product steps below. Say the plan once, make all the images, and show them in one `show_review` panel, as for a single product.

## Before starting (more than 4 images)

List the products you matched, by name, and say:

- the number of images (products times colours);
- the time estimate (about a minute and a half per image);
- that the user's own image limits apply, and that you will stop cleanly if one is reached.

If the user has not named the products, let them pick with `show_products`.

Ask once how the user wants to approve:

- **Each product**: you show a product's images and wait for a yes before moving on.
- **First product only**: you show the first product's images, and after a yes you carry on through the rest without stopping, showing each product's images as you go.

Then ask nothing more until the list is done, unless something fails.

## One product at a time

For each product, in order:

1. Make the images for that product, one per colour.
2. Check each image (`references/preserve.md`). Resize when the dimensions differ. Make an image again once if it fails.
3. Show the images for approval with `show_review`, called after the product's last image, and write no more than one short sentence after it.
4. If the user asked for the images to go into their store, do that for this product now (`references/publish.md`), including reading it back.
5. Only then start the next product.

Never prepare the store for products whose images do not exist yet. A product is either untouched or complete.

Do not stop between products to ask whether to continue. Do not stop to report progress. Keep a short running count in your replies ("4 of 12 done") and carry on.

## If you have to stop

A limit, an error or the user may end the run early. When that happens:

- Finish or undo the product you are on, so it is not left half done. If a colour's variants exist without their photo, say exactly which.
- Give the table below for what is done and what is left.

## When the user says "continue"

Do not rely on memory of the earlier run. For each product on the list, look at what is actually there:

- colours that already have their images and, if publishing was asked for, their variants and photos: skip;
- everything else: do it.

Never add the same image twice.

## Final table

When the list is done, or when you stop, give one table:

| Product | Colours done | Colours failed | Why |
|---|---|---|---|

If the images went into a store, fill the table from what the store shows when read back.
