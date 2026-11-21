import fs from 'node:fs/promises';
import http from 'node:http';
import os from 'node:os';
import path from 'node:path';
import { required } from './options.mjs';
import { writeQR } from './qr.mjs';

const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8', '.css': 'text/css', '.json': 'application/json', '.webmanifest': 'application/manifest+json', '.png': 'image/png', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.gif': 'image/gif', '.ico': 'image/x-icon', '.wasm': 'application/wasm', '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.otf': 'font/otf' };
export async function createPreview(args) {
  const dir = await fs.realpath(required(args, 'dir'));
  const inventory = JSON.parse(await fs.readFile(path.join(dir, 'device-it-build.json'), 'utf8'));
  if (inventory.format !== 1 || !Array.isArray(inventory.publicAssets)) throw new Error('Not a Device It prepared output');
  const port = args.port === undefined ? 0 : Number(args.port);
  if (!Number.isInteger(port) || port < 0 || port > 65535) throw new Error('Port must be 0 to 65535');
  if (args['lan-address']) {
    const addresses = Object.values(os.networkInterfaces()).flat().filter(x => x && !x.internal && x.family === 'IPv4').map(x => x.address);
    if (!addresses.includes(args['lan-address'])) throw new Error('LAN address must be an IPv4 address on this computer');
  }
  const allowed = new Set([...inventory.publicAssets, 'device-it-build.json']);
  for (const file of allowed) {
    if (typeof file !== 'string' || !/^[A-Za-z0-9_./-]+$/.test(file) || file.split('/').some(part => !part || part.startsWith('.'))) throw new Error('Invalid prepared inventory path');
    let current = dir;
    for (const segment of file.split('/')) {
      current = path.join(current, segment);
      if ((await fs.lstat(current)).isSymbolicLink()) throw new Error('Prepared output must not contain symlinks');
    }
  }
  const host = args['lan-address'] ? '0.0.0.0' : '127.0.0.1';
  const server = http.createServer(async (request, response) => {
    try {
      const localHosts = new Set([`127.0.0.1:${server.address().port}`, `localhost:${server.address().port}`, ...(args['lan-address'] ? [`${args['lan-address']}:${server.address().port}`] : [])]);
      if (!localHosts.has(request.headers.host) || !['GET', 'HEAD'].includes(request.method)) { response.writeHead(403).end(); return; }
      const url = new URL(request.url, `http://${request.headers.host}`);
      const rel = url.pathname === '/' ? 'index.html' : decodeURIComponent(url.pathname.slice(1));
      if (url.search || !allowed.has(rel)) { response.writeHead(404).end(); return; }
      const file = path.join(dir, rel);
      const resolved = await fs.realpath(file);
      if (!resolved.startsWith(dir + path.sep)) { response.writeHead(403).end(); return; }
      const bytes = await fs.readFile(file);
      response.writeHead(200, { 'Content-Type': MIME[path.extname(file)] ?? 'application/octet-stream', 'Cache-Control': 'no-cache', 'X-Content-Type-Options': 'nosniff', 'Referrer-Policy': 'no-referrer', 'Content-Security-Policy': "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'" });
      response.end(request.method === 'HEAD' ? undefined : bytes);
    } catch { response.writeHead(404).end(); }
  });
  await new Promise((resolve, reject) => { server.once('error', reject); server.listen(port, host, resolve); });
  const loopbackURL = `http://127.0.0.1:${server.address().port}/`;
  const url = args['lan-address'] ? `http://${args['lan-address']}:${server.address().port}/` : loopbackURL;
  return { server, url, loopbackURL, host, dir };
}
export async function preview(args) {
  required(args, 'qr');
  const runtime = await createPreview(args);
  const stop = () => { runtime.server.closeAllConnections(); runtime.server.close(); };
  try {
    const qr = await writeQR(runtime.url, args.qr);
    console.log(JSON.stringify({ ok: true, ...qr, loopbackURL: runtime.loopbackURL, pid: process.pid, host: runtime.host, note: args['lan-address'] ? 'LAN HTTP preview only. Phones generally cannot use service workers on this insecure origin; no installation claim.' : 'Loopback URL works on this computer only. QR is not a phone installation.', stop: 'Ctrl+C in this terminal' }));
    process.once('SIGINT', stop);
    process.once('SIGTERM', stop);
  } catch (error) { stop(); throw error; }
}
