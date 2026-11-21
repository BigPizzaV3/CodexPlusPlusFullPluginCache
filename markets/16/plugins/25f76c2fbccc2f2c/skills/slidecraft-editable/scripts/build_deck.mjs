// Native build, compatibility conversion, finalization, and two rendering engines.
import fs from 'node:fs/promises';
import path from 'node:path';
import {spawn} from 'node:child_process';
import {createHash} from 'node:crypto';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
import {validateBuildSpec} from './validate_build_spec.mjs';

const argv=process.argv.slice(2), specArg=argv.shift(), outputArg=argv.shift();
const options={};
while(argv.length){const key=argv.shift();if(key==='--pdf')options.pdf=true;else if(['--expect','--work-dir','--workspace','--compatibility','--presentation-skill-dir'].includes(key)&&argv.length)options[key.slice(2)]=argv.shift();else throw new Error(`Unknown or incomplete option: ${key}`);}
if(!specArg||!outputArg||!options.expect||!options.workspace)throw new Error('Usage: build_deck.mjs SPEC FINAL.pptx --expect EXPECT --workspace WORKSPACE [--work-dir PRIVATE-DIR] [--compatibility required|auto|off] [--pdf]');
const root=path.dirname(path.dirname(new URL(import.meta.url).pathname));
const workspace=path.resolve(options.workspace), finalPath=path.resolve(outputArg), specPath=path.resolve(specArg);
if(!finalPath.startsWith(workspace+path.sep))throw new Error('Output must be inside workspace');
try{await fs.access(finalPath);throw new Error('Output already exists');}catch(e){if(e.code!=='ENOENT')throw e;}
await fs.mkdir(path.dirname(finalPath),{recursive:true});
const mode=options.compatibility??'required';
if(!['required','auto','off'].includes(mode))throw new Error('Invalid compatibility mode');
const node=process.env.CODEX_PRIMARY_RUNTIME_NODE, python=process.env.CODEX_PRIMARY_RUNTIME_PYTHON;
if(!node||!python||!process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES)throw new Error('The presentation runtime is required');
const runtime=process.env.CODEX_PRIMARY_RUNTIME_ROOT??process.env.CODEX_PRIMARY_RUNTIME;
const presentationSkill=path.resolve(options['presentation-skill-dir']??'/root/.codex/skills/builtins/presentations');
const work=options['work-dir']?path.resolve(options['work-dir']):await fs.mkdtemp(path.join(workspace,'slidecraft-build-'));
if(!work.startsWith(workspace+path.sep)||work.startsWith(path.dirname(finalPath)+path.sep))throw new Error('Build directory must be private and inside workspace');
await fs.mkdir(work,{recursive:true});
async function run(executable,args){
  return await new Promise((resolve,reject)=>{
    const child=spawn(executable,args,{cwd:workspace,env:process.env,stdio:['ignore','pipe','pipe']});
    let output='';const timer=setTimeout(()=>child.kill('SIGTERM'),240000);
    child.stdout.on('data',b=>{output+=b;});child.stderr.on('data',b=>{output+=b;});
    child.on('error',e=>{clearTimeout(timer);reject(e);});
    child.on('close',code=>{clearTimeout(timer);if(code===0)resolve(output);else reject(new Error(`${path.basename(executable)} failed (${code}): ${output.slice(-6000)}`));});
  });
}
const spec=JSON.parse(await fs.readFile(specPath,'utf8'));
const expectations=JSON.parse(await fs.readFile(path.resolve(options.expect),'utf8'));
validateBuildSpec(spec,expectations);
const absolute=p=>path.resolve(path.dirname(specPath),p);
if(spec.baseDeck)spec.baseDeck=absolute(spec.baseDeck);
const contracts=[];
const appendedCount=spec.slides.filter(s=>s.targetIndex===undefined).length;
const retainedCount=spec.baseDeck?expectations.slideCount-appendedCount:0;
let appendedIndex=0;
for(const [i,slide] of spec.slides.entries()){
  if(slide.targetIndex!==undefined&&slide.replaceContents!==true)throw new Error('Existing-slide reconstruction requires replaceContents:true; use the native API for focused edits');
  const slideNumber=slide.targetIndex===undefined?retainedCount+(++appendedIndex):slide.targetIndex+1;
  let totalTitles=0;
  for(const e of slide.elements??[]){
    if(e.kind==='image'){
      e.path=absolute(e.path);
      if(e.role==='logo')contracts.push({slide:slideNumber,role:'logo',x:e.x,y:e.y,w:e.w,h:e.h,sha256:createHash('sha256').update(await fs.readFile(e.path)).digest('hex')});
    }
    if(e.kind==='text'&&e.role==='title')totalTitles++;
  }
  if(totalTitles!==1)throw new Error('Each authored slide requires exactly one text element with role:title');
}
spec.previewDir=path.join(work,'draft-previews');
await fs.writeFile(path.join(work,'spec.json'),JSON.stringify(spec));
await fs.writeFile(path.join(work,'contracts.json'),JSON.stringify(contracts));
const draft=path.join(work,'draft.pptx'), normalized=path.join(work,'normalized.pptx');
await run(node,[path.join(root,'scripts/render_deck.mjs'),path.join(work,'spec.json'),draft]);
const packageHelper=path.join(root,'scripts/prepare_package.py');
const first=JSON.parse(await run(python,[packageHelper,draft,'--output',normalized,'--contracts',path.join(work,'contracts.json')]));
const size=first.slideSizeEmu.join(',');
let candidate=normalized, compatibility={mode,officeRoundTrip:false,secondRenderer:false};
const soffice=runtime?path.join(runtime,'dependencies/bin/override/soffice'):null;
let officeAvailable=false;
if(soffice){try{await fs.access(soffice);officeAvailable=true;}catch{}}
if(mode==='required'&&!officeAvailable)throw new Error('LibreOffice compatibility runtime is unavailable; do not claim phone compatibility');
if(mode!=='off'&&officeAvailable){
  const officeDir=path.join(work,'office');await fs.mkdir(officeDir,{recursive:true});
  const profile=pathToFileURL(path.join(work,'office-profile')).href;
  await run(soffice,[`-env:UserInstallation=${profile}`,'--headless','--convert-to','pptx:Impress MS PowerPoint 2007 XML','--outdir',officeDir,normalized]);
  candidate=path.join(work,'candidate.pptx');
  await run(python,[packageHelper,path.join(officeDir,'normalized.pptx'),'--output',candidate,'--size',size,'--contracts',path.join(work,'contracts.json')]);
  compatibility.officeRoundTrip=true;
}
await run(python,[path.join(root,'scripts/audit_pptx.py'),candidate,'--expect',path.resolve(options.expect)]);
const {finalizePresentation}=await import(pathToFileURL(path.join(presentationSkill,'container_tools/artifact_tool_utils.mjs')).href);
const families=[...new Set(spec.fontFamilies??[spec.fontFamily,...spec.slides.flatMap(s=>(s.elements??[]).map(e=>e.font))].filter(Boolean))];
if(!families.length)throw new Error('Declare fontFamilies for the authored deck and retained template fonts');
await finalizePresentation({workspaceDir:workspace,candidatePath:candidate,finalPath,
  pythonExecutable:python,integrityValidatorPath:path.join(presentationSkill,'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(presentationSkill,'container_tools/inspect_presentation_layout_geometry.py'),
  layoutArgs:['--expected-slide-size-emu',size,'--validate-bullet-geometry','--validate-heading-fit'],
  explicitTotalSlideCount:expectations.slideCount,
  requiredNativeTableOwnerSlides:expectations.slides.filter(s=>s.nativeTables>0).map(s=>s.slide),
  requiredNativeChartOwnerSlides:expectations.slides.filter(s=>s.nativeCharts>0).map(s=>s.slide),
  fontPolicy:{basis:'design',families},verifyArtifactToolImport:true,receiptPath:path.join(work,'validation.json')});
await run(python,[packageHelper,finalPath,'--contracts',path.join(work,'contracts.json')]);
const require=createRequire(import.meta.url);
const modulePath=require.resolve('@oai/artifact-tool',{paths:[path.dirname(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES)]});
const {FileBlob,PresentationFile}=await import(pathToFileURL(modulePath).href);
const p=await PresentationFile.importPptx(await FileBlob.load(finalPath));
const previews=path.join(work,'final-previews');await fs.mkdir(previews,{recursive:true});
for(const [i,slide] of p.slides.items.entries()){
  const png=await p.export({slide,format:'png',scale:1});
  await fs.writeFile(path.join(previews,`slide-${i+1}.png`),new Uint8Array(await png.arrayBuffer()));
}
let pdfPath=null;
if(compatibility.officeRoundTrip){
  const pdfDir=path.join(work,'office-pdf');await fs.mkdir(pdfDir,{recursive:true});
  await run(soffice,[`-env:UserInstallation=${pathToFileURL(path.join(work,'office-profile')).href}`,'--headless','--convert-to','pdf','--outdir',pdfDir,finalPath]);
  const pdf=path.join(pdfDir,path.basename(finalPath,'.pptx')+'.pdf');
  for(let i=1;i<=p.slides.items.length;i++){
    await run('pdftoppm',['-f',String(i),'-singlefile','-scale-to','1411','-png',pdf,path.join(previews,`office-slide-${i}`)]);
  }
  await run(python,['-c','from PIL import Image; import sys; [Image.open(p).verify() for p in sys.argv[1:]]',
    ...p.slides.items.map((_,i)=>path.join(previews,`office-slide-${i+1}.png`))]);
  compatibility.secondRenderer=true;
  if(options.pdf){pdfPath=finalPath.replace(/\.pptx$/i,'.pdf');try{await fs.access(pdfPath);throw new Error('PDF output already exists');}catch(e){if(e.code!=='ENOENT')throw e;}await fs.copyFile(pdf,pdfPath);}
}else if(options.pdf)throw new Error('PDF output requires the compatibility renderer');
const result={pptx:finalPath,pdf:pdfPath,previews,compatibility,requiresVisualReview:true,phoneRenderingVerified:false};
await fs.writeFile(path.join(work,'result.json'),JSON.stringify(result,null,2));
console.log(JSON.stringify(result));
