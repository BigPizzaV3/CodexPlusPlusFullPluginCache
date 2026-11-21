'use strict';
const $=id=>document.getElementById(id),HOUR=3600000,STORE='pace-v2',API='/api/usage';
const fmt=(v,d=1)=>Number(v).toLocaleString(undefined,{maximumFractionDigits:d});
const time=t=>new Date(t).toLocaleTimeString([],{hour:'numeric',minute:'2-digit'});
const escapeHTML=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let saved={prefs:{reserve:0,workHours:0},plans:{},history:{},selected:null};
try{const s=JSON.parse(localStorage.getItem(STORE));if(s&&s.prefs&&s.plans&&s.history)saved=s;}catch{}
let live=null,connection='connecting',error='',demo=false,demoData=null,busy=false,focusEnd=0,lastChart=0,archive=[],historyError='',historyView='current',chartView='week';
function persist(){try{localStorage.setItem(STORE,JSON.stringify(saved))}catch{toast('Browser storage is unavailable. Preferences will last for this session.')}}
function toast(message){$('toast').textContent=message;$('toast').hidden=false;setTimeout(()=>$('toast').hidden=true,4500)}
function data(){return demo?demoData:live}
function selected(){const d=data();return d?.buckets.find(b=>b.id===saved.selected)||d?.buckets.find(b=>b.windowMinutes===10080)||d?.buckets[0]}
function key(b){return `${demo?'demo':data()?.accountKey||'account'}:${b.id}:${b.sourceReset??b.reset}`}
function plannedBucket(b){
 if(!b)return b;
 const override=saved.resetOverrides?.[key(b)],start=b.reset-b.windowMinutes*60000;
 return override&&Number.isFinite(override.at)&&override.at>start?{...b,sourceReset:b.reset,sourceWindowMinutes:b.windowMinutes,reset:override.at,windowMinutes:(override.at-start)/60000,customReset:true}:b;
}
function getPlan(b){return {at:b.reset-b.windowMinutes*60000,remaining:100,reserve:0}}
function target(p,b,t){return Math.max(0,Math.min(100,(b.reset-t)/(b.windowMinutes*60000)*100))}
function label(b){const duration=b.windowMinutes===10080?'Weekly':b.windowMinutes===300?'5-hour':`${fmt(b.windowMinutes/60)}-hour`;return `${b.label==='codex'?'Codex':b.label} · ${duration}`}
function accept(result){const prior=live;live=result;const now=result.checkedAt;for(const b of result.buckets){const k=`${result.accountKey||'account'}:${b.id}:${b.reset}`;if(!saved.plans[k]){const first=result.history?.[k]?.[0];saved.plans[k]={at:first?.at||now,remaining:first?.remaining??b.remaining,reserve:Math.min(saved.prefs.reserve,b.remaining)};}const cloudHistory=result.history?.[k];const hist=Array.isArray(cloudHistory)&&cloudHistory.length?cloudHistory.slice():(saved.history[k]||[]);const last=hist.at(-1);if(!last||last.remaining!==b.remaining||now-last.at>=5*60000)hist.push({at:now,remaining:b.remaining});saved.history[k]=hist;}
 const all=Object.keys(saved.plans);if(all.length>20){for(const k of all.slice(0,-20)){delete saved.plans[k];delete saved.history[k]}}
 if(prior&&selected()&&prior.buckets.find(b=>b.id===selected().id)?.reset!==selected().reset)toast('A new allowance period is ready. Your plan has restarted automatically.');persist();}
function windowMenu(){const d=data();if(!d)return;const b=selected();const options=d.buckets.map(x=>`<option value="${escapeHTML(x.id)}">${escapeHTML(label(x))}</option>`).join('');if($('windowSelect').innerHTML!==options)$('windowSelect').innerHTML=options;if(b)$('windowSelect').value=b.id;}
async function sync(){if(busy||demo)return;busy=true;$('refresh').disabled=true;try{const response=await fetch(API,{headers:{'X-Pace-Client':'pace-v2'},cache:'no-store',signal:AbortSignal.timeout(25000)});if(!response.ok)throw Error('Desktop connection is unavailable.');const payload=await response.json();if(!payload||!['live','stale','connecting'].includes(payload.status))throw Error('Unexpected connection response.');if(payload.data?.buckets?.length)accept(payload.data);connection=payload.status;error=payload.error||'';try{const h=await fetch('/api/history',{headers:{'X-Pace-Client':'pace-v2'},cache:'no-store',signal:AbortSignal.timeout(15000)});if(!h.ok)throw Error();archive=(await h.json()).periods||[];historyError='';}catch{historyError='Saved history could not load. Try Refresh.';}}catch(e){connection=live?'stale':'offline';error='Unable to reach your local tracker. Ask Codex to Start Orbit.';}finally{busy=false;$('refresh').disabled=false;windowMenu();render(true)}}
function render(force=false){const d=data(),b=plannedBucket(selected()),now=Date.now(),stale=!demo&&(connection!=='live'||!d||now-d.checkedAt>150000);$('connectPanel').hidden=demo||(Boolean(d)&&connection!=='offline');$('demoBanner').hidden=!demo;$('led').className=!stale&&!demo?'live':'';$('connectionText').textContent=demo?'Demo mode':connection==='connecting'?'Waiting for sync':stale?d?'Connection paused':'Sync unavailable':'Live from Codex';$('lastSync').textContent=demo?'Sample data only':d?`${stale?'Last reading':'Synced'} ${Math.max(0,Math.floor((now-d.checkedAt)/1000))}s ago`:'Waiting for a reading from your PC';$('footerStatus').textContent=demo?'Demo preview · not connected to an account':error||'Local tracking · updates every 60 seconds';$('refresh').disabled=busy||demo;
 $('resetOverrideOpen').disabled=!b;$('resetOverrideOpen').textContent=b?.customReset?'Edit reset time':'Set reset time';if(!b){$('targetRemaining').innerHTML='—<span>%</span>';$('targetDifference').textContent='Waiting for the reset time';$('chartEmpty').hidden=false;$('chart').innerHTML='';$('milestones').innerHTML='';$('remaining').innerHTML='—<span>%</span>';$('used').textContent='Waiting for your balance';$('balanceCaption').textContent='Waiting for the local tracker';$('ring').style.strokeDashoffset=351.86;$('hourly').innerHTML='—<small>% / hour</small>';$('rateCaption').textContent='Waiting for a live reading';$('quarter').textContent='Your next move appears here.';$('countdown').textContent='—';$('resetDate').textContent='Your reset time comes from Codex';$('timeBar').style.width='0%';$('paceBadge').textContent='Waiting for data';$('insight').textContent='100% at the start. 0% at reset. Your actual balance alongside it.';$('sessionTarget').textContent='Make space for focused work.';$('sessionDetail').textContent='Your session budget appears after the next sync.';$('focusButton').disabled=true;return}const p=getPlan(b),remaining=b.remaining,elapsed=Math.max(0,(b.reset-now)/HOUR),expired=elapsed===0,reserve=Math.min(saved.prefs.reserve,remaining),usable=Math.max(0,remaining-reserve),hours=saved.prefs.workHours>0?Math.min(elapsed,saved.prefs.workHours):elapsed,rate=hours>0?usable/hours:0,blocked=stale||expired;
 $('remaining').innerHTML=fmt(remaining)+'<span>%</span>';$('used').textContent=`${fmt(b.used)}% of your allowance used`;$('balanceCaption').textContent=stale?'Last known balance · connection paused':demo?'Illustrative sample balance':'Balance synced automatically';$('ring').style.strokeDashoffset=351.86*(1-remaining/100);
 $('hourly').innerHTML=blocked?'—<small>% / hour</small>':fmt(rate,2)+'<small>% / hour</small>';$('rateCaption').textContent=expired?'Waiting for a fresh reset reading':stale?'Waiting for a fresh local reading':saved.prefs.workHours>0?`Across ${fmt(hours)} planned working hours`:'Of your full allowance, each hour';$('quarter').textContent=blocked?'Targets resume after the tracker gets a fresh reading.':usable===0?'Reserve reached. You’re right on budget.':`Use about ${fmt(Math.min(usable,rate*.25),2)}% in the next ${Math.min(15,Math.ceil(hours*60))} min`;
 const minutes=Math.ceil(elapsed*60),days=Math.floor(minutes/1440),h=Math.floor(minutes%1440/60),m=minutes%60;$('countdown').innerHTML=expired?'Reset reached':`${days?days+'<small>d</small> ':''}${h}<small>h</small> ${m}<small>m</small>`;$('resetDate').textContent=(b.customReset?'Planned - ':'')+new Date(b.reset).toLocaleString([],{weekday:'short',month:'short',day:'numeric',hour:'numeric',minute:'2-digit'});$('timeBar').style.width=`${Math.max(0,Math.min(100,100-elapsed*60/b.windowMinutes*100))}%`;
 const ideal=target(p,b,now),gap=remaining-ideal;
 $('targetRemaining').innerHTML=fmt(ideal)+'<span>%</span>';
 $('targetDifference').textContent=stale?'Comparison paused · last balance is stale':`${fmt(Math.abs(gap))} percentage points ${gap>=0?'above':'below'} target`;
 $('targetCaption').textContent=`${fmt(100-ideal)}% should be used by now`;
 $('paceBadge').textContent=stale?'Reading is stale':expired?'Awaiting reset':Math.abs(gap)<.75?'On target':gap>0?'Room to use more':'Using too fast';
 $('insight').textContent=blocked?'Showing your last recorded balance. Keep this computer awake for live updates.':`Target: ${fmt(ideal)}% remaining now. Actual: ${fmt(remaining)}%. ${gap>.75?'You have room to use more.':gap<-.75?'You are using allowance faster than even pacing.':'You are following the target closely.'}`;
 $('planSummary').textContent=saved.prefs.reserve===0?'Use it all. Finish at reset.':`Finish with ${saved.prefs.reserve}% in reserve.`;$('planDetail').textContent=`${saved.prefs.reserve}% reserve · ${saved.prefs.workHours?fmt(saved.prefs.workHours)+' working hours':'all remaining time'}`;
 $('sessionTarget').textContent=blocked?'Waiting for a fresh reading.':`A ${fmt(Math.min(usable,rate*.5),2)}% budget for your next session.`;$('sessionDetail').textContent=blocked?'Keep this computer awake to resume syncing.':'30 minutes of focus, paced to your allowance.';
 if(focusEnd>now){const secs=Math.ceil((focusEnd-now)/1000);$('focusButton').textContent=`${Math.floor(secs/60)}:${String(secs%60).padStart(2,'0')} remaining`;$('focusCancel').hidden=false;}else{if(focusEnd){focusEnd=0;toast('Session complete. Time for a breather.');}$('focusButton').textContent='Start focus timer';$('focusCancel').hidden=true;}$('focusButton').disabled=blocked;
 if(force||now-lastChart>10000){draw(b,p,now);lastChart=now;}}
const dateLabel=t=>new Date(t).toLocaleDateString([],{month:'short',day:'numeric'});
// Exact 24-hour blocks anchored to the allowance period's reset, independent of timezone.
function dayWindow(b,now){const begin=b.reset-b.windowMinutes*60000,day=86400000;const index=Math.max(0,Math.min(Math.ceil((b.reset-begin)/day)-1,Math.floor((now-begin)/day)));const start=begin+index*day;return {start,end:start+day};}
function dayChartData(b,points,now){
 const {start,end}=dayWindow(b,now),begin=b.reset-b.windowMinutes*60000;
 const from=Math.max(start,begin),to=Math.min(end,b.reset);
 const visible=points.filter(v=>v.at>=from&&v.at<=to&&v.at<=now);
 const levels=from<=to?[target(null,b,from),target(null,b,to),...visible.map(v=>v.remaining)]:[0,100];
 let lo=Math.max(0,Math.floor((Math.min(...levels)-1)/2)*2),hi=Math.min(100,Math.ceil((Math.max(...levels)+1)/2)*2);
 if(hi-lo<6){lo=Math.max(0,hi-6);hi=Math.min(100,lo+6);}
 return {start,end,from,to,visible,lo,hi};
}
function draw(b,p,now){
 $('dayView').setAttribute('aria-pressed',String(chartView==='day'));$('weekView').setAttribute('aria-pressed',String(chartView==='week'));
 $('historyView').parentElement.hidden=chartView==='day';
 if(chartView==='day')drawDay(b,now);else{$('chartRange').textContent='Full period · 100% → 0%';drawWeek(b,p,now);}
}
function gapLines(points,x,y){return points.slice(1).map((v,i)=>{const prev=points[i];return v.at-prev.at>600000?`<path d="M${x(prev.at)} ${y(prev.remaining)} L${x(v.at)} ${y(v.remaining)}" fill="none" stroke="#b9d5df" stroke-width="2" stroke-dasharray="3 6" opacity=".65"><title>Change while tracking was offline; exact timing unknown</title></path>`:'';}).join('');}
function drawDay(b,now){
 const source=demo?[{at:data().checkedAt,remaining:b.remaining}]:saved.history[key(b)]||[];
 const {start,end,from,to,visible,lo,hi}=dayChartData(b,source,now),narrow=window.matchMedia('(max-width:560px)').matches,right=narrow?405:960;
 const x=t=>55+(t-start)/(end-start)*(right-55),y=v=>205-(v-lo)/(hi-lo)*180;
 $('chartEmpty').hidden=true;$('chart').setAttribute('viewBox',`0 0 ${narrow?430:1000} 255`);
 $('chartRange').textContent=`${dateLabel(start)} ${time(start)} to ${dateLabel(end)} ${time(end)} | zoomed ${fmt(lo)}-${fmt(hi)}%`;
 let svg='<title>24 hours anchored to your reset time. Zoomed remaining percentage scale. Dashed weekly target and recorded actual balance.</title>';
 for(let i=0;i<=4;i++){const v=lo+(hi-lo)*i/4;svg+=`<line x1="55" x2="${right}" y1="${y(v)}" y2="${y(v)}" stroke="#34303f"/><text x="43" y="${y(v)+5}" text-anchor="end">${fmt(v)}%</text>`;}
 if(from<=to){svg+=`<path d="M${x(from)} ${y(target(null,b,from))} L${x(to)} ${y(target(null,b,to))}" fill="none" stroke="#d6ba83" stroke-width="3" stroke-dasharray="8 6"/>`;}
 svg+=gapLines(visible,x,y);let path='';visible.forEach((v,i)=>{const prev=visible[i-1];path+=!prev||v.at-prev.at>600000?`M${x(v.at)} ${y(v.remaining)}`:` H${x(v.at)} V${y(v.remaining)}`;});
 svg+=`<path d="${path}" fill="none" stroke="#b9d5df" stroke-width="3"/>`;
 for(const v of visible.filter((v,i)=>i===0||i===visible.length-1||v.at-visible[i-1].at>600000))svg+=`<circle cx="${x(v.at)}" cy="${y(v.remaining)}" r="4" style="fill:#b9d5df;stroke:none"><title>${fmt(v.remaining)}% · ${escapeHTML(time(v.at))}</title></circle>`;
 const resetAt=b.reset-b.windowMinutes*60000;
 if(resetAt>start&&resetAt<end)svg+=`<line x1="${x(resetAt)}" x2="${x(resetAt)}" y1="23" y2="207" stroke="#685c81" stroke-dasharray="2 6"/>`;
 svg+=`<line x1="${x(now)}" x2="${x(now)}" y1="20" y2="210" stroke="#c7bfd6" stroke-dasharray="3 5"/><text x="${Math.min(right-15,Math.max(85,x(now)))}" y="14" text-anchor="middle">Now</text>`;
 const hours=narrow?[0,12,24]:[0,6,12,18,24];
 for(const hour of hours){const t=start+hour*3600000;svg+=`<text x="${x(t)}" y="239" text-anchor="${hour===0?'start':hour===24?'end':'middle'}">${escapeHTML(time(t))}</text>`;}
 $('chart').innerHTML=svg;
 $('historyNote').textContent=(demo?'Illustrative sample. ':historyError?historyError+' ':'')+`Each Day view covers 24 hours starting from your reset time, following the same weekly target. ${visible.length?'Solid blue shows saved readings. Dotted blue connects readings across a gap; exact timing is unknown.':'No readings recorded in this block yet.'}`;
 $('milestones').innerHTML='';
}
$('dayView').onclick=()=>{chartView='day';saved.chartView=chartView;persist();render(true)};
$('weekView').onclick=()=>{chartView='week';saved.chartView=chartView;persist();render(true)};
function drawWeek(b,p,now){
 $('chartEmpty').hidden=true;
 const current={...b,points:demo?[{at:data().checkedAt,remaining:b.remaining}]:(saved.history[key(b)]||[])};
 const previous=demo?[]:archive.filter(v=>v.id===b.id&&v.reset<=b.reset-b.windowMinutes*60000+60000&&v.windowMinutes===(b.sourceWindowMinutes??b.windowMinutes)).sort((a,b)=>b.reset-a.reset);
 const menu='<option value="current">This period</option><option value="long">Last 4 periods</option>'+previous.map(v=>`<option value="${v.reset}">Period ending ${escapeHTML(dateLabel(v.reset))}</option>`).join('');
 if($('historyView').innerHTML!==menu)$('historyView').innerHTML=menu;
 if(historyView!=='current'&&historyView!=='long'&&!previous.some(v=>String(v.reset)===historyView))historyView='current';
 $('historyView').value=historyView;
 const shown=historyView==='current'?[current]:historyView==='long'?[current,...previous.slice(0,3)].sort((a,b)=>a.reset-b.reset):previous.filter(v=>String(v.reset)===historyView);
 const start=Math.min(...shown.map(v=>v.reset-v.windowMinutes*60000)),end=Math.max(...shown.map(v=>v.reset)),span=Math.max(1,end-start);
 const narrow=window.matchMedia('(max-width:560px)').matches,right=narrow?405:960;
 $('chart').setAttribute('viewBox',`0 0 ${narrow?430:1000} 255`);
 const x=t=>55+(t-start)/span*(right-55),y=v=>205-v*1.8;
 let svg='<title>Target remaining falls from 100 percent to zero each period. Blue marks show recorded actual balances.</title>';
 for(let v=0;v<=100;v+=25)svg+=`<line x1="55" x2="${right}" y1="${y(v)}" y2="${y(v)}" stroke="#34303f"/><text x="40" y="${y(v)+5}" text-anchor="end">${v}%</text>`;
 for(const period of shown){
  const begin=period.reset-period.windowMinutes*60000;
  svg+=`<path d="M${x(begin)} ${y(100)} L${x(period.reset)} ${y(0)}" fill="none" stroke="#d6ba83" stroke-width="3" stroke-dasharray="8 6"/>`;
  const pts=period.points.filter(v=>v.at>=begin&&v.at<=period.reset);
  svg+=gapLines(pts,x,y);let path='';pts.forEach((v,i)=>{const prev=pts[i-1];path+=(!prev||v.at-prev.at>600000?`M${x(v.at)} ${y(v.remaining)}`:` H${x(v.at)} V${y(v.remaining)}`);});
  svg+=`<path d="${path}" fill="none" stroke="#b9d5df" stroke-width="3"/>`;
  // Points are real observations. Never extend a balance into missing time.
  for(const v of pts.filter((v,i)=>i===0||i===pts.length-1||!pts[i-1]||v.at-pts[i-1].at>600000))svg+=`<circle cx="${x(v.at)}" cy="${y(v.remaining)}" r="4" style="fill:#b9d5df;stroke:none"><title>${fmt(v.remaining)}% · ${escapeHTML(new Date(v.at).toLocaleString())}</title></circle>`;
 }
 if(now>=start&&now<=end)svg+=`<line x1="${x(now)}" x2="${x(now)}" y1="20" y2="210" stroke="#c7bfd6" stroke-dasharray="3 5"/><text x="${Math.min(right-15,Math.max(85,x(now)))}" y="14" text-anchor="middle">Now</text>`;
 const ticks=narrow?2:4;for(let i=0;i<=ticks;i++){const t=start+span*i/ticks;svg+=`<text x="${x(t)}" y="239" text-anchor="${i===0?'start':i===ticks?'end':'middle'}">${escapeHTML(b.windowMinutes<1440&&shown.length===1?time(t):dateLabel(t))}</text>`;}
 $('chart').innerHTML=svg;
 const actual=shown.flatMap(v=>v.points),first=actual.length?Math.min(...actual.map(v=>v.at)):null;
 $('historyNote').textContent=historyError||(demo?'Illustrative sample only.':first?`Recorded from ${new Date(first).toLocaleString([], {month:'short',day:'numeric',hour:'numeric',minute:'2-digit'})}. Dotted blue shows change across gaps, not the exact timing. Completed periods are saved automatically.`:'No readings recorded for this period yet.');
 $('milestones').innerHTML='';
}
function openResetOverride(){
 const b=selected();if(!b)return;
 const current=plannedBucket(b),local=new Date(current.reset-new Date(current.reset).getTimezoneOffset()*60000).toISOString().slice(0,16);
 $('resetTimeInput').value=local;$('resetTimeInput').setCustomValidity('');
 $('resetTimezone').textContent='Time zone: '+Intl.DateTimeFormat().resolvedOptions().timeZone;
 $('resetOverrideDialog').showModal();
}
$('resetOverrideOpen').onclick=openResetOverride;
$('resetOverrideCancel').onclick=()=>$('resetOverrideDialog').close();
$('resetTimeInput').oninput=()=>$('resetTimeInput').setCustomValidity('');
$('resetOverrideForm').onsubmit=e=>{
 e.preventDefault();const b=selected(),input=$('resetTimeInput'),at=new Date(input.value).getTime();
 if(!b||!Number.isFinite(at)||at<=Date.now()||at<=b.reset-b.windowMinutes*60000){input.setCustomValidity('Choose a future reset date and time.');input.reportValidity();return;}
 saved.resetOverrides??={};saved.resetOverrides[key(b)]={at};persist();historyView='current';render(true);$('resetOverrideDialog').close();toast('Plan updated for your announced reset.');
};
$('resetOverrideClear').onclick=()=>{const b=selected();if(b&&saved.resetOverrides)delete saved.resetOverrides[key(b)];persist();render(true);$('resetOverrideDialog').close();toast('Using the reset time detected by Codex.');};
$('historyView').onchange=()=>{historyView=$('historyView').value;render(true)};
function openSettings(){$('reserve').value=saved.prefs.reserve;$('workHours').value=saved.prefs.workHours;$('settings').showModal()}
$('settingsOpen').onclick=openSettings;$('planEdit').onclick=openSettings;$('connectionOpen').onclick=()=>$('connectionDialog').showModal();$('closeConnection').onclick=()=>$('connectionDialog').close();
$('preferences').addEventListener('submit',e=>{if(e.submitter?.value!=='save')return;saved.prefs={reserve:Number($('reserve').value),workHours:Number($('workHours').value)};const b=selected();if(b)saved.plans[key(b)]={at:Date.now(),remaining:b.remaining,reserve:Math.min(saved.prefs.reserve,b.remaining)};persist();render(true);toast('Your pacing plan has been updated.');});
$('windowSelect').onchange=()=>{saved.selected=$('windowSelect').value;persist();render(true)};$('refresh').onclick=sync;
$('demo').onclick=()=>{demo=true;const now=Date.now();demoData={checkedAt:now,buckets:[{id:'sample',label:'codex',used:83,remaining:17,windowMinutes:10080,reset:now+3.9*HOUR}]};saved.plans[key(demoData.buckets[0])]={at:now,remaining:17,reserve:Math.min(saved.prefs.reserve,17)};$('connectPanel').hidden=true;windowMenu();render(true)};
$('exitDemo').onclick=()=>{demo=false;demoData=null;windowMenu();render(true);sync()};$('focusButton').onclick=()=>{if(!focusEnd){focusEnd=Date.now()+30*60000;toast('Focus session started. Your allowance keeps syncing.');render()}};$('focusCancel').onclick=()=>{focusEnd=0;render();toast('Focus session ended.')};
if(location.hostname==='127.0.0.1')$('download').hidden=true;
window.addEventListener('online',sync);document.addEventListener('visibilitychange',()=>{if(!document.hidden)sync()});sync();setInterval(()=>{if(!demo)sync()},60000);setInterval(()=>render(),1000);
window.addEventListener('resize',()=>render(true));
