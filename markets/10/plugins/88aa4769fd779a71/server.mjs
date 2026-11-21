import { createHttpServer } from './src/http.mjs';

const CANONICAL_ORIGIN = 'https://peptara-calculator.vercel.app';
const VERCEL_HOST = /^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.vercel\.app$/;
const isVercel = process.env.VERCEL === '1';

function configuredOrigin(value) {
  const url = new URL(value);
  if (url.protocol !== 'https:' || url.username || url.password ||
      url.pathname !== '/' || url.search || url.hash) {
    throw new Error('PUBLIC_BASE_URL must be an HTTPS origin without credentials, a path, query, or fragment.');
  }
  return url.origin;
}

const explicitOrigin = process.env.PUBLIC_BASE_URL
  ? configuredOrigin(process.env.PUBLIC_BASE_URL)
  : undefined;
const vercelOrigins = isVercel
  ? [process.env.VERCEL_URL, process.env.VERCEL_PROJECT_PRODUCTION_URL, process.env.VERCEL_BRANCH_URL]
    .filter(value => typeof value === 'string' && VERCEL_HOST.test(value))
    .map(host => `https://${host}`)
  : [];

if (isVercel && !explicitOrigin && vercelOrigins.length === 0) {
  throw new Error('Vercel requires a configured public HTTPS origin or a valid Vercel deployment hostname.');
}

const publicBaseUrls = [...new Set([
  explicitOrigin,
  ...(isVercel ? [CANONICAL_ORIGIN, ...vercelOrigins] : []),
].filter(Boolean))];
const port = Number(process.env.PORT ?? 4317);
if (!Number.isInteger(port) || port < 1 || port > 65535) {
  throw new Error('PORT must be an integer from 1 to 65535.');
}

const server = createHttpServer({ publicBaseUrls });
// Vercel captures this listener. Direct local use stays on loopback.
if (isVercel) server.listen(port);
else server.listen(port, '127.0.0.1');
