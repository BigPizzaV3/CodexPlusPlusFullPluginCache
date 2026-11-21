---
name: product-render
description: Render the product shown in a technical drawing or sketch as a photoreal studio image with TechDraw AI. Use when the user wants a product shot, a catalogue image or a visual of a design before it is made.
---

# Drawing to photoreal render

## Steps

1. Use the drawing or sketch the user shared, or a TechDraw AI drawing made earlier in the chat.
2. Ask for the material and finish if the user has not said, such as brushed steel, oak or matte black plastic.
3. Call `render_product` with the image (5 credits). Pass `material`, `background`, `angle` and `style` when the user named them.
