import { readFileSync, existsSync } from 'node:fs';
import { mkdir, readFile, writeFile, rm, stat } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { randomUUID } from 'node:crypto';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { setTimeout as delay } from 'node:timers/promises';
import sharp from 'sharp';
import { DocumentError } from './errors.mjs';

const exec = promisify(execFile);
const simctl = async (args, timeout = 30_000) => (await exec('/usr/bin/xcrun', ['simctl', ...args], { timeout, maxBuffer: 2 * 1024 * 1024 })).stdout.trim();

export async function contactSheet(slides) {
  const columns = Math.min(4, slides.length), thumb = 300, gutter = 16, label = 28;
  const height = Math.round(thumb * slides[0].height / slides[0].width);
  const width = gutter + columns * (thumb + gutter);
  const rows = Math.ceil(slides.length / columns);
  const layers = [];
  for (const [index, slide] of slides.entries()) {
    const left = gutter + (index % columns) * (thumb + gutter);
    const top = gutter + Math.floor(index / columns) * (height + label + gutter);
    layers.push({ input: await sharp(slide.bytes).resize(thumb, height).png().toBuffer(), left, top });
    layers.push({ input: Buffer.from(`<svg width="${thumb}" height="${label}"><text x="${thumb / 2}" y="20" text-anchor="middle" font-size="14" font-family="sans-serif" fill="#444">${index + 1} / ${slides.length}</text></svg>`), left, top: top + height });
  }
  return sharp({ create: { width, height: gutter + rows * (height + label + gutter), channels: 3, background: '#eeeeee' } }).composite(layers).png().toBuffer();
}

/** The renderer is a local macOS worker; its capability must never be advertised on Linux. */
export function nativeRenderer(configPath = process.env.CAROUSEL_RENDERER_CONFIG) {
  if (!configPath) return null;
  if (process.platform !== 'darwin') throw new Error('Native ACE rendering requires macOS and Xcode Simulator');
  const config = JSON.parse(readFileSync(configPath, 'utf8'));
  if (config.protocol !== 1 || config.engine !== 'ACE SlideRasterizer' || !/^[a-f0-9-]{36}$/i.test(config.device)
      || config.bundleId !== 'software.quokka.ace-plugin-renderer' || !existsSync(config.app)) throw new Error('Invalid native renderer configuration; run setup-native-renderer.mjs');
  let pending = 0, tail = Promise.resolve();
  const metadata = { engine: config.engine, protocol: config.protocol, rasterizer_sha256: config.rasterizer_sha256, built_at: config.built_at };
  return {
    metadata,
    async render(archive, { width = 720, slideCount } = {}) {
      if (!Number.isInteger(width) || width < 360 || width > 1080) throw new DocumentError('Preview width must be 360…1080 pixels');
      if (pending >= 3) throw new DocumentError('Native renderer is busy. Retry after the current previews finish.');
      pending++;
      const work = tail.then(() => renderNative(configPath, config, archive, width, slideCount));
      tail = work.catch(() => {});
      try { return { ...await work, engine: metadata }; } finally { pending--; }
    }
  };
}

// A file lock also serializes CLI and MCP requests targeting the same worker.
async function lockRenderer(path) {
  const deadline = Date.now() + 45_000;
  while (true) {
    try {
      await mkdir(path);
      try { await writeFile(join(path, 'pid'), String(process.pid)); }
      catch (error) { await rm(path, { recursive: true, force: true }); throw error; }
      return () => rm(path, { recursive: true, force: true });
    } catch (error) {
      if (error.code !== 'EEXIST') throw error;
      try {
        const pid = Number(await readFile(join(path, 'pid'), 'utf8'));
        if (Number.isInteger(pid) && pid > 0) {
          try { process.kill(pid, 0); }
          catch (error) { if (error.code === 'ESRCH') { await rm(path, { recursive: true, force: true }); continue; } }
        }
      } catch (error) {
        if (error.code === 'ENOENT' && Date.now() - (await stat(path).catch(() => ({ mtimeMs: Date.now() }))).mtimeMs > 60_000) {
          await rm(path, { recursive: true, force: true }); continue;
        }
      }
      if (Date.now() > deadline) throw new DocumentError('Another native preview is still running; try again shortly');
      await delay(200);
    }
  }
}

async function renderNative(configPath, config, archive, width, slideCount) {
  const unlock = await lockRenderer(join(dirname(configPath), 'render.lock'));
  let job;
  try {
    const devices = JSON.parse(await simctl(['list', 'devices', 'available', '-j'])).devices;
    const device = Object.values(devices).flat().find(device => device.udid === config.device);
    if (!device) throw new DocumentError('ACE preview simulator is unavailable; run setup-native-renderer.mjs');
    if (device.state !== 'Booted') {
      await simctl(['boot', config.device]);
      await simctl(['bootstatus', config.device, '-b'], 120_000);
    }
    const container = await simctl(['get_app_container', config.device, config.bundleId, 'data']);
    const id = randomUUID();
    job = join(container, 'Documents', 'RenderJobs', id);
    await mkdir(job, { recursive: true });
    await writeFile(join(job, 'input.carousel'), archive);
    await writeFile(join(job, 'request.json'), JSON.stringify({ width }));
    const launch = await simctl(['launch', '--terminate-running-process', config.device, config.bundleId, '--render-job', id]);
    const workerPID = Number(launch.match(/:\s*(\d+)$/)?.[1]);
    const deadline = Date.now() + 90_000;
    let result;
    while (!result) {
      try { result = JSON.parse(await readFile(join(job, 'result.json'), 'utf8')); }
      catch (error) { if (error.code !== 'ENOENT') throw error; }
      if (!result && Number.isInteger(workerPID) && workerPID > 0) {
        try { process.kill(workerPID, 0); }
        catch (error) {
          if (error.code === 'ESRCH') {
            result = await readFile(join(job, 'result.json'), 'utf8').then(JSON.parse).catch(() => null);
            if (!result) throw new DocumentError('Native renderer exited without a preview. Rebuild the worker or inspect its crash report.');
          }
        }
      }
      if (!result && Date.now() > deadline) throw new DocumentError('Native preview timed out; the editable project is still available');
      if (!result) await delay(100);
    }
    if (result.ok !== true) throw new DocumentError(`Native renderer: ${result.error ?? 'unknown failure'}`);
    if (!Array.isArray(result.slides) || result.slides.length !== slideCount) throw new DocumentError('Native preview did not return every slide');
    const slides = [];
    for (const [index, item] of result.slides.entries()) {
      if (item.file !== `slide-${String(index + 1).padStart(2, '0')}.png` || item.width !== width || !Number.isInteger(item.height) || item.height < 1 || item.height > 1920) throw new DocumentError('Invalid native preview output');
      const bytes = await readFile(join(job, item.file));
      if (bytes.length > 12 * 1024 * 1024) throw new DocumentError('Native preview exceeds its size limit');
      const info = await sharp(bytes, { limitInputPixels: 2_100_000 }).metadata();
      if (info.format !== 'png' || info.width !== width || info.height !== item.height) throw new DocumentError('Native preview image dimensions do not match');
      slides.push({ ...item, bytes });
    }
    return { slides, sheet: await contactSheet(slides), warnings: result.warnings ?? [] };
  } finally {
    if (job) {
      await simctl(['terminate', config.device, config.bundleId]).catch(() => {});
      await rm(job, { recursive: true, force: true });
    }
    await unlock();
  }
}
