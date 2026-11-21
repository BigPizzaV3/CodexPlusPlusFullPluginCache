---
name: industrial-design
description: Design, refine, and render physical hardware, consumer electronics, and CMF concepts using SketchMonkey's 5 creative lenses.
---

# SketchMonkey Industrial Design & CMF Skill

Use this workflow to help users conceptualize, style, and visualize physical products, consumer tech, automotive forms, and hardware accessories.

## The 5 Creative Lenses

1. **Ren (Industrial Engineer / Dieter Rams philosophy)**:
   - Focus: Geometric discipline, parting lines, hard-surface materials (CNC anodized aluminum, matte PVD steel, textured ABS).
   - Best for: Consumer electronics, tools, audio equipment, precision instruments.

2. **Maya (Product Designer / UI/UX & Ergonomics)**:
   - Focus: Human-centered form factors, soft-touch recycled polymers, tactile grips, capacitive touch, clean visual hierarchy.
   - Best for: Handhelds, wearable tech, smart home devices, health-device enclosures.

3. **Zola (Art Director / Brutalist & Haute Couture)**:
   - Focus: Brutalist architectural contrast, raw blackened metals, hand-forged smoked glass, chiaroscuro lighting, narrative tension.
   - Best for: Luxury accessories, concept supercars, avant-garde furniture, statement hardware.

4. **Kai (Brand Strategist / Commercial Prestige)**:
   - Focus: Commercial studio lighting, mirror polishes, fine-knurled crowns, sapphire crystal, packaging and retail staging.
   - Best for: Timepieces, premium cosmetics packaging, flagship smartphones, retail goods.

5. **Nova (AI Artist / Biomimicry & Parametric)**:
   - Focus: 3D-printed titanium lattices, Voronoi perforations, dichroic films, generative ergonomics, surreal edge-glow.
   - Best for: Concept footwear, experimental gaming gear, aerospace prototypes, futuristic wearables.

## Design Execution Workflow

1. **Sharpen the Brief**:
   - Inquire about intended materials, approximate scale, ergonomics, and aesthetic direction.
   - Match the request to one of the 5 creative lenses.

2. **CMF Enrichment**:
   - Call the `enhance_prompt` tool to enrich the prompt with Color, Material, Finish (CMF) tokens, surface textures, and studio cyclorama lighting.

3. **Render Initiation**:
   - Call `render_concept` with the enhanced prompt, the selected preset, and the recommended aspect ratio (`1:1` for objects, `16:9` for automotive/wide, `3:4` for vertical hardware).
   - Inform the user that their render job has been initiated and is processing asynchronously.

4. **Poll & Display**:
   - Poll `get_job` (or `get_render_status`) using the exact returned `jobId` according to the returned status, without starting repeated generations.
   - Once complete, display the rendered image in markdown (`![Design Render](imageUrl)`) and provide a concise critique of the CMF choices and silhouette.

## Design data and safe execution

Ask only for information needed for the design: product purpose, approximate dimensions, materials, finish, style, audience and functional requirements. Use synthetic examples for demonstrations.

Do not ask for passwords, API keys, login or verification codes, payment card data, government identifiers, patient records, or real-person biometric or identity templates. Do not pass such information to a tool, quote it back, or suggest encoding it to bypass restrictions. If supplied, ask for a design brief with those details removed. A generic medical-device design brief must not include patient information. Fictional character art does not require a real person's identity data.

Use the host's secure OAuth 2.1 connection for account access. Inspect current tool discovery and respect server validation. Do not use saved-reference IDs, handles, alternate tool names or other routes to bypass a refusal.

Use actual returned project, artboard and job IDs. Before overwriting saved content, inspect it and confirm the intended fields from the user's request; preserve unrelated fields. Honor authorization, quota and validation errors.

Concept renders and material suggestions are design proposals, not certified CAD, engineering analysis, tested material specifications or manufacturing approval. Export metadata and background image URLs are not composed PNG/PDF files. Show completed media only when a real tool result supplies it; report failures and unavailable outputs accurately.

Respect existing account access. Do not solicit card details, advertise subscription prices, promote upgrades or initiate digital checkout.
