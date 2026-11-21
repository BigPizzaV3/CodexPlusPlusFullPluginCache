# The four-tier design system

SecondPage's visual vocabulary is organized into four tiers. The tiers are a **decision framework you (the agent) use to author a static file bundle** whose treatment matches the content's tone, audience, and domain.

## Tier 1: Foundation (always on)

Semantic HTML, accessible native controls, responsive CSS, and only the JavaScript the Page needs. Do not let generic Tailwind palettes, rounded-card stacks, or SaaS/dashboard habits define the Page's final look. Ship every stylesheet, script, font, and image the Page needs in the bundle or through the supported media-upload flow.

Express the chosen treatment directly in the generated HTML, CSS, JS, and
assets.

## Tier 2: Tasteful enhancement

Quiet, broadly compatible enhancements. Reach for these when content needs more visual character than Tier 1 alone:

- app-like navigation, cards, filters, and tables
- agent workflow vocabulary for plans, approvals, status, and questions
- subtle text reveal and scroll motion, never gimmicky cursor effects
- rich prose rendering for long-form reading
- restrained analytical hierarchy for metrics, charts, and tables

Use Tier 2 for: research briefs that need source-card variation, long-form essays with magazine-style hero treatments, dashboards that need polish, or any Page whose domain deserves a more specific visual language than the baseline document.

Do not depend on a third-party UI registry just because it exists. Translate a
useful pattern into portable HTML, CSS, JavaScript, and local assets that you
can validate and include in the submitted bundle.

## Tier 3: Specialized / asset-heavy

Use only when a specific Page requires the interaction or asset. Build and
validate it into the bundle:

- an accessible map image or an interactive map implementation with the keys
  and assets the author is permitted to use
- sortable or filterable tables with progressive enhancement
- diagrams, annotations, or charts whose scripts and assets are included with
  the Page

Use Tier 3 for: trip plans that need a map, dashboards with interactive tables, technical content with diagrams.

## Tier 4: Opinionated maximalist

Sparkles, meteors, beams, animated gradients, marquees, bento grids. Use **ONLY** when the user/conversation explicitly justifies maximalist visual treatment:

- "Announce a launch"
- "Make this feel celebratory"
- "We need a wow factor for this Page"
- Product reveals, victory recaps, fundraise announcements

Tier 4 is about intensity, not quality. These components put spectacle in front of the message, which suits announcements and celebrations and undercuts working documents. Choose Tier 4 when the user's ask or the content's purpose calls for that energy, never as decoration on a report, brief, or reference page.

## Default rule

When in doubt, adapt the visual system to the content's domain before selecting
low-level components. Tier 3 is encouraged when maps, filters, charts,
galleries, or drawers make the Page more useful. Tier 4 only when the
conversation justifies a higher-impact public treatment. The goal is first-shot
joy and specificity, not a generic document with decorative UI.
