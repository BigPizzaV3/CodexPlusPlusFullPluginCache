import { readFile, stat } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';

export const MAX_IMAGE_UPLOAD_BYTES = 4 * 1024 * 1024;

const MIME_SIGNATURES = [
  {
    mimeType: 'image/png',
    matches: (bytes) => bytes.length >= 8
      && bytes.subarray(0, 8).equals(Buffer.from([137, 80, 78, 71, 13, 10, 26, 10])),
  },
  {
    mimeType: 'image/jpeg',
    matches: (bytes) => bytes.length >= 3
      && bytes[0] === 0xff
      && bytes[1] === 0xd8
      && bytes[2] === 0xff,
  },
  {
    mimeType: 'image/webp',
    matches: (bytes) => bytes.length >= 12
      && bytes.toString('ascii', 0, 4) === 'RIFF'
      && bytes.toString('ascii', 8, 12) === 'WEBP',
  },
];

function fail(message) {
  throw new Error(message);
}

function parseJsonText(text) {
  try {
    return JSON.parse(text);
  } catch {
    return undefined;
  }
}

function unwrapUploadResult(value) {
  let candidate = value;

  if (typeof candidate === 'string') {
    candidate = parseJsonText(candidate);
  }
  if (!candidate || typeof candidate !== 'object') return undefined;

  for (let depth = 0; depth < 3; depth += 1) {
    if (candidate.uploadSessionId && candidate.uploadUrl) return candidate;

    if (candidate.structuredContent && typeof candidate.structuredContent === 'object') {
      candidate = candidate.structuredContent;
      continue;
    }

    if (Array.isArray(candidate.content)) {
      const parsedText = candidate.content
        .filter((item) => item && typeof item.text === 'string')
        .map((item) => parseJsonText(item.text))
        .find((item) => item && typeof item === 'object');
      if (parsedText) {
        candidate = parsedText;
        continue;
      }
    }

    return undefined;
  }

  return candidate?.uploadSessionId && candidate?.uploadUrl ? candidate : undefined;
}

function getUploadSessionId(value) {
  if (typeof value !== 'string' || !/^[A-Za-z0-9_-]{1,128}$/.test(value)) {
    fail('The upload session ID is missing or invalid.');
  }
  return value;
}

function getExpiryTimestamp(value) {
  const timestamp = typeof value === 'number'
    ? (value < 10_000_000_000 ? value * 1000 : value)
    : Date.parse(value);

  if (!Number.isFinite(timestamp)) fail('The upload session has no valid expiry time.');
  return timestamp;
}

function validateUploadUrl(rawUrl, sessionId, allowLocalhost) {
  let uploadUrl;
  try {
    uploadUrl = new URL(rawUrl);
  } catch {
    fail('The upload session returned an invalid URL.');
  }

  if (uploadUrl.username || uploadUrl.password || uploadUrl.hash) {
    fail('The upload URL contains unsupported URL components.');
  }

  const productionHost = uploadUrl.protocol === 'https:'
    && (uploadUrl.hostname === 'smepost.io' || uploadUrl.hostname === 'local.smepost.io')
    && (!uploadUrl.port || uploadUrl.port === '443');
  const loopbackHost = allowLocalhost
    && ['localhost', '127.0.0.1', '[::1]'].includes(uploadUrl.hostname)
    && ['http:', 'https:'].includes(uploadUrl.protocol);

  if (!productionHost && !loopbackHost) {
    fail('The upload URL must use an approved SMEPost HTTPS host. Use --allow-localhost only for a local emulator.');
  }

  if (uploadUrl.pathname !== `/api/workdesk/uploads/${sessionId}`) {
    fail('The upload URL does not match the upload session.');
  }

  if (!uploadUrl.searchParams.get('capability')) {
    fail('The upload URL is missing its short-lived capability.');
  }

  return uploadUrl;
}

function detectImageMimeType(bytes) {
  const signature = MIME_SIGNATURES.find(({ matches }) => matches(bytes));
  if (!signature) fail('The local file is not a supported PNG, JPEG, or WebP image.');
  return signature.mimeType;
}

function getContentType(headers, imageMimeType) {
  if (!headers || typeof headers !== 'object' || Array.isArray(headers)) {
    fail('The upload session returned invalid headers.');
  }

  const entries = Object.entries(headers);
  if (entries.some(([name]) => name.toLowerCase() !== 'content-type')) {
    fail('The upload session returned an unsupported header.');
  }

  const contentType = entries.find(([name]) => name.toLowerCase() === 'content-type')?.[1];
  if (contentType !== undefined && contentType !== imageMimeType) {
    fail('The image MIME type does not match the upload session.');
  }
  return contentType ?? imageMimeType;
}

async function readImageFile(filePath) {
  try {
    const fileStat = await stat(filePath);
    if (!fileStat.isFile() || fileStat.size <= 0) {
      fail('Choose a non-empty local image file.');
    }
    if (fileStat.size > MAX_IMAGE_UPLOAD_BYTES) {
      fail(`The image exceeds the ${MAX_IMAGE_UPLOAD_BYTES / (1024 * 1024)} MiB upload limit.`);
    }

    const bytes = await readFile(filePath);
    if (bytes.length > MAX_IMAGE_UPLOAD_BYTES) {
      fail(`The image exceeds the ${MAX_IMAGE_UPLOAD_BYTES / (1024 * 1024)} MiB upload limit.`);
    }
    const mimeType = detectImageMimeType(bytes);
    return { bytes, mimeType };
  } catch (error) {
    if (error instanceof Error && /^(The |Choose )/.test(error.message)) throw error;
    fail('The local image file could not be read.');
  }
}

/** Upload image bytes to a prepared SMEPost capability URL without completing the session. */
export async function uploadPreparedImage({
  uploadResult,
  imagePath,
  allowLocalhost = false,
  fetchImpl = fetch,
  now = Date.now(),
}) {
  const prepared = unwrapUploadResult(uploadResult);
  if (!prepared) fail('The prepare_asset_upload result is missing upload details.');

  const uploadSessionId = getUploadSessionId(prepared.uploadSessionId);
  const expiryTimestamp = getExpiryTimestamp(prepared.expiresAt);
  if (expiryTimestamp <= now) fail('The upload session has expired; prepare a new session.');

  const uploadUrl = validateUploadUrl(prepared.uploadUrl, uploadSessionId, allowLocalhost);
  if (typeof prepared.uploadMethod !== 'string' || prepared.uploadMethod.toUpperCase() !== 'PUT') {
    fail('The upload session must use PUT.');
  }

  const { bytes, mimeType } = await readImageFile(imagePath);
  const contentType = getContentType(prepared.headers, mimeType);

  let response;
  try {
    response = await fetchImpl(uploadUrl, {
      method: 'PUT',
      headers: { 'Content-Type': contentType },
      body: bytes,
      redirect: 'manual',
      signal: AbortSignal.timeout(120_000),
    });
  } catch {
    fail('The image upload request failed. Check the network and prepare a fresh upload session if needed.');
  }

  if (response.status >= 300 && response.status < 400) {
    fail('The upload server returned a redirect; the helper stopped without following it.');
  }
  if (!response.ok) {
    fail(`The upload server rejected the image with HTTP ${response.status}.`);
  }

  return { uploadSessionId };
}

async function main() {
  const args = process.argv.slice(2);
  const allowLocalhost = args.includes('--allow-localhost');
  const positionalArgs = args.filter((arg) => arg !== '--allow-localhost');
  const [preparedPath, imagePath, ...extraArgs] = positionalArgs;

  if (!preparedPath || !imagePath || extraArgs.length > 0) {
    console.error('Usage: node upload-asset.mjs <prepare-result.json> <image-file> [--allow-localhost]');
    process.exitCode = 2;
    return;
  }

  let uploadResult;
  try {
    uploadResult = JSON.parse(await readFile(preparedPath, 'utf8'));
  } catch {
    console.error('Could not read a valid prepare_asset_upload JSON result.');
    process.exitCode = 1;
    return;
  }

  try {
    const result = await uploadPreparedImage({ uploadResult, imagePath, allowLocalhost });
    console.log(JSON.stringify({
      uploaded: true,
      uploadSessionId: result.uploadSessionId,
      nextAction: 'Call complete_asset_upload with this uploadSessionId.',
    }));
  } catch (error) {
    console.error(error instanceof Error ? error.message : 'The image upload failed.');
    process.exitCode = 1;
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  await main();
}
