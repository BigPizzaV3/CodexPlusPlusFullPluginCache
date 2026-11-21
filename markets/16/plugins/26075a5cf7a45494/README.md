# Sprite Fusion

Generate sprites, edit existing artwork, match visual references, create eight directional views, and animate pixel art with the Sprite Fusion Pixel Art Generator API. The plugin also retrieves saved assets, downloads results, and checks account credits.

## Requirements

Use your own [Sprite Fusion API key](https://www.spritefusion.com/account/api-keys). The bundled Python client reads `SPRITE_FUSION_API_KEY` or accepts a key through standard input. Generation uses your Sprite Fusion account credits. The client requires Python 3.9 or later and uses the Python standard library.

## Included documentation

This package includes the [Sprite Fusion Agent Guide](https://www.spritefusion.com/docs/pixel-art-generator/api/agent-guide) and supporting [public API documentation](https://www.spritefusion.com/docs/pixel-art-generator/api).

Paths inside this package:

- `skills/pixel-art/SKILL.md`: the skill and Agent Guide.
- `skills/pixel-art/references/`: API documentation and animation guidance.
- `skills/pixel-art/references/client.md`: command syntax and local output information for the bundled client.
- `skills/pixel-art/scripts/sprite_fusion.py`: the Python API client.

The Agent Guide and supporting documentation retain their original wording, with documentation and image links made absolute.

[Sprite Fusion](https://www.spritefusion.com) · [API documentation](https://www.spritefusion.com/docs/pixel-art-generator/api) · [API keys](https://www.spritefusion.com/account/api-keys)
