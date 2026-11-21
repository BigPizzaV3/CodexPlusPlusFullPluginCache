import { McpServer, preloadSchemas, specTypeSchemas, parseJSONRPCMessage, PROTOCOL_VERSION_META_KEY, CLIENT_INFO_META_KEY, CLIENT_CAPABILITIES_META_KEY } from '@modelcontextprotocol/server';
import { createMcpHandler } from 'agents/mcp/server';
import { BudgetInputError } from './budget';
import { remoteInputSchema, remoteOutputSchema, planRemoteBudget, validateRemote, cachedMcpSchema } from './remote-budget';

// Move static wire/schema construction into isolate startup. Each request
// still gets its own MCP server/transport; no request or user result is cached.
preloadSchemas();
const mcpInputSchema = cachedMcpSchema(remoteInputSchema);
const mcpOutputSchema = cachedMcpSchema(remoteOutputSchema);
remoteInputSchema.safeParse({});
remoteOutputSchema.safeParse(planRemoteBudget({}));
const syntheticMethods = [
  { method: 'initialize', params: { protocolVersion: '2025-11-25', capabilities: {},
    clientInfo: { name: 'schema-startup', version: '1' } } },
  { method: 'server/discover', params: {} },
  { method: 'tools/list', params: {} },
  { method: 'tools/call', params: { name: 'plan_context_budget', arguments: {} } },
  { method: 'ping', params: {} },
];
// SDK preload builds the schema objects; validate synthetic protocol shapes
// here as well to avoid charging their first validator setup to a real call.
for (const message of syntheticMethods) {
  specTypeSchemas.ClientRequest['~standard'].validate(message);
  parseJSONRPCMessage({ jsonrpc: '2.0', id: 1, ...message });
}
specTypeSchemas.CallToolResult['~standard'].validate({
  content: [{ type: 'text', text: '{}' }], structuredContent: planRemoteBudget({}),
});

interface Env {
  PUBLIC_ORIGIN?: string;
  DOMAIN_VERIFICATION_TOKEN?: string;
  MCP_IP_LIMITER?: RateLimit;
  MCP_SERVICE_LIMITER?: RateLimit;
}
const MAX_BYTES = 16 * 1024;
const DESCRIPTION = 'Calculate reference headroom, next-task usage and five future turns from explicit token counts and a supplied growth-rate estimate. Missing inputs stay unknown. No chat history, past-turn arrays, local file, account, model API or pricing access.';
function createServer() {
  const server = new McpServer({ name: 'token-weather-budget', version: '1.0.0' });
  server.registerTool('plan_context_budget', {
    title: 'Plan a token budget', description: DESCRIPTION, inputSchema:mcpInputSchema, outputSchema:mcpOutputSchema,
    annotations: { readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: false },
  }, async args => {
    try {
      const result = planRemoteBudget(args);
      return { content: [{ type: 'text' as const, text: JSON.stringify(result) }], structuredContent: result };
    } catch {
      return { isError: true, content: [{ type: 'text' as const, text: new BudgetInputError().message }] };
    }
  });
  return server;
}
// Instantiate a disconnected synthetic server to prepare static SDK helpers.
// Every HTTP request still receives a new server from the factory above.
createServer();

function rpcError(code: number, message: string, id: string | number | null = null, status = 400) {
  return Response.json({ jsonrpc: '2.0', id, error: { code, message } },
    { status, headers: { 'Cache-Control': 'no-store' } });
}
function record(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}
function only(value: Record<string, unknown>, names: string[]) {
  return Object.keys(value).every(key => names.includes(key));
}
function validId(value: unknown): value is string | number {
  return (typeof value === 'number' && Number.isSafeInteger(value)) ||
    (typeof value === 'string' && /^[A-Za-z0-9_.:-]{1,96}$/.test(value) && !value.startsWith('sk-'));
}

function transportMeta(raw: unknown) {
  if (raw === undefined) return undefined;
  if (!record(raw)) throw new SyntaxError();
  const meta: Record<string, unknown> = {};
  const version = raw[PROTOCOL_VERSION_META_KEY];
  if (version !== undefined) {
    if (typeof version !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(version)) throw new SyntaxError();
    meta[PROTOCOL_VERSION_META_KEY] = version;
  }
  const client = raw[CLIENT_INFO_META_KEY];
  if (client !== undefined) {
    if (!record(client) || typeof client.name !== 'string' || typeof client.version !== 'string' ||
        client.name.length > 96 || client.version.length > 96) throw new SyntaxError();
    meta[CLIENT_INFO_META_KEY] = { name: client.name, version: client.version };
  }
  if (raw[CLIENT_CAPABILITIES_META_KEY] !== undefined) meta[CLIENT_CAPABILITIES_META_KEY] = {};
  return Object.keys(meta).length ? meta : undefined;
}

async function readBody(request: Request) {
  const length = request.headers.get('Content-Length');
  if (length !== null && (!/^\d{1,5}$/.test(length) || Number(length) > MAX_BYTES)) throw new RangeError();
  if (!request.body) throw new SyntaxError();
  const reader = request.body.getReader();
  const chunks: Uint8Array[] = [];
  let size = 0;
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      size += value.length;
      if (size > MAX_BYTES) { await reader.cancel(); throw new RangeError(); }
      chunks.push(value);
    }
  } finally { reader.releaseLock(); }
  const raw = new Uint8Array(size);
  let offset = 0;
  for (const chunk of chunks) { raw.set(chunk, offset); offset += chunk.length; }
  const text = new TextDecoder('utf-8', { fatal: true }).decode(raw);
  const data: unknown = JSON.parse(text);
  // JSON.parse alone silently accepts duplicate keys. Validate each object
  // scope after syntax parsing to refuse ambiguous input without echoing it.
  const stack: Array<Set<string> | null> = [];
  for (let index = 0; index < text.length; index++) {
    const char = text[index];
    if (char === '{' || char === '[') {
      stack.push(char === '{' ? new Set() : null);
      if (stack.length > 32) throw new SyntaxError();
    } else if (char === '}' || char === ']') stack.pop();
    else if (char === '"') {
      const start = index++;
      while (index < text.length && text[index] !== '"') {
        if (text[index] === '\\') index++;
        index++;
      }
      let next = index + 1;
      while (/\s/.test(text[next] ?? '') && next < text.length) next++;
      if (text[next] === ':' && stack.at(-1) !== null) {
        const keys = stack.at(-1)!;
        const key: string = JSON.parse(text.slice(start, index + 1));
        if (keys.has(key)) throw new SyntaxError();
        keys.add(key);
      }
    }
  }
  return data;
}

async function enforceRateLimit(request: Request, env: Env, local: boolean) {
  if (local && !env.MCP_IP_LIMITER && !env.MCP_SERVICE_LIMITER) return null;
  if (!env.MCP_IP_LIMITER || !env.MCP_SERVICE_LIMITER) {
    return rpcError(-32603, 'Request protection is unavailable.', null, 503);
  }
  try {
    const total = await env.MCP_SERVICE_LIMITER.limit({ key: 'token-weather-budget:requests' });
    // Cloudflare supplies CF-Connecting-IP at the public edge. Never use a
    // caller-selected X-Forwarded-For value or a per-request random identifier.
    // Missing/invalid addresses share a bucket rather than bypassing the limit.
    const supplied = request.headers.get('CF-Connecting-IP') ?? '';
    const address = /^[0-9a-fA-F:.]{3,64}$/.test(supplied) ? supplied.toLowerCase() : 'unknown';
    const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(address));
    const key = 'token-weather-budget:ip:' + Array.from(new Uint8Array(digest),
      byte => byte.toString(16).padStart(2, '0')).join('');
    const actor = total.success ? await env.MCP_IP_LIMITER.limit({ key }) : { success: false };
    if (total.success && actor.success) return null;
    const response = rpcError(-32000, 'Too many requests. Retry later.', null, 429);
    response.headers.set('Retry-After', '60');
    return response;
  } catch {
    return rpcError(-32603, 'Request protection is unavailable.', null, 503);
  }
}

async function handleRequest(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    const local = ['127.0.0.1', 'localhost', '[::1]'].includes(url.hostname);
    if (!local && (!env.PUBLIC_ORIGIN || url.origin !== env.PUBLIC_ORIGIN || url.protocol !== 'https:')) {
      return rpcError(-32600, 'Production origin is not configured.', null, 503);
    }
    const limited = await enforceRateLimit(request, env, local);
    if (limited) return limited;
    if (url.search || request.headers.has('Authorization')) return rpcError(-32600, 'Unsupported request metadata.');
    const origin = request.headers.get('Origin');
    const permitted = [url.origin, 'https://chatgpt.com', 'https://chat.openai.com'];
    if (origin && !permitted.includes(origin)) return rpcError(-32600, 'Origin is not allowed.', null, 403);
    if (url.pathname === '/health' && request.method === 'GET') {
      return Response.json({ name: 'token-weather-budget', version: '1.0.0', stateless: true,
        tool_count: 1, model_api_calls: false, business_data_storage: false }, { headers: { 'Cache-Control': 'no-store' } });
    }
    if (url.pathname === '/.well-known/openai-apps-challenge' && request.method === 'GET') {
      const token = env.DOMAIN_VERIFICATION_TOKEN;
      if (!token || !/^[!-~]{1,2048}$/.test(token)) return new Response('Not configured', { status: 404 });
      return new Response(token, { headers: { 'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store' } });
    }
    if (url.pathname !== '/mcp') return rpcError(-32600, 'Endpoint not found.', null, 404);
    if (request.method !== 'POST') return new Response(null, { status: 405, headers: { Allow: 'POST' } });
    if (request.headers.get('Content-Type')?.split(';')[0].trim().toLowerCase() !== 'application/json') {
      return rpcError(-32600, 'Use application/json.', null, 415);
    }
    if (request.headers.get('Content-Encoding') && request.headers.get('Content-Encoding') !== 'identity') {
      return rpcError(-32600, 'Compressed request bodies are not accepted.', null, 415);
    }
    let message: unknown;
    try { message = await readBody(request); }
    catch (error) { return rpcError(error instanceof RangeError ? -32600 : -32700,
      error instanceof RangeError ? 'Request exceeds the 16 KiB limit.' : 'Invalid JSON.', null,
      error instanceof RangeError ? 413 : 400); }
    if (!record(message) || message.jsonrpc !== '2.0' || typeof message.method !== 'string' ||
      !only(message, ['jsonrpc', 'id', 'method', 'params'])) return rpcError(-32600, 'Expected one JSON-RPC request or notification.');
    const id = message.id;
    if (id !== undefined && !validId(id)) return rpcError(-32600, 'Invalid request identifier.');
    const method = message.method;
    if (id === undefined) {
      // No event/body history is retained. Only standard notifications are accepted.
      return new Response(null, { status: method.startsWith('notifications/') ? 202 : 400 });
    }
    const params = message.params ?? {};
    if (!record(params)) return rpcError(-32602, 'Parameters must be an object.', id);
    let safeParams: Record<string, unknown>;
    if (method === 'tools/call') {
      if (!only(params, ['name', 'arguments', '_meta']) || params.name !== 'plan_context_budget') {
        return rpcError(-32602, 'Unknown tool or unsupported call parameters.', id);
      }
      try { validateRemote(params.arguments ?? {}); }
      catch { return Response.json({ jsonrpc: '2.0', id, result: { isError: true,
        content: [{ type: 'text', text: new BudgetInputError().message }] } },
        { headers: { 'Cache-Control': 'no-store' } }); }
      safeParams = { name: 'plan_context_budget', arguments: params.arguments ?? {} };
    } else if (method === 'initialize') {
      if (!only(params, ['protocolVersion', 'capabilities', 'clientInfo', '_meta']) ||
        typeof params.protocolVersion !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(params.protocolVersion) ||
        !record(params.capabilities) || !record(params.clientInfo) ||
        typeof params.clientInfo.name !== 'string' || typeof params.clientInfo.version !== 'string' ||
        params.clientInfo.name.length > 96 || params.clientInfo.version.length > 96) {
        return rpcError(-32602, 'Invalid initialization metadata.', id);
      }
      safeParams = { protocolVersion: params.protocolVersion, capabilities: {},
        clientInfo: { name: params.clientInfo.name, version: params.clientInfo.version } };
    } else if (method === 'tools/list' || method === 'ping' || method === 'server/discover') {
      if (!only(params, ['_meta'])) return rpcError(-32602, 'Unsupported parameters.', id);
      safeParams = {};
    } else return rpcError(-32601, 'Method not supported.', id);
    try {
      const meta = transportMeta(params._meta);
      if (meta) safeParams._meta = meta;
    } catch { return rpcError(-32602, 'Unsupported transport metadata.', id); }
    const safeHeaders = new Headers(request.headers);
    safeHeaders.delete('Content-Length');
    const safeRequest = new Request(request, { headers: safeHeaders, body: JSON.stringify({ jsonrpc: '2.0', id, method, params: safeParams }) });
    try {
      const handler = createMcpHandler(createServer, { route: '/mcp', corsOptions: false,
        allowedHostnames: local ? ['localhost', '127.0.0.1', '[::1]', '::1'] : [url.hostname],
        allowedOriginHostnames: '*', onerror: () => {} });
      const response = await handler(safeRequest, env, ctx);
      const headers = new Headers(response.headers);
      headers.set('Cache-Control', 'no-store');
      return new Response(response.body, { status: response.status, headers });
    } catch { return rpcError(-32603, 'Budget service unavailable.', id, 500); }
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    let response: Response;
    try { response = await handleRequest(request, env, ctx); }
    catch { response = rpcError(-32603, 'Budget service unavailable.', null, 500); }
    const headers = new Headers(response.headers);
    headers.set('Cache-Control', 'no-store');
    headers.set('X-Content-Type-Options', 'nosniff');
    headers.set('Referrer-Policy', 'no-referrer');
    headers.set('Content-Security-Policy', "default-src 'none'; frame-ancestors 'none'");
    if (new URL(request.url).protocol === 'https:') {
      headers.set('Strict-Transport-Security', 'max-age=31536000');
    }
    return new Response(response.body, { status: response.status, headers });
  },
};
