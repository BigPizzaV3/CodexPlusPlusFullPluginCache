---
name: get-started
description: Design an electronics circuit with EasyCircuit. Use when the user wants to build, wire, or check a circuit, asks for a part's pinout or capabilities, or wants an EasyCircuit design link.
---

# Designing circuits with EasyCircuit

1. Pick parts with `search_parts`. Prefer catalog parts that match what the user asked for; ask one short question only when the request leaves a key choice open, such as which controller board.
2. Read each part's exact pinout with `get_part_pins` before wiring it. Use the real pin labels. Never invent a pin.
3. Write the design: `nets`, `components` (each with `id`, `name`, `type`, and `pins` that carry their `net`), and `connections` between `componentId.pinId` endpoints. Wire every part's power and ground, give all parts a common ground, and give motors, pumps, solenoids, and heaters an explicit battery or power supply.
4. Run `check_design`. Fix every blocking issue. For each design warning, fix it if it is real, or tell the user why it does not apply. Check again after each fix.
5. Call `save_design` with a short project name and give the user the link. It opens the design in the EasyCircuit editor, where they can view the schematic, breadboard, and perfboard layouts, edit, and order parts.

Tell the user when a pin fact is unverified reference data. Do not design mains (wall AC) wiring; suggest a low-voltage alternative or a qualified electrician instead.
