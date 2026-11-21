import { z } from 'zod';
import { isAlias, parseDocument, stringify, visit } from 'yaml';

import { catalog, resourceMaps } from './catalog.mjs';
import { DocumentError } from './errors.mjs';
export { DocumentError } from './errors.mjs';
export { specification, getSpec } from './spec.mjs';
const stickerSources = new Set(resourceMaps.stickers.keys());
const fontFamilies = new Set(resourceMaps.fonts.keys());
const frames = resourceMaps.frames;

const finite = z.number().finite().min(-1_000_000).max(1_000_000);
const positive = finite.positive();
const nonnegative = finite.nonnegative();
const unit = z.number().finite().min(0).max(1);
const pair = z.tuple([finite, finite]);
const size = z.tuple([positive, positive]);
const color = z.string().regex(/^(?:[\da-fA-F]{6}|[\da-fA-F]{8})$/);
const opaque = z.string().regex(/^[\da-fA-F]{6}$/);
const source = z.string().min(1).nullable();
const object = fields => z.object(fields).strict();
const border = object({ width: nonnegative, color });
const shadow = object({ color: opaque, enabled: z.boolean().optional(), opacity: unit.optional(), angle: finite.optional(), distance: nonnegative.optional(), blur: nonnegative.optional() });
const crop = z.tuple([nonnegative, nonnegative, positive, positive]).refine(([x, y, w, h]) => x + w <= 1.000001 && y + h <= 1.000001, 'crop must stay inside the source image');
const photoFields = { source, crop: crop.optional(), order: z.number().int().nonnegative().optional(), required: z.boolean().optional(), muted: z.boolean().optional() };
const photo = object({ ...photoFields, pan: pair.optional(), zoom: positive.optional(), rotate: finite.optional() }).superRefine((p, ctx) => {
  if (p.source === null && ['crop', 'pan', 'zoom', 'rotate', 'muted'].some(k => k in p)) ctx.addIssue({ code: 'custom', message: 'Empty slots must not contain photographic adjustments' });
});
const base = { slide: z.number().int().min(1).max(20), at: pair, locked: z.boolean().optional() };
const movable = { rotate: finite.optional() };
const flipped = { flip: z.tuple([z.boolean(), z.boolean()]).optional() };
const appearance = { opacity: unit.optional(), shadow: shadow.optional() };
const blendMode = z.enum(['normal', 'darken', 'multiply', 'plusDarker', 'colorBurn', 'lighten', 'screen', 'plusLighter', 'colorDodge', 'overlay', 'softLight', 'hardLight', 'difference', 'exclusion', 'hue', 'saturation', 'color', 'luminosity']);
const blendFields = { mode: z.enum(['normal', 'screen', 'multiply', 'lighten', 'darken', 'overlay', 'softLight', 'difference']), opacity: unit.optional(), mask: z.enum(['off', 'darkAreas', 'brightAreas']).optional(), threshold: unit.optional(), softness: unit.optional() };
const font = object({ design: z.enum(['system', 'rounded', 'serif', 'mono']).optional(), family: z.string().optional(), weight: z.enum(['light', 'regular', 'medium', 'semibold', 'bold', 'heavy']).optional(), italic: z.boolean().optional(), size: positive }).refine(f => Boolean(f.design) !== Boolean(f.family), 'Provide exactly one of font.design and font.family');
const gradient = object({ style: z.enum(['linear', 'radial', 'triangle']), angle: z.number().finite().min(0).max(360).optional(), stops: z.array(object({ at: unit, color })).min(2).max(32) });
const schemas = {
  text: object({ ...base, ...movable, ...flipped, string: z.string().trim().min(1).max(24000), font, color, background: color.nullable().optional(), align: z.enum(['left', 'center', 'right']).optional(), case: z.enum(['original', 'upper', 'lower', 'title']).optional(), tracking: finite.optional(), leading: nonnegative.optional(), decorations: z.array(z.enum(['underline', 'strikethrough'])).optional(), blendMode: blendMode.optional() }),
  shape: object({ ...base, ...movable, ...flipped, ...appearance, size, kind: z.enum(catalog.resources.shapes.map(entry => entry.id)), fill: color.nullable(), stroke: border.optional(), gradient: gradient.optional(), blendMode: blendMode.optional() }),
  image: object({ ...base, ...movable, ...photoFields, size, opacity: unit.optional(), corner: nonnegative.optional(), border: border.optional(), blendMode: blendMode.optional(), blend: object({ source: z.string().min(1), ...blendFields }).optional() }),
  sticker: object({ ...base, ...movable, ...flipped, ...appearance, size, source, color: opaque.optional() }),
  frame: object({ ...base, ...movable, ...flipped, ...appearance, width: positive, preset: z.string().min(1), photos: z.array(photo), ink: object({ color: opaque, opacity: unit.optional() }).optional() }),
  grid: object({ ...base, size, color, spacing: nonnegative.optional(), outside: nonnegative.optional(), corner: nonnegative.optional(), cells: z.array(object({ rect: z.tuple([nonnegative, nonnegative, positive, positive]).refine(([x, y, w, h]) => x + w <= 1.000001 && y + h <= 1.000001, 'cell rect must stay inside the grid'), photo })).min(1).max(200), swap: object({ mode: z.enum(['vertical', 'horizontal']), area: unit.optional(), aspect: z.number().finite().min(0.25).max(4).optional(), window: z.enum(['rectangle', 'stamp']).optional(), offset: pair.optional(), border: border.optional() }).nullable().optional() }),
  blender: object({ ...base, size, ...blendFields }),
  mask: object({ ...base, size, color, strength: unit.optional() })
};
const requirements = new Set(['layer.shape', 'layer.shape.gradient', 'layer.blender', 'layer.mask', 'blend.multi-exposure', 'swap.stamp', 'frame.ink', 'frame.flip', 'sticker.color', 'shape.blend-mode', 'image.blend-mode', 'text.blend-mode']);
const root = object({ carousel: z.literal(1), ratio: z.enum(['square-1-1', 'portrait-4-5', 'portrait-3-4', 'story-9-16', 'landscape-191-1']), slides: z.number().int().min(1).max(20), background: color, requires: z.array(z.string()).max(32), assets: z.record(object({ file: z.string().regex(/^assets\/[a-f0-9]{64}\.(png|jpg)$/), pixels: z.tuple([z.number().int().positive(), z.number().int().positive()]).optional() })).optional(), layers: z.array(z.record(z.unknown())).min(1).max(2000) });

function checked(schema, value, prefix) {
  const result = schema.safeParse(value);
  if (!result.success) throw new DocumentError(result.error.issues.map(i => `${prefix}${i.path.length ? '.' + i.path.join('.') : ''}: ${i.message}`).join('\n'));
  return result.data;
}

export function parseLayout(yaml) {
  if (typeof yaml !== 'string' || Buffer.byteLength(yaml) > 4 * 1024 * 1024) throw new DocumentError('YAML must be UTF-8 text of at most 4 MiB');
  const ast = parseDocument(yaml, { uniqueKeys: true, version: '1.2', strict: true });
  if (ast.errors.length) throw new DocumentError(ast.errors.map(e => e.message).join('\n'));
  visit(ast, (_key, node) => {
    if (isAlias(node) || node?.anchor || node?.tag) throw new DocumentError('YAML anchors, aliases, and explicit tags are unsupported');
    if (node?.type === 'BLOCK_LITERAL' || node?.type === 'BLOCK_FOLDED') throw new DocumentError('Use quoted strings with explicit \\n, not block strings');
  });
  return ast.toJS({ maxAliasCount: 0 });
}

export function referencedAssets(document) {
  const names = new Set();
  for (const wrapper of document.layers ?? []) {
    const [kind, layer] = Object.entries(wrapper)[0] ?? [];
    if (!layer || typeof layer !== 'object') continue;
    const photos = kind === 'frame' ? layer.photos ?? [] : kind === 'grid' ? (layer.cells ?? []).map(c => c.photo) : [layer];
    for (const p of photos) {
      if (typeof p?.source === 'string' && !(kind === 'sticker' && p.source.startsWith('catalog:'))) names.add(p.source);
      if (typeof p?.blend?.source === 'string') names.add(p.blend.source);
    }
  }
  return names;
}

export function validateDocument(input, { allowUnresolvedAssets = false } = {}) {
  const document = checked(root, input, 'document');
  for (const tag of document.requires) if (!requirements.has(tag)) throw new DocumentError(`requires: unsupported capability ${tag}`);
  const required = new Set(document.requires);
  const need = tag => required.add(tag);
  document.layers = document.layers.map((wrapper, index) => {
    const path = `layers.${index}`;
    const entries = Object.entries(wrapper);
    if (entries.length !== 1 || !Object.hasOwn(schemas, entries[0]?.[0])) throw new DocumentError(`${path}: expected exactly one supported layer type`);
    const [kind, value] = entries[0];
    const p = checked(schemas[kind], value, `${path}.${kind}`);
    if (p.slide > document.slides) throw new DocumentError(`${path}.${kind}.slide: this slide does not exist`);
    if (kind === 'text') {
      if (p.font.family && !fontFamilies.has(p.font.family)) throw new DocumentError(`${path}.text.font.family: use a bundled family from the catalog or a system design`);
      p.string = p.string.replace(/\r\n|[\r\u0085\u2028\u2029]/g, '\n');
    }
    if (p.blendMode) need(`${kind}.blend-mode`);
    if (kind === 'shape') {
      need('layer.shape');
      if (p.gradient) {
        need('layer.shape.gradient');
        if (p.fill?.toUpperCase() !== p.gradient.stops[0].color.toUpperCase()) throw new DocumentError(`${path}.shape.fill: must equal the first gradient stop`);
        if (p.gradient.style === 'radial' && 'angle' in p.gradient) throw new DocumentError(`${path}.shape.gradient.angle: omit for radial gradients`);
        if (p.gradient.stops.some((stop, i, all) => i > 0 && stop.at < all[i - 1].at)) throw new DocumentError(`${path}.shape.gradient.stops: positions must be sorted`);
      }
    }
    if (kind === 'image') {
      if (p.source === null && ['crop', 'muted', 'blend'].some(k => k in p)) throw new DocumentError(`${path}.image: empty slots cannot have photo adjustments or blending`);
      if (p.blend) need('blend.multi-exposure');
    }
    if (kind === 'sticker') {
      if (p.source?.startsWith('catalog:') && !stickerSources.has(p.source)) throw new DocumentError(`${path}.sticker.source: unknown catalog sticker`);
      if (p.color) need('sticker.color');
    }
    if (kind === 'frame') {
      const preset = frames.get(p.preset);
      if (!preset) throw new DocumentError(`${path}.frame.preset: unknown frame preset`);
      if (p.photos.length !== preset.windows) throw new DocumentError(`${path}.frame.photos: ${p.preset} requires ${preset.windows} slots`);
      if (p.ink && !preset.ink) throw new DocumentError(`${path}.frame.ink: this preset cannot be recolored`);
      if (p.ink) need('frame.ink');
      if (p.flip) need('frame.flip');
    }
    if (kind === 'grid') {
      const heightInWidths = p.size[1] * ({ 'square-1-1': 1, 'portrait-4-5': 1.25, 'portrait-3-4': 4 / 3, 'story-9-16': 16 / 9, 'landscape-191-1': 1 / 1.91 }[document.ratio]);
      const outside = p.outside ?? 0;
      const spacing = p.spacing ?? 0;
      for (const cell of p.cells) {
        const [x, y, w, h] = cell.rect;
        const insetX = spacing / 2 * (Number(x > 0.000001) + Number(x + w < 0.999999));
        const insetY = spacing / 2 * (Number(y > 0.000001) + Number(y + h < 0.999999));
        if (w * (p.size[0] - outside * 2) <= insetX || h * (heightInWidths - outside * 2) <= insetY) throw new DocumentError(`${path}.grid: spacing or outside removes a cell's visible area`);
      }
      if (p.swap) {
        if (p.cells.length !== 2) throw new DocumentError(`${path}.grid.swap: requires exactly two cells`);
        const minArea = p.swap.window === 'stamp' ? 0.08 : 0.2;
        if ((p.swap.area ?? 0.2) < minArea || (p.swap.area ?? 0.2) > 0.5) throw new DocumentError(`${path}.grid.swap.area: must be ${minArea}…0.5`);
        if (p.swap.window === 'stamp') need('swap.stamp');
      }
    }
    if (kind === 'blender' || kind === 'mask') {
      need(`layer.${kind}`);
      const content = w => !('mask' in w) && !('blender' in w);
      if (!input.layers.slice(0, index).some(content) || !input.layers.slice(index + 1).some(content)) throw new DocumentError(`${path}.${kind}: requires content layers below and above`);
    }
    return { [kind]: p };
  });
  if (!allowUnresolvedAssets) for (const name of referencedAssets(document)) if (!Object.hasOwn(document.assets ?? {}, name)) throw new DocumentError(`assets.${name}: referenced image was not supplied`);
  document.requires = [...required];
  return document;
}

export function documentYAML(document) {
  return stringify(document, { lineWidth: 0, defaultStringType: 'QUOTE_DOUBLE', defaultKeyType: 'PLAIN', doubleQuotedAsJSON: true, aliasDuplicateObjects: false });
}
