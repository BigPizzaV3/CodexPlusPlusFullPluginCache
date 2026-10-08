# Provenance & External Basis

This skill is an original synthesis/adaptation. It is not a verbatim copy of a single external skill.

Primary sources reviewed for the original and transversal adaptation:

- **OpenAI — Google Sheets skill**: spreadsheet workflow grounding, scannability, style routing, verification discipline, and progressive use of reference files.
  https://github.com/openai/plugins/blob/main/plugins/google-drive/skills/google-sheets/SKILL.md

- **Agent Skills specification**: required `SKILL.md` structure, frontmatter constraints, optional `scripts/`, `references/`, `assets/`, and progressive disclosure.
  https://agentskills.io/specification

- **TerminalSkills — UI/UX Pro Max** (Apache-2.0): human-centered context, progressive disclosure, recognition over recall, error prevention, consistency, accessibility, and validation patterns.
  https://github.com/TerminalSkills/skills/blob/main/skills/ui-ux-pro-max/SKILL.md

- **NIST Human-Centered Design**: user/task/context-centered design, self-descriptiveness, controllability, error tolerance, and learnability.
  https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design

- **UK Government — Creating and sharing spreadsheets**: user needs, accessibility, machine readability, headers, avoiding color-only meaning, and cautious merged/frozen structures.
  https://www.gov.uk/guidance/creating-and-sharing-spreadsheets

- **Chalhoub & Sarkar, CHI 2022 — “It’s Freedom to Put Things Where My Mind Wants”**: empirical framing of the trade-off between spreadsheet flexibility and imposed structure.
  https://doi.org/10.1145/3491102.3501833

Adaptation decision: **ADAPT**. The prior project-specific skill already contained a strong general UX method. The transversal version removes hard-coded Project/user dependencies from the core and preserves financial-specific guidance as an optional profile.
