#!/usr/bin/env node
// Smoke test for the access layer. Boots the server with ENFORCE_OAUTH=1 on a
// random port and walks the whole OAuth + entitlement loop. Run: npm run smoke

import { spawn } from "node:child_process";
import { createHash, randomBytes } from "node:crypto";
import { mkdtemp } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = dirname(fileURLToPath(import.meta.url)) + "/..";
const PORT = 8799 + Math.floor(Math.random() * 100);
const BASE = `http://127.0.0.1:${PORT}`;
const REDIRECT = "https://chatgpt.com/connector_platform_oauth_redirect";
const GHL_SECRET = "smoke-ghl-secret";

const tmp = await mkdtemp(join(tmpdir(), "admachine-smoke-"));

const child = spawn("node", ["server.mjs"], {
  cwd: ROOT,
  stdio: ["ignore", "pipe", "pipe"],
  env: {
    ...process.env,
    PORT: String(PORT),
    HOST: "127.0.0.1",
    PUBLIC_URL: BASE,
    ENFORCE_OAUTH: "1",
    OAUTH_SECRET: "smoke-oauth-secret",
    ENTITLEMENT_SECRET: GHL_SECRET,
    DB_PATH: join(tmp, "smoke.db"),
    OPENAI_APPS_CHALLENGE: "challenge-token"
  }
});
child.stdout.resume();
child.stderr.resume();

let passed = 0;
const failures = [];

// Handles both the plain-JSON and SSE answers of a modern-era exchange.
async function jsonOrSse(res, requestId) {
  const text = await res.text();
  try {
    return JSON.parse(text);
  } catch {}
  return text
    .split("\n")
    .filter((line) => line.startsWith("data: "))
    .map((line) => JSON.parse(line.slice(6)))
    .find((msg) => msg?.id === requestId);
}

function check(name, condition, extra) {
  if (condition) {
    passed++;
    console.log(`  ok  ${name}`);
  } else {
    failures.push(name);
    console.log(`FAIL  ${name}${extra ? ` — ${extra}` : ""}`);
  }
}

async function waitForServer() {
  for (let i = 0; i < 60; i++) {
    try {
      const res = await fetch(`${BASE}/health`);
      if (res.ok) return true;
    } catch { /* not up yet */ }
    await new Promise((r) => setTimeout(r, 150));
  }
  return false;
}

function pkcePair() {
  const verifier = randomBytes(32).toString("base64url");
  const challenge = createHash("sha256").update(verifier).digest("base64url");
  return { verifier, challenge };
}

try {
  check("server boots", await waitForServer());

  // discovery
  const pr = await (await fetch(`${BASE}/.well-known/oauth-protected-resource`)).json();
  check("protected-resource metadata", pr.authorization_servers?.[0] === BASE);
  const as = await (await fetch(`${BASE}/.well-known/oauth-authorization-server`)).json();
  check("auth-server metadata", as.token_endpoint === `${BASE}/token` && as.code_challenge_methods_supported.includes("S256"));

  // dynamic client registration
  const regRes = await fetch(`${BASE}/register`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ client_name: "smoke", redirect_uris: [REDIRECT] })
  });
  const reg = await regRes.json();
  check("register client", regRes.status === 201 && !!reg.client_id);

  // webhook: grant buyer@smoke.test (server generates license code)
  const grantRes = await fetch(`${BASE}/entitlement`, {
    method: "POST",
    headers: { "content-type": "application/json", "x-ghl-secret": GHL_SECRET },
    body: JSON.stringify({ action: "grant", email: "buyer@smoke.test" })
  });
  const grant = await grantRes.json();
  check("webhook grant", grant.ok === true && /^AD-[A-Z2-9]{8}$/.test(grant.license_code ?? ""), JSON.stringify(grant));

  // webhook: bad secret rejected
  const badSecret = await fetch(`${BASE}/entitlement`, {
    method: "POST",
    headers: { "content-type": "application/json", "x-ghl-secret": "wrong" },
    body: JSON.stringify({ action: "grant", email: "x@y.z" })
  });
  check("webhook rejects bad secret", badSecret.status === 401);

  // metadata reads stay open for the portal's automated scan
  const noAuth = await fetch(`${BASE}/mcp`, {
    method: "POST",
    headers: { "content-type": "application/json", accept: "application/json, text/event-stream" },
    body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "2025-03-26", capabilities: {}, clientInfo: { name: "t", version: "0" } } })
  });
  check("unauth initialize allowed (scan path)", noAuth.status === 200);

  // tool execution without license -> 401 + metadata header
  const noAuthCall = await fetch(`${BASE}/mcp`, {
    method: "POST",
    headers: { "content-type": "application/json", accept: "application/json, text/event-stream" },
    body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "tools/call", params: { name: "search_knowledge", arguments: { query: "forever ad" } } })
  });
  check("unauth tools/call -> 401", noAuthCall.status === 401);
  check("401 carries resource_metadata", (noAuthCall.headers.get("www-authenticate") ?? "").includes("resource_metadata"));

  // portal scanner's 2026-07-28 discovery: envelope claim + version/method
  // headers route it to the modern leg. Responses may stream SSE frames.
  const discoverRes = await fetch(`${BASE}/mcp`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      accept: "application/json, text/event-stream",
      "MCP-Protocol-Version": "2026-07-28",
      "Mcp-Method": "server/discover"
    },
    body: JSON.stringify({
      jsonrpc: "2.0", id: 1, method: "server/discover",
      params: { _meta: { "io.modelcontextprotocol/protocolVersion": "2026-07-28", "io.modelcontextprotocol/clientCapabilities": {} } }
    })
  });
  const discoverBody = await jsonOrSse(discoverRes, 1);
  check("server/discover answered", discoverRes.status === 200 && discoverBody?.result?.resultType === "complete" && discoverBody?.result?.supportedVersions?.[0] === "2026-07-28");
  check("server/discover stamps serverInfo", !!discoverBody?.result?._meta?.["io.modelcontextprotocol/serverInfo"]?.name);

  // modern-envelope tools/list proves the tools capability handlers installed
  const modernListRes = await fetch(`${BASE}/mcp`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      accept: "application/json, text/event-stream",
      "MCP-Protocol-Version": "2026-07-28",
      "Mcp-Method": "tools/list"
    },
    body: JSON.stringify({
      jsonrpc: "2.0", id: 2, method: "tools/list",
      params: { _meta: { "io.modelcontextprotocol/protocolVersion": "2026-07-28", "io.modelcontextprotocol/clientCapabilities": {} } }
    })
  });
  const modernListBody = await jsonOrSse(modernListRes, 2);
  const modernToolNames = (modernListBody?.result?.tools ?? []).map((t) => t.name);
  check("modern tools/list serves both tools", modernListRes.status === 200 && modernToolNames.includes("search_knowledge") && modernToolNames.includes("read_knowledge_document"));

  // login page renders
  const { verifier, challenge } = pkcePair();
  const authUrl = `${BASE}/authorize?response_type=code&client_id=${encodeURIComponent(reg.client_id)}&redirect_uri=${encodeURIComponent(REDIRECT)}&code_challenge=${challenge}&code_challenge_method=S256&state=st123&resource=${encodeURIComponent(BASE + "/mcp")}`;
  const realAuthUrl = authUrl;
  const loginPage = await fetch(realAuthUrl);
  const loginHtml = await loginPage.text();
  check("login page renders", loginPage.status === 200 && loginHtml.includes("Email used at checkout"));

  // email match login -> authorization code
  const formParams = new URLSearchParams(realAuthUrl.split("?")[1]);
  const grantForm = new URLSearchParams(formParams);
  grantForm.set("email", "buyer@smoke.test");
  grantForm.set("license_code", "");
  const loginRes = await fetch(`${BASE}/authorize/grant`, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: grantForm.toString(),
    redirect: "manual"
  });
  const location = loginRes.headers.get("location") ?? "";
  check("login redirects with code", loginRes.status === 302 && location.startsWith(REDIRECT) && location.includes("code="));
  const code = new URL(location).searchParams.get("code");
  check("state round-trips", new URL(location).searchParams.get("state") === "st123");

  // wrong email without code -> retry page, not a code
  const badForm = new URLSearchParams(formParams);
  badForm.set("email", "stranger@smoke.test");
  badForm.set("license_code", "");
  const badRes = await fetch(`${BASE}/authorize/grant`, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: badForm.toString(),
    redirect: "manual"
  });
  check("unknown email rejected", badRes.status === 401 && !(await badRes.text()).includes("name=\"code\""));

  // exchange code (PKCE) -> tokens
  const tokenRes = await fetch(`${BASE}/token`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      grant_type: "authorization_code",
      code,
      code_verifier: verifier,
      client_id: reg.client_id,
      redirect_uri: REDIRECT,
      resource: `${BASE}/mcp`
    })
  });
  const tokens = await tokenRes.json();
  check("token exchange", tokenRes.status === 200 && !!tokens.access_token && !!tokens.refresh_token);

  // code replay rejected
  const replay = await fetch(`${BASE}/token`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ grant_type: "authorization_code", code, code_verifier: verifier, client_id: reg.client_id, redirect_uri: REDIRECT })
  });
  check("code replay rejected", replay.status === 400);

  // wrong verifier rejected
  const grantForm2 = new URLSearchParams(grantForm);
  const login2 = await fetch(`${BASE}/authorize/grant`, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: grantForm2.toString(),
    redirect: "manual"
  });
  const code2 = new URL(login2.headers.get("location") ?? "", BASE).searchParams.get("code");
  const badPkce = await fetch(`${BASE}/token`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ grant_type: "authorization_code", code: code2, code_verifier: "wrong-verifier-aaaaaaaaaaaa", client_id: reg.client_id, redirect_uri: REDIRECT })
  });
  check("wrong PKCE verifier rejected", badPkce.status === 400);

  // authenticated tool call
  const mcpRes = await fetch(`${BASE}/mcp`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      accept: "application/json, text/event-stream",
      authorization: `Bearer ${tokens.access_token}`
    },
    body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "tools/call", params: { name: "search_knowledge", arguments: { query: "forever ad" } } })
  });
  const mcpBody = await jsonOrSse(mcpRes, 1);
  check("authenticated tools/call works", mcpRes.status === 200 && !!mcpBody?.result?.content);

  // license-code fallback binds a new email (second entitlement, as in real life)
  const grant2Res = await fetch(`${BASE}/entitlement`, {
    method: "POST",
    headers: { "content-type": "application/json", "x-ghl-secret": GHL_SECRET },
    body: JSON.stringify({ action: "grant", email: "net-new-buyer@smoke.test" })
  });
  const grant2 = await grant2Res.json();
  const fallbackForm = new URLSearchParams(formParams);
  fallbackForm.set("email", "chatgpt-user@smoke.test");
  fallbackForm.set("license_code", grant2.license_code);
  const fallbackRes = await fetch(`${BASE}/authorize/grant`, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: fallbackForm.toString(),
    redirect: "manual"
  });
  const fallbackLoc = fallbackRes.headers.get("location") ?? "";
  const code3 = new URL(fallbackLoc, BASE).searchParams.get("code");
  const t3 = await (await fetch(`${BASE}/token`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ grant_type: "authorization_code", code: code3, code_verifier: verifier, client_id: reg.client_id, redirect_uri: REDIRECT })
  })).json();
  const t3payload = JSON.parse(Buffer.from(t3.access_token.split(".")[1], "base64url").toString());
  check("license fallback binds email", t3payload.sub === "chatgpt-user@smoke.test");

  // refresh grant
  const refreshRes = await fetch(`${BASE}/token`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ grant_type: "refresh_token", refresh_token: tokens.refresh_token, client_id: reg.client_id })
  });
  const refreshed = await refreshRes.json();
  check("refresh grant", refreshRes.status === 200 && !!refreshed.access_token);

  // revoke -> old token now 403
  await fetch(`${BASE}/entitlement`, {
    method: "POST",
    headers: { "content-type": "application/json", "x-ghl-secret": GHL_SECRET },
    body: JSON.stringify({ action: "revoke", email: "buyer@smoke.test" })
  });
  const revokedRes = await fetch(`${BASE}/mcp`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      accept: "application/json, text/event-stream",
      authorization: `Bearer ${tokens.access_token}`
    },
    body: JSON.stringify({ jsonrpc: "2.0", id: 2, method: "tools/call", params: { name: "search_knowledge", arguments: { query: "forever ad" } } })
  });
  check("revoked license -> 403", revokedRes.status === 403);

  // challenge + health still open
  const challengeRes = await fetch(`${BASE}/.well-known/openai-apps-challenge`);
  check("challenge endpoint intact", (await challengeRes.text()) === "challenge-token");
} catch (error) {
  failures.push(`unexpected: ${error?.message ?? error}`);
  console.error(error);
} finally {
  child.kill();
}

console.log(`\n${passed} passed, ${failures.length} failed${failures.length ? `: ${failures.join("; ")}` : ""}`);
process.exit(failures.length ? 1 : 0);
