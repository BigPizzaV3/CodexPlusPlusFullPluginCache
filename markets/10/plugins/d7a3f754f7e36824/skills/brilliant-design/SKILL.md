---
name: brilliant-design
description: Design and edit user interfaces, web pages and graphics as editable layers on a live Brilliant canvas in the chat. Use when the user asks for a UI design, mockup, wireframe, website or landing page, app screen, dashboard, slide, social post or poster, wants a design they can edit by hand, or names Brilliant.
---

# Designing on a Brilliant canvas

1. Before the first design in a conversation, call get_knowledge with blueprint/core, blueprint/layout,
   blueprint/paint, blueprint/text and design/foundations.
2. Call design once with a title and a one-line intent. It opens an empty live canvas in the chat.
3. Build with edit_design in batches of about 20 rows. The first batch sets the frame and the main
   sections; later batches fill in the details. Use literal values (hex colors, numbers).
4. To change something, send a row that leads with the id of the layer it changes. Get ids from
   inspect_design.
5. Before telling the user the design is finished, call inspect_design with wait and report what it
   says, including any rows that did not apply.
6. To use a picture the user attached or one generated in the conversation, call place_image.
7. The user can edit every layer by hand on the canvas, and Open in Brilliant continues the design in
   the full editor.
8. For a photo cutout, call remove_background. Do not use it to generate a new image.
