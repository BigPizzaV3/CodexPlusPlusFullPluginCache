// Pure seeded planning, independent model checks, and bounded failure reduction.
export function createSeededRandom(seed) {
  if (!Number.isInteger(seed) || seed < 0 || seed > 0xffffffff) throw new Error('Seed must be uint32');
  let state=seed;
  return () => {
    state=(state+0x6D2B79F5)>>>0;
    let x=state;
    x=Math.imul(x^(x>>>15),x|1);
    x^=x+Math.imul(x^(x>>>7),x|61);
    return ((x^(x>>>14))>>>0)/4294967296;
  };
}

function auditCommandMap(commands) {
  if (!Array.isArray(commands) || !commands.length) throw new Error('Commands required');
  const map=new Map();
  for (const c of commands) {
    if (!c.id || map.has(c.id) || typeof c.enabled!=='function' || typeof c.next!=='function' ||
      (c.weight!==undefined && (!Number.isFinite(c.weight) || c.weight<=0))) throw new Error('Invalid command contract');
    map.set(c.id,c);
  }
  return map;
}

export function generateSequence({seed,length,initial,commands}) {
  if (!Number.isInteger(length) || length<1 || length>10000) throw new Error('Bounded positive sequence length required');
  const random=createSeededRandom(seed), map=auditCommandMap(commands), sequence=[];
  let model=structuredClone(initial);
  for(let i=0;i<length;i++) {
    const enabled=[...map.values()].filter(c=>c.enabled(structuredClone(model))===true);
    if(!enabled.length) return {seed,sequence,stopped:'no-enabled-command'};
    let pick=random()*enabled.reduce((sum,c)=>sum+(c.weight??1),0);
    const command=enabled.find(c=>(pick-=c.weight??1)<0) || enabled.at(-1);
    const args=command.generate ? command.generate(structuredClone(model),random) : null;
    sequence.push({id:command.id,args:structuredClone(args)});
    model=command.next(structuredClone(model),structuredClone(args));
    if(model===undefined) throw new Error('Model transition returned undefined');
  }
  return {seed,sequence,stopped:'length'};
}

export async function runModelSequence({initial,sequence,commands,perform,observe,invariants}) {
  const map=auditCommandMap(commands), trace=[];
  if(!Array.isArray(sequence) || !sequence.length || typeof perform!=='function' || typeof observe!=='function' ||
    !Array.isArray(invariants) || !invariants.length ||
    new Set(invariants.map(i=>i.id)).size!==invariants.length ||
    invariants.some(i=>!i.id || typeof i.check!=='function')) throw new Error('Sequence, actions, observations and unique invariants required');
  let model=structuredClone(initial);
  const verify=async (step,command) => {
    const observation=await observe();
    const checks=invariants.map(invariant=>{
      const result=invariant.check(structuredClone(model),structuredClone(observation));
      if(typeof result?.pass!=='boolean' || !result.evidence || typeof result.evidence!=='object' ||
        !Object.keys(result.evidence).length) throw new Error('Invariant must return pass and measured evidence: '+invariant.id);
      return {...result,id:invariant.id};
    });
    trace.push({step,command,checks});
    const failed=checks.find(c=>!c.pass);
    return failed ? {outcome:'failed',signature:failed.id,trace} : null;
  };
  try {
    const baseline=await verify(-1,null);
    if(baseline) return baseline;
    for(let step=0;step<sequence.length;step++) {
      const action=sequence[step], command=map.get(action.id);
      if(!command || command.enabled(structuredClone(model))!==true)
        return {outcome:'invalid-sequence',step,trace};
      const expected=command.next(structuredClone(model),structuredClone(action.args));
      if(expected===undefined) throw new Error('Model transition returned undefined');
      await perform(structuredClone(action));
      model=expected;
      const failed=await verify(step,action.id);
      if(failed) return failed;
    }
    return {outcome:'passed',trace};
  } catch(error) { return {outcome:'harness-error',reason:String(error.message),trace}; }
}

export async function minimizeFailure({sequence,replay,signature,maxReplays=32}) {
  if(!Array.isArray(sequence) || !sequence.length || typeof replay!=='function' || !signature ||
    !Number.isInteger(maxReplays) || maxReplays<2 || maxReplays>1000) throw new Error('Invalid reduction contract');
  let calls=0, candidate=structuredClone(sequence), width=Math.ceil(candidate.length/2);
  const attempts=[];
  const reproduces=async steps=>{
    calls++;
    const result=await replay(structuredClone(steps));
    const same=result?.outcome==='failed' && result.signature===signature;
    attempts.push({length:steps.length,outcome:result?.outcome,signature:result?.signature??null,same});
    return same;
  };
  if(!await reproduces(candidate) || !await reproduces(candidate))
    return {outcome:'unstable-baseline',sequence:candidate,calls,attempts};
  while(width>=1 && calls<maxReplays) {
    let reduced=false;
    for(let at=0;at<candidate.length && calls<maxReplays;at+=width) {
      const shorter=candidate.slice(0,at).concat(candidate.slice(at+width));
      if(!shorter.length) continue;
      if(await reproduces(shorter)) {candidate=shorter; reduced=true; break;}
    }
    if(!reduced) width=Math.floor(width/2);
    else width=Math.min(width,Math.ceil(candidate.length/2));
  }
  return {outcome:'reproduced',sequence:candidate,calls,attempts,
    budgetExhausted:calls>=maxReplays,minimality:'bounded contiguous-deletion search, not a proof of global minimality'};
}
