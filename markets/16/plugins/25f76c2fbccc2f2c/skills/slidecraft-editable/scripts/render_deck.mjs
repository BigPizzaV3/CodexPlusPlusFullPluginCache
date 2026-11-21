import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const [specArg, outputArg] = process.argv.slice(2);
if (!specArg || !outputArg) throw new Error('Usage: render_deck.mjs SPEC.json NEW-DRAFT.pptx');
const specPath = path.resolve(specArg);
const output = path.resolve(outputArg);
if (output === specPath) throw new Error('Output must be a separate PPTX file');
try { await fs.access(output); throw new Error('Output already exists; choose a new draft path'); }
catch (e) { if (e.code !== 'ENOENT') throw e; }
const spec = JSON.parse(await fs.readFile(specPath, 'utf8'));
if (!Array.isArray(spec.slides) || !spec.slides.length) throw new Error('At least one slide specification is required');
const localPath = p => path.resolve(path.dirname(specPath), p);
const require = createRequire(import.meta.url);
let modulePath;
try {
  modulePath = require.resolve('@oai/artifact-tool', {paths: process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES ? [path.dirname(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES)] : [process.cwd()]});
} catch { throw new Error('Artifact Tool is unavailable in this file-authoring environment; use the available native presentation renderer'); }
const { FileBlob, Presentation, PresentationFile } = await import(pathToFileURL(modulePath).href);
const presentation = spec.baseDeck
  ? await PresentationFile.importPptx(await FileBlob.load(localPath(spec.baseDeck)))
  : Presentation.create({ slideSize: spec.slideSize ?? { width: 1280, height: 720 } });
const mime = {'.jpg':'image/jpeg','.jpeg':'image/jpeg','.png':'image/png','.webp':'image/webp','.svg':'image/svg+xml'};
function position(e) {
  const p = {left:e.x,top:e.y,width:e.w,height:e.h};
  if (Object.values(p).some(n => !Number.isFinite(n)) || p.width <= 0 || p.height <= 0) throw new Error(`Invalid geometry for ${e.name ?? e.kind}`);
  return p;
}
for (const item of spec.slides) {
  if (item.targetIndex !== undefined && item.targetIndex !== null && (!Number.isInteger(item.targetIndex) || item.targetIndex < 0 || item.targetIndex >= presentation.slides.items.length)) throw new Error('Invalid existing slide index');
  const slide = item.targetIndex === undefined || item.targetIndex === null ? presentation.slides.add() : presentation.slides.items[item.targetIndex];
  if (item.replaceContents) {
    if (item.targetIndex === undefined || item.targetIndex === null) throw new Error('replaceContents requires an existing slide');
    const snapshot = await presentation.inspect({kind:'shape,textbox,image,table,chart',maxChars:1000000});
    const ids = snapshot.ndjson.split('\n').filter(Boolean).map(line => JSON.parse(line))
      .filter(record => record.slideIndex === item.targetIndex && record.editable !== false && /^(sh|im|tb|ch)\//.test(record.id ?? ''))
      .map(record => record.id);
    if (ids.length) presentation.delete([...new Set(ids)]);
    slide.background.fill = item.background ?? '#FFFFFF';
  }
  if (item.background) slide.background.fill = item.background;
  if (item.notes !== undefined) slide.speakerNotes.text = item.notes;
  for (const e of item.elements ?? []) {
    if (e.kind === 'text') {
      if (typeof e.text !== 'string' || !Number.isFinite(e.size) || e.size <= 0) throw new Error('Text requires a string and explicit positive font size');
      const shape = slide.shapes.add({geometry:'textbox',name:e.name,position:position(e),fill:'none',line:{fill:'none',width:0}});
      shape.text = e.text;
      shape.text.style = {typeface:e.font ?? spec.fontFamily ?? 'Arial',fontSize:e.size,bold:e.bold ?? false,italic:e.italic ?? false,color:e.color ?? '#14243C',alignment:e.align ?? 'left',verticalAlignment:e.valign ?? 'top',wrap:e.wrap ?? 'square',insets:e.insets ?? 0,autoFit:'none',...(e.lineSpacing === undefined ? {} : {lineSpacing:e.lineSpacing})};
    } else if (e.kind === 'image') {
      const imagePath = localPath(e.path);
      const contentType = mime[path.extname(imagePath).toLowerCase()];
      if (!contentType) throw new Error('Unsupported local image format');
      const b = await fs.readFile(imagePath);
      slide.images.add({blob:b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),contentType,alt:e.alt ?? e.name ?? 'Image',fit:e.fit ?? 'contain',position:position(e),...(e.crop?{crop:e.crop}:{}),...(e.geometry?{geometry:e.geometry}:{}),...(e.borderRadius?{borderRadius:e.borderRadius}:{})});
    } else if (e.kind === 'shape') {
      slide.shapes.add({geometry:e.geometry ?? 'rect',name:e.name,position:position(e),fill:e.fill ?? 'none',line:{fill:e.lineColor ?? 'none',width:e.lineWidth ?? 0,style:'solid'}});
    } else if (e.kind === 'table') {
      slide.tables.add(e.config);
    } else if (e.kind === 'chart') {
      slide.charts.add(e.chartType,e.config);
    } else throw new Error(`Unsupported element kind: ${e.kind}`);
  }
}
await fs.mkdir(path.dirname(output),{recursive:true});
const previewDir = spec.previewDir ? localPath(spec.previewDir) : path.join(path.dirname(output),'previews');
await fs.mkdir(previewDir,{recursive:true});
for (const [i,slide] of presentation.slides.items.entries()) {
  const stem = `slide-${String(i+1).padStart(2,'0')}`;
  const png = await presentation.export({slide,format:'png',scale:1});
  await fs.writeFile(path.join(previewDir,`${stem}.png`),new Uint8Array(await png.arrayBuffer()));
  const layout = await slide.export({format:'layout'});
  await fs.writeFile(path.join(previewDir,`${stem}.layout.json`),await layout.text());
}
await (await PresentationFile.exportPptx(presentation)).save(output);
const inspection = await presentation.inspect({kind:'slide,textbox,shape,image,table,chart',maxChars:40000});
await fs.writeFile(`${output}.inspect.ndjson`,inspection.ndjson);
console.log(JSON.stringify({draft:output,slideCount:presentation.slides.items.length,previewDir}));
