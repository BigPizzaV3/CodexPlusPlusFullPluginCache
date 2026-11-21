import { readFile, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { buildCarousel } from '../src/archive.mjs';

const [input, output, option, assetFile] = process.argv.slice(2);
try {
  if (!input || !output || (option && (option !== '--assets' || !assetFile)) || !output.endsWith('.carousel')) throw new Error('Usage: node scripts/build-carousel.mjs layout.yaml output.carousel [--assets assets.json]');
  const imagePaths = assetFile ? JSON.parse(await readFile(assetFile, 'utf8')) : {};
  if (!imagePaths || typeof imagePaths !== 'object' || Array.isArray(imagePaths)) throw new Error('assets.json must map source names to image paths');
  const images = new Map(await Promise.all(Object.entries(imagePaths).map(async ([name, path]) => [name, await readFile(path)])));
  const result = await buildCarousel(await readFile(input, 'utf8'), images);
  await writeFile(output, result.bytes);
  console.log(JSON.stringify({ file: resolve(output), slides: result.document.slides, layers: result.document.layers.length, bytes: result.bytes.byteLength, ...result.diagnostics }));
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
