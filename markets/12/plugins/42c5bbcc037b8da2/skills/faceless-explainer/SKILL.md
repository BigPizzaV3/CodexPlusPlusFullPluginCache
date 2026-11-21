---
name: faceless-explainer
description: "A narrated video with no presenter, from a topic or document, in a style you can pick. Use for \"faceless video\", \"explainer\", \"YouTube Shorts about\", \"narrated story\", \"documentary video\", \"stickman cartoon\", \"editorial motion graphics\", \"paper diorama video\", \"picture story\", \"children's song video\", \"turn this article into a video\"."
---

# Faceless explainer video

## Ask first

- The topic or source text, and the length.
- The look: offer two or three styles from the list below that suit the topic.
- The shape: 9:16 for Shorts and TikTok, 16:9 for YouTube.

## Pick the kind

| Kind | Use it for | How it is built |
| --- | --- | --- |
| Explainer | An idea or a process | One idea per scene, 8 to 10 seconds each, with simple diagrams and no rapid cuts |
| Story or documentary | History, true stories, lists | Shots of 3 to 6 seconds. Vary the distance, angle and place so neighbouring shots differ |
| Picture story | A low budget, or when they ask for stills | One still per narration beat, with slow motion added to some or all of them |
| Children's song | Only when they ask for a song | Lyrics first, with verses and a repeating chorus. Then 10-second scenes showing what the lyrics name, with no lip sync |

## Styles

Write one style description and repeat it word for word in every scene prompt, so the video looks like one piece.

| Style | Description |
| --- | --- |
| Editorial motion graphics | A warm beige handmade-paper set, cutout figures and props with thin white borders and soft shadows, some black-and-white engraving cutouts, deep crimson accents such as a big paper circle and marker lines, lots of empty paper |
| Stickman cartoon | A simple flat cartoon: chibi characters with round heads as big as their bodies, very thick dark outlines, flat colours with one shadow tone, cute faces with dot eyes and thick eyebrows, a warm muted palette |
| Paper diorama | A miniature set of craft paper, cardboard and old newspaper with faint print, cutout paper figures, one accent colour such as teal-blue sails, warm side light, shallow focus and floating dust |
| Pastel flat | Flat shapes in soft pastel colours, no outlines, friendly and simple |
| Hand drawn | Ink and pencil lines with a light watercolour wash and visible paper, like a sketchbook |
| Fairy tale | Painted 2D scenes, rich jewel colours, warm light against deep shadow, expressive characters |
| Mannequin | Matte clay figures with no faces, simple sets, even neutral light |
| Documentary | Photographic stills, natural light, muted colour, details true to the period |
| Children's 3D | Soft rounded characters, bright colours, simple toy-like sets |

## Plan

1. Write the script at about 2.5 words a second, with a hook in the first line. Stick to facts you can support, and say when something is uncertain.
2. Split it into scenes. For each one, write one line of narration and one line of what is on screen, showing the action the narration names. Keep words out of the pictures unless they ask for them: image models misspell.
3. List recurring characters, places and props. Give each one a short fixed description, and make a reference image for any that appear more than twice.
4. Show the script, the scene list and the total price. Video is most of the cost, so offer a picture story as a cheaper option.

## Make it

| Part | Model | Notes |
| --- | --- | --- |
| Voiceover | `generate_heygen_voice_speech` | One request per scene line, so each line's length is known. Pick a voice that suits the story |
| The first scene still | `generate_gpt_image_2_5_image` | Sets the style. Show it before making the rest |
| The other scene stills | `edit_gpt_image_2_5_image` | Give it the first still and say "in exactly the same style as the image", so every scene matches. Add a character's earlier still to keep them the same |
| Moving scenes | `generate_seedance_2_5_video` | Three stills per clip, each opening one shot, with the clip as long as their three lines. Ask for gentle movement in the style of the stills, no text and no speech |
| A song or background music | `generate_ace_step_music` | Only when they ask for one |

Make the voiceover first and fit the scenes to its real length: each scene lasts as long as its line. If the narration runs long, tighten the script rather than rushing the voice.

## Deliver

Give the voiceover, then the clips in order with their narration line. RunComfy has no tool for joining clips or adding captions: join them with ffmpeg if you can run commands, otherwise explain that the user can drop them into any editor in that order.

## Rules for every RunComfy skill

- Reply in the user's language. Tool arguments stay in English.
- Ask at most three short questions before starting, with choices where you can. Skip what the request, an attached file or an earlier turn already answers, and use a sensible default for the rest. Do not turn a single generation into a long workflow.
- Each step names the RunComfy tool to use. Never guess its inputs: use the ones the tool lists.
- Price first. Each generation tool names its model: read that model's price with `get_model` and tell the user the model and the total for the whole plan, adding up every step. Wait for their yes. Anything beyond the plan they agreed to, or a dearer model, needs another yes.
- Files. Tool inputs take public https links. For a past result use `list_my_generations` and for a file in My Assets use `get_asset_download_url` when they are available. Otherwise ask the user for a public link.
- Run with `wait_for_completion: false` and keep the `request_id`. Check `get_model_request_status` no more than every 15 seconds for images and every 30 seconds for video, then `get_model_request_result`. A timeout or an unclear outcome is not a failure: check the request before submitting again.
- Prompts. Be concrete: subject, setting, camera, light, style. For an edit, say what stays the same and what changes, and do not describe the rest of the image. For image to video, describe the motion, not the frame. Say what you want rather than what you do not want. With two or more references, open the prompt by naming each one, such as "image 1 is the product, image 2 is the creator".
- Work you do not own. Use someone else's image or video for its mood, pacing and layout only. Do not copy its people, logos, words or exact composition.
- Truth. Use only facts the user gave you or that you can point to. Never invent claims, results, prices, discounts, statistics, testimonials, awards or certifications.
- Several results. When a plan has many parts, make one, check it, then make the rest. Each result should differ in a way you can name, not be the same picture reworded. Redo only what is wrong and say what was wrong. If a safety filter refuses a prompt, tell the user instead of working around it.
- Deliver the output links with a short label for each. No raw JSON, no internal ids and no running commentary on status checks unless the user asks.
