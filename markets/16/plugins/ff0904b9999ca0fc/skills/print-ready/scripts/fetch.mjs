// Download a 3D model from an https link, for example a GLB a 3D generation tool returned.
//
// The link comes from a conversation, so it is treated as untrusted. Only public https
// addresses on port 443 are fetched: every address a name resolves to is checked, the
// checked address is the one actually connected to (so a name cannot resolve one way when
// checked and another when used), redirects are followed by hand and checked the same way,
// nothing is sent but the request itself, and the download is capped in size and time.
import fs from 'node:fs';
import path from 'node:path';
import https from 'node:https';
import dns from 'node:dns';
import net from 'node:net';
import crypto from 'node:crypto';

export const LIMITS = { bytes: 200 * 1024 * 1024, redirects: 3, connectMs: 10_000, totalMs: 180_000 };

// Addresses that are not the public internet: this machine, the local network, carrier
// NAT, cloud metadata, documentation and reserved ranges, multicast, and IPv6 forms that
// carry or translate an IPv4 address.
// Two lists: Node's BlockList matches IPv4 addresses against IPv4-mapped IPv6 rules, so one
// list holding both would treat every IPv4 address as blocked.
const blocked4 = new net.BlockList();
const blocked6 = new net.BlockList();
for (const [address, prefix] of [
  ['0.0.0.0', 8], ['10.0.0.0', 8], ['100.64.0.0', 10], ['127.0.0.0', 8], ['169.254.0.0', 16], ['172.16.0.0', 12],
  ['192.0.0.0', 24], ['192.0.2.0', 24], ['192.88.99.0', 24], ['192.168.0.0', 16], ['198.18.0.0', 15],
  ['198.51.100.0', 24], ['203.0.113.0', 24], ['224.0.0.0', 4], ['240.0.0.0', 4],
]) blocked4.addSubnet(address, prefix, 'ipv4');
for (const [address, prefix] of [
  ['::', 128], ['::1', 128], ['::ffff:0:0', 96], ['64:ff9b::', 96], ['64:ff9b:1::', 48], ['100::', 64],
  ['2001::', 32], ['2001:db8::', 32], ['2002::', 16], ['fc00::', 7], ['fe80::', 10], ['fec0::', 10], ['ff00::', 8],
]) blocked6.addSubnet(address, prefix, 'ipv6');

/** Is this an address on the public internet? */
export function isPublic(address) {
  const bare = String(address).replace(/^\[|\]$/g, '');
  const family = net.isIP(bare);
  if (family === 4) return !blocked4.check(bare, 'ipv4');
  if (family !== 6) return false;
  // An IPv6 address written with an IPv4 tail (::ffff:10.0.0.1, ::10.0.0.1) is judged by that IPv4 address too.
  const tail = bare.match(/(\d+\.\d+\.\d+\.\d+)$/);
  if (tail && !isPublic(tail[1])) return false;
  return !blocked6.check(bare, 'ipv6');
}

/** A link as shown in messages and reports: without its query or fragment, which can carry access tokens. */
export function shortLink(link) {
  try { const url = new URL(link); return `${url.origin}${url.pathname}`; } catch { return String(link).split(/[?#]/)[0]; }
}

/** Check a link before fetching it. Returns the parsed URL or throws with the reason. */
export function checkLink(link) {
  let url;
  try { url = new URL(link); } catch { throw new Error('This is not a link.'); }
  if (url.protocol !== 'https:') throw new Error('Only https links are fetched.');
  if (url.username || url.password) throw new Error('Links with a user name or password are not fetched.');
  if (url.port && url.port !== '443') throw new Error('Only the standard https port is used.');
  // A host written as an address (including forms the URL parser normalizes, such as a
  // single number) is connected to without any name lookup, so it is checked here.
  const host = url.hostname.replace(/^\[|\]$/g, '');
  if (net.isIP(host) && !isPublic(host)) throw new Error(`${host} is not on the public internet.`);
  return url;
}

/**
 * A DNS lookup for the request that refuses the host unless every address it has is
 * public, and then connects to one of those checked addresses.
 */
export function guardedLookup(resolve = dns.lookup) {
  return (hostname, options, callback) => {
    resolve(hostname, { all: true, verbatim: true }, (error, addresses) => {
      if (error) return callback(error);
      if (!addresses.length) return callback(new Error(`No address for ${hostname}`));
      const bad = addresses.find(entry => !isPublic(entry.address));
      if (bad) return callback(Object.assign(new Error(`${hostname} is not on the public internet`), { code: 'EBLOCKED' }));
      if (options?.all) return callback(null, addresses);
      callback(null, addresses[0].address, addresses[0].family);
    });
  };
}

/** One request, no redirects followed, no cookies or credentials, uncompressed, with timeouts. */
function request(url, lookup, deadline) {
  return new Promise((resolve, reject) => {
    const req = https.get(url, { lookup, headers: { 'user-agent': 'polymend-fetch', accept: '*/*', 'accept-encoding': 'identity' }, timeout: LIMITS.connectMs, agent: false }, response => { clearTimeout(timer); resolve(response); });
    // A wall-clock limit for this request as well as the idle timeout: the whole fetch, with
    // its redirects, has one deadline.
    const timer = setTimeout(() => req.destroy(new Error('The download took too long.')), Math.max(1, deadline - Date.now()));
    req.on('timeout', () => req.destroy(new Error('The server did not answer in time.')));
    req.on('error', error => { clearTimeout(timer); reject(error); });
  });
}

/** The start of a file that could be a model: a GLB's magic, or something an STL could be. */
function looksLikeModel(head) {
  if (head.length >= 4 && head.toString('latin1', 0, 4) === 'glTF') return true;
  const text = head.toString('latin1', 0, Math.min(head.length, 512)).trimStart().toLowerCase();
  if (text.startsWith('<') || text.startsWith('{')) return false; // an HTML or JSON page, such as an error
  return head.length >= 84; // a binary STL has an 80-byte header and a count
}

/**
 * Download `link` into `dir` and return the saved path. The file name comes from the link,
 * made safe; `takenName(name)` may return a different, unused name.
 */
export async function fetchModel(link, dir, { lookup = guardedLookup(), limits = LIMITS } = {}) {
  let url = checkLink(link);
  const deadline = Date.now() + limits.totalMs;
  let response;
  for (let hop = 0; ; hop++) {
    response = await request(url, lookup, deadline);
    if (response.statusCode >= 300 && response.statusCode < 400 && response.headers.location) {
      response.resume();
      if (hop >= limits.redirects) throw new Error('Too many redirects.');
      url = checkLink(new URL(response.headers.location, url).href);
      continue;
    }
    break;
  }
  if (response.statusCode !== 200) { response.resume(); throw new Error(`The server answered ${response.statusCode}.`); }
  if (response.headers['content-encoding'] && response.headers['content-encoding'] !== 'identity') { response.destroy(); throw new Error('The server sent a compressed file; download it and pass the file instead.'); }
  const declared = Number(response.headers['content-length']);
  if (declared > limits.bytes) { response.destroy(); throw new Error(`The file is larger than ${limits.bytes / 1024 ** 2} MB.`); }

  const fromLink = decodeURIComponent(path.posix.basename(url.pathname)) || 'model';
  const base = fromLink.replace(/[^A-Za-z0-9._()+ -]/g, '_').replace(/^[.]+/, '_').slice(0, 100) || 'model';
  const name = /\.(glb|stl)$/i.test(base) ? base : `${base}.glb`;
  fs.mkdirSync(dir, { recursive: true });
  const target = path.join(dir, name);
  // A temporary name of its own, so an earlier interrupted download can neither block this
  // one nor be removed by it.
  const partial = path.join(dir, `.${crypto.randomBytes(8).toString('hex')}.part`);
  const out = fs.createWriteStream(partial, { flags: 'wx' });
  let size = 0, head = Buffer.alloc(0), checked = false;
  try {
    await new Promise((resolve, reject) => {
      const fail = error => { clearTimeout(timer); response.destroy(); out.destroy(); reject(error); };
      const timer = setTimeout(() => fail(new Error('The download took too long.')), Math.max(1, deadline - Date.now()));
      response.on('data', chunk => {
        size += chunk.length;
        if (!checked && head.length < 512) head = Buffer.concat([head, chunk.subarray(0, 512 - head.length)]);
        // Judge the start of the file as soon as there is enough of it, not after the whole download.
        if (!checked && (head.length >= 512 || size >= 512)) { checked = true; if (!looksLikeModel(head)) return fail(new Error('The link did not give a 3D model file.')); }
        if (size > limits.bytes) fail(new Error(`The file is larger than ${limits.bytes / 1024 ** 2} MB.`));
      });
      response.on('error', fail);
      out.on('error', fail);
      out.on('finish', () => { clearTimeout(timer); resolve(); });
      response.pipe(out);
    });
    if (!looksLikeModel(head)) throw new Error('The link did not give a 3D model file.');
    let final = target;
    for (let n = 2; fs.existsSync(final); n++) final = target.replace(/(\.[^.]+)$/, `-${n}$1`);
    fs.renameSync(partial, final);
    return final;
  } catch (error) {
    out.destroy();
    await new Promise(resolve => (out.closed ? resolve() : out.once('close', resolve)));
    fs.rmSync(partial, { force: true });
    throw error;
  }
}
