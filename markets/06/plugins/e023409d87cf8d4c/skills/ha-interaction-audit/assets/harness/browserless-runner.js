export default async ({page: suppliedPage, browser: suppliedBrowser, context: input}) => {
  const automatic = [
    'gate.adapter-ready','gate.transport-probes','gate.unexpected-traffic',
    'gate.mock-contracts','gate.runtime-errors','gate.cleanup'
  ].map(id => ({id,required:true}));
  const ledger = createLedger(input.meta, [...automatic, ...input.plan]);
  const network = [], errors = [], owned = {context:null,page:null};
  const probePaths = new Set(['/__audit_probe__/get','/__audit_probe__/post']);
  let finished = false, deadlineTimer, interruption = null, contextCreationPending = false;
  const record = (id,status,evidence) => {
    if (finished) throw new Error('Pass already ended');
    ledger.record(id,status,evidence);
  };
  const execute = async () => {
    const browser = suppliedBrowser || suppliedPage?.browser();
    const createContext = browser?.createBrowserContext || browser?.createIncognitoBrowserContext;
    if (!createContext) throw new Error('Fresh browser context is unavailable');
    contextCreationPending = true;
    let created;
    try { created = await createContext.call(browser); }
    finally { contextCreationPending = false; }
    if (finished) {
      await created.close();
      throw new Error('Context arrived after pass deadline and was closed');
    }
    owned.context = created;
    const page = owned.page = await owned.context.newPage();
    page.setDefaultTimeout(input.stepTimeoutMs);
    await page.setViewport(input.viewport);
    await page.setCacheEnabled(false);
    if (typeof page.setBypassServiceWorker !== 'function') throw new Error('Service-worker bypass unavailable');
    await page.setBypassServiceWorker(true);
    await page.evaluateOnNewDocument(installBrowserGuards);
    const decide = createResourcePolicy(input.resources);
    const csp = "default-src 'none'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; font-src 'self' data:; connect-src 'self'; worker-src 'none'; frame-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'";
    await page.setRequestInterception(true);
    page.on('request', req => {
      const decision = decide(req.method(),req.url());
      let path = '';
      try { path = new URL(req.url()).pathname; } catch {}
      network.push({method:req.method(),path,action:decision.action,probe:probePaths.has(path)});
      const promise = decision.action === 'fulfill' ? req.respond({status:200,
        contentType:decision.contentType,body:decision.body,
        headers:{'Content-Security-Policy':csp,'Cache-Control':'no-store'}}) : req.abort('blockedbyclient');
      promise.catch(() => { if(!finished) errors.push({kind:'interception',message:'Request handling failed'}); });
    });
    page.on('pageerror', e => { if(!finished) errors.push({kind:'runtime',message:String(e.message).slice(0,1000)}); });
    page.on('console', m => {
      if(finished || m.type() !== 'error') return;
      const location = m.location?.() || {};
      let expectedProbe = false;
      try {const url=new URL(location.url);expectedProbe=url.origin===VIRTUAL_ORIGIN&&probePaths.has(url.pathname);} catch {}
      if(!expectedProbe) errors.push({kind:'console',message:m.text().slice(0,1000)});
    });
    await page.goto(VIRTUAL_ORIGIN+input.entry,{waitUntil:'domcontentloaded',timeout:input.stepTimeoutMs});
    await page.waitForFunction(() => window.__HA_AUDIT?.ready === true,{timeout:input.stepTimeoutMs});
    const identity = await page.evaluate(() => ({identity:window.__HA_AUDIT.identity,
      mountedTag:window.__HA_AUDIT.app?.tagName?.toLowerCase()}));
    const parity = identity.mountedTag === input.expectedTag && input.meta.sourceStatus === 'verified';
    record('gate.adapter-ready',parity?'passed':'failed',{expectedTag:input.expectedTag,...identity});
    if(!parity) throw new Error('Mounted target or source verification does not match');
    const probes = await page.evaluate(async () => {
      for(const [method,path] of [['GET','get'],['POST','post']]) {
        try { await fetch('/__audit_probe__/'+path,{method}); } catch {}
      }
      const g=window.__HA_AUDIT_GUARDS;
      g.probe(() => {
        for(const name of ['WebSocket','EventSource','Worker','SharedWorker','RTCPeerConnection']) {
          try {new window[name]('https://ha-audit.invalid/__audit_probe__/transport');} catch {}
        }
        navigator.sendBeacon('/__audit_probe__/beacon','probe');
      });
      return g.events.filter(e=>e.probe);
    });
    const blockedHTTP = network.filter(n=>n.probe&&n.action==='abort');
    const requiredSurfaces=['WebSocket','EventSource','Worker','SharedWorker','RTCPeerConnection','beacon'];
    const contained = ['GET','POST'].every(m=>blockedHTTP.some(n=>n.method===m)) &&
      requiredSurfaces.every(s=>probes.some(p=>p.surface===s&&p.blocked));
    record('gate.transport-probes',contained?'passed':'failed',{http:blockedHTTP,transports:probes});
    if(!contained) throw new Error('Containment probes failed');
    const helpers = createBrowserHelpers(page);
    const advanced={generateSequence,runModelSequence,minimizeFailure,assessTemporalTrace};
    await runSuite({page,helpers,record,input,advanced});
    // Allow terminal events queued by the final browser action to be collected.
    await page.evaluate(() => new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
    const final = await page.evaluate(() => ({
      guards:window.__HA_AUDIT_GUARDS.events.filter(e=>!e.probe),
      intents:window.__HA_AUDIT?.mock?.intents ?? null,
      faults:window.__HA_AUDIT?.faults?.snapshot() ?? null
    }));
    const unexpected = network.filter(n=>!n.probe&&n.action==='abort');
    record('gate.unexpected-traffic',!unexpected.length&&!final.guards.length?'passed':'failed',
      {unexpectedHTTP:unexpected,blockedTransports:final.guards,forwardingPolicy:'no upstream forwarding branch'});
    if(!Array.isArray(final.intents)) record('gate.mock-contracts','blocked',{reason:'Adapter has no mock intent ledger'});
    else record('gate.mock-contracts',final.intents.every(i=>typeof i.mutation==='boolean'&&!['unsupported','pending'].includes(i.status)) &&
      (!final.faults || (!final.faults.pending.length && final.faults.unconsumedRules===0))?'passed':'failed',
      {intents:final.intents,faults:final.faults,mutationIntents:final.intents.filter(i=>i.mutation===true).length});
    record('gate.runtime-errors',errors.length?'failed':'passed',{errors});
  };
  try {
    await Promise.race([execute(),new Promise((_,reject)=>{
      deadlineTimer=setTimeout(()=>reject(new Error('Pass budget exceeded')),input.maxPassMs);
    })]);
  } catch(error) {
    interruption = String(error.message).slice(0,1000);
    // Missing results retain not-run. A timeout must never fabricate partial evidence.
    if(!ledger.hasResult('gate.adapter-ready')) record('gate.adapter-ready','blocked',{reason:interruption});
  } finally {
    clearTimeout(deadlineTimer);
    finished=true;
    let cleanup=contextCreationPending?'unconfirmed':'confirmed', cleanupTimer;
    try {
      if(owned.context) await Promise.race([owned.context.close(),new Promise((_,reject)=>{
        cleanupTimer=setTimeout(()=>reject(new Error('Context close timeout')),2000);
      })]);
    } catch { cleanup='unconfirmed'; }
    finally { clearTimeout(cleanupTimer); }
    ledger.record('gate.cleanup',cleanup==='confirmed'?'passed':'blocked',{cleanup,ownedContextCreated:!!owned.context});
  }
  return {data:ledger.finish({interruption,network,errors}),type:'application/json'};
};
