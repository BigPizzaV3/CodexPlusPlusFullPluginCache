import test from 'node:test';
import assert from 'node:assert/strict';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { InMemoryTransport } from '@modelcontextprotocol/sdk/inMemory.js';
import { documentYAML, validateDocument } from '../src/document.mjs';
import { diagnoseDocument } from '../src/diagnostics.mjs';
import { createMCPServer } from '../src/server.mjs';
import { buildCarousel } from '../src/archive.mjs';

const shape = (slide=1,at=[.5,.5],size=[.5,.4],extra={})=>({shape:{slide,at,size,kind:'rectangle',fill:'FFFFFF',...extra}});
const image = (slide=1,at=[.5,.5],size=[.46,.368],extra={})=>({image:{slide,at,size,source:null,...extra}});
const doc = (layers,slides=1)=>({carousel:1,ratio:'portrait-4-5',slides,background:'FFFFFF',requires:[],layers});
const warnings = document=>diagnoseDocument(validateDocument(document)).warnings;
const codes = document=>warnings(document).map(w=>w.code);

test('colored image borders produce a portability warning without mutating the document', async () => {
  const input=doc([image(1,[.5,.5],[.5,.4],{border:{width:.01,color:'FF0000'}})]);
  const result=await buildCarousel(documentYAML(input));
  assert.ok(result.diagnostics.warnings.some(w=>w.code==='IMAGE_BORDER_COLOR_LOSS'&&w.path==='layers.0.image.border.color'));
  assert.equal(result.document.layers[0].image.border.color,'FF0000');
  for(const color of ['FFFFFF','1F1F1F']) assert.ok(!codes(doc([image(1,[.5,.5],[.5,.4],{border:{width:.01,color}})])).includes('IMAGE_BORDER_COLOR_LOSS'));
});

test('simple uniform mats are suggested as borders but deliberate shadows are preserved', () => {
  assert.ok(codes(doc([shape(),image()])).includes('POSSIBLE_NATIVE_IMAGE_BORDER'));
  assert.ok(!codes(doc([shape(1,[.5,.5],[.5,.4],{shadow:{color:'000000',blur:.02}}),image()])).includes('POSSIBLE_NATIVE_IMAGE_BORDER'));
  assert.ok(!codes(doc([shape(1,[.5,.5],[.5,.4],{fill:'FF0000'}),image()])).includes('POSSIBLE_NATIVE_IMAGE_BORDER'));
});

test('regular galleries get a grid suggestion while rotated photos and overlapping collages do not', () => {
  const gallery=[image(1,[.2,.3],[.2,.2]),image(1,[.5,.3],[.2,.2]),image(1,[.8,.3],[.2,.2])];
  assert.ok(codes(doc(gallery)).includes('POSSIBLE_NATIVE_GRID'));
  const rotated=structuredClone(gallery);rotated[1].image.rotate=10;
  assert.ok(!codes(doc(rotated)).includes('POSSIBLE_NATIVE_GRID'));
  assert.ok(!codes(doc([image(),image(),image()])).includes('POSSIBLE_NATIVE_GRID'));
});

test('overlapping grid cells produce warnings but intentional compositions still validate', () => {
  const input=doc([{grid:{slide:1,at:[.5,.5],size:[1,1],color:'FFFFFF',cells:[{rect:[0,0,1,1],photo:{source:null}},{rect:[0,0,1,1],photo:{source:null}}]}}]);
  assert.ok(codes(input).includes('OVERLAPPING_GRID_CELLS'));
  input.layers[0].grid.cells=[{rect:[0,0,.5,1],photo:{source:null}},{rect:[.5,0,.5,1],photo:{source:null}}];
  assert.ok(!codes(input).includes('OVERLAPPING_GRID_CELLS'));
});

test('blank-slide and operator checks use world geometry rather than only home slide IDs', () => {
  assert.ok(warnings(doc([image()],2)).some(w=>w.code==='NO_PLACED_CONTENT'&&w.slide===2));
  assert.ok(!codes(doc([image(1,[1,.5],[2,1])],2)).includes('NO_PLACED_CONTENT'));
  const mask={mask:{slide:2,at:[.5,.5],size:[1,1],color:'000000'}};
  assert.ok(codes(doc([shape(1),mask,shape(3)],3)).includes('EFFECT_OPERANDS_OUTSIDE_REGION'));
  assert.ok(!codes(doc([shape(1,[1.5,.5],[3,1]),mask,shape(3,[-.5,.5],[3,1])],3)).includes('EFFECT_OPERANDS_OUTSIDE_REGION'));
});

test('draft validation reports unresolved assets, but creation still requires their actual bytes', async () => {
  const server=createMCPServer({publicURL:'https://example.test'});
  const client=new Client({name:'diagnostic-test',version:'1'});
  const [a,b]=InMemoryTransport.createLinkedPair();
  await Promise.all([server.connect(a),client.connect(b)]);
  try {
    const yaml=documentYAML(doc([image(1,[.5,.5],[.5,.5],{source:'photo_1'})]));
    const strict=await client.callTool({name:'validate_carousel',arguments:{yaml}});
    assert.equal(strict.isError,true);
    const draft=await client.callTool({name:'validate_carousel',arguments:{yaml,allow_unresolved_assets:true}});
    assert.equal(draft.structuredContent.valid,true);
    assert.equal(draft.structuredContent.asset_references_resolved,false);
    assert.deepEqual(draft.structuredContent.unresolved_assets,['photo_1']);
    assert.equal(draft.structuredContent.asset_bytes_checked,false);
    assert.equal((await client.callTool({name:'create_carousel',arguments:{yaml}})).isError,true);
    const spec=await client.callTool({name:'get_carousel_spec',arguments:{section:'catalogs',query:'сетки',limit:50}});
    assert.equal(spec.structuredContent.catalog.total,28);
    assert.ok(spec.structuredContent.catalog.entries.every(e=>e.example.layers[0].grid));
    const output=await client.callTool({name:'create_carousel',arguments:{yaml:documentYAML(doc([image(1,[.5,.5],[.5,.4],{border:{width:.01,color:'FF0000'}})]))}});
    assert.ok(output.structuredContent.warnings.some(w=>w.code==='IMAGE_BORDER_COLOR_LOSS'));
    assert.equal(output.structuredContent.visual_check,'not performed');
  } finally { await client.close(); await server.close(); }
});
