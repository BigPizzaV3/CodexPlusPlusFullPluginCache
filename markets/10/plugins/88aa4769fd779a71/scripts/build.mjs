import { build } from 'esbuild';
import { readFile, mkdir, writeFile } from 'node:fs/promises';

const root = new URL('../', import.meta.url);
const result = await build({ absWorkingDir: root.pathname, entryPoints: ['web/app.mjs'], bundle: true, write: false, format: 'iife', platform: 'browser', target: ['es2022'], minify: true, legalComments: 'none' });
const template = await readFile(new URL('web/index.html', root), 'utf8');
const css = `${await readFile(new URL('web/style.css', root), 'utf8')}\n${await readFile(new URL('web/design.css', root), 'utf8')}`;
const logo = `data:image/png;base64,${(await readFile(new URL('assets/peptara-logo.png', root))).toString('base64')}`;
const syringeDiagram = await readFile(new URL('assets/syringe-reference.svg', root), 'utf8');
const vialDiagram = await readFile(new URL('assets/vial-reference.svg', root), 'utf8');
const html = template.replace('/* BUILD_STYLES */', css).replaceAll('/* BRAND_LOGO */', logo).replace('/* SYRINGE_DIAGRAM */', syringeDiagram).replace('/* VIAL_DIAGRAM */', vialDiagram).replace('/* BUILD_SCRIPT */', () => result.outputFiles[0].text.replaceAll('</script', '<\\/script'));
await mkdir(new URL('dist/', root), { recursive: true });
await writeFile(new URL('dist/calculator.html', root), html);
console.log(`Built self-contained calculator (${Buffer.byteLength(html)} bytes).`);
