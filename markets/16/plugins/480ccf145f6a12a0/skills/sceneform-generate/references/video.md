# Video

How to turn a brief into a video prompt. The model's `prompt_guide` sets the
notation (timestamps, shot labels, how speech and sound are written); this
file sets the content.

## Pick the path

- **From text.** The prompt describes everything.
- **From an image.** Pass the frame as `start_frame_ref` and describe only
  what happens next. With an `end_frame_ref` too, describe the one move that
  connects the two frames.
- **With references.** A Persona, product, or Element in `reference_refs`
  supplies identity; it is not a first frame.
- **Change an existing clip.** `reshoot_video`, below.
- **Animated text, numbers, charts, or UI.** sceneform-motion: a video model
  smears lettering and loses the beat.
- **A remix, storybook, or restyle.** `references/short-videos.md`.

Choose the shortest duration that holds the action: about 5 seconds for one
action, 8 to 10 for two or three beats. A longer story is several clips.

To try an idea cheaply, generate it with Seedance 2.5 and
`settings.resolution: "draft"`: a 480p take at the 480p price. Then
`finish_draft` with that video's `asset_ref` as `draft_ref` renders the same
take in 1080p, or in 4K with `resolution: "4k"`, at that resolution's price;
small details can change. A draft can be finished once, within 14 days
(`sceneform finish-draft`, `--resolution 4k`).

## Write one shot

- **Open in motion.** Unless the brief wants a still opening, the first frame
  already moves; an unplanned still opening reads as dead. Say what moves at
  the start.
- **One change.** The opening state, the single thing that changes, and how
  the shot settles. One action described precisely beats three crammed in.
- **One camera move,** with where it starts and stops: "a slow push-in from
  a medium shot to her hands, stopping before the cup leaves the frame". A
  held frame is a valid choice.
- **Motion that models render well:** slow, continuous, small. Sprints,
  jumps, thrown objects, and bouncing balls break physics. Exact counts do
  not hold ("a small crowd", not "twelve people").
- **Feeling as action:** "her shoulders drop and she exhales", not "she
  feels relieved".
- **One action per beat.** "Again", "back and forth", and "opens and closes"
  render as loops. A two-step action (uncap, then spray) is two beats.
- **Energy with magnitude.** Models come back calmer than asked: "fast
  handheld push-in", "a whip pan left", not "dynamic".

## Several beats

Split into beats only when the request carries ordered events, never to
fill time. Use the notation the `prompt_guide` gives.

- Neighbouring shots differ in both size and angle (wide, then close-up from
  low). Two similar neighbours morph into each other instead of cutting.
- Timing marks are hints. Models often land a gesture late, so put the beat
  that must happen early.
- Repeat the subject's identifying details in each beat when the guide says
  the model does not carry them forward.
- Only the opening shot of a place starts wide.

## Camera traps

- An over-the-shoulder shot needs a named person in the foreground, or the
  model invents one.
- Backlit silhouettes go black, and strong glints on metal become white bars.
- Selfie framing with the words "mirror", "phone in hand", or "reflection"
  draws the phone into the shot.
- Shot on a phone: "handheld, slight natural shake". A locked-off shot:
  name it static and leave every motion word out of it.

## Speech and sound in the clip

Check the `prompt_guide`: some models render sound, others are silent.

- Speech: one short line per spoken beat, about six to eight words for five
  seconds. Crowded lines come out rushed. Write numbers as words, keep one
  language per clip, and name the language before a non-English line.
- With dialogue, add "No subtitles."; models burn captions in by default.
- No speech: say mouths stay closed and no narration is added.
- Sound effects land on what moves on screen; room tone and off-screen
  ambience fill the rest when the scene calls for them.
- When exact narration matters, generate the speech separately
  (`references/audio.md`), then lip-sync it or build the video in
  sceneform-motion.

## References in a video

Give each reference one job and name it where the prompt uses it as
`@{ref:<ref>}`, with the exact ref you pass; Sceneform turns the mention into
the model's own token. A mention of the start frame reads as "the start
frame". When the reference shows the person or product exactly, refer to it
and describe what it does, not what it looks like. A product the prompt
describes without an image becomes a made-up product.

Some models also take audio in `reference_refs`: a voice for a character to
speak in, or a track for the motion to follow ("Takes" in
`references/models.md` says which). Name it the same way and say its job: "the
woman speaks in the voice of @{ref:media_abc123}". Send at least one
reference image or clip in `reference_refs` with the audio: Seedance and most
other models refuse audio as the only reference.

## Reshoot an existing clip

`reshoot_video` changes who or what appears in a finished clip and keeps its
motion, timing, and spoken words. Pass the clip's `asset_ref` as
`source_video_ref`, every reference in `reference_refs`, and an
`instruction` that names them `@Image1`, `@Image2` in that order. Say who
appears, what they wear or hold, the place, and the light. Describe a new
person by positive traits ("a man in his 50s with a grey beard and a navy
sweater"), never only as "a different person". The result is as long as the
clip (a Remake rounds it to whole seconds) and the quote is priced on that
length. A Reshoot of the user's own
video ad belongs to sceneform-ad-studio.

`mode: "remake"` (`sceneform reshoot --remake`) redraws the whole video from
the clip's motion, camera, timing, and sound, with the people from the
references. The setting stays unless the instruction names a new one. Use it
for a new look or a new setting, or when the safety filter refuses a Reshoot
of the clip. A Remake can leave the instruction out: each person who has a
reference is replaced with it and everything else stays. A Reshoot of the
clip as filmed always needs one.

`model` (`sceneform reshoot --model`) picks the tier: `pro` by default,
`lite` for a cheaper edit of the clip as filmed (clips up to 15 seconds, 1
to 8 references, no Remake or Ad reshoot), or `kling` (up to 7 references).
`keep_outfit` (`--keep-outfit`) dresses the new person in the clothes from
the clip; Lite cannot. `resolution` (`--resolution`) is 720p unless the user
asks for 480p, 1080p, or 4k (4k is Pro only; Kling has no 480p). `generate_audio: false`
(`--no-sound`) makes a silent result on Pro only. `amount` (`--amount`)
makes up to 4 videos of the same edit; Lite makes one. The quote shows each
choice's credits.

## Aspect ratio

TikTok, Reels, and Shorts take 9:16. YouTube and websites take 16:9. Feeds
take 1:1, or 4:5 when the option offers it. Set it in `settings` when the
option has that control.

## Checklist

- The first frame moves, or the brief asked for a still opening.
- Each shot has one action and one camera move, with an end.
- Beats exist only for ordered events, and neighbours differ in size and
  angle.
- Every reference has one job and an `@{ref:…}` mention where it is used.
- Speech fits the duration, with "No subtitles." when there is dialogue.
- Sound is described only for a model that renders it.

## Fixes

| Observed | Change |
| --- | --- |
| A frozen first second | "in motion from the first frame", with the opening action named |
| A morph where a cut was wanted | neighbouring shots differ in size and angle; a hard cut between them |
| Too calm | the camera move and action with magnitude: fast, handheld, whip |
| A repeating loop | one action per beat, each step its own beat |
| Burned-in captions | "No subtitles." |
| A face or product that drifted | the reference passed again, one shot, one identity source |
| Rushed or cut-off speech | fewer words |
| An extra arm | at most two hand actions; the product held or resting, never floating |
