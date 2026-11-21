#!/usr/bin/env node
// Repair one model and write everything for it, in one pass: the STL, the 3MF, a report,
// and the four views with Polymend's changes marked. prepare.mjs runs this once per model in
// its own process, under a memory cap and a time limit, so a bad file fails alone.
//
//   node mend-one.mjs <model.glb|model.stl> --out <dir> --name <name> (--height <mm> | --as-is) [--separate] [--wide] [--no-previews]
//
// Prints one line of JSON: the report.
import fs from 'node:fs';
import path from 'node:path';
import { loadAsync, mend } from './polymend/src/pipeline.js';
import { EdgeTable } from './polymend/src/mesh.js';
import { writeSTL } from './polymend/src/stl.js';
import { layout, write3MF, VERSION } from './polymend/src/output.js';
import { writePreview, writeResult } from './preview.mjs';
import { balance } from './balance.mjs';

const args = process.argv.slice(2);
const value = name => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : undefined; };
const input = args.find((a, i) => !a.startsWith('--') && !['--out', '--name', '--height'].includes(args[i - 1]));
const out = value('--out'), name = value('--name');
const height = Number(value('--height'));
if (!input || !out || !name) { console.error('Usage: node mend-one.mjs <model> --out <dir> --name <name> (--height <mm> | --as-is) [--separate] [--wide] [--no-previews]'); process.exit(1); }

let mesh, result;
try {
  mesh = await loadAsync(fs.readFileSync(input), input);
  result = mend(mesh, { separatePinches: args.includes('--separate'), patchWide: args.includes('--wide') });
} catch (error) {
  console.log(JSON.stringify({ status: 'failed', error: error.message }));
  process.exit(0);
}

const r = result.report;
const unit = mesh.unit === 'meter' ? 1000 : 1;
const sized = layout(result.positions, { heightMm: height > 0 ? height : undefined, unitMm: unit });
fs.mkdirSync(out, { recursive: true });
const stl = path.join(out, `${name}-mended.stl`), threeMF = path.join(out, `${name}-mended.3mf`);
fs.writeFileSync(stl, writeSTL(sized.positions, result.tris, 1, `polymend ${VERSION}`));
fs.writeFileSync(threeMF, await write3MF(sized.positions, result.tris, { title: name }));

const summary = {
  polymend: VERSION, input: path.resolve(input), status: r.status, notes: mesh.notes || [],
  before: r.before, after: r.after, sizeMm: sized.size.map(v => Math.round(v * 100) / 100),
  done: { strayTrianglesRemoved: r.strayFacesRemoved, separatePiecesRemoved: r.specksRemoved, collapsedOrDuplicateRemoved: r.degenerateRemoved + r.duplicateRemoved,
    holesPatched: r.holesFilled.length, holes: r.holes, patchesGrazing: r.patchesCrossing, seamPointsJoined: r.seamPointsJoined, trianglesTurned: r.facesFlipped, pinchedEdgesCut: r.pinchedEdgesCut },
  left: { holesLeftOpen: r.holesLeftOpen, sheetsLeft: r.sheetsLeft, flatPieces: r.flatPieces, pinchedEdgesLeft: r.pinchedEdgesLeft, selfCrossings: r.crossingsSkipped ? null : r.crossingsAfter, pointsTouching: r.pointsTouching },
  files: { stl, threeMF },
};

// Whether it stands: only meaningful at a real print size.
try {
  const b = balance(sized.positions, result.tris);
  if (b) summary.stands = { marginMm: Math.round(b.margin * 10) / 10, tipDegrees: Math.round(b.tipDegrees), towards: b.towards, ...(b.hanging ? { hangingMm: Math.round(b.hanging.height * 10) / 10 } : {}) };
} catch {}

if (!args.includes('--no-previews')) {
  try {
    const caption = `${summary.sizeMm.map(v => +v.toFixed(1)).join(' X ')} MM`;
    summary.result = writeResult(stl, path.join(out, `${name}-result.png`), 1200, caption);
  } catch (error) {
    summary.previewError = error.message;
  }
  try {
    // The places Polymend changed and the faults it left, placed exactly as the print files
    // are: the same scale and shift layout() applied, worked out from its own result.
    const lo = [Infinity, Infinity, Infinity], hi = [-Infinity, -Infinity, -Infinity];
    for (let i = 0; i < result.positions.length; i++) { const c = i % 3; if (result.positions[i] < lo[c]) lo[c] = result.positions[i]; if (result.positions[i] > hi[c]) hi[c] = result.positions[i]; }
    const shift = height > 0 ? [(lo[0] + hi[0]) / 2, (lo[1] + hi[1]) / 2, lo[2]] : [0, 0, 0];
    const place = (x, y, z) => [(x - shift[0]) * sized.scale, (y - shift[1]) * sized.scale, (z - shift[2]) * sized.scale];
    const size = Math.hypot(hi[0] - lo[0], hi[1] - lo[1], hi[2] - lo[2]) || 1;
    const group = (points, kind) => {
      const cell = size * 0.01, places = new Map();
      for (const [x, y, z] of points) {
        const key = `${Math.round(x / cell)},${Math.round(y / cell)},${Math.round(z / cell)}`;
        const p = places.get(key) || places.set(key, { sum: [0, 0, 0], n: 0 }).get(key);
        p.sum[0] += x; p.sum[1] += y; p.sum[2] += z; p.n++;
      }
      return [...places.values()].map(p => { const [x, y, z] = place(...p.sum.map(v => v / p.n)); return { kind, x, y, z }; });
    };
    const centre = (positions, tris, f) => [0, 1, 2].map(c => (positions[tris[f * 3] * 3 + c] + positions[tris[f * 3 + 1] * 3 + c] + positions[tris[f * 3 + 2] * 3 + c]) / 3);
    const removed = [], added = [], turned = [];
    for (let f = 0; f < mesh.tris.length / 3; f++) if (!result.kept[f]) removed.push(centre(mesh.positions, mesh.tris, f));
    for (let f = 0; f < result.tris.length / 3; f++) {
      if (result.origin[f] < 0) added.push(centre(result.positions, result.tris, f));
      else if (result.flipped?.[f] === 1) turned.push(centre(result.positions, result.tris, f));
    }
    const open = [], shared = [];
    const edges = new EdgeTable(result.tris);
    for (let i = 0; i < edges.size; i++) {
      const slot = edges.order[i], used = edges.count[slot];
      if (used === 2) continue;
      const a = edges.lo[slot] * 3, b = edges.hi[slot] * 3;
      (used === 1 ? open : shared).push([0, 1, 2].map(c => (result.positions[a + c] + result.positions[b + c]) / 2));
    }
    // A whole piece turned the right way round is not marked spot by spot; the report says so.
    const wholeTurned = turned.length > 2000;
    const spots = { fixed: [...group(removed, 'removed'), ...group(added, 'patched'), ...(wholeTurned ? [] : group(turned, 'turned'))], left: [...group(open, 'opening'), ...group(shared, 'surfaces meeting')] };
    summary.preview = writePreview(stl, path.join(out, `${name}-views.png`), 480, [], spots).file;
    summary.marked = { fixed: spots.fixed.length, left: spots.left.length, ...(wholeTurned ? { wholePiecesTurned: true } : {}) };
  } catch (error) {
    summary.previewError = error.message;
  }
}

fs.writeFileSync(path.join(out, `${name}-report.json`), JSON.stringify(summary, null, 2));
console.log(JSON.stringify(summary));
