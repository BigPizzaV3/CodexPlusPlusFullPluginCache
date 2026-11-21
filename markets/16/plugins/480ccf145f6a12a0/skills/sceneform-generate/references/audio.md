# Audio, lip sync, and avatars

## Speech

`script` is the exact text spoken, up to 2,048 characters.

- **Pacing.** Natural narration runs about 2.5 words a second: about 25
  words for 10 seconds, 75 for 30. To change the length, change the words;
  a sped-up read sounds rushed.
- **Write for the ear.** Numbers, dates, symbols, and abbreviations as they
  are said: "forty percent", "March third", "twenty twenty-six". Digits and
  symbols get misread and throw off the timing.
- **Punctuation is timing.** A period pauses longer than a comma. Unroll a
  long comma list into one clause to keep it moving.
- **One new fact per sentence,** no filler words. A line that runs short
  gets another fact, not another adjective.
- **One voice per piece.** A model that takes a voice (its option has a
  `voice` input role) gets a `voice_ref`: saved and Sceneform voices come
  from `query_generation_options` with `action: "voices"` and the speech
  option's `option_ref`. A model without one, such as Gemini, picks its
  narrator with `settings.voice` instead. Pick one and pass the same one on
  every line of the piece. An audio upload is not a voice.
- **Long scripts** split at sentence ends into parts under 2,048 characters,
  each with the same voice.
- **Check it.** `analyze_media` on the result returns a transcript; compare
  it with the script before using the audio.

### Directing the read

Each speech model takes its direction in a different place:
`references/prompt-speech.md` lists, per model, whether it reads audio tags
and which settings it has. What each kind means:

- **Audio tags**, on a model marked for them: performance cues in square
  brackets inside the `script`, right where they apply: `[whispers]`,
  `[laughs]`, `[sighs]`, `[excited]`, `[sarcastic]`. Each tag adds a short
  pause, so count it against the length. On a model without tags, delivery
  follows the punctuation and the words themselves.
- **`style_instructions`**: one sentence of direction for the whole read,
  "warm and unhurried, like a late-night radio host".
- **`description`**: acting direction: who is speaking, the mood, and the
  pace, "a tired night-shift nurse, quiet and kind, slowing on the last
  line".
- **`stability`**: lower gives a livelier, less even read.
  **`similarity_boost`** keeps it closer to the chosen voice.
- **`language`**: set it when the script is not English.
- **`pitch`, `speed`, `intensity`, `timbre`**: numeric fine-tuning; leave
  them at their defaults unless the user asks for a change.

## Music

The `prompt` names genre, tempo (a BPM beats "upbeat"), instruments, the
feel, and whether it has vocals, in at most two sentences: "Warm lo-fi hip
hop at 85 BPM, dusty Rhodes chords, soft vinyl crackle, brushed drums,
instrumental." `references/prompt-music.md` lists each model's settings.

- **Length.** `settings.duration` takes only the values a model lists: pick
  the shortest that covers the video and trim in the edit. A model with no
  duration setting decides the length itself.
- **Vocals.** A model with `force_instrumental` stays instrumental until you
  set it to false; do that for a song, and write the lyrics into the prompt.
- Under narration: instrumental, sparse, with no lead melody competing with
  the voice.
- Name a sound, never an artist or a song.
- Acoustic, jazz, lo-fi, and small-band prompts pass moderation more
  reliably than big orchestral or "bass drop" ones.

## Sound effects

One sound per prompt: the source, the material, the action, the space, and
the distance. "A ceramic mug set down on an oak table in a quiet kitchen,
close to the microphone." Set the length when the option allows it, and
`loop: true` for an ambience bed that repeats seamlessly. Where offered, a
higher `prompt_influence` follows the words more literally.

## Voice change

Re-voices one finished recording: `audio_ref` plus a `voice_ref` from
`action: "voices"`. Timing and delivery stay; only the voice changes. It
bills the recording's length.

## Lip sync

Needs one finished video `asset_ref` (`video_ref`) and one finished audio
`asset_ref` (`audio_ref`) of about the same length. Works best on a clip
where the face is visible, roughly frontal, and the mouth is never covered.

## Avatar

A talking video from a face and a finished voice track: `image_ref` (an
image `asset_ref` or a `persona_ref`) plus `audio_ref`, with an optional
`prompt` for the scene and style. Make the speech first. The best portrait
faces the camera, shows head and shoulders, has even light, and a closed,
relaxed mouth.

## Checklist

- Speech: the word count fits the target length at about 2.5 words a
  second, numbers are written as words, and one voice (`voice_ref` or
  `settings.voice`) covers the piece.
- Music: tempo, instruments, feel, and vocals are named; the length is set.
- A sound effect names its source, material, and space.
- Lip sync and avatar inputs are finished assets of matching length.
