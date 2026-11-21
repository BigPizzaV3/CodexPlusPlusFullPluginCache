---
name: synergieloc-cao
description: Take a house from design to the building permit and the construction schedule with the Synergieloc CAO tools — layouts from a brief, construction checks, permit file, site schedule, drawing set, DXF and IFC exports, quantities and cost estimates.
---

# Synergieloc CAO

Use this skill when the user wants to design, check or document a house: a layout from a brief, a plan to check, a building-permit file, a construction schedule, a drawing set, a DXF or IFC file, quantities, a cost estimate, energy, sunlight, planning rules or a walkthrough.

## Workflow

1. **Get a scene.** Start from `cao_demo` (`exemple`: `maison`, `appartement`, `extension`, or `projet_complet` — the house on its plot with driveway, parking, footpath, gate, buried networks and landscaping) or lay out a house with `cao_programme` (bedrooms, `surface_m2`, open or closed kitchen, bathrooms, roof). To edit a scene, change its walls, openings or rooms yourself (millimetres), then check it again with `cao_verifier`.
2. **Check it.** Call `cao_verifier` before producing anything. Fix every critical alert (`appliquer: true` returns the corrected scene) and tell the user what was fixed.
3. **Produce what was asked**, always from the checked scene:
   - building permit: `cao_permis` (French Cerfa 13406 for a detached house);
   - construction schedule: `cao_4d` with a start date `debut` (YYYY-MM-DD); `images: true` only if the user wants the views;
   - drawings and models: `cao_carnet` (drawing set), `cao_generer_dxf`, `cao_generer_ifc`, `cao_pdf`, `cao_rendu`;
   - figures: `cao_metres`, `cao_devis`, `cao_nomenclatures`, `cao_energie`, `cao_soleil`, `cao_urbanisme`;
   - furnishing and garden: `cao_mobilier` lists the catalogue (trees, hedges, fences, gates, terrace…);
   - walkthrough: `cao_visite_studio`.

## Conventions

- All coordinates and dimensions are in millimetres; north is +y, east is +x.
- Large files come back as a download link valid for 30 minutes: give the link and say it expires.

## Honesty

- Checks, schedules, estimates and the permit file are indicative technical aids and drafts. Never present them as an official certification, a permit approval or a replacement for an architect, an engineer or a building inspector.
- Local zoning (PLU) is not checked. Permit pieces that need real-world data (location map, landscape insertion, photos, RE 2020 certificate) are to be supplied by the user: never invent them.
- Outdoor works (driveway, networks, landscaping) are drawn and checked but not yet scheduled or priced: say so when the user asks for them.
- Building rules are mainly French: say so when the project is elsewhere.
- Report the figures the tools return; do not invent dimensions, areas, dates or prices.
