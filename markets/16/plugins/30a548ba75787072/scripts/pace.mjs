import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import http from 'node:http';
import crypto from 'node:crypto';
import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {readUsage,close} from './provider.cjs';
import {configureStartup,startupSettings,pauseStartup} from './startup.mjs';
import {mergeSnapshot,finishedPeriods,periods,reading,validateSnapshot} from '../lib/usage-sync.mjs';

const root=fileURLToPath(new URL('../',import.meta.url));
const base=process.env.PACE_DATA_DIR||path.join(process.platform==='win32'?(process.env.LOCALAPPDATA||os.tmpdir()):process.platform==='darwin'?path.join(os.homedir(),'Library','Application Support'):(process.env.XDG_DATA_HOME||path.join(os.homedir(),'.local','share')),'PacePlugin');
const runtime=path.join(base,'runtime.json');
const pause=ms=>new Promise(resolve=>setTimeout(resolve,ms));
async function readJSON(file){try{return JSON.parse(await fs.readFile(file,'utf8'));}catch(e){if(e.code==='ENOENT')return null;throw Error('Orbit could not read its saved data. Back up the data folder before repairing it.');}}
async function saveJSON(file,value){await fs.mkdir(path.dirname(file),{recursive:true,mode:0o700});const temp=file+'.tmp-'+process.pid;await fs.writeFile(temp,JSON.stringify(value),{mode:0o600});await fs.rename(temp,file);}
function periodFile(p){return `${String(9999999999999-p.reset).padStart(13,'0')}-${crypto.createHash('sha256').update(p.id).digest('hex').slice(0,20)}.json`;}
async function active(){const r=await readJSON(runtime);if(!r||!Number.isInteger(r.port)||r.port<1||r.port>65535)return null;try{const response=await fetch(`http://127.0.0.1:${r.port}/health`,{headers:{'X-Pace-Control':r.token},signal:AbortSignal.timeout(1500)});if(!response.ok)return null;const status=await response.json();return status.app==='pace-plugin'?{...r,...status}:null;}catch{return null;}}

async function serve(){
 await fs.mkdir(base,{recursive:true,mode:0o700});
 const token=crypto.randomBytes(32).toString('hex');let snapshot=null,error='Connecting to your Codex account.',refreshing=null,origin='',closing=false;
 async function refresh(){if(refreshing)return refreshing;refreshing=(async()=>{try{
  const data=validateSnapshot(await readUsage());const folder=path.join(base,'accounts',data.accountKey);const latest=path.join(folder,'latest.json');const previous=await readJSON(latest);const next=mergeSnapshot(previous,data);
  for(const p of finishedPeriods(previous,next.data))await saveJSON(path.join(folder,'periods',periodFile(p)),p);
  await saveJSON(latest,next);snapshot=next;error='';
 }catch(e){snapshot=null;error=e.message||'Unable to read Codex usage.';}finally{refreshing=null;}})();return refreshing;}
 const json=(res,code,data)=>{res.writeHead(code,{'Content-Type':'application/json','Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});res.end(JSON.stringify(data));};
 const server=http.createServer(async(req,res)=>{try{
  if(req.headers.host!==new URL(origin).host||req.headers.origin&&req.headers.origin!==origin){return json(res,403,{error:'Local Orbit requests only.'});}
  const url=new URL(req.url,origin);
  if(url.pathname==='/health'&&req.method==='GET'&&req.headers['x-pace-control']===token)return json(res,200,{app:'pace-plugin',url:origin,status:snapshot?'tracking':'connecting',error});
  if(url.pathname==='/stop'&&req.method==='POST'&&req.headers['x-pace-control']===token){json(res,200,{stopped:true});return stop();}
  if(req.method!=='GET')return json(res,405,{error:'Method not allowed.'});
  if(url.pathname.startsWith('/api/')){
   if(req.headers['x-pace-client']!=='pace-v2')return json(res,403,{error:'Orbit client required.'});
   if(url.pathname==='/api/usage')return json(res,200,snapshot?reading(snapshot):{status:'connecting',data:null,error,nextRefreshMs:60000});
   if(url.pathname==='/api/history'){
    if(!snapshot)return json(res,200,{periods:[]});
    const selected=snapshot;const folder=path.join(base,'accounts',selected.data.accountKey,'periods');let files=[];try{files=(await fs.readdir(folder)).filter(f=>/^\d{13}-[a-f0-9]{20}\.json$/.test(f)).sort().slice(0,52);}catch(e){if(e.code!=='ENOENT')throw e;}
    const old=await Promise.all(files.map(f=>readJSON(path.join(folder,f))));return json(res,200,{periods:[...periods(selected),...old.filter(Boolean)]});
   }
   return json(res,404,{error:'Not found.'});
  }
  const files={'/':'index.html','/index.html':'index.html','/app.js':'app.js','/style.css':'style.css','/icon.svg':'icon.svg','/saturn.png':'saturn.png','/heading.ttf':'heading.ttf'};const name=files[url.pathname];if(!name)return json(res,404,{error:'Not found.'});
  const mime=name.endsWith('.png')?'image/png':name.endsWith('.ttf')?'font/ttf':name.endsWith('.js')?'text/javascript':name.endsWith('.css')?'text/css':name.endsWith('.svg')?'image/svg+xml':'text/html';const bytes=await fs.readFile(path.join(root,'web',name));
  res.writeHead(200,{'Content-Type':mime+'; charset=utf-8','Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Content-Security-Policy':"default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'"});res.end(bytes);
 }catch{json(res,500,{error:'Orbit could not read its local data.'});}});
 const interval=setInterval(refresh,60000);
 async function stop(){if(closing)return;closing=true;clearInterval(interval);close();server.close();server.closeAllConnections();try{if((await readJSON(runtime))?.token===token)await fs.unlink(runtime);}catch{}process.exit(0);}
 process.on('SIGINT',stop);process.on('SIGTERM',stop);
 await new Promise((resolve,reject)=>{server.once('error',reject);server.listen(0,'127.0.0.1',resolve);});
 origin=`http://127.0.0.1:${server.address().port}`;await saveJSON(runtime,{port:server.address().port,token,pid:process.pid});await refresh();
}

async function main(){
 if(Number(process.versions.node.split('.')[0])<22)throw Error('Orbit needs Node.js 22 or newer.');
 const command=process.argv[2]||'status';
 if(command==='enable-startup'){
  const settings=await configureStartup(root,base,true);
  const child=spawn(process.execPath,[settings.script,'supervise'],{detached:true,windowsHide:true,stdio:'ignore',env:process.env});child.unref();
  console.log(JSON.stringify({startupEnabled:true,message:'Orbit starts at Windows sign-in and recovers if its tracker stops. Stop Orbit pauses until the next sign-in. Disable Orbit startup removes automatic startup.'}));return;
 }
 if(command==='disable-startup'){console.log(JSON.stringify(await configureStartup(root,base,false)));return;}
 if(command==='supervise'||command==='resume-startup'){
  if(command==='resume-startup')await pauseStartup(base,false);
  const lockFile=path.join(base,'supervisor.json');await fs.mkdir(base,{recursive:true});
  let lock;
  try{lock=await fs.open(lockFile,'wx');}
  catch(e){
   if(e.code!=='EEXIST')throw e;
   const old=await readJSON(lockFile);try{process.kill(old.pid,0);return;}catch(e){if(e.code!=='ESRCH')return;}
   await fs.unlink(lockFile);try{lock=await fs.open(lockFile,'wx');}catch{return;}
  }
  await lock.writeFile(JSON.stringify({pid:process.pid}));await lock.close();
  try{while(true){
   const settings=await startupSettings(base);if(!settings.enabled||settings.paused)break;
   if(!await active()){
    const child=spawn(process.execPath,[settings.script,'serve'],{detached:true,windowsHide:true,stdio:'ignore',env:process.env});child.unref();
   }
   await pause(5000);
  }}finally{try{if((await readJSON(lockFile))?.pid===process.pid)await fs.unlink(lockFile);}catch{}}
  return;
 }
 if(command==='serve')return serve();
 if(command==='start'){
  await pauseStartup(base,false);
  let r=await active();if(!r){await fs.mkdir(base,{recursive:true,mode:0o700});const child=spawn(process.execPath,[fileURLToPath(import.meta.url),'serve'],{detached:true,windowsHide:true,stdio:'ignore',env:process.env});child.unref();for(let i=0;i<60&&!r;i++){await pause(250);r=await active();}}
  if(!r)throw Error('Orbit did not start. Check Node.js and the data-folder permissions.');
  const settings=await startupSettings(base);if(settings.enabled){const child=spawn(process.execPath,[settings.script,'supervise'],{detached:true,windowsHide:true,stdio:'ignore',env:process.env});child.unref();}
  console.log(JSON.stringify({running:true,url:r.url,status:r.status,error:r.error,dataDirectory:base}));return;
 }
 const r=await active();
 if(command==='stop'){await pauseStartup(base,true);if(r)await fetch(r.url+'/stop',{method:'POST',headers:{'X-Pace-Control':r.token},signal:AbortSignal.timeout(3000)});console.log(JSON.stringify({stopped:true}));return;}
 if(command==='status'){if(!r){console.log(JSON.stringify({running:false}));return;}const response=await fetch(r.url+'/api/usage',{headers:{'X-Pace-Client':'pace-v2'},signal:AbortSignal.timeout(3000)});const result=await response.json();console.log(JSON.stringify({running:true,url:r.url,...result}));return;}
 throw Error('Use start, status, or stop.');
}
main().catch(e=>{console.error(e.message);process.exitCode=1;});
