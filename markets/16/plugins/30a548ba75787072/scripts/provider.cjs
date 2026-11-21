const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const {spawn, execFileSync} = require('node:child_process');
const readline = require('node:readline');
const crypto = require('node:crypto');

let child=null, connecting=null, seq=0, last=null, failure=null, pending=new Map(), refreshing=null, lastAttempt=0;
function executable(){
  if(process.env.PACE_CODEX_PATH)return process.env.PACE_CODEX_PATH.endsWith('.js')||process.env.PACE_CODEX_PATH.endsWith('.cjs')?{file:process.execPath,args:[process.env.PACE_CODEX_PATH]}:{file:process.env.PACE_CODEX_PATH,args:[]};
  const dirs=(process.env.PATH||'').split(path.delimiter);
  for(const d of dirs){const exe=path.join(d,process.platform==='win32'?'codex.exe':'codex');if(fs.existsSync(exe))return {file:exe,args:[]};}
  const candidates=[process.env.APPDATA&&path.join(process.env.APPDATA,'npm/node_modules/@openai/codex/bin/codex.js')];
  try{candidates.push(path.join(execFileSync('npm'+(process.platform==='win32'?'.cmd':''),['root','-g'],{encoding:'utf8',windowsHide:true,timeout:5000,shell:process.platform==='win32'}).trim(),'@openai/codex/bin/codex.js'));}catch{}
  const js=candidates.find(p=>p&&fs.existsSync(p));if(js)return {file:process.execPath,args:[js]};
  throw Error('Install Codex CLI, sign in with your ChatGPT account, then restart Pace.');
}
function rpc(method,params){return new Promise((resolve,reject)=>{const id=++seq;const timeout=setTimeout(()=>{pending.delete(id);reject(Error('Usage connection timed out.'))},20000);pending.set(id,{resolve,reject,timeout});child.stdin.write(JSON.stringify({id,method,...(params?{params}:{})})+'\n');});}
async function connect(){
  if(connecting)return connecting;
  connecting=(async()=>{const cmd=executable();const p=spawn(cmd.file,[...cmd.args,'app-server','--listen','stdio://'],{windowsHide:true,stdio:['pipe','pipe','pipe']});child=p;
    const fail=()=>{if(child===p){child=null;connecting=null;}for(const v of pending.values()){clearTimeout(v.timeout);v.reject(Error('Codex connection closed. Restart Pace or sign in to Codex.'));}pending.clear();};
    p.on('error',fail);p.on('exit',fail);p.stderr.on('data',()=>{});p.stdin.on('error',()=>{});
    readline.createInterface({input:p.stdout}).on('line',line=>{let msg;try{msg=JSON.parse(line)}catch{return}if(pending.has(msg.id)){const item=pending.get(msg.id);pending.delete(msg.id);clearTimeout(item.timeout);if(msg.error)item.reject(Error('Codex could not read usage. Check that Codex CLI is signed in with ChatGPT.'));else item.resolve(msg.result);}else if(msg.method&&msg.id!=null){p.stdin.write(JSON.stringify({id:msg.id,error:{code:-32601,message:'Pace supports read-only usage requests only.'}})+'\n');}});
    await rpc('initialize',{clientInfo:{name:'pace_desktop',title:'Pace',version:'0.2.0'}});p.stdin.write(JSON.stringify({method:'initialized'})+'\n');
  })();try{await connecting}catch(e){connecting=null;if(child){child.stdin.end();child.kill();child=null;}throw e;}
}
function normalize(result,now=Date.now()){
  const source=result.rateLimitsByLimitId??(result.rateLimits?{[result.rateLimits.limitId||'codex']:result.rateLimits}:{});
  const buckets=[];
  for(const [id,b] of Object.entries(source)){for(const key of ['primary','secondary']){const w=b[key];if(!w||!Number.isFinite(w.usedPercent)||!Number.isFinite(w.windowDurationMins)||!Number.isFinite(w.resetsAt)||w.windowDurationMins<=0)continue;buckets.push({id:id+':'+key,label:b.limitName||id,used:Math.min(100,Math.max(0,w.usedPercent)),remaining:Math.min(100,Math.max(0,100-w.usedPercent)),windowMinutes:w.windowDurationMins,reset:w.resetsAt*1000});}}
  return {checkedAt:now,accountKey:typeof result.accountId==='string'?crypto.createHash('sha256').update(result.accountId).digest('hex').slice(0,16):'local',buckets};
}

function accountKey(a){const v=a?.account;if(v?.type!=='chatgpt'||!(v.id||v.email))throw Error('Sign in to Codex CLI with your ChatGPT account.');return crypto.createHash('sha256').update(String(v.id||v.email).trim().toLowerCase()).digest('hex').slice(0,32);}
async function readUsage(){try{await connect();const before=accountKey(await rpc('account/read',{refreshToken:false}));const raw=await rpc('account/rateLimits/read');const after=accountKey(await rpc('account/read',{refreshToken:false}));if(before!==after)throw Error('Account changed. Waiting for the next reading.');const value=normalize(raw);value.accountKey=crypto.createHash('sha256').update(before+':'+(raw.accountId||'default')).digest('hex').slice(0,32);if(!value.buckets.length)throw Error('No subscription usage windows returned.');return value;}finally{if(child){child.stdin.end();child.kill();child=null;}connecting=null;}}
function close(){if(child){child.stdin.end();child.kill();child=null;}connecting=null;}
module.exports={readUsage,accountKey,close};
