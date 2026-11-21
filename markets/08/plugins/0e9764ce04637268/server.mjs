import { createServer } from "node:http";
import { readFile, readdir, stat, mkdir } from "node:fs/promises";
import { join, extname, resolve, relative, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { createHash, createHmac, randomBytes, timingSafeEqual } from "node:crypto";
import { Readable } from "node:stream";
import Database from "better-sqlite3";
import { McpServer, SUPPORTED_PROTOCOL_VERSIONS, createMcpHandler } from "@modelcontextprotocol/server";
import { z } from "zod";

const ROOT = fileURLToPath(new URL(".", import.meta.url));
const PORT = Number(process.env.PORT ?? 8787);
const HOST = process.env.HOST ?? "127.0.0.1";
const KNOWLEDGE_DIR = resolve(ROOT, process.env.KNOWLEDGE_DIR ?? "./knowledge");
const DEFAULT_MAX_RESULTS = Number(process.env.MAX_RESULTS ?? 6);
const OPENAI_APPS_CHALLENGE = process.env.OPENAI_APPS_CHALLENGE ?? "Noy3_hf71A6M_nIotajciRpusTIZfQxyppI6R93usfs";

// Access layer config. ENFORCE_OAUTH=0 keeps the pre-GHL behavior (open /mcp);
// flip to 1 when GHL checkout + entitlements are live.
const PUBLIC_URL = (process.env.PUBLIC_URL ?? "https://mcp.mikeauton.com").replace(/\/+$/, "");
const ENFORCE_OAUTH = process.env.ENFORCE_OAUTH === "1";
const OAUTH_SECRET = process.env.OAUTH_SECRET ?? "";
const ENTITLEMENT_SECRET = process.env.ENTITLEMENT_SECRET ?? "";
const DB_PATH = resolve(ROOT, process.env.DB_PATH ?? "./data/ad-machine.db");

const ACCESS_TOKEN_TTL_S = 60 * 60 * 24 * 30;      // 30 days
const REFRESH_TOKEN_TTL_S = 60 * 60 * 24 * 365;    // 1 year
const AUTH_CODE_TTL_MS = 10 * 60 * 1000;

const ALLOWED_EXTENSIONS = new Set([".md", ".txt", ".json"]);
const MAX_FILE_BYTES = 2_000_000;

// ---------------------------------------------------------------------------
// Entitlement store (SQLite)
// ---------------------------------------------------------------------------

await mkdir(dirname(DB_PATH), { recursive: true });
const db = new Database(DB_PATH);
db.pragma("journal_mode = WAL");

db.exec(`
CREATE TABLE IF NOT EXISTS entitlements (
  id           INTEGER PRIMARY KEY,
  email        TEXT UNIQUE NOT NULL,
  license_code TEXT UNIQUE,
  status       TEXT NOT NULL DEFAULT 'active',
  created_at   TEXT NOT NULL,
  updated_at   TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS oauth_clients (
  client_id     TEXT PRIMARY KEY,
  client_name   TEXT,
  redirect_uris TEXT NOT NULL,
  created_at    TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS auth_codes (
  code         TEXT PRIMARY KEY,
  client_id    TEXT NOT NULL,
  redirect_uri TEXT NOT NULL,
  challenge    TEXT NOT NULL,
  method       TEXT NOT NULL,
  resource     TEXT,
  email        TEXT NOT NULL,
  expires_at   INTEGER NOT NULL,
  used         INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS refresh_tokens (
  token_hash TEXT PRIMARY KEY,
  email      TEXT NOT NULL,
  client_id  TEXT NOT NULL,
  expires_at INTEGER NOT NULL
);
`);

const insertEntitlement = db.prepare(
  "INSERT INTO entitlements (email, license_code, status, created_at, updated_at) VALUES (?, ?, 'active', ?, ?)"
);
const findEntitlementByEmail = db.prepare(
  "SELECT * FROM entitlements WHERE email = ?"
);
const findEntitlementByCode = db.prepare(
  "SELECT * FROM entitlements WHERE license_code = ?"
);
const setEntitlementEmail = db.prepare(
  "UPDATE entitlements SET email = ?, updated_at = ? WHERE id = ?"
);
const setEntitlementStatus = db.prepare(
  "UPDATE entitlements SET status = ?, updated_at = ? WHERE id = ?"
);
const insertClient = db.prepare(
  "INSERT INTO oauth_clients (client_id, client_name, redirect_uris, created_at) VALUES (?, ?, ?, ?)"
);
const findClient = db.prepare(
  "SELECT * FROM oauth_clients WHERE client_id = ?"
);
const insertAuthCode = db.prepare(
  "INSERT INTO auth_codes (code, client_id, redirect_uri, challenge, method, resource, email, expires_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
);
const findAuthCode = db.prepare("SELECT * FROM auth_codes WHERE code = ?");
const markCodeUsed = db.prepare("UPDATE auth_codes SET used = 1 WHERE code = ?");
const deleteRefreshByHash = db.prepare(
  "DELETE FROM refresh_tokens WHERE token_hash = ?"
);
const deleteRefreshByEmail = db.prepare(
  "DELETE FROM refresh_tokens WHERE email = ?"
);

const LICENSE_ALPHABET = "ABCDEFGHJKMNPQRSTUVWXYZ23456789";

function generateLicenseCode() {
  for (;;) {
    const bytes = randomBytes(8);
    let suffix = "";
    for (const byte of bytes) suffix += LICENSE_ALPHABET[byte % LICENSE_ALPHABET.length];
    const code = `AD-${suffix}`;
    if (!findEntitlementByCode.get(code)) return code;
  }
}

function nowISO() {
  return new Date().toISOString();
}

// ---------------------------------------------------------------------------
// Crypto helpers
// ---------------------------------------------------------------------------

function sha256b64url(value) {
  return createHash("sha256").update(value).digest("base64url");
}

function sha256hex(value) {
  return createHash("sha256").update(value).digest("hex");
}

function hmacSign(data, secret) {
  return createHmac("sha256", secret).update(data).digest("base64url");
}

function safeEqualStrings(a, b) {
  const ha = createHash("sha256").update(a).digest();
  const hb = createHash("sha256").update(b).digest();
  return timingSafeEqual(ha, hb);
}

function signJwt(payload) {
  const header = Buffer.from(JSON.stringify({ alg: "HS256", typ: "JWT" })).toString("base64url");
  const body = Buffer.from(JSON.stringify(payload)).toString("base64url");
  const signingInput = `${header}.${body}`;
  return `${signingInput}.${hmacSign(signingInput, OAUTH_SECRET)}`;
}

function verifyJwt(token) {
  if (!OAUTH_SECRET) return null;
  const parts = token.split(".");
  if (parts.length !== 3) return null;
  const [header, body, signature] = parts;
  const expected = hmacSign(`${header}.${body}`, OAUTH_SECRET);
  if (!safeEqualStrings(signature, expected)) return null;
  let payload;
  try {
    payload = JSON.parse(Buffer.from(body, "base64url").toString("utf8"));
  } catch {
    return null;
  }
  if (typeof payload.exp !== "number" || payload.exp * 1000 < Date.now()) return null;
  return payload;
}

// ---------------------------------------------------------------------------
// Knowledge base (unchanged from v1)
// ---------------------------------------------------------------------------

function tokenize(text) {
  return text
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, " ")
    .split(/\s+/)
    .filter(Boolean);
}

function unique(items) {
  return [...new Set(items)];
}

async function listKnowledgeFiles(dir = KNOWLEDGE_DIR) {
  const output = [];

  async function walk(current) {
    const entries = await readdir(current, { withFileTypes: true });
    for (const entry of entries) {
      const full = join(current, entry.name);
      if (entry.isDirectory()) {
        await walk(full);
      } else if (ALLOWED_EXTENSIONS.has(extname(entry.name).toLowerCase())) {
        output.push(full);
      }
    }
  }

  await walk(dir);
  return output.sort();
}

function cleanRelativePath(fullPath) {
  return relative(KNOWLEDGE_DIR, fullPath).replaceAll("\\", "/");
}

async function loadDocument(fullPath) {
  const info = await stat(fullPath);
  if (info.size > MAX_FILE_BYTES) {
    throw new Error(`Knowledge file is too large: ${cleanRelativePath(fullPath)}`);
  }
  const text = await readFile(fullPath, "utf8");
  return { path: cleanRelativePath(fullPath), text };
}

function splitIntoChunks(text, maxChars = 1800, overlap = 200) {
  const normalized = text.replace(/\r\n/g, "\n").trim();
  if (!normalized) return [];

  const paragraphs = normalized.split(/\n{2,}/);
  const chunks = [];
  let current = "";

  for (const paragraph of paragraphs) {
    const p = paragraph.trim();
    if (!p) continue;

    if ((current + "\n\n" + p).length <= maxChars) {
      current = current ? `${current}\n\n${p}` : p;
      continue;
    }

    if (current) chunks.push(current);

    if (p.length <= maxChars) {
      current = p;
    } else {
      let start = 0;
      while (start < p.length) {
        const end = Math.min(start + maxChars, p.length);
        chunks.push(p.slice(start, end));
        if (end >= p.length) {
          current = "";
          break;
        }
        start = Math.max(end - overlap, start + 1);
      }
    }
  }

  if (current) chunks.push(current);
  return chunks;
}

function scoreChunk(queryTokens, chunk) {
  const chunkTokens = tokenize(chunk);
  if (!chunkTokens.length) return 0;

  const counts = new Map();
  for (const token of chunkTokens) {
    counts.set(token, (counts.get(token) ?? 0) + 1);
  }

  let score = 0;
  for (const q of queryTokens) {
    const count = counts.get(q) ?? 0;
    if (count) score += 1 + Math.log2(1 + count);
  }

  return score;
}

async function searchKnowledge(query, maxResults) {
  const queryTokens = unique(tokenize(query)).filter((x) => x.length > 1);
  if (!queryTokens.length) return [];

  const files = await listKnowledgeFiles();
  const scored = [];

  for (const fullPath of files) {
    const { path, text } = await loadDocument(fullPath);
    for (const chunk of splitIntoChunks(text)) {
      const score = scoreChunk(queryTokens, chunk);
      if (score > 0) scored.push({ path, score, text: chunk });
    }
  }

  return scored
    .sort((a, b) => b.score - a.score)
    .slice(0, Math.min(maxResults, 10))
    .map((item, index) => ({
      rank: index + 1,
      source: item.path,
      relevance: Number(item.score.toFixed(2)),
      excerpt: item.text
    }));
}

// ---------------------------------------------------------------------------
// MCP server + tools (unchanged from v1)
// ---------------------------------------------------------------------------

const SERVER_INSTRUCTIONS = `
ROLE

You are The Ad Machine, a conversational ad-copy generator. You interview the user about their offer, then write a finished ad (headlines + first lines + body) in the "Forever Ad" format. The three copy structures (Event/Webinar, E-commerce, Lead Gen/Sales) live in this plugin's knowledge base under "Forever Ad Launcher - Ad Templates" — use search_knowledge to retrieve the matching template at generation time.

The user is likely not a copywriter or technical. They may give short, vague answers. Nudge for real detail, then do all the rewriting yourself — they should never have to "write well."

TONE

Warm, coach-like, not corporate. Short messages. One question at a time. Acknowledge good answers; gently push for more on thin ones.

FLOW

PROHIBITED OFFERS — CHECK FIRST, BEFORE ASKING ANYTHING: If the user's request is to advertise a prescription-only or age-restricted medicine (including weight-loss injections and GLP-1 products), adult or sexual content, gambling, weapons, tobacco or nicotine products, illegal goods, or any other category prohibited under OpenAI's usage policies, do not start the interview. Decline in one short, neutral message (e.g. "I can't write ads for that product — it falls into a category I'm not able to advertise.") and stop. Do not ask clarifying questions about the prohibited product, do not offer to reframe, soften, or write around it, and do not suggest adjacent offers for the same product line. If the user then brings a genuinely different, permitted offer, proceed normally from Q1.

Step 1: Ask Q1. Based on the answer, silently pick the matching template from the knowledge base (event/webinar, ecom, or lead gen/sales).

Step 2: Ask Q2-Q16 one at a time, in order, using the wording below. For thin/generic answers: (a) one warm nudge asking for a specific real example, (b) if still thin, one smaller targeted follow-up question, (c) if still stuck, offer a copyable prompt they can paste into any AI tool (ChatGPT, Claude, etc.) that restates their offer/audience and asks that AI to interview them for specifics. After that, always respect their choice to move on — be honest that more detail = a stronger ad, but never nag further.

Step 3: Once all 16 are answered, summarize in 4-6 bullets (offer, audience, top pain, top benefit, CTA) and confirm before generating.

Step 4: Search the knowledge base for the "Forever Ad Launcher - Ad Templates" document and generate using the matching template. Rewrite and sharpen everything — don't just insert raw answers. Output, in order:

1. 5 headline options, each a distinct angle (benefit, pain word, mechanism, objection-flip, identity line) — all <=65 characters including spaces/punctuation. Count each before showing; rewrite if over.
2. 5 first lines (FL1-FL5), each a different angle on the opening hook, with a short parenthetical note on its angle.
3. One shared body of ad copy used across all combos (don't rewrite per headline).
4. Clear section labels: headlines, first lines w/ rationale, "REST OF AD COPY — SAME FOR ALL VARIANTS," then body through to CTA/link.

Writing rules for the body:

- PACING: break escalating/tension beats (e.g. "tried X, helped for a while, then life took over") into short standalone lines, not one dense sentence.
- NO OVERPROMISE: the "what you'll learn" checklist describes what's taught/delivered — never a specific guaranteed personal outcome or behavior the user described as their own hoped-for result.
- AUDIENCE: name the specific audience once near the top to anchor, then use pronouns rather than repeating the label each sentence.
- NO REDUNDANCY WITH HEADLINES/FIRST LINES: the shared body is read alongside whichever headline and first line the user picks, so don't restate specific pain words, benefit words, or phrases already used in the 5 headlines or 5 first lines. Check the headlines and first lines you just wrote before finalizing the body, and cut anything that echoes them.
- TIGHTEN RUTHLESSLY: after drafting the body, do one more pass and cut any word, phrase, or example that isn't pulling real weight. Prefer the shorter version of a line if it loses no meaning. Err toward fewer, punchier lines over longer, fully-spelled-out ones.

After the ad, offer one round of revision or to lock in a headline/first-line pairing.

QUESTION SET (ask one at a time, in order)

Q1: What are you advertising — event/webinar, physical/e-commerce product, or service/lead gen offer?
Q2: What's the exact name of the thing you're selling?
Q3: What category does it belong to — how would your buyer describe it to a friend, in their words, not your jargon?
Q4: What's the big-picture life-change outcome your buyer is really after, not just the feature? Take your time.
Q5: Who is your ideal buyer specifically (job title/life stage/identity)? If multiple, pick ONE.
Q6: What does this buyer already know or do reasonably well related to this problem? List everything, even small stuff.
Q7: What have they already tried that didn't fully work? List as many specifics as possible (products, DIY, providers, books). Example of specific vs vague: not "tried to relax" but "tried meditation — calmed them for a few minutes, then they reacted the same way as always once back in the real world."
Q8: List 2-4 concrete, tangible benefits — things seen/felt/measured, described in how they show up in real life, not just labels.
Q9: Beyond the tangible stuff, what's the deeper emotional/identity outcome? How does daily life, confidence, or relationships change?
Q10: What makes your approach different from everything else they've tried — a specific method, tech, philosophy you can name? Geek out.
Q11: What's still frustrating/unresolved for them right now, vividly, day to day?
Q12: What specific words would they use to describe this problem — what they'd type into Google at 11pm frustrated?
Q13: Is there a deeper layer of pain — how this hits them emotionally, socially, or in identity, beyond the practical issue?
Q14: What's the #1 reason someone hesitates to buy even if they want the result (cost, past letdowns, skepticism, fear)? Explain in detail.
Q15: What do you want them to do right now — be exact (book a call, claim a ticket, shop now, etc.)?
Q16: What's the link or next step? Paste the URL if you have it.

RULES

- Never show the raw template/brackets — only finished, natural copy.
- Never skip a question or ask more than one at once.
- Cap thin-answer handling at: one nudge, one follow-up, one AI-prompt offer — then follow the user's lead.
- Never invent facts/claims/numbers the user didn't give you; write around gaps instead of fabricating.
- Always deliver the full fixed output: 5 headlines, 5 labeled first lines, one shared body.
- Apply the headline length, pacing, no-overpromise, audience-anchoring, no-redundancy, and tightening rules to every ad.
- Always offer one round of revision at the end.
`.trim();

function createAdMachineServer() {
  const server = new McpServer(
    {
      name: "the-ad-machine",
      version: "1.1.1"
    },
    {
      instructions: SERVER_INSTRUCTIONS,
      // v2 installs tools/list + tools/call handlers only when the capability
      // is declared (no more implicit registration on first registerTool).
      capabilities: { tools: {} },
      // 2026-07-28 enables server/discover (the portal scanner's handshake).
      supportedProtocolVersions: [...SUPPORTED_PROTOCOL_VERSIONS, "2026-07-28"]
    }
  );

  server.registerTool(
    "search_knowledge",
    {
      title: "Search ad knowledge",
      description:
        "Search the ad-machine knowledge base, primarily the 'Forever Ad Launcher - Ad Templates' document holding the three Forever Ad copy structures (Event/Webinar, E-commerce, Lead Gen/Sales). Call this in Step 4 before generating an ad to load the matching template.",
      inputSchema: {
        query: z.string().min(2).describe("The user's question or the key information to find."),
        max_results: z.number().int().min(1).max(10).optional().describe("Maximum number of relevant passages to return.")
      },
      annotations: {
        readOnlyHint: true,
        destructiveHint: false,
        openWorldHint: false
      }
    },
    async ({ query, max_results }) => {
      try {
        const results = await searchKnowledge(query, max_results ?? DEFAULT_MAX_RESULTS);

        if (!results.length) {
          return {
            content: [{
              type: "text",
              text: "No relevant knowledge-base passages were found for this query."
            }],
            structuredContent: { results: [] }
          };
        }

        const text = results.map(
          (r) => `[${r.rank}] ${r.source}\n${r.excerpt}`
        ).join("\n\n---\n\n");

        return {
          content: [{
            type: "text",
            text
          }],
          structuredContent: { results }
        };
      } catch (error) {
        console.error("search_knowledge error:", error);
        return {
          isError: true,
          content: [{
            type: "text",
            text: "The knowledge base could not be searched."
          }]
        };
      }
    }
  );

  server.registerTool(
    "read_knowledge_document",
    {
      title: "Read ad knowledge document",
      description:
        "Read the full 'Forever Ad Launcher - Ad Templates' document (or another knowledge-base document) when search results need closer inspection before generating an ad.",
      inputSchema: {
        path: z.string().min(1).describe("Relative knowledge-base path returned by search_knowledge.")
      },
      annotations: {
        readOnlyHint: true,
        destructiveHint: false,
        openWorldHint: false
      }
    },
    async ({ path }) => {
      try {
        const candidate = resolve(KNOWLEDGE_DIR, path);
        const rel = relative(KNOWLEDGE_DIR, candidate);

        if (!rel || rel.startsWith("..") || rel.includes("..")) {
          return {
            isError: true,
            content: [{ type: "text", text: "Invalid knowledge document path." }]
          };
        }

        const { path: safePath, text } = await loadDocument(candidate);

        return {
          content: [{
            type: "text",
            text: `Source: ${safePath}\n\n${text}`
          }],
          structuredContent: {
            source: safePath,
            text
          }
        };
      } catch (error) {
        console.error("read_knowledge_document error:", error);
        return {
          isError: true,
          content: [{
            type: "text",
            text: "The requested knowledge document could not be read."
          }]
        };
      }
    }
  );

  return server;
}

// One fetch-style handler serving both wire eras: 2025-era traffic statelessly
// (each request gets a fresh server instance) plus native 2026-07-28 support.
const mcpHandler = createMcpHandler(
  () => createAdMachineServer(),
  { legacy: "stateless" }
);

// ---------------------------------------------------------------------------
// HTML helpers
// ---------------------------------------------------------------------------

function esc(value) {
  return String(value)
    .replaceAll("&", "&" + "amp;")
    .replaceAll("<", "&" + "lt;")
    .replaceAll(">", "&" + "gt;")
    .replaceAll('"', "&" + "quot;")
    .replaceAll("'", "&" + "#39;");
}

const PAGE_STYLE = `
  * { box-sizing: border-box; }
  body { margin: 0; min-height: 100vh; display: flex; align-items: center; justify-content: center;
         font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
         background: #111; color: #fafafa; }
  .card { background: #1c1c1c; border: 1px solid #2c2c2c; border-radius: 16px;
          padding: 40px 36px; width: 100%; max-width: 380px; }
  h1 { font-size: 22px; margin: 0 0 6px; }
  p.sub { margin: 0 0 24px; color: #a8a8a8; font-size: 14px; line-height: 1.5; }
  label { display: block; font-size: 13px; color: #a8a8a8; margin: 14px 0 6px; }
  input { width: 100%; padding: 11px 12px; border-radius: 8px; border: 1px solid #3a3a3a;
          background: #111; color: #fafafa; font-size: 15px; }
  button { width: 100%; margin-top: 22px; padding: 12px; border: 0; border-radius: 8px;
           background: #ffb020; color: #111; font-size: 15px; font-weight: 600; cursor: pointer; }
  .error { background: #3d1d1d; border: 1px solid #7c2d2d; color: #ffb4b4;
           padding: 10px 12px; border-radius: 8px; font-size: 13px; margin-bottom: 8px; }
  .foot { margin-top: 24px; font-size: 12px; color: #6f6f6f; line-height: 1.5; }
  .foot a { color: #ffb020; text-decoration: none; }
`;

function errorPage(title, message) {
  return `<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)}</title><style>${PAGE_STYLE}</style></head>
<body><div class="card"><h1>${esc(title)}</h1><p class="sub">${esc(message)}</p>
<div class="foot">Need access? Get it at <a href="https://ads.mikeauton.com/simple">ads.mikeauton.com/simple</a></div></div></body></html>`;
}

function authorizePage(params, errorMessage) {
  const hidden = Object.entries({
    response_type: params.response_type,
    client_id: params.client_id,
    redirect_uri: params.redirect_uri,
    code_challenge: params.code_challenge,
    code_challenge_method: params.code_challenge_method,
    state: params.state,
    resource: params.resource
  })
    .filter(([, value]) => value !== null && value !== undefined)
    .map(([key, value]) => `<input type="hidden" name="${key}" value="${esc(value)}">`)
    .join("\n");

  return `<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Ad Machine — Sign in</title><style>${PAGE_STYLE}</style></head>
<body>
<form class="card" method="POST" action="/authorize/grant">
  <h1>The Ad Machine</h1>
  <p class="sub">Sign in with the email you used at checkout. If you used a different one, enter your license code from the receipt email instead.</p>
  ${errorMessage ? `<div class="error">${esc(errorMessage)}</div>` : ""}
  ${hidden}
  <label for="email">Email used at checkout</label>
  <input id="email" name="email" type="email" required autocomplete="email">
  <label for="license_code">License code (only if different email)</label>
  <input id="license_code" name="license_code" type="text" placeholder="AD-XXXXXXXX" autocomplete="off">
  <button type="submit">Connect my license</button>
  <div class="foot">One-time purchase at <a href="https://ads.mikeauton.com/simple">ads.mikeauton.com/simple</a>. Questions: eugene@mikeauton.com</div>
</form>
</body></html>`;
}

// ---------------------------------------------------------------------------
// Body parsing + responses
// ---------------------------------------------------------------------------

function readBody(req, limit = 100_000) {
  return new Promise((resolveBody, rejectBody) => {
    const chunks = [];
    let size = 0;
    req.on("data", (chunk) => {
      size += chunk.length;
      if (size > limit) {
        rejectBody(new Error("Body too large"));
        req.destroy();
        return;
      }
      chunks.push(chunk);
    });
    req.on("end", () => resolveBody(Buffer.concat(chunks)));
    req.on("error", rejectBody);
  });
}

async function readBodyObject(req) {
  const buffer = await readBody(req);
  const type = String(req.headers["content-type"] ?? "");
  if (!buffer.length) return {};
  if (type.includes("application/json")) return JSON.parse(buffer.toString("utf8"));
  if (type.includes("application/x-www-form-urlencoded")) {
    return Object.fromEntries(new URLSearchParams(buffer.toString("utf8")));
  }
  try {
    return JSON.parse(buffer.toString("utf8"));
  } catch {
    return Object.fromEntries(new URLSearchParams(buffer.toString("utf8")));
  }
}

// Raw bytes for the MCP endpoint: the OAuth gate inspects the parsed JSON,
// but the full buffer is what gets handed to the MCP handler as the request
// body (the handler does its own era classification and parsing).
function readBodyBuffer(req, limit = 4194304) {
  return readBody(req, limit);
}
function sendJSON(res, status, payload, extraHeaders = {}) {
  const body = JSON.stringify(payload);
  res.writeHead(status, {
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store",
    ...extraHeaders
  });
  res.end(body);
}

function sendHTML(res, status, html) {
  res.writeHead(status, { "content-type": "text/html; charset=utf-8" });
  res.end(html);
}

// ---------------------------------------------------------------------------
// OAuth: authorization server endpoints
// ---------------------------------------------------------------------------

const PROTECTED_RESOURCE_DOC = () => ({
  resource: `${PUBLIC_URL}/`,
  authorization_servers: [PUBLIC_URL],
  scopes_supported: ["mcp"],
  bearer_methods_supported: ["header"],
  resource_documentation: "https://ads.mikeauton.com/simple"
});

const AUTH_SERVER_DOC = () => ({
  issuer: PUBLIC_URL,
  authorization_endpoint: `${PUBLIC_URL}/authorize`,
  token_endpoint: `${PUBLIC_URL}/token`,
  registration_endpoint: `${PUBLIC_URL}/register`,
  response_types_supported: ["code"],
  grant_types_supported: ["authorization_code", "refresh_token"],
  code_challenge_methods_supported: ["S256", "plain"],
  token_endpoint_auth_methods_supported: ["none"],
  scopes_supported: ["mcp"],
  service_documentation: "https://ads.mikeauton.com/support"
});

function validRedirectUri(uri) {
  try {
    const url = new URL(uri);
    if (url.protocol === "https:") return true;
    return url.protocol === "http:" && ["127.0.0.1", "localhost"].includes(url.hostname);
  } catch {
    return false;
  }
}

async function handleRegister(req, res) {
  try {
    const body = await readBodyObject(req);
    const redirectUris = Array.isArray(body.redirect_uris) ? body.redirect_uris : null;
    if (!redirectUris || !redirectUris.length || !redirectUris.every(validRedirectUri)) {
      sendJSON(res, 400, { error: "invalid_client_metadata", error_description: "redirect_uris must be HTTPS URLs." });
      return;
    }
    const clientId = `adm_${randomBytes(12).toString("base64url")}`;
    insertClient.run(
      clientId,
      typeof body.client_name === "string" ? body.client_name.slice(0, 200) : "",
      JSON.stringify(redirectUris),
      nowISO()
    );
    sendJSON(res, 201, {
      client_id: clientId,
      client_id_issued_at: Math.floor(Date.now() / 1000),
      client_name: body.client_name ?? "",
      redirect_uris: redirectUris,
      grant_types: ["authorization_code", "refresh_token"],
      response_types: ["code"],
      token_endpoint_auth_method: "none"
    });
  } catch {
    sendJSON(res, 400, { error: "invalid_client_metadata" });
  }
}

async function handleAuthorize(req, res, url) {
  const params = {
    response_type: url.searchParams.get("response_type"),
    client_id: url.searchParams.get("client_id"),
    redirect_uri: url.searchParams.get("redirect_uri"),
    code_challenge: url.searchParams.get("code_challenge"),
    code_challenge_method: url.searchParams.get("code_challenge_method") ?? "S256",
    state: url.searchParams.get("state"),
    resource: url.searchParams.get("resource")
  };

  const fail = (message) => sendHTML(res, 400, errorPage("Sign-in error", message));

  if (params.response_type !== "code") return fail("This request is missing required OAuth parameters. Please reconnect from ChatGPT.");
  const client = params.client_id ? findClient.get(params.client_id) : null;
  if (!client) return fail("Unknown app. Please reconnect from ChatGPT.");
  let registered;
  try {
    registered = JSON.parse(client.redirect_uris);
  } catch {
    registered = [];
  }
  if (!params.redirect_uri || !registered.includes(params.redirect_uri)) {
    return fail("Unregistered redirect address. Please reconnect from ChatGPT.");
  }
  if (!params.code_challenge) return fail("Missing code challenge (PKCE). Please reconnect from ChatGPT.");
  if (!["S256", "plain"].includes(params.code_challenge_method)) {
    return fail("Unsupported code challenge method. Please reconnect from ChatGPT.");
  }
  if (params.code_challenge.length < 16 || !/^[A-Za-z0-9\-._~]+$/.test(params.code_challenge)) {
    return fail("Malformed code challenge. Please reconnect from ChatGPT.");
  }

  sendHTML(res, 200, authorizePage(params));
}

async function handleAuthorizeGrant(req, res) {
  const body = await readBodyObject(req);
  const params = {
    response_type: body.response_type,
    client_id: body.client_id,
    redirect_uri: body.redirect_uri,
    code_challenge: body.code_challenge,
    code_challenge_method: body.code_challenge_method ?? "S256",
    state: body.state,
    resource: body.resource
  };

  const failPage = (message, status = 400) =>
    sendHTML(res, status, authorizePage(params, message));

  const client = params.client_id ? findClient.get(params.client_id) : null;
  let registered = [];
  try {
    registered = client ? JSON.parse(client.redirect_uris) : [];
  } catch { /* fallthrough to generic fail */ }
  if (!client || !registered.includes(params.redirect_uri)) {
    return sendHTML(res, 400, errorPage("Sign-in error", "Unknown app. Please reconnect from ChatGPT."));
  }

  const email = typeof body.email === "string" ? body.email.trim().toLowerCase() : "";
  const licenseCode = typeof body.license_code === "string" ? body.license_code.trim().toUpperCase() : "";

  let entitlement = email ? findEntitlementByEmail.get(email) : null;

  if (!entitlement && licenseCode) {
    entitlement = findEntitlementByCode.get(licenseCode);
  }
  if (entitlement && entitlement.status !== "active") {
    return failPage("Your license is no longer active. Need help? eugene@mikeauton.com", 403);
  }
  if (!entitlement) {
    return failPage(
      'No active license found for those details. Double-check the checkout email (or enter your license code from the receipt). If you haven\'t bought it yet, get it at ads.mikeauton.com/simple.',
      401
    );
  }

  // License-code fallback: bind the buyer's chosen email to this entitlement.
  if (email && entitlement.email !== email) {
    const alreadyBound = findEntitlementByEmail.get(email);
    if (alreadyBound && alreadyBound.id !== entitlement.id) {
      return failPage("That email is already linked to a different license.", 409);
    }
    try {
      setEntitlementEmail.run(email, nowISO(), entitlement.id);
      entitlement = findEntitlementByEmail.get(email);
    } catch {
      return failPage("Could not link that email. Contact eugene@mikeauton.com.", 500);
    }
  }

  const code = randomBytes(32).toString("base64url");
  insertAuthCode.run(
    code,
    params.client_id,
    params.redirect_uri,
    params.code_challenge,
    params.code_challenge_method,
    params.resource,
    entitlement.email,
    Date.now() + AUTH_CODE_TTL_MS
  );

  const target = new URL(params.redirect_uri);
  target.searchParams.set("code", code);
  if (params.state) target.searchParams.set("state", params.state);
  target.searchParams.set("iss", PUBLIC_URL);

  res.writeHead(302, { location: target.toString(), "cache-control": "no-store" });
  res.end();
}

async function handleToken(req, res) {
  let body;
  try {
    body = await readBodyObject(req);
  } catch {
    return sendJSON(res, 400, { error: "invalid_request" });
  }

  if (body.grant_type === "refresh_token") {
    const hash = sha256b64url(String(body.refresh_token ?? ""));
    const stored = db.prepare("SELECT * FROM refresh_tokens WHERE token_hash = ?").get(hash);
    if (!stored || stored.expires_at < Date.now()) {
      return sendJSON(res, 400, { error: "invalid_grant", error_description: "Refresh token is invalid or expired." });
    }
    const entitlement = findEntitlementByEmail.get(stored.email);
    if (!entitlement || entitlement.status !== "active") {
      deleteRefreshByHash.run(hash);
      return sendJSON(res, 403, { error: "access_denied", error_description: "License is no longer active." });
    }
    deleteRefreshByHash.run(hash);
    const issued = issueTokens(stored.email, stored.client_id);
    return sendJSON(res, 200, issued);
  }

  if (body.grant_type !== "authorization_code") {
    return sendJSON(res, 400, { error: "unsupported_grant_type" });
  }

  const row = body.code ? findAuthCode.get(String(body.code)) : null;
  if (!row) return sendJSON(res, 400, { error: "invalid_grant", error_description: "Unknown code." });
  if (row.used) {
    return sendJSON(res, 400, { error: "invalid_grant", error_description: "Code already used." });
  }
  if (row.expires_at < Date.now()) {
    return sendJSON(res, 400, { error: "invalid_grant", error_description: "Code expired." });
  }
  if (!body.client_id || body.client_id !== row.client_id) {
    return sendJSON(res, 400, { error: "invalid_grant", error_description: "Client mismatch." });
  }
  if (!body.redirect_uri || body.redirect_uri !== row.redirect_uri) {
    return sendJSON(res, 400, { error: "invalid_grant", error_description: "Redirect mismatch." });
  }

  const verifier = String(body.code_verifier ?? "");
  if (!verifier) return sendJSON(res, 400, { error: "invalid_grant", error_description: "Missing code_verifier." });
  const expected = row.method === "S256" ? sha256b64url(verifier) : verifier;
  if (!safeEqualStrings(expected, row.challenge)) {
    return sendJSON(res, 400, { error: "invalid_grant", error_description: "PKCE verification failed." });
  }

  markCodeUsed.run(row.code);
  sendJSON(res, 200, issueTokens(row.email, row.client_id, row.resource));
}

function issueTokens(email, clientId, resource) {
  const now = Math.floor(Date.now() / 1000);
  const accessToken = signJwt({
    iss: PUBLIC_URL,
    sub: email,
    aud: resource || "mcp",
    client_id: clientId,
    jti: randomBytes(8).toString("base64url"),
    iat: now,
    exp: now + ACCESS_TOKEN_TTL_S
  });
  const refreshToken = randomBytes(48).toString("base64url");
  db.prepare(
    "INSERT INTO refresh_tokens (token_hash, email, client_id, expires_at) VALUES (?, ?, ?, ?)"
  ).run(sha256b64url(refreshToken), email, clientId, Date.now() + REFRESH_TOKEN_TTL_S * 1000);

  return {
    access_token: accessToken,
    token_type: "Bearer",
    expires_in: ACCESS_TOKEN_TTL_S,
    refresh_token: refreshToken,
    scope: "mcp"
  };
}

// ---------------------------------------------------------------------------
// Entitlement webhook (GHL -> VPS)
// ---------------------------------------------------------------------------

async function handleEntitlement(req, res) {
  const provided = String(req.headers["x-ghl-secret"] ?? "");
  if (!ENTITLEMENT_SECRET || !provided || !safeEqualStrings(provided, ENTITLEMENT_SECRET)) {
    return sendJSON(res, 401, { ok: false, error: "unauthorized" });
  }

  let body;
  try {
    body = await readBodyObject(req);
  } catch {
    return sendJSON(res, 400, { ok: false, error: "invalid_body" });
  }

  const action = String(body.action ?? "").toLowerCase();
  const email = typeof body.email === "string" ? body.email.trim().toLowerCase() : "";

  if (!["grant", "revoke"].includes(action)) {
    return sendJSON(res, 400, { ok: false, error: "unknown_action" });
  }
  if (!email || !email.includes("@")) {
    return sendJSON(res, 400, { ok: false, error: "invalid_email" });
  }

  const licenseCode =
    typeof body.license_code === "string" && body.license_code.trim()
      ? body.license_code.trim().toUpperCase()
      : null;

  if (action === "grant") {
    let entitlement = findEntitlementByEmail.get(email);
    if (entitlement) {
      setEntitlementStatus.run("active", nowISO(), entitlement.id);
    } else {
      for (let attempt = 0; attempt < 5; attempt++) {
        try {
          insertEntitlement.run(email, licenseCode ?? generateLicenseCode(), nowISO(), nowISO());
          break;
        } catch (error) {
          if (!(error && String(error.message).includes("UNIQUE"))) throw error;
          // email/license collision — retry with a fresh generated license
        }
      }
      entitlement = findEntitlementByEmail.get(email);
    }
    return sendJSON(res, 200, {
      ok: true,
      email,
      status: "active",
      license_code: entitlement ? entitlement.license_code : null
    });
  }

  // revoke
  const entitlement = findEntitlementByEmail.get(email);
  if (entitlement) {
    setEntitlementStatus.run("revoked", nowISO(), entitlement.id);
    deleteRefreshByEmail.run(email);
    return sendJSON(res, 200, { ok: true, email, status: "revoked" });
  }
  return sendJSON(res, 200, { ok: true, email, status: "unknown" });
}

// ---------------------------------------------------------------------------
// Auth gate for /mcp
// ---------------------------------------------------------------------------

function denyUnauthorized(res) {
  sendJSON(
    res,
    401,
    { error: "unauthorized", errorhint: "Sign in with your purchase email or license code." },
    {
      "WWW-Authenticate": `Bearer realm="the-ad-machine", resource_metadata="${PUBLIC_URL}/.well-known/oauth-protected-resource"`
    }
  );
}

// Connection-level check: identity + active license. Returns JWT payload or null (response already sent).
function checkBearer(req, res) {
  const header = req.headers.authorization ?? "";
  if (!header.startsWith("Bearer ")) {
    denyUnauthorized(res);
    return null;
  }
  const payload = verifyJwt(header.slice(7).trim());
  if (!payload || !payload.sub) {
    denyUnauthorized(res);
    return null;
  }
  const entitlement = findEntitlementByEmail.get(payload.sub);
  if (!entitlement || entitlement.status !== "active") {
    sendJSON(res, 403, {
      error: "license_inactive",
      error_description: "No active license for this account. Get access at https://ads.mikeauton.com/simple"
    });
    return null;
  }
  return payload;
}

// Metadata reads stay open so the portal's automated scan works without a stored
// OAuth authorization; the paid value (tool execution) always requires a license.
const PUBLIC_MCP_METHODS = new Set(["initialize", "tools/list", "ping", "server/discover"]);

// ---------------------------------------------------------------------------
// HTTP server + routing
// ---------------------------------------------------------------------------

const httpServer = createServer(async (req, res) => {
  let url;
  try {
    if (!req.url) throw new Error("missing url");
    url = new URL(req.url, `http://${req.headers.host ?? "localhost"}`);
  } catch {
    res.writeHead(400).end("Bad Request");
    return;
  }
  const path = url.pathname;

  // TEMP-DIAG: portal-scan diagnostics (paths + IPs only). Remove after scan resolves.
  if (path === "/mcp" || path === "/register" || path.startsWith("/authorize") || path === "/token" || path === "/entitlement") {
    console.error(`[MCP-DBG] ${req.method} ${path} ip=${req.socket.remoteAddress}`);
  }

  if (req.method === "OPTIONS" && path === "/mcp") {
    res.writeHead(204, {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, GET, DELETE, OPTIONS",
      "Access-Control-Allow-Headers": "content-type, mcp-session-id, authorization",
      "Access-Control-Expose-Headers": "Mcp-Session-Id"
    });
    res.end();
    return;
  }

  if (req.method === "GET" && path === "/") {
    res.writeHead(200, { "content-type": "text/plain; charset=utf-8" });
    res.end("The Ad Machine MCP server");
    return;
  }

  if (req.method === "GET" && path === "/health") {
    sendJSON(res, 200, { ok: true });
    return;
  }

  if (req.method === "GET" && path === "/.well-known/openai-apps-challenge") {
    res.writeHead(200, { "content-type": "text/plain; charset=utf-8" });
    res.end(OPENAI_APPS_CHALLENGE);
    return;
  }

  // Access discovery
  if (req.method === "GET" && path === "/.well-known/oauth-protected-resource") {
    sendJSON(res, 200, PROTECTED_RESOURCE_DOC());
    return;
  }
  if (req.method === "GET" && path === "/.well-known/oauth-authorization-server") {
    sendJSON(res, 200, AUTH_SERVER_DOC());
    return;
  }

  // OAuth flows
  if (req.method === "POST" && path === "/register") {
    await handleRegister(req, res);
    return;
  }
  if (req.method === "GET" && path === "/authorize") {
    await handleAuthorize(req, res, url);
    return;
  }
  if (req.method === "POST" && path === "/authorize/grant") {
    await handleAuthorizeGrant(req, res);
    return;
  }
  if (req.method === "POST" && path === "/token") {
    await handleToken(req, res);
    return;
  }

  // Entitlement webhook
  if (req.method === "POST" && path === "/entitlement") {
    await handleEntitlement(req, res);
    return;
  }

  // MCP endpoint. With ENFORCE_OAUTH=1: metadata methods open (portal scan),
  // tool execution requires an active license.
  if (path === "/mcp" && ["POST", "GET", "DELETE"].includes(req.method ?? "")) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Expose-Headers", "Mcp-Session-Id");

    let raw;
    if (req.method === "POST") {
      try {
        raw = await readBodyBuffer(req);
      } catch {
        res.writeHead(400).end("Invalid request body");
        return;
      }
      if (ENFORCE_OAUTH) {
        let parsed = null;
        try {
          parsed = raw.length ? JSON.parse(raw.toString("utf8")) : null;
        } catch {
          // Not JSON — the MCP handler rejects it on its own.
        }
        const methods = (Array.isArray(parsed) ? parsed : [parsed])
          .map((m) => String(m?.method ?? ""));
        const needsAuth = methods.some(
          (m) => m && !m.startsWith("notifications/") && !PUBLIC_MCP_METHODS.has(m)
        );
        if (needsAuth && checkBearer(req, res) === null) {
          return;
        }
      }
    }

    // Hand the exchange to the fetch-style handler (serves 2025-era and
    // 2026-07-28 traffic); pipe its web Response back over Node's res.
    const abort = new AbortController();
    res.on("close", () => abort.abort());

    const target = new URL(
      `http://${req.headers.host ?? "localhost"}${req.url ?? "/mcp"}`
    );
    const headers = {};
    for (const [key, value] of Object.entries(req.headers)) {
      if (["connection", "transfer-encoding", "keep-alive", "content-length", "expect"].includes(key)) continue;
      headers[key] = Array.isArray(value) ? value.join(", ") : value;
    }

    let response;
    try {
      response = await mcpHandler.fetch(new Request(target, {
        method: req.method,
        headers,
        ...(req.method === "POST" && raw.length ? { body: raw } : {}),
        signal: abort.signal
      }));
    } catch (error) {
      console.error("MCP request error:", error);
      if (!res.headersSent) {
        res.writeHead(500).end("Internal server error");
      }
      return;
    }

    const outHeaders = {};
    response.headers.forEach((value, key) => { outHeaders[key] = value; });
    res.writeHead(response.status, outHeaders);
    if (response.body) {
      Readable.fromWeb(response.body).pipe(res);
    } else {
      res.end();
    }
    return;
  }

  res.writeHead(404).end("Not Found");
});

httpServer.listen(PORT, HOST, () => {
  console.log(`The Ad Machine MCP server listening on http://${HOST}:${PORT}/mcp (OAuth ${ENFORCE_OAUTH ? "ENFORCED" : "open"})`);
});
