import { createServer } from 'node:http';
import { randomBytes } from 'node:crypto';
import { pathToFileURL } from 'node:url';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { z } from 'zod';
import { buildCarousel, imageLimit, photoFormat } from './archive.mjs';
import { DocumentError, parseLayout, referencedAssets, validateDocument } from './document.mjs';

import { getSpecResponse, designGuide, packageVersion, capabilities } from './spec.mjs';
import { categories } from './catalog.mjs';
import { diagnoseDocument } from './diagnostics.mjs';
import { nativeRenderer } from './renderer.mjs';

const fileInput = z.object({ download_url: z.string().url(), file_id: z.string().min(1), mime_type: z.string().optional(), file_name: z.string().optional(), asset_name: z.string().min(1).max(128).optional() }).strict();
const fileName = name => (name.normalize('NFC').replace(/[\u0000-\u001f\u007f/\\<>:"|?*]/g, '-').replace(/\.carousel$/i, '').trim().slice(0, 64) || 'carousel') + '.carousel';
const failure = error => ({ isError: true, content: [{ type: 'text', text: error instanceof DocumentError ? error.message : `Could not create the file: ${error.message}` }] });

export class ArtifactStore {
  constructor({ ttl = 3_600_000, capacity = 256 * 1024 * 1024, now = Date.now } = {}) {
    this.ttl = ttl; this.capacity = capacity; this.now = now; this.files = new Map();
  }
  prune() {
    for (const [id, entry] of this.files) if (entry.expires <= this.now()) this.files.delete(id);
  }
  add(name, bytes) { return this.addMany([{ name, bytes, mimeType: 'application/octet-stream' }])[0]; }
  addMany(items) {
    this.prune();
    const total = [...this.files.values()].reduce((n, f) => n + f.bytes.byteLength, 0);
    if (total + items.reduce((n, item) => n + item.bytes.byteLength, 0) > this.capacity || this.files.size + items.length > 200) throw new DocumentError('Temporary storage is full. Wait for old download links to expire.');
    const prepared = items.map(({ name, bytes, mimeType }) => {
      if (!['image/png', 'application/octet-stream'].includes(mimeType)) throw new DocumentError('Unsupported artifact type');
      const safeName = mimeType === 'image/png' ? fileName(name.replace(/\.png$/i, '')).replace(/\.carousel$/, '.png') : fileName(name);
      return { id: randomBytes(24).toString('hex'), name: safeName, bytes, mimeType, expires: this.now() + this.ttl };
    });
    for (const { id, ...entry } of prepared) this.files.set(id, entry);
    return prepared;
  }
  get(id) { this.prune(); return this.files.get(id); }
}

class UploadError extends DocumentError {
  constructor(message, status) { super(message); this.status = status; }
}

// One-time links for photographs that exist only on the user's computer. Bytes are only packaged into projects, never served back.
export class UploadStore {
  constructor({ ttl = 3_600_000, capacity = 256 * 1024 * 1024, limit = imageLimit, now = Date.now } = {}) {
    this.ttl = ttl; this.capacity = capacity; this.limit = limit; this.now = now; this.slots = new Map();
  }
  prune() {
    for (const [id, slot] of this.slots) if (slot.expires <= this.now()) this.slots.delete(id);
  }
  reserve(names) {
    this.prune();
    if (new Set(names).size !== names.length) throw new DocumentError('asset_names: each photograph needs a distinct asset_name; duplicate names');
    if (this.slots.size + names.length > 200) throw new DocumentError('Temporary storage is full. Wait for old upload links to expire.');
    const expires = this.now() + this.ttl;
    return names.map(name => {
      const id = randomBytes(24).toString('hex');
      this.slots.set(id, { name, expires, bytes: null });
      return { id, name, expires };
    });
  }
  async receive(id, bytes) {
    const slot = this.get(id);
    if (!slot) throw new UploadError('Upload link expired or not found; call prepare_photo_upload again', 404);
    if (slot.bytes) throw new UploadError('This upload link was already used; call prepare_photo_upload for a new one', 409);
    if (bytes.byteLength > this.limit) throw new UploadError(`Photograph exceeds ${this.limit} bytes`, 413);
    const stored = [...this.slots.values()].reduce((n, entry) => n + (entry.bytes?.byteLength ?? 0), 0);
    if (stored + bytes.byteLength > this.capacity) throw new UploadError('Temporary storage is full. Try again later.', 507);
    const format = await photoFormat(bytes);
    if (!format) throw new UploadError('Send one still photograph per link: JPEG, PNG, WebP or AVIF', 415);
    // Another request may have filled or expired the slot while the header was read.
    if (slot.bytes || this.get(id) !== slot) throw new UploadError('This upload link was already used; call prepare_photo_upload for a new one', 409);
    slot.bytes = bytes;
    return { upload_id: id, asset_name: slot.name, format, bytes: bytes.byteLength };
  }
  get(id) { this.prune(); return this.slots.get(id); }
}

const readUpload = (request, limit) => new Promise((resolve, reject) => {
  const tooLarge = () => new UploadError(`Photograph exceeds ${limit} bytes`, 413);
  if (Number(request.headers['content-length']) > limit) { reject(tooLarge()); return; }
  const chunks = []; let length = 0;
  request.on('data', chunk => { length += chunk.byteLength; if (length <= limit) chunks.push(chunk); });
  request.on('end', () => length > limit ? reject(tooLarge()) : resolve(Buffer.concat(chunks)));
  request.on('error', reject);
});

export async function downloadImage(file, fetcher = fetch) {
  const url = new URL(file.download_url);
  const allowed = url.hostname === 'chatgpt.com' || url.hostname === 'oaiusercontent.com' || url.hostname.endsWith('.oaiusercontent.com');
  if (url.protocol !== 'https:' || !allowed || url.username || url.password || (url.port && url.port !== '443')) throw new DocumentError('Image download URL must be an HTTPS file URL supplied by ChatGPT');
  // Do not follow redirects from allowed public hosts into arbitrary/private networks.
  const response = await fetcher(url, { redirect: 'error', signal: AbortSignal.timeout(30_000) });
  if (!response.ok) throw new DocumentError(`Image download failed with HTTP ${response.status}; attach the file again if its link expired`);
  if (Number(response.headers.get('content-length')) > imageLimit) throw new DocumentError('Attached image exceeds 20 MiB');
  const reader = response.body.getReader();
  const chunks = []; let length = 0;
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      length += value.byteLength;
      if (length > imageLimit) throw new DocumentError('Attached image exceeds 20 MiB');
      chunks.push(value);
    }
  } catch (error) {
    await reader.cancel(); throw error;
  } finally { reader.releaseLock(); }
  return Buffer.concat(chunks);
}

export function createMCPServer({ publicURL, store = new ArtifactStore(), uploads = new UploadStore(), download = downloadImage, renderer = null } = {}) {
  const url = new URL(publicURL);
  if (url.username || url.password || url.search || url.hash || !['https:', 'http:'].includes(url.protocol) || (url.protocol === 'http:' && !['localhost', '127.0.0.1', '[::1]'].includes(url.hostname))) throw new Error('CAROUSEL_PUBLIC_URL must be an HTTPS origin, or localhost for development');
  const baseURL = url.href.replace(/\/$/, '');
  const versions = { ...capabilities, native_renderer: Boolean(renderer), renderer: renderer?.metadata ?? null, preview_formats: renderer ? ['image/png'] : [], photo_uploads: true };
  const artifactURL = entry => `${baseURL}/downloads/${entry.id}/${encodeURIComponent(entry.name)}`;
  const buildInput = async (yaml, asset_files = [], photo_uploads = []) => {
    const draft = validateDocument(parseLayout(yaml), { allowUnresolvedAssets: true });
    const images = new Map(), used = referencedAssets(draft);
    const uploaded = photo_uploads.map(id => {
      const slot = uploads.get(id);
      if (!slot) throw new DocumentError(`photo_uploads: upload ${id} expired or was never prepared; call prepare_photo_upload again`);
      if (!slot.bytes) throw new DocumentError(`photo_uploads: no file was sent for ${slot.name}; PUT the photograph to its upload_url first`);
      return [slot.name, slot.bytes];
    });
    const names = [...asset_files.map((file, index) => file.asset_name ?? `photo_${index + 1}`), ...uploaded.map(([name]) => name)];
    const duplicate = names.find((name, index) => names.indexOf(name) !== index);
    if (duplicate !== undefined) throw new DocumentError(`asset_files/photo_uploads: duplicate asset_name ${duplicate}`);
    for (const [name, bytes] of uploaded) if (used.has(name)) images.set(name, bytes);
    for (const [index, file] of asset_files.entries()) if (used.has(names[index])) images.set(names[index], await download(file));
    return buildCarousel(yaml, images);
  };
  const uploadInput = z.array(z.string().regex(/^[a-f0-9]{48}$/)).max(20).optional();
  const renderPreview = async (project, width) => {
    const result = await renderer.render(project.bytes, { width, slideCount: project.document.slides });
    const entries = store.addMany([
      { name: 'preview.png', bytes: result.sheet, mimeType: 'image/png' },
      ...result.slides.map(slide => ({ name: slide.file, bytes: slide.bytes, mimeType: 'image/png' }))
    ]);
    return {
      preview: { status: 'rendered', engine: result.engine, sheet_url: artifactURL(entries[0]), expires_at: new Date(entries[0].expires).toISOString(), warnings: result.warnings,
        slides: result.slides.map(({ bytes, file, ...slide }, index) => ({ ...slide, url: artifactURL(entries[index + 1]) })) },
      content: [
        { type: 'image', mimeType: 'image/png', data: Buffer.from(result.sheet).toString('base64') },
        ...entries.map(entry => ({ type: 'resource_link', name: entry.name, uri: artifactURL(entry), mimeType: 'image/png', description: 'Native ACE preview' }))
      ]
    };
  };
  const server = new McpServer({ name: 'carousel-creator', version: packageVersion }, {
    instructions: 'Create editable ACE projects. Read get_carousel_spec overview, then rules and relevant catalogs/examples. When writing or revising copy, also read section: writing. Compose before create_carousel. Use real catalog IDs and supplied photographs. For photographs on the user’s computer, when you can run shell commands, call prepare_photo_upload, PUT each file to its upload_url, and pass the upload IDs as photo_uploads. Photographs attached only in a chat without file references cannot reach this server: leave intentional empty photo slots (source: null) and say that the photos are added in ACE. Preserve language and line breaks. Review warnings; do not flatten content to suppress them. When native_renderer is true, create_carousel automatically returns a native contact sheet as image content and per-slide PNG links. Display that image in the chat alongside the editable file. Inspect every slide and use render_carousel to iterate; rendering alone is not a visual review. Report preview failures instead of claiming it was checked. Import via ACE → Projects or Templates → Import.\n\n' + designGuide
  });
  server.registerTool('get_carousel_spec', {
    title: 'Carousel Format and Resources',
    description: 'Read overview for design decisions and capability versions, writing before composing or revising copy (grounded angles, voice, storytelling and editorial review), rules for the native contract, catalogs for complete resources/geometry, or examples for diverse editable compositions. Catalog category avoids ambiguous substring matches; query supports exact IDs and category synonyms. Follow next_offset for more matches. Examples and schemas are not visual previews or ready-to-use copy.',
    inputSchema: { section: z.enum(['overview', 'writing', 'rules', 'catalogs', 'examples', 'full']).default('rules'), query: z.string().max(200).default(''), category: z.enum(categories).optional(), offset: z.number().int().nonnegative().default(0), limit: z.number().int().min(1).max(50).default(12) },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false }
  }, async ({ section, query, ...options }) => {
    try {
      const result = getSpecResponse(section, query, options);
      const { text, ...metadata } = result;
      return { content: [{ type: 'text', text: section === 'overview' ? text + '\n\nConnected server capabilities:\n' + JSON.stringify(versions) : text }], structuredContent: { ...metadata, capabilities: versions } };
    } catch (error) { return failure(error); }
  });
  server.registerTool('validate_carousel', {
    title: 'Validate Carousel', description: 'Validate native YAML and return actionable, non-blocking design/portability warnings. Set allow_unresolved_assets for a draft with real asset keys; the result explicitly lists unresolved references. Creation still requires real image bytes. No native visual or text measurement check is performed.',
    inputSchema: { yaml: z.string().max(4 * 1024 * 1024), allow_unresolved_assets: z.boolean().default(false) },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false }
  }, async ({ yaml, allow_unresolved_assets }) => {
    try {
      const document = validateDocument(parseLayout(yaml), { allowUnresolvedAssets: allow_unresolved_assets });
      const unresolved_assets = [...referencedAssets(document)].filter(name => !Object.hasOwn(document.assets ?? {}, name));
      const result = { valid: true, slides: document.slides, layers: document.layers.length, requires: document.requires, asset_references_resolved: unresolved_assets.length === 0, unresolved_assets, asset_bytes_checked: false, ...diagnoseDocument(document), visual_check: 'not performed', versions };
      return { content: [{ type: 'text', text: JSON.stringify(result) }], structuredContent: result };
    } catch (error) { return failure(error); }
  });
  server.registerTool('create_carousel', {
    title: 'Create Carousel File',
    description: 'Package complete editable YAML into a downloadable ACE .carousel project. When native_renderer is available, automatically return a native contact-sheet image for display in chat and PNG links for every slide. Compose content and layout first using get_carousel_spec. For photographs, omit draft assets and use source keys matching asset_files[].asset_name (default photo_1, photo_2...) or the asset_name of each upload listed in photo_uploads. Only referenced images are included; metadata is stripped and hashes generated automatically. Empty slots use source: null. Supports still images, not video. Preview failure is reported without losing the editable file. Links expire after one hour.',
    inputSchema: { yaml: z.string().max(4 * 1024 * 1024), filename: z.string().min(1).max(100).default('carousel'), asset_files: z.array(fileInput).max(20).optional(), photo_uploads: uploadInput, preview: z.boolean().default(true), preview_width: z.number().int().min(360).max(1080).default(720) },
    annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: true },
    _meta: { 'openai/fileParams': ['asset_files'] }
  }, async ({ yaml, filename, asset_files = [], photo_uploads = [], preview, preview_width }) => {
    try {
      const result = await buildInput(yaml, asset_files, photo_uploads);
      const entry = store.add(filename, result.bytes);
      const downloadURL = artifactURL(entry);
      let rendered = { preview: { status: preview ? 'unavailable' : 'skipped', reason: preview ? 'Native renderer is not configured on this server' : 'Preview was disabled by the caller' }, content: [] };
      if (preview && renderer) {
        try { rendered = await renderPreview(result, preview_width); }
        catch (error) { rendered = { preview: { status: 'failed', reason: error.message }, content: [] }; }
      }
      const summary = { filename: entry.name, download_url: downloadURL, expires_at: new Date(entry.expires).toISOString(), slides: result.document.slides, layers: result.document.layers.length, bytes: result.bytes.byteLength, ...result.diagnostics, versions, preview: rendered.preview, visual_check: rendered.preview.status === 'rendered' ? 'native preview rendered; visual review pending' : 'not performed', import: 'ACE: Aesthetic Carousel Editor → Projects (or Templates) → Import → choose the downloaded .carousel file' };
      return { content: [{ type: 'text', text: JSON.stringify(summary) }, { type: 'resource_link', name: entry.name, uri: downloadURL, mimeType: 'application/octet-stream', description: 'Editable ACE project; download and import into ACE: Aesthetic Carousel Editor' }, ...rendered.content], structuredContent: summary };
    } catch (error) { return failure(error); }
  });
  server.registerTool('render_carousel', {
    title: 'Render Native Carousel Preview',
    description: 'Render every slide with ACE SlideRasterizer, including native fonts, frames, grids, blend modes, masks and multi-composition. Returns a contact sheet as image content for display in chat and individual PNG URLs. Requires capabilities.native_renderer=true and real supplied assets. Use for visual iteration before final delivery; this does not certify visual quality.',
    inputSchema: { yaml: z.string().max(4 * 1024 * 1024), asset_files: z.array(fileInput).max(20).optional(), photo_uploads: uploadInput, width: z.number().int().min(360).max(1080).default(720) },
    annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: true },
    _meta: { 'openai/fileParams': ['asset_files'] }
  }, async ({ yaml, asset_files, photo_uploads, width }) => {
    try {
      if (!renderer) throw new DocumentError('Native rendering is unavailable on this server. Configure CAROUSEL_RENDERER_CONFIG on macOS.');
      const project = await buildInput(yaml, asset_files, photo_uploads);
      const rendered = await renderPreview(project, width);
      const summary = { slides: project.document.slides, ...project.diagnostics, versions, preview: rendered.preview, visual_check: 'native preview rendered; visual review pending' };
      return { content: [{ type: 'text', text: JSON.stringify(summary) }, ...rendered.content], structuredContent: summary };
    } catch (error) { return failure(error); }
  });
  server.registerTool('prepare_photo_upload', {
    title: 'Prepare Photo Upload',
    description: 'Reserve one-time HTTPS upload links for photographs stored on the user’s computer, for clients that can run shell commands. Send each file with an HTTP PUT, for example curl -sS --fail-with-body -T photo.jpg "<upload_url>", then pass the upload IDs as photo_uploads to create_carousel or render_carousel and use each asset_name as an image layer source. Each link takes one still JPEG, PNG, WebP or AVIF photograph up to max_bytes; convert HEIC to JPEG first. Uploaded photographs are only packaged into projects, never served back, and expire after one hour.',
    inputSchema: { asset_names: z.array(z.string().min(1).max(128)).min(1).max(20) },
    annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: false }
  }, async ({ asset_names }) => {
    try {
      const slots = uploads.reserve(asset_names);
      const result = { uploads: slots.map(slot => ({ asset_name: slot.name, upload_id: slot.id, upload_url: `${baseURL}/uploads/${slot.id}` })), method: 'PUT', max_bytes: uploads.limit, expires_at: new Date(slots[0].expires).toISOString() };
      return { content: [{ type: 'text', text: JSON.stringify(result) }], structuredContent: result };
    } catch (error) { return failure(error); }
  });
  return server;
}

export function httpServer(configuration) {
  const store = configuration.store ?? new ArtifactStore();
  const uploads = configuration.uploads ?? new UploadStore();
  const renderer = configuration.renderer ?? null;
  return createServer(async (request, response) => {
    const path = new URL(request.url, 'http://localhost').pathname;
    if (path === '/health' && request.method === 'GET') {
      response.writeHead(200, { 'Content-Type': 'application/json' }); response.end('{"ok":true}'); return;
    }
    const upload = /^\/uploads\/([a-f0-9]{48})$/.exec(path);
    if (upload) {
      if (!['PUT', 'POST'].includes(request.method)) { response.writeHead(405, { Allow: 'PUT, POST' }); response.end(); return; }
      let status = 200, body;
      try { body = await uploads.receive(upload[1], await readUpload(request, uploads.limit)); }
      catch (error) { status = error.status ?? 400; body = { error: error.message }; }
      // An oversized body is left unread, so the connection cannot be reused.
      response.writeHead(status, { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', ...(status === 413 ? { Connection: 'close' } : {}) });
      response.end(JSON.stringify(body)); return;
    }
    const match = /^\/downloads\/([a-f0-9]{48})\/([^/]+)$/.exec(path);
    if (match && ['GET', 'HEAD'].includes(request.method)) {
      const entry = store.get(match[1]);
      let name;
      try { name = decodeURIComponent(match[2]); } catch { /* invalid URI is a missing file */ }
      if (!entry || name !== entry.name) { response.writeHead(404); response.end('Download expired or not found'); return; }
      response.writeHead(200, { 'Content-Type': entry.mimeType, 'Content-Length': entry.bytes.byteLength, 'Content-Disposition': `${entry.mimeType === 'image/png' ? 'inline' : 'attachment'}; filename*=UTF-8''${encodeURIComponent(entry.name)}`, 'Cache-Control': 'private, no-store', 'X-Content-Type-Options': 'nosniff' });
      response.end(request.method === 'HEAD' ? undefined : entry.bytes); return;
    }
    if (path !== '/mcp' || request.method !== 'POST') { response.writeHead(path === '/mcp' ? 405 : 404); response.end(); return; }
    const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined, enableJsonResponse: true });
    const server = createMCPServer({ publicURL: configuration.publicURL, store, uploads, renderer, download: configuration.download });
    response.on('close', () => { void transport.close(); void server.close(); });
    try { await server.connect(transport); await transport.handleRequest(request, response); }
    catch { if (!response.headersSent) response.writeHead(500); response.end(); }
  });
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const port = Number(process.env.CAROUSEL_PORT ?? 8787);
  const publicURL = process.env.CAROUSEL_PUBLIC_URL ?? `http://127.0.0.1:${port}`;
  // Validate configuration at startup, instead of failing during the first tool call.
  const renderer = nativeRenderer();
  const check = createMCPServer({ publicURL, renderer }); await check.close();
  const app = httpServer({ publicURL, renderer });
  app.listen(port, process.env.CAROUSEL_HOST ?? '127.0.0.1', () => console.log(`Carousel Creator MCP: ${publicURL}/mcp`));
  for (const signal of ['SIGINT', 'SIGTERM']) process.on(signal, () => app.close(() => process.exit(0)));
}
