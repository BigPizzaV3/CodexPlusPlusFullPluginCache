export function createLedger(meta, plan) {
  const valid = new Set(['passed','failed','blocked','inconclusive','skipped','not-run']);
  const entries = new Map();
  if (!Array.isArray(plan) || !plan.length) throw new Error('A nonempty assertion plan is required');
  for (const item of plan) {
    if (!item.id || entries.has(item.id)) throw new Error('Missing or duplicate planned ID');
    entries.set(item.id, {...item,required:item.required !== false,status:'not-run',evidence:null,recorded:false});
  }
  let closed = false;
  const record = (id, status, evidence) => {
    const entry = entries.get(id);
    if (closed || !entry || entry.recorded || !valid.has(status) || status === 'not-run')
      throw new Error('Invalid, repeated, or closed assertion: '+id);
    if (!evidence || typeof evidence !== 'object' || !Object.keys(evidence).length)
      throw new Error('Evidence or an explicit reason is required');
    Object.assign(entry, {status,evidence,recorded:true});
  };
  return {
    record,
    hasResult:id => Boolean(entries.get(id)?.recorded),
    finish(extra = {}) {
      if (closed) throw new Error('Ledger already closed');
      closed = true;
      const assertions = [...entries.values()].map(({recorded,...rest}) => rest);
      const counts = Object.fromEntries([...valid].map(s => [s, assertions.filter(a => a.status === s).length]));
      const required = assertions.filter(a => a.required);
      const outcome = required.some(a => a.status === 'failed') ? 'failed' :
        required.length && required.every(a => a.status === 'passed') ? 'passed' : 'incomplete';
      return {...extra,schemaVersion:1,meta:{...meta},assertions,counts,planned:assertions.length,outcome};
    }
  };
}
