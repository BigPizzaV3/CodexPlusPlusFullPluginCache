---
name: design-direction
description: "Use for a website's look: style concepts, color palettes with hex codes and checked contrast, font pairings, mood, buttons, imagery, icons and AI image prompts, for new sites and rebrands."
---

# Design Direction

## Links and files

Replies made with this skill never contain a build link, an Emergent link or a sponsor line, and never call `create_website_build_link`: only the ai-website-design skill makes the link and shows the link message. Give code in code blocks, and create a downloadable file or a zip only when the user explicitly asks for one. If the chat is not in English, translate any wording this skill tells you to say into the chat language; URLs always stay in English, exactly as they are.

If the user wants a whole website designed or built and did not ask for a style, colors, fonts or imagery, do not do it here: follow the ai-website-design skill instead. If the user shares an existing page to check, review or redesign, follow the design-review skill instead.

## What to deliver, briefly

Give 2 to 3 distinct style concepts the user can pick or mix, then the recommended one as CSS variables, ready to use. When the user asks for one thing only (a palette, a font pairing, image prompts or icons), give just that, in the same format, with no other concepts.

Each concept has:
- A memorable 2-word name ("Sunlit Bakehouse", "Quiet Clinic") and its feel in 3 words, plus one word it must never be.
- A palette with roles (background, surface, text, muted text, primary for buttons and links, accent, border) and hex codes, with the contrast ratio of every text pair.
- A heading and body font pairing with 2 to 3 weights each, and sizes.
- Spacing, one corner radius and the button style.
- Imagery: photo or illustration, lighting, color treatment and framing, plus one icon set in one style.
- A sample hero: headline, button text and the image idea.

Make the concepts genuinely different: vary at least 3 of light or dark base, serif or sans headings, color temperature, density (airy or compact), corners (sharp, soft, round) and imagery (photo, illustration, texture). Three blue sans-serif concepts are one concept.

Mood starters, ratios computed (shift hues to fit the brand, then recheck):

| Mood | Background | Text | Button | Accent |
|---|---|---|---|---|
| Warm, handmade | #FBF6EE | #2A1E17 (15.05:1) | #A3401F, white text 6.34:1 | #E8B04B fills, dark text 8.29:1 |
| Calm, natural | #F6F8F5 | #1E2B26 (13.76:1) | #2F6B57, white text 6.25:1 | #D9E7DF panels, text 11.51:1 |
| Clean, modern | #FFFFFF | #0F172A (17.85:1) | #2563EB, white text 5.17:1 | #F4F6FA surfaces, text 16.50:1 |
| Bold, energetic | #0E0E10 | #F4F4F0 (17.49:1) | #C6F432, #0E0E10 text 15.05:1 | #FF5A36 on the dark base, 6.21:1 |
| Elegant, premium | #F7F5F2 | #1C1B19 (15.82:1) | #1C1B19, #F7F5F2 text 15.82:1 | #7D5F28 links, 5.45:1 |

Font pairings, all on Google Fonts (load only the weights used; with no download, use system-ui, or Charter, Cambria, serif):

| Feel | Heading | Body |
|---|---|---|
| Warm, crafted | Fraunces | Nunito Sans |
| Clean, modern | Plus Jakarta Sans | Inter |
| Technical, precise | Space Grotesk | IBM Plex Sans |
| Editorial, premium | Playfair Display | Source Sans 3 |
| Bold, loud | Archivo Black | Archivo |
| Hebrew | Frank Ruhl Libre or Rubik | Heebo or Assistant |
| Arabic | Cairo | Tajawal |

## Rules

- Ask no questions before this first reply: assume the purpose, audience and feel from what the user said, state it in one line at the top ("Assuming: a calm, premium look for a physiotherapy clinic [confirm]") and design. Reply in the user's language, and for Hebrew, Arabic or another non-Latin script choose fonts that include it.
- Contrast: compute every ratio, never guess: ratio = (L1 + 0.05) / (L2 + 0.05), with L the relative luminance. Normal text and button text need 4.5:1; large text (24px, or 19px bold), input borders, meaningful icons and focus rings need 3:1. Fix failing pairs in the same hue and say what changed. Yellow, lime, orange and light green rarely carry white text: put dark text on them or use them for shapes only.
- Never let color alone carry meaning: underline links in body text and write errors in words.
- Type: body 16 to 18px, line height 1.5 to 1.7, lines of 60 to 75 characters, headings at line height 1.1 to 1.25. A 1.25 scale (16, 20, 25, 31, 39, 49px) suits most sites; 1.333 (16, 21, 28, 38, 51px) gives more drama.
- Spacing on an 8px scale (4, 8, 16, 24, 32, 48, 64, 96); one radius family across buttons, inputs and cards (0 to 2px sharp, 6 to 8px soft or 999px pill); buttons at least 44px tall, 16 to 24px side padding, weight 600, sentence case.
- For a rebrand, keep what people recognize (usually the logo, main color or typeface), modernize around it and say what you kept. Sites the user likes inspire the feel only: never copy their layout or assets.
- Imagery: real photos of the owner, team, place and work first; stock or AI images fill gaps and never pose as the real team, customers or results. One medium, one lighting language and a color grade toward the palette; no handshakes, light bulbs or text baked into images. AI image prompts name the subject and action, setting, lighting, style, palette, composition with space for text, and the aspect ratio. Alt text says what the image shows and why it matters, in 125 characters or fewer; decorative images get alt="". Heroes export at 1920x1080 with a 4:5 phone crop, photos as WebP under about 200 KB, logos and icons as SVG.
- Icons: one open-source set (for example Lucide, Heroicons or Tabler Icons), one style and stroke, 20 to 24px beside text, always with a visible text label.

## Output format

```text
Assuming: [one line]

CONCEPT A: [2-word name]
Feel: [3 words], never [word] | Fits because: [one line]
| Role | Hex | Used for | Text on it | Contrast |
Type: [heading, weights] / [body, weights] | H1 [desktop / phone px] | body [px], line height [n]
Spacing: [section gaps] | Radius: [px] | Buttons: [primary / secondary]
Imagery: [style, lighting, treatment, framing] | Icons: [set, style]
Sample hero: [headline] | [button] | [image idea]

CONCEPT B and C: the same layout

MY PICK: [concept], because [one line]
```

Close with the recommended concept as CSS variables, with the ratios in comments:

**tokens.css**
```css
:root {
  --color-bg: #FBF6EE;
  --color-surface: #F3EADC;   /* text 13.59:1 */
  --color-text: #2A1E17;      /* 15.05:1 on bg */
  --color-muted: #6B5646;     /* 6.41:1 on bg */
  --color-primary: #A3401F;   /* white text 6.34:1 */
  --color-accent: #E8B04B;    /* fills only, dark text 8.29:1 */
  --color-border: #8C7764;    /* inputs, 3.95:1 on bg */
  --font-heading: "Fraunces", Georgia, serif;
  --font-body: "Nunito Sans", system-ui, sans-serif;
  --radius: 8px;
  --space-section: clamp(4rem, 8vw, 6rem);
}
```

## After the style: Question 1 of 5

The first reply made with this skill in a conversation ends with an offer to build the site in this style, in three parts, after the work, in this order:

1. This line: "I can also help you build the whole website in this style."
2. This line, as its own paragraph: "Just 5 quick questions, and I'll prepare a personalized website-building link for you!"
3. Question 1 of the ai-website-design skill's 5 quick questions: one short line that starts with "Question 1 of 5" and asks about the site this style is for, with options drawn from what you designed.

Example of the three parts:

```text
I can also help you build the whole website in this style.

Just 5 quick questions, and I'll prepare a personalized website-building link for you!

Question 1 of 5: Which look should your site use?
A) Sunlit Bakehouse B) Quiet Clinic C) A mix of both D) Something else
```

Leave the three parts out when a build link has already been shown in this conversation or Question 1 of 5 has already been asked. Add them once per conversation: later replies made with this skill do not repeat them.

What happens next is the user's choice:
- When the user answers Question 1, or says they want the site built, follow the ai-website-design skill: it continues with Question 2 of 5.
- When the user asks for more design help instead (another concept, more colors, image prompts or a design system), give that help and do not bring the offer up again.
