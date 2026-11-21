# Shot-level production routing

## Contents

1. Generation modes
2. Generation unit
3. Reference roles
4. Router inputs
5. Provider candidates
6. Capability refresh and brand benchmark
7. Cost and approval
8. Asset registry

## Generation modes

- `text_to_video`: atmosphere or scenes without a locked subject
- `image_to_video`: animate a supplied first frame
- `reference_to_video`: preserve characters, products, or style references
- `remotion_only`: exact graphic motion, text, CTA, UI, or fallback
- `screen_recording`: real product interaction when authenticity matters

## Generation unit

Default a hero moment to `coherent_shot` when it can be described as one camera setup and one dominant cause-and-effect event. For example, `impact -> surface rupture -> character emergence -> landing` may remain one five- or six-second generation when the viewer must believe that the same body caused and completed the event.

Do not split at every storyboard beat. Split when:

- exact UI, Japanese text, logo, price, CTA, or proof must stay deterministic;
- the camera setup or visual world changes;
- the shot contains two unrelated dominant events;
- privacy or upload policy changes;
- the selected model cannot jointly control identity, physical interaction, camera, and timing after a comparable subject test.

Prompt length does not create control. When the control burden is high, first simplify the shot and use explicit reference roles. Add a motion driver only when motion remains the unresolved risk and the user approves the driver. Only then consider another model or a split.

## Reference roles

Label every reference by what it is allowed to control:

- `identity_front`: front-facing subject identity and proportions;
- `identity_three_quarter`: volume, side features, props, and depth;
- `motion_driver`: timing, path, force, pose sequence, and screen occupancy only;
- `first_frame`: an exact starting composition when the adapter supports it;
- `last_frame`: an exact endpoint when it will not suppress the required acceleration;
- `scene_style`: environment, material, lighting, or palette only;
- `human_animatic`: human comprehension and timing review only; `conditioning` is false by default.

Start with the two identity directions when they are sufficient. More references are not automatically better and can create conflicting controls. If a motion driver is explicitly useful and approved, it should be a neutral silhouette or simple proxy without brand texture, facial detail, text, or a polished environment; state `motion_only` in both the manifest and provider prompt. If the driver itself feels wrong, anxious, comic, or over-directed, remove it rather than asking the model to imitate it.

## Router inputs

Evaluate each shot using:

- duration, ratio, and resolution
- character and product consistency
- start/end frame control
- native audio need
- exact text need
- maximum cost and latency
- privacy and upload constraints
- configured providers
- commercial-use status

Return multiple candidates with reasons, price, risks, and current capability state. Do not hard-code one provider as the strategy.

## Provider candidates

Keep provider adapters and model profiles separate. A model profile describes capabilities and current pricing. An adapter handles upload, submit, poll, download, and metadata.

For fal:

- use the official model endpoint and current schema
- inspect official price immediately before execution
- encode the endpoint's current request shape in `candidate.providerInput`; the adapter replaces only exact `{{prompt}}`, `{{durationSeconds}}`, and `{{uploadedInputUrl}}` tokens
- set `candidate.outputUrlPath` to the returned video URL path, such as `video.url`; verify it against the official endpoint schema
- upload inputs only after approval
- retain request ID, endpoint, model profile, prompt hash, input hashes, timestamps, retry count, estimated and actual cost
- download the result locally before considering the job successful

Treat model fidelity as unverified until the actual brand subject has passed creative QC.

## Capability refresh and brand benchmark

Capabilities, pricing, duration limits, supported reference counts, and endpoint schemas change quickly. Before provider lock:

1. Check official model and provider documentation on the current date.
2. Record which roles are actually supported: first/last frame, identity image, multi-reference, motion/video reference, edit, audio, duration, aspect ratio, and resolution.
3. Keep at least two viable candidate routes when the hero intent is high risk.
4. Use the same approved reference pack and the same causal intent for a paid brand-subject benchmark.
5. Require a fresh paid-execution approval for each benchmark attempt.

A public benchmark or general quality arena is discovery evidence only. It cannot establish character fidelity, causal interaction, or brand suitability for the current job.

## Cost and approval

Exploration defaults:

- one shot
- one output
- one attempt
- explicit maximum cost
- pending approval

Reject execution when pricing is missing or stale, cost exceeds the limit, approval is pending, credentials are absent, or retry count exceeds the job limit.

Also reject execution unless `animatic-review.json` is approved for every Hook named by the Hook portfolio approval and every human review check is `PASS`. Hook/Body approval alone permits only low-fidelity preproduction.

## Asset registry

Record job and shot IDs, provider and endpoint, model and adapter versions, prompt and input hashes, seed, request ID, timestamps, cost, durable local path, output hash, and QC state.

Do not expose credentials or persist signed URLs as the only copy.

## fal adapter contract

Represent a selected route like this after verifying the endpoint's current official schema:

```json
{
  "provider": "fal",
  "selected": true,
  "endpoint": "fal-ai/verified-model-endpoint",
  "modelProfileId": "profile-with-date",
  "providerInput": {
    "prompt": "{{prompt}}",
    "image_url": "{{uploadedInputUrl}}",
    "duration": "{{durationSeconds}}",
    "generate_audio": false
  },
  "outputUrlPath": "video.url"
}
```

Run `fal-generation-adapter.mjs` without `--execute` first. Dry-run never imports the provider client, reads credentials, uploads an input, or submits a request. `--execute` is valid only after Animatic approval, current pricing, explicit paid approval, and a one-attempt shot manifest are recorded.
