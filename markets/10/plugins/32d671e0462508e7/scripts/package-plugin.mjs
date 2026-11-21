import assert from 'node:assert/strict';
import { lstat, readdir, readFile, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { zipSync, unzipSync } from 'fflate';
import { parse } from 'yaml';

const root = fileURLToPath(new URL('../', import.meta.url));
const output = resolve(process.argv[2] ?? fileURLToPath(new URL('../../carousel-creator.zip', import.meta.url)));
const included = ['plugin.json', 'mcp.json', 'package.json', 'package-lock.json', 'README.md', 'LICENSE', 'Dockerfile', '.dockerignore', 'assets/icon.png'];
const claudeOnly = new Set(['scripts/package-claude-plugin.mjs', 'tests/claude-package.test.mjs']);
async function includeDirectory(relative) {
  for (const entry of await readdir(resolve(root, relative), { withFileTypes: true })) {
    const child = relative + '/' + entry.name;
    if (entry.name === '.DS_Store' || claudeOnly.has(child)) continue;
    if (entry.isDirectory()) await includeDirectory(child);
    else if (entry.isFile()) included.push(child);
    else throw new Error('Package entries must be regular files or directories: ' + child);
  }
}
for (const directory of ['src', 'data', 'scripts', 'skills', 'examples', 'tests', 'native']) await includeDirectory(directory);
included.sort();

const files = {};
for (const relative of included) {
  const path = resolve(root, relative);
  assert.ok((await lstat(path)).isFile(), `Expected a regular file: ${relative}`);
  files[relative] = await readFile(path);
}
const manifest = JSON.parse(files['plugin.json']);
const runtime = JSON.parse(files['package.json']);
const lock = JSON.parse(files['package-lock.json']);
assert.equal(manifest.version, runtime.version);
assert.equal(manifest.version, lock.packages[''].version);
delete runtime.scripts['package:claude'];
delete runtime.scripts['export:claude'];
files['package.json'] = Buffer.from(JSON.stringify(runtime, null, 2) + '\n');
// The repository has separate client instructions. A re-pack of the extracted
// OpenAI archive already has its public README at the root.
try { files['README.md'] = await readFile(resolve(root, 'publication/openai/README.md')); }
catch (error) { if (error.code !== 'ENOENT') throw error; }
const metadata = manifest.extensions['com.openai'].interface;
const singleLine = (value, maximum, field) => {
  assert.equal(typeof value, 'string', `${field} must be a string`);
  assert.ok(value.trim() && [...value].length <= maximum && !/[\r\n\t]/.test(value), `Invalid ${field}`);
};
singleLine(manifest.name, 64, 'name');
assert.match(manifest.name, /^[a-z0-9]+(?:-[a-z0-9]+)*$/);
assert.match(manifest.version, /^\d+\.\d+\.\d+$/);
singleLine(metadata.displayName, 30, 'displayName');
singleLine(metadata.shortDescription, 30, 'shortDescription');
singleLine(metadata.developerName, 80, 'developerName');
assert.ok(metadata.longDescription.trim() && [...metadata.longDescription].length <= 4000);
assert.equal(metadata.category, 'Creativity');
assert.ok(metadata.capabilities.length <= 20);
for (const value of metadata.capabilities) singleLine(value, 120, 'capability');
for (const field of ['websiteURL', 'supportURL', 'privacyPolicyURL', 'termsOfServiceURL']) {
  singleLine(metadata[field], 1024, field);
  const url = new URL(metadata[field]);
  assert.equal(url.protocol, 'https:');
  assert.ok(!url.username && !url.password);
}
assert.ok(metadata.defaultPrompt.length <= 3);
assert.equal(new Set(metadata.defaultPrompt.map(s => s.normalize('NFC').trim())).size, metadata.defaultPrompt.length);
for (const prompt of metadata.defaultPrompt) singleLine(prompt, 128, 'defaultPrompt');
for (const field of ['logo', 'composerIcon']) {
  assert.ok(metadata[field].startsWith('./'));
  assert.ok(files[metadata[field].slice(2)], `Missing ${field} file`);
}
const icon = files['assets/icon.png'];
assert.equal(icon.subarray(0, 8).toString('hex'), '89504e470d0a1a0a');
assert.equal(icon.readUInt32BE(16), icon.readUInt32BE(20));
assert.ok(icon.readUInt32BE(16) >= 48 && icon.readUInt32BE(16) <= 4096 && icon.length <= 5 * 1024 * 1024);

const mcp = JSON.parse(files['mcp.json']);
assert.equal(mcp.$schema, 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json');
assert.equal(Object.keys(mcp.mcpServers).length, 1);
assert.deepEqual(mcp.mcpServers['carousel-creator'], { type: 'streamable-http', url: 'https://mcp.quokka.software/mcp' });
const skill = files['skills/create-carousel/SKILL.md'].toString('utf8');
const frontmatter = skill.match(/^---\n([\s\S]*?)\n---\n/);
assert.ok(frontmatter, 'Skill frontmatter missing');
const identity = parse(frontmatter[1]);
assert.equal(identity.name, 'create-carousel');
singleLine(identity.description, 1024, 'skill description');
assert.ok(skill.slice(frontmatter[0].length).trim());
assert.ok(files['skills/create-carousel/references/DSL_LAYOUT_SPEC.md'].length);

const review = manifest.extensions['com.openai'].review;
if (review.demo_recording_url) {
  const demoUrl = new URL(review.demo_recording_url);
  assert.equal(demoUrl.protocol, 'https:');
  assert.ok(!demoUrl.username && !demoUrl.password);
}
assert.equal(review.test_cases.positive.length, 5);
assert.equal(review.test_cases.negative.length, 3);
for (const test of [...review.test_cases.positive, ...review.test_cases.negative]) {
  assert.ok(test.description.trim() && test.prompt.trim() && test.expected_behavior.trim());
}
for (const test of review.test_cases.positive) assert.ok(test.tools_triggered.trim());
for (const translation of Object.values(manifest.extensions['com.openai'].publication.translations ?? {})) {
  singleLine(translation.subtitle, 30, 'translated subtitle');
  assert.ok(translation.description.trim() && [...translation.description].length <= 4000);
}

// Match the ASCII JSON encoding and Unix file attributes of the accepted 0.1.2 ZIP.
for (const name of included.filter(name => name.endsWith('.json'))) {
  const json = JSON.stringify(JSON.parse(files[name].toString('utf8')), null, 2);
  const ascii = json.replace(/[\u007f-\uffff]/g, char => '\\u' + char.charCodeAt(0).toString(16).padStart(4, '0'));
  files[name] = Buffer.from(ascii + '\n');
}
const bytes = zipSync(files, { level: 9, os: 3, attrs: 0o100644 * 65536 });
assert.ok(bytes.length < 100_000_000);
const extracted = unzipSync(bytes);
assert.deepEqual(Object.keys(extracted).sort(), included.toSorted());
for (const name of included) assert.deepEqual(Buffer.from(extracted[name]), files[name], `ZIP mismatch: ${name}`);
await writeFile(output, bytes);
console.log(JSON.stringify({ zip: output, bytes: bytes.length, files: included.length, version: manifest.version, display_name: metadata.displayName, mcp_url: mcp.mcpServers['carousel-creator'].url, demo_recording_url: review.demo_recording_url ?? null, positive_cases: 5, negative_cases: 3 }, null, 2));
