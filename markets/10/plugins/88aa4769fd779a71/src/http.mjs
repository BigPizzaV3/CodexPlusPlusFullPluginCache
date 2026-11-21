import { createServer } from 'node:http';
import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { createCalculatorServer } from './mcp-server.mjs';

const MAX_BODY = 32768;
const HTTP_TIMEOUTS = { headersTimeout: 10000, requestTimeout: 15000, keepAliveTimeout: 5000, connectionsCheckingInterval: 1000 };
const readBuiltHtml = () => readFileSync(new URL('../dist/calculator.html', import.meta.url), 'utf8');

export function createHttpServer({ publicBaseUrl, publicBaseUrls = [], readHtml = readBuiltHtml } = {}) {
  const publicOrigins = [...new Set([publicBaseUrl, ...publicBaseUrls].filter(Boolean).map(value => {
    const url = new URL(value);
    if (url.protocol !== 'https:' || url.username || url.password || url.pathname !== '/' || url.search || url.hash) {
      throw new Error('Public base URLs must be HTTPS origins without credentials, paths, or queries.');
    }
    return url.origin;
  }))];
  const loadHtml = () => {
    try {
      const html = readHtml();
      if (typeof html !== 'string' || !/<html(?:\s|>)/i.test(html) || !/<\/html\s*>/i.test(html) || html.includes('/* BUILD_SCRIPT */')) {
        throw new Error('Calculator HTML is incomplete or has not been built.');
      }
      return html;
    } catch (cause) {
      throw new Error('Calculator UI is unavailable. Run npm run build before starting the server.', { cause });
    }
  };
  loadHtml(); // Fail before listening if the deploy is missing its built component.
  const server = createServer(HTTP_TIMEOUTS, async (req, res) => {
    const localHosts = new Set([`127.0.0.1:${req.socket.localPort}`, `localhost:${req.socket.localPort}`, `[::1]:${req.socket.localPort}`]);
    const allowedHosts = new Set([...localHosts, ...publicOrigins.map(value => new URL(value).host)]);
    res.setHeader('X-Content-Type-Options', 'nosniff');
    res.setHeader('Referrer-Policy', 'no-referrer');
    res.setHeader('Cache-Control', 'no-store');
    if (!allowedHosts.has(req.headers.host)) return res.writeHead(403).end('Host not allowed');
    const origin = req.headers.origin;
    const allowedOrigins = new Set([...localHosts].map(host => `http://${host}`));
    for (const publicOrigin of publicOrigins) allowedOrigins.add(publicOrigin);
    if (origin && !allowedOrigins.has(origin)) return res.writeHead(403).end('Origin not allowed');
    if (origin) { res.setHeader('Access-Control-Allow-Origin', origin); res.setHeader('Vary', 'Origin'); }
    let path;
    try { path = new URL(req.url ?? '/', 'http://localhost').pathname; }
    catch { return res.writeHead(400).end('Invalid request URL'); }
    if (req.method === 'GET' && ['/privacy', '/support'].includes(path)) {
      try {
        const page = readFileSync(new URL(`../public${path}.html`, import.meta.url), 'utf8');
        return res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Content-Security-Policy': "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'" }).end(page);
      } catch { return res.writeHead(503).end('Page temporarily unavailable'); }
    }
    if (req.method === 'GET' && path === '/.well-known/openai-apps-challenge') {
      const challenge = process.env.OPENAI_APPS_CHALLENGE;
      if (!challenge) return res.writeHead(404).end('Verification is not configured');
      return res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' }).end(challenge);
    }
    let html;
    if (path === '/' || path === '/health' || path === '/mcp') {
      // Re-read so local preview reloads still work and readiness catches a lost build.
      try { html = loadHtml(); }
      catch { return res.writeHead(503, { 'Content-Type': 'application/json', 'Retry-After': '5' }).end(JSON.stringify({ status: 'unavailable' })); }
    }
    if (req.method === 'GET' && path === '/') {
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
      res.setHeader('Content-Security-Policy', "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; connect-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'");
      return res.end(html);
    }
    if (req.method === 'GET' && path === '/health') return res.writeHead(200, { 'Content-Type': 'application/json' }).end(JSON.stringify({ status: 'ok', version: '0.5.0' }));
    if (path !== '/mcp') return res.writeHead(404).end('Not found');
    if (req.method === 'OPTIONS') return res.writeHead(204, {
      'Access-Control-Allow-Methods': 'POST, GET, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'content-type, mcp-protocol-version, mcp-session-id',
      'Access-Control-Expose-Headers': 'mcp-session-id'
    }).end();
    if (!['POST', 'GET', 'DELETE'].includes(req.method)) return res.writeHead(405, { Allow: 'POST, GET, DELETE, OPTIONS' }).end('Method not allowed');
    let body;
    if (req.method === 'POST') {
      if (!(req.headers['content-type'] ?? '').toLowerCase().startsWith('application/json')) return res.writeHead(415).end('JSON required');
      if (Number(req.headers['content-length']) > MAX_BODY) return res.writeHead(413).end('Request too large');
      let length = 0; const chunks = [];
      try {
        for await (const chunk of req) {
          length += chunk.length;
          if (length > MAX_BODY) { res.writeHead(413).end('Request too large'); return; }
          chunks.push(chunk);
        }
        body = JSON.parse(Buffer.concat(chunks).toString('utf8'));
      } catch { if (!res.headersSent) res.writeHead(400).end('Invalid JSON'); return; }
    }
    const server = createCalculatorServer();
    const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined, enableJsonResponse: true });
    res.on('close', () => { void transport.close(); void server.close(); });
    try { await server.connect(transport); await transport.handleRequest(req, res, body); }
    catch { if (!res.headersSent) res.writeHead(500).end('MCP request failed'); }
  });
  server.setTimeout(20000, socket => socket.destroy());
  return server;
}

export function closeHttpServer(server, { graceMs = 5000 } = {}) {
  if (!Number.isInteger(graceMs) || graceMs < 0) throw new Error('Shutdown grace must be a nonnegative integer.');
  return new Promise((resolve, reject) => {
    const deadline = setTimeout(() => server.closeAllConnections(), graceMs);
    deadline.unref();
    server.close(error => {
      clearTimeout(deadline);
      if (error && error.code !== 'ERR_SERVER_NOT_RUNNING') reject(error);
      else resolve();
    });
    server.closeIdleConnections();
  });
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const port = Number(process.env.PORT ?? 4317);
  const host = process.env.BIND_ADDRESS ?? '127.0.0.1';
  if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('PORT must be an integer from 1 to 65535.');
  if (!['127.0.0.1', '::1'].includes(host) && !process.env.PUBLIC_BASE_URL) throw new Error('Non-loopback binding requires an approved HTTPS PUBLIC_BASE_URL.');
  const server = createHttpServer({ publicBaseUrl: process.env.PUBLIC_BASE_URL });
  server.listen(port, host, () => console.log(`Calculator preview: http://${host}:${port}\nMCP endpoint: http://${host}:${port}/mcp`));
  let stopping = false;
  const stop = () => {
    if (stopping) return;
    stopping = true;
    void closeHttpServer(server).then(() => process.exit(0), () => process.exit(1));
  };
  process.once('SIGINT', stop); process.once('SIGTERM', stop);
}
