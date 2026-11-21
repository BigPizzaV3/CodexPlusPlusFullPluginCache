---
name: contrast-checker
description: WCAG color contrast checker and accessible color palette generator. Use check_color_contrast for one text/background pair (ratio, AA/AAA, nearest passing colours), check_palette_contrast for every pair in 2-12 colours, and generate_accessible_palette for a 50-950 OKLCH scale with CSS variables and a Tailwind config.
---

# Zovo Palette Lab

Use `check_color_contrast` when the user asks whether a text, icon or border colour has enough contrast on a background, asks for a contrast ratio, or asks which text colour to use on a background.

1. Pass `foreground` (the text or icon colour) and `background` exactly as the user wrote them: hex, 8-digit hex with alpha, rgb(), hsl(), hwb(), lab(), lch(), oklab(), oklch(), color(display-p3 ...) or a CSS name. For a CSS variable, currentColor or a gradient, ask for the resolved colour (for gradients, check each stop). "White text on #F59E0B" means foreground `white`, background `#F59E0B`.
2. If the user mentions a text size or bold text, pass `font_size_px` (18pt = 24px, 14pt = 18.66px) and `bold` to get one verdict for that text.
3. Leave `adjust` unset unless the user says which colour may change; the tool then changes the more colourful one.

Use `check_palette_contrast` for 3 or more colours, or when the user wants to know which combinations in a palette work for text. Pass labels in `names` if the user gave them.

Use `generate_accessible_palette` when the user wants a colour scale, shades or tints, a Tailwind palette, or an accessible palette from one colour. Pass `name` if the user named the token (e.g. primary).

After a result, quote the ratio exactly as returned (it is truncated, never rounded up), say which levels pass or fail, and give the suggested fix or the download links. Present APCA only as draft, informational information, never as a pass or fail.

Do not use these tools for picking colours by mood, matching clothes or paint, recolouring images, reading colours from screenshots, or colour theory history.
