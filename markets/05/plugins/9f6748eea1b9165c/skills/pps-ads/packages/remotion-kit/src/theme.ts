import { darken, luminance } from './motion/color'

export type Canvas = 'light' | 'dark'

/** One brand color plus the canvas's own surfaces and ink. Nothing else is colored in a beat. */
export interface AdTheme {
  canvas: Canvas
  /** The brand color, for blocks, buttons, keywords on footage and the cursor. */
  accent: string
  /** The brand color as TEXT on the canvas: darkened when it would not read on a light canvas. */
  accentInk: string
  canvasBg: string
  surface: string
  canvasFg: string
  canvasMuted: string
  hairline: string
  footageFg: string
  displayFont: string
  uiFont: string
}

export const DEFAULT_ACCENT = '#d4a84b'
/** Below this the brand color reads as text on white; above it the ink variant is darkened to reach it. */
const LIGHT_INK_MAX_LUMINANCE = 0.35

export function themeFromBrand(brand: { color?: string; canvas?: Canvas }): AdTheme {
  const accent = brand.color ?? DEFAULT_ACCENT
  const canvas: Canvas = brand.canvas ?? 'light'
  let accentInk = accent
  if (canvas === 'light') {
    let guard = 0
    while (luminance(accentInk) > LIGHT_INK_MAX_LUMINANCE && guard < 12) {
      accentInk = darken(accentInk, 0.12)
      guard += 1
    }
  }
  return canvas === 'light'
    ? {
        canvas, accent, accentInk,
        canvasBg: '#fafafa', surface: '#ffffff', canvasFg: '#111113', canvasMuted: 'rgba(17,17,19,0.6)',
        hairline: 'rgba(17,17,19,0.1)', footageFg: '#ffffff', displayFont: 'Bricolage Grotesque', uiFont: 'Inter',
      }
    : {
        canvas, accent, accentInk,
        canvasBg: '#0f0f11', surface: '#1a1a1e', canvasFg: '#fafafa', canvasMuted: 'rgba(250,250,250,0.6)',
        hairline: 'rgba(250,250,250,0.12)', footageFg: '#ffffff', displayFont: 'Bricolage Grotesque', uiFont: 'Inter',
      }
}
