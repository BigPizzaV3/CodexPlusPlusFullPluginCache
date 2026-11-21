# Product, references and exact text in image prompts

This is general craft for reference and edit inputs. It was checked on 2026-09-07 against the
primary sources for GPT Image 2 and Seedream 5 Pro (listed at the end). Parameters, the number
of inputs and editing are set by the current contract of the chosen model, not by this file; the
chosen model's current prompting guidance owns model-specific syntax; its live contract owns available fields.

## Reference control

Give each input a specific role: source frame, product, face, material, composition or style.
Use the real aliases the host provides. If one reference sets the product and another sets the
light and palette, do not carry over a person, packaging, lettering or props from the second.
Do not describe an invisible texture as an established fact.

For an exact product, name a short list of the important invariants: silhouette, proportions,
cap or seams, the visible surface, color and markings. For placement in a new scene, set scale,
perspective, contact shadow and reflections separately. A new background gives no right to rework
the product's design or invent its properties.

A generated reference sheet does not prove what the hidden side of the product looks like. If
there is only a front photo, the back view, the seams and the markings on the other side are
unknown. An exact commercial result needs real additional photos; invented angles can be used
only as an agreed concept.

## Text and local edits

Pass the user's lettering verbatim in quotes; give it one place, a hierarchy, contrast and a free
area. Keep the letter case and diacritics. Do not add a slogan, a discount, a quality mark or new
product properties unless asked.

Even models with strong editing and text rendering keep caveats in their official guides (the
GPT Image 2 and Seedream 5 Pro guides included) about exact layout, small characters and the
consistency of edits. Do not present a good prompt as a guarantee of a correct logo or lettering.
A mask or markup helps define the target, but it does not guarantee the accuracy of every pixel
either. Do not put API quality parameters into the creative text.

For a single edit, use the supported editing rather than a hidden full redesign. When checking
the result, look separately at whether the edit was made; whether the shape, material and
markings survived; whether the reference roles got mixed up; whether the lettering is verbatim;
and whether there is extra text or an unrequested change. If the result's pixels are not
available, say that the visual check has not been done yet.

## Example with two different roles

Setup of the example: the first reference is a product photo, the second is only a lighting
sample.

```text
@Image1 supplies the product's identity. @Image2 supplies only the soft side-light
and restrained color palette; do not copy its objects, text or background.
Place the product on a simple neutral surface, preserving its visible silhouette,
proportions, color, material and label from @Image1. Match perspective, reflections
and contact shadow to the new light. Leave a clear area above the product and
render exactly once: "ЛЁГКО БРАТЬ С СОБОЙ". Use a legible dark sans-serif with
strong contrast. No extra words, badges, logos or invented product features.
```

Replace the input labels in the example only with confirmed aliases. The example is synthetic,
not evidence of a completed generation.

## Sources

- OpenAI image guide: https://developers.openai.com/api/docs/guides/image-generation
- OpenAI prompting guide: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
- ByteDance Seedream 5 Pro: https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro

Reference aliases apply only when the chosen model declares inline-reference support.
Bind them to actual reference order and roles; for dedicated source/start/end fields,
use the slot role instead of inventing an alias.
