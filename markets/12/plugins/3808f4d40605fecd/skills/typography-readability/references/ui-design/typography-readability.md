# Typography and Readability

## Mandatory Use

Use this skill whenever visible website or interface text is created, changed, reviewed, or audited. Default to the [canonical type system](../canonical/type-scale.md); use headline exceptions only after their required confirmation.

## Required Related Resources

- Use [Type Scale](../canonical/type-scale.md) for every canonical text role and its complete type tuple.
- Use [Components](../canonical/components.md) and [Component Tokens](../canonical/component-tokens.md) when a canonical component owns the text.

## Purpose

Make visible text readable, scannable, and reliable in real use.

Typography and Readability owns standalone [canonical role selection](../canonical/type-scale.md), complete tuples, rendered suitability, measure, line formation, casing, emphasis, numerals, exact characters, supported font features, wrapping, truncation, language, fallbacks, and the confirmed headline exceptions. It receives meaning and wording from [User Experience](../user-experience.md), priority from [Visual Hierarchy](visual-hierarchy.md), structure from [Grid and Layout](grid-layout.md), grouping from [Gestalt](gestalt.md), outer spacing from [Rhythm and Space](rhythm-space.md), text alignment from [Alignment](alignment.md), and text color from [Color Discipline](color-discipline.md).

It does not rewrite content, set hierarchy or layout, style [component internals](../canonical/components.md), choose color, transform responsively, implement fonts, or verify accessibility. [Responsive Adaptation](../responsive-adaptation.md) owns transformations, the coding agent owns implementation and font loading, and [Accessibility Audit](../accessibility-audit.md) verification. A website style may add character only through supported typography options.

## Canonical Component Boundary

[Canonical components](../canonical/components.md) own internal text roles, bindings, states, casing, wrapping, truncation, and behavior. Use only supported variants, properties, content options, and [component-token bindings](../canonical/component-tokens.md).

- Never restyle component text, replace its family, shrink it to fit, or add a local overflow rule.
- Apply this skill to outer context and standalone text. Report missing or unsuitable roles to [Type Scale](../canonical/type-scale.md); report missing variants, bindings, language coverage, or wrapping to [Components](../canonical/components.md) or [Component Tokens](../canonical/component-tokens.md).

## Core Rules

1. **Use [canonical roles](../canonical/type-scale.md) as complete tuples.** Select each standalone role by its reading job and never mix tuple values.
2. **Choose type by suitability, not stereotype.** Classification must fit the content, rendered conditions, and required scripts.
3. **Judge the rendered result.** Legibility depends on the actual face, size, weight, words, language, and container.
4. **Keep measure responsive and line formation readable.** Use a bounded fluid measure justified by content; a single-word final line is forbidden.
5. **Use differentiation purposefully.** Case, weight, style, decoration, and numeral treatment must serve a clear reading or task need.
6. **Keep essential text complete.** Consequential and interactive text stays visible; supporting truncation must be recoverable.
7. **Prove language and font variation.** Required scripts, directions, real styles, supported features, platform fonts, and fallbacks must preserve meaning and legibility.
8. **Isolate optional headline families.** A user-confirmed alternate family stays in standalone page and section headlines.
9. **Isolate display exceptions.** Only confirmed [Bold Typography](../website-styles/bold-typography.md) may use [Oversized Display Type](#oversized-display-type) and [Headline spacing](#headline-spacing).

### Oversized Display Type

Use only when confirmed [Bold Typography](../website-styles/bold-typography.md) authorizes a focal headline beyond [Type Scale](../canonical/type-scale.md). It may change size, line height, and letter spacing—not family, ordinary headings, body, or interface text.

Compose one readable unit with short real copy, complete words, clear order, and usually one to three lines; use up to five only when confirmed and still obvious. Tighten only enough for cohesion without obscuring counters, punctuation, accents, or adjacent lines. Never force fit with crushed spacing or inserted breaks; recompose and recheck the rendered size after [Responsive Adaptation](../responsive-adaptation.md).

### Headline spacing

Use the complete [canonical tuple](../canonical/type-scale.md) unless Oversized Display Type is active. Within that exception, choose a starting range by rendered size—not H1–H6—then inspect the face, words, weight, and lines. Larger type usually needs tighter leading; smaller or wrapping headings need more.

| Headline size | Starting line height | Typical use |
|---|---:|---|
| `18–24px` | `1.35–1.5` | H5, H6, and compact section headings |
| `25–32px` | `1.3–1.4` | Small page and section headings |
| `33–48px` | `1.2–1.3` | Standard page and feature headings |
| `49–72px` | `1.1–1.2` | Large hero and campaign headings |
| Above `72px` | `1.0–1.15` | Short display headlines with few lines |

A `19px` H6 should usually use `26–29px`, not `21px`. Favor the upper end for wrapping, narrow columns, heavy or decorative faces, tall x-heights, or stacked marks; use the lower end only for short, clearly separated display lines.

Start with the typeface's natural spacing and judge whole words. Mixed-case spacing may tighten slightly as size grows.

| Headline size | Mixed-case starting range | Guidance |
|---|---:|---|
| `18–24px` | `0–0.01em` | Keep the natural spacing or open it slightly; do not tighten small headings |
| `25–39px` | `0` to `-0.01em` | Tighten only when the face looks visibly loose |
| `40–63px` | `0` to `-0.015em` | A small reduction can improve cohesion in open letterforms |
| `64px` and above | `0` to `-0.02em` | Reserve the tightest setting for large, short display headlines |

A `19px` H6 should stay at `0` or open slightly; `-0.02em` removes about `0.38px` per pair and often looks cramped.

Case and typeface character matter:

- Use uppercase only for brief headlines and usually open it to `0.03–0.08em`; spacing cannot rescue long uppercase text.
- Keep lowercase and mixed case near natural spacing.
- Never tighten condensed, distressed, script, blackletter, or dense faces; open heavy, narrow-counter, or decorative faces when crowded.
- Do not apply Latin ranges to connected or complex scripts; preserve their shaping and rhythm.

Recheck every rendered size: a `72px` headline reduced to `28px` must use `28px` guidance. Aim for one to three natural lines, never a single-word final line. Avoid manual breaks and collisions among accents, descenders, letters, or lines. Let text wrap or choose a better-fitting face; never crush spacing to fit.

### Category priors for exploration

Use only to explore a user-confirmed optional headline family. A category suggests directions; it never selects or authorizes a face.

Each linked Google Font is one researched starting point, not a default. Test the real headline and reject it when brand, content, script, weight, fallback, or rendering calls for another direction.

| Context | Headline directions to explore | Google Fonts starting point |
|---|---|---|
| Productivity SaaS, B2B, enterprise | Character grotesk; restrained editorial serif; relevant technical display | [Manrope](https://fonts.google.com/specimen/Manrope) |
| Developer, infrastructure, security | Industrial, terminal-derived, technical, or condensed editorial display | [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) |
| AI, data, science | Precise grotesk; scholarly serif; subject-grounded variable display | [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) |
| Fintech, payments, banking | Open grotesk; narrative serif; confident challenger display | [DM Sans](https://fonts.google.com/specimen/DM+Sans) |
| Wealth, insurance, professional | Restrained serif; humanist warmth; editorial authority | [Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4) |
| Healthcare, clinical, wellness | Warm humanist; patient-story serif; calm or athletic display | [Lato](https://fonts.google.com/specimen/Lato) |
| K–12, family, children | Friendly serif; rounded, hand-drawn, or modular display | [Nunito](https://fonts.google.com/specimen/Nunito) |
| University, research, education | Institutional, archival, scholarly, or school-specific display | [Crimson Pro](https://fonts.google.com/specimen/Crimson+Pro) |
| Government, civic, legal | Local civic, statute-inspired, multilingual, or public-service display | [Public Sans](https://fonts.google.com/specimen/Public+Sans) |
| Nonprofit, activism, impact | Documentary, community-authored, protest, or condensed display | [League Gothic](https://fonts.google.com/specimen/League+Gothic) |
| News, editorial, publishing | Headline serif or grotesk; condensed news; distinct section voice | [Newsreader](https://fonts.google.com/specimen/Newsreader) |
| Arts, culture, museums, portfolios | Archival, variable, kinetic, collaged, or expressive display | [Gloock](https://fonts.google.com/specimen/Gloock) |
| Architecture, interiors, real estate | Structural, wide, condensed, material-inspired, or place-derived display | [Urbanist](https://fonts.google.com/specimen/Urbanist) |
| Luxury, fashion, jewelry, fragrance | High-contrast serif; severe grotesk; custom, wide, or condensed display | [Bodoni Moda](https://fonts.google.com/specimen/Bodoni+Moda) |
| Beauty, skincare | Sensuous serif; lab-inspired mono; soft humanist; eccentric display | [Fraunces](https://fonts.google.com/specimen/Fraunces) |
| Ecommerce, marketplace, retail | Category-specific display; editorial merchandising voice | [Outfit](https://fonts.google.com/specimen/Outfit) |
| Food, beverage, restaurants | Signage, packaging, regional, playful, or historical display | [Bricolage Grotesque](https://fonts.google.com/specimen/Bricolage+Grotesque) |
| Hospitality, travel | Place-derived, historical, transport-inspired, or editorial display | [Lora](https://fonts.google.com/specimen/Lora) |
| Wedding, celebration | Calligraphic names; editorial serif; personal ceremonial display | [Parisienne](https://fonts.google.com/specimen/Parisienne) |
| Events, conferences, festivals | Condensed, kinetic, variable, poster-like, or local display | [Anton](https://fonts.google.com/specimen/Anton) |
| Sports, outdoors, automotive, mobility | Condensed, extended, slab, kinetic, team-inspired, or transport-derived display | [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed) |
| Music, film, entertainment, games | Genre, subcultural, pixel, or kinetic display | [Unbounded](https://fonts.google.com/specimen/Unbounded) |
| Sustainability, agriculture, craft | Scientific, maker, archival, material, or regional display | [Alegreya](https://fonts.google.com/specimen/Alegreya) |
| Religion, spirituality, community | Relevant manuscript, calligraphic, or humanist display | [Spectral](https://fonts.google.com/specimen/Spectral) |
| Industrial, logistics, utilities | Stencil, slab, serial, technical, or humanist display | [IBM Plex Sans Condensed](https://fonts.google.com/specimen/IBM+Plex+Sans+Condensed) |

For compound contexts, assign roles instead of averaging aesthetics. Expressive display may own the headline; [canonical typography](../canonical/type-scale.md) still owns reading, navigation, forms, prices, status, and transactions. Reject stereotypes and candidates lacking required glyphs, weights, licensing, fallback compatibility, or clarity.

## How to Apply

### Typography and Readability Pass

1. Receive real content, priority, structure, and supported [component bindings](../canonical/component-tokens.md). Mark component text, then work frame → region → group → standalone content.
2. Select one complete [canonical tuple](../canonical/type-scale.md) per reading job. At rendered size, inspect x-height, counters, apertures, stroke contrast, ascenders, descenders, accents, punctuation, similar glyphs, and weights. If no role passes the content and container, report it to [Type Scale](../canonical/type-scale.md); never patch the tuple.
3. Test responsive measure, wrapping, line formation, case, emphasis, numerals, exact characters, overflow, scripts, direction, platform rendering, and fallback with real content. Reject single-word final lines and report missing coverage.
4. Apply optional-family and display guidance only after confirmation. Route transformations to [Responsive Adaptation](../responsive-adaptation.md) and verification to [Accessibility Audit](../accessibility-audit.md).

### Frame and Shell

- Use stable [canonical roles](../canonical/type-scale.md) for standalone titles and shell copy; preserve [component bindings](../canonical/component-tokens.md) for navigation, search, account, and utilities.
- Check compact text for clear counters, apertures, distinct glyphs, and usable weight. Diagnose baselines and cap or x-height relationships; route placement to [Alignment](alignment.md) instead of nudging boxes.
- Keep location, account, security, and persistent status complete. If space runs out, use supported wrapping, confirmed wording, or disclosure—never shrink critical text or patch [component internals](../canonical/components.md).
- When [Type Scale](../canonical/type-scale.md) resolves a native system font, inspect each platform. Keep essential shell text readable during font delay or failure; the coding agent owns delivery.

### Content and Task Regions

- For English long-form text, start at `45–75` characters per line and aim near `60–66`; use `20–40` for short support and `40–50` in multi-column reading. Adjust for face, script, size, and reading duration.
- Never use an arbitrary fixed `max-width` to force wrapping. Prefer a bounded fluid measure with a relative text-aware limit. Do not reuse prose measure for short headlines, task copy, or labels. At wide breakpoints, route unused space to [Grid and Layout](grid-layout.md) instead of leaving a narrow text island.
- Use the complete [canonical tuple](../canonical/type-scale.md). Let paragraphs, lists, headings, and labels grow without collisions, manual breaks, forced single lines, or fit-driven tracking. [Rhythm and Space](rhythm-space.md) owns distance; [Grid and Layout](grid-layout.md) region width.
- Never leave one word on a final line in a multi-line heading, paragraph, list item, caption, card title, or support block. Use supported wrapping, or route measure to [Grid and Layout](grid-layout.md), copy to [User Experience](../user-experience.md), and viewport changes to [Responsive Adaptation](../responsive-adaptation.md). Never use manual breaks, repeated or nonbreaking spaces, tracking, or smaller type.
- Match wrapping to the job when supported: `text-wrap: balance` for short headings, `pretty` for descriptions, `overflow-wrap` for unbroken values, and `nowrap` only for indivisible short labels. The coding agent owns implementation; inspect the result because a declaration does not prove acceptable wrapping.
- Use language-aware hyphenation only when permitted and useful in constrained prose. Never hyphenate headings, names, controls, code, URLs, emails, identifiers, or user input, or reuse another language's rules.
- On a supported single-question form page, the label or legend may carry the page-heading role. With several questions, keep page heading, labels, and legends distinct; never rebuild [component anatomy](../canonical/components.md).
- Use a canonical serif or sans for reading when rendered copy passes. Reserve supported monospace for code or character comparison; use body or data roles for ordinary IDs, paths, and technical prose.
- Use sentence case for ordinary standalone copy. Reserve uppercase for brief supported uses and bold or italic for necessary emphasis.
- Keep instructions, requirements, help, errors, legal terms, totals, consequences, and next actions complete at the decision. Route alignment to [Alignment](alignment.md) and color to [Color Discipline](color-discipline.md).
- For standalone text links, inspect underline thickness, offset, and descender clearance. Preserve [canonical link components](../canonical/components.md) and route unsupported rendering to their owner; the coding agent owns implementation.
- Use [Category priors](#category-priors-for-exploration) only to explore optional page, hero, feature, campaign, or editorial headline families. Limit script, handwriting, blackletter, and display faces to short, large headlines; test real words in wide and narrow results.

### Repeated and Data Regions

- Keep peer cards, lists, feeds, results, comparisons, tables, and collections on equivalent [canonical roles](../canonical/type-scale.md). Let content change item height; never shrink text or create one-off roles.
- Use tabular figures for changing values, timers, and compared numeric columns; use proportional figures in prose. Reserve metric treatment for one focal answer—not labels, axes, keys, timestamps, units, or every total.
- Preserve exact characters in code, formulas, units, citations, footnotes, serials, and identifiers. Use semantic fractions, superscripts, and subscripts with supported features, not arbitrary small text or offsets; suppress optional ligatures when characters must remain distinct and copyable.
- Wrap titles, names, prices, IDs, and user content before truncating. Give long words, URLs, emails, and identifiers valid break opportunities; never insert a visible hyphen that could become part of the value.
- Truncate only nonessential support whose full value remains available by keyboard, pointer, and assistive technology. Never truncate focusable, editable, copy-critical, or meaning-changing content.
- Recheck baselines and first lines after wrapping. [Alignment](alignment.md) owns columns, rows, and numeric edges; this skill supplies metrics.

### Layers, States, and Contexts

- Keep purpose, consequence, status, and next action complete in dialogs, drawers, menus, popovers, banners, toasts, inline feedback, and recovery states.
- Preserve [canonical component typography](../canonical/components.md) through interaction, loading, empty, success, warning, and error states. Let live values wrap and keep essential text visible during font delay or failure.
- Use only loaded styles and features supported by the family and script; reject harmful synthesis. Prefer semantic properties such as `font-weight`, `font-optical-sizing`, and `font-variant-numeric` over raw feature tags. The coding agent owns files and declarations. Keep canonical text on its bound tuple; never use width, weight, or grade to force fit.
- Test glyphs, diacritics, shaping, word breaks, bidi text, vertical writing, numeral features, weights, and fallback metrics with real content. Require correct `lang` and `dir`, and isolate mixed-direction values with `<bdi>`. The coding agent owns markup; route verification to [Accessibility Audit](../accessibility-audit.md) and do not apply Latin spacing to other scripts.
- Check mobile inputs on iOS: text below `16px` may trigger page zoom. Report the unsupported size to [Components](../canonical/components.md) or [Type Scale](../canonical/type-scale.md); never scale or override the component locally.
- Recheck narrow containers, zoom, text enlargement, user spacing, translation, modes, input conditions, and responsive results. Text may grow, wrap, or reflow; it must not clip, collide, lose function, or become unrecoverable.

## Focused Audit

- Do standalone roles match reading jobs and use complete [canonical tuples](../canonical/type-scale.md), with [component typography](../canonical/components.md) intact?
- Do glyphs, bounded fluid measure, lines, case, emphasis, numerals, underlines, exact characters, and baselines work at every size without a single-word final line or narrow text island?
- Is consequential, dynamic, localized, input, or truncated text complete or recoverable through states, fallback, zoom, spacing overrides, and responsive results?
- Are monospace, metric, optional-family, and display treatments limited to supported uses?
- Are missing roles, features, component behavior, transformations, implementation, and accessibility verification routed to their owners?
