import { z } from 'zod';
import { DocumentError } from './errors.mjs';

export const ratioAspects = Object.freeze({ 'square-1-1': 1, 'portrait-4-5': 4 / 5, 'portrait-3-4': 3 / 4, 'story-9-16': 9 / 16, 'landscape-191-1': 1.91 });
const finite = z.number().finite().min(-1_000_000).max(1_000_000);
const optionsSchema = z.object({
  ratio: z.enum(Object.keys(ratioAspects)).default('portrait-4-5'),
  slide: z.number().int().min(1).max(20).default(1),
  at: z.tuple([finite, finite]).default([0.5, 0.5]),
  size: z.tuple([finite.positive(), finite.positive()]).optional(),
  width: finite.positive().optional(),
  sources: z.array(z.string().min(1).nullable()).optional(),
  color: z.string().regex(/^[0-9a-fA-F]{6}$/).default('FFFFFF'),
  spacing: finite.nonnegative().default(0.015),
  outside: finite.nonnegative().default(0.02),
  corner: finite.nonnegative().default(0),
}).strict();

/** Expands catalog data; recipe IDs and helper metadata never enter the native layer. */
export function instantiateRecipe(category, entry, input = {}) {
  const parsed = optionsSchema.safeParse(input);
  if (!parsed.success) throw new DocumentError(`recipe options: ${parsed.error.message}`);
  const o = parsed.data;
  if (!['frames', 'grids'].includes(category)) throw new DocumentError('Recipe helpers support frames and grids');
  if (category === 'frames' && ['size', 'spacing', 'outside', 'corner', 'color'].some(key => key in input)) throw new DocumentError('Frame recipes use width; grid size, color and gutter options do not apply');
  if (category === 'grids' && 'width' in input) throw new DocumentError('Grid recipes use size, not width');
  const count = category === 'frames' ? entry.windows : entry.rects.length;
  if (o.sources && o.sources.length !== count) throw new DocumentError(`${entry.id} requires exactly ${count} sources, including null for empty slots`);
  const photos = (o.sources ?? Array(count).fill(null)).map(source => ({ source }));
  const common = { slide: o.slide, at: o.at };
  if (category === 'frames') {
    const aspect = entry.pixels[0] / entry.pixels[1];
    const width = o.width ?? Math.min(0.72, 0.60 * aspect / ratioAspects[o.ratio]);
    return { layer: { frame: { ...common, width, preset: entry.id, photos } }, requires: [], geometry: { normalizedHeight: width * ratioAspects[o.ratio] / aspect } };
  }
  const size = o.size ?? [0.9, 0.72];
  const grid = { ...common, size, color: o.color, spacing: o.spacing, outside: o.outside, corner: o.corner, cells: entry.rects.map((rect, index) => ({ rect: [...rect], photo: photos[index] })) };
  const heightInWidths = size[1] / ratioAspects[o.ratio];
  for (const [x, y, w, h] of entry.rects) {
    const ix = o.spacing / 2 * (Number(x > 0.000001) + Number(x + w < 0.999999));
    const iy = o.spacing / 2 * (Number(y > 0.000001) + Number(y + h < 0.999999));
    if (w * (size[0] - o.outside * 2) <= ix || h * (heightInWidths - o.outside * 2) <= iy) throw new DocumentError('Recipe spacing or outside removes a visible cell');
  }
  if (entry.swap) grid.swap = structuredClone(entry.swap);
  return { layer: { grid }, requires: entry.swap?.window === 'stamp' ? ['swap.stamp'] : [] };
}

export function exampleDocument(category, entry) {
  let layer, requires = [];
  if (category === 'frames' || category === 'grids') ({ layer, requires } = instantiateRecipe(category, entry));
  else if (category === 'fonts') layer = { text: { slide: 1, at: [0.5, 0.5], string: 'Aa', font: { family: entry.id, size: 0.08 }, color: '202020' } };
  else if (category === 'stickers') {
    layer = { sticker: { slide: 1, at: [0.5, 0.5], size: [0.5, 0.4], source: entry.id } };
    if (entry.tintRecommended) { layer.sticker.color = '202020'; requires.push('sticker.color'); }
  } else if (category === 'shapes') { layer = { shape: { slide: 1, at: [0.5, 0.5], size: [0.4, 0.32], kind: entry.id, fill: '202020' } }; requires.push('layer.shape'); }
  else return null; // A template name does not supply its document or assets.
  return { carousel: 1, ratio: 'portrait-4-5', slides: 1, background: 'F4F0E8', requires, layers: [layer] };
}
