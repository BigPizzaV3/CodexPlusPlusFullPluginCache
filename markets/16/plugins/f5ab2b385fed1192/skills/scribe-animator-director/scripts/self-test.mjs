#!/usr/bin/env node
import { readFile, readdir } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { validateTemplateJson, compositionReviewRoute, PACKAGE_VERSION } from './validator.mjs';
const packageRoot = new URL('../../../', import.meta.url);
const skillRoot = new URL('../',import.meta.url);
// This test must work with network and repository access absent.
globalThis.fetch=()=>{throw new Error('Network is forbidden in offline self-test');};
const integrity=JSON.parse(await readFile(new URL('integrity.json',packageRoot),'utf8'));
if(integrity.version!==PACKAGE_VERSION) throw new Error('Package version mismatch');
for(const [p,expected] of Object.entries(integrity.files)) {
  if(p.startsWith('/') || p.split('/').includes('..')) throw new Error('Escaping package resource');
  const data=await readFile(new URL(p,packageRoot));
  if(createHash('sha256').update(data).digest('hex')!==expected) throw new Error(`Resource drift: ${p}`);
}
const manifest=JSON.parse(await readFile(new URL('plugin.json',packageRoot),'utf8'));
if(manifest.version!==PACKAGE_VERSION) throw new Error('Manifest/validator version mismatch');
const outcomes=[];
for(const [dir,expected] of [['valid',true],['invalid',false]]) for(const name of (await readdir(new URL(`examples/${dir}/`,skillRoot))).sort()) {
  const result=await validateTemplateJson(await readFile(new URL(`examples/${dir}/${name}`,skillRoot),'utf8'));
  if(result.ok!==expected) throw new Error(`Unexpected ${dir}/${name}: ${JSON.stringify(result)}`);
  outcomes.push({fixture:`${dir}/${name}`,ok:result.ok,runtimeOk:result.runtimeOk,schemaOk:result.schemaOk});
}
if(compositionReviewRoute(100,true)!=='diagnostic-plus-exact-frame' || compositionReviewRoute(101,true)!=='manual-exact-frame-review'
  || compositionReviewRoute(null,false)!=='manual-exact-frame-review') throw new Error('Composition fallback regression');
console.log(JSON.stringify({ok:true,packageVersion:PACKAGE_VERSION,fixtureCount:outcomes.length,outcomes,
  browserAcceptance:'NOT_RUN',scope:'isolated package self-test only'},null,2));
