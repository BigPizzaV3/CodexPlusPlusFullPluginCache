# Products with no model photo

## Finding them

Use this when the user asks which products have no photo of the garment being worn, or need a model photo.

1. Work from the products the user means. If they did not say, use every product you can see, not a subset you remember from an earlier conversation. Say how many you checked.
2. For each product, look at its photos. Decide from what the photos show, never from the title, tags, description or anything said earlier. A tag such as "flat" or "no model" is not evidence; look at the photos.
   - **On-model**: at least one photo shows the garment worn by a person. The product does not need a model photo.
   - **Garment only**: every photo shows the garment on its own: laid flat, on a hanger, on a mannequin or an invisible mannequin, or folded.
   - **Unclear**: a close-up, a detail shot, or a photo you cannot judge. Say so; do not guess.
3. List the garment-only products, each with a few words on what the photo shows ("laid flat on white", "on a hanger"). List the unclear ones separately. Then offer them with `show_products`, saying in one short sentence before the screen what each photo shows, so the user can pick which to make on-model photos for.
4. If you could only see some of the photos or some of the products, say which.
5. To look at many photos quickly, take the photo links from the product list, download them, and view them as contact sheets of up to 24 photos, each labelled with its product. Open a single product's details only when the list does not give its photos. Do not open every product one by one.

## Making an on-model photo

Only after the user asks for it.

1. Ask once, for the whole request, what the photos should look like: the model (or "similar to my other photos"), the pose, the background. Use the same choice for every product in the request, so they look like one shoot.
2. Make one image per product from its garment-only photo. One image generation per product, one file each. Give each generation only that product's own photo: never an image made earlier in the request, even for the same look. Similar products (two blue sweaters) borrow each other's colour and knit when they share a reference.
3. Compare the result with the garment photo before showing it, on each of these:
   - garment type and length (a tunic stays a tunic);
   - colour: compare it with this product's own photo, not with the other images in the request;
   - fabric and knit texture (a smooth rib stays smooth, not fluffy);
   - details that are made in a particular way (gathering, ruching, cable, lace-up): the same construction, not a different one in the same place;
   - pattern or print: shapes, scale and direction;
   - collar or neckline;
   - buttons, zips, ties and their number where visible;
   - pockets and which side they are on;
   - sleeve length and cuffs;
   - hem shape.
   Say any difference you see. If the garment itself has changed, make it again once.
4. Show the image for approval with `show_review`, and say that the model is AI-generated, and that how such images are labelled in a store is the user's decision.
5. When approved, the image is added as a new photo. It never replaces the garment photo.
6. Colour variants can then be made from the approved on-model photo, following the main instructions.
