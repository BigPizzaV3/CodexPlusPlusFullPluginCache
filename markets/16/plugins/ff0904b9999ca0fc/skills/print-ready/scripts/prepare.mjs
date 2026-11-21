#!/usr/bin/env node
// Make 3D models ready to print with Polymend: repair them, size them, write an STL and a 3MF
// of each, draw them from four sides with Polymend's changes marked, and write a review.
// Inputs can be .glb or .stl files, folders (the models directly inside), or https links such
// as the GLB links a 3D generation tool returns; up to 20 at once.
//
//   node prepare.mjs <file|folder|https link>... [--height <mm> | --as-is] [--out <dir>] [--separate] [--wide] [--no-previews] [--json]
//
// Each run writes into its own folder: --out, or ./polymend/<date>-<time>-<first model>.
// Links are downloaded into <out>/sources first. Each model is then handled by mend-one.mjs
// in a separate process with a memory cap and a time limit, so one bad file fails alone.
// Per model: <name>-mended.stl, <name>-mended.3mf, <name>-report.json, <name>-result.png, <name>-views.png.
// Per run: polymend-batch.json and polymend-review.md.
// The exit code is 0 whenever the run finished, whatever each model's outcome (that is in
// the results); 1 only when the command itself could not run (bad options, no inputs).
// Nothing is uploaded: the only network use is downloading the links given.
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { fetchModel, shortLink } from './fetch.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const MEND_ONE = path.join(here, 'mend-one.mjs');
const MAX_MODELS = 20;
const PER_MODEL_MS = 180_000;
const MEMORY_MB = 4096;
const MODEL = /\.(glb|stl)$/i;
const OWN_OUTPUT = /-mended\.stl$/i;

const args = process.argv.slice(2);
const flag = name => args.includes(name);
const value = name => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : undefined; };
const WITH_VALUE = ['--height', '--out', '--name'];
const KNOWN = [...WITH_VALUE, '--as-is', '--separate', '--wide', '--no-previews', '--json', '--help'];
const given = args.filter((arg, i) => !arg.startsWith('--') && !WITH_VALUE.includes(args[i - 1]));
const USAGE = 'Usage: node prepare.mjs <file|folder|https link>... [--height <mm> | --as-is] [--name <name>] [--out <dir>] [--separate] [--wide] [--no-previews] [--json]';
const stop = text => { console.error(text); process.exit(1); };
const clean = text => String(text).replace(/[\u0000-\u001f\u007f‪-‮⁦-⁩]/g, ' ');

if (!given.length || flag('--help')) { console.log(USAGE); process.exit(given.length ? 0 : 1); }
for (const arg of args.filter(arg => arg.startsWith('--'))) if (!KNOWN.includes(arg)) stop(`Unknown option ${arg}.\n${USAGE}`);
for (const name of WITH_VALUE) if (flag(name) && (!value(name) || value(name).startsWith('--'))) stop(`${name} needs a value.`);
const height = Number(value('--height'));
if (flag('--height') && !(height > 0 && height <= 2000 && Number.isFinite(height))) stop('--height must be a number of millimeters, above zero and at most 2000.');
// No height is a valid answer: the files keep their own size (a GLB's meters become millimeters).
if (flag('--height') && flag('--as-is')) stop('Give --height <mm> or --as-is, not both.');
const json = flag('--json');
const say = json ? () => {} : text => console.log(text);

// Safe in any folder on any system, and unique even where capitals are ignored.
const RESERVED = /^(con|prn|aux|nul|com[0-9]|lpt[0-9])$/i;
const safeStem = text => {
  let stem = String(text).replace(/[^A-Za-z0-9._()+ -]/g, '_').replace(/^[.]+/, '_').replace(/[. ]+$/, '').slice(0, 100) || 'model';
  if (RESERVED.test(stem)) stem = `_${stem}`;
  return stem;
};
const taken = new Set();
const unique = name => {
  const stem = safeStem(name.replace(MODEL, ''));
  let candidate = stem;
  for (let n = 2; taken.has(candidate.toLowerCase()); n++) candidate = `${stem}-${n}`;
  taken.add(candidate.toLowerCase());
  return candidate;
};

// Gather the inputs: links are downloaded, folders opened, model files taken as they are.
const isFile = file => { try { return fs.statSync(file).isFile(); } catch { return false; } };
const isLink = text => /^[a-z][a-z0-9+.-]*:\/\//i.test(text);
const items = [];
for (const input of given) {
  if (isLink(input)) { items.push({ input, shown: shortLink(input), link: input }); continue; }
  let stat;
  try { stat = fs.statSync(input); } catch { items.push({ input, shown: input, error: 'Not found.' }); continue; }
  if (stat.isDirectory()) {
    const found = fs.readdirSync(input).filter(name => MODEL.test(name) && !OWN_OUTPUT.test(name) && isFile(path.join(input, name))).sort();
    if (!found.length) items.push({ input, shown: input, error: 'No .glb or .stl files in this folder.' });
    for (const name of found) items.push({ input: path.join(input, name), shown: path.join(input, name), file: path.join(input, name) });
  } else if (!stat.isFile()) items.push({ input, shown: input, error: 'Not a file.' });
  else if (!MODEL.test(input)) items.push({ input, shown: input, error: 'Polymend takes .glb and .stl files.' });
  else items.push({ input, shown: input, file: input });
}
const models = items.filter(item => !item.error).length;
if (models > MAX_MODELS) stop(`Up to ${MAX_MODELS} models at a time; these are ${models}.`);
if (flag('--name') && models > 1) stop('--name names one model; run each model on its own to name it.');

// Each run gets its own folder, so nothing earlier is overwritten and nothing is mixed in.
const first = items.find(item => !item.error);
let firstName = 'run';
try { if (first) firstName = safeStem(value('--name') || path.basename(first.link ? new URL(first.link).pathname : first.file).replace(MODEL, '')); } catch {}
const stamp = new Date().toISOString().replace(/[-:]/g, '').replace('T', '-').slice(0, 15);
let out = path.resolve(value('--out') || path.join('polymend', `${stamp}-${firstName}`.slice(0, 80)));
if (!value('--out')) for (let n = 2, base = out; fs.existsSync(out); n++) out = `${base}-${n}`;
if (fs.existsSync(out) && !fs.statSync(out).isDirectory()) stop(`--out must be a folder: ${clean(out)}`);
fs.mkdirSync(out, { recursive: true });

const sources = path.join(out, 'sources');
for (const item of items.filter(item => item.link)) {
  say(`Downloading ${clean(item.shown)}`);
  try { item.file = await fetchModel(item.link, sources); }
  catch (error) { item.error = `Could not download it: ${clean(error.message)}`; }
}

/** Run one model in its own process, with a memory cap and a time limit. */
function mendOne(file, name) {
  return new Promise(resolve => {
    const child = spawn(process.execPath, [`--max-old-space-size=${MEMORY_MB}`, MEND_ONE, file, '--out', out, '--name', name,
      ...(height > 0 ? ['--height', String(height)] : ['--as-is']), ...(flag('--separate') ? ['--separate'] : []), ...(flag('--wide') ? ['--wide'] : []),
      ...(flag('--no-previews') ? ['--no-previews'] : [])], { stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = '', stderr = '', settled = false;
    const finish = result => { if (!settled) { settled = true; clearTimeout(timer); resolve(result); } };
    const timer = setTimeout(() => { child.kill('SIGKILL'); finish({ status: 'failed', error: `Stopped after ${PER_MODEL_MS / 1000} seconds.` }); }, PER_MODEL_MS);
    child.stdout.on('data', chunk => { stdout += chunk; });
    child.stderr.on('data', chunk => { stderr += chunk; });
    child.on('error', error => finish({ status: 'failed', error: `Could not start: ${error.message}` }));
    child.on('close', (code, signal) => {
      let result = null;
      try { result = JSON.parse(stdout.trim().split('\n').pop()); } catch {}
      if (result && typeof result.status === 'string') return finish(result);
      const memory = /heap out of memory|allocation failed|Abort/i.test(stderr) || signal;
      finish({ status: 'failed', error: memory ? 'Ran out of memory or was stopped: the model may be too large for this computer.' : clean(stderr.trim().split('\n').pop() || `Exited with code ${code}.`) });
    });
  });
}

const results = [];
const ready = items.filter(item => item.file && !item.error);
for (const item of items) {
  if (item.error) { results.push({ input: item.shown, status: 'failed', error: item.error }); continue; }
  const name = unique(value('--name') || path.basename(item.file));
  say(`[${ready.indexOf(item) + 1}/${ready.length}] Repairing ${clean(path.basename(item.file))}`);
  const result = await mendOne(item.file, name);
  results.push({ ...result, input: item.shown, ...(value('--name') ? { name: value('--name') } : {}), ...(item.link ? { downloaded: item.file } : {}) });
}

const TITLES = { repaired: 'Repaired', sound: 'Nothing to fix', partial: 'Partly repaired', failed: 'Not repaired' };

/**
 * Polymend's review of each model, in plain words. It covers what Polymend can measure;
 * how the model looks is judged from the views. It describes the model, not where it came from.
 */
function reviewText(results) {
  const n = (count, one, many = one + 's') => `${count.toLocaleString('en-US')} ${count === 1 ? one : many}`;
  const lines = ['# Polymend review', '', `Files are in ${out}`, '',
    'Each `-result.png` shows the repaired model from the front, large. In each `-views.png`: pink marks where Polymend removed triangles, green where it added patches, blue where it turned faces outward, orange where a fault is left. Faint marks are on the far side.', ''];
  for (const r of results) {
    lines.push(`## ${clean(r.name || path.basename(r.input))}: ${TITLES[r.status] || 'Not repaired'}`, '');
    if (r.status === 'failed' || !TITLES[r.status]) { lines.push(`- Not repaired: ${r.error}`, ''); continue; }
    const d = r.done || {}, left = r.left || {}, before = r.before || {}, after = r.after || {};
    const size = r.sizeMm || r.size_mm;
    // What the model arrived with, stated neutrally before the two columns.
    const arrived = [before.openEdges && n(before.openEdges, 'open edge'), before.nonManifoldEdges && n(before.nonManifoldEdges, 'non-manifold edge'), before.inconsistentEdges && n(before.inconsistentEdges, 'wrongly facing join')].filter(Boolean);
    lines.push(`**What Polymend found**: ${arrived.length ? `the model arrived with ${arrived.join(', ')}, the faults a slicer warns about.` : 'no open or non-manifold edges.'}`, '');
    const good = [], weak = [];
    const fixed = [d.strayTrianglesRemoved && `removed ${n(d.strayTrianglesRemoved, 'stray triangle')} stuck to the surface`, d.separatePiecesRemoved && `removed ${n(d.separatePiecesRemoved, 'tiny loose piece')}`,
      d.collapsedOrDuplicateRemoved && `removed ${n(d.collapsedOrDuplicateRemoved, 'collapsed or duplicate triangle')}`, d.holesPatched && `patched ${n(d.holesPatched, 'hole')}`,
      d.seamPointsJoined && `joined ${n(d.seamPointsJoined, 'pair')} of seam points`, d.trianglesTurned && `turned ${n(d.trianglesTurned, 'triangle')} to face outward`, d.pinchedEdgesCut && `separated surfaces along ${n(d.pinchedEdgesCut, 'edge')}`].filter(Boolean);
    if (r.status === 'sound') good.push('Already sound, and left exactly as it was.');
    else if (fixed.length) good.push(`Polymend ${fixed.join(', ')}. No existing point of the model was moved${d.seamPointsJoined ? ' apart from the joined seam points' : ''}.`);
    if (r.status === 'repaired') good.push('No open or non-manifold edges remain, and the faces agree on which way is out, which is what slicers check on import.');
    if (size) good.push(`Sized for print: ${size.join(' × ')} mm (width × depth × height), standing on the bed.`);
    // Whether it stands on its own, from its balance point and where it touches the bed.
    const st = r.stands;
    if (st && Number.isFinite(st.marginMm)) {
      if (st.marginMm < 0) weak.push(`It will not stand on its own: its balance point is ${-st.marginMm} mm beyond where it touches the bed, towards the ${st.towards}. Print it with a base, or plan a stand.`);
      else if (st.tipDegrees < 10) weak.push(`It stands, but tips easily: tilted about ${st.tipDegrees}° towards the ${st.towards} it falls over (its balance point is ${st.marginMm} mm inside the edge of where it touches the bed). A wider base, a small stand, or gluing it to a base will steady it.`);
      else good.push(`It stands steadily: it would have to tilt about ${st.tipDegrees}° towards the ${st.towards} to fall over.`);
      if (st.hangingMm !== undefined) weak.push(`A part hangs ${st.hangingMm} mm above the bed, outside where the model touches it: it will need support to print, and if it reached the bed it would help the model stand.`);
    }
    if (r.status === 'partial') {
      const remain = [after.openEdges && n(after.openEdges, 'open edge'), after.nonManifoldEdges && n(after.nonManifoldEdges, 'non-manifold edge'), after.inconsistentEdges && n(after.inconsistentEdges, 'wrongly facing join')].filter(Boolean);
      weak.push(`${remain.length ? remain.join(' and ') + ' remain' : 'It is not a closed solid'}, so a slicer will probably still warn.`);
      if (left.pinchedEdgesLeft) weak.push(`${n(left.pinchedEdgesLeft, 'edge')} where surfaces touch. Running again with --separate cuts them apart, but it can also part things meant to touch, such as fingers.`);
      const holes = left.holesLeftOpen || [];
      const wide = holes.filter(h => h === 'wide').length;
      if (wide) weak.push(`${n(wide, 'wide opening')} left open in case it is meant (like the top of a vase); --wide closes it.`);
      const large = holes.filter(h => typeof h === 'number');
      if (large.length) weak.push(`${n(large.length, 'hole')} too large to patch safely.`);
      if (left.sheetsLeft) weak.push(`${n(left.sheetsLeft, 'thin sheet')} with no thickness attached to the model; it cannot print as it is.`);
      if (left.flatPieces) weak.push(`${n(left.flatPieces, 'flat piece')} with no inside.`);
    }
    if (d.patchesGrazing) weak.push(`${n(d.patchesGrazing, 'patch', 'patches')} had to graze nearby surface where the model already overlaps itself. Slicers usually accept this; the marks show where to look.`);
    if (left.selfCrossings) weak.push(`As received, the model's surface passes through itself in ${n(left.selfCrossings, 'place')}. Polymend counted these and left them as they are. Most slicers fill them as solid, and in a preview they can show as small dark flecks; check those spots in your slicer.`);
    if (left.pointsTouching) weak.push(`The surface pinches to a single point in ${n(left.pointsTouching, 'place')}, where two parts just touch; most slicers accept this.`);
    if (r.notes?.length) weak.push(`This GLB has ${r.notes.join(', ')}; it was read in its rest pose.`);
    if (size && !(height > 0)) {
      const tall = size[2];
      if (tall < 5) weak.push(`At the file's own size it is only ${tall} mm tall; it may be meant in other units. Scale it in the slicer, or run again with a height in millimeters.`);
      if (tall > 500) weak.push(`At the file's own size it is ${tall} mm tall, larger than most printers. Scale it in the slicer, or run again with a height in millimeters.`);
    }
    if (size && size[2] < 80) weak.push(`At ${size[2]} mm tall, details thinner than about 0.4 mm (a common nozzle), such as teeth, fingertips or spikes, may print soft or not at all. Check them in the slicer preview.`);
    if (r.marked?.wholePiecesTurned) weak.push('A whole piece was turned the right way out; the views do not mark it face by face.');
    if (r.previewError) weak.push(`The views could not be drawn (${r.previewError}); the print files are not affected.`);
    lines.push('**Went well**', '', ...good.map(t => `- ${t}`), '');
    lines.push('**Less successful**', '', ...(weak.length ? weak : ['Nothing Polymend can measure. Check the views for likeness, the back, and thin parts.']).map(t => `- ${t}`), '');
    lines.push(`Files: ${[r.files?.stl, r.files?.threeMF, r.result, r.preview].filter(Boolean).map(f => '`' + path.basename(f) + '`').join(', ')}`, '');
  }
  return lines.join('\n');
}

const count = status => results.filter(r => r.status === status).length;
const batch = {
  out, height_mm: height > 0 ? height : null,
  models: results.length, repaired: count('repaired'), sound: count('sound'), partial: count('partial'), failed: count('failed'),
  review: path.join(out, 'polymend-review.md'),
  results: results.map(r => ({ input: r.input, ...(r.name ? { name: r.name } : {}), status: r.status, ...(r.downloaded ? { downloaded: r.downloaded } : {}), ...(r.error ? { error: r.error } : {}),
    ...(r.files ? { files: r.files, ...(r.result ? { result: r.result } : {}), ...(r.preview ? { preview: r.preview } : {}), size_mm: r.sizeMm, before: r.before, after: r.after, done: r.done, left: r.left, notes: r.notes, marked: r.marked, ...(r.stands ? { stands: r.stands } : {}) } : {}) })),
};
fs.writeFileSync(path.join(out, 'polymend-batch.json'), JSON.stringify(batch, null, 2));
fs.writeFileSync(batch.review, reviewText(results));
if (json) console.log(JSON.stringify(batch));
else {
  say(`\n${results.length} model${results.length === 1 ? '' : 's'}: ${['repaired', 'sound', 'partial', 'failed'].filter(count).map(s => `${count(s)} ${TITLES[s].toLowerCase()}`).join(', ')}.`);
  for (const r of results) say(`  ${(TITLES[r.status] || 'Not repaired').padEnd(16)} ${clean(r.name || path.basename(r.input))}${r.error ? `: ${r.error}` : r.sizeMm ? ` (${r.sizeMm.join(' × ')} mm)` : ''}`);
  say(`Files are in ${out}`);
  say(`Review: ${batch.review}`);
}
process.exit(0);
