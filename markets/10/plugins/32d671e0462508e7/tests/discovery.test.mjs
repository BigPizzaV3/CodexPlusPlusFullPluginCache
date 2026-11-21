import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import sharp from 'sharp';
import { unzipSync } from 'fflate';
import { catalog, resourceMaps, searchCatalog, renderCatalogMarkdown } from '../src/catalog.mjs';
import { instantiateRecipe, exampleDocument, ratioAspects } from '../src/recipes.mjs';
import { getSpecResponse, capabilities } from '../src/spec.mjs';
import { documentYAML, parseLayout, validateDocument } from '../src/document.mjs';
import { buildCarousel } from '../src/archive.mjs';

test('category words select resources instead of matching unrelated ID substrings', () => {
  for (const query of ['grid', 'grids', 'сетки', 'ГРИДЫ', 'коллаж']) {
    const page = searchCatalog({ query, limit: 50 });
    assert.equal(page.total, 28);
    assert.ok(page.entries.every(entry => entry.category === 'grids'));
    assert.ok(page.entries.some(entry => entry.id === 'quad'));
  }
  for (const query of ['frame', 'frames', 'рамки']) {
    const page = searchCatalog({ query, limit: 50 });
    assert.equal(page.total, 43);
    assert.ok(page.entries.every(entry => entry.category === 'frames'));
  }
  assert.equal(searchCatalog({ query: 'Hagrid' }).entries[0].category, 'fonts');
  assert.equal(searchCatalog({ query: 'frame', category: 'stickers' }).entries[0].category, 'stickers');
});

test('exact IDs outrank substring matches and preserve significant resource spaces', () => {
  assert.equal(searchCatalog({ query: 'Grunge01' }).entries[0].id, 'Grunge01');
  const id = 'catalog:VintagePaper/ 321x12';
  const entry = searchCatalog({ query: id }).entries[0];
  assert.equal(entry.id, id);
  assert.equal(entry.example.layers[0].sticker.source, id);
  assert.equal(searchCatalog({ query: 'DOES_NOT_EXIST' }).total, 0);
});

test('pagination retrieves the whole sticker catalog without dropping or duplicating resources', () => {
  const ids = [];
  let offset = 0;
  do {
    const page = searchCatalog({ category: 'stickers', offset, limit: 17 });
    ids.push(...page.entries.map(entry => entry.id));
    offset = page.next_offset;
  } while (offset !== null);
  assert.equal(ids.length, 464);
  assert.equal(new Set(ids).size, 464);
  assert.deepEqual(new Set(ids), new Set(resourceMaps.stickers.keys()));
  assert.throws(() => searchCatalog({ limit: 0 }));
  assert.throws(() => searchCatalog({ offset: -1 }));
});

test('quad is a complete native recipe and smart recipes retain swap defaults', () => {
  const quad = getSpecResponse('catalogs', 'quad').catalog.entries[0];
  const grid = quad.example.layers[0].grid;
  assert.deepEqual(grid.cells.map(cell => cell.rect), [[0,0,.5,.5],[.5,0,.5,.5],[0,.5,.5,.5],[.5,.5,.5,.5]]);
  assert.equal(grid.preset, undefined);
  assert.ok(grid.cells.every(cell => cell.photo.source === null));
  const stamp = getSpecResponse('catalogs', 'smartStampHorizontal').catalog.entries[0].example;
  assert.equal(stamp.layers[0].grid.swap.window, 'stamp');
  assert.equal(stamp.layers[0].grid.swap.area, 0.08);
  assert.deepEqual(stamp.requires, ['swap.stamp']);
  const thirds = instantiateRecipe('grids', resourceMaps.grids.get('v3')).layer.grid.cells;
  assert.deepEqual(thirds.map(cell => cell.rect[2]), [.34,.33,.33]);
});

test('all catalog examples validate with the same canonical resource IDs', () => {
  assert.deepEqual(Object.fromEntries(Object.entries(catalog.resources).map(([k,v])=>[k,v.length])), {grids:28,frames:43,fonts:22,shapes:19,templates:13,stickers:464});
  for (const [category, entries] of Object.entries(catalog.resources)) for (const entry of entries) {
    const example = exampleDocument(category, entry);
    if (category === 'templates') { assert.equal(example, null); continue; }
    assert.doesNotThrow(() => validateDocument(example), category + ':' + entry.id);
  }
});

test('every frame and grid recipe packages real shared photo bytes and preserves its native type', async () => {
  const photo = await sharp({create:{width:12,height:18,channels:3,background:'#c07042'}}).png().toBuffer();
  for (const category of ['frames','grids']) for (const entry of catalog.resources[category]) {
    const count = category === 'frames' ? entry.windows : entry.rects.length;
    const { layer, requires } = instantiateRecipe(category, entry, { sources: Array(count).fill('photo_1') });
    const input = { carousel:1,ratio:'portrait-4-5',slides:1,background:'FFFFFF',requires,layers:[layer] };
    const result = await buildCarousel(documentYAML(input),new Map([['photo_1',photo]]));
    const zip = unzipSync(result.bytes);
    const reopened = validateDocument(parseLayout(Buffer.from(zip['carousel.yaml']).toString()));
    assert.equal(Object.keys(reopened.layers[0])[0],category === 'frames' ? 'frame' : 'grid');
    assert.equal(Object.keys(reopened.assets).length,1);
    assert.equal(Object.keys(zip).length,2);
  }
});

test('frame helper respects source count and computes physical aspect for every slide ratio', () => {
  const entry = resourceMaps.frames.get('Polaroid01');
  for (const [ratio, aspect] of Object.entries(ratioAspects)) {
    const { layer, geometry } = instantiateRecipe('frames',entry,{ratio,width:0.5,sources:['real-photo']});
    assert.equal(layer.frame.photos[0].source,'real-photo');
    assert.ok(Math.abs(geometry.normalizedHeight - .5 * aspect * 1107 / 996) < 1e-10);
    assert.equal(layer.frame.height,undefined);
  }
  assert.throws(()=>instantiateRecipe('frames',resourceMaps.frames.get('Polaroid03'),{sources:['one']}));
  assert.throws(()=>instantiateRecipe('frames',entry,{size:[1,1]}));
  assert.throws(()=>instantiateRecipe('grids',resourceMaps.grids.get('quad'),{outside:2}));
  assert.throws(()=>instantiateRecipe('grids',resourceMaps.grids.get('quad'),{sources:['a','b','c']}));
});

test('query results and helper outputs cannot mutate the shared catalog', () => {
  const page = searchCatalog({ query:'quad' });
  page.entries[0].rects[0][0] = 99;
  page.entries[0].example.layers[0].grid.cells[0].rect[0] = 99;
  assert.equal(searchCatalog({query:'quad'}).entries[0].rects[0][0],0);
});

test('catalog documentation is generated from the canonical data and retains all IDs', async () => {
  const spec = await readFile(new URL('../skills/create-carousel/references/DSL_LAYOUT_SPEC.md',import.meta.url),'utf8');
  assert.equal('## 23. Каталоги'+spec.split('## 23. Каталоги')[1],renderCatalogMarkdown());
  for (const entries of Object.values(catalog.resources)) for (const entry of entries) assert.ok(spec.includes(entry.id),entry.id);
});

test('examples package as native editable documents with genuinely different element choices', async () => {
  const examples = getSpecResponse('examples').examples;
  assert.equal(examples.length,6);
  const results = new Map();
  for (const example of examples) {
    const {document} = await buildCarousel(example.yaml);
    results.set(example.id,document);
    assert.equal(example.visual_check,'not performed');
    assert.ok(example.plan.idea);
  }
  assert.ok(results.get('photo-story').layers.some(layer=>layer.frame));
  assert.ok(results.get('contact-gallery').layers.some(layer=>layer.grid));
  assert.ok(results.get('type-led').layers.every(layer=>layer.text||layer.shape));
  assert.ok(results.get('free-collage').layers.some(layer=>layer.image?.rotate));
  assert.ok(results.get('smart-stamp').layers.some(layer=>layer.grid?.swap));
  assert.ok(results.get('effects-study').layers.some(layer=>layer.mask));
  assert.ok(results.get('effects-study').layers.some(layer=>layer.blender));
});

test('versions are coherent and capabilities do not claim unavailable rendering', async () => {
  const plugin = JSON.parse(await readFile(new URL('../plugin.json',import.meta.url),'utf8'));
  assert.equal(capabilities.plugin_version,plugin.version);
  assert.equal(capabilities.server_version,plugin.version);
  assert.equal(capabilities.native_renderer,false);
  assert.equal(capabilities.text_measurement,false);
  assert.equal(getSpecResponse('overview').capabilities.format_version,1);
  assert.throws(()=>getSpecResponse('rules','',{category:'frames'}));
});
