# When the user asks for the images to go into their store

Follow this right after the user approves images, when store tools are connected, and only for the approved images. Use the store tools the user has connected. If a step cannot be done with them, say so and leave the files with the user.

## Before writing anything

Show the user what will change with `show_go_ahead`, with the approved images as files, for each product in the request:

- `create_colours`: the colours to be added;
- `attach_images`: the labels of the approved images to attach;
- `stays`: the colours left as they are, one name per entry, so that existing variants, prices, stock and photos are not touched;
- `existing_sizes_colour`: only when the product has no colour option yet, the colour name its current sizes receive, because adding a colour gives them one.

If a colour already exists on the product, its existing photos stay: say so, and propose no change for that colour unless the user asks for one. If a product is live in the store, say so in the chat sentence before the screen. Make no change until the user confirms in their own words in the chat, such as "go ahead". A click on a screen is not permission. If they choose Not now, make none.

Ask once, for the whole request:

- whether new variants should have SKUs, and in what pattern (default: none);
- the starting stock for new variants (default: zero).

## Order of work, per product

1. The image for a colour exists and is approved.
2. If the product has no variant for that colour, create one for each size the product already has, copying the price from the existing variants. Never create a colour's variants before its image is approved.
3. Add the image to the product.
4. Set that image as the photo of every variant of that colour.
5. Read the product back from the store.

Finish all five steps for one colour before starting the next colour, and finish one product before starting the next.

## Never

- Delete, replace or reorder existing photos.
- Change the price, SKU or stock of an existing variant.
- Change the product's status or where it is sold.
- Rename or remove an existing option or option value.

## Report

After reading the product back, report what the store shows, not what you intended: for each colour, the variants found and whether each has the new photo. Start with one line, for example "Done: Champagne added to Satin Blouse, 5 variants, photo attached." If something is missing, say so and offer to try that step again. Then offer up to three numbered next steps, such as another colour, another product, or seeing the product in the store.
