import { readFile, writeFile } from 'node:fs/promises';
import { renderCatalogMarkdown } from '../src/catalog.mjs';

const file = new URL('../skills/create-carousel/references/DSL_LAYOUT_SPEC.md', import.meta.url);
const current = await readFile(file, 'utf8');
const next = current.split('## 23. Каталоги')[0] + renderCatalogMarkdown();
if (process.argv.includes('--check')) {
  if (current !== next) { console.error('Catalog documentation is stale. Run npm run catalog:sync.'); process.exitCode = 1; }
} else {
  await writeFile(file, next);
  console.log('Generated catalog documentation from data/catalog.json');
}
