#!/usr/bin/env node
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import QRCode from 'qrcode';

export function localURL(value) {
  const url = new URL(value);
  if (url.protocol !== 'http:' || url.username || url.password || url.search || url.hash) throw new Error('Target must be a local HTTP URL without credentials, query or fragment');
  if (!['localhost', '127.0.0.1'].includes(url.hostname)) {
    let addresses;
    try { addresses = Object.values(os.networkInterfaces()).flat().filter(Boolean).map(x => x.address); }
    catch { throw new Error('Cannot verify a LAN address on this host; use a loopback local HTTP URL.'); }
    if (!addresses.includes(url.hostname)) throw new Error('Target must be a local HTTP URL without credentials, query or fragment');
  }
  return url;
}
export async function writeQR(value, output) {
  const url = localURL(value);
  const target = path.resolve(output);
  const bytes = await QRCode.toBuffer(url.href, { type: 'png', width: 512, margin: 4, errorCorrectionLevel: 'M' });
  await fs.writeFile(target, bytes, { flag: 'wx' });
  return { url: url.href, qr: target };
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    if (process.argv.length !== 4) throw new Error('Usage: qr.mjs LOCAL_HTTP_URL NEW_QR.png');
    console.log(JSON.stringify(await writeQR(process.argv[2], process.argv[3]), null, 2));
  } catch (error) { console.error(`device-it qr: ${error.message}`); process.exitCode = 1; }
}
