#!/usr/bin/env node
import { readFile, stat } from 'node:fs/promises';
import { createProceduralContracts, parseProceduralRecipe, DEFAULT_PROCEDURAL_BUDGETS } from './validator.mjs';
if(process.argv.length!==3) { console.error('Usage: node recipe-revision.mjs <recipe.json>'); process.exitCode=2; }
else try {
  if((await stat(process.argv[2])).size>DEFAULT_PROCEDURAL_BUDGETS.input.jsonBytes) throw new Error('Recipe input exceeds byte budget.');
  // Production parser enforces forbidden keys, depth, syntax and recipe contracts.
  const contracts=createProceduralContracts();
  const parsed=parseProceduralRecipe(await readFile(process.argv[2],'utf8'));
  if(!parsed.ok) { console.log(JSON.stringify(parsed)); process.exitCode=1; }
  else { const result=await contracts.recipeRevision(parsed.value); console.log(JSON.stringify(result,null,2)); process.exitCode=result.ok?0:1; }
} catch(e) { console.error(e.message); process.exitCode=2; }
