# Homey Device Asset Creator

Turn device reference photos into product images and vector icons for Homey app drivers.

## Get started

1. Select **Homey Device Asset Creator** in a new ChatGPT Work conversation.
2. Attach a clear photo of your device. Add front and side views if you have them.
3. Ask: **“Create all Homey driver assets from this device photo. Clean it up first.”**
4. Download the finished files individually or together in a ZIP.

## What you receive

| File | Format |
| --- | --- |
| `small.png` | 75 × 75 pixels |
| `large.png` | 500 × 500 pixels |
| `xlarge.png` | 1000 × 1000 pixels |
| `icon.svg` | Black vector artwork with a 960 × 960 viewBox |

The PNGs show the same device on a white background, at three sizes. The SVG uses native vector lines and shapes on a transparent background. The ZIP contains the four production files. You can ask for fewer files if that is all you need.

## Getting a good result

Use a photo that shows the complete device and its important controls. Include its model name if you know it. Choose the product variant you want when supplying several references.

The workflow preserves the visible design and simplifies small SVG details for readability. If a photo leaves an important feature unclear, ChatGPT may ask for another view.

## Using it in ChatGPT

Image processing and file creation use the tools available in your conversation. In cloud ChatGPT Work, processing runs in ChatGPT's provided execution environment. You do not need to install Python, Pillow, Inkscape or CairoSVG on your own computer for this workflow.

Use a conversation with image editing and file creation available. If an operation cannot be completed with the available tools, ChatGPT will explain what is missing.

## Example

See `assets/preview.png` for a reference photo, its previously cleaned product image, and the corresponding vector icon.

Created by Johan Bendz for the Homey community.

## Privacy policy

https://bortbytt.se/privacy-policy/
