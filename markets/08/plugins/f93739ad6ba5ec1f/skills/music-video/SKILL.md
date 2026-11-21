---
name: music-video
description: Make a music video with Crealix for a library track, an AI song made for it or the user's own song, with visuals that follow the lyrics and the beat, lyric captions and a waveform. Use when the user wants a music video, a lyric video, a visualizer, or visuals for their song or beat.
---

# Music video

The song drives the video. Crealix transcribes the lyrics with their timing and
plans the scenes on the beat; you add the visual story they follow. Lyrics can
show as captions, and an animated waveform can pulse with the audio.

## 1. Get the song

A music video needs exactly one song:
- a track from Crealix's library: `musicId` from `browse_catalog('music')`;
- an AI song made for it: `generate_music` (a prompt, style tags, and lyrics if
  the user has them). It costs credits and takes about a minute; wait for it
  with `get_status`, then use its `trackId` as `musicId`;
- the user's own file: bring it into Crealix (`import_media_from_url` for an
  attachment or a link, `upload_media` for a file on their device) and pass its
  URL as `options.songUrl`.

A long song can be trimmed with `options.musicTrimStartSec` and
`musicTrimEndSec`. The video lasts as long as the song.

## 2. Read the guide

Call `get_creation_guide('music_video', durationSec, language)`: the format of the
visual story, the options (modes, tiers, scene lengths, waveform) and the cast
(visual styles, captions).

## 3. Write the visual story (hybrid)

Send it as `script`, up to the guide's limit. Describe what we SEE across the
song:
- the main characters and their look, the same all video long;
- the world: places, era, palette;
- the arc: how it opens, builds and peaks with the song's climax.

Don't write lyrics or timings: Crealix hears the song and places the beats.
Without a story (crealix mode), Crealix plans the visuals from the lyrics alone.
That works well when the user has no idea yet.

## 4. Cast it

Choose what suits this song, its mood and its audience:
- The visual style (`visualStyleId`) from the cast.
- `options.generationMode`: IMAGES_FIRST (moving stills, the cheapest) or
  FULL_VIDEO (animated clips, much more). Say the price difference and let the
  user choose if they didn't.
- `options.tier` for image quality. Scene rhythm: `autoSceneDuration`, or a
  fixed `maxSceneDurationSec` for faster or slower cuts.
- Lyric captions (a caption style, or off), and the waveform
  (`options.enableWaveform`, its style, colours and position) when it suits a
  visualizer.
- The user's saved characters (`characterIds`) when they want themselves or a
  mascot in it.
- 16:9 for YouTube, 9:16 for short-form. `cover` for the thumbnail.

## 5. Propose, create, finish

`check_plan` until it is valid, one `validate_plan` with two or three lines of why,
then `create_video` with the `proposalId` on a yes in the chat. Follow it with
`get_status`.

Afterwards, `edit_video` changes the title, lyric captions and the mix. Scenes
are reworked in the Crealix editor: share its link. Render only when they ask.
