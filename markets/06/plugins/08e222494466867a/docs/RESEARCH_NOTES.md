# Research Notes — Atelier Pottery Mentor

Current package version: **0.1.1**

Research date: 2026-09-23

## Recommended public name

Use **Atelier Pottery Mentor** rather than plain **Atelier**.

The short brand name is elegant but ambiguous: current web results include unrelated products named Atelier for agentic workspaces, design systems, presentation themes, and other creative tools.

The public name should communicate the niche immediately while preserving the Atelier brand.

Package: `atelier-pottery-mentor`
Skill: `pottery-mentor`

## Product definition

Atelier is a pottery and ceramics mentor, distinct from Imago.

Its value is:
- constructive ceramic critique;
- technique coaching;
- clay/glaze/firing troubleshooting;
- kiln/cone education;
- controlled testing;
- functional-ware caution;
- safer studio practice.

It should not become a generic image-generation or design plugin.

## Architecture

Use a **skills-only plugin** for v0.1.

No MCP server is needed because the current user value is knowledge, image/file interpretation, troubleshooting logic, critique, test design, and safety guidance.

A later MCP integration would only make sense for a specific controlled system such as:
- importing kiln logs from a supported controller;
- a studio firing database;
- a glaze-test database;
- inventory/SDS lookup;
- studio equipment telemetry.

Do not add live kiln control or destructive equipment actions merely to make the plugin more "agentic."

## OpenAI plugin rules checked

Current directory requirements include:
- display name <= 30 characters;
- short description <= 30 characters;
- long description <= 4,000 characters;
- <= 20 capabilities, each <= 120 characters;
- <= 3 starter prompts, each <= 128 characters;
- a valid `SKILL.md` with name/description frontmatter;
- verified publisher identity and policy attestations;
- skill safety/security scans.

A skills-only plugin can package instructions and references without an MCP server.

Sources:
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## Silica and studio safety

NIOSH currently identifies pottery/ceramics as an activity/industry where respirable crystalline silica exposure can occur.

NIOSH's pottery-control work specifically supports:
- reducing airborne dry dust;
- wetting some work;
- local exhaust/ventilation;
- improved housekeeping;
- eliminating dry sweeping in favor of safer dust-control methods such as appropriate HEPA vacuuming.

This is a core safety boundary for Atelier.

Sources:
- https://www.cdc.gov/niosh/silica/about/
- https://www.cdc.gov/niosh/engcontrols/ecd/detail172.html

## Kiln safety

Current Skutt kiln-safety guidance emphasizes:
- proper clearances;
- electrical/fire safety;
- ventilation;
- thermocouple condition/placement;
- using the correct equipment/stand.

Atelier should always prefer the actual kiln manufacturer's manual over generic instructions.

Source:
https://skutt.com/skutt-resources/resources-just-for-you/architectural-specifications/kiln-safety/

## Pyrometric cones

Orton describes cones as a way to monitor heatwork and kiln uniformity.

Important product rule:
**Do not describe a cone as one fixed temperature.**

Cone equivalency changes with heating rate/profile. For exact numbers, use the current Orton chart for the correct cone type/rate.

Orton also recommends witness-cone use as verification even with electronic controllers.

Sources:
- https://www.ortonceramic.com/pyrometric-cones
- https://www.ortonceramic.com/pyrometric-cones-resources
- https://www.ortonceramic.com/post/are-pyrometric-cones-necessary-in-an-electronically-controlled-kiln

## Food-contact ceramicware

FDA guidance documents lead/cadmium concerns in ceramicware and notes that firing conditions matter to whether lead in some traditional glazes is adequately incorporated.

Atelier therefore must not infer food safety from:
- glaze appearance;
- a photo;
- a cone number;
- a recipe alone;
- "lead free" wording alone.

Use manufacturer instructions and appropriate testing/regulatory guidance for actual claims.

Sources:
- https://www.fda.gov/food/environmental-contaminants-food/questions-and-answers-lead-glazed-traditional-pottery
- https://www.fda.gov/regulatory-information/search-fda-guidance-documents/guidance-industry-safety-imported-traditional-pottery-intended-use-food-and-use-term-lead-free

## Glaze troubleshooting

Current Ceramic Arts Network references confirm that common faults such as crazing/shivering, crawling, pinholing, and blistering can arise from different interactions among glaze fit, application, body, composition, and firing.

Atelier should diagnose the first useful variable/test rather than prescribe a universal "fire hotter," "fire slower," or recipe change.

Sources:
- https://ceramicartsnetwork.org/daily/article/common-glaze-faults-and-how-to-correct-them
- https://ceramicartsnetwork.org/ceramics-monthly/ceramics-monthly-article/techno-file-glaze-fit-and-fault

## Core behavior retained

1. Be a mentor, not a cheerleader.
2. Observe before inferring from images.
3. Give prioritized, actionable critique.
4. Teach cause and effect.
5. Treat defect diagnosis as hypothesis + test.
6. Treat cones as heatwork.
7. Use small controlled experiments.
8. Never certify food safety from appearance.
9. Never recommend bypassing kiln safety systems.
10. Put silica/material safety into studio advice by default when relevant.


## 0.1.1 visual-capability update

Atelier now explicitly uses native host image-generation/editing capabilities when a user asks for a ceramics-focused visual.

This includes:
- new pottery/form concepts;
- alternative handles, rims, feet, proportions, and surfaces;
- conceptual glaze/finish previews;
- direct edits to uploaded pottery photos;
- educational technique diagrams and studio graphics.

The core domain boundary remains important:
- generated glaze/firing visuals are concepts, not physical test results;
- a visual cannot establish glaze fit, food safety, absorption, chemistry, firing success, or structural integrity;
- image edits should preserve the user's actual piece except for requested changes.

No separate image-generation MCP is required because the host product already provides native image creation/editing capabilities.
