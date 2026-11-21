export const MAX_AGE = 150000;
export function validateSnapshot(value, now=Date.now()) {
  if(!value || !Number.isFinite(value.checkedAt) || value.checkedAt>now+60000 || value.checkedAt<now-120000) throw Error('A fresh reading is required.');
  if(typeof value.accountKey!=='string'||!/^[a-z0-9_-]{1,64}$/i.test(value.accountKey))throw Error('Invalid account key.');
  if(!Array.isArray(value.buckets)||value.buckets.length<1||value.buckets.length>16)throw Error('Invalid usage windows.');
  const ids=new Set();
  const buckets=value.buckets.map(b=>{
    if(typeof b.id!=='string'||b.id.length>100||ids.has(b.id))throw Error('Invalid window ID.');ids.add(b.id);
    if(typeof b.label!=='string'||b.label.length>100)throw Error('Invalid label.');
    if(!Number.isFinite(b.used)||b.used<0||b.used>100||!Number.isFinite(b.windowMinutes)||b.windowMinutes<=0||b.windowMinutes>525600||!Number.isFinite(b.reset)||b.reset<now-86400000||b.reset>now+366*86400000)throw Error('Invalid usage values.');
    return {id:b.id,label:b.label,used:b.used,remaining:100-b.used,windowMinutes:b.windowMinutes,reset:b.reset};
  });
  return {checkedAt:value.checkedAt,accountKey:value.accountKey,buckets};
}
export function mergeSnapshot(previous, data, now=Date.now()) {
  if(previous?.data?.checkedAt>=data.checkedAt)return previous;
  data=stableWindows(previous,data);
  const same=previous?.data?.accountKey===data.accountKey, history={};
  for(const b of data.buckets){const k=`${data.accountKey}:${b.id}:${b.reset}`;const points=same?(previous.history?.[k]||[]):[];const last=points.at(-1);history[k]=[...points];if(!last||last.remaining!==b.remaining||data.checkedAt-last.at>=300000)history[k].push({at:data.checkedAt,remaining:b.remaining});}
  return {version:2,receivedAt:now,data,history};
}
export function stableWindows(previous,data){
  if(previous?.data?.accountKey!==data.accountKey)return data;
  return {...data,buckets:data.buckets.map(b=>{const old=previous.data.buckets.find(p=>p.id===b.id&&p.windowMinutes===b.windowMinutes&&Math.abs(p.reset-b.reset)<=60000);return old?{...b,reset:old.reset}:b;})};
}
export function periods(snapshot){
  if(!snapshot?.data)return [];
  return snapshot.data.buckets.map(b=>({...b,accountKey:snapshot.data.accountKey,points:snapshot.history?.[`${snapshot.data.accountKey}:${b.id}:${b.reset}`]||[]}));
}
export function finishedPeriods(previous,data){
  return periods(previous).filter(p=>p.accountKey!==data.accountKey||!data.buckets.some(b=>b.id===p.id&&b.reset===p.reset));
}
export function archiveKey(p){return `pace/periods/${p.accountKey}/${String(9999999999999-p.reset).padStart(13,'0')}-${encodeURIComponent(p.id)}.json`;}
export function reading(snapshot,now=Date.now()) {
  if(!snapshot?.data)return {status:'connecting',data:null,error:'Waiting for the desktop sync service.',nextRefreshMs:60000};
  const fresh=now-snapshot.data.checkedAt<=MAX_AGE;
  return {status:fresh?'live':'stale',data:{...snapshot.data,history:snapshot.history},receivedAt:snapshot.receivedAt,error:fresh?null:'Sync paused. Your PC may be asleep or offline. Showing the last successful reading.',nextRefreshMs:60000};
}
