/** Hex color helpers for the theme's contrast guard. No dependencies. */
function channels(hex: string): [number, number, number] {
  const h = hex.replace('#', '')
  const full = h.length === 3 ? h.split('').map((c) => c + c).join('') : h
  const n = parseInt(full, 16)
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255]
}

function toHex(r: number, g: number, b: number): string {
  return '#' + [r, g, b].map((v) => Math.round(Math.min(255, Math.max(0, v))).toString(16).padStart(2, '0')).join('')
}

/** WCAG relative luminance, 0 (black) to 1 (white). */
export function luminance(hex: string): number {
  const [r, g, b] = channels(hex).map((v) => {
    const c = v / 255
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4)
  })
  return 0.2126 * r + 0.7152 * g + 0.0722 * b
}

/** Multiply every channel by (1 - amount). */
export function darken(hex: string, amount: number): string {
  const [r, g, b] = channels(hex)
  return toHex(r * (1 - amount), g * (1 - amount), b * (1 - amount))
}

/** Translucent version of a hex color. */
export function alpha(hex: string, a: number): string {
  const [r, g, b] = channels(hex)
  return `rgba(${r},${g},${b},${a})`
}
