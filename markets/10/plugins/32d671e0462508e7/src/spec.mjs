import { readFileSync } from 'node:fs';
import { catalog, categories, searchCatalog, renderCatalogPage } from './catalog.mjs';
import { DocumentError } from './errors.mjs';

export const specification = readFileSync(new URL('../skills/create-carousel/references/DSL_LAYOUT_SPEC.md', import.meta.url), 'utf8');
export const designGuide = readFileSync(new URL('../skills/create-carousel/references/DESIGN_GUIDE.md', import.meta.url), 'utf8');
export const writingGuide = readFileSync(new URL('../skills/create-carousel/references/WRITING_GUIDE.md', import.meta.url), 'utf8');
export const packageVersion = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8')).version;
export const capabilities = {
  plugin_version: packageVersion, server_version: packageVersion, format_version: 1,
  spec_revision: catalog.sourceRevision, catalog_revision: catalog.revision,
  app_compatibility: { verified_source_commit: catalog.sourceCommit, deployed_app_build: null },
  layer_types: ['text', 'shape', 'image', 'sticker', 'frame', 'grid', 'blender', 'mask'],
  resource_counts: Object.fromEntries(categories.map(kind => [kind, catalog.resources[kind].length])),
  media: 'still raster images only', fonts: 'system designs and catalog families',
  native_renderer: false, text_measurement: false, visual_check: 'not performed',
};

export function getSpecResponse(section = 'rules', query = '', options = {}) {
  if (section === 'catalogs') {
    const page = searchCatalog({ ...options, query });
    return { section, text: renderCatalogPage(page), catalog: page, capabilities };
  }
  if (options.category) throw new DocumentError('category is only available for section: catalogs');
  if (section === 'writing') return { section, text: writingGuide, capabilities };
  if (section === 'overview') return { section, text: designGuide + '\nRead rules for the native contract. Search catalogs by category or exact ID; examples returns complete editable documents. Check capabilities.native_renderer on the connected server. When true, create_carousel returns native PNG previews and render_carousel supports visual iteration; otherwise previews are unavailable.', capabilities };
  if (section === 'examples') {
    const index = JSON.parse(readFileSync(new URL('../data/examples.json', import.meta.url), 'utf8'));
    const q = query.toLocaleLowerCase();
    const matches = index.filter(entry => !q || JSON.stringify(entry).toLocaleLowerCase().includes(q));
    const examples = matches.map(entry => ({ ...entry, yaml: readFileSync(new URL('../' + entry.file, import.meta.url), 'utf8'), copy_role: 'layout_demo_only', visual_check: 'not performed' }));
    return { section, text: examples.length ? 'These examples demonstrate native layout. Their sample copy is not a headline library: write from the user’s material and read section: writing when composing copy.\n\n' + examples.map(entry => '## ' + entry.id + '\n' + entry.description + '\n\n```yaml\n' + entry.yaml + '\n```').join('\n\n') : 'No matching examples. Omit query to list all examples.', examples, capabilities };
  }
  if (!['rules', 'full'].includes(section)) throw new DocumentError('section must be overview, writing, rules, catalogs, examples, or full');
  const text = section === 'full' ? specification : specification.split('## 23. Каталоги')[0];
  if (!query) return { section, text, capabilities };
  // Return complete sections, including formulas and tables; never isolated matching lines.
  const q = query.toLocaleLowerCase();
  const blocks = text.split(/(?=^## )/m).map(body => ({ body, heading: body.split('\n')[0].toLocaleLowerCase() }));
  const matches = blocks.filter(block => block.body.toLocaleLowerCase().includes(q)).sort((a, b) => Number(b.heading.includes(q)) - Number(a.heading.includes(q)));
  const offset = options.offset ?? 0, limit = Math.min(options.limit ?? 3, 3);
  if (!Number.isInteger(offset) || offset < 0 || !Number.isInteger(limit) || limit < 1) throw new DocumentError('Invalid rules pagination');
  const selected = matches.slice(offset, offset + limit);
  return { section, text: selected.map(block => block.body).join('\n') || 'No matching rule sections. Read overview or search catalogs.', total: matches.length, offset, next_offset: offset + selected.length < matches.length ? offset + selected.length : null, capabilities };
}

export function getSpec(section = 'rules', query = '', options = {}) { return getSpecResponse(section, query, options).text; }
