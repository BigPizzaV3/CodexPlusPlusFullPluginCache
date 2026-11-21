import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, mkdir, readFile, writeFile, symlink, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { unzipSync } from 'fflate';

const exec = promisify(execFile);
test('the distributable includes every runtime dependency file and works after extraction', async () => {
  const scratch = await mkdtemp(join(tmpdir(),'carousel-package-'));
  const root = fileURLToPath(new URL('../',import.meta.url));
  try {
    const zip = join(scratch,'plugin.zip');
    await exec(process.execPath,[join(root,'scripts/package-plugin.mjs'),zip]);
    const files = unzipSync(await readFile(zip));
    assert.ok(files['LICENSE']);
    const distribution = JSON.parse(Buffer.from(files['package.json']).toString());
    for (const script of Object.values(distribution.scripts)) {
      const entry = script.match(/^node (scripts\/\S+\.mjs)$/)?.[1];
      if (entry) assert.ok(files[entry], 'Missing script referenced in the distributable: ' + entry);
    }
    assert.ok(!files['tests/claude-package.test.mjs']);
    assert.ok(files['data/catalog.json']);
    assert.ok(files['data/examples.json']);
    assert.ok(files['skills/create-carousel/references/DESIGN_GUIDE.md']);
    assert.ok(files['skills/create-carousel/references/WRITING_GUIDE.md']);
    assert.ok(files['native/RendererApp.swift']);
    assert.ok(files['src/renderer.mjs']);
    assert.ok(files['scripts/setup-native-renderer.mjs']);
    assert.ok(files['scripts/render-carousel.mjs']);
    assert.ok(!Object.keys(files).some(name=>name.includes('node_modules')));
    const extracted = join(scratch,'extracted');
    for (const [name,bytes] of Object.entries(files)) {
      const path=join(extracted,name);await mkdir(dirname(path),{recursive:true});await writeFile(path,bytes);
    }
    await symlink(join(root,'node_modules'),join(extracted,'node_modules'),'dir');
    const {stdout} = await exec(process.execPath,['scripts/get-spec.mjs','catalogs','quad','grids'],{cwd:extracted,maxBuffer:2*1024*1024});
    assert.equal(JSON.parse(stdout).catalog.entries[0].example.layers[0].grid.cells.length,4);
    const writing = await exec(process.execPath,['scripts/get-spec.mjs','writing'],{cwd:extracted});
    assert.equal(JSON.parse(writing.stdout).text, Buffer.from(files['skills/create-carousel/references/WRITING_GUIDE.md']).toString('utf8'));
    const result=await exec(process.execPath,['scripts/build-carousel.mjs','examples/photo-story.yaml',join(scratch,'story.carousel')],{cwd:extracted});
    assert.equal(JSON.parse(result.stdout).slides,2);
    assert.ok(unzipSync(await readFile(join(scratch,'story.carousel')))['carousel.yaml']);
  } finally { await rm(scratch,{recursive:true,force:true}); }
});
