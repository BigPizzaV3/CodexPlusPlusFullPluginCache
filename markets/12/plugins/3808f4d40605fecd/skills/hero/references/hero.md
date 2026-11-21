# Hero

## Mandatory Use

Use this skill whenever a task creates, changes, reviews, or audits a homepage or landing-page hero. It is also mandatory when deciding whether that page should have no hero.

For creation or material redesign, use only the structure and optional treatments confirmed through the homepage hero question in `AGENTS.md`. Do not silently substitute another structure.

## Purpose

Choose and compose the opening region so people can quickly understand what the page is about, why it matters, and what to do next.

A hero is not mandatory. Use **No hero** when the primary content or task should begin immediately, the page has several equal priorities, or a large opening would add ceremony without clarity.

## Choose the Structure

| Structure | Choose it when |
|---|---|
| Centered / stacked | One concise message and action should command attention without competing media. |
| Split-column | The message and one meaningful image, illustration, proof point, or product view deserve equal presence. |
| Input-capture | The page's primary task can begin immediately through a confirmed search, signup, location, or other canonical input. |
| Product preview | One real product view is the clearest proof of the experience. |
| Product showcase | Several real views, features, or a short demonstration are needed to explain the product. |
| Full-bleed media | A confirmed image or video carries essential story, place, product, or brand meaning. |
| Carousel | Several peer messages must share one region and users can control the sequence. Prefer static sections when discoverability matters more than compactness. |
| Editorial / typography-led | Language is the main expressive asset and media would dilute the message. |
| Illustration / character-led | A confirmed illustration system or character makes the idea easier to understand or remember. |
| Bento / mosaic | Several related capabilities need different visual weight within one coherent overview. |
| Interactive demo | A safe, bounded interaction proves the value better than explanation alone. Use only confirmed behavior. |
| Before-and-after / comparison | The central value is a visible transformation and both states are truthful and comparable. |
| Social-proof-led | Trust is the main barrier and confirmed evidence is stronger than a product or lifestyle image. |
| Immersive 3D | A real object, space, or spatial experience is central and a useful static fallback is available. |
| No hero | The page should begin with content, navigation, results, or a task instead of a promotional opening. |

## Optional Treatments

Treatments modify the selected structure; they never replace it.

[Motion and Transition](ui-design/motion-transition.md) owns the behavior, timing, interruption, and static or reduced result of every confirmed moving treatment.

| Treatment | Guidance |
|---|---|
| Minimal | Remove nonessential media and decoration while preserving the message and action. |
| Animated | Use motion only when it explains, demonstrates, or reinforces meaning. The resting state must remain complete. |
| Typing effect | Reserve for brief, genuinely changing language. Keep the full meaning available without waiting. |
| Parallax | Use only when depth supports the story. Preserve reading, control, and an equivalent reduced-motion experience. |

## Hero Anatomy

A strong hero usually contains:

1. One page subject or promise in the headline.
2. Brief supporting text only when the headline cannot carry enough context.
3. One primary action when the page has a clear next step.
4. A secondary action only when it represents a genuinely different path.
5. Media, demonstration, or proof only when it strengthens understanding or trust.

Do not force every element into every hero. Remove badges, navigation-like links, decorative cards, duplicate claims, and competing actions until one focal path is clear.

Use real content. Never invent testimonials, customer logos, ratings, metrics, product screens, certifications, availability, or performance claims.

## Practical Guidance

- Make the page subject, value, and primary path understandable in a quick scan. Do not cram the whole page above the fold.
- Keep the headline focused on one idea and aim for one to three natural lines. Do not add manual breaks or tighten typography to force a composition.
- Keep supporting copy short enough to read before the primary action loses its connection to the headline.
- Use direct action labels that describe the destination or outcome. Avoid several equally strong calls to action.
- Let content determine hero height. Do not use a fixed or full-viewport hero merely to make it feel important.
- Keep text separate from informative imagery. Avoid baking headlines, actions, prices, or essential claims into images or video.
- Use a real product view for product-led heroes. Do not fabricate dashboards or stretch one screenshot into a generic decorative panel.
- Use the canonical Alpy Image component and its supported aspect ratios when media is needed. Choose a crop that preserves the actual subject.

## Mobile

- Left-align hero text by default for predictable scanning. Preserve another alignment only when it remains clearly intentional and readable.
- Stack the message, action, and media in the order people need them. Keep the primary action near its explanation.
- Recompose the hero instead of shrinking a desktop arrangement. Remove decorative layers before essential content.
- Avoid fixed heights, overlapping text and media, clipped imagery, and actions pushed below a large decorative opening.
- Use a mobile-appropriate crop or asset when the desktop media loses its subject. Do not rely on background positioning to rescue important content.
- Avoid carousel autorotation on mobile. If a carousel is confirmed, keep the first slide useful, provide canonical controls, support touch and keyboard use, and never make later slides the only route to important content.
- Test long headlines, translated copy, zoom, narrow screens, landscape orientation, and reduced motion.

## Media, Motion, and Performance

The hero must remain understandable without media, animation, autoplay, pointer movement, or 3D rendering.

Use video, animation, parallax, typing, carousels, and 3D only when confirmed and supported. Apply [Motion and Transition](ui-design/motion-transition.md) without delaying access to the headline or primary action.

Treat hero media as performance-sensitive. Load the smallest suitable asset and prioritize the actual opening image when it is the page's largest visible content. Do not preload several hero candidates or hide a heavy desktop asset behind a mobile crop.

## Alpy Rules

Compose the hero from canonical Alpy components and semantic tokens. Hardcoded color, spacing, typography, border, radius, shadow, sizing, or local component substitutes are forbidden.

This skill chooses the hero structure and content relationship. It does not authorize a new Hero component, new component anatomy, invented interaction, unsupported breakpoint, or raw visual value.

## Review

- Can someone identify the page subject, value, and next step without studying the full page?
- Is there one dominant message rather than several competing campaigns?
- Does every action, proof point, and visual support that message?
- Would **No hero** make the page faster and clearer?
- Does the narrow-screen version preserve the same meaning and priority?
- Are motion, media, controls, contrast, focus, alternatives, and loading behavior usable in the rendered result?
