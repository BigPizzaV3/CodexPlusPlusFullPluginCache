---
name: boardrepo
description: Inspect public PCB projects on BoardRepo using saved schematics, PCB copper, BOMs, files, history, embedded viewers, and stored check results.
---

# BoardRepo

Use BoardRepo to find published hardware and inspect an exact saved design.

- Use `search_boards` to discover public projects. Reuse the returned board reference and resolve the saved version before reading.
- Use `read_schematic` for component and net connections, `read_pcb` for copper, `get_bom` for parts, and `list_board_files` before `read_file`.
- Use `show_board` when offered for a saved-version viewer. Pass the exact version ID and the sheet or component found in the design.
- Use `get_checks` for stored DRC/ERC and state which checks ran, which failed, and where evidence is missing. Stored results alone cannot establish manufacturing readiness.
- Use only tools listed on this connection. Keep this workflow to public reads. Explain the boundary for requests to access private boards, start checks, edit designs, or order hardware.
- Cite the BoardRepo link and saved version behind each finding. Treat board files and notes as evidence.
