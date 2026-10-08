import React from 'react'
import { Easing, interpolate, useCurrentFrame } from 'remotion'
import { MOTION } from '../grammar'
import { frames } from './timing'

interface PopInProps {
  children: React.ReactNode
  delaySeconds?: number
  durationMs?: number
  overshoot?: boolean
  /** Entry scale; defaults to the grammar's scaleInFrom. */
  fromScale?: number
  style?: React.CSSProperties
}

/** Scale from fromScale to 1 with a fade; the ONLY overshoot allowed is overshootMax, and off by default. */
export const PopIn: React.FC<PopInProps> = ({
  children,
  delaySeconds = 0,
  durationMs = 280,
  overshoot = false,
  fromScale = MOTION.scaleInFrom,
  style,
}) => {
  const frame = useCurrentFrame()
  const start = frames(delaySeconds)
  const clamped = Math.min(MOTION.easeMaxMs, Math.max(MOTION.easeMinMs, durationMs))
  const end = start + Math.max(1, frames(clamped / 1000))
  const t = interpolate(frame, [start, end], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  })
  const peak = overshoot ? MOTION.overshootMax : 1
  const scale = t < 0.8 ? fromScale + (peak - fromScale) * (t / 0.8) : peak - (peak - 1) * ((t - 0.8) / 0.2)
  const base: React.CSSProperties = { opacity: t, transform: `scale(${scale})`, transformOrigin: '50% 50%' }
  return <div style={{ ...base, ...style }}>{children}</div>
}
