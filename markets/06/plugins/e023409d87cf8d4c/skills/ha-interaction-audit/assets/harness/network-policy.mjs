export const VIRTUAL_ORIGIN = 'https://ha-audit.invalid';

export function createResourcePolicy(resources) {
  const table = new Map();
  for (const item of resources) {
    const url = new URL(item.path, VIRTUAL_ORIGIN);
    if (!item.path.startsWith('/') || item.path.startsWith('//') ||
        url.origin !== VIRTUAL_ORIGIN || url.hash || url.username || url.password ||
        table.has(url.href) || typeof item.body !== 'string') {
      throw new Error('Invalid or duplicate fixture resource');
    }
    table.set(url.href, {body:item.body, contentType:item.contentType || 'text/plain'});
  }
  return (method, rawURL) => {
    let url;
    try { url = new URL(rawURL); } catch { return {action:'abort', reason:'invalid-url'}; }
    const resource = table.get(url.href);
    if (method !== 'GET' || !resource || url.origin !== VIRTUAL_ORIGIN)
      return {action:'abort', reason:'unmapped-request'};
    return {action:'fulfill', ...resource};
  };
}

// This function must remain self-contained for evaluateOnNewDocument().
export function installBrowserGuards() {
  const events = [];
  const add = (surface, probe = false) => events.push({surface, probe, blocked:true, at:Date.now()});
  let probing = false;
  Object.defineProperty(window, '__HA_AUDIT_GUARDS', {value:{
    events,
    probe(fn) { probing = true; try { return fn(); } finally { probing = false; } }
  }, configurable:false, writable:false});
  for (const name of ['WebSocket','EventSource','Worker','SharedWorker','RTCPeerConnection','webkitRTCPeerConnection']) {
    const blocked = class {
      static CONNECTING = 0; static OPEN = 1; static CLOSING = 2; static CLOSED = 3;
      constructor() { add(name, probing); throw new Error('Fixture blocks native '+name); }
    };
    Object.defineProperty(window, name, {value:blocked, writable:false, configurable:false});
  }
  Object.defineProperty(navigator, 'sendBeacon', {value:() => {add('beacon', probing);return false;}});
  if (navigator.serviceWorker) {
    Object.defineProperty(navigator.serviceWorker, 'register', {value:() => {
      add('serviceWorker', probing); return Promise.reject(new Error('Fixture blocks service workers'));
    }});
  }
  Object.defineProperty(window, 'open', {value:() => {add('window.open', probing);return null;}});
}
