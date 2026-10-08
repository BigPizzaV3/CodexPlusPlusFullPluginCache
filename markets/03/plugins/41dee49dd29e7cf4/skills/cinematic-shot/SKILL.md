---
name: cinematic-shot
description: Create a short cinematic clip from a written idea or a reference frame, using film camera and lighting language. Trigger when the user asks for a cinematic shot, a film-look clip, a movie scene, b-roll, an establishing shot, a moody or atmospheric video, or describes a scene they want shot. Do not trigger for animating a personal photograph, for product marketing videos, for editing existing footage, or when the user wants a still image rather than motion.
---

# Cinematic Shot

Produce one short clip built with deliberate film grammar rather than a generic description.

## Morphix tool contract

These are the tools available and the order they run in. Follow it exactly.

**Getting the user's image in.** Chat attachments cannot be passed to generation. When a reference is needed, call show_upload_widget, which shows a drop box and returns an asset id once the user uploads. Never call upload_asset directly. If the user uploaded something earlier in the conversation, call get_assets and reuse that asset id rather than asking again.

**Before spending credits.** Call explore_models to choose a model for this job, and get_account to confirm the user has credits. Both are read-only and free. Choosing a model blind, or starting a generation the user cannot pay for, are the two most common wasted turns.

**Choosing a model.** Never hardcode a model name. Read the capabilities returned by explore_models and pick for the job at hand: reference fidelity when the result is anchored to a supplied image, text handling when legible type matters, motion quality for video, voice range for audio.

**Generating.** generate_image and generate_video accept asset ids to edit or reference existing images, including image-to-video. generate_audio takes the script plus a voice chosen through explore_models. Each spends credits and renders a live view that polls itself, so never poll manually and never tell the user you will check back.

**Retry spends again.** A regeneration costs credits a second time. The quality gate in this skill allows one automatic retry. Beyond that, say what is wrong and let the user decide.

**Finishing.** upscale_image and upscale_video raise an existing asset. Offer these instead of regenerating at a larger size.

**Recovering work.** get_assets lists the library newest first. get_generations fetches a generation by id. Use them to pick up earlier work instead of remaking it.

## The difference this skill makes

A generic video prompt returns motion. A cinematic shot returns a decision: a specific lens, a specific light source, a specific camera behaviour, and a reason for all three. Always make those decisions explicitly, and state them back to the user in one line so they can redirect.

## Preconditions

Either a written scene description or a reference frame. If the user supplies a photograph of a real person, route to photo-to-video instead, which protects likeness.

## Intake

Ask once, bundled: the scene; the mood in one word; duration; and aspect ratio. Offer five, eight, and ten seconds. If the user gives only a subject with no mood, choose one, say which you chose, and proceed.

## Build the shot from four decisions

Make all four before writing a word of the prompt.

**1. Shot size.** Extreme wide for scale and isolation. Wide for context. Medium for relationship. Close for intent. Extreme close for texture and tension. Do not default to medium.

**2. Lens behaviour.** Wide angle exaggerates depth and distorts edges, good for space and unease. Normal reads neutral and documentary. Long lens compresses planes and separates subject from ground, good for intimacy and surveillance. Name the implied focal length in the prompt.

**3. Light.** Name the source, direction, and quality. Hard low sun from behind for rim and haze. Soft north window from the side for skin and melancholy. Single practical in frame for noir. Overcast top light for flat realism. Moonlight and fill for night. Light is what separates cinematic from rendered.

**4. Camera behaviour.** Locked for stillness and dread. Slow push for growing focus. Slow pull for reveal and loneliness. Handheld drift for presence and unease. Slow lateral track for observation. Crane or tilt for scale. One move per shot, never two.

## Grade and atmosphere

Name the grade in concrete terms: cold shadows with warm highlights, bleached and low contrast, heavy blacks with a single colour source, natural and unpushed. Avoid the phrase cinematic as a style word in the prompt, because it collapses into a generic look. Describe what makes it cinematic instead.

Atmosphere carries motion cheaply and safely: dust in a beam, rain on glass, fog rolling, steam, embers, curtains, foliage. Add at least one when the frame would otherwise be static.

## Write the prompt

One continuous description: subject and action, setting, shot size, implied lens, light source and direction, camera behaviour and speed, atmosphere, grade, and duration.

Avoid stacked style words, avoid naming directors or films, avoid trademarked looks.

## Execute

Call generate_video with the reference frame when one exists. Use sixteen-by-nine for film feel, nine-by-sixteen for vertical social, and two-point-three-nine to one only if the user asks for anamorphic framing.

## Quality gate

Reject if the clip drifts into a different scene, if the light source changes direction mid shot, if the camera performs a second unrequested move, if faces or hands deform, or if text appears in frame.

Regenerate once with a slower move or a simpler frame.

## Deliver

Return the clip and one line naming the four decisions made: shot size, lens, light, camera. That line is what lets the user ask for a different take rather than a different prompt.

## Stop conditions

| Condition | Response |
|---|---|
| Neither description nor reference supplied | Stop and ask what the scene is |
| User supplies a photo of a real person to animate | Route to photo-to-video |
| Request names a specific film, director, or trademarked look | Offer the underlying technique instead |
| Quality gate fails twice | Deliver the most coherent take and state what broke |
