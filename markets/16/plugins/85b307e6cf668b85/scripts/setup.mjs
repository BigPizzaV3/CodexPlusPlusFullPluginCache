#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const installArgs = ['ci', '--ignore-scripts', '--no-audit', '--no-fund', '--include=dev', '--include=optional'];

export function runCommand(command, args, cwd, install = false) {
  // Windows npm is a .cmd launcher. Only fixed npm arguments pass through cmd.exe.
  if (process.platform === 'win32' && command === 'npm') {
    args = ['/d', '/s', '/c', `npm ${args.join(' ')}`];
    command = 'cmd.exe';
  }
  return spawnSync(command, args, { cwd, encoding: 'utf8', stdio: install ? ['ignore', 2, 2] : 'pipe', maxBuffer: 1024 * 1024, env: install ? { ...process.env, PLAYWRIGHT_SKIP_BROWSER_GC: '1' } : process.env });
}

export async function dependencyState(directory) {
  const pkg = JSON.parse(await fs.readFile(path.join(directory, 'package.json'), 'utf8'));
  const lock = JSON.parse(await fs.readFile(path.join(directory, 'package-lock.json'), 'utf8'));
  for (const group of ['dependencies', 'devDependencies']) {
    for (const [name, version] of Object.entries(pkg[group] || {})) {
      if (!/^\d+\.\d+\.\d+$/.test(version) || lock.packages?.['']?.[group]?.[name] !== version || lock.packages?.[`node_modules/${name}`]?.version !== version) {
        throw new Error(`Package and lock disagree for ${name}; restore the supplied package files before setup`);
      }
    }
  }
  try {
    if ((await fs.lstat(path.join(directory, 'node_modules'))).isSymbolicLink()) throw new Error('node_modules is a symlink; use a separate package extraction before setup');
  } catch (error) { if (error.code !== 'ENOENT') throw error; }
  const issues = [];
  let checkedPackages = 0;
  for (const [relative, entry] of Object.entries(lock.packages || {})) {
    if (!relative) continue;
    if (!relative.startsWith('node_modules/') || relative.split('/').includes('..') || !entry.version || entry.link) throw new Error('Unsupported dependency lock entry; restore the supplied lockfile');
    checkedPackages++;
    try {
      const installed = JSON.parse(await fs.readFile(path.join(directory, relative, 'package.json'), 'utf8'));
      if (installed.version !== entry.version) issues.push(`${relative}: expected ${entry.version}, found ${installed.version}`);
    } catch (error) {
      if (entry.optional && error.code === 'ENOENT') continue;
      issues.push(`${relative}: missing or unreadable package`);
    }
  }
  if (!checkedPackages) throw new Error('Empty dependency lock; restore the supplied lockfile');
  return { ok: issues.length === 0, checkedPackages, issues };
}

async function browserProbe(directory, run) {
  const result = run(process.execPath, [path.join(directory, 'scripts/setup.mjs'), '--probe-browser'], directory);
  if (result.status !== 0) return { ok: false, phase: 'browser', missing: false, error: `Browser probe process failed (${result.error?.code || result.status}); inspect local runtime access` };
  try { return JSON.parse(result.stdout); }
  catch { return { ok: false, phase: 'browser', missing: false, error: 'Browser probe did not return a readiness result' }; }
}

export async function setup({ install = false, directory = root, nodeVersion = process.versions.node, run = runCommand, probe = browserProbe } = {}) {
  const result = { ok: false, mode: install ? 'setup' : 'preflight', root: directory, runtime: { node: nodeVersion, platform: process.platform, arch: process.arch }, actions: [], nextSteps: [] };
  if (!/^\d+\.\d+\.\d+$/.test(nodeVersion) || Number(nodeVersion.split('.')[0]) < 22) {
    result.nextSteps.push(`Install Node.js 22 or newer with npm on this local host, then rerun node scripts/run.mjs ${result.mode}. No runtime was installed.`);
    return result;
  }
  const npm = run('npm', ['--version'], directory);
  if (npm.status !== 0 || !/^\d+\.\d+\.\d+\s*$/.test(npm.stdout || '')) {
    result.runtime.npm = 'unavailable';
    result.nextSteps.push('Make npm available on PATH with your local Node.js installation, then rerun this command. No dependencies were installed.');
    return result;
  }
  result.runtime.npm = npm.stdout.trim();
  let dependenciesInstalled = false;
  async function installDependencies() {
    const installed = run('npm', installArgs, directory, true);
    result.actions.push({ command: `npm ${installArgs.join(' ')}`, exitCode: installed.status, ok: installed.status === 0 });
    if (installed.status !== 0) throw new Error('Locked dependency installation failed. Check the command output and npm registry/network access, then rerun setup. No fallback installer ran.');
    dependenciesInstalled = true;
    result.dependencies = await dependencyState(directory);
    if (!result.dependencies.ok) throw new Error('Locked dependency installation completed but required package versions are still missing. Check npm output before rerunning setup.');
  }
  try {
    result.dependencies = await dependencyState(directory);
    if (!result.dependencies.ok) {
      if (!install) { result.nextSteps.push('Run node scripts/run.mjs setup when dependency/browser downloads are authorized.'); return result; }
      await installDependencies();
    }
    result.browser = await probe(directory, run);
    if (result.browser.phase === 'dependencies' && install && !dependenciesInstalled) {
      await installDependencies();
      result.browser = await probe(directory, run);
    }
    if (!result.browser.ok && result.browser.missing && install) {
      const args = [path.join(directory, 'node_modules/playwright/cli.js'), 'install', 'chromium'];
      const installed = run(process.execPath, args, directory, true);
      result.actions.push({ command: 'node node_modules/playwright/cli.js install chromium', exitCode: installed.status, ok: installed.status === 0 });
      if (installed.status !== 0) throw new Error('Pinned Chromium download failed. Check the command output and network/cache permissions, then rerun setup. No system packages were installed.');
      result.browser = await probe(directory, run);
    }
    if (!result.browser.ok) {
      result.nextSteps.push(result.browser.phase === 'dependencies' ? 'Run node scripts/run.mjs setup to repair incomplete package dependencies when downloads are authorized.' : result.browser.missing ? 'Run node scripts/run.mjs setup when the pinned Chromium download is authorized.' : 'Read browser.error below. Resolve the local browser/runtime or OS dependency problem, then rerun preflight. Setup never installs OS packages.');
      return result;
    }
    result.ok = true;
    result.nextSteps.push('Ready. Follow FIRST-RUN.md: select approved public assets, prepare a fresh output, preview it, then verify the known shell text.');
  } catch (error) { result.error = error.message; result.nextSteps.push('Resolve the reported error before preparing an app.'); }
  return result;
}

async function probeLocalBrowser() {
  let browser, result;
  try {
    const require = createRequire(path.join(root, 'package.json'));
    let chromium;
    try {
      ({ chromium } = require('playwright'));
      for (const name of ['qrcode', 'pngjs', 'jsqr']) require(name);
    } catch (error) { return { ok: false, phase: 'dependencies', missing: false, error: error.message }; }
    try {
      browser = await chromium.launch({ headless: true, timeout: 15000 });
      result = { ok: true, phase: 'browser', version: browser.version(), executable: chromium.executablePath(), browserClosed: false };
    } catch (error) {
      result = { ok: false, phase: 'browser', missing: /Executable doesn't exist at /.test(error.message), error: error.message.slice(0, 2500) };
    }
  } finally {
    if (browser) {
      try { await browser.close(); result.browserClosed = true; }
      catch (error) { result.ok = false; result.error = `Browser cleanup failed: ${error.message}`; }
    }
  }
  return result;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  if (process.argv[2] === '--probe-browser' && process.argv.length === 3) {
    console.log(JSON.stringify(await probeLocalBrowser()));
  } else if (process.argv.length === 2 || (process.argv.length === 3 && process.argv[2] === '--check')) {
    const result = await setup({ install: process.argv[2] !== '--check' });
    console.log(JSON.stringify(result, null, 2));
    if (!result.ok) process.exitCode = 1;
  } else { console.error('Usage: node scripts/setup.mjs [--check]'); process.exitCode = 1; }
}
