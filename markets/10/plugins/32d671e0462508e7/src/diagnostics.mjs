import { resourceMaps } from './catalog.mjs';
import { ratioAspects } from './recipes.mjs';

const EPS = 1e-6;
const near = (a, b, tolerance = 0.002) => Math.abs(a - b) <= tolerance;
const intersects = (a, b) => a && b && Math.min(a.right, b.right) - Math.max(a.left, b.left) > EPS && Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > EPS;

/** Conservative world-space bounds in slide-width units, including rotation. Text needs real font metrics. */
export function layerBounds(kind, layer, ratio) {
  const aspect = ratioAspects[ratio];
  let w, h;
  if (kind === 'text') return null;
  if (kind === 'frame') {
    const entry = resourceMaps.frames.get(layer.preset);
    if (!entry) return null;
    w = layer.width; h = w * entry.pixels[1] / entry.pixels[0];
  } else if (layer.size) { w = layer.size[0]; h = layer.size[1] / aspect; }
  else return null;
  const angle = (layer.rotate ?? 0) * Math.PI / 180;
  const bw = Math.abs(w * Math.cos(angle)) + Math.abs(h * Math.sin(angle));
  const bh = Math.abs(w * Math.sin(angle)) + Math.abs(h * Math.cos(angle));
  const extra = kind === 'shape' ? layer.stroke?.width ?? 0 : 0;
  const x = layer.slide - 1 + layer.at[0], y = layer.at[1] / aspect;
  return { left: x - bw / 2 - extra, right: x + bw / 2 + extra, top: y - bh / 2 - extra, bottom: y + bh / 2 + extra };
}

export function diagnoseDocument(document) {
  const warnings = [], usage = {}, maxWarnings = 100;
  let omitted = 0;
  const add = (code, path, slide, message, suggestion) => {
    if (warnings.length === maxWarnings) { omitted++; return; }
    warnings.push({ code, severity: 'warning', path, slide, message, suggestion });
  };
  const rows = document.layers.map((wrapper, index) => {
    const [kind, layer] = Object.entries(wrapper)[0];
    usage[kind] = (usage[kind] ?? 0) + 1;
    return { kind, layer, index, bounds: layerBounds(kind, layer, document.ratio) };
  });
  const aspect = ratioAspects[document.ratio];
  const imageGroups = new Map();
  for (const row of rows) {
    const { kind, layer: p, index, bounds } = row, path = `layers.${index}.${kind}`;
    if (kind === 'image') {
      if (p.border && !['FFFFFF', '1F1F1F'].includes(p.border.color.toUpperCase())) add('IMAGE_BORDER_COLOR_LOSS', path + '.border.color', p.slide, 'ACE saves only a white or dark image border; this color will change.', 'Use FFFFFF/1F1F1F, a suitable grid mat, or keep an intentional colored shape backing.');
      const back = rows[index - 1];
      if (back?.kind === 'shape') {
        const s = back.layer;
        const dx = (s.size[0] - p.size[0]) / 2, dy = (s.size[1] - p.size[1]) / (2 * aspect);
        if (s.kind === 'rectangle' && ['FFFFFF', '1F1F1F'].includes(s.fill?.toUpperCase()) && !s.shadow && !s.gradient && !s.stroke && !s.blendMode && (s.opacity ?? 1) === 1 && s.slide === p.slide && s.at.every((v, i) => near(v, p.at[i])) && near(s.rotate ?? 0, p.rotate ?? 0) && dx > EPS && dx < 0.06 && near(dx, dy) && !p.border && !p.corner) {
          add('POSSIBLE_NATIVE_IMAGE_BORDER', path, p.slide, 'A uniform white/dark rectangle directly behind this photo resembles a photo border.', 'Consider image.border if it preserves the intended geometry; retain the backing when independently editable decoration is intended.');
        }
      }
      if (!(p.rotate ?? 0) && !(p.opacity !== undefined && p.opacity !== 1) && !p.blend && !p.blendMode && !p.border && !p.corner) {
        const group = imageGroups.get(p.slide) ?? [];
        group.push(row); imageGroups.set(p.slide, group);
      }
    }
    if (kind === 'grid') {
      for (let i = 0; i < p.cells.length; i++) for (let j = i + 1; j < p.cells.length; j++) {
        const rect = cell => { const [x,y,w,h] = cell.rect; return { left:x, right:x+w, top:y, bottom:y+h }; };
        if (intersects(rect(p.cells[i]), rect(p.cells[j]))) { add('OVERLAPPING_GRID_CELLS', path + '.cells', p.slide, `Cells ${i} and ${j} overlap before gutters.`, 'Check the recipe coordinates; keep intentional overlap if it is part of the composition.'); i = p.cells.length; break; }
      }
    }
    if (kind === 'mask' || kind === 'blender') {
      // Operators apply to groups on a continuous strip. Different home slides can still overlap.
      const lower = rows.slice(0, index).filter(r => !['mask','blender'].includes(r.kind));
      const upper = rows.slice(index + 1).filter(r => !['mask','blender'].includes(r.kind));
      const canReach = group => group.some(r => r.kind === 'text' || intersects(bounds, r.bounds));
      if (!canReach(lower) || !canReach(upper)) add('EFFECT_OPERANDS_OUTSIDE_REGION', path, p.slide, 'At least one side of this operator has no content bounds intersecting its region.', 'Inspect the operator region and layer order in ACE. Text bounds and actual mask pixels need native rendering.');
    }
    if (bounds && !intersects(bounds, {left:0,right:document.slides,top:0,bottom:1/aspect})) add('OUTSIDE_CAROUSEL', path, p.slide, 'This layer bounds is outside the whole carousel strip.', 'Check global geometry; preserve an intentional off-canvas layer.');
    if (kind === 'shape' && p.kind === 'rectangle' && p.fill?.toUpperCase() === document.background.toUpperCase() && !p.gradient && !p.stroke && !p.shadow) {
      const back = rows[index - 1];
      if (back?.kind === 'shape') {
        const s = back.layer;
        if (s.kind === 'rectangle' && s.fill && !s.gradient && !s.stroke && !s.shadow && s.slide === p.slide && near(s.rotate ?? 0, p.rotate ?? 0) && s.at.every((v,i) => near(v,p.at[i])) && s.size.every((v,i) => v > p.size[i] && v < p.size[i] * 1.25)) add('POSSIBLE_SHAPE_OUTLINE', path, p.slide, 'Two filled rectangles may be simulating an outline by covering the center.', 'Consider one shape with fill:null and stroke; do not replace if the inner fill intentionally hides other content.');
      }
    }
  }
  // Detect complete regular galleries only; unrelated photos and free collages remain valid.
  for (const [slide, photos] of imageGroups) {
    if (photos.length < 3 || photos.length > 16) continue;
    const [first] = photos;
    if (!photos.every(r => r.layer.size.every((v,i) => near(v, first.layer.size[i])))) continue;
    const unique = values => values.toSorted((a,b) => a-b).filter((v,i,all) => i === 0 || !near(v,all[i-1]));
    const xs = unique(photos.map(r => r.layer.at[0])), ys = unique(photos.map(r => r.layer.at[1]));
    const evenlySpaced = values => values.length < 3 || values.slice(2).every((v,i) => near(v-values[i+1],values[1]-values[0]));
    if (xs.length * ys.length !== photos.length || !evenlySpaced(xs) || !evenlySpaced(ys)) continue;
    const occupied = new Set(photos.map(r => xs.findIndex(x=>near(x,r.layer.at[0])) + ':' + ys.findIndex(y=>near(y,r.layer.at[1]))));
    if (occupied.size !== photos.length || photos.some((a,i) => photos.slice(i+1).some(b => intersects(a.bounds,b.bounds)))) continue;
    add('POSSIBLE_NATIVE_GRID', `layers.${first.index}.image`, slide, `${photos.length} equal-size aligned photos form a regular gallery.`, 'Consider a native grid for shared spacing and photo replacement. Check gutter units and preserve independent photo treatment when intended.');
  }
  for (let slide = 1; slide <= document.slides; slide++) {
    const region = { left:slide-1, right:slide, top:0, bottom:1/aspect };
    if (!rows.some(r => r.kind === 'text' ? r.layer.slide === slide : intersects(r.bounds,region))) add('NO_PLACED_CONTENT', 'layers', slide, 'No sized layer intersects this slide and no text is anchored here.', 'Check whether the blank slide is intentional. Cross-slide text needs actual font measurement.');
  }
  return { warnings, omitted_warnings: omitted, layer_usage: usage, checks: { structure: 'passed', semantics: 'heuristic', text_measurement: 'not performed', visual_check: 'not performed' } };
}
