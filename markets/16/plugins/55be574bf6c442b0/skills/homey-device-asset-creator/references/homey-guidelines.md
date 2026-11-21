# Homey asset baseline

Verified against Homey Apps SDK App Store Guidelines on 2026-10-08.
Official source: https://apps.developer.homey.app/app-store/guidelines

## Driver images

Homey specifies individual driver images with a white background and a recognizable picture of the supported device.

Resolutions:
- Small: 75 × 75
- Large: 500 × 500
- XLarge: 1000 × 1000

Homey documents Small and Large as mandatory and XLarge as optional. This skill intentionally creates all three every time.

## Driver icons

Homey describes driver icons as clean vector-based drawings that accurately represent the device and remain recognizable at small sizes.

Key guidance:
- 960 × 960 canvas
- use the full canvas
- transparent background
- where possible, use an angle from the right side rather than a front-facing view to add dimension
- use lines and shapes to depict the device form
- avoid images, filled illustrations, gradients and background colours
- each driver should have its own unique icon

This skill adds the user's stricter project rule: visible SVG artwork must use black only (#000000).
