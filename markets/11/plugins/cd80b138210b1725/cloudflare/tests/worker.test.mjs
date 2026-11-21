import {after,before,test} from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {Miniflare,convertV4MiniflareOptions} from 'miniflare';
import {Client,StreamableHTTPClientTransport} from '@modelcontextprotocol/client';
let mf;let outbound=0;
before(async()=>{
  mf=new Miniflare(convertV4MiniflareOptions({modules:true,scriptPath:'build/worker.mjs',
    compatibilityDate:'2026-10-11',compatibilityFlags:['nodejs_compat'],cf:false,
    ratelimits:{MCP_IP_LIMITER:{namespace_id:'1001',simple:{limit:120,period:60}},
      MCP_SERVICE_LIMITER:{namespace_id:'1002',simple:{limit:1200,period:60}}},
    bindings:{PUBLIC_ORIGIN:'https://budget.test',DOMAIN_VERIFICATION_TOKEN:'synthetic-domain-challenge'},
    outboundService:async()=>{outbound++;throw new Error('Outbound network is forbidden in this numeric-only test.');}}));
});
after(async()=>{await mf?.dispose();});
const headers={'Content-Type':'application/json',Accept:'application/json, text/event-stream','MCP-Protocol-Version':'2025-11-25'};
async function jsonResult(response) {
  const text=await response.text();
  if(response.headers.get('content-type')?.includes('text/event-stream')) {
    const rows=text.split('\n').filter(line=>line.startsWith('data:')).map(line=>JSON.parse(line.slice(5).trim()));
    assert.ok(rows.length>0,text);return rows.at(-1);
  }
  return text ? JSON.parse(text) : null;
}
async function rpc(method,params={},extra={}) {
  return mf.dispatchFetch('http://localhost/mcp',{method:'POST',headers,
    body:JSON.stringify({jsonrpc:'2.0',id:1,method,params}),...extra});
}
test('actual Workers runtime serves health and exact challenge text without a cloud deployment',async()=>{
  assert.equal((await mf.dispatchFetch('http://localhost/health')).status,200);
  const response=await mf.dispatchFetch('https://budget.test/.well-known/openai-apps-challenge');
  assert.equal(await response.text(),'synthetic-domain-challenge');
  assert.equal((await mf.dispatchFetch('https://unconfigured.test/health')).status,503);
  assert.equal((await mf.dispatchFetch('http://localhost/private-file')).status,404);
});
test('legacy initialization and discovery expose exactly one annotated numeric tool',async()=>{
  const init=await jsonResult(await rpc('initialize',{protocolVersion:'2025-11-25',capabilities:{},clientInfo:{name:'local-test',version:'1'}}));
  assert.equal(init.result.serverInfo.name,'token-weather-budget');
  const response=await rpc('tools/list');assert.equal(response.status,200);
  const tools=(await jsonResult(response)).result.tools;
  assert.deepEqual(tools.map(tool=>tool.name),['plan_context_budget']);
  assert.equal(tools[0].inputSchema.additionalProperties,false);
  assert.ok(!('recent_turn_tokens' in tools[0].inputSchema.properties));
  assert.ok('growth_per_turn_tokens' in tools[0].inputSchema.properties);
  assert.deepEqual(tools[0].annotations,{readOnlyHint:true,destructiveHint:false,idempotentHint:true,openWorldHint:false});
  assert.ok(tools[0].outputSchema);
});
test('tools/call performs real arithmetic and never creates account/cost telemetry',async()=>{
  const response=await rpc('tools/call',{name:'plan_context_budget',arguments:{reference_limit_tokens:100000,
    used_tokens:65000,planned_increase_tokens:20000,reserved_output_tokens:5000}});
  const result=(await jsonResult(response)).result;
  assert.equal(result.isError??false,false);
  assert.equal(result.structuredContent.plan.after.remaining_tokens,10000);
  assert.ok(result.structuredContent.unknowns.includes('account_quota'));
  assert.ok(result.structuredContent.unknowns.includes('monetary_cost'));
});
test('SDK v2 client connects and calls this Worker over its HTTP transport',async()=>{
  const client=new Client({name:'local-client',version:'1.0.0'},{capabilities:{}});
  const transport=new StreamableHTTPClientTransport(new URL('http://localhost/mcp'),{
    fetch:async(url,init)=>mf.dispatchFetch(String(url),init)});
  try {
    await client.connect(transport);
    assert.equal((await client.listTools()).tools.length,1);
    const result=await client.callTool({name:'plan_context_budget',arguments:{reference_limit_tokens:100,used_tokens:85}});
    assert.equal(result.structuredContent.current.weather,'Storm');
  } finally{await client.close();}
});
test('modern MCP discovery and pinned SDK client work without persistent sessions',async()=>{
  const client=new Client({name:'modern-client',version:'1.0.0'},{capabilities:{},versionNegotiation:{mode:{pin:'2026-07-28'}}});
  const transport=new StreamableHTTPClientTransport(new URL('http://localhost/mcp'),{
    fetch:async(url,init)=>mf.dispatchFetch(String(url),init)});
  try{
    await client.connect(transport);
    assert.equal((await client.listTools()).tools[0].name,'plan_context_budget');
    const result=await client.callTool({name:'plan_context_budget',arguments:{used_tokens:65000}});
    assert.equal(result.structuredContent.reference_limit_tokens,null);
  }finally{await client.close();}
});
test('forbidden fields, tool names, errors and methods never echo private values',async()=>{
  for(const params of [{name:'plan_context_budget',arguments:{messages:'PRIVATE_SENTINEL'}},
    {name:'plan_context_budget',arguments:{thread_id:'PRIVATE_SENTINEL'}},
    {name:'PRIVATE_SENTINEL',arguments:{}}, {name:'plan_context_budget',arguments:{recent_turn_tokens:[1,2,3]}},
    {name:'plan_context_budget',arguments:{used_tokens:'PRIVATE_SENTINEL'}}]) {
    const response=await rpc('tools/call',params);const text=await response.text();
    assert.ok(!text.includes('PRIVATE_SENTINEL'),text);
    assert.ok(text.includes('error')||text.includes('isError'));
  }
  const response=await rpc('PRIVATE_SENTINEL');assert.ok(!(await response.text()).includes('PRIVATE_SENTINEL'));
});
test('request framing, size, nesting, duplicate keys and unsafe origins are refused',async()=>{
  const cases=[
    ['[]',400],['{"jsonrpc":"2.0","jsonrpc":"2.0"}',400],
    ['{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"plan_context_budget","arguments":{"used_tokens":1,"used_tokens":2}}}',400],
    ['{"padding":"'+ 'x'.repeat(17000)+'"}',413],
    ['['.repeat(40)+'0'+']'.repeat(40),400],
  ];
  for(const [body,status]of cases) assert.equal((await mf.dispatchFetch('http://localhost/mcp',{method:'POST',headers,body})).status,status);
  assert.equal((await rpc('ping',{}, {headers:{...headers,Origin:'https://evil.test'}})).status,403);
  assert.equal((await rpc('ping',{}, {headers:{...headers,Authorization:'Bearer PRIVATE_SENTINEL'}})).status,400);
  assert.equal((await mf.dispatchFetch('http://localhost/mcp')).status,405);
});
test('worker has no paid/storage bindings and no outbound network calls',async()=>{
  const config=JSON.parse(await readFile('wrangler.jsonc','utf8'));
  assert.deepEqual(Object.keys(config.vars),['PUBLIC_ORIGIN']);
  for(const key of ['ai','d1_databases','durable_objects','kv_namespaces','r2_buckets','queues','triggers','services'])assert.ok(!(key in config));
  await rpc('tools/call',{name:'plan_context_budget',arguments:{}});
  assert.equal(outbound,0);
  const meta=JSON.parse(await readFile('build/metafile.json','utf8'));
  const imports=Object.values(meta.outputs).flatMap(output=>output.imports).filter(item=>item.external).map(item=>item.path);
  assert.deepEqual(imports,['node:async_hooks']);
});

test('production rate limits refuse excess traffic before reading the request body',async()=>{
  const {default:worker}=await import('../build/worker.mjs');
  const captured=[];
  let reads=0;
  const request=new Request('https://budget.test/mcp',{method:'POST',headers:{...headers,
    'CF-Connecting-IP':'192.0.2.1'},body:new ReadableStream({pull(){reads++;}},
      {highWaterMark:0}),duplex:'half'});
  const before=reads;
  const response=await worker.fetch(request,{PUBLIC_ORIGIN:'https://budget.test',
    MCP_SERVICE_LIMITER:{limit:async()=>({success:true})},
    MCP_IP_LIMITER:{limit:async({key})=>{captured.push(key);return{success:false};}}},{});
  assert.equal(response.status,429);
  assert.equal(response.headers.get('Retry-After'),'60');
  assert.equal(response.headers.get('Cache-Control'),'no-store');
  assert.equal(response.headers.get('X-Content-Type-Options'),'nosniff');
  assert.equal(reads,before);
  assert.match(captured[0],/^token-weather-budget:ip:[0-9a-f]{64}$/);
  assert.ok(!captured[0].includes('192.0.2.1'));
  await request.body.cancel();
});

test('unavailable protection fails closed and never exposes the provider error',async()=>{
  const {default:worker}=await import('../build/worker.mjs');
  for(const bindings of [{},{MCP_IP_LIMITER:{limit:async()=>({success:true})}},
    {MCP_IP_LIMITER:{limit:async()=>({success:true})},
      MCP_SERVICE_LIMITER:{limit:async()=>{throw new Error('PRIVATE_SENTINEL');}}}]) {
    const response=await worker.fetch(new Request('https://budget.test/health'),
      {PUBLIC_ORIGIN:'https://budget.test',...bindings},{});
    assert.equal(response.status,503);
    assert.ok(!(await response.text()).includes('PRIVATE_SENTINEL'));
  }
});

test('global protection counts invalid routes; spoofed forwarding headers cannot change a bucket',async()=>{
  const {default:worker}=await import('../build/worker.mjs');
  const keys=[];
  const env={PUBLIC_ORIGIN:'https://budget.test',
    MCP_SERVICE_LIMITER:{limit:async()=>({success:true})},
    MCP_IP_LIMITER:{limit:async({key})=>{keys.push(key);return{success:true};}}};
  for(const forwarded of ['192.0.2.1','192.0.2.2']) {
    const response=await worker.fetch(new Request('https://budget.test/unknown',{
      headers:{'X-Forwarded-For':forwarded}}),env,{});
    assert.equal(response.status,404);
    assert.equal(response.headers.get('Referrer-Policy'),'no-referrer');
    assert.equal(response.headers.get('Strict-Transport-Security'),'max-age=31536000');
  }
  assert.equal(keys[0],keys[1]);
  let perIpReached=false;
  const response=await worker.fetch(new Request('https://budget.test/health'),{
    ...env,MCP_SERVICE_LIMITER:{limit:async()=>({success:false})},
    MCP_IP_LIMITER:{limit:async()=>{perIpReached=true;return{success:true};}}},{});
  assert.equal(response.status,429);
  assert.equal(perIpReached,false);
});

test('real Workers rate-limit binding throttles repeated calls on a shared edge address',async()=>{
  const runtime=new Miniflare(convertV4MiniflareOptions({modules:true,scriptPath:'build/worker.mjs',
    compatibilityDate:'2026-10-11',compatibilityFlags:['nodejs_compat'],cf:false,
    bindings:{PUBLIC_ORIGIN:'https://budget.test'},
    ratelimits:{MCP_IP_LIMITER:{namespace_id:'3001',simple:{limit:1,period:60}},
      MCP_SERVICE_LIMITER:{namespace_id:'3002',simple:{limit:100,period:60}}}}));
  try{
    const init={headers:{'CF-Connecting-IP':'192.0.2.9'}};
    assert.equal((await runtime.dispatchFetch('https://budget.test/health',init)).status,200);
    let blocked=false;
    for(let index=0;index<10;index++) {
      const response=await runtime.dispatchFetch('https://budget.test/health',init);
      if(response.status===429){blocked=true;assert.equal(response.headers.get('Retry-After'),'60');break;}
    }
    assert.equal(blocked,true);
  }finally{await runtime.dispose();}
});
