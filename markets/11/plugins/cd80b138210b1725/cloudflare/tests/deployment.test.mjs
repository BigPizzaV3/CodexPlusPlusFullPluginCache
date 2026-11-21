import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile, mkdtemp, copyFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { spawnSync } from 'node:child_process';
import { prepareConfig } from '../scripts/configure-origin.mjs';
import { inspectConfig } from '../scripts/preflight.mjs';

const base = JSON.parse(await readFile('wrangler.jsonc', 'utf8'));
const options = { origin: 'https://budget.synthetic-account.workers.dev',
  accountId: 'a'.repeat(32), namespaceBase: 2001 };
test('deployment configuration selects the explicit account and exact hostname without keeping unwanted bindings', () => {
  const prepared = prepareConfig({ ...base, ai: { binding: 'UNEXPECTED' } }, options);
  assert.equal(prepared.account_id, options.accountId);
  assert.equal(prepared.name, 'budget');
  assert.ok(!('ai' in prepared));
  assert.equal(prepared.preview_urls, false);
  assert.deepEqual(prepared.ratelimits.map(binding => binding.namespace_id), ['2001', '2002']);
  const proof = inspectConfig(prepared);
  assert.equal(proof.deployed, false);
  assert.equal(proof.free_plan_verified, false);
  assert.equal(proof.endpoint, options.origin + '/mcp');
});
test('credential URLs, loopback hosts, ambiguous paths and unselected accounts cannot become a production config', () => {
  for (const origin of ['http://budget.synthetic-account.workers.dev', 'https://localhost',
    'https://budget.synthetic-account.workers.dev/mcp', 'https://budget.synthetic-account.workers.dev?token=x',
    'https://token@budget.synthetic-account.workers.dev', 'https://budget.workers.dev',
    'https://budget.synthetic-account.workers.dev/', 'https://budget.synthetic-account.workers.dev.evil.test']) {
    assert.throws(() => prepareConfig(base, { ...options, origin }));
  }
  for (const accountId of ['', undefined, 'email@example.test']) {
    assert.throws(() => prepareConfig(base, { ...options, accountId }));
  }
  for (const namespaceBase of [0, -1, 1.5, NaN, 2147483647]) {
    assert.throws(() => prepareConfig(base, { ...options, namespaceBase }));
  }
});
test('local preflight refuses storage, alternate entry points, missing limiters and logging changes', () => {
  for (const alter of [config => { config.kv_namespaces = []; },
    config => { config.routes = []; }, config => { config.main = 'other.js'; },
    config => { config.observability.enabled = true; }, config => { config.preview_urls = true; },
    config => { delete config.ratelimits; },
    config => { config.ratelimits[1].namespace_id = config.ratelimits[0].namespace_id; },
    config => { config.vars.EXTRA = 'unreviewed'; }, config => { config.name = 'other'; }]) {
    const config = prepareConfig(base, options);
    alter(config);
    assert.throws(() => inspectConfig(config));
  }
});
test('config CLI writes a separate file and refuses overwriting an earlier choice', async () => {
  const folder = await mkdtemp(join(tmpdir(), 'token-weather-config-'));
  try {
    await copyFile('wrangler.jsonc', join(folder, 'wrangler.jsonc'));
    const args = [resolve('scripts/configure-origin.mjs'), '--origin', options.origin,
      '--account-id', options.accountId, '--namespace-base', '2001', '--output', 'wrangler.production.json'];
    const run = () => spawnSync(process.execPath, args, { cwd: folder, encoding: 'utf8' });
    assert.equal(run().status, 0);
    const saved = await readFile(join(folder, 'wrangler.production.json'), 'utf8');
    assert.equal(run().status, 1);
    assert.equal(await readFile(join(folder, 'wrangler.production.json'), 'utf8'), saved);
    assert.deepEqual(JSON.parse(await readFile(join(folder, 'wrangler.jsonc'), 'utf8')), base);
  } finally { await rm(folder, { recursive: true, force: true }); }
});
