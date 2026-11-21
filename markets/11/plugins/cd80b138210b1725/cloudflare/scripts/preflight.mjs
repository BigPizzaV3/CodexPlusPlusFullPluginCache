import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

export function inspectConfig(config) {
  const allowed = ['$schema', 'name', 'account_id', 'main', 'compatibility_date',
    'compatibility_flags', 'workers_dev', 'preview_urls', 'observability', 'vars', 'ratelimits', 'dev'];
  if (Object.keys(config).some(key => !allowed.includes(key))) {
    throw new Error('Unexpected deployment options or resource bindings. Review them before deployment.');
  }
  if (!/^[0-9a-f]{32}$/.test(config.account_id ?? '')) throw new Error('Select the target Cloudflare account first.');
  const origin = config.vars?.PUBLIC_ORIGIN;
  if (typeof origin !== 'string') throw new Error('Set the confirmed production origin.');
  const url = new URL(origin);
  if (origin !== url.origin || url.protocol !== 'https:' || url.username || url.password ||
      url.port || !/^[a-z0-9-]+\.[a-z0-9-]+\.workers\.dev$/.test(url.hostname) ||
      url.hostname.split('.')[0] !== config.name) throw new Error('Worker name and confirmed workers.dev origin must match.');
  if (config.main !== 'src/index.ts' || config.workers_dev !== true || config.preview_urls !== false ||
      config.observability?.enabled !== false || Object.keys(config.observability).length !== 1 ||
      JSON.stringify(config.compatibility_flags) !== JSON.stringify(['nodejs_compat']) ||
      !/^\d{4}-\d{2}-\d{2}$/.test(config.compatibility_date ?? '') ||
      Object.keys(config.vars).length !== 1) throw new Error('Source, routing, metadata logging or variable settings differ from this profile.');
  const limiters = config.ratelimits;
  if (!Array.isArray(limiters) || limiters.length !== 2) throw new Error('Both request limiters are required.');
  const names = ['MCP_IP_LIMITER', 'MCP_SERVICE_LIMITER'];
  for (let index = 0; index < 2; index++) {
    const entry = limiters[index];
    if (entry.name !== names[index] || !/^[1-9]\d*$/.test(entry.namespace_id ?? '') ||
        entry.simple?.period !== 60 || entry.simple?.limit !== [120, 1200][index] ||
        Object.keys(entry).some(key => !['name', 'namespace_id', 'simple'].includes(key)) ||
        Object.keys(entry.simple).some(key => !['limit', 'period'].includes(key))) {
      throw new Error('Request limiter configuration differs from the reviewed profile.');
    }
  }
  if (limiters[0].namespace_id === limiters[1].namespace_id) throw new Error('Use distinct rate limit namespaces.');
  return { worker: config.name, endpoint: `${origin}/mcp`, account_selected: true,
    preview_urls: false, body_limit_bytes: 16384,
    per_ip_per_location_per_minute: 120, per_service_per_location_per_minute: 1200,
    cloud_account_accessed: false, free_plan_verified: false, deployed: false,
    remaining: ['Verify the selected account is on Workers Free',
      'Check for an existing Worker and unused limiter namespaces',
      'Verify ownership, domain challenge and production CPU after deployment'] };
}

async function main() {
  const args = process.argv.slice(2);
  if (args.length !== 2 || args[0] !== '--config') throw new Error('Use --config <prepared-config.json>. This command is local and never deploys.');
  const config = JSON.parse(await readFile(args[1], 'utf8'));
  console.log(JSON.stringify(inspectConfig(config), null, 2));
}
if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  main().catch(error => { console.error(error.message); process.exitCode = 1; });
}
