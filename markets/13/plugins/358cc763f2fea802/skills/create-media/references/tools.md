# Tool guide

This guide maps requests to the tools exposed by the getimg MCP server. Use each connected tool's current schema for its inputs.

| Request                                                       | Tool                                                                  |
| ------------------------------------------------------------- | --------------------------------------------------------------------- |
| Generate an image from text, with optional reference images   | `generate_image`                                                      |
| Generate video from text, frames, or reference media          | `generate_video`                                                      |
| Generate a music track                                        | `generate_music`                                                      |
| Convert text into speech                                      | `list_models` with `operation: create-speech`, then `generate_speech` |
| Generate a sound effect                                       | `generate_sound_effect`                                               |
| Turn a selfie into professional profile photos                | `headshots`                                                           |
| Create an original character portrait                         | `character_creator`                                                   |
| Repair a damaged or faded photo, optionally with colorization | `photo_restoration`                                                   |
| Make transparent stickers from a subject photo                | `sticker_maker`                                                       |
| Remove unwanted people or objects from a photo's background   | `background_cleanup`                                                  |
| Change a photo's lighting                                     | `relight`                                                             |
| Animate a photo with a dolly zoom                             | `dolly_zoom`                                                          |
| Transition between two images in a video                      | `image_transition`                                                    |
| Create a product orbit video from product photos              | `product_orbit`                                                       |
| Create a presenter-led UGC product ad                         | `ugc_video`                                                           |
| Create a transparent cutout                                   | `remove_background`                                                   |
| Change an image's aspect ratio or extend its canvas           | `resize_image`                                                        |
| Increase an image's resolution                                | `upscale_image`                                                       |
| Upscale a video to 1080p or 4K                                | `upscale_video`                                                       |
| Browse or reuse the connected team's media                    | `list_media`                                                          |
| Upload media from the user's device                           | `upload_media`                                                        |
| Discover models, capabilities, credit costs, or speech voices | `list_models`                                                         |
| Check the connected team, subscription, and balance           | `get_account`                                                         |
| Finish a pending generation without submitting another one    | `get_generation_status`                                               |

Generation and transformation tools spend getimg credits. Account, model, library, and status lookups are read-only.
