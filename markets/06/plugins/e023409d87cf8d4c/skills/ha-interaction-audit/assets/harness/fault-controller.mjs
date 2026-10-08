// Fixture-only response scheduling. No networking and no wall-clock sleeps.
export function createFaultController() {
  const rules = [], pending = new Map(), events = [];
  const modes = new Set(['hold-before','hold-after','reject-before','commit-then-reject']);
  let serial = 0, disposed = false;
  const failure = code => Object.assign(new Error('Injected fixture failure: '+code), {code});
  const emit = (entry, phase) => events.push({id:entry.id, surface:entry.surface,
    key:entry.key, phase, committed:entry.committed});
  const commitOnce = async entry => {
    if (entry.started) throw new Error('Contract execution already started');
    if (disposed) throw failure('fixture_disposed');
    entry.started = true;
    emit(entry, 'commit-start');
    try {
      entry.value = await entry.commit();
      entry.committed = true;
      emit(entry, 'commit-complete');
    } catch (error) {
      // A throwing handler might already have made a partial change.
      entry.committed = 'unknown';
      emit(entry, 'commit-error');
      throw error;
    }
  };
  const settle = async (entry, outcome, code) => {
    try {
      if (outcome !== 'reject' && !entry.started) await commitOnce(entry);
      if (disposed) throw failure('fixture_disposed');
      if (outcome !== 'fulfill') throw failure(code);
      emit(entry, 'response-fulfilled');
      entry.resolve(entry.value);
    } catch (error) {
      emit(entry, 'response-rejected');
      entry.reject(error);
    } finally { pending.delete(entry.id); }
  };
  return {
    arm({surface, key, mode, code = 'simulated_failure'}) {
      if (disposed) throw new Error('Fault controller disposed');
      if (!surface || !key || !modes.has(mode) || typeof code !== 'string' || !code)
        throw new Error('Fault requires an exact surface/key, supported mode and code');
      rules.push({surface,key,mode,code});
    },
    async execute({surface,key}, commit) {
      if (disposed) throw new Error('Fault controller disposed');
      if (typeof commit !== 'function') throw new Error('Explicit contract callback required');
      const entry = {id:++serial,surface,key,commit,started:false,committed:false};
      const index = rules.findIndex(r=>r.surface===surface && r.key===key);
      const rule = index < 0 ? null : rules.splice(index,1)[0];
      emit(entry, 'request');
      if (!rule) { await commitOnce(entry); emit(entry,'response-fulfilled'); return entry.value; }
      if (rule.mode==='reject-before') { emit(entry,'response-rejected'); throw failure(rule.code); }
      if (rule.mode==='commit-then-reject') {
        await commitOnce(entry); emit(entry,'response-rejected'); throw failure(rule.code);
      }
      return new Promise((resolve,reject) => {
        Object.assign(entry,{resolve,reject,ready:rule.mode==='hold-before',code:rule.code});
        pending.set(entry.id,entry);
        if (rule.mode==='hold-before') emit(entry,'held-before');
        else commitOnce(entry).then(()=>{
          if (disposed) return;
          entry.ready=true; emit(entry,'held-after');
        }, error=>{
          emit(entry,'response-rejected'); pending.delete(entry.id); reject(error);
        });
      });
    },
    async release(id, {outcome='fulfill',code}={}) {
      if (!['fulfill','reject','commit-then-reject'].includes(outcome)) throw new Error('Invalid release outcome');
      const entry = pending.get(id);
      if (!entry || !entry.ready) throw new Error('Request is absent, already released, or not ready');
      entry.ready=false;
      await settle(entry,outcome,code || entry.code);
    },
    snapshot() {
      return {pending:[...pending.values()].map(({id,surface,key,ready,committed})=>({id,surface,key,ready,committed})),
        unconsumedRules:rules.length, events:structuredClone(events)};
    },
    dispose() {
      disposed=true; rules.length=0;
      for (const entry of pending.values()) {emit(entry,'disposed'); entry.reject(failure('fixture_disposed'));}
      pending.clear();
    }
  };
}
