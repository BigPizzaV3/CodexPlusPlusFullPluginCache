---
name: create-frame-simulation
description: "Create educational 2D and interactive 3D circular-frame simulations from teaching radiographs or generic anatomy. Explore Ilizarov rings, wires, half-pins, Rancho-style fixation, connecting rods, trauma struts and hexapod constructs for orthopaedic education and frame-design training. Not for patient-specific planning or clinical decision-making."
---

# Create Frame Simulation

Create one internally consistent circular-frame learning simulation. Use generic anatomy by default or de-identified teaching/example radiographs when the user supplies them. The described construct controls every hardware element.

Always include: “For orthopaedic education and frame-design training. Not for patient-specific planning or clinical decision-making.”

## Inputs

- Accept generic anatomy without requiring an image.
- Accept only de-identified teaching/example AP and lateral radiographs. If identifiers are visible, pause and ask for de-identified copies.
- Before image generation, explain that deliberately attached radiographs are processed by OpenAI under the user’s ChatGPT settings and applicable terms. Do not send them to another service.
- Accept typed or dictated constructs containing full rings, true open 2/3 rings, foot plates, fine wires, half-pins, Rancho posts, longitudinal Ilizarov rods, trauma/telescopic struts and hexapod struts.
- Accept optional learning objectives and teaching notes. Do not create diagnosis, care recommendations or instructions for real-world care.

## Workflow

1. Read [construct-schema.md](references/construct-schema.md). Convert the request into one structured construct ordered proximal to distal.
2. Show a concise confirmation table. Keep the four connector classes distinct: Ilizarov rods, trauma/telescopic struts, six-strut hexapod platforms and Rancho posts.
3. Preserve unspecified details as `CHECK` questions. Do not silently infer fixation, ring diameter, wire trajectory, connector class or opening orientation.
4. When a 2D illustration is requested, use generic anatomy or the supplied teaching radiographs plus [illustration-reference.png](assets/illustration-reference.png). Include only requested hardware. Keep every 2/3 ring as an approximately 240° arc with a genuinely empty open sector and realistic holes.
5. Make wires visibly cross the generic bone. Show half-pins engaging it. Keep wires and half-pins independently removable on the same support. When Rancho fixation is requested, mount the half-pin from a short ring post.
6. Use straight, longitudinal, matching-hole connections for Ilizarov rods. Use three or four rods as requested. If the ring openings make this impossible, flag it and do not substitute diagonal members. Trauma struts may be oblique; a hexapod interval uses six deliberately oblique struts.
7. Read [simulation-output.md](references/simulation-output.md) for a printable worksheet. Visually inspect every rendered page before returning it.
8. For the interactive model, open `https://trauma-frame-planner.nicholasnoye.chatgpt.site` and call `apply_frame_construct`. Then call `get_frame_construct` to verify every support, rotation, fixation count, mounting style and connector interval. If site tools are unavailable, use the fallback link in the schema reference.

## Educational boundary

- Teach circular fixation principles, frame construction, fixation geometry and 2D/3D construct visualisation.
- Treat the anatomy, fracture pattern and hardware trajectories as schematic learning representations.
- Do not recommend or optimise a construct for an individual or convert the simulation into real-world instructions.
- Repeat the educational disclaimer in the worksheet and when returning a simulation.
