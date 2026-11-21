---
name: get-started
description: Use when someone first connects Aya Studio or asks what it can do. Checks the account, then helps them make a first cartoon character, picture, clip, song or voice-over.
---

# Get started with Aya Studio

Aya Studio makes cartoons: pictures, short animated clips, talking characters, songs and voice-overs. Everything is a cartoon, never photorealistic. It works with the person's existing Aya Studio account.

1. Call `get_account` to confirm the connection and see which workspace is in use.
2. Ask what they want to make, in one short question, with a few ideas: a character for their show, a picture, a 5-second animated clip, a talking character, a kids' song or a voice-over.
3. Make one version unless they ask for more.
   - Picture: `create_picture` with a clear description and a style. Show the picture inline.
   - Recurring character: after they like a picture, offer `save_character` so future pictures and clips keep the same look; pass the saved id in `character_ids`.
   - Clip: `animate_picture` from the picture id, or from a description.
   - Talking character: `make_character_talk` with the picture id, a short script and a voice.
   - Song: `make_song` with an idea or their own lyrics.
   - Voice-over: `make_voiceover` with the exact text.
4. Clips, talking characters and songs take a few minutes. Call `get_creation` with the creation id until it is ready, then share the link.
5. For full episodes with a timeline, mention the studio at https://ayastudio.si/app/.

Keep content suitable for the audience they describe. If a request isn't something Aya Studio makes (photorealistic images of real people, deleting files, payments), say so plainly and offer what it can make instead.
