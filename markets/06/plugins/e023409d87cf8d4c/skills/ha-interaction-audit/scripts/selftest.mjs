import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import {createResourcePolicy,installBrowserGuards} from '../assets/harness/network-policy.mjs';
import {createMockHass} from '../assets/harness/mock-hass.mjs';
import {createLedger} from '../assets/harness/ledger.mjs';

test('only exact supplied GET resources are fulfilled; no external or write fallback',()=>{
  const policy=createResourcePolicy([{path:'/app.js?v=1',body:'source',contentType:'application/javascript'}]);
  assert.equal(policy('GET','https://ha-audit.invalid/app.js?v=1').action,'fulfill');
  for(const [method,url] of [
    ['POST','https://ha-audit.invalid/app.js?v=1'],
    ['GET','https://ha-audit.invalid/app.js?v=2'],
    ['GET','https://ha-audit.invalid/api/action/start'],
    ['GET','https://example.com/app.js?v=1'],
    ['GET','https://ha-audit.invalid.evil.invalid/app.js?v=1']
  ]) assert.equal(policy(method,url).action,'abort');
});

test('invalid and duplicate resource maps are rejected',()=>{
  assert.throws(()=>createResourcePolicy([{path:'//example.com/a',body:'x'}]));
  assert.throws(()=>createResourcePolicy([{path:'/a',body:'x'},{path:'/a',body:'y'}]));
});

test('preload blocks native transports and identifies probes without logging URLs',async()=>{
  const sandbox={navigator:{serviceWorker:{}},Date}; sandbox.window=sandbox;
  vm.runInNewContext('('+installBrowserGuards.toString()+')()',sandbox);
  for(const name of ['WebSocket','EventSource','Worker','SharedWorker','RTCPeerConnection'])
    assert.throws(()=>new sandbox[name]('https://private.invalid/token'));
  assert.equal(sandbox.navigator.sendBeacon('private','data'),false);
  await assert.rejects(sandbox.navigator.serviceWorker.register('/worker.js'));
  sandbox.__HA_AUDIT_GUARDS.probe(()=>assert.throws(()=>new sandbox.WebSocket('reserved')));
  assert.equal(sandbox.__HA_AUDIT_GUARDS.events.filter(x=>x.probe).length,1);
  assert.ok(sandbox.__HA_AUDIT_GUARDS.events.every(x=>x.blocked));
  assert.ok(!JSON.stringify(sandbox.__HA_AUDIT_GUARDS.events).includes('private'));
});

test('known service mutates only independent fixture store and logs exact target',async()=>{
  const original={enabled:false};
  const mock=createMockHass({store:original,services:{'switch.turn_on':{mutation:true,
    handle:({target},store)=>{store.enabled=true;return {target};}}}});
  const result=await mock.hass.callService('switch','turn_on',{}, {entity_id:'switch.audit'});
  assert.deepEqual(result,{target:{entity_id:'switch.audit'}});
  assert.equal(original.enabled,false);assert.equal(mock.store.enabled,true);
  assert.equal(mock.intents.length,1);assert.equal(mock.intents[0].status,'fulfilled');
  assert.equal(mock.intents[0].mutation,true);
});

test('unknown services, raw WS commands and API paths reject instead of succeeding',async()=>{
  const mock=createMockHass();
  await assert.rejects(mock.hass.callService('lock','unlock',{}));
  await assert.rejects(mock.hass.callWS({type:'call_service'}));
  await assert.rejects(mock.hass.callApi('GET','unexpected/action'));
  assert.equal(mock.intents.length,3);
  assert.ok(mock.intents.every(i=>i.status==='unsupported'&&i.mutation===null));
});

test('mock read result is independent and failed writes stay rejected',async()=>{
  const mock=createMockHass({store:{records:[1]},ws:{read:{mutation:false,handle:(_,s)=>s.records}},
    api:{'PUT record':{mutation:true,handle:()=>{throw new Error('409 conflict');}}}});
  const result=await mock.hass.connection.sendMessagePromise({type:'read'});result.push(2);
  assert.deepEqual(mock.store.records,[1]);
  await assert.rejects(mock.hass.callApi('put','record',{}),/409/);
  assert.equal(mock.intents.at(-1).status,'rejected');
});

test('HA updates create fresh identities, preserve last_changed for attributes, and unsubscribe',async()=>{
  const seed={state:'on',entity_id:'switch.audit',attributes:{value:1},last_changed:'old',last_updated:'old'};
  const mock=createMockHass({states:{'switch.audit':seed}});let events=0;
  const unsub=await mock.hass.connection.subscribeEvents(()=>events++);
  const before=mock.hass;const after=mock.update('switch.audit',{attributes:{value:2}},'now');
  assert.notEqual(before,after);assert.notEqual(before.states,after.states);
  assert.notEqual(before.states['switch.audit'],after.states['switch.audit']);
  assert.equal(after.states['switch.audit'].last_changed,'old');
  assert.equal(seed.attributes.value,1);assert.equal(events,1);
  unsub();mock.update('switch.audit',null);assert.equal(events,1);
  assert.equal(mock.hass.states['switch.audit'],undefined);
  mock.dispose();assert.throws(()=>mock.update('x',{state:'off'}));
});

test('ledger keeps not-run distinct and refuses duplicate/unknown IDs',()=>{
  const l=createLedger({sourceFingerprint:'test'},[{id:'a'},{id:'b'}]);
  l.record('a','passed',{observed:true});
  assert.throws(()=>l.record('a','passed',{observed:true}));
  assert.throws(()=>l.record('c','passed',{observed:true}));
  const r=l.finish();assert.equal(r.counts['not-run'],1);assert.equal(r.outcome,'incomplete');
  assert.throws(()=>l.record('b','passed',{observed:true}));
});

test('empty plans and evidence-free successes are rejected',()=>{
  assert.throws(()=>createLedger({},[]));
  assert.throws(()=>createLedger({},[{id:'same'},{id:'same'}]));
  const l=createLedger({},[{id:'a'}]);assert.throws(()=>l.record('a','passed',{}));
  l.record('a','blocked',{reason:'No adapter'});assert.equal(l.finish().outcome,'incomplete');
});

test('failed checks cannot be hidden by forged summary extras',()=>{
  const l=createLedger({},[{id:'a'}]);l.record('a','failed',{expected:1,actual:2});
  const r=l.finish({outcome:'passed',counts:{passed:10}});
  assert.equal(r.outcome,'failed');assert.equal(r.counts.failed,1);
});
