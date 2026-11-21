# EW Manim Draw 0.5.0

Provide a source and say: **Draw this as a guided animated architecture diagram.**

提供文件／流程／原圖，說：**把這份文件畫成動態架構圖。**

Default: 16:9, restrained dark presentation style, full architecture visible from frame one, multi-row nested groups, fixed geometry, current-step emphasis, moving light points, synchronized captions and progress dots. The agent reads the source and selects architecture, branch-flow or relation-tour examples; source parsing is not OCR performed by the renderer.

Exports: GIF, PNG, SVG, offline HTML and editable JSON plus layout/capability report. GIF is 1920×1080, default 8 fps and looping. PNG is a fully lit overview. Fonts and Python/Pillow are supplied by the execution host, not by this ZIP. No MP4/native editable PPTX is implemented. HTML browser playback was not verified in the build environment.

Use `skills/ew-manim-draw/SKILL.md` as the runtime instruction. See `INSTALLATION_GUIDE.md` for import/update instructions. Schema 0.5 is new; schema 0.4 and legacy 0.2 scripts remain available.
