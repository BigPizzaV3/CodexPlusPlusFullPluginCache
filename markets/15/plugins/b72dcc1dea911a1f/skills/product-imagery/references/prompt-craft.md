# Prompt craft for product photos

Use this file when you write a product photo prompt. The model limits from `list_models` decide the prompt length, the reference count and the aspect ratios. If this file differs from a tool description or a server guide, follow the server.

## Prompt shape

Write the parts in this order. Fill each bracket. Remove a bracket that does not apply.

```
The [product] from reference 1, [label facing camera / cap on / lid open], [placed on / held / standing in] [surface and setting].
[Light: direction, quality, colour].
[Lens], [angle], the product fills [part] of the frame, empty space on the [side] for copy.
[Style: editorial product photography / clean e-commerce / candid lifestyle], true colour, no colour cast.
Keep the label text, logo, colours and shape exactly as in reference 1. No extra text, no extra products.
[Brand line from the brand kit, if any]
```

## Defaults

- Packshot: on a seamless white sweep, a soft key light from the left, a gentle contact shadow, a 50 mm lens at eye level, the product centred and filling most of the frame.
- Lifestyle: in a real place, natural light from one side, a shallow depth of field, an 85 mm lens, the product slightly off-centre, empty space on one side.
- Hero: a dark or coloured surface, one strong key light from behind and to one side, a low angle, the product large in the frame, empty space at the top for a headline.

## Worked example

The user writes: "bottle on table nice light".

A better prompt, for one product reference at 4:5:

```
The glass serum bottle from reference 1, label facing camera, standing on a pale oak table by a window.
Soft morning light from the left, a long gentle shadow to the right, a slight warm cast.
85 mm lens, eye level, the bottle fills about half of the frame, empty space in the top third for a headline.
Editorial product photography, true colour, fine detail on the label.
Keep the label text, logo, colours and shape exactly as in reference 1. No extra text, no extra products.
```

## Edit rules for a rewritten prompt

When `enhance_prompt` returns a rewrite, show it to the user as it is. Then check it and suggest these fixes. Quote only the version the user approves:

- Put the subject first.
- Keep the keep line. Never cut it to fit the length limit. Cut style words first.
- Remove any product detail the reference does not show.
- Remove any invented text on the image.
- Keep one light direction and one lens.

## When the product drifts

- If the label warps or the text is wrong, move the keep line to the start of the prompt. Add a close-up of the label as a second reference. Or pick a model from `list_models` that takes more references.
- If the product changes shape, use fewer scene words and more exact words.
