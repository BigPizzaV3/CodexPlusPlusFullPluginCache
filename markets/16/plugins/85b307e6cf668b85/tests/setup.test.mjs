import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import { mkdirSync, writeFileSync } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { dependencyState, setup, runCommand } from '../scripts/setup.mjs';

async function fixture(t, installed = true) {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), 'device-it-setup-test-'));
  t.after(() => fs.rm(directory, { recursive: true, force: true }));
  await fs.writeFile(path.join(directory, 'package.json'), JSON.stringify({ dependencies: { fixture: '1.0.0' } }));
  await fs.writeFile(path.join(directory, 'package-lock.json'), JSON.stringify({ packages: { '': { dependencies: { fixture: '1.0.0' } }, 'node_modules/fixture': { version: '1.0.0' }, 'node_modules/optional-fixture': { version: '1.0.0', optional: true } } }));
  const install = (version = '1.0.0') => {
    mkdirSync(path.join(directory, 'node_modules/fixture'), { recursive: true });
    writeFileSync(path.join(directory, 'node_modules/fixture/package.json'), JSON.stringify({ version }));
  };
  if (installed) install();
  const commands = [];
  const run = (command, args, cwd, mutation) => {
    commands.push({ command, args, cwd, mutation });
    if (command === 'npm' && args[0] === '--version') return { status: 0, stdout: '10.9.4\n' };
    if (command === 'npm' && args[0] === 'ci') install();
    return { status: 0, stdout: '' };
  };
  return { directory, run, commands, writePackage: install };
}
const ready = async () => ({ ok: true, phase: 'browser', browserClosed: true, version: 'fixture' });

test('installation disables browser cache deletion without changing parent environment', async t => {
  const f = await fixture(t);
  const output = path.join(f.directory, 'child-cache-setting.txt');
  const before = process.env.PLAYWRIGHT_SKIP_BROWSER_GC;
  const result = runCommand(process.execPath, ['-e', "require('node:fs').writeFileSync(process.argv[1], process.env.PLAYWRIGHT_SKIP_BROWSER_GC)", output], f.directory, true);
  assert.equal(result.status, 0);
  assert.equal(await fs.readFile(output, 'utf8'), '1');
  assert.equal(process.env.PLAYWRIGHT_SKIP_BROWSER_GC, before);
});

test('readiness checks full lock versions and tolerates absent optional packages', async t => {
  const f = await fixture(t);
  assert.deepEqual(await dependencyState(f.directory), { ok: true, checkedPackages: 2, issues: [] });
  f.writePackage('2.0.0');
  const state = await dependencyState(f.directory);
  assert.equal(state.ok, false);
  assert.match(state.issues[0], /expected 1.0.0, found 2.0.0/);
});

test('lock mismatch and node_modules symlink refuse installation', async t => {
  const f = await fixture(t, false);
  await fs.writeFile(path.join(f.directory, 'package.json'), JSON.stringify({ dependencies: { fixture: '2.0.0' } }));
  let result = await setup({ ...f, install: true, probe: ready });
  assert.equal(result.ok, false);
  assert.match(result.error, /Package and lock disagree/);
  assert.equal(result.actions.length, 0);
  await fs.writeFile(path.join(f.directory, 'package.json'), JSON.stringify({ dependencies: { fixture: '1.0.0' } }));
  await fs.symlink(os.tmpdir(), path.join(f.directory, 'node_modules'), 'dir');
  result = await setup({ ...f, install: true, probe: ready });
  assert.match(result.error, /node_modules is a symlink/);
  assert.equal(result.actions.length, 0);
});

test('old Node and missing npm give prerequisites without downloads', async t => {
  const f = await fixture(t);
  const old = await setup({ ...f, install: true, nodeVersion: '20.18.0', probe: ready });
  assert.equal(old.ok, false);
  assert.match(old.nextSteps[0], /Node.js 22/);
  assert.equal(f.commands.length, 0);
  const missing = await setup({ ...f, install: true, run: () => ({ status: null, error: { code: 'ENOENT' } }), probe: ready });
  assert.equal(missing.ok, false);
  assert.equal(missing.runtime.npm, 'unavailable');
  assert.equal(missing.actions.length, 0);
});

test('preflight missing dependencies is read-only', async t => {
  const f = await fixture(t, false);
  const result = await setup({ ...f, probe: async () => { assert.fail('Browser must not run with missing dependencies'); } });
  assert.equal(result.ok, false);
  assert.match(result.nextSteps[0], /run.mjs setup/);
  assert.equal(f.commands.length, 1);
  await assert.rejects(fs.stat(path.join(f.directory, 'node_modules')), { code: 'ENOENT' });
});

test('first setup installs once and second setup reuses ready dependencies/browser', async t => {
  const f = await fixture(t, false);
  const first = await setup({ ...f, install: true, probe: ready });
  assert.equal(first.ok, true);
  assert.equal(first.actions.length, 1);
  assert.deepEqual(f.commands[1].args, ['ci', '--ignore-scripts', '--no-audit', '--no-fund', '--include=dev', '--include=optional']);
  assert.equal(f.commands[1].cwd, f.directory);
  assert.equal(f.commands[1].mutation, true);
  const second = await setup({ ...f, install: true, probe: ready });
  assert.equal(second.ok, true);
  assert.deepEqual(second.actions, []);
  assert.equal(f.commands.filter(x => x.mutation).length, 1);
});

test('matching package versions with broken imports are repaired once', async t => {
  const f = await fixture(t);
  let probes = 0;
  const result = await setup({ ...f, install: true, probe: async () => ++probes === 1 ? { ok: false, phase: 'dependencies', missing: false, error: 'Missing module file' } : ready() });
  assert.equal(result.ok, true);
  assert.equal(probes, 2);
  assert.equal(result.actions.length, 1);
});

test('missing Chromium downloads only from pinned local CLI and is rechecked', async t => {
  const f = await fixture(t);
  let probes = 0;
  const result = await setup({ ...f, install: true, probe: async () => ++probes === 1 ? { ok: false, phase: 'browser', missing: true, error: "Executable doesn't exist at fixture" } : ready() });
  assert.equal(result.ok, true);
  assert.equal(probes, 2);
  assert.equal(result.actions.length, 1);
  assert.deepEqual(f.commands[1].args, [path.join(f.directory, 'node_modules/playwright/cli.js'), 'install', 'chromium']);
});

test('missing browser preflight and OS launch failure never install', async t => {
  const f = await fixture(t);
  const missing = await setup({ ...f, probe: async () => ({ ok: false, phase: 'browser', missing: true, error: 'missing executable' }) });
  assert.equal(missing.ok, false);
  assert.match(missing.nextSteps[0], /setup/);
  const broken = await setup({ ...f, install: true, probe: async () => ({ ok: false, phase: 'browser', missing: false, error: 'Missing OS library fixture' }) });
  assert.equal(broken.ok, false);
  assert.equal(broken.browser.error, 'Missing OS library fixture');
  assert.match(broken.nextSteps[0], /never installs OS packages/);
  assert.deepEqual(broken.actions, []);
});

test('failed dependency/browser install stops with truthful non-ready result', async t => {
  const f = await fixture(t, false);
  const failureRun = (command, args, cwd, mutation) => mutation ? { status: 1 } : f.run(command, args, cwd, mutation);
  const failed = await setup({ ...f, install: true, run: failureRun, probe: async () => { assert.fail('Failed install must stop before browser'); } });
  assert.equal(failed.ok, false);
  assert.match(failed.error, /dependency installation failed/);
  assert.equal(failed.actions.length, 1);
  f.writePackage();
  const browserFailed = await setup({ ...f, install: true, run: failureRun, probe: async () => ({ ok: false, phase: 'browser', missing: true }) });
  assert.equal(browserFailed.ok, false);
  assert.match(browserFailed.error, /Chromium download failed/);
  assert.equal(browserFailed.actions.length, 1);
});
