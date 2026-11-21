---
name: create-promptkosh-image
description: Use the PromptKosh plugin to choose a style and generate or edit an image in ChatGPT when a user requests a PromptKosh image or supplies a PromptKosh style ID or link.
---

# Create an image with PromptKosh

Use PromptKosh's MCP tools to retrieve a public style prompt, then use ChatGPT's own image tool to generate or edit the image. Image generation runs on the plugin user's ChatGPT account and is subject to that account's limits. Never call a paid external image API, spend PromptKosh credits, or ask the publisher for an API key.

## Select the style

1. If the user supplies a PromptKosh style UUID or a `promptkosh.in/prompt/...-<uuid>` URL, call `get_promptkosh_style` with that UUID. Do not search for a different style.
2. Otherwise call `search_promptkosh_styles` with the user's visual goal. Select the strongest match based on title, description, and example image. If the choices differ meaningfully and the user has not specified a preference, offer up to three style names and links for the user to choose.
3. If a requested style is missing or the tools are unavailable, say so. Do not invent PromptKosh prompts or claim an image used a PromptKosh style when it did not.

## Generate

1. Call `get_promptkosh_style` for the selected style. Read its `required_inputs` and `image_instructions`, then adapt the main prompt to details the user supplied. Keep the style's defining composition and respect its negative prompt, variations, and style details.
2. If `required_inputs.reference_image` is true and no user photo is attached, ask the user to upload one and wait. Do not generate until it is supplied. If `required_inputs.prompt_variables` contains fields, ask for missing values and replace the listed placeholders before generating.
3. Invoke ChatGPT's built-in image generation or editing tool with the adapted prompt. If the user supplied a reference photo for editing or likeness, pass that photo as an image input through ChatGPT; do not upload it to PromptKosh.
4. Return the generated image with the style name and PromptKosh page link. Do not print the full style prompt in the normal image response unless the user asks to see it. The prompt is sent to ChatGPT and is not a secret from ChatGPT or guaranteed hidden from chat/tool history.
5. If ChatGPT image generation is unavailable or the user's limit is reached, explain that the image could not be generated in this conversation. Never switch to a separately billed API.

Public PromptKosh prompt pages currently show their full text. This plugin does not grant private prompt access or guarantee secrecy.
