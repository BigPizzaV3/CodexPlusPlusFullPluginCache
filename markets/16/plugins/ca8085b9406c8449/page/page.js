(() => {
  const config = window.HDI_MARKETING_CONFIG || {};

  function allowedUrl(value, allowMail = false) {
    if (typeof value !== 'string' || !value.trim()) return null;
    try {
      const url = new URL(value);
      if (url.protocol !== 'https:' && !(allowMail && url.protocol === 'mailto:')) return null;
      if (url.username || url.password) return null;
      return url.href;
    } catch { return null; }
  }

  function setLink(element, value, allowMail = false) {
    const url = allowedUrl(value, allowMail);
    if (element && url) element.href = url;
  }

  const contactLink = document.getElementById('contact-link');
  const demoLink = document.getElementById('demo-link');
  setLink(contactLink, config.contactUrl, true);
  setLink(demoLink, config.demoUrl);

  // Standalone previews keep normal links; embedded MCP Apps use their host.
  if (window.parent === window) return;

  let rpcId = 0;
  let bridgeReady = false;
  const pending = new Map();

  function rpcNotify(method, params) {
    window.parent.postMessage({ jsonrpc: '2.0', method, params }, '*');
  }

  function rpcRequest(method, params) {
    return new Promise((resolve, reject) => {
      const id = ++rpcId;
      const timer = window.setTimeout(() => {
        pending.delete(id);
        reject(new Error('The host did not respond.'));
      }, 2500);
      pending.set(id, { resolve, reject, timer });
      window.parent.postMessage({ jsonrpc: '2.0', id, method, params }, '*');
    });
  }

  function mergeResponse(response) {
    const data = response?.structuredContent;
    if (!data) return;
    setLink(contactLink, data.contactUrl, true);
    setLink(demoLink, data.demoUrl);

    const supportSection = document.getElementById('support-section');
    const hasSupport = typeof data.support?.body === 'string' && data.support.body.trim();
    supportSection.hidden = !hasSupport;
    if (hasSupport) {
      document.getElementById('support-title').textContent = data.support.title || 'Support';
      document.getElementById('support-copy').textContent = data.support.body;
    }
  }

  window.addEventListener('message', event => {
    if (event.source !== window.parent) return;
    const message = event.data;
    if (!message || message.jsonrpc !== '2.0') return;

    if (typeof message.id === 'number') {
      const request = pending.get(message.id);
      if (!request) return;
      pending.delete(message.id);
      window.clearTimeout(request.timer);
      if (message.error) request.reject(message.error);
      else request.resolve(message.result);
      return;
    }
    if (message.method === 'ui/notifications/tool-result') mergeResponse(message.params);
  }, { passive: true });

  document.addEventListener('click', event => {
    const link = event.target instanceof Element ? event.target.closest('a[href]') : null;
    const url = link && allowedUrl(link.href, link === contactLink);
    if (!bridgeReady || !url) return;
    event.preventDefault();
    rpcRequest('ui/open-link', { url }).catch(() => {
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  });

  rpcRequest('ui/initialize', {
    appInfo: { name: 'oracle-health-ph-widget', version: '0.1.0' },
    appCapabilities: {},
    protocolVersion: '2026-01-26',
  }).then(() => {
    bridgeReady = true;
    rpcNotify('ui/notifications/initialized', {});
  }).catch(() => {
    // Ordinary browser iframes without an MCP Apps host retain working links.
  });
})();
