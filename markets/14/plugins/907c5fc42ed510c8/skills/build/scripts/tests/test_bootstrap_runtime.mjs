import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import vm from 'node:vm';
import test from 'node:test';
import { bootstrapRuntime } from '../bootstrap_runtime.mjs';

const skillRoot = fileURLToPath(new URL('../../', import.meta.url));
const modulePath = fileURLToPath(new URL('../bootstrap_runtime.mjs', import.meta.url));
const inventory = JSON.parse(fs.readFileSync(path.join(skillRoot, 'Automation/EX89.json'), 'utf8'));
const python = process.env.BUILD_TEST_PYTHON || process.env.CODEX_PRIMARY_RUNTIME_PYTHON || 'python3';

function harness({ change, pageSize = Infinity } = {}) {
  const roots = new Set();
  const calls = [];
  const reads = [];
  return {
    roots, calls, reads,
    async readResource(relative, cursor) {
      reads.push({ relative, cursor });
      let text = fs.readFileSync(path.join(skillRoot, relative), 'utf8');
      if (change) text = change(relative, text);
      const offset = cursor === undefined ? 0 : Number(cursor);
      const end = Math.min(offset + pageSize, text.length);
      return { contents: text.slice(offset, end), next_cursor: end < text.length ? String(end) : null };
    },
    async runPython(code, input) {
      const data = JSON.stringify(input);
      calls.push({ op: input.op, resource: input.name, codeBytes: Buffer.byteLength(code), inputBytes: Buffer.byteLength(data), text: input.op === 'chunk' ? input.text : undefined });
      // A real file descriptor avoids a sandbox-specific Node spawnSync pipe/EOF
      // failure. Python still receives the identical JSON document on stdin.
      const inputRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'build-bridge-test-input-'));
      const inputPath = path.join(inputRoot, 'stdin.json');
      fs.writeFileSync(inputPath, data, { mode: 0o600 });
      const descriptor = fs.openSync(inputPath, 'r');
      let result;
      try {
        result = spawnSync(python, ['-B', '-c', code], {
          stdio: [descriptor, 'pipe', 'pipe'], encoding: 'utf8', timeout: 65000, maxBuffer: 256 * 1024
        });
      } finally {
        fs.closeSync(descriptor); fs.rmSync(inputRoot, { recursive: true, force: true });
      }
      assert.equal(result.status, 0, result.stderr || String(result.error));
      const value = JSON.parse(result.stdout);
      if (value.session?.root) roots.add(value.session.root);
      return value;
    },
    cleanup() {
      for (const root of roots) fs.rmSync(root, { recursive: true, force: true });
    }
  };
}

test('plain V8 bridge transfers every source through bounded JSON and probes clean final runtime', async () => {
  const source = fs.readFileSync(modulePath, 'utf8');
  const footer = '\nexport { bootstrapRuntime };\n';
  assert.ok(source.endsWith(footer));
  const context = vm.createContext({});
  assert.equal(vm.runInContext('typeof Buffer + "," + typeof TextEncoder + "," + typeof require', context), 'undefined,undefined,undefined');
  const plainBootstrap = vm.runInContext(source.slice(0, -footer.length) + '\nbootstrapRuntime;', context);
  const h = harness();
  try {
    const result = await plainBootstrap(h);
    assert.equal(result.status, 'passed', JSON.stringify(result));
    assert.equal(result.schema, 'build.runtime-bridge/1');
    assert.equal(result.application_qualified, false);
    assert.equal(result.network_used, false);
    assert.equal(result.owner_api_used, false);
    assert.equal(result.files_verified, 14);
    assert.equal(result.command_probes.length, 3);
    assert.ok(result.command_probes.every(item => item.status === 'passed' && item.exit_code === 0));
    assert.equal(path.dirname(result.helper_path), result.workspace_root);
    assert.equal(path.dirname(result.runtime_root), result.workspace_root);
    assert.equal(fs.existsSync(path.join(result.runtime_root, 'prepare_runtime.py')), false);
    for (const record of inventory.runtime_files) {
      assert.deepEqual(fs.readFileSync(path.join(result.runtime_root, record.path)), fs.readFileSync(path.join(skillRoot, record.skill_path)));
    }
    const seen = new Set(h.reads.map(item => item.relative));
    assert.equal(seen.size, 16); // EX89 + helper + original14.
    assert.equal(h.calls[0].op, 'init');
    assert.equal(h.calls.at(-1).op, 'finish');
    assert.ok(h.calls.every(item => item.codeBytes + item.inputBytes <= 48 * 1024));
    assert.ok(h.calls.filter(item => item.op === 'chunk').every(item => [...item.text].length <= 4096));
    assert.ok(h.calls.filter(item => item.op === 'chunk').length > 14);
    assert.ok(h.calls.some(item => item.op === 'begin' && item.resource === 'iteration/engine.py'));
    // Original ambiguity: helper mixed with pinned files fails direct --check,
    // while the bridge's prescribed --copy-from route above produced a clean14.
    fs.copyFileSync(result.helper_path, path.join(result.source_root, 'prepare_runtime.py'));
    const direct = spawnSync(python, ['-B', result.helper_path, '--check', result.source_root, '--probe'], { encoding: 'utf8', timeout: 20000 });
    assert.equal(direct.status, 1);
    const blocked = JSON.parse(direct.stdout);
    assert.equal(blocked.files_verified, 14);
    assert.deepEqual(blocked.unexpected_python_files, ['prepare_runtime.py']);
    assert.equal(fs.existsSync(path.join(result.runtime_root, 'prepare_runtime.py')), false);
  } finally { h.cleanup(); }
});

test('pagination is joined verbatim before verification and transfer', async () => {
  const h = harness({ pageSize: 2500 });
  try {
    const result = await bootstrapRuntime(h);
    assert.equal(result.status, 'passed', JSON.stringify(result));
    assert.ok(h.reads.some(item => item.relative === 'scripts/iteration/engine.py' && item.cursor !== undefined));
    assert.deepEqual(fs.readFileSync(path.join(result.runtime_root, 'iteration/engine.py')), fs.readFileSync(path.join(skillRoot, 'scripts/iteration/engine.py')));
  } finally { h.cleanup(); }
});

test('truncated source is rejected before probe and partial root is removed', async () => {
  const h = harness({ change: (name, text) => name === 'scripts/iteration/engine.py' ? text.slice(0, -1) : text });
  try {
    const result = await bootstrapRuntime(h);
    assert.equal(result.status, 'blocked');
    assert.equal(result.error_code, 'resource_hash_mismatch');
    assert.equal(result.resource, 'iteration/engine.py');
    assert.equal(result.actual_bytes, result.expected_bytes - 1);
    assert.equal(result.cleanup, 'completed');
    assert.ok(!h.calls.some(item => item.op === 'finish'));
    assert.ok([...h.roots].every(root => !fs.existsSync(root)));
    assert.ok(!JSON.stringify(result).includes('from __future__'));
  } finally { h.cleanup(); }
});

test('same-size altered source cannot execute and does not weaken expected hash', async () => {
  const h = harness({ change: (name, text) => name === 'scripts/deliver.py' ? '!' + text.slice(1) : text });
  try {
    const result = await bootstrapRuntime(h);
    assert.equal(result.status, 'blocked');
    assert.equal(result.error_code, 'resource_hash_mismatch');
    assert.equal(result.resource, 'deliver.py');
    assert.equal(result.actual_bytes, result.expected_bytes);
    assert.notEqual(result.actual_sha256, result.expected_sha256);
    assert.equal(result.cleanup, 'completed');
    assert.ok(!h.calls.some(item => item.op === 'finish'));
  } finally { h.cleanup(); }
});

test('missing Python adapter or execution fails before any resource traversal', async () => {
  let reads = 0;
  const readResource = async () => { reads++; throw new Error('must not read'); };
  const absent = await bootstrapRuntime({ readResource });
  assert.equal(absent.error_code, 'python_adapter_unavailable');
  const failed = await bootstrapRuntime({ readResource, runPython: async () => { throw new Error('no executor'); } });
  assert.equal(failed.error_code, 'python_execution_unavailable');
  assert.equal(failed.operation, 'init');
  assert.equal(reads, 0);
});

test('resource reader absence is reported before creating a temporary root', async () => {
  let executions = 0;
  const result = await bootstrapRuntime({ runPython: async () => { executions++; } });
  assert.equal(result.error_code, 'resource_adapter_unavailable');
  assert.equal(executions, 0);
});

test('pagination cycle is bounded and cleans its owned temporary root', async () => {
  const h = harness();
  let reads = 0;
  h.readResource = async () => { reads++; return { contents: '{', next_cursor: 'same-cursor' }; };
  try {
    const result = await bootstrapRuntime(h);
    assert.equal(result.error_code, 'resource_pagination_cycle');
    assert.equal(reads, 2);
    assert.equal(result.cleanup, 'completed');
    assert.ok([...h.roots].every(root => !fs.existsSync(root)));
  } finally { h.cleanup(); }
});

test('unexpected inventory path cannot write or execute a resource', async () => {
  const h = harness({ change: (name, text) => {
    if (name !== 'Automation/EX89.json') return text;
    const value = JSON.parse(text); value.runtime_files[0].path = '../outside.py'; return JSON.stringify(value);
  } });
  try {
    const result = await bootstrapRuntime(h);
    assert.equal(result.error_code, 'inventory_invalid');
    assert.equal(result.cleanup, 'completed');
    assert.ok(!h.calls.some(item => item.op === 'begin'));
  } finally { h.cleanup(); }
});

test('reader protocol failure returns bounded diagnostics without source content', async () => {
  const h = harness();
  h.readResource = async () => ({ text: 'a wrapper, not the complete contents field' });
  try {
    const result = await bootstrapRuntime(h);
    assert.equal(result.error_code, 'resource_reader_protocol_error');
    assert.equal(result.resource, 'Automation/EX89.json');
    assert.equal(result.cleanup, 'completed');
    assert.ok(JSON.stringify(result).length < 1024);
  } finally { h.cleanup(); }
});
