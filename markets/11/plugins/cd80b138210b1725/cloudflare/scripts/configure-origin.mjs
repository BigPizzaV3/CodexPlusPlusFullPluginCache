import { readFile, writeFile } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { randomInt } from 'node:crypto';
import { pathToFileURL } from 'node:url';

export function prepareConfig(base, { origin, accountId, namespaceBase }) {
  const url = new URL(origin);
  const match = url.hostname.match(/^([a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)\.([a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)\.workers\.dev$/);
  if (!match || url.protocol !== 'https:' || url.username || url.password ||
      url.pathname !== '/' || url.search || url.hash || url.port || origin !== url.origin) {
    throw new Error('Use the exact confirmed HTTPS origin: https://<worker>.<account-subdomain>.workers.dev');
  }
  if (!/^[0-9a-f]{32}$/.test(accountId ?? '')) {
    throw new Error('Supply the intended Cloudflare account ID (32 lowercase hexadecimal characters).');
  }
  const start = namespaceBase ?? randomInt(100000, 2000000000);
  if (!Number.isSafeInteger(start) || start < 1 || start >= 2147483647) {
    throw new Error('Namespace base must be a positive integer below 2147483647.');
  }
  return {
    $schema: './node_modules/wrangler/config-schema.json',
    name: match[1], account_id: accountId, main: 'src/index.ts',
    compatibility_date: base.compatibility_date,
    compatibility_flags: ['nodejs_compat'], workers_dev: true, preview_urls: false,
    observability: { enabled: false }, vars: { PUBLIC_ORIGIN: url.origin },
    ratelimits: [
      { name: 'MCP_IP_LIMITER', namespace_id: String(start), simple: { limit: 120, period: 60 } },
      { name: 'MCP_SERVICE_LIMITER', namespace_id: String(start + 1), simple: { limit: 1200, period: 60 } },
    ],
    dev: { ip: '127.0.0.1', port: 8787, local_protocol: 'http' },
  };
}

async function main() {
  const args = process.argv.slice(2);
  const allowed = ['--origin', '--output', '--account-id', '--namespace-base'];
  const values = {};
  for (let index = 0; index < args.length; index += 2) {
    const flag = args[index], value = args[index + 1];
    if (!allowed.includes(flag) || !value || value.startsWith('--') || flag in values) {
      throw new Error('Use --origin, --account-id and a new --output path; --namespace-base is optional.');
    }
    values[flag] = value;
  }
  if (!values['--origin'] || !values['--account-id'] || !values['--output']) {
    throw new Error('Supply --origin, --account-id and a new --output config path. No deployment occurs.');
  }
  const output = resolve(values['--output']);
  if (dirname(output) !== process.cwd()) {
    throw new Error('Write the new config beside wrangler.jsonc so source/schema paths remain valid.');
  }
  const base = JSON.parse(await readFile('wrangler.jsonc', 'utf8'));
  const config = prepareConfig(base, { origin: values['--origin'], accountId: values['--account-id'],
    namespaceBase: values['--namespace-base'] === undefined ? undefined : Number(values['--namespace-base']) });
  await writeFile(output, JSON.stringify(config, null, 2) + '\n', { flag: 'wx', mode: 0o600 });
  console.log('New config prepared for the selected account and hostname. No account login, deployment or ownership check occurred. Check namespace IDs are unused in this account.');
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main().catch(error => { console.error(error.message); process.exitCode = 1; });
}
