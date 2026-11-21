/*
 * EXECUTION-TOOL HELPER — not a schema reference.
 * Shared by the sibling runnable scripts; keep it alongside them. Do NOT copy
 * its payload literals or logic into a new codebase as if they were the API
 * spec — for payload shape, load the canonical developers.sinch.com docs
 * linked from ../../SKILL.md instead.
 */
/**
 * Shared Sinch API client utilities.
 *
 * Provides OAuth2 authentication, environment variable helpers, URL
 * construction restricted to documented Conversation API regions, and output
 * redaction. Used by all send_*.cjs, list_messages.cjs, and webhook scripts.
 */

const AUTH_URL = "https://auth.sinch.com/oauth2/token";
const REGION_HOSTS = Object.freeze({
  us: "us.conversation.api.sinch.com",
  eu: "eu.conversation.api.sinch.com",
  br: "br.conversation.api.sinch.com",
});
const ALLOWED_HOSTS = new Set(["auth.sinch.com", ...Object.values(REGION_HOSTS)]);
const REQUEST_TIMEOUT_MS = 30000;

const SENSITIVE_KEY = /secret|password|passwd|token|authorization|api[-_]?key|credential|private[-_]?key/i;
const NON_SENSITIVE_KEY = /^(next_?)?page_?token$|^token_request_type$|^total_size$/i;

function getEnv(name, defaultValue) {
  const value = process.env[name] || defaultValue;
  if (value === undefined || value === null) {
    process.stderr.write(`Error: ${name} environment variable is required\n`);
    process.exit(1);
  }
  return value;
}

/** Recursively replace values of secret-looking keys with "[REDACTED]". */
function redact(value) {
  if (Array.isArray(value)) return value.map(redact);
  if (value && typeof value === "object") {
    const out = {};
    for (const [key, v] of Object.entries(value)) {
      const isLeaf = v === null || typeof v !== "object";
      out[key] = isLeaf && v !== null && v !== "" && SENSITIVE_KEY.test(key) && !NON_SENSITIVE_KEY.test(key)
        ? "[REDACTED]"
        : redact(v);
    }
    return out;
  }
  return value;
}

/** Summarize an error response without echoing arbitrary server content. */
function describeError(status, bodyText) {
  let parsed;
  try {
    parsed = JSON.parse(bodyText);
  } catch {
    return `HTTP ${status}`;
  }
  const err = parsed && typeof parsed.error === "object" && parsed.error ? parsed.error : parsed;
  const parts = [];
  for (const field of ["code", "status", "message"]) {
    const v = err && err[field];
    if (typeof v === "string" || typeof v === "number") {
      parts.push(`${field}=${String(v).slice(0, 200)}`);
    }
  }
  return parts.length ? `HTTP ${status} (${parts.join(", ")})` : `HTTP ${status}`;
}

function assertAllowedUrl(url) {
  const parsed = url instanceof URL ? url : new URL(url);
  if (parsed.protocol !== "https:" || !ALLOWED_HOSTS.has(parsed.hostname) || parsed.port) {
    throw new Error(`Refusing to send credentials to unexpected URL origin: ${parsed.origin}`);
  }
  return parsed;
}

async function getAccessToken(keyId, keySecret) {
  const credentials = Buffer.from(`${keyId}:${keySecret}`).toString("base64");
  const res = await fetch(assertAllowedUrl(AUTH_URL), {
    method: "POST",
    headers: {
      Authorization: `Basic ${credentials}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({ grant_type: "client_credentials" }).toString(),
    redirect: "error",
    signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
  });

  const body = await res.text();
  if (!res.ok) {
    throw new Error(`Auth failed: ${describeError(res.status, body)}`);
  }
  let token;
  try {
    token = JSON.parse(body).access_token;
  } catch {
    token = undefined;
  }
  if (typeof token !== "string" || !token) {
    throw new Error("Auth failed: response did not contain an access token");
  }
  return token;
}

function encodeSegment(segment) {
  if (segment === "" || segment === "." || segment === "..") {
    throw new Error(`Invalid URL path segment: "${segment}"`);
  }
  // Keep ':' readable for custom methods such as messages:send.
  return encodeURIComponent(segment).replace(/%3A/gi, ":");
}

/**
 * Build a Conversation API URL. `region` must be one of us, eu, br.
 * `path` segments are percent-encoded; an optional "?query" suffix is kept as given.
 */
function apiUrl(region, projectId, path) {
  const key = String(region || "").toLowerCase();
  if (!Object.prototype.hasOwnProperty.call(REGION_HOSTS, key)) {
    throw new Error(
      `Unknown SINCH_REGION '${region}'. Valid: ${Object.keys(REGION_HOSTS).join(", ")}`,
    );
  }
  const [pathPart, query] = String(path).split(/\?(.*)/s, 2);
  const encodedPath = pathPart.split("/").map(encodeSegment).join("/");
  const url = new URL(
    `https://${REGION_HOSTS[key]}/v1/projects/${encodeSegment(String(projectId))}/${encodedPath}`,
  );
  if (query) url.search = query;
  return assertAllowedUrl(url).toString();
}

async function httpRequest(url, options, body) {
  const res = await fetch(assertAllowedUrl(url), {
    method: options.method || "GET",
    headers: options.headers || {},
    body: body,
    redirect: "error",
    signal: AbortSignal.timeout(options.timeoutMs || REQUEST_TIMEOUT_MS),
  });

  const data = await res.text();
  if (!res.ok) {
    throw new Error(`API error: ${describeError(res.status, data)}`);
  }

  try {
    return JSON.parse(data);
  } catch {
    return data;
  }
}

module.exports = {
  REGION_HOSTS,
  getEnv,
  getAccessToken,
  apiUrl,
  httpRequest,
  redact,
};
