---
name: "Compare ski resorts"
description: "Compare 2-5 ski resorts side by side and give a verdict for what the user optimizes for."
---

When the user wants to compare two or more specific resorts, call
`compare_resorts` with the resort names (and their city as `home` if known, to include
drive times). Present a compact comparison across piste km by difficulty, elevation
range and vertical drop, lifts, glacier status, season/open status, current snow depth,
7-day snow forecast, and ski passes. Give a verdict depending on what the user
optimizes for (size, snow reliability, proximity).
