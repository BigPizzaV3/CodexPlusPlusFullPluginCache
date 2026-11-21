/* Optional local-only browser verification, version-dispatched. */
const fs=require('fs'),path=require('path');
const dir=path.resolve(process.argv[2]||'output');
const spec=JSON.parse(fs.readFileSync(path.join(dir,'diagram.json'),'utf8'));
if(spec.schema_version!=='0.5'){require('./browser_export_v04.cjs');}else{
(async()=>{
 const args=process.argv.slice(3);let browser;
 for(let i=0;i<args.length;i+=2){if(args[i]==='--browser')browser=args[i+1];else throw Error('For 0.5, embed fonts with Python --embed-font after checking the license');}
 const {chromium}=require('playwright');const b=await chromium.launch({headless:true,...(browser?{executablePath:browser}:{})});
 try{
  const page=await b.newPage({viewport:{width:1920,height:1200}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.route('**/*',r=>{const u=r.request().url();if(u.startsWith('file:')||u.startsWith('data:'))r.continue();else r.abort();});
  await page.goto('file://'+path.join(dir,'diagram.html'));await page.evaluate(()=>document.fonts.ready);await page.addStyleTag({content:'svg{width:1920px!important;height:1080px!important;max-height:none!important}'});
  const checkpoints=[];let t=0;
  for(let i=0;i<spec.story.steps.length;i++){
   const s=await page.evaluate(t=>EWDiagram.renderAt(t),t);if(s.index!==i)throw Error('Incorrect timeline step');
   await page.locator('svg').screenshot({path:path.join(dir,`browser-step-${i+1}.png`)});checkpoints.push(s);t+=spec.story.steps[i].duration??3;
  }
  await page.evaluate(()=>EWDiagram.renderAt(0));await page.locator('#next').click();if(Number(await page.locator('[data-progress]').textContent())!==(spec.story.steps.length>1?2:1))throw Error('Next failed');await page.locator('#prev').click();if(Number(await page.locator('[data-progress]').textContent())!==1)throw Error('Previous failed');await page.locator('#speed').selectOption('2');await page.locator('#play').click();await page.locator('#play').click();await page.locator('#motion').check();await page.locator('#reset').click();
  const visible=await page.evaluate(()=>EWDiagram.data.spec.graph.nodes.every(n=>{const x=document.querySelector('[data-target="'+n.id+'"]');return !!x&&getComputedStyle(x).visibility!=='hidden';}));if(!visible||errors.length)throw Error('Visibility/script error '+errors);
  const file=path.join(dir,'capability-report.json');const report=JSON.parse(fs.readFileSync(file));report.html_browser_tested=true;report.browser_checks={controls:true,all_nodes_visible:true,offline:true,checkpoints,visual_review:'pending'};fs.writeFileSync(file,JSON.stringify(report,null,2));console.log('Offline browser checks passed; manually inspect browser-step PNGs.');
 }finally{await b.close();}
})().catch(e=>{console.error(e.message);process.exitCode=1;});}
