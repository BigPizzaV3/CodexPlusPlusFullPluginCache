---
name: tapnow-storyboard-film
description: Turn a story, script or ad idea into a storyboarded short film with TapNow - plan the shots, make a keyframe for each, then animate each keyframe into a clip, all in one TapNow project ready to edit. Includes shot-planning craft (shot sizes, camera moves, continuity, pacing, ad and social story structures, keeping the look consistent). Use when the user wants a short film, an ad or commercial, a teaser, a product video with several shots, or a storyboard.
---

# Storyboard film

Script in, a set of matching shots out: a storyboard, one keyframe per shot, one clip per shot, all in one TapNow project.

## Set expectations first

- Each video generation renders one shot. TapNow does not cut the shots into one film, and does not add titles or subtitles. A "30-second commercial" here means a storyboard, a handful of clips and a project; the user assembles the film in TapNow or an editor. Say this in the first reply, and never promise a finished edit.
- Every shot costs two generations on the user's TapNow account: a keyframe and a clip. Before you start, say how many shots there are and get the user's agreement.
- Clip lengths, formats, sound and models depend on the video model. Read them from the `create_video` description instead of assuming them.

## Step 1: Storyboard

Pick a structure, then break it into shots (3–6 is usually right). Show the user one table: shot number, length, shot size and angle, what we see (who, where, doing what), camera move, notes (copy to overlay, vertical or horizontal). Wait for approval before making anything. If the user already has a storyboard, use it and only check it against the rules below.

Fix three things for the whole film and repeat them in every prompt:

- **Format**: horizontal or vertical, the same for every shot.
- **Style anchor** (one or two sentences): palette (two or three specific colors), one kind of light, one lens feel, one texture, one way of moving. For example: "cream, sage and warm wood; soft morning side light; shallow depth of field; clean digital; smooth gimbal moves".
- **Fixed descriptions** of each character and the product, word for word in every shot ("woman in her thirties, short hair, beige linen shirt"; "matte black bottle with fine vertical ridges").

### Structures

| Purpose | Beats | Shots |
| --- | --- | --- |
| Short product ad | hook → product hero shot → benefit → brand and call to action | 3–4, hero shot longest |
| Longer product ad | hook → problem or scene → hero shot → benefit → brand → call to action | 5–6, hero shot near the middle |
| Social video | hook → setup → payoff → call to action | 3–4, a visual hook in the first seconds |
| Brand mood film | atmosphere → emotional peak → brand sign-off | 3–5, slow moves, lots of space |
| Story | setup → conflict → turn → ending | 4–6, shot sizes follow the emotion |

Two rules for ads: plan the product hero shot first and make every other shot serve it; and a short cut is not the long cut with the boring parts removed, but only the hook, hero shot, brand and call to action.

### Shot craft

- **Shot size answers one question.** Wide: where, and what mood. Full: who is doing what. Medium: relationships, handling the product. Close-up: emotion. Extreme close-up: detail and texture, the most reliable shot for products. Change the shot size between neighboring shots; the classic build is wide → medium → close.
- **Angle is attitude.** Eye level is neutral; low angle makes the subject heroic; high angle and top-down suit hands, tabletop and flat lays.
- **One move per shot.** Static, push in, pull out, pan, follow, orbit, or rise. Slow and steady looks better than fast. Let either the subject or the camera carry the motion, not both.
- **Leave room for copy.** In ad shots keep about a third of the frame clear and say where ("subject on the left, space on the right").
- **Continuity.** Keep the camera on one side of the line between two characters, or between a person and the product, so screen direction never flips. Match eyelines. Cut motion to motion and still to still. Each shot adds one new piece of information.
- **Pacing.** Slow emotion means longer shots and slower moves; tension means shorter shots. The first shot has to stop the scroll.
- **Silent and vertical.** Most social video plays muted, so every shot must read without sound. Vertical frames are narrow: keep the subject centered and avoid wide vistas. If the film is needed in both formats, make keyframes for each format; do not crop one into the other.

## Step 2: Keyframes

1. For each shot, call `create_image` in the film's format. Prompt: style anchor + shot size and angle + fixed description + the moment in the scene + light + where the empty space goes. Describe one moment only.
2. Keep the look consistent with references: pass the product photo, a character image, or the first approved keyframe as reference images to the later keyframes. For product shots, a real product photo or a finished product shot is the best keyframe of all.
3. When every keyframe is done, show them together and let the user swap shots now. Changing a keyframe costs far less than changing a clip.

## Step 3: Clips

1. Animate the first shot only: `create_video` with that keyframe as the image, its project ID and the shot's length. The prompt describes motion only: camera move and speed, what the subject does, how the frame evolves, and the style anchor's way of moving. Do not describe the picture again.
2. If the video model list offers a faster model for previews, use it for this first clip, and render the finals once the user likes the direction.
3. Show the first clip, then submit the remaining shots one at a time. Video renders take minutes: use the waiting option of `get_production_result` instead of asking again and again.
4. A failed shot will not recover. Say so, offer to retry that shot, and carry on with the others. Never submit the same shot twice while it is still rendering.

## Step 4: Deliver

- The storyboard table with a playable link for each shot.
- The TapNow project link: every keyframe and clip is there, ready to arrange and edit.
- Which clips are previews, and an offer to render them as finals.

## Common mistakes

- The product gets lost: the story runs long and the hero shot is short or missing.
- Several moves or actions crammed into one shot.
- Crossing the line: screen direction flips between neighboring shots of the same scene.
- Two neighboring shots at the same size, or every shot a push in.
- A shot that only makes sense with sound.
- Animating keyframes the user has not approved.
