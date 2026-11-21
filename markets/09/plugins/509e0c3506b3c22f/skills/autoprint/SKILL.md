---
name: autoprint
description: "Print existing artwork on wall art, apparel, and personalized gifts through AutoPrint's MCP server."
---

# AutoPrint

Prepare artwork for printed wall art, apparel, and personalized gifts.

## Connect

Add AutoPrint's MCP server: https://autoprintstudio.com/mcp (Streamable HTTP, no sign-in).

## Print existing artwork

Use the person's public HTTPS image link as `artwork_url` and describe the requested product, size, or style in `idea`. The link must point directly to a PNG, JPEG, or WebP image under 25 MB. AutoPrint imports that artwork without generating a replacement. If the person has a file rather than a public image link, they can upload it in AutoPrint's studio.

## Artwork files and new designs

The MCP requires an existing artwork link and does not generate images. If the person has a file or wants to create new artwork, AutoPrint's studio supports uploads and artwork creation: https://autoprintstudio.com/studio.

## Preview and order

1. Call `start_design` with the appropriate inputs. It returns an id.
2. Call `check_design` with that id until the artwork is ready; it usually takes under a minute.
3. Show the artwork and studio link. The person previews the product, chooses the size, and orders on AutoPrint's website.

The tools do not place orders or take payment.
