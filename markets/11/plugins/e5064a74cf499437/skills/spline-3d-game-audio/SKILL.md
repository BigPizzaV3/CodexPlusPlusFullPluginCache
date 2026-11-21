---
name: spline-3d-game-audio
description: "Procedural WebAudio sound effects for games and interactive scenes (no audio assets): the shared synth helpers, AudioContext resume-on-gesture wiring, and per-effect recipes — engine hum, weapons, footsteps, pickups, win/lose stingers. Load alongside the games skill when writing the sound code."
---

## Procedural sound effects (WebAudio — on by default)

Games ship with sound unless the user says otherwise, and every sound is
SYNTHESIZED in the document with the WebAudio API: the sandbox has no
guaranteed network, so there are no audio assets to fetch — and none are
needed. Oscillators, one noise buffer and gain envelopes cover the whole
classic game palette for zero bytes. (The scene's own `'Audio'` actions
need uploaded sound assets — they are not part of a code-driven game.)

Plumbing rules:
- ONE `AudioContext`, created — or `ctx.resume()`d — INSIDE the Start
  click handler. Browsers block audio until a user gesture, which the
  start gate provides by design; never create the context at boot.
- ONE master gain (~0.2) between everything and `ctx.destination` — SFX
  stack fast and headroom prevents clipping. A HUD mute toggle is just
  flipping `master.gain.value`.
- One-shots build fresh nodes per trigger: oscillator or noise source →
  gain envelope → master. Envelope = `gain.setValueAtTime(vol, t)` then
  `gain.exponentialRampToValueAtTime(0.001, t + dur)` (never ramp to
  exactly 0), and `stop(t + dur)` so the nodes free themselves.
- Continuous sources (engine, wind) are created ONCE at init, run forever
  through their own gain starting at 0, and the game loop writes their
  frequency/gain every frame — this is all inside the iframe, no bridge
  traffic. Duck them to 0 in `setState` for any state that isn't
  `'playing'` (the loop early-returns there and won't do it for you).
- Pitch sweeps (lasers, jumps, slides) are one more line on a one-shot:
  `o.frequency.exponentialRampToValueAtTime(target, t + dur)`.

The worked example carries `audioInit` + a `blip` oscillator one-shot;
add this filtered-noise `thud` (sharing one noise buffer) when the game
needs steps, hits or shots:

```
let noise;
function thud(dur = 0.08, cutoff = 600, vol = 0.35) {
  if (!noise) {
    noise = ctx.createBuffer(1, ctx.sampleRate, ctx.sampleRate);
    const d = noise.getChannelData(0);
    for (let i = 0; i < d.length; i++) d[i] = Math.random() * 2 - 1;
  }
  const t = ctx.currentTime;
  const src = ctx.createBufferSource();
  src.buffer = noise;
  const f = ctx.createBiquadFilter();
  f.type = 'lowpass';
  f.frequency.value = cutoff;
  const g = ctx.createGain();
  g.gain.setValueAtTime(vol, t);
  g.gain.exponentialRampToValueAtTime(0.001, t + dur);
  src.connect(f).connect(g).connect(master);
  src.start(t);
  src.stop(t + dur);
}
```

The palette:
- **Car engine**: looping sawtooth → lowpass → gain (the example). Map
  frequency 40–180 Hz and filter cutoff 300–1200 Hz from `|speed| / TOP`
  each frame — the pitch rise IS the acceleration feel. Two slightly
  detuned oscillators into the same filter sound richer.
- **Footsteps** (walking/running): `thud(0.05, 600, 0.25)` on a cadence
  timer while moving and grounded — every ~0.34s walking, ~0.22s running.
- **Jump**: a blip with a rising sweep (150→600 Hz over ~0.18s);
  **landing**: a deeper `thud(0.1, 300, 0.5)`.
- **Weapons**: laser = square blip swept DOWN (900→120 Hz, ~0.12s);
  gunshot = a loud 60ms noise burst (highpass ~1000 Hz instead of the
  lowpass) + a 150 Hz sine thump; explosion = a 0.4–0.6s noise burst with
  the lowpass cutoff sweeping 3000→100 Hz.
- **Pickup/coin**: two ascending square blips (880 then 1320 Hz, ~70ms
  apart — the example). **Win**: a little arpeggio (523/659/784 Hz
  triangle notes, ~120ms apart); **lose/hit**: one descending saw sweep
  (400→80 Hz, ~0.3s).
