#!/usr/bin/env node
import { readFile, stat } from 'node:fs/promises';
import { validateTemplateJson, limits } from './validator.mjs';
const args=process.argv.slice(2), importCompatible=args[0]==='--import-compatible';
if(importCompatible) args.shift();
if(args.length!==1 || args[0].startsWith('--')) { console.error('Usage: node validate.mjs [--import-compatible] <input.json>'); process.exitCode=2; }
else try {
  const info=await stat(args[0]);
  if(info.size>limits.json.maxSnapshotJsonBytes) { console.log(JSON.stringify({ok:false,errors:['Input file exceeds offline byte limit.']})); process.exitCode=1; }
  else { const result=await validateTemplateJson(await readFile(args[0],'utf8'),{importCompatible}); console.log(JSON.stringify(result,null,2)); process.exitCode=result.ok?0:1; }
} catch(e) { console.error(e.message); process.exitCode=2; }
