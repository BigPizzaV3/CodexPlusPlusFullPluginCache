---
name: image-to-stl
description: Turn a logo, outline, sign or line art into a 3D-printable STL with TechDraw AI. Use when the user wants to 3D print, emboss or extrude a flat image.
---

# Line art to STL

## Steps

1. Use the image the user shared. Flat, high-contrast art works best: logos, silhouettes, outlines, text.
2. Ask for the size and thickness if they matter, and pass `size_mm` (the longest side) and `thickness_mm`.
3. Call `image_to_stl` with the image (free). The card offers the STL download.

## Tips

- For a real 3D object from a photo, use the photo-to-3d skill instead.
- Raise `min_feature_mm` if thin details would be too fragile to print.
