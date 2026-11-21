import type { PluginConfig } from './types'

export const SURFACES = ['inline', 'panel', 'sidebar', 'fileviewer', 'event'] as const
export type Surface = (typeof SURFACES)[number]

/** The ONLY way a plugin builds an outbound link. Four static params, nothing else:
 * utm_source=chatgpt, utm_medium=plugin, utm_campaign=<config>, utm_content=<tool>--<surface>.
 * Path must be a static string from code (never user input) - tests assert no user value reaches a URL. */
export function funnelLink(cfg: PluginConfig, tool: string, surface: Surface = 'inline', path?: string): string {
  if (!SURFACES.includes(surface)) throw new Error('bad surface')
  if (!cfg.tools.some((t) => t.name === tool)) throw new Error(`utm tool ${tool} is not a registered tool`)
  if (!/^[a-z0-9_]+$/.test(cfg.funnel.campaign)) throw new Error('bad campaign')
  const p = path ?? cfg.funnel.path ?? '/'
  if (!/^\/[A-Za-z0-9/_.#-]*$/.test(p)) throw new Error('funnel path must be a static path')
  const [pathname, hash] = p.split('#')
  const url = new URL(pathname, cfg.funnel.origin)
  if (url.origin !== new URL(cfg.funnel.origin).origin) throw new Error('funnel origin mismatch')
  url.search = new URLSearchParams({ utm_source: 'chatgpt', utm_medium: 'plugin', utm_campaign: cfg.funnel.campaign, utm_content: `${tool}--${surface}` }).toString()
  if (hash) url.hash = hash
  return url.toString()
}
