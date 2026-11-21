# OpenAI Model Prompting

Sources:

- https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide

## GPT Image (`gpt-image-*`)

- Use a stable brief order: background or scene, subject, key details and constraints.
- Include the intended use when it changes layout, such as poster, product image, UI mock or
  edit.
- For complex requests, prefer short labeled sections or line breaks to one dense paragraph.
- Specify materials, shapes, textures, framing, viewpoint and lighting when they matter.
- For edits, name the requested change and the important preserved elements.
- Put literal rendered text in quotes and describe hierarchy, placement and typography.
- Identify each image input by its role in a multi-reference request.

Use schema fields for quality, size, masks, references and other typed controls.
