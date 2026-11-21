import type { PluginConfig } from './types'

const esc = (s: string) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]!)

export function privacyHtml(cfg: PluginConfig): string {
  const li = (xs: string[]) => (xs.length ? `<ul>${xs.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>` : '<p>None.</p>')
  return `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(cfg.name)} - Privacy</title>
<style>body{font:15px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;max-width:720px;margin:40px auto;padding:0 20px;color:#1c1917}h1{font-size:24px}h2{font-size:17px;margin-top:28px}</style></head><body>
<h1>${esc(cfg.name)} - Privacy Policy</h1>
<p>Last updated: October 3, 2026. This policy covers the ${esc(cfg.name)} app for ChatGPT, operated by Upsurge Labs Pte. Ltd., Singapore.${cfg.privacy.fullPolicyUrl ? ` It is part of our full privacy policy at <a href="${esc(cfg.privacy.fullPolicyUrl)}">${esc(cfg.privacy.fullPolicyUrl.replace(/^https?:\/\//, ''))}</a>.` : ''}</p>
<h2>What the app receives</h2>${li(cfg.privacy.dataProcessed)}
<p>Only what ChatGPT passes to a tool when you ask. No name, email, account, location or device identifier is requested.</p>
<h2>How it is used and what is not stored</h2>
<p>Inputs are processed in memory only to answer the request and discarded when the answer is returned. We do not store, log, sell or share them, we do not build profiles, and we do not use them to train models. There are no accounts and no cookies.</p>
<h2>What we keep</h2>
<p>A short operational log line per request recording the tool name and the broad client type (for example, ChatGPT), and, if a tool fails, the tool name and error type. These lines contain no inputs, IP addresses or identifiers.</p>
<h2>Third parties</h2>
<p>Our hosting provider, Cloudflare, processes requests to run the app under its standard terms. Your conversation with ChatGPT is governed by OpenAI's privacy policy: <a href="https://openai.com/policies/privacy-policy">openai.com/policies/privacy-policy</a>.</p>
<p>Other services the app calls at runtime:</p>${li(cfg.privacy.thirdParties)}
<h2>Your choices</h2><p>Because nothing you enter is stored, there is nothing to access or delete. You can stop using the app at any time from ChatGPT settings.</p>
<h2>Links and attribution</h2>
<p>Links in results may open ${esc(new URL(cfg.funnel.origin).host)}. Those links carry fixed campaign tags (utm_source=chatgpt, utm_medium=plugin, utm_campaign=${esc(cfg.funnel.campaign)}, utm_content=the tool name) that identify ChatGPT as the source. They never contain your inputs or any identifier about you.</p>
<h2>Data sources</h2>${li(cfg.privacy.attributions)}
<h2>Children</h2><p>This app is not directed to anyone under ${cfg.privacy.minAge ?? 13}.</p>
<h2>Contact</h2><p>${esc(cfg.privacy.contact)}</p>
</body></html>`
}
