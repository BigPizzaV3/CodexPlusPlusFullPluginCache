// Usage: npm run package -- <mcp_url>
// OpenAI plugin ZIP format (developers.openai.com/plugins/deploy/submission, Oct 2 2026; reference jawd-chatgpt-plugin 4e5e3c4):
//   root plugin.json (listing in extensions.com.openai.interface) + root mcp.json + assets/icon.png + assets/logo.png.
//   NO .app.json, NO .codex-plugin/, NO hooks (portal rejects them).
// Listing per plugin lives in listing.json at the repo root: { product, displayName?, subtitle (<=30), category }.
// product picks the brand: icon (assets/brand/<product>.png, 512px, the product's real logo) + real privacy page.
// Checks before zipping: exact MCP URL initializes with our slug, privacy URL = 200 with NO redirect, subtitle/name <=30,
// category in OpenAI's list, icon square 48-4096px <=5MiB. Then zips <slug>/ (no node_modules) to dist/<slug>.zip + sha256.
import { writeFileSync, mkdirSync, rmSync, existsSync, readFileSync, copyFileSync, statSync } from 'node:fs'
import { execFileSync } from 'node:child_process'
import { createHash } from 'node:crypto'
import { config } from '../src/plugin.config.ts'

export const BRANDS = {
  lauki: { website: 'https://lauki.ai', privacy: 'https://lauki.ai/privacy/', developer: 'Upsurge Labs', color: '#1F7A3A', colorDark: '#E8F5EC' },
  naksha: { website: 'https://naksha.social', privacy: 'https://naksha.social/privacy', developer: 'Upsurge Labs', color: '#1B1440', colorDark: '#F3EEDF' },
  gulab: { website: 'https://gulab.ai', privacy: 'https://gulab.ai/privacy', developer: 'Upsurge Labs', color: '#C2185B', colorDark: '#FCE4EC' },
  zelta: { website: 'https://zelta.in', privacy: 'https://zelta.in/privacy-policy', developer: 'Upsurge Labs', color: '#0F4C5C', colorDark: '#E6F2F4' },
}
// terms + support pages (portal requires a support URL; Jawd's accepted manifest carries both). All verified 200 Oct 3 2026.
export const BRAND_LINKS = {
  lauki: { terms: 'https://lauki.ai/terms/', support: 'https://lauki.ai/support/' },
  naksha: { terms: 'https://naksha.social/terms', support: 'https://naksha.social/support' },
  gulab: { terms: 'https://gulab.ai/terms', support: 'mailto:hi@lauki.ai' },
  zelta: { terms: 'https://zelta.in/terms-of-service', support: 'https://zelta.in/contact' },
}
export const CATEGORIES = ['Productivity', 'Creativity', 'Developer Tools', 'Business & Operations', 'Data & Analytics', 'Communication', 'Education & Research', 'Security', 'Finance', 'Healthcare', 'Travel', 'Entertainment', 'Other']

const fail = (m) => { console.error(m); process.exit(1) }
const mcpUrl = process.argv[2]
if (!mcpUrl || !/^https:\/\/[a-z0-9.-]+\/mcp$/.test(mcpUrl)) { console.error('usage: npm run package -- https://<host>/mcp'); process.exit(2) }
if (!existsSync('listing.json')) fail('listing.json missing: { "product": "lauki|naksha|gulab|zelta", "subtitle": "<=30 chars", "category": "<OpenAI category>" }')
const listing = JSON.parse(readFileSync('listing.json', 'utf8'))
const brand = BRANDS[listing.product] ?? fail(`listing.product must be one of ${Object.keys(BRANDS).join(', ')}`)
const displayName = listing.displayName ?? config.name
if (!displayName || displayName.length > 30) fail(`displayName must be 1-30 chars: "${displayName}"`)
if (!listing.subtitle || listing.subtitle.length > 30) fail(`subtitle must be 1-30 chars: "${listing.subtitle}"`)
if (!CATEGORIES.includes(listing.category)) fail(`category "${listing.category}" not in ${CATEGORIES.join(', ')}`)
const icon = `assets/brand/${listing.product}.png`
if (!existsSync(icon)) fail(`${icon} missing`)
const dims = execFileSync('identify', ['-format', '%w %h', icon]).toString().split(' ').map(Number)
if (dims[0] !== dims[1] || dims[0] < 48 || dims[0] > 4096 || statSync(icon).size > 5 * 1024 * 1024) fail(`icon not square 48-4096px <=5MiB: ${dims}`)

// 1. URL checks against the exact URLs that go into the manifests
const res = await fetch(mcpUrl, { method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json, text/event-stream', 'x-lauki-qa': '1', 'user-agent': 'lauki-qa/package' }, body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'initialize', params: { protocolVersion: '2025-06-18', capabilities: {}, clientInfo: { name: 'package-check', version: '1' } } }) })
const body = await res.json().catch(() => ({}))
if (res.status !== 200 || body?.result?.serverInfo?.name !== config.slug) fail(`URL CHECK FAILED: ${mcpUrl} -> ${res.status} ${JSON.stringify(body).slice(0, 200)}`)
// privacyPolicyURL = the app's own short policy on the MCP host (core/privacy.ts). The OpenAI portal kept flagging
// "Review the plugin's privacy policy" against long brand pages whose ChatGPT section sat at the end (naksha, Oct 3 2026).
const privacyUrl = new URL('/privacy', mcpUrl).href
const priv = await fetch(privacyUrl, { redirect: 'manual', headers: { 'user-agent': 'Mozilla/5.0 lauki-qa/package' } })
const privText = priv.status === 200 ? await priv.text() : ''
if (priv.status !== 200 || !privText.includes(`${config.name} app for ChatGPT`)) fail(`PRIVACY CHECK FAILED: ${privacyUrl} -> ${priv.status} (must be 200, no redirect, naming the ChatGPT app)`)
console.log(`url check ok: ${mcpUrl} (serverInfo ${body.result.serverInfo.name} ${body.result.serverInfo.version}), privacy ${privacyUrl} 200`)

// 2. manifests (old .app.json / .codex-plugin are removed: the portal rejects them)
rmSync('.app.json', { force: true }); rmSync('.codex-plugin', { recursive: true, force: true })
mkdirSync('assets', { recursive: true })
copyFileSync(icon, 'assets/icon.png'); copyFileSync(icon, 'assets/logo.png')
const plugin = {
  $schema: 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json',
  name: config.slug,
  version: config.version,
  description: config.longDescription,
  author: { name: brand.developer, email: config.privacy.contact, url: brand.website },
  homepage: brand.website,
  extensions: {
    'com.openai': {
      interface: {
        displayName,
        shortDescription: listing.subtitle,
        longDescription: `${config.longDescription} Outbound links carry campaign tags identifying ChatGPT as the source.`,
        developerName: brand.developer,
        category: listing.category,
        capabilities: config.tools.map((t) => t.title).filter(Boolean),
        // starter prompts: listing.json `prompts` (max 3), taken from real user queries (cite-probe)
        ...(Array.isArray(listing.prompts) && listing.prompts.length ? { defaultPrompt: listing.prompts.slice(0, 3) } : {}),
        websiteURL: brand.website,
        privacyPolicyURL: privacyUrl,
        ...(BRAND_LINKS[listing.product] ? { termsOfServiceURL: BRAND_LINKS[listing.product].terms, supportURL: BRAND_LINKS[listing.product].support } : {}),
        brandColor: brand.color,
        brandColorDark: brand.colorDark,
        composerIcon: './assets/icon.png',
        logo: './assets/logo.png',
      },
    },
  },
}
writeFileSync('plugin.json', JSON.stringify(plugin, null, 2) + '\n')
writeFileSync('mcp.json', JSON.stringify({ $schema: 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json', mcpServers: { [config.slug]: { type: 'streamable-http', url: mcpUrl } } }, null, 2) + '\n')

// 3. zip from a staging copy named <slug>/
const stage = `/tmp/pkg-${config.slug}`
rmSync(stage, { recursive: true, force: true }); mkdirSync(stage, { recursive: true })
execFileSync('rsync', ['-a', '--exclude', 'node_modules', '--exclude', '.wrangler', '--exclude', 'dist', '--exclude', '.git', '--exclude', 'assets/brand', '--exclude', '.app.json', '--exclude', '.codex-plugin', './', `${stage}/${config.slug}/`])
mkdirSync('dist', { recursive: true })
const zip = `${process.cwd()}/dist/${config.slug}.zip`
if (existsSync(zip)) rmSync(zip)
execFileSync('zip', ['-q', '-r', '-X', zip, config.slug], { cwd: stage })
execFileSync('unzip', ['-tq', zip])
const names = execFileSync('unzip', ['-Z1', zip]).toString().split('\n')
for (const bad of ['.app.json', '.codex-plugin/', 'hooks']) if (names.some((n) => n.includes(`/${bad}`))) fail(`ZIP contains forbidden ${bad}`)
for (const need of ['plugin.json', 'mcp.json', 'assets/icon.png', 'assets/logo.png']) if (!names.includes(`${config.slug}/${need}`)) fail(`ZIP missing ${need}`)
const sha = createHash('sha256').update(readFileSync(zip)).digest('hex')
writeFileSync(`dist/${config.slug}.zip.sha256`, `${sha}  ${config.slug}.zip\n`)
console.log(JSON.stringify({ zip, sha256: sha, mcp_server_url: mcpUrl, privacy: privacyUrl, category: listing.category, subtitle: listing.subtitle }))
