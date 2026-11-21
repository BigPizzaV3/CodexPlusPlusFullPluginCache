#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';
import { localURL } from './qr.mjs';
import { options, required } from './options.mjs';

export async function verify(args) {
  const url = localURL(required(args, 'url'));
  if (!['localhost', '127.0.0.1'].includes(url.hostname) || url.pathname !== '/') throw new Error('Offline verification requires a root-mounted loopback URL on this computer');
  const expected = required(args, 'expect-text').trim();
  if (!expected) throw new Error('Expected visible text must not be empty');
  for (const file of [args.report, args.screenshot].filter(Boolean)) {
    try { await fs.lstat(file); throw new Error(`Evidence path already exists: ${file}`); } catch (e) { if (e.code !== 'ENOENT') throw e; }
  }
  const results = [];
  const check = (name, ok, detail = '') => { results.push({ name, ok: Boolean(ok), detail }); };
  const report = { url: url.href, ok: false, offline: 'not verified', browserStarted: false, browserClosed: false, results };
  let browser;
  async function get(file) {
    const target = new URL(file, url);
    if (target.origin !== url.origin || target.search) throw new Error('Unexpected non-local asset URL');
    const response = await fetch(target, { redirect: 'error', signal: AbortSignal.timeout(10000) });
    if (!response.ok) throw new Error(`${file}: HTTP ${response.status}`);
    return response;
  }
  try {
    const manifest = await (await get('manifest.webmanifest')).json();
    const inventory = await (await get('device-it-build.json')).json();
    check('manifest has local standalone scope', manifest.display === 'standalone' && manifest.start_url === './' && manifest.scope === './');
    const icons = [...manifest.icons, { src: './device-it/apple-touch-icon-180.png', sizes: '180x180' }];
    check('manifest includes 192, 512 and maskable icons', manifest.icons.some(x => x.sizes === '192x192') && manifest.icons.some(x => x.sizes === '512x512' && x.purpose === 'maskable'));
    for (const icon of icons) {
      const bytes = Buffer.from(await (await get(icon.src)).arrayBuffer());
      const [width, height] = icon.sizes.split('x').map(Number);
      check(`PNG icon ${icon.sizes}${icon.purpose ? ' ' + icon.purpose : ''}`, bytes.length > 24 && bytes.subarray(0, 8).equals(Buffer.from([137, 80, 78, 71, 13, 10, 26, 10])) && bytes.readUInt32BE(16) === width && bytes.readUInt32BE(20) === height);
    }
    browser = await chromium.launch({ headless: true });
    report.browserStarted = true;
    report.browserVersion = browser.version();
    const context = await browser.newContext();
    // Verification visits only this local origin, in a disposable browser profile.
    await context.route('**/*', route => new URL(route.request().url()).origin === url.origin ? route.continue() : route.abort());
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(url.href, { waitUntil: 'load', timeout: 15000 });
    check('expected online shell is visible', (await page.locator('body').innerText()).includes(expected));
    await page.waitForFunction(() => navigator.serviceWorker?.controller !== null && navigator.serviceWorker?.controller !== undefined, null, { timeout: 15000 });
    const state = await page.evaluate(async () => {
      const registration = await navigator.serviceWorker.ready;
      return { state: registration.active?.state, script: registration.active?.scriptURL, scope: registration.scope };
    });
    check('service worker activated for local root', state.state === 'activated' && state.scope === url.href && state.script === new URL('sw.js', url).href, state);
    const cached = await page.evaluate(async () => {
      const result = [];
      for (const name of await caches.keys()) {
        const cache = await caches.open(name);
        for (const request of await cache.keys()) {
          const response = await cache.match(request);
          const hash = [...new Uint8Array(await crypto.subtle.digest('SHA-256', await response.arrayBuffer()))].map(x => x.toString(16).padStart(2, '0')).join('');
          result.push({ url: request.url, sha256: hash, cache: name });
        }
      }
      return result;
    });
    const expectedCache = inventory.precache.map(entry => ({ url: new URL(entry.file, url).href, sha256: entry.sha256 }));
    check('cache contains exactly approved static bytes', cached.length === expectedCache.length && expectedCache.every(entry => cached.some(actual => actual.url === entry.url && actual.sha256 === entry.sha256)));
    report.cachedAssets = cached;
    await context.setOffline(true);
    await page.reload({ waitUntil: 'load', timeout: 15000 });
    const offlineVisible = (await page.locator('body').innerText()).includes(expected);
    check('expected offline shell is visible after reload', offlineVisible);
    report.offline = offlineVisible ? 'verified shell' : 'failed';
    check('no uncaught page errors', errors.length === 0, errors);
    if (args.screenshot) await fs.writeFile(args.screenshot, await page.screenshot({ fullPage: true }), { flag: 'wx' });
  } catch (error) {
    check('verification completed', false, error.message);
  } finally {
    if (browser) {
      try { await browser.close(); report.browserClosed = true; }
      catch (error) { check('browser cleanup', false, error.message); }
    }
  }
  report.ok = report.browserStarted && report.browserClosed && results.every(x => x.ok);
  if (args.report) await fs.writeFile(args.report, JSON.stringify(report, null, 2) + '\n', { flag: 'wx' });
  return report;
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const report = await verify(options(process.argv.slice(2), ['url', 'expect-text', 'report', 'screenshot']));
    console.log(JSON.stringify(report, null, 2));
    if (!report.ok) process.exitCode = 1;
  } catch (error) { console.error(`device-it verify: ${error.message}`); process.exitCode = 1; }
}
