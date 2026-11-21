---
name: on-brand
description: Use when the user asks to design, write or build something in the style of a named brand or website (landing page, slide, mockup, email, social post). Looks the brand up in WikiBrand and applies its real logo, colors, typefaces and tone of voice.
---

# Build on-brand

1. Identify the brand's website domain from the request (for example "Stripe" is stripe.com). If the brand is ambiguous, ask which website the user means.
2. Call `get_brand` with that domain. A website WikiBrand has not read yet takes about a minute; tell the user it is being read.
3. Apply what the tool returns, and nothing invented:
   - Colors: `colors.brand` for accents and calls to action, `colors.page` for the background, `colors.ink` for text, `colors.palette` for secondary accents.
   - Type: `typography.display` for headings and `typography.text` for body copy. If the font is not freely available, name it and fall back to a close system stack.
   - Logo: use `logo.svg` inline or `logo.url` as an image, on the ground given by the logo object.
   - Voice: match the copy to the `voice` traits (each a value between two poles, such as Serious to Funny).
   - Code: for HTML or CSS, start from `variables`, the brand's theme as CSS custom properties.
4. If a field is null, say it was not found on the website instead of guessing.
5. Do not present the result as official brand material, and do not give trademark or usage-rights advice.
