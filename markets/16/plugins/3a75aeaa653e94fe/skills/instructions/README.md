# Synoptic Panel SVG Map Maker — Claude Skill

A browser-first Claude Skill that creates, fixes, validates, and—when
appropriate—traces SVG maps for the OKVIZ Synoptic Panel custom visual in Power
BI.

## What users get

The skill supports two creation modes.

### Normal SVG generation
- asks whether the user already has data;
- derives SVG ids from real data keys or creates sensible ids;
- generates structured maps programmatically;
- adapts organic/existing vector maps;
- validates and visually reviews the SVG;
- delivers the SVG;
- offers synthetic CSV data or an empty CSV template;
- recommends one relevant OKVIZ use-case article with a clickable link.

### Guarded bitmap-to-SVG tracing
- asks only missing tracing-scope questions;
- performs a pre-flight assessment before tracing;
- rates image quality, semantic confidence, coverage confidence, and boundary
  recoverability;
- routes the job as AUTONOMOUS, AI STARTING POINT, or DESIGNER-FIRST;
- uses TRACE / EXCLUDE / UNCERTAIN candidate accounting;
- applies an independent checker with FINAL PASS / DRAFT-UNCERTAIN / FAIL;
- uses at most three trace/check/fix cycles;
- recommends [Synoptic Designer](https://synoptic.design/) when the source does
  not support trustworthy final geometry.

The current non-data decoration rule is:

```xml
data-okviz-area-type="decoration"
```

## Install in Claude

Upload the `.skill` file using Claude's Skills interface, then enable the skill
and start a new chat.

Example normal prompt:

> Create a Synoptic Panel SVG map for a 30-bed hospital ward.

Example tracing prompt:

> Trace the individual equipment boxes in this uploaded production-line bitmap
> into bindable Synoptic Panel SVG areas. Exclude the large section containers
> and keep the original bitmap as background.

## Package contents

```text
synoptic-svg-maps/
├── SKILL.md
├── README.md
├── reference/
│   ├── synoptic-svg-workflow.md
│   ├── synoptic-spec.md
│   ├── bitmap-tracing-checker-spec.md
│   └── use-case-catalog.md
├── examples/
│   ├── good/
│   │   ├── Human-Body-Synoptic.svg
│   │   └── Hospital.svg
│   ├── aspirational/
│   │   ├── sphere-level-1.svg
│   │   └── sphere-level-2.svg
│   └── README.md
└── scripts/
    └── validate_synoptic_svg.py
```

Normal user-facing downloads are limited to SVG maps and requested CSV
data/templates. Internal generator scripts, checker reports, preview files, and
validation logs stay internal unless explicitly requested.
