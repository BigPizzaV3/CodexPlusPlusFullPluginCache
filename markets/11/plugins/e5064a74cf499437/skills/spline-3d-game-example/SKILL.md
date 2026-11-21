---
name: spline-3d-game-example
description: "The complete worked example for the games skill: a drive-&-collect game end to end — the run_code scene call and the full HTML game document (start gate, input, fixed-timestep loop, chase camera with exact aim math, JS collisions, HUD, restart-from-snapshots, sound hooks). Load it when building a NEW game or game-like scene; edits to an existing game usually only need the games skill itself."
---

# Games — worked example (drive & collect)

This is the reference implementation of the `games` skill's rules — load
that skill first; every contract it states is instantiated here.

## Worked example — drive & collect

Scene (one run_code call):

```
mesh('Plane', { width: 9000, height: 9000 });
rotation({ x: -90 }); position({ y: 0 }); color('#8fbf6f'); rename('Ground');

// player car — placeholder box. When the generated hero lands, run the
// swap procedure above: scale/wrap/yaw-fix the mesh, remove() THIS
// object, give the wrapper this exact name, wheels at group-local y = 0.
mesh('Cube', { width: 180, height: 90, depth: 340 });
position({ x: 0, y: 60, z: 0 }); color('#e0552b'); rename('Player');

for (let i = 0; i < 6; i++) {
  const a = (i / 6) * Math.PI * 2;
  mesh('Cylinder', { radius: 60, height: 16 });
  position({ x: Math.cos(a) * 1600, y: 90, z: Math.sin(a) * 1600 });
  rotation({ x: 90 }); color('#f2c14e'); rename('Coin ' + (i + 1));
}

// chase camera at the ROOT (never grouped), aimed like the game loop aims it
const cam = add('PerspectiveCamera');
rename('ChaseCam'); position({ x: 0, y: 320, z: -720 }); // behind & above
rotation({ x: 12, y: 180 }); // ≡ aimEuler(0, -12): along +Z, tilted down 12°
setPlayCamera(cam);
playControls('none'); // game code drives the camera — no play orbit controls

// size matches the ground span — the default 2000 shadow footprint would
// cut shadows off a quarter of the way across this 9000-unit play area
light('Directional', { intensity: 0.9, size: 9000 });
translate({ x: 500, y: 900, z: 400 });
background('#bfd9ee');
```

The complete game document (set_html_content):

```html
<!doctype html>
<html>
<head>
<style>
  #stage { position: fixed; inset: 0; }
  .panel { position: fixed; inset: 0; display: flex; flex-direction: column;
           align-items: center; justify-content: center; gap: 14px;
           background: rgba(10,12,18,.55); color: #fff;
           font: 15px/1.5 system-ui; text-align: center; }
  .hud { position: fixed; top: 16px; left: 16px; padding: 10px 14px;
         border-radius: 10px; background: rgba(10,12,18,.7); color: #fff;
         font: 13px/1.6 system-ui; }
  button { font: 600 15px system-ui; padding: 12px 28px; border: 0;
           border-radius: 10px; background: #4c8dff; color: #fff;
           cursor: pointer; }
  .hidden { display: none; }
</style>
</head>
<body>
<div id="stage"></div>
<div class="hud hidden" id="hud">
  Coins: <span id="score">0</span>/6 · <span id="kmh">0</span> km/h
</div>
<div class="panel" id="menu">
  <h1>Coin Chase</h1>
  <p>W/↑ throttle · S/↓ brake · A D/← → steer · R restart</p>
  <button id="start">Start</button>
</div>
<div class="panel hidden" id="paused">
  <h1>Paused</h1>
  <button id="resume">Resume</button>
</div>
<div class="panel hidden" id="over">
  <h1>You win!</h1>
  <button id="again">Play again</button>
</div>
<script>
(async () => {
  await spline.ready;
  const player = await spline.findObjectByName('Player');
  const cam = await spline.findObjectByName('ChaseCam');
  const coins = (await spline.getAllObjects())
    .filter((o) => o.name.startsWith('Coin '));

  const keys = new Set();
  let state = 'menu'; // 'menu' | 'playing' | 'paused' | 'over'
  let x, z, yaw, speed, score; // sim state — integrated at a FIXED step
  let vx, vz, vyaw;            // visual state — low-passed copy that gets written
  let cx, cy, cz;              // eased chase camera

  // ---- procedural sound (created on Start — the click unlocks audio) ----
  let ctx, master, engine;
  function audioInit() {
    if (ctx) { ctx.resume(); return; }
    ctx = new AudioContext();
    master = ctx.createGain();
    master.gain.value = 0.2; // headroom — every SFX routes through this
    master.connect(ctx.destination);
    const filt = ctx.createBiquadFilter();
    filt.type = 'lowpass';
    engine = { osc: ctx.createOscillator(), filt, gain: ctx.createGain() };
    engine.osc.type = 'sawtooth';
    engine.gain.gain.value = 0; // silent until 'playing' (see setState)
    engine.osc.connect(filt).connect(engine.gain).connect(master);
    engine.osc.start();
  }
  function blip(freq, dur = 0.09, type = 'square', delay = 0) {
    const t = ctx.currentTime + delay;
    const o = ctx.createOscillator();
    const g = ctx.createGain();
    o.type = type;
    o.frequency.setValueAtTime(freq, t);
    g.gain.setValueAtTime(0.5, t);
    g.gain.exponentialRampToValueAtTime(0.001, t + dur);
    o.connect(g).connect(master);
    o.start(t);
    o.stop(t + dur);
  }

  const el = (id) => document.getElementById(id);
  function setState(next) {
    state = next;
    if (engine) engine.gain.gain.value = state === 'playing' ? 0.1 : 0;
    el('menu').classList.toggle('hidden', state !== 'menu');
    el('paused').classList.toggle('hidden', state !== 'paused');
    el('over').classList.toggle('hidden', state !== 'over');
    el('hud').classList.toggle('hidden', state === 'menu');
  }
  function reset() {
    ({ x, z } = player.position);
    yaw = player.rotation.y; speed = 0; score = 0;
    vx = x; vz = z; vyaw = yaw; // visuals start ON the sim
    el('score').textContent = '0';
    for (const c of coins) {
      c.taken = false;
      spline.updateObject(c.id, { visible: true });
    }
    spline.updateObject(player.id, { position: { x, z }, rotation: { y: yaw } });
    moveCamera(0); // 0 = snap to the chase point, no swoop-in
  }
  el('start').onclick = () => { audioInit(); reset(); setState('playing'); };
  el('again').onclick = () => { audioInit(); reset(); setState('playing'); };
  el('resume').onclick = () => { audioInit(); setState('playing'); };
  // Focus loss = keys go dead (toolbar Play, tab switch, chrome clicks).
  // Never stay 'playing' deaf: clear held keys and gate on a Resume click,
  // which brings focus back into this document.
  addEventListener('blur', () => {
    keys.clear();
    if (state === 'playing') setState('paused');
  });

  const GAME_KEYS = ['KeyW', 'KeyA', 'KeyS', 'KeyD', 'ArrowUp', 'ArrowDown',
    'ArrowLeft', 'ArrowRight', 'KeyR'];
  addEventListener('keydown', (e) => {
    if (GAME_KEYS.includes(e.code)) e.preventDefault();
    keys.add(e.code);
    if (e.code === 'KeyR' && state !== 'menu' && !e.repeat) {
      reset(); setState('playing');
    }
  });
  addEventListener('keyup', (e) => keys.delete(e.code));
  const held = (...codes) => codes.some((c) => keys.has(c));

  const wrap = (d) => ((d + 540) % 360) - 180;
  const damp = (a, b, rate, dt) => a + (b - a) * (1 - Math.exp(-rate * dt));
  const dampAngle = (a, b, rate, dt) =>
    a + wrap(b - a) * (1 - Math.exp(-rate * dt));
  function aimEuler(yawDeg, pitchDeg) { // see Layer 2 — exact XYZ aim
    const yr = (yawDeg + 180) * Math.PI / 180;
    const pr = pitchDeg * Math.PI / 180;
    const cy = Math.cos(yr), sy = Math.sin(yr);
    const cp = Math.cos(pr), sp = Math.sin(pr);
    const r2d = 180 / Math.PI;
    return {
      x: Math.atan2(sp, cy * cp) * r2d,
      y: Math.asin(sy * cp) * r2d,
      z: Math.atan2(-sy * sp, cy) * r2d,
    };
  }

  // Eased follow + aim-at-car (Layer 2): the car and the camera are two
  // separate updateObject writes that can land a render frame apart — a
  // camera bolted to "car minus offset" turns that skew into the car
  // buzzing in place at speed. Everything here reads the VISUAL state.
  const CAM_DIST = 720, CAM_HEIGHT = 320, CAM_AIM_UP = 120;
  function moveCamera(dt) {
    const pr = (vyaw * Math.PI) / 180;
    const gx = vx - Math.sin(pr) * CAM_DIST;
    const gz = vz - Math.cos(pr) * CAM_DIST;
    if (dt) {
      cx = damp(cx, gx, 6, dt); cy = damp(cy, CAM_HEIGHT, 6, dt);
      cz = damp(cz, gz, 6, dt);
    } else { cx = gx; cy = CAM_HEIGHT; cz = gz; } // reset: snap
    const dx = vx - cx, dy = CAM_AIM_UP - cy, dz = vz - cz;
    spline.updateObject(cam.id, {
      position: { x: cx, y: cy, z: cz },
      rotation: aimEuler(Math.atan2(dx, dz) * 180 / Math.PI,
                         Math.atan2(dy, Math.hypot(dx, dz)) * 180 / Math.PI),
    });
  }

  const ACCEL = 2200, BRAKE = 3200, DRAG = 1.4;
  const TOP = 2400, TOP_REV = -700, STEER = 150;
  const STEP = 1 / 120; // FIXED sim step — raw-dt integration lurches on hitches
  let acc = 0, hudT = 0, last = performance.now();

  function simulate(dt) { // fixed-step slices only — never the frame delta
    const throttle = held('KeyW', 'ArrowUp') ? 1 : 0;
    const brake = held('KeyS', 'ArrowDown') ? 1 : 0;
    speed += (throttle * ACCEL - brake * BRAKE) * dt;
    speed = Math.max(TOP_REV, Math.min(TOP, speed * Math.exp(-DRAG * dt)));
    const steer = (held('KeyA', 'ArrowLeft') ? 1 : 0) -
      (held('KeyD', 'ArrowRight') ? 1 : 0);
    yaw += steer * STEER * (speed / TOP) * dt; // no pivoting in place
    const rad = (yaw * Math.PI) / 180;
    x = Math.max(-4300, Math.min(4300, x + Math.sin(rad) * speed * dt));
    z = Math.max(-4300, Math.min(4300, z + Math.cos(rad) * speed * dt));
  }

  (function tick(now) {
    requestAnimationFrame(tick);
    const dt = Math.min((now - last) / 1000, 0.05);
    last = now;
    if (state !== 'playing') return;

    acc += dt;
    while (acc >= STEP) { simulate(STEP); acc -= STEP; }

    // what the scene shows is a low-passed copy — a dropped frame can't jump
    vx = damp(vx, x, 25, dt); vz = damp(vz, z, 25, dt);
    vyaw = dampAngle(vyaw, yaw, 25, dt);
    spline.updateObject(player.id,
      { position: { x: vx, z: vz }, rotation: { y: vyaw } });
    moveCamera(dt);

    // engine hum: pitch and brightness follow the speed
    engine.osc.frequency.value = 40 + (Math.abs(speed) / TOP) * 140;
    engine.filt.frequency.value = 300 + (Math.abs(speed) / TOP) * 900;

    for (const c of coins) {
      if (c.taken) continue;
      if (Math.hypot(c.position.x - x, c.position.z - z) < 170) {
        c.taken = true;
        score++;
        spline.updateObject(c.id, { visible: false });
        el('score').textContent = String(score);
        blip(880);
        blip(1320, 0.12, 'square', 0.07);
        if (score === coins.length) {
          [523, 659, 784].forEach((f, i) => blip(f, 0.18, 'triangle', i * 0.12));
          setState('over');
        }
      }
    }
    hudT += dt;
    if (hudT >= 0.1) { // ~10 Hz — DOM text every frame causes hitches
      hudT = 0;
      el('kmh').textContent = String(Math.round((Math.abs(speed) / 200) * 3.6));
    }
  })(last);
})();
</script>
</body>
</html>
```
