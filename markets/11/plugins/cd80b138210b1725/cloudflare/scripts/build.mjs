import { build } from 'esbuild';
import { mkdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';

await mkdir('build', { recursive: true });
await build({
  entryPoints: ['src/index.ts'], bundle: true, format: 'esm', platform: 'browser',
  target: 'es2022', conditions: ['workerd', 'worker', 'browser'],
  external: ['cloudflare:workers', 'cloudflare:sockets', 'node:*'],
  outfile: 'build/worker.mjs', minify: true, legalComments: 'external', metafile: true,
}).then(async result => {
  const { writeFile } = await import('node:fs/promises');
  await writeFile('build/metafile.json', JSON.stringify(result.metafile, null, 2) + '\n');
  const packages=new Set(Object.keys(result.metafile.inputs).filter(path=>path.startsWith('node_modules/')).map(path=>{
    const parts=path.split('/');return parts[1].startsWith('@')?parts.slice(1,3).join('/'):parts[1];
  }));
  let notices='Third-party components actually included in the Worker bundle. Original project code is MIT.\n';
  for(const name of [...packages].sort()) {
    const folder=join('node_modules',name),meta=JSON.parse(await readFile(join(folder,'package.json'),'utf8'));
    let licence='';
    for(const file of ['LICENSE','LICENSE.md','LICENSE.txt','license','COPYING']) {
      try{licence=await readFile(join(folder,file),'utf8');break;}catch{}
    }
    if(!licence)throw new Error('Inspect missing bundled dependency licence: '+name);
    notices+='\n--- '+name+' '+meta.version+' ('+meta.license+') ---\n'+licence+'\n';
  }
  await writeFile('build/THIRD-PARTY-LICENSES.txt',notices);
});
await build({ entryPoints: ['src/budget.ts'], bundle: true, format: 'esm', platform: 'node',
  target: 'es2022', outfile: 'build/budget.mjs' });
await build({ entryPoints: ['src/remote-budget.ts'], bundle: true, format: 'esm', platform: 'node',
  target: 'es2022', outfile: 'build/remote-budget.mjs' });
console.log('Local bundles built. No Cloudflare deployment or account access performed.');
