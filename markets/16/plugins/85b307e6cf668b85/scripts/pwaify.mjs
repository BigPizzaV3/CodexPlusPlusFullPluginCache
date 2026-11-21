#!/usr/bin/env node
// Copy an explicitly approved static shell into a new, local PWA output.
import fs from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { makeIcon } from './icons.mjs';
import { options, required } from './options.mjs';

const TYPES = new Set(['.html', '.js', '.mjs', '.css', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg', '.ico', '.woff', '.woff2', '.ttf', '.otf', '.wasm']);
export const digest = bytes => createHash('sha256').update(bytes).digest('hex');

export function publicPath(value) {
  if (typeof value !== 'string' || !/^[a-zA-Z0-9_./-]+$/.test(value) || value.startsWith('/') || value.includes('//')) throw new Error(`Invalid public asset path: ${value}`);
  const parts = value.split('/');
  if (parts.some(p => !p || p.startsWith('.') || /^(api|private|secret|secrets|local-state|node_modules|device-it)$/i.test(p))) throw new Error(`Reserved or private asset path: ${value}`);
  if (!TYPES.has(path.extname(value).toLowerCase())) throw new Error(`Unsupported static asset type: ${value}`);
  return value;
}

export async function prepare(args) {
  const input = await fs.realpath(required(args, 'dist'));
  const requestedOutput = path.resolve(required(args, 'out'));
  const parent = await fs.realpath(path.dirname(requestedOutput));
  const output = path.join(parent, path.basename(requestedOutput));
  if (output === input || output.startsWith(input + path.sep) || input.startsWith(output + path.sep)) throw new Error('Input and output must be separate, non-nested directories');
  try { await fs.lstat(output); throw new Error('Output already exists. Choose a new path; nothing is overwritten'); } catch (e) { if (e.code !== 'ENOENT') throw e; }
  const name = required(args, 'name').trim();
  if (!name || name.length > 80) throw new Error('Name must contain 1 to 80 characters');
  const theme = args.theme ?? '#2155CD';
  if (!/^#[0-9a-f]{6}$/i.test(theme)) throw new Error('Theme must be a six-digit hex color');
  const selected = JSON.parse(await fs.readFile(required(args, 'assets'), 'utf8'));
  if (!Array.isArray(selected) || selected.length > 1000 || !selected.includes('index.html')) throw new Error('Assets must be a JSON array of at most 1000 public file paths, including index.html');
  if (new Set(selected).size !== selected.length) throw new Error('Duplicate assets are not allowed');
  const rootFiles = await fs.readdir(input);
  if (rootFiles.some(f => /^(manifest(?:\.json|\.webmanifest)|sw\.js|service-worker(?:\.min)?\.js|device-it(?:\..*)?)$/i.test(f) || /\.webmanifest$/i.test(f))) throw new Error('Input already contains PWA files. Preserve them and use their existing PWA workflow');
  const files = new Map();
  let total = 0;
  for (const item of selected) {
    const rel = publicPath(item);
    let current = input;
    for (const segment of rel.split('/')) {
      current = path.join(current, segment);
      if ((await fs.lstat(current)).isSymbolicLink()) throw new Error(`Symlink is not allowed: ${rel}`);
    }
    const stat = await fs.stat(current);
    if (!stat.isFile() || stat.size > 8 * 1024 * 1024) throw new Error(`Asset is not a regular file of at most 8 MiB: ${rel}`);
    total += stat.size;
    if (total > 64 * 1024 * 1024) throw new Error('Selected assets exceed 64 MiB');
    const bytes = await fs.readFile(current);
    if (/\.(html|m?js)$/i.test(rel) && /serviceWorker|rel\s*=\s*["']?manifest\b/i.test(bytes.toString('utf8'))) throw new Error(`Existing PWA registration or manifest reference in ${rel}; input is preserved`);
    files.set(rel, bytes);
  }
  let html = files.get('index.html').toString('utf8');
  if (!/<head\b/i.test(html) || !/<\/head\s*>/i.test(html) || !/<\/body\s*>/i.test(html) || /<base\b/i.test(html)) throw new Error('index.html needs normal head/body tags and no base URL override');
  const manifest = {
    id: './', name, short_name: name.slice(0, 12), start_url: './', scope: './', display: 'standalone',
    background_color: '#FFFFFF', theme_color: theme,
    icons: [
      { src: './device-it/icon-192.png', sizes: '192x192', type: 'image/png' },
      { src: './device-it/icon-512.png', sizes: '512x512', type: 'image/png' },
      { src: './device-it/icon-maskable-512.png', sizes: '512x512', type: 'image/png', purpose: 'maskable' },
    ],
  };
  html = html.replace(/<\/head\s*>/i, `<link rel="manifest" href="./manifest.webmanifest">\n<link rel="apple-touch-icon" href="./device-it/apple-touch-icon-180.png">\n<meta name="theme-color" content="${theme}">\n</head>`);
  html = html.replace(/<\/body\s*>/i, '<script src="./device-it/register.js" defer></script>\n</body>');
  files.set('index.html', Buffer.from(html));
  files.set('manifest.webmanifest', Buffer.from(JSON.stringify(manifest, null, 2) + '\n'));
  files.set('device-it/register.js', Buffer.from("if ('serviceWorker' in navigator) navigator.serviceWorker.register('./sw.js', {scope:'./'}).catch(error => console.error('Device It service worker:', error.message));\n"));
  for (const [file, size] of [['icon-192.png', 192], ['icon-512.png', 512], ['icon-maskable-512.png', 512], ['apple-touch-icon-180.png', 180]]) files.set(`device-it/${file}`, makeIcon(size, theme));
  const entries = [...files].map(([file, bytes]) => ({ file, sha256: digest(bytes) })).sort((a, b) => a.file.localeCompare(b.file));
  const revision = digest(JSON.stringify(entries)).slice(0, 20);
  files.set('sw.js', Buffer.from(serviceWorker(entries.map(x => x.file), revision)));
  const inventory = { format: 1, name, revision, publicAssets: [...files.keys()].sort(), precache: entries, limits: 'Exact public static files only. No runtime cache, API cache, off-origin cache, query cache or deep-route fallback.' };
  files.set('device-it-build.json', Buffer.from(JSON.stringify(inventory, null, 2) + '\n'));
  const temporary = await fs.mkdtemp(path.join(parent, '.device-it-prepare-'));
  try {
    for (const [rel, bytes] of files) {
      await fs.mkdir(path.dirname(path.join(temporary, rel)), { recursive: true });
      await fs.writeFile(path.join(temporary, rel), bytes, { flag: 'wx' });
    }
    // mkdir is the final exclusive claim; copy only into a directory we just created.
    await fs.mkdir(output);
    try {
      for (const entry of await fs.readdir(temporary)) {
        await fs.cp(path.join(temporary, entry), path.join(output, entry), { recursive: true, force: false, errorOnExist: true });
      }
    }
    catch (e) { await fs.rm(output, { recursive: true, force: true }); throw e; }
  } finally { await fs.rm(temporary, { recursive: true, force: true }); }
  return { ok: true, output, name, revision, precachedFiles: entries.length, icon: 'Generated generic device placeholder', sourceChanged: false };
}

function serviceWorker(files, revision) {
  return `// Device It: an exact public static precache; network responses are never added at runtime.
const FILES = ${JSON.stringify(files)};
const PREFIX = 'device-it:' + self.registration.scope + ':';
const CACHE = PREFIX + ${JSON.stringify(revision)};
const URLS = FILES.map(file => new URL(file, self.registration.scope).href);
const ALLOWED = new Set(URLS);
self.addEventListener('install', event => event.waitUntil((async () => {
  const cache = await caches.open(CACHE);
  try {
    for (const url of URLS) {
      const response = await fetch(new Request(url, {credentials:'omit', cache:'reload'}));
      if (!response.ok || response.redirected || response.type !== 'basic' || /(?:no-store|private)/i.test(response.headers.get('cache-control') || '')) throw new Error('Asset is not public and cacheable: ' + url);
      await cache.put(url, response);
    }
  } catch (error) { await caches.delete(CACHE); throw error; }
  await self.skipWaiting();
})()));
self.addEventListener('activate', event => event.waitUntil((async () => {
  for (const name of await caches.keys()) if (name.startsWith(PREFIX) && name !== CACHE) await caches.delete(name);
  await self.clients.claim();
})()));
self.addEventListener('fetch', event => {
  const request = event.request;
  const url = new URL(request.url);
  if (request.method !== 'GET' || request.headers.has('authorization') || url.origin !== self.location.origin || url.search) return;
  if (url.href === self.registration.scope) url.pathname += 'index.html';
  if (!ALLOWED.has(url.href)) return;
  event.respondWith(caches.open(CACHE).then(cache => cache.match(url.href)).then(response => response || fetch(request)));
});
`;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try { console.log(JSON.stringify(await prepare(options(process.argv.slice(2), ['dist', 'out', 'name', 'assets', 'theme'])), null, 2)); }
  catch (error) { console.error(`device-it prepare: ${error.message}`); process.exitCode = 1; }
}
