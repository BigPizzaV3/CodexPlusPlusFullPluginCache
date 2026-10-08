// Evaluate explicitly sampled observations. Passing never proves continuous visibility.
export function assessTemporalTrace({samples,durationMs,maxGapMs,timeDomain,requirements}) {
  if(!Array.isArray(samples) || !Number.isFinite(durationMs) || durationMs<=0 ||
    !Number.isFinite(maxGapMs) || maxGapMs<=0 ||
    !['monotonic-real','wall-real','virtual'].includes(timeDomain) ||
    !Array.isArray(requirements) || !requirements.length ||
    new Set(requirements.map(r=>r.id)).size!==requirements.length ||
    requirements.some(r=>!r.id || !['always','eventually'].includes(r.mode) || typeof r.check!=='function'))
    throw new Error('Explicit temporal window, time domain and unique requirements are required');
  if(samples.some((s,i)=>!Number.isFinite(s.at) || (i>0 && s.at<=samples[i-1].at)))
    throw new Error('Sample times must be finite and strictly increasing');
  const deadline=samples.length ? samples[0].at+durationMs : null;
  const endIndex=samples.findIndex(s=>s.at>=deadline);
  const observed=endIndex<0?samples:samples.slice(0,endIndex+1);
  const inWindow=observed.filter(s=>s.at<=deadline);
  const spanMs=observed.length ? observed.at(-1).at-observed[0].at : 0;
  const largestGapMs=observed.length>1 ? Math.max(...observed.slice(1).map((s,i)=>s.at-observed[i].at)) : null;
  const coverageComplete=observed.length>=2 && spanMs>=durationMs && largestGapMs<=maxGapMs;
  const checks=requirements.map(requirement=>{
    const observations=inWindow.map(sample=>{
      const result=requirement.check(structuredClone(sample.observation));
      if(typeof result?.pass!=='boolean' || !result.evidence || typeof result.evidence!=='object' ||
        !Object.keys(result.evidence).length) throw new Error('Temporal oracle needs measured evidence');
      return {at:sample.at,...result};
    });
    const satisfied=requirement.mode==='always' ? observations.every(s=>s.pass) : observations.some(s=>s.pass);
    const violated=requirement.mode==='always' && observations.some(s=>!s.pass);
    return {id:requirement.id,status:violated?'failed':!coverageComplete?'inconclusive':satisfied?'passed':'failed',observations};
  });
  return {outcome:checks.some(c=>c.status==='failed')?'failed':coverageComplete?'passed':'inconclusive',
    timeDomain,spanMs,largestGapMs,coverageComplete,sampleCount:inWindow.length,suppliedSampleCount:samples.length,checks,
    scope:'Only sampled observations; no inference about unsampled intervals or native device behavior'};
}
