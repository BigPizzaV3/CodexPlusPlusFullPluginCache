---
name: spline-3d-texture-drawing
description: "The generateTexture contract and recipes: draw seamless repeating textures locally with canvas 2D (brick/stone walls, wood planks, roof tiles, ceramic/checker floors, pavement) — the seam-wrap rules (rng-only randomness, save/restore transforms, opaque base, one draw per feature), sizing/repeat math, and worked per-material drawing recipes. Load BEFORE writing any generateTexture call."
---

# Drawing seamless textures (generateTexture)

Load `materials-and-look` for where texture layers fit in the material
stack; this skill is the drawing contract for making the texture itself.

### generateTexture — draw seamless patterns locally (canvas 2D)

`generateTexture(name, draw, size?)` renders your own canvas-2D drawing into
a SEAMLESS tile and mints it as an image asset — locally and instantly, no
image service, no quota, no checkerboard wait. It is THE tool for crisp
REPEATING, GEOMETRIC real-world detail: brick/stone walls, roof tiles, wood
planks and parquet, ceramic/checker floors, pavement, windows-grid facades,
woven/fabric grids. (Keep `style` generation for photographic/organic looks —
bark, marble, rust, lava — and the noise layer for formless micro-variation.)

```
// call 1 — draw the tile and apply it (same block is fine)
const bricks = generateTexture('Red Bricks', (ctx, { size, rng }) => {
  ctx.fillStyle = '#b8b0a4';                       // opaque mortar base — ALWAYS first
  ctx.fillRect(0, 0, size, size);
  const rows = 8, gap = size * 0.012;
  const bh = size / rows;
  for (let r = 0; r < rows; r++) {
    const bw = size / 4;
    const shift = (r % 2) * bw * 0.5;              // running bond offset
    // Draw each brick ONCE (cover [0, size) plus the shift overhang) — the
    // replication passes complete whatever pokes past an edge on the other
    // side. Never draw a feature twice "to cover both edges": the two
    // copies would get different rng() values and the seam would mismatch.
    for (let c = 0; c < 4; c++) {
      const x = c * bw + shift, y = r * bh;
      const tint = 18 - rng() * 36;                // per-brick variation via rng()
      ctx.fillStyle = `rgb(${168 + tint}, ${74 + tint * 0.6}, ${56 + tint * 0.4})`;
      ctx.fillRect(x + gap, y + gap, bw - gap * 2, bh - gap * 2);
    }
  }
});
select('Wall');
layer('texture', { image: bricks.id, projection: 'triplanar', alpha: 0.85,
  texture: { repeat: [2, 2] } });
```

The draw callback is replicated at the 8 neighboring tile offsets with an
IDENTICALLY seeded `rng`, so anything crossing an edge wraps to the opposite
side — that machinery makes three rules load-bearing:
- randomness ONLY via the provided `rng()` — `rand()`/`Math.random` would
  give each replication pass a different pattern and tear every seam;
- transforms only with `translate`/`rotate`/`scale` inside `save`/`restore`
  — `setTransform`/`resetTransform` would wipe the replication offset;
- an OPAQUE full-tile base fill first — uncovered pixels are transparent and
  sample BLACK in the material.
Also: draw in TILE-relative units (fractions of `size`), keep features
smaller than the tile, and let `texture: { repeat }` set the real-world
scale. Redrawing under the SAME name replaces that asset's pixels in place
(every surface using it updates — iterate freely without littering assets),
and the same name keeps the same rng layout. `size` defaults to 512; use
1024 for hero close-ups or when one tile must span a large surface (see
REPEAT IS ALSO RESOLUTION below).

Pattern vocabulary that reads instantly: running-bond offset rows (bricks),
grout-gap grids (bathroom/kitchen tiles, checker floors via alternating
fills), long vertical boards + a few darker knots/streaks per board (planks;
rotate the repeat or the layer for horizontal), staggered scallops (roof
shingles), irregular rounded polygons on a dark base (flagstone), thin
double pinstripes (fabric). Two or three `rng`-jittered tones per feature
beat flat fills every time.
