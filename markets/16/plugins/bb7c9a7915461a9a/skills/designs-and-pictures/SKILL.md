---
name: designs-and-pictures
description: Choose Frexy's designs for new pages, and bring pictures into a Frexy website: stock photographs, the person's own photos and logo, files from their computer, 3D models, and a site or picture they want theirs to look like. Use when they ask for a new page, a design, a picture, a logo or a model.
---

# Designs and pictures

1. **A new page** starts from a design they choose: `show_designs` with that kind
   of page, then `add_page` with the one they pick. Offer only Frexy's designs and
   never choose for them. The agent then fills it with the business's own words.
2. **Something to look like.** A website they name, or a picture of one, is a
   reference: `capture_reference`, then `view_reference`. Build it as real pages;
   never put a picture of a page on the site.
3. **Stock photographs**: `search_images`, then `import_image` the one that fits.
4. **Their own pictures**: `add_image` with a file they attached, an address or SVG
   (a logo with `use: "logo"` goes into the header and Settings). A file only on
   their computer comes in through `request_upload`; `get_upload` returns it.
5. **3D models**: `search_models`, then `import_model`.
6. A picture on the site is always Frexy's: `write_files` refuses one loaded from
   another website, so bring it in first. Give every picture alt text that says
   what it shows.
