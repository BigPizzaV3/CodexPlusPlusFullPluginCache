import { createHash } from 'node:crypto';
import { zipSync, unzipSync } from 'fflate';
import sharp from 'sharp';
import { diagnoseDocument } from './diagnostics.mjs';
import { DocumentError, documentYAML, parseLayout, referencedAssets, validateDocument } from './document.mjs';

export const imageLimit = 20 * 1024 * 1024;
export const archiveLimit = 100 * 1024 * 1024;
// sharp reports AVIF as heif.
const photoFormats = ['jpeg', 'png', 'webp', 'avif', 'heif'];
const pixelLimit = 25_000_000;

// Reads only the header: the format of one still raster photograph, or null.
export async function photoFormat(bytes) {
  const meta = await sharp(bytes, { limitInputPixels: pixelLimit, failOn: 'error', animated: false }).metadata().catch(() => null);
  return meta && photoFormats.includes(meta.format) && (meta.pages ?? 1) <= 1 && meta.width * meta.height <= pixelLimit ? meta.format : null;
}

export async function buildCarousel(yaml, suppliedImages = new Map()) {
  const draft = validateDocument(parseLayout(yaml), { allowUnresolvedAssets: true });
  const used = referencedAssets(draft);
  const files = {};
  const assets = Object.create(null);
  let total = 0;
  for (const name of used) {
    const bytes = suppliedImages.get(name);
    if (!bytes) throw new DocumentError(`assets.${name}: supply the real image bytes; external URLs or invented hashes are insufficient`);
    if (bytes.byteLength > imageLimit) throw new DocumentError(`assets.${name}: image exceeds 20 MiB`);
    const image = sharp(bytes, { limitInputPixels: pixelLimit, failOn: 'error', animated: false });
    const meta = await image.metadata();
    if (!photoFormats.includes(meta.format) || (meta.pages ?? 1) > 1) throw new DocumentError(`assets.${name}: use a single raster photograph, not SVG, animation, or video`);
    // sharp removes EXIF/IPTC by default; rotate applies EXIF orientation before removal.
    const ext = meta.format === 'jpeg' ? 'jpg' : 'png';
    const { data, info } = await (ext === 'jpg' ? image.rotate().jpeg({ quality: 95 }) : image.rotate().png()).toBuffer({ resolveWithObject: true });
    const file = `assets/${createHash('sha256').update(data).digest('hex')}.${ext}`;
    if (!(file in files)) total += data.byteLength;
    if (total > archiveLimit - 4 * 1024 * 1024) throw new DocumentError('Project images exceed the 96 MiB total limit');
    files[file] = data;
    assets[name] = { file, pixels: [info.width, info.height] };
  }
  draft.assets = assets;
  const document = validateDocument(draft);
  const text = documentYAML(document);
  if (Buffer.byteLength(text) > 4 * 1024 * 1024) throw new DocumentError('Serialized YAML exceeds 4 MiB');
  // Stored ZIP members avoid ratio limits and are supported by the native reader.
  const bytes = zipSync({ 'carousel.yaml': Buffer.from(text, 'utf8'), ...files }, { level: 0 });
  if (bytes.byteLength > archiveLimit) throw new DocumentError('Archive exceeds 100 MiB');
  // Verify the actual deliverable, including the hashes of transformed image bytes.
  const unpacked = unzipSync(bytes);
  validateDocument(parseLayout(Buffer.from(unpacked['carousel.yaml']).toString('utf8')));
  for (const [path, data] of Object.entries(unpacked)) {
    if (path === 'carousel.yaml') continue;
    if (createHash('sha256').update(data).digest('hex') !== path.split('/')[1].split('.')[0]) throw new DocumentError(`Archive hash verification failed: ${path}`);
  }
  return { bytes, document, yaml: text, diagnostics: diagnoseDocument(document) };
}
