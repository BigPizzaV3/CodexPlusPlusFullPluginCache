#!/usr/bin/env node
import { open, readFile } from "node:fs/promises";
import { basename, extname } from "node:path";
import { pathToFileURL } from "node:url";

const MAX_BYTES = 20 * 1024 * 1024;
const MIME = { ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp", ".avif": "image/avif" };

export async function inspectLocalPhoto(filePath) {
  const mime_type = MIME[extname(filePath).toLowerCase()];
  if (!mime_type) throw new Error("Use JPEG, PNG, WebP or AVIF photographs.");
  const file = await open(filePath, "r");
  try {
    const stat = await file.stat();
    if (!stat.isFile() || stat.size < 1 || stat.size > MAX_BYTES) throw new Error("Choose a nonempty photograph up to 20 MB.");
    return { file_name: basename(filePath), mime_type, size_bytes: stat.size };
  } finally { await file.close(); }
}

export async function uploadLocalPhoto(filePath, ticket, fetcher = fetch) {
  const metadata = await inspectLocalPhoto(filePath);
  const url = new URL(ticket.upload_url);
  const trusted = url.origin === "https://photography-website-builder.mcp.newnoetic.com"
    || (url.protocol === "http:" && url.hostname === "127.0.0.1" && url.port === "8788");
  if (!trusted || url.username || url.password || url.search || url.hash || !/^\/device-upload\/[A-Za-z0-9_-]{40,}$/.test(url.pathname)) {
    throw new Error("The upload ticket does not target the photography server.");
  }
  if (!Number.isFinite(Date.parse(ticket.expires_at)) || Date.parse(ticket.expires_at) <= Date.now()) throw new Error("The upload ticket expired. Request a new one.");
  // Bound allocation before reading, and reject files changed since inspection.
  const file = await open(filePath, "r");
  let bytes;
  try {
    const stat = await file.stat();
    if (!stat.isFile() || stat.size !== metadata.size_bytes) throw new Error("The photograph changed. Request a new upload ticket.");
    bytes = Buffer.alloc(metadata.size_bytes);
    let offset = 0;
    while (offset < bytes.length) {
      const read = await file.read(bytes, offset, bytes.length - offset, offset);
      if (!read.bytesRead) throw new Error("The photograph changed during upload preparation.");
      offset += read.bytesRead;
    }
    if ((await file.stat()).size !== metadata.size_bytes) throw new Error("The photograph changed. Request a new upload ticket.");
  } finally { await file.close(); }
  let response;
  try {
    response = await fetcher(url, { method: "POST", redirect: "error", signal: AbortSignal.timeout(60_000),
      headers: { "content-type": metadata.mime_type, "content-length": String(metadata.size_bytes) }, body: bytes });
  } catch { throw new Error("The upload could not reach the photography server. The original local file is unchanged."); }
  if (!response.ok) throw new Error(`Photography upload failed (${response.status}). Inspect the saved site before retrying.`);
  const result = await response.json();
  if (!result.uploaded?.id) throw new Error("The server did not confirm a stored photograph.");
  return { uploaded: result.uploaded };
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    const [mode, filePath, ticketFile] = process.argv.slice(2);
    if (!filePath || !["inspect", "upload"].includes(mode)) throw new Error("Usage: upload-local.mjs inspect FILE | upload-local.mjs upload FILE [TICKET_JSON_FILE]");
    if (mode === "inspect") console.log(JSON.stringify(await inspectLocalPhoto(filePath)));
    else {
      let raw;
      if (ticketFile) raw = await readFile(ticketFile, "utf8");
      else {
        raw = "";
        for await (const chunk of process.stdin) {
          raw += chunk.toString();
          if (raw.length > 16_384) throw new Error("Upload ticket is too large.");
        }
      }
      const ticket = JSON.parse(raw);
      console.log(JSON.stringify(await uploadLocalPhoto(filePath, ticket)));
    }
  } catch (error) { console.error(error.message); process.exitCode = 1; }
}
