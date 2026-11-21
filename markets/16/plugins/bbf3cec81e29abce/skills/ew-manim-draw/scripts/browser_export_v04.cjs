/* Optional Playwright exporter; no network required at render time. */
const fs=require('fs'),path=require('path');
async function main(){
 const dir=path.resolve(process.argv[2]||'output'),args=process.argv.slice(3);let font,browser;
 for(let i=0;i<args.length;i+=2){if(args[i]==='--font')font=args[i+1];else if(args[i]==='--browser')browser=args[i+1];else throw Error('Unknown argument');}
 const {chromium}=require('playwright');const b=await chromium.launch({headless:true,...(browser?{executablePath:browser}:{})});
 try{const page=await b.newPage({viewport:{width:1920,height:1200},deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(e.message));
 // Inline only user-authorized licensed font, never add it to the skill package.
 if(font){const bytes=fs.readFileSync(font);if(bytes.length>32*1024*1024)throw Error('Font exceeds 32 MB');let html=fs.readFileSync(path.join(dir,'diagram.html'),'utf8');let layout=JSON.parse(fs.readFileSync(path.join(dir,'layout.json')));let family=layout.font_family.replace(/["\\<>]/g,'');let css=`<style>@font-face{font-family:"${family}";src:url(data:font/otf;base64,${bytes.toString('base64')})}</style>`;html=html.replace('</style>','</style>'+css);fs.writeFileSync(path.join(dir,'diagram.html'),html);}
 await page.route('**/*',r=>{const u=r.request().url();if(u.startsWith('file:')||u.startsWith('data:'))r.continue();else r.abort();});
 await page.goto('file://'+path.join(dir,'diagram.html'));await page.evaluate(()=>document.fonts.ready);
 await page.addStyleTag({content:'svg{width:1920px!important;height:1080px!important;max-height:none!important}'});
 const steps=await page.evaluate(()=>EWDiagram.data.spec.story.steps.length);let checkpoints=[];
 for(let i=0;i<steps;i++){const state=await page.evaluate(index=>{const a=EWDiagram.data.spec.story.steps;const t=a.slice(0,index).reduce((s,x)=>s+x.duration,0);return EWDiagram.renderAt(t);},i);if(state.index!==i)throw Error('Incorrect timeline step');await page.locator('svg').screenshot({path:path.join(dir,`step-${i+1}.png`)});checkpoints.push(state);}
 await page.evaluate(()=>EWDiagram.renderAt(0));await page.locator('svg').screenshot({path:path.join(dir,'diagram.png')});
 await page.locator('#next').click();if((await page.locator('#progress').textContent())!==`2 / ${steps}`&&steps>1)throw Error('Next failed');await page.locator('#prev').click();await page.locator('#speed').selectOption('2');await page.locator('#play').click();await page.locator('#play').click();await page.locator('#motion').check();await page.locator('#reset').click();
 const visible=await page.evaluate(()=>EWDiagram.data.spec.graph.nodes.every(n=>{const x=document.getElementById(n.id);return !!x&&getComputedStyle(x).visibility!=='hidden';}));if(!visible||errors.length)throw Error('Visibility or script error: '+errors);
 const reportPath=path.join(dir,'capability-report.json'),r=JSON.parse(fs.readFileSync(reportPath));for(const x of ['json','svg','html','png'])r.formats[x]={implemented:true,dependency_available:true,produced:true,checked:true};r.checks={html_controls:true,all_nodes_visible:true,offline:true,checkpoints,visual_review:'pending',font_embedded:!!font};fs.writeFileSync(reportPath,JSON.stringify(r,null,2));console.log('PNG exported; offline timeline/control checks passed; inspect step PNGs visually.');
 }finally{await b.close();}
}
main().catch(e=>{console.error(e.message);process.exitCode=1;});
