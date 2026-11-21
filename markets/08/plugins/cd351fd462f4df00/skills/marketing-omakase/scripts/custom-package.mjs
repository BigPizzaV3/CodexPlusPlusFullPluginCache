import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { constants } from 'node:fs';
import { lstat, mkdir, open, realpath } from 'node:fs/promises';
import path from 'node:path';

export const sha256 = value => createHash('sha256').update(value).digest('hex');
export function canonicalJson(value) {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  if (value && typeof value === 'object') return `{${Object.keys(value).sort().map(k => `${JSON.stringify(k)}:${canonicalJson(value[k])}`).join(',')}}`;
  assert.ok(value !== undefined && (typeof value !== 'number' || Number.isFinite(value)), 'non-JSON value');
  return JSON.stringify(value);
}
export function safeRelative(name) {
  assert.equal(typeof name, 'string');
  assert.ok(name.length > 0 && name.length <= 240 && !/[\\\x00-\x1f:]/.test(name), 'invalid package path');
  assert.ok(!path.posix.isAbsolute(name) && name.split('/').every(p => p && p !== '.' && p !== '..'), 'unsafe package path');
  assert.equal(name, name.normalize('NFC'), 'noncanonical package path');
  assert.ok(!name.split('/').some(p => /^(?:\.env(?:\..*)?|\.git|\.ssh|node_modules|credentials|secrets?)(?:\..*)?$/i.test(p)), 'secret/config path');
  return name;
}
const exactKeys = (value, keys) => assert.deepEqual(Object.keys(value).sort(), [...keys].sort(), 'unexpected package fields');
const secretPattern = /-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\b(?:sk-[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16})\b|(?:api[_-]?key|fal[_-]?key|(?:[a-z_]+_)?access[_-]?token|leaseToken|client[_-]?secret|authorization|password)\s*[=:]\s*["']?[^\s"'<>]{12,}/i;
export function validateCustomPackage(bundle) {
  exactKeys(bundle, ['schemaVersion', 'executionPermission', 'sourceText', 'manifest', 'files']);
  exactKeys(bundle.manifest, ['files']);
  assert.equal(bundle.schemaVersion, 1);
  assert.equal(bundle.executionPermission, 'none', 'hashes never grant execution permission');
  assert.equal(typeof bundle.sourceText, 'string');
  assert.ok(bundle.sourceText.trim() && bundle.sourceText.length <= 100_000);
  assert.ok(!secretPattern.test(bundle.sourceText), 'possible secret in source');
  assert.ok(Array.isArray(bundle.manifest?.files) && bundle.manifest.files.length > 0 && bundle.manifest.files.length <= 100);
  assert.ok(Array.isArray(bundle.files));
  const declared = new Map();
  const folded = new Set();
  for (const entry of bundle.manifest.files) {
    exactKeys(entry, ['path', 'bytes', 'sha256']);
    const name = safeRelative(entry.path);
    const key = name.toLocaleLowerCase('en-US');
    assert.ok(!folded.has(key), 'duplicate package path');
    folded.add(key);
    assert.match(entry.sha256, /^[a-f0-9]{64}$/);
    assert.ok(Number.isSafeInteger(entry.bytes) && entry.bytes >= 0);
    declared.set(name, entry);
  }
  assert.equal(bundle.files.length, declared.size, 'undeclared or missing file');
  const seen = new Set();
  let total = 0;
  for (const file of bundle.files) {
    exactKeys(file, ['path', 'kind', 'text']);
    const name = safeRelative(file.path);
    assert.ok(!seen.has(name), 'duplicate file'); seen.add(name);
    assert.equal(file.kind, 'text', 'symlinks and binary/executable archives are not restored');
    assert.equal(typeof file.text, 'string');
    assert.ok(!file.text.includes('\0') && !secretPattern.test(file.text), 'binary or possible secret');
    const entry = declared.get(name);
    assert.ok(entry, 'undeclared file');
    const bytes = Buffer.byteLength(file.text); total += bytes;
    assert.ok(total <= 2_000_000, 'package too large');
    assert.equal(bytes, entry.bytes, 'file size mismatch');
    assert.equal(sha256(file.text), entry.sha256, 'file hash mismatch');
  }
  for (const name of declared.keys()) {
    assert.ok(![...declared.keys()].some(other => other.startsWith(`${name}/`)), 'file/directory collision');
  }
  return bundle;
}
// Restore data only. Never import, spawn, install, chmod, or evaluate source files.
export async function restoreCustomPackage(bundle, destination) {
  validateCustomPackage(bundle);
  const target = path.resolve(destination);
  const parent = path.dirname(target);
  assert.equal(await realpath(parent), parent, 'symlinked restore parent');
  assert.equal((await lstat(parent)).isDirectory(), true);
  await mkdir(target, { mode: 0o700 }); // EEXIST is intentionally fatal, including empty/symlink targets.
  for (const file of bundle.files) {
    const output = path.join(target, file.path);
    await mkdir(path.dirname(output), { recursive: true, mode: 0o700 });
    const handle = await open(output, constants.O_WRONLY | constants.O_CREAT | constants.O_EXCL | constants.O_NOFOLLOW, 0o600);
    try { await handle.writeFile(file.text); await handle.sync(); } finally { await handle.close(); }
  }
  return { directory: target, files: bundle.files.map(f => f.path), executionPermission: 'none' };
}
