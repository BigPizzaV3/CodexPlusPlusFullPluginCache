// Explicit contracts only. This module never performs network I/O.
export function createMockHass({states = {}, store = {}, services = {}, ws = {}, api = {}, config = {}, locale = {language:'en'}, faults = null} = {}) {
  const clone = value => value === undefined ? undefined : structuredClone(value);
  const data = clone(store), intents = [], subscribers = new Set();
  let state = clone(states), current, sequence = 0, disposed = false;
  const execute = async (surface, key, payload, registry) => {
    if (disposed) throw new Error('Mock disposed');
    const contract = Object.hasOwn(registry, key) ? registry[key] : null;
    const item = {sequence:++sequence, surface, key, payload:clone(payload), mocked:true,
      mutation:contract?.mutation ?? null, status:'pending'};
    intents.push(item);
    if (!contract || typeof contract.handle !== 'function' || typeof contract.mutation !== 'boolean') {
      item.status = 'unsupported';
      throw new Error('Unsupported mock contract: '+surface+' '+key);
    }
    try {
      const commit = () => {
        if (disposed) throw new Error('Mock disposed before contract execution');
        const result=contract.handle(clone(payload), data);
        // Capture read data when the handler completes, before a held response
        // can be affected by subsequent mutations to the independent store.
        return result && typeof result.then==='function' ? Promise.resolve(result).then(clone) : clone(result);
      };
      const result = faults ? await faults.execute({surface,key},commit) : await commit();
      item.status = 'fulfilled';
      return clone(result);
    } catch (error) {
      item.status = 'rejected';
      // Do not log response bodies, stack traces or credentials by default.
      throw error;
    }
  };
  const callWS = message => execute('ws', message.type, message, ws);
  const subscribeEvents = async (callback, eventType = 'state_changed') => {
    if (disposed) throw new Error('Mock disposed');
    if (typeof callback !== 'function') throw new Error('Subscriber must be a function');
    const sub = {callback, eventType}; subscribers.add(sub);
    return () => subscribers.delete(sub);
  };
  const base = {
    config:clone(config), locale:clone(locale), language:locale.language,
    connected:true, user:{id:'audit-user',name:'Fixture user',is_admin:false},
    callService:(domain, service, serviceData = {}, target = {}) =>
      execute('service', domain+'.'+service, {serviceData, target}, services),
    callWS,
    callApi:(method, path, body) => execute('api', method.toUpperCase()+' '+path, body, api),
    connection:{sendMessagePromise:callWS, subscribeEvents}
  };
  const rebuild = () => (current = {...base, states:{...state}});
  rebuild();
  return {
    get hass() { return current; }, store:data, intents,
    update(entityId, patch, now = new Date().toISOString()) {
      if (disposed) throw new Error('Mock disposed');
      const before = state[entityId] ?? null;
      let after = null;
      if (patch !== null) {
        const nextState = String(patch.state ?? before?.state ?? 'unknown');
        after = {...clone(before || {}), ...clone(patch), entity_id:entityId, state:nextState,
          attributes:clone(patch.attributes ?? before?.attributes ?? {}),
          last_changed:before && before.state === nextState ? before.last_changed : now,
          last_updated:now, context:{id:'audit-'+(++sequence),parent_id:null,user_id:null}};
      }
      state = {...state};
      if (after) state[entityId] = after; else delete state[entityId];
      rebuild();
      const event = {event_type:'state_changed',data:{entity_id:entityId,old_state:clone(before),new_state:clone(after)},time_fired:now,origin:'LOCAL'};
      for (const sub of [...subscribers]) if (sub.eventType === 'state_changed' || sub.eventType === '*') sub.callback(clone(event));
      return current;
    },
    dispose() { disposed = true; subscribers.clear(); faults?.dispose(); },
    get subscriberCount() { return subscribers.size; }
  };
}
