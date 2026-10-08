import React, { createContext, useContext } from 'react'
import { Easing, interpolate, useCurrentFrame, useVideoConfig } from 'remotion'
import { frames } from '../motion/timing'
import type { AdTheme } from '../theme'

export interface StageSize {
  width: number
  height: number
}

/**
 * The box a canvas beat lays itself out in. The whole canvas by default; a Device beat renders its inner
 * beat at a virtual stage with the screen's own shape and scales it down, so every inner size and every
 * cursor target still adds up.
 */
const StageContext = createContext<StageSize | null>(null)

export const StageProvider: React.FC<{ size: StageSize; children: React.ReactNode }> = ({ size, children }) => (
  <StageContext.Provider value={size}>{children}</StageContext.Provider>
)

/** The stage box plus `u`, its short side: the one scale unit every canvas size is written in. */
export function useStage(): StageSize & { u: number } {
  const config = useVideoConfig()
  const stage = useContext(StageContext) ?? { width: config.width, height: config.height }
  return { ...stage, u: Math.min(stage.width, stage.height) }
}

/** The one card look on the canvas: surface, hairline border, soft shadow; sized by the stage's short side `u`. */
export function cardStyle(theme: AdTheme, width: number, u: number): React.CSSProperties {
  return {
    background: theme.surface,
    border: `1px solid ${theme.hairline}`,
    borderRadius: 24,
    boxShadow: theme.canvas === 'light' ? '0 18px 50px rgba(17,17,19,0.10)' : '0 18px 50px rgba(0,0,0,0.45)',
    padding: u * 0.05,
    width: Math.min(width * 0.9, u * 1.25),
    boxSizing: 'border-box',
  }
}

/** Text on a brand-colored block: dark, because the accent is a bright brand color either way. */
export const ON_ACCENT = '#111113'

/** The Cursor arrow's tip sits at (5, 3) of its 24-unit box; aim a path here so the tip, not the corner, lands. */
export function cursorTip(size: number): { x: number; y: number } {
  return { x: (size * 5) / 24, y: (size * 3) / 24 }
}

/** A zero-size box centered on its positioned parent, so a Cursor inside it aims at the parent's center. */
export const CENTER_ANCHOR: React.CSSProperties = {
  position: 'absolute',
  left: '50%',
  top: '50%',
  width: 0,
  height: 0,
  zIndex: 5,
}

/** The ring a press leaves: it opens from the tip in the brand color and fades, 0.35 s after `pressFrame`. */
export const PressRing: React.FC<{ pressFrame: number; size: number; color: string }> = ({
  pressFrame,
  size,
  color,
}) => {
  const frame = useCurrentFrame()
  if (frame < pressFrame) return null
  const t = interpolate(frame, [pressFrame, pressFrame + frames(0.35)], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  })
  if (t >= 1) return null
  const d = size * (0.5 + t)
  return (
    <div
      style={{
        position: 'absolute',
        left: -d / 2,
        top: -d / 2,
        width: d,
        height: d,
        borderRadius: 999,
        border: `${Math.max(2, size * 0.06)}px solid ${color}`,
        opacity: 1 - t,
        pointerEvents: 'none',
      }}
    />
  )
}
