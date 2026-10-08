import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import {createFaultController} from '../assets/harness/fault-controller.mjs';
import {createMockHass} from '../assets/harness/mock-hass.mjs';
import {generateSequence,runModelSequence,minimizeFailure} from '../assets/harness/sequence-engine.mjs';
import {assessTemporalTrace} from '../assets/harness/temporal-oracles.mjs';
import {createBrowserHelpers} from '../assets/harness/browser-helpers.mjs';

const ticks=async()=>{for(let i=0;i<12;i++) await Promise.resolve();};
const setup=()=>{
  const faults=createFaultController();
  const mock=createMockHass({faults,store:{records:[]},api:{'POST record':{mutation:true,
    handle:(body,store)=>{store.records.push(body);return {saved:body};}}}});
  return {faults,mock};
};

test('held writes execute and resolve in explicitly reversed order',async()=>{
  const {faults,mock}=setup();
  for(let i=0;i<2;i++) faults.arm({surface:'api',key:'POST record',mode:'hold-before'});
  const a=mock.hass.callApi('post','record','A'),b=mock.hass.callApi('post','record','B');
  assert.deepEqual(mock.store.records,[]);
  const [first,second]=faults.snapshot().pending;
  await faults.release(second.id);assert.deepEqual(await b,{saved:'B'});
  assert.deepEqual(mock.store.records,['B']);
  await faults.release(first.id);await a;
  assert.deepEqual(mock.store.records,['B','A']);
  assert.deepEqual(mock.intents.map(i=>i.status),['fulfilled','fulfilled']);
  assert.equal(faults.snapshot().pending.length,0);
});

test('held acknowledgment preserves a completed commit without executing it twice',async()=>{
  const {faults,mock}=setup();faults.arm({surface:'api',key:'POST record',mode:'hold-after'});
  const result=mock.hass.callApi('POST','record','A');await ticks();
  const held=faults.snapshot().pending[0];
  assert.equal(held.ready,true);assert.equal(held.committed,true);
  assert.equal(mock.intents[0].status,'pending');assert.deepEqual(mock.store.records,['A']);
  await faults.release(held.id);await result;
  assert.deepEqual(mock.store.records,['A']);
  await assert.rejects(faults.release(held.id),/absent/);
});

test('failure before execution and lost acknowledgment have different store effects',async()=>{
  const {faults,mock}=setup();
  faults.arm({surface:'api',key:'POST record',mode:'reject-before',code:'denied'});
  await assert.rejects(mock.hass.callApi('POST','record','A'),{code:'denied'});
  assert.deepEqual(mock.store.records,[]);
  faults.arm({surface:'api',key:'POST record',mode:'commit-then-reject',code:'lost_ack'});
  await assert.rejects(mock.hass.callApi('POST','record','B'),{code:'lost_ack'});
  assert.deepEqual(mock.store.records,['B']);
  assert.equal(mock.intents[1].status,'rejected');
  assert.equal(faults.snapshot().events.at(-1).committed,true);
});

test('release rejection never executes a held-before handler',async()=>{
  const {faults,mock}=setup();faults.arm({surface:'api',key:'POST record',mode:'hold-before'});
  const rejected=assert.rejects(mock.hass.callApi('POST','record','A'),{code:'cancelled'});
  await faults.release(faults.snapshot().pending[0].id,{outcome:'reject',code:'cancelled'});
  await rejected;assert.deepEqual(mock.store.records,[]);
});

test('dispose rejects held operations and prevents later execution',async()=>{
  const {faults,mock}=setup();faults.arm({surface:'api',key:'POST record',mode:'hold-before'});
  const rejected=assert.rejects(mock.hass.callApi('POST','record','A'),{code:'fixture_disposed'});
  const held=faults.snapshot().pending[0];mock.dispose();await rejected;
  await assert.rejects(faults.release(held.id));
  assert.deepEqual(mock.store.records,[]);assert.equal(mock.intents[0].status,'rejected');
});

test('fault rules cannot turn an unsupported service into success',async()=>{
  const {faults,mock}=setup();faults.arm({surface:'service',key:'lock.unlock',mode:'hold-before'});
  await assert.rejects(mock.hass.callService('lock','unlock'),/Unsupported/);
  assert.equal(faults.snapshot().unconsumedRules,1);
  assert.equal(faults.snapshot().pending.length,0);
});

test('partial handler failure has unknown commit status and preserves actual store evidence',async()=>{
  const faults=createFaultController(),store=[];
  faults.arm({surface:'api',key:'write',mode:'hold-after'});
  await assert.rejects(faults.execute({surface:'api',key:'write'},()=>{store.push(1);throw new Error('partial');}),/partial/);
  assert.deepEqual(store,[1]);assert.equal(faults.snapshot().events.at(-1).committed,'unknown');
  assert.equal(faults.snapshot().pending.length,0);
});

test('delayed read preserves its response snapshot while later store writes occur',async()=>{
  const faults=createFaultController();
  const mock=createMockHass({faults,store:{items:['old']},ws:{read:{mutation:false,handle:(_,s)=>s.items}}});
  faults.arm({surface:'ws',key:'read',mode:'hold-after'});
  const read=mock.hass.callWS({type:'read'});await ticks();
  mock.store.items.push('new');
  await faults.release(faults.snapshot().pending[0].id);
  assert.deepEqual(await read,['old']);assert.deepEqual(mock.store.items,['old','new']);
});

const commands=[
  {id:'start',enabled:m=>!m.running,next:m=>({...m,running:true,starts:m.starts+1})},
  {id:'stop',enabled:m=>m.running,next:m=>({...m,running:false})},
  {id:'redraw',enabled:()=>true,next:m=>m}
];
const initial={running:false,starts:0};
const invariants=[{id:'timer.state',check:(model,observed)=>({
  pass:model.running===observed.running && model.starts===observed.starts,evidence:{expected:model,actual:observed}})}];

test('same seed reproduces concrete guarded actions without changing seed model',()=>{
  const a=generateSequence({seed:17,length:60,initial,commands});
  const b=generateSequence({seed:17,length:60,initial,commands});
  assert.deepEqual(a,b);assert.deepEqual(initial,{running:false,starts:0});
  let running=false;
  for(const action of a.sequence) {
    if(action.id==='start'){assert.equal(running,false);running=true;}
    if(action.id==='stop'){assert.equal(running,true);running=false;}
  }
  assert.equal(a.sequence.length,60);
});

test('no enabled actions stops explicitly and invalid seed/weight reject',()=>{
  const result=generateSequence({seed:0,length:4,initial,commands:[{id:'x',enabled:()=>false,next:m=>m}]});
  assert.equal(result.stopped,'no-enabled-command');assert.equal(result.sequence.length,0);
  assert.throws(()=>generateSequence({seed:-1,length:4,initial,commands}));
  assert.throws(()=>generateSequence({seed:1,length:4,initial,commands:[{...commands[0],weight:0}]}));
});

async function runTimer(sequence,broken=false) {
  let app={running:false,starts:0};
  return runModelSequence({initial,sequence,commands,invariants,
    perform:async action=>{
      if(action.id==='start'){app.running=true;app.starts+=broken?2:1;}
      if(action.id==='stop')app.running=false;
    },observe:async()=>structuredClone(app)});
}

test('independent model accepts clean behavior and catches deliberate duplicate start',async()=>{
  const sequence=[{id:'redraw'},{id:'start'},{id:'redraw'},{id:'stop'}];
  assert.equal((await runTimer(sequence)).outcome,'passed');
  const broken=await runTimer(sequence,true);
  assert.equal(broken.outcome,'failed');assert.equal(broken.signature,'timer.state');
  assert.equal(broken.trace.at(-1).step,1);
  assert.equal(broken.trace.at(-1).checks[0].evidence.actual.starts,2);
});

test('illegal sequence is distinct from product failure',async()=>{
  const result=await runTimer([{id:'stop'}]);
  assert.equal(result.outcome,'invalid-sequence');assert.equal(result.step,0);
});

test('missing observations and evidence-free invariants do not pass',async()=>{
  const base={initial,sequence:[{id:'start'}],commands,perform:async()=>{},observe:async()=>({}),invariants};
  const missing=await runModelSequence({...base,observe:async()=>{throw new Error('missing control');}});
  assert.equal(missing.outcome,'harness-error');
  const empty=await runModelSequence({...base,invariants:[{id:'weak',check:()=>({pass:true,evidence:{}})}]});
  assert.equal(empty.outcome,'harness-error');
});

test('failure reduction keeps the same independently reproduced signature',async()=>{
  const result=await minimizeFailure({sequence:[{id:'redraw'},{id:'start'},{id:'redraw'},{id:'stop'}],
    replay:steps=>runTimer(steps,true),signature:'timer.state',maxReplays:24});
  assert.equal(result.outcome,'reproduced');assert.deepEqual(result.sequence,[{id:'start'}]);
  assert.ok(result.calls<=24);assert.equal(result.attempts[0].same,true);
});

test('reduction retains original when baseline changes and ignores unrelated failures',async()=>{
  let calls=0;
  const unstable=await minimizeFailure({sequence:[{id:'a'}],signature:'same',replay:async()=>({
    outcome:++calls===1?'failed':'passed',signature:'same'})});
  assert.equal(unstable.outcome,'unstable-baseline');
  const different=await minimizeFailure({sequence:[{id:'a'},{id:'b'}],signature:'same',maxReplays:4,
    replay:async s=>({outcome:'failed',signature:s.length===2?'same':'different'})});
  assert.equal(different.sequence.length,2);
});

const temporalBase={durationMs:1000,maxGapMs:250,timeDomain:'monotonic-real',requirements:[
  {id:'timer.visible',mode:'always',check:o=>({pass:o.visible,evidence:{visible:o.visible,running:o.running}})}]};
const goodSamples=Array.from({length:5},(_,i)=>({at:i*250,observation:{visible:true,running:true}}));

test('temporal oracle catches transient disappearance despite passing endpoints and running model',()=>{
  const samples=structuredClone(goodSamples);samples[2].observation.visible=false;
  const result=assessTemporalTrace({...temporalBase,samples});
  assert.equal(result.outcome,'failed');assert.equal(result.checks[0].observations[2].evidence.running,true);
  assert.equal(assessTemporalTrace({...temporalBase,samples:goodSamples}).outcome,'passed');
});

test('long gaps, short windows and empty samples cannot prove sustained behavior',()=>{
  for(const samples of [[],[goodSamples[0]],goodSamples.slice(0,3),[goodSamples[0],goodSamples[4]]])
    assert.equal(assessTemporalTrace({...temporalBase,samples}).outcome,'inconclusive');
});

test('observed violation remains failed even with incomplete sampling',()=>{
  const samples=[{at:0,observation:{visible:false,running:true}}];
  assert.equal(assessTemporalTrace({...temporalBase,samples}).outcome,'failed');
});

test('eventual result and always-held invariant are separate contracts',()=>{
  const samples=goodSamples.map((s,i)=>({...s,observation:{visible:i===4}}));
  const result=assessTemporalTrace({...temporalBase,samples,requirements:[
    {...temporalBase.requirements[0],id:'eventual',mode:'eventually'},...temporalBase.requirements]});
  assert.equal(result.checks[0].status,'passed');assert.equal(result.checks[1].status,'failed');
});

test('success after a deadline cannot retroactively satisfy the requested window',()=>{
  const samples=Array.from({length:9},(_,i)=>({at:i*250,observation:{visible:i>=5}}));
  const result=assessTemporalTrace({...temporalBase,samples,
    requirements:[{...temporalBase.requirements[0],mode:'eventually'}]});
  assert.equal(result.outcome,'failed');assert.equal(result.sampleCount,5);
});

test('malformed clocks and evidence-free temporal answers reject',()=>{
  assert.throws(()=>assessTemporalTrace({...temporalBase,samples:[goodSamples[0],goodSamples[0]]}));
  assert.throws(()=>assessTemporalTrace({...temporalBase,samples:goodSamples,timeDomain:'iPhone-native'}));
  assert.throws(()=>assessTemporalTrace({...temporalBase,samples:goodSamples,
    requirements:[{id:'weak',mode:'always',check:()=>({pass:true,evidence:{}})}]}));
});

function geometryPage({hiddenAncestor=false,covered=false,inert=false,viewportHeight=100}={}) {
  const normal={display:'block',visibility:'visible',opacity:'1'};
  const parent={style:{...normal,opacity:hiddenAncestor?'0':'1'},hasAttribute:key=>key==='inert'&&inert,
    parentElement:null,getRootNode:()=>({})};
  const el={style:normal,parentElement:parent,hasAttribute:()=>false,
    getBoundingClientRect:()=>({left:20,top:20,right:80,bottom:80,width:60,height:60}),
    matches:()=>false,checkVisibility:()=>true,tagName:'BUTTON',id:'stop',scrollTop:0};
  const overlay={parentElement:null,getRootNode:()=>({})};
  const document={querySelectorAll:()=>[el],elementFromPoint:()=>covered?overlay:el,activeElement:el};
  const sandbox={document,window:{visualViewport:{offsetLeft:0,offsetTop:0,width:100,height:viewportHeight}},
    innerWidth:100,innerHeight:100,scrollY:0,getComputedStyle:e=>e.style};
  return {evaluate:async(fn,arg)=>vm.runInNewContext('('+fn.toString()+')('+JSON.stringify(arg)+')',sandbox)};
}

test('geometry evidence distinguishes DOM presence, hidden ancestors and intercepted input',async()=>{
  const visible=await createBrowserHelpers(geometryPage()).inspect(['#stop']);
  assert.equal(visible.visible,true);assert.equal(visible.sampledHitFraction,1);
  const hidden=await createBrowserHelpers(geometryPage({hiddenAncestor:true})).inspect(['#stop']);
  assert.equal(hidden.width,60);assert.equal(hidden.visible,false);
  const covered=await createBrowserHelpers(geometryPage({covered:true})).inspect(['#stop']);
  assert.equal(covered.visible,true);assert.equal(covered.receives,false);assert.equal(covered.sampledHitFraction,0);
});

test('inert ancestry and visual viewport shrink are explicit evidence',async()=>{
  const result=await createBrowserHelpers(geometryPage({inert:true,viewportHeight:50})).inspect(['#stop']);
  assert.equal(result.disabled,true);assert.equal(result.inert,true);assert.equal(result.viewportFraction,.5);
});

test('sample helper measures actual duration and retains observations before missing target',async()=>{
  const collected=await createBrowserHelpers({evaluate:async()=>({visible:true})}).sample(['#stop'],{durationMs:12,intervalMs:4});
  assert.ok(collected.samples.at(-1).at-collected.samples[0].at>=12);
  assert.equal(collected.timeDomain,'monotonic-real');
  let calls=0;
  const missing=createBrowserHelpers({evaluate:async()=>{
    if(++calls===2)throw new Error('Target removed');return {visible:true};
  }});
  await assert.rejects(missing.sample(['#stop'],{durationMs:20,intervalMs:2}),error=>{
    assert.equal(error.auditSamples.length,1);return error.message==='Target removed';
  });
});
