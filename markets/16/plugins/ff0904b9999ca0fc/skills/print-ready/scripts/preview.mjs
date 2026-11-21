#!/usr/bin/env node
// Draw a repaired model from four sides into one PNG, so the model can be checked without
// any 3D software: front, side, back and three-quarter, in clay grey under a studio light on polymend.xyz's dark stage.
//
//   node preview.mjs <model-mended.stl> [--refs <front.png> [<side.png> [<back.png>]]] [--spots <spots.json>] [--out <file.png>] [--size <px>]
//
// It reads the binary STL Polymend writes (Z up, standing on the bed), draws each view with
// a depth buffer and simple lighting, and writes <name>-views.png beside the STL by default.
// With reference pictures (PNG, or JPEG on a Mac), they fill a top row above the matching views (front, side,
// back), so the model can be compared with what it was made from at a glance.
// No dependencies; nothing leaves the computer.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import os from 'node:os';
import { execFileSync } from 'node:child_process';

/** Triangles of a binary STL as a Float32Array of nine numbers each. */
export function readSTL(file) {
  const bytes = fs.readFileSync(file);
  const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  const count = view.getUint32(80, true);
  if (84 + count * 50 !== bytes.length) throw new Error('Not a binary STL.');
  const out = new Float32Array(count * 9);
  for (let t = 0; t < count; t++) for (let k = 0; k < 9; k++) out[t * 9 + k] = view.getFloat32(84 + t * 50 + 12 + k * 4, true);
  return out;
}

/** One view: the model turned by `angle` about Z, seen from the front, as grey levels. */
function drawView(tris, angle, size, bounds, studio = null) {
  const [cx, cy] = [(bounds.lo[0] + bounds.hi[0]) / 2, (bounds.lo[1] + bounds.hi[1]) / 2];
  const cos = Math.cos(angle), sin = Math.sin(angle);
  const radius = Math.hypot(bounds.hi[0] - bounds.lo[0], bounds.hi[1] - bounds.lo[1]) / 2;
  const height = bounds.hi[2] - bounds.lo[2];
  const span = Math.max(radius * 2, height) * 1.08;
  const scale = size / span;
  const zMid = (bounds.lo[2] + bounds.hi[2]) / 2;
  const depth = new Float32Array(size * size).fill(-Infinity);
  const shade = new Uint8Array(size * size).fill(0); // 0 = background
  const light = [-0.45, -0.75, 0.5];
  const norm = Math.hypot(...light);
  const L = light.map(v => v / norm);
  const p = new Float32Array(9);
  for (let t = 0; t < tris.length; t += 9) {
    for (let k = 0; k < 3; k++) {
      const x = tris[t + k * 3] - cx, y = tris[t + k * 3 + 1] - cy, z = tris[t + k * 3 + 2];
      const rx = x * cos - y * sin, ry = x * sin + y * cos; // turned about Z
      p[k * 3] = size / 2 + rx * scale;                    // screen x
      p[k * 3 + 1] = size / 2 - (z - zMid) * scale;        // screen y
      p[k * 3 + 2] = -ry;                                   // nearer the viewer is larger
    }
    // Face normal in view space, for lighting; faces seen from behind are still drawn.
    const ux = p[3] - p[0], uy = p[4] - p[1], uz = p[5] - p[2], vx = p[6] - p[0], vy = p[7] - p[1], vz = p[8] - p[2];
    let nx = uy * vz - uz * vy, ny = uz * vx - ux * vz, nz = ux * vy - uy * vx;
    const len = Math.hypot(nx, ny, nz) || 1;
    nx /= len; ny /= len; nz /= len;
    let level;
    if (studio) {
      // A light from the upper left, raking across the surface. Seen surfaces face the viewer,
      // so the normal is turned toward the viewer whatever the triangle's winding.
      const toward = nz >= 0 ? 1 : -1;
      const [lx, ly, lz] = studio.light;
      const lit = Math.max(0, toward * (nx * lx + -ny * ly + nz * lz));
      level = Math.max(1, Math.min(255, Math.round(255 * (studio.ambient + (1 - studio.ambient) * lit))));
    } else {
      const lit = Math.abs(nx * L[0] + -ny * L[2] + nz * -L[1]);
      level = Math.max(1, Math.min(255, Math.round(70 + 165 * lit)));
    }
    const minX = Math.max(0, Math.floor(Math.min(p[0], p[3], p[6]))), maxX = Math.min(size - 1, Math.ceil(Math.max(p[0], p[3], p[6])));
    const minY = Math.max(0, Math.floor(Math.min(p[1], p[4], p[7]))), maxY = Math.min(size - 1, Math.ceil(Math.max(p[1], p[4], p[7])));
    const area = (p[3] - p[0]) * (p[7] - p[1]) - (p[6] - p[0]) * (p[4] - p[1]);
    if (!area) continue;
    for (let y = minY; y <= maxY; y++) for (let x = minX; x <= maxX; x++) {
      const px = x + 0.5, py = y + 0.5;
      const w0 = ((p[3] - px) * (p[7] - py) - (p[6] - px) * (p[4] - py)) / area;
      const w1 = ((p[6] - px) * (p[1] - py) - (p[0] - px) * (p[7] - py)) / area;
      const w2 = 1 - w0 - w1;
      if (w0 < 0 || w1 < 0 || w2 < 0) continue;
      const d = w0 * p[2] + w1 * p[5] + w2 * p[8];
      const i = y * size + x;
      if (d > depth[i]) { depth[i] = d; shade[i] = level; }
    }
  }
  const project = (x0, y0, z0) => {
    const x = x0 - cx, y = y0 - cy;
    return [size / 2 + (x * cos - y * sin) * scale, size / 2 - (z0 - zMid) * scale, -(x * sin + y * cos)];
  };
  return { shade, depth, project };
}

/** Read an 8-bit, non-interlaced PNG (grey, grey+alpha, RGB, RGBA or palette) as RGB on white. */
export function readPNG(file) {
  const bytes = fs.readFileSync(file);
  if (bytes.readUInt32BE(0) !== 0x89504e47) throw new Error('Not a PNG.');
  let at = 8, width = 0, height = 0, depth = 0, type = 0, interlace = 0, palette = null, alpha = null;
  const data = [];
  while (at < bytes.length) {
    const length = bytes.readUInt32BE(at), kind = bytes.toString('latin1', at + 4, at + 8), body = bytes.subarray(at + 8, at + 8 + length);
    if (kind === 'IHDR') { width = body.readUInt32BE(0); height = body.readUInt32BE(4); depth = body[8]; type = body[9]; interlace = body[12]; }
    else if (kind === 'PLTE') palette = body;
    else if (kind === 'tRNS') alpha = body;
    else if (kind === 'IDAT') data.push(body);
    else if (kind === 'IEND') break;
    at += 12 + length;
  }
  if (depth !== 8 || interlace) throw new Error('Only 8-bit, non-interlaced PNG pictures are read.');
  if (width * height > 40_000_000) throw new Error('The picture is too large.');
  const channels = { 0: 1, 2: 3, 3: 1, 4: 2, 6: 4 }[type];
  if (!channels) throw new Error('Unsupported PNG colour type.');
  const raw = zlib.inflateSync(Buffer.concat(data));
  const stride = width * channels, pixels = Buffer.alloc(stride * height);
  for (let y = 0; y < height; y++) {
    const filter = raw[y * (stride + 1)], line = raw.subarray(y * (stride + 1) + 1, (y + 1) * (stride + 1));
    for (let x = 0; x < stride; x++) {
      const a = x >= channels ? pixels[y * stride + x - channels] : 0, b = y ? pixels[(y - 1) * stride + x] : 0, c = x >= channels && y ? pixels[(y - 1) * stride + x - channels] : 0;
      const pa = Math.abs(b - c), pb = Math.abs(a - c), pc = Math.abs(a + b - 2 * c);
      const predict = filter === 1 ? a : filter === 2 ? b : filter === 3 ? (a + b) >> 1 : filter === 4 ? (pa <= pb && pa <= pc ? a : pb <= pc ? b : c) : 0;
      pixels[y * stride + x] = (line[x] + predict) & 0xff;
    }
  }
  const rgb = Buffer.alloc(width * height * 3);
  for (let i = 0; i < width * height; i++) {
    let r, g, bl, al = 255;
    const o = i * channels;
    if (type === 3) { const k = pixels[o]; r = palette[k * 3]; g = palette[k * 3 + 1]; bl = palette[k * 3 + 2]; if (alpha && k < alpha.length) al = alpha[k]; }
    else if (type === 0 || type === 4) { r = g = bl = pixels[o]; if (type === 4) al = pixels[o + 1]; }
    else { r = pixels[o]; g = pixels[o + 1]; bl = pixels[o + 2]; if (type === 6) al = pixels[o + 3]; }
    const blend = v => Math.round((v * al + 255 * (255 - al)) / 255);
    rgb[i * 3] = blend(r); rgb[i * 3 + 1] = blend(g); rgb[i * 3 + 2] = blend(bl);
  }
  return { width, height, rgb };
}

/**
 * Read a reference picture. PNG is read directly; another format (such as a JPEG photo) is
 * converted with the system's own tool where there is one (sips on a Mac), or refused.
 */
export function readPicture(file) {
  const head = fs.readFileSync(file).subarray(0, 8);
  if (head.readUInt32BE(0) === 0x89504e47) return readPNG(file);
  if (process.platform === 'darwin') {
    const temp = path.join(os.tmpdir(), `polymend-ref-${process.pid}-${Date.now()}.png`);
    try {
      execFileSync('/usr/bin/sips', ['-s', 'format', 'png', file, '--out', temp], { stdio: 'ignore', timeout: 30_000 });
      return readPNG(temp);
    } finally { fs.rmSync(temp, { force: true }); }
  }
  throw new Error('Only PNG pictures can be read here; save the reference as PNG.');
}

/** Fit a picture into a size × size square (contain, centred) on the ground colour. */
export function fitInto(picture, size, ground, top = 0) {
  const out = Buffer.alloc(size * size * 3);
  for (let i = 0; i < size * size; i++) { out[i * 3] = ground[0]; out[i * 3 + 1] = ground[1]; out[i * 3 + 2] = ground[2]; }
  const room = size - top, scale = Math.min(size / picture.width, room / picture.height);
  const w = Math.round(picture.width * scale), h = Math.round(picture.height * scale), ox = (size - w) >> 1, oy = top + ((room - h) >> 1);
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const sx = Math.min(picture.width - 1, Math.floor(x / scale)), sy = Math.min(picture.height - 1, Math.floor(y / scale));
    picture.rgb.copy(out, ((oy + y) * size + ox + x) * 3, (sy * picture.width + sx) * 3, (sy * picture.width + sx) * 3 + 3);
  }
  return out;
}

// A small pixel font (5 x 7) for labels: capitals, digits and a few marks.
const GLYPHS = {
  '.': '00000000000000000000000000110001100',
  A: '01110100011000111111100011000110001', B: '11110100011000111110100011000111110', C: '01110100011000010000100001000101110',
  D: '11110100011000110001100011000111110', E: '11111100001000011110100001000011111', F: '11111100001000011110100001000010000',
  G: '01110100011000010111100011000101111', H: '10001100011000111111100011000110001', I: '01110001000010000100001000010001110',
  K: '10001100101010011000101001001010001', L: '10000100001000010000100001000011111', M: '10001110111010110101100011000110001',
  N: '10001110011010110011100011000110001', O: '01110100011000110001100011000101110', P: '11110100011000111110100001000010000',
  R: '11110100011000111110101001001010001', S: '01111100001000001110000010000111110', T: '11111001000010000100001000010000100',
  U: '10001100011000110001100011000101110', V: '10001100011000110001100010101000100', Y: '10001100010101000100001000010000100',
  W: '10001100011000110101101011101110001', X: '10001100010101000100010101000110001', J: '00111000100001000010000101001001100',
  Q: '01110100011000110001101011001001101', Z: '11111000010001000100010001000011111',
  0: '01110100011001110101110011000101110', 1: '00100011000010000100001000010001110', 2: '01110100010000100010001000100011111',
  3: '11110000010000101110000010000111110', 4: '00010001100101010010111110001000010', 5: '11111100001111000001000011000101110',
  6: '00110010001000011110100011000101110', 7: '11111000010001000100010000100001000', 8: '01110100011000101110100011000101110',
  9: '01110100011000101111000010001001100', '/': '00001000010001000100010001000010000', '(': '00010001000100001000010000010000010',
  ')': '01000001000001000010000100010001000', '-': '00000000000000011111000000000000000', '·': '00000000000010001110001000000000000',
};
function text(rgb, width, x0, y0, words, scale, colour) {
  let x = x0;
  for (const ch of words.toUpperCase()) {
    const glyph = GLYPHS[ch];
    if (glyph) for (let gy = 0; gy < 7; gy++) for (let gx = 0; gx < 5; gx++) if (glyph[gy * 5 + gx] === '1') {
      for (let dy = 0; dy < scale; dy++) for (let dx = 0; dx < scale; dx++) {
        const px = x + gx * scale + dx, o = ((y0 + gy * scale + dy) * width + px) * 3;
        if (px >= 0 && px < width && o >= 0 && o < rgb.length - 2) { rgb[o] = colour[0]; rgb[o + 1] = colour[1]; rgb[o + 2] = colour[2]; }
      }
    }
    x += 6 * scale;
  }
  return x;
}
function dot(rgb, width, height, cx, cy, radius, colour, strength) {
  for (let y = Math.floor(cy - radius - 1); y <= cy + radius + 1; y++) for (let x = Math.floor(cx - radius - 1); x <= cx + radius + 1; x++) {
    if (x < 0 || y < 0 || x >= width || y >= height) continue;
    const d = Math.hypot(x + 0.5 - cx, y + 0.5 - cy);
    const edge = d > radius ? 0 : d > radius - 1.6 ? 1 : 0.85; // a darker rim reads on light and dark clay
    if (!edge && d > radius) continue;
    const o = (y * width + x) * 3, c = edge === 1 ? colour.map(v => v * 0.6) : colour;
    for (let k = 0; k < 3; k++) rgb[o + k] = Math.round(rgb[o + k] * (1 - strength) + c[k] * strength);
  }
}

/** A minimal PNG writer for an RGB image. */
function png(width, height, rgb) {
  const raw = Buffer.alloc((width * 3 + 1) * height);
  for (let y = 0; y < height; y++) rgb.copy(raw, y * (width * 3 + 1) + 1, y * width * 3, (y + 1) * width * 3);
  const table = new Int32Array(256).map((_, n) => { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1; return c; });
  const crc = bytes => { let c = -1; for (const b of bytes) c = table[(c ^ b) & 0xff] ^ (c >>> 8); return (c ^ -1) >>> 0; };
  const chunk = (type, data) => {
    const head = Buffer.alloc(8); head.writeUInt32BE(data.length, 0); head.write(type, 4, 'latin1');
    const tail = Buffer.alloc(4); tail.writeUInt32BE(crc(Buffer.concat([head.subarray(4), data])), 0);
    return Buffer.concat([head, data, tail]);
  };
  const ihdr = Buffer.alloc(13); ihdr.writeUInt32BE(width, 0); ihdr.writeUInt32BE(height, 4); ihdr[8] = 8; ihdr[9] = 2;
  return Buffer.concat([Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]), chunk('IHDR', ihdr), chunk('IDAT', zlib.deflateSync(raw, { level: 6 })), chunk('IEND', Buffer.alloc(0))]);
}

// polymend.xyz's dark-theme stage and text, and the clay of its 3D view: the model stands out.
const OUTLINE = [124, 196, 248];
const STAGE = [15, 29, 46], CLAY = [194, 189, 179], INK = [230, 229, 222], MUTED = [120, 136, 156], EMPTY = [24, 40, 60];

function boundsOf(tris) {
  const lo = [Infinity, Infinity, Infinity], hi = [-Infinity, -Infinity, -Infinity];
  for (let i = 0; i < tris.length; i++) { const c = i % 3; if (tris[i] < lo[c]) lo[c] = tris[i]; if (tris[i] > hi[c]) hi[c] = tris[i]; }
  return { lo, hi };
}

/**
 * One view under a studio light from the upper left, with creases and the edges of nearer
 * parts darkened, drawn at twice the size and averaged down for smooth edges. Returns the
 * size × size tile, and project/depthAt in the tile's own pixels for placing marks.
 */
function studioView(tris, angle, size, bounds, look = {}) {
  const { light = [-0.6, 0.6, 0.5], ambient = 0.25, gain = 1.3, occlusion = 0.8, outline = 0.35 } = look;
  const { lo, hi } = bounds, big = size * 2;
  const n = Math.hypot(...light);
  const { shade, depth, project } = drawView(tris, angle, big, bounds, { light: light.map(c => c / n), ambient });
  // A pixel is dimmed by how much of the surface around it sits nearer the viewer.
  const dim = new Float32Array(big * big).fill(1);
  if (occlusion || outline) {
    const span = Math.max(hi[0] - lo[0], hi[1] - lo[1], hi[2] - lo[2]);
    const toPx = big / (Math.max(Math.hypot(hi[0] - lo[0], hi[1] - lo[1]), hi[2] - lo[2]) * 1.08);
    const reach = span * 0.02 * toPx, ring = [0.35, 0.7, 1].map(f => Math.max(2, Math.round(reach * f)));
    const dirs = [...Array(12).keys()].map(k => [Math.cos(k * Math.PI / 6), Math.sin(k * Math.PI / 6)]);
    for (let y = 0; y < big; y++) for (let x = 0; x < big; x++) {
      const i = y * big + x; if (!shade[i]) continue;
      const d = depth[i];
      let hidden = 0, count = 0, edge = 0;
      for (const r of ring) for (const [dx, dy] of dirs) {
        const sx = Math.round(x + dx * r), sy = Math.round(y + dy * r);
        if (sx < 0 || sy < 0 || sx >= big || sy >= big) continue;
        const e = depth[sy * big + sx]; count++;
        if (e > d) hidden += Math.min(1, (e - d) / (r / toPx * 1.5));
      }
      for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
        const sx = x + dx * 2, sy = y + dy * 2;
        const e = sx < 0 || sy < 0 || sx >= big || sy >= big ? -Infinity : depth[sy * big + sx];
        if (e - d > span * 0.01) edge = 1;
      }
      dim[i] = (1 - occlusion * (count ? hidden / count : 0)) * (1 - outline * edge);
    }
  }
  const tile = Buffer.alloc(size * size * 3);
  for (let y = 0; y < size; y++) for (let x = 0; x < size; x++) {
    const sum = [0, 0, 0];
    for (const [dx, dy] of [[0, 0], [1, 0], [0, 1], [1, 1]]) {
      const at = (y * 2 + dy) * big + x * 2 + dx, s = shade[at];
      for (let c = 0; c < 3; c++) sum[c] += s ? Math.min(255, CLAY[c] * gain * s / 255 * dim[at]) : STAGE[c];
    }
    for (let c = 0; c < 3; c++) tile[(y * size + x) * 3 + c] = Math.min(255, Math.round(sum[c] / 4));
  }
  return {
    tile,
    project: (x, y, z) => { const [a, b, d] = project(x, y, z); return [a / 2, b / 2, d]; },
    depthAt: (px, py) => depth[Math.min(big - 1, py * 2) * big + Math.min(big - 1, px * 2)],
  };
}

/** The backdrop of a picture: the commonest colour along its edge, to within a small step. */
function backdropOf(picture, size) {
  const counts = new Map();
  for (let k = 0; k < size; k++) for (const [x, y] of [[k, 0], [k, size - 1], [0, k], [size - 1, k]]) {
    const o = (y * size + x) * 3, key = (picture[o] >> 4) * 256 + (picture[o + 1] >> 4) * 16 + (picture[o + 2] >> 4);
    counts.set(key, (counts.get(key) || 0) + 1);
  }
  const key = [...counts].sort((a, b) => b[1] - a[1])[0][0];
  return [(key >> 8) * 16 + 8, ((key >> 4) & 15) * 16 + 8, (key & 15) * 16 + 8];
}

/** The subject of a picture as a mask: everything clearly unlike the backdrop. */
export function maskOf(picture, size) {
  const back = backdropOf(picture, size);
  const like = new Uint8Array(size * size).map((_, i) => Math.abs(picture[i * 3] - back[0]) + Math.abs(picture[i * 3 + 1] - back[1]) + Math.abs(picture[i * 3 + 2] - back[2]) > 60 ? 0 : 1);
  // A floor shadow is the backdrop, only darker: the same balance of red, green and blue.
  // Only in the lowest fifth of the subject, so a grey subject's body is never taken for one.
  let top = size, bottom = -1;
  for (let i = 0; i < size * size; i++) if (!like[i]) { const y = Math.floor(i / size); if (y < top) top = y; if (y > bottom) bottom = y; }
  for (let y = Math.max(0, Math.floor(bottom - (bottom - top) * 0.2)); y <= bottom; y++) for (let x = 0; x < size; x++) {
    const i = y * size + x; if (like[i]) continue;
    const f = [0, 1, 2].map(c => picture[i * 3 + c] / Math.max(1, back[c]));
    if (f[0] < 0.97 && f[0] > 0.4 && Math.max(...f) - Math.min(...f) < 0.06) like[i] = 1;
  }
  // Backdrop is what is backdrop-coloured and joined to the edge; a highlight inside the
  // subject is backdrop-coloured too, but enclosed, so it stays part of the subject.
  const outside = new Uint8Array(size * size), stack = [];
  for (let k = 0; k < size; k++) for (const i of [k, (size - 1) * size + k, k * size, k * size + size - 1]) if (like[i] && !outside[i]) { outside[i] = 1; stack.push(i); }
  while (stack.length) {
    const i = stack.pop(), x = i % size;
    for (const j of [x > 0 ? i - 1 : -1, x < size - 1 ? i + 1 : -1, i - size, i + size]) if (j >= 0 && j < size * size && like[j] && !outside[j]) { outside[j] = 1; stack.push(j); }
  }
  return outside.map(v => v ? 0 : 1);
}

/**
 * How deep an outline is for its height: across the whole outline and across its top fifth,
 * ignoring the lowest 4 percent (where photos carry the floor and its shadow).
 */
function proportions(mask, size) {
  const rows = [];
  for (let y = 0; y < size; y++) {
    let a = -1, b = -1;
    for (let x = 0; x < size; x++) if (mask[y * size + x]) { if (a < 0) a = x; b = x; }
    if (a >= 0) rows.push({ y, a, b });
  }
  if (rows.length < 20) return null;
  const top = rows[0].y, bottom = rows[rows.length - 1].y, height = bottom - top + 1;
  const extent = list => { const used = list.filter(r => r.y <= bottom - height * 0.04); return used.length ? Math.max(...used.map(r => r.b)) - Math.min(...used.map(r => r.a)) + 1 : 0; };
  return { whole: extent(rows) / height, top: extent(rows.filter(r => r.y < top + height * 0.2)) / height };
}

/**
 * Compare the model's depth with the side reference's, both as depth for the height, so the
 * size of the picture and of the print do not matter. Positive: the model is deeper.
 */
function depthAgainst(sidePicture, sideShade, size, refMask = maskOf(sidePicture, size)) {
  const modelMask = sideShade.map(v => v ? 1 : 0);
  const ref = proportions(refMask, size), model = proportions(modelMask, size);
  if (!ref || !model || !ref.whole || !ref.top) return null;
  const pct = (m, r) => Math.round((m / r - 1) * 100);
  // The reference's outline, scaled to the model's height and centred on the top of each
  // (usually the head), so the two can be laid over each other.
  const frame = mask => {
    let top = -1, bottom = -1;
    for (let y = 0; y < size; y++) for (let x = 0; x < size; x++) if (mask[y * size + x]) { if (top < 0) top = y; bottom = y; break; }
    let sum = 0, n = 0;
    for (let y = top; y < top + (bottom - top) * 0.2; y++) for (let x = 0; x < size; x++) if (mask[y * size + x]) { sum += x; n++; }
    return { top, height: bottom - top + 1, centre: n ? sum / n : size / 2 };
  };
  const r = frame(refMask), m = frame(modelMask), k = m.height / r.height;
  const outline = [];
  for (let y = 1; y < Math.min(size - 1, r.top + r.height * 0.96); y++) for (let x = 1; x < size - 1; x++) {
    const i = y * size + x;
    if (refMask[i] && (!refMask[i - 1] || !refMask[i + 1] || !refMask[i - size] || !refMask[i + size])) outline.push([(x - r.centre) * k + m.centre, (y - r.top) * k + m.top]);
  }
  // How well the lined-up outlines agree (shared over combined area).
  let both = 0, either = 0;
  for (let y = 0; y < size; y++) for (let x = 0; x < size; x++) {
    const rx = Math.round((x - m.centre) / k + r.centre), ry = Math.round((y - m.top) / k + r.top);
    const a = modelMask[y * size + x], b = rx >= 0 && ry >= 0 && rx < size && ry < size ? refMask[ry * size + rx] : 0;
    both += a & b; either += a | b;
  }
  // Which way the outline faces, from its feet: toes reach further forward than heels.
  const toes = (mask, f) => {
    let reach = 0;
    for (let y = Math.round(f.top + f.height * 0.86); y < f.top + f.height * 0.96; y++) for (let x = 0; x < size; x++) if (mask[y * size + x]) reach += Math.sign(x - f.centre);
    return reach;
  };
  const facing = [toes(refMask, r), toes(modelMask, m)];
  return { whole: pct(model.whole, ref.whole), top: pct(model.top, ref.top), outline, agreement: either ? both / either : 0, facing };
}

/**
 * Write a sheet of the model's front, side, back and three-quarter views (2 × 2), each
 * labelled. With reference pictures it is 4 × 2: the references (front, side, back) on top,
 * each above the matching view. With `spots` (from review.mjs), places Polymend fixed are
 * marked green and places where a fault is left orange: solid when on the side facing the
 * viewer, faint when behind. A footer gives the key and the counts.
 * Returns { file, skipped } with any references that could not be read.
 */
export function writePreview(stlFile, outFile, size = 480, refs = [], spots = null) {
  const tris = readSTL(stlFile);
  const lo = [Infinity, Infinity, Infinity], hi = [-Infinity, -Infinity, -Infinity];
  for (let i = 0; i < tris.length; i++) { const c = i % 3; if (tris[i] < lo[c]) lo[c] = tris[i]; if (tris[i] > hi[c]) hi[c] = tris[i]; }
  const names = ['FRONT', 'SIDE', 'BACK', '3/4'];
  const skipped = [];
  const label = Math.max(2, Math.round(size / 160)), band = 7 * label + 20;
  const read = refs.slice(0, 3).map(ref => { try { return readPicture(ref); } catch (error) { skipped.push(`${path.basename(ref)}: ${error.message}`); return null; } });
  // For matching the side view, each picture fills the square; for showing, it sits whole
  // below its label, never drawn over: the references are shown exactly as given.
  const pictures = read.map(picture => picture && fitInto(picture, size, [255, 255, 255]));
  const shown = read.map(picture => picture && fitInto(picture, size, STAGE, band));
  // A side reference may show either side. Draw the model's side both ways, line each up
  // with the reference's outline, and keep the way they agree on more.
  let sideAngle = Math.PI / 2, depth = null;
  if (pictures[1]) {
    const refMask = maskOf(pictures[1], size);
    const tries = [Math.PI / 2, -Math.PI / 2].map(angle => ({ angle, found: depthAgainst(pictures[1], drawView(tris, angle, size, { lo, hi }).shade, size, refMask) }));
    // Feet decide when both outlines clearly have them; otherwise, the closer overlap.
    const clear = t => t.found && Math.abs(t.found.facing[0]) > size && Math.abs(t.found.facing[1]) > size;
    const byFeet = tries.filter(clear).filter(t => Math.sign(t.found.facing[0]) === Math.sign(t.found.facing[1]));
    const best = (byFeet.length === 1 ? byFeet : tries.filter(t => t.found).sort((a, b) => b.found.agreement - a.found.agreement))[0];
    if (best) { sideAngle = best.angle; depth = best.found; }
  }
  const views = [0, sideAngle, Math.PI, Math.PI / 4].map(angle => studioView(tris, angle, size, { lo, hi }));
  const KINDS = { removed: [240, 6, 131], patched: [18, 189, 61], turned: [0, 139, 234], left: [230, 126, 34] };
  const colourOf = spot => KINDS[spot.kind] || KINDS.left;
  const withRefs = pictures.some(Boolean);
  const columns = withRefs ? 4 : 2, rows = 2;
  const footer = spots ? Math.round(size * 0.12) : 0;
  const width = size * columns, height = size * rows + footer;
  const rgb = Buffer.alloc(width * height * 3);
  for (let i = 0; i < width * height; i++) rgb.set(STAGE, i * 3);
  const viewAt = v => withRefs ? [v * size, size] : [(v % 2) * size, Math.floor(v / 2) * size];
  // References on top, labelled.
  if (withRefs) [0, 1, 2, 3].map(i => shown[i]).forEach((tile, i) => {
    if (!tile) {
      for (let y = 0; y < size; y++) for (let x = 0; x < size; x++) { const o = (y * width + i * size + x) * 3; rgb.set(EMPTY, o); }
      if (i < 3) text(rgb, width, i * size + 10, 10, `NO ${names[i]} REFERENCE`, label, MUTED);
      return;
    }
    for (let y = 0; y < size; y++) tile.copy(rgb, (y * width + i * size) * 3, y * size * 3, (y + 1) * size * 3);
    text(rgb, width, i * size + 10, 10, `REFERENCE ${names[i]}`, label, INK);
  });
  views.forEach(({ tile, depthAt, project }, v) => {
    const [ox, oy] = viewAt(v);
    for (let y = 0; y < size; y++) tile.copy(rgb, ((oy + y) * width + ox) * 3, y * size * 3, (y + 1) * size * 3);
    if (v === 1 && depth) {
      for (const [x, y] of depth.outline) dot(rgb, width, height, ox + x, oy + y, Math.max(1, size / 400), OUTLINE, 0.9);
      text(rgb, width, ox + 10, oy + 20 + 7 * label, 'OUTLINE OF SIDE REFERENCE', Math.max(1, label - 1), OUTLINE);
    }
    if (spots) {
      const radius = Math.max(4, size / 70);
      for (const [spot, colour] of [...spots.fixed.map(spot => [spot, colourOf(spot)]), ...spots.left.map(spot => [spot, KINDS.left])]) {
        const [sx, sy, sd] = project(spot.x, spot.y, spot.z);
        const px = Math.round(sx), py = Math.round(sy);
        if (px < 0 || py < 0 || px >= size || py >= size) continue;
        // Facing the viewer when nothing drawn there is clearly nearer than the spot.
        const near = !(depthAt(px, py) > sd + size * 0.002 / (size / 480));
        dot(rgb, width, height, ox + sx, oy + sy, radius, colour, near ? 1 : 0.35);
      }
    }
    text(rgb, width, ox + 10, oy + 10, names[v], label, INK);
  });
  if (spots) {
    // The key, in the website's words: what Polymend removed, added and turned, and what is left.
    const count = kind => spots.fixed.filter(s => s.kind === kind).length;
    const keys = [['REMOVED', KINDS.removed, count('removed')], ['ADDED', KINDS.patched, count('patched')], ['TURNED TO FACE OUT', KINDS.turned, count('turned')], ['STILL A FAULT', KINDS.left, spots.left.length]];
    // One line across the sheet: the letters shrink until the whole key fits.
    let r = Math.max(5, footer / 6), scale = label;
    const across = () => 20 + keys.reduce((sum, [word, , n]) => sum + r * 2 + 8 + `${word} ${n}`.length * 6 * scale + 22, 0);
    while (across() > width && scale > 1) scale--;
    while (across() > width && r > 3) r--;
    const y = size * rows + Math.round((footer - 7 * scale) / 2);
    let x = 20;
    for (const [word, colour, n] of keys) {
      dot(rgb, width, height, x + r, y + 3.5 * scale, r, colour, 1);
      x = text(rgb, width, x + r * 2 + 8, y, `${word} ${n}`, scale, INK) + 22;
    }
  }
  fs.writeFileSync(outFile, png(width, height, rgb));
  return { file: outFile, skipped, depth };
}

/**
 * Write a clean picture of the repaired model from the front, filling the frame, with no
 * marks: where it ended up, large enough to judge closely. The other angles are in the views
 * and the comparison. An optional caption (such as the print size) runs along the bottom.
 */
export function writeResult(stlFile, outFile, size = 1200, caption = '', look = {}) {
  const tris = readSTL(stlFile);
  const label = Math.max(2, Math.round(size / 240));
  const footer = caption ? Math.round(size * 0.05) : 0;
  const width = size, height = size + footer;
  const rgb = Buffer.alloc(width * height * 3);
  for (let i = 0; i < width * height; i++) rgb.set(STAGE, i * 3);
  studioView(tris, 0, size, boundsOf(tris), look).tile.copy(rgb, 0);
  if (caption) text(rgb, width, 20, size + Math.round((footer - 7 * label) / 2), caption, label, INK);
  fs.writeFileSync(outFile, png(width, height, rgb));
  return outFile;
}

if (process.argv[1] && path.resolve(process.argv[1]) === path.resolve(new URL(import.meta.url).pathname)) {
  const args = process.argv.slice(2);
  const at = args.indexOf('--refs');
  const refs = at >= 0 ? args.slice(at + 1).filter((a, i, all) => !a.startsWith('--') && all.slice(0, i).every(b => !b.startsWith('--'))) : [];
  const valueOf = name => (args.includes(name) ? args[args.indexOf(name) + 1] : undefined);
  const file = args.find((a, i) => !a.startsWith('--') && !['--out', '--size', '--spots'].includes(args[i - 1]) && !refs.includes(a));
  if (!file) { console.log('Usage: node preview.mjs <model-mended.stl> [--refs <front.png> [<side.png> [<back.png>]]] [--out <file.png>] [--size <px>]'); process.exit(1); }
  const out = valueOf('--out') || file.replace(/-mended\.stl$/i, '').replace(/\.stl$/i, '') + (refs.length ? '-compare.png' : '-views.png');
  const size = Math.min(1024, Math.max(128, Number(valueOf('--size')) || 480));
  const spotsFile = valueOf('--spots');
  const result = writePreview(file, out, size, refs, spotsFile ? JSON.parse(fs.readFileSync(spotsFile, 'utf8')) : null);
  console.log(result.file);
  if (result.depth) {
    const say = (n, part) => `${part}: ${n === 0 ? 'the same depth as' : `about ${Math.abs(n)}% ${n > 0 ? 'deeper than' : 'shallower than'}`} the side reference, for its height`;
    console.log(`Depth (front to back), measured against the side reference. ${say(result.depth.whole, 'Whole model')}. ${say(result.depth.top, 'Top fifth')}.`);
  } else if (refs.length) console.log('Depth: not measured (no side reference).');
  for (const note of result.skipped) console.error(`Reference not used: ${note}`);
}
