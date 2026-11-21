#!/usr/bin/env node
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = file => JSON.parse(fs.readFileSync(path.join(root, file), 'utf8'));
const portable = read('plugin.json'), codex = read('.codex-plugin/plugin.json'), claude = read('.claude-plugin/plugin.json');
assert.equal(portable.$schema, 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json');
assert.equal(portable.name, 'device-it');
assert.equal(portable.skills, undefined);
for (const field of ['name', 'version', 'description', 'author']) {
  assert.deepEqual(portable[field], codex[field]); assert.deepEqual(portable[field], claude[field]);
}
const ui = portable.extensions['com.openai'].interface;
const nativeUI = { ...ui };
delete nativeUI.supportURL; // Supported by portable listing schema, omitted by native adapter schema.
assert.deepEqual(nativeUI, codex.interface);
assert.ok(ui.shortDescription.length <= 30 && ui.displayName.length <= 30 && ui.longDescription.length <= 4000 && ui.developerName.length <= 80);
assert.equal(ui.category, 'Developer Tools');
assert.ok(ui.defaultPrompt.length <= 3 && ui.defaultPrompt.every(x => x.length <= 128));
assert.equal(portable.license, 'MIT');
assert.equal(codex.license, 'MIT');
assert.equal(claude.license, 'MIT');
for (const field of ['logo', 'composerIcon']) {
  const bytes = fs.readFileSync(path.join(root, ui[field]));
  assert.equal(bytes.toString('hex', 0, 8), '89504e470d0a1a0a');
  const width = bytes.readUInt32BE(16), height = bytes.readUInt32BE(20);
  assert.equal(width, height); assert.ok(width >= 48 && width <= 4096);
  assert.ok(bytes.length <= 5 * 1024 * 1024);
}
assert.equal(fs.readFileSync(path.join(root, 'SKILL.md'), 'utf8'), fs.readFileSync(path.join(root, 'skills/device-it/SKILL.md'), 'utf8'));
const pkg = read('package.json'), lock = read('package-lock.json');
assert.equal(pkg.version, portable.version);
assert.equal(pkg.license, 'MIT'); assert.equal(lock.packages[''].license, 'MIT');
for (const group of ['dependencies', 'devDependencies']) for (const [name, version] of Object.entries(pkg[group])) {
  assert.match(version, /^\d+\.\d+\.\d+$/);
  assert.equal(lock.packages[''][group][name], version);
  assert.equal(lock.packages[`node_modules/${name}`].version, version);
}
const list = read('package-files.json');
assert.equal(new Set(list).size, list.length);
for (const file of list) {
  assert.ok(!path.isAbsolute(file) && !file.split('/').some(p => p === '..'));
  assert.ok(!/(^|\/)(node_modules|local-state|work|deploy|mdm|push|templates|references)(\/|$)/.test(file), `Excluded package path: ${file}`);
  assert.ok(fs.lstatSync(path.join(root, file)).isFile(), `Missing or non-file package entry: ${file}`);
  if (file.endsWith('.mjs')) {
    const checked = spawnSync(process.execPath, ['--check', path.join(root, file)], { encoding: 'utf8' });
    assert.equal(checked.status, 0, checked.stderr);
    const code = fs.readFileSync(path.join(root, file), 'utf8');
    for (const match of code.matchAll(/(?:from\s+|import\s*\()(['"])(\.\.?\/[^'"]+)\1/g)) {
      const target = path.posix.normalize(path.posix.join(path.posix.dirname(file), match[2]));
      assert.ok(list.includes(target), `Import absent from package: ${target}`);
    }
  }
}
console.log(`Device It package checks passed: ${list.length} allowed files, synchronized manifests/skills, exact dependency lock, PNG icon and JavaScript syntax/imports.`);
