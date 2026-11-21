import assert from 'node:assert/strict';
import { readFile, access, readdir } from 'node:fs/promises';
const root = new URL('../', import.meta.url);
const json = async path => JSON.parse(await readFile(new URL(path, root), 'utf8'));
const manifest = await json('plugin.json');
const mcp = await json('mcp.json');
assert.equal(manifest.name, 'peptide-reconstitution-calculator');
assert.equal(manifest.version, (await json('package.json')).version);
const listing = manifest.extensions['com.openai'].interface;
// Documented directory enum, verified 2026-10-04:
// https://developers.openai.com/plugins/deploy/submission-errors#listing-and-interface-errors
const allowedCategories = new Set([
  'Productivity', 'Creativity', 'Developer Tools', 'Business & Operations',
  'Data & Analytics', 'Communication', 'Education & Research', 'Security',
  'Finance', 'Healthcare', 'Travel', 'Entertainment', 'Other'
]);
assert.ok(allowedCategories.has(listing.category), `Unsupported directory category: ${listing.category}. Use an exact documented category value.`);
assert.ok(listing.displayName.length <= 30, 'Directory display name exceeds 30 characters');
assert.ok(listing.shortDescription.length <= 30, 'Directory subtitle exceeds 30 characters');
assert.equal(mcp.mcpServers['concentration-calculator'].type, 'streamable-http');
assert.equal(new URL(mcp.mcpServers['concentration-calculator'].url).pathname, '/mcp');
for (const path of ['src/http.mjs', 'src/stdio.mjs', 'dist/calculator.html', 'skills/peptide-concentration/SKILL.md', manifest.extensions['com.openai'].interface.logo]) await access(new URL(path, root));
let checked = 0;
async function scan(directory) {
  for (const file of await readdir(directory, { withFileTypes: true })) {
    if (['node_modules', '.git', '.vercel', 'dist'].includes(file.name)) continue;
    const url = new URL(`${file.name}${file.isDirectory() ? '/' : ''}`, directory);
    if (file.isDirectory()) await scan(url);
    else if (/\.(mjs|html|css|md|json|svg)$/.test(file.name)) {
      const text = await readFile(url, 'utf8');
      if (file.name !== 'validate-package.mjs') {
        assert.ok(!/DoseVault|The Protocol|peptidesvietnam|stripe|posthog|google-analytics/i.test(text), `Forbidden brand, payment, or tracking reference: ${file.name}`);
        assert.ok(!/[\u2013\u2014]/.test(text), `Long dash found: ${file.name}`);
      }
      assert.ok(!/sk-(?:proj-)?[a-zA-Z0-9_-]{20,}/.test(text), `Possible credential: ${file.name}`);
      checked++;
    }
  }
}
await scan(root);
const html = await readFile(new URL('dist/calculator.html', root), 'utf8');
assert.ok(html.includes('Peptide Reconstitution Calculator by Peptara Labs'), 'Missing requested branding');
assert.ok(!/DoseVault|peptidesvietnam|stripe|posthog|google-analytics/i.test(html), 'Forbidden reference in shipped component');
const anchors = [...html.matchAll(/<a\s[^>]*href="([^"]+)"/g)].map(match => new URL(match[1]));
const allowedLinks = new Set([
  'https://www.peptaralabs.io/',
  'https://www.peptaralabs.io/coa',
  'https://peptara-calculator.vercel.app/privacy',
  'https://peptara-calculator.vercel.app/support',
  'https://goldbook.iupac.org/terms/view/M03713',
  'https://www.embecta.com/ca/en-ca/insulin-syringes/ultra-fine/'
]);
for (const link of anchors) assert.ok(allowedLinks.has(link.href), `Unexpected outbound destination: ${link.href}`);
assert.equal(anchors.filter(link => link.hostname === 'www.peptaralabs.io').length, 2, 'Expected two brand CTAs');
console.log(`Package checks passed across ${checked} source files. Public endpoint is configured; deployment and directory approval must be verified separately.`);
