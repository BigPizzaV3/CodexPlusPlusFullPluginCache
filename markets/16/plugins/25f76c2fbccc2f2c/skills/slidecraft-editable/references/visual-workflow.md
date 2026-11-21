# Design and image workflow

Execute this workflow with the available ChatGPT tools, then run the native builder. The scripts do not call an image model or provide a hosted image API. Never claim image generation occurred if only the PPTX renderer ran. Do not request credentials for built-in tools.

## Resolve the composition

1. Read the brief and references. Choose exactly one slide title, a complete main thesis, supporting evidence, and necessary attribution. Make the title visibly distinct from a thesis, kicker or quote. Do not leave two unrelated headings competing for the same role.
2. Extract the template palette, typefaces, canvas, typography and repeated branding when a template is supplied. Otherwise choose an appropriate direction from the current brief and audience. Carry this project style profile forward between its slides. Branding, portraits and icons are optional; do not reserve empty logo space or inherit branding from another project.
3. Use ImageGen for a full-slide concept for a new design, substantial redesign, or a request for a finish comparable to generated artwork. Reference supplied cover/background images and the actual photos when relevant. Choose the composition without a confirmation loop unless the user asks to approve it.
4. Compare the concept with the source and brief. Select or revise it. Treat it as a visual plan, not the delivered editable slide.

## Obtain separate assets

- Generate a clean decorative background without words, numbers, logos or people. Reserve negative space for editable text. Match the reference palette and composition.
- Generate needed semantic icons as a separate transparent asset. Use ordinary image objects with appropriate cropping, rather than baking icons into paragraphs.
- For actual people and events, retrieve real photos and record their source. Use ImageGen for removal of photo backgrounds or another requested image edit, preserving identity and pose. Do not generate a fake event photograph.
- Copy supplied logos from original bytes. Never ask ImageGen to recreate a coat of arms or logo. Mark their image objects `role: "logo"` so the builder checks their bytes and placement after export.
- View each asset before placing it. Keep a private asset inventory with role, local path, provenance/source URL, pixel dimensions and intended position. Do not include private assets or the inventory in the reusable plugin.

## Reconstruct and inspect

Use native text with `role: "title"` for the one slide title. Keep the main thesis as a complete sentence or coherent phrase, even when its typography spans different boxes. Use native charts, tables and diagrams when the information needs exactness and editing. Keep backgrounds, portraits and icons independent from informative text.

When replacing a slide design, set `replaceContents: true` rather than covering its old objects. Keep unrelated slides and their content. Do not add a cover for a one-slide task.

Run `build_deck.mjs` using the specification reference. Inspect both its native previews and LibreOffice previews. Fix any visual mismatch or overflow, rebuild with a new candidate/output path, and repeat the affected checks. The pipeline prepares both renderings; the agent must still inspect them. Neither renderer proves how a specific phone or PowerPoint installation will display a file. If the user reports an application-specific error, record it as an unresolved compatibility failure until observed there, provide the verified PDF preview, and avoid claiming an untested device fix.
