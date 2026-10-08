import React from 'react'
import { Easing, interpolate, useCurrentFrame } from 'remotion'
import { frames } from './timing'

interface MaskRevealProps {
  children: React.ReactNode
  delaySeconds?: number
  durationMs?: number
  from?: 'left' | 'bottom'
  style?: React.CSSProperties
}

/** A wipe-free reveal: the content is clipped from one edge and the clip opens. Titles enter this way. */
export const MaskReveal: React.FC<MaskRevealProps> = ({
  children,
  delaySeconds = 0,
  durationMs = 400,
  from = 'bottom',
  style,
}) => {
  const frame = useCurrentFrame()
  const start = frames(delaySeconds)
  const end = start + Math.max(1, frames(durationMs / 1000))
  const t = interpolate(frame, [start, end], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  })
  const inset = `${(1 - t) * 100}%`
  const clipPath = from === 'left' ? `inset(0 ${inset} 0 0)` : `inset(${inset} 0 0 0)`
  const shift = from === 'left' ? `translateX(${(1 - t) * -12}px)` : `translateY(${(1 - t) * 18}px)`
  return <div style={{ clipPath, transform: shift, ...style }}>{children}</div>
}
