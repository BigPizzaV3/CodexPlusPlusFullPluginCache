import React from 'react'
import { Easing, interpolate, useCurrentFrame } from 'remotion'
import { MOTION } from '../grammar'
import { frames } from './timing'

/** The only entrance the grammar allows: a 20 to 40 px slide with a fade, eased 200 to 400 ms. */
export const SlideFade: React.FC<{
  children: React.ReactNode
  delaySeconds?: number
  durationMs?: number
  distancePx?: number
  from?: 'up' | 'down' | 'left' | 'right'
  style?: React.CSSProperties
}> = ({ children, delaySeconds = 0, durationMs = 320, distancePx = 30, from = 'up', style }) => {
  const frame = useCurrentFrame()
  const d = Math.min(MOTION.easeMaxMs, Math.max(MOTION.easeMinMs, durationMs))
  const dist = Math.min(MOTION.slidePxMax, Math.max(MOTION.slidePxMin, distancePx))
  const start = frames(delaySeconds)
  const end = start + frames(d / 1000)
  const t = interpolate(frame, [start, end], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  })
  const dx = from === 'left' ? -dist : from === 'right' ? dist : 0
  const dy = from === 'up' ? dist : from === 'down' ? -dist : 0
  return (
    <div style={{ opacity: t, transform: `translate(${dx * (1 - t)}px, ${dy * (1 - t)}px)`, ...style }}>{children}</div>
  )
}
