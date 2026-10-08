---
name: image-generator
description: Create or edit images across many visual formats by selecting the right image workflow and producing precise, production-ready briefs.
---

# Image Generator

Use this skill for any image creation, image-editing, visual-design, or image-prompt request.

## Universal workflow

1. Identify the image's purpose, audience, platform, dimensions, aspect ratio, and required output format.
2. Identify the subject, composition, style, palette, lighting, materials, mood, and visual hierarchy.
3. Preserve exact text, brand names, numbers, and layout constraints when the user supplies them.
4. Choose the most specific skill below and add only details that improve the result.
5. Include an avoid list for artifacts, unwanted objects, misspellings, watermarks, incorrect anatomy, and style drift.
6. Generate or provide a complete production-ready prompt. For edits, state what must change and what must remain unchanged.
7. Inspect the result for legibility, composition, subject accuracy, continuity, and intended-use suitability.

## Skill routing

Route requests to the focused skill that matches the deliverable. Combine skills only when the user clearly needs a combined asset.

### Thumbnail design

Optimize for instant recognition, mobile readability, strong focal point, contrast, safe text margins, and a clear emotional or informational hook. Include platform dimensions and readable title text.

### Logo and brand marks

Create a simple, distinctive, scalable mark with a clear silhouette, balanced negative space, and usable light and dark variants. Avoid unnecessary detail and never add text unless requested. Include favicon and small-size considerations when relevant.

### Favicon and icons

Use one recognizable shape, bold contrast, minimal detail, and a square composition. Test conceptual readability at 16px, 32px, and 64px. Provide transparent-background and app-icon considerations when relevant.

### Flat illustration

Use clean shapes, controlled line weight, intentional layering, limited palette, and clear visual hierarchy. Specify whether the style should be editorial, playful, geometric, hand-drawn, or infographic-like.

### 3D image

Specify modeling style, camera angle, lens feel, materials, depth of field, lighting setup, surface detail, shadows, environment, and render quality. Distinguish realistic product rendering from stylized 3D illustration.

### Drawing and sketch

Specify medium, paper or canvas texture, line character, shading, perspective, level of roughness, and whether the result should feel like a study, storyboard, concept sketch, ink drawing, watercolor, or pencil work.

### Product and marketing visual

Define the product, target audience, placement, background, brand palette, campaign mood, copy, call to action, and space for layout overlays. Never invent product claims or certifications.

### Website and social graphics

Design for the exact crop and responsive context. Protect important content from platform overlays, provide variants when aspect ratios differ, and preserve brand consistency across a set.

### Image editing

Treat the supplied image as the edit target. List invariants explicitly: preserve identity, pose, product geometry, typography, framing, or lighting unless the user asks to change them. Make one targeted change at a time and avoid accidental additions.

## Text in images

For exact text, quote it verbatim and specify hierarchy, placement, font character, contrast, and safe margins. If reliable text rendering is not possible, recommend generating a clean background and adding typography in a design tool.

## Responsible generation

- Do not claim a generated image is an authentic photograph or documentary evidence.
- Do not imitate a living artist's exact style; describe high-level visual properties instead.
- Do not add logos, watermarks, people, products, or claims that the user did not request.
- Flag ambiguous identity, copyrighted-character, trademark, or sensitive-person requests and preserve the user's legitimate creative goal with a safer alternative.
