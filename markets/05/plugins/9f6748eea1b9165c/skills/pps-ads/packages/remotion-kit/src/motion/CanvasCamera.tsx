import React from 'react'
import { AbsoluteFill, Easing, interpolate, useCurrentFrame } from 'remotion'
import { MOTION, type CanvasFamily } from '../grammar'

/**
 * Scale over a beat: 1 at its first frame, never above 1 + pushInMax. Parallax changes the RATE (deeper layers get
 * there sooner), not the ceiling, so no layer ever exceeds the spec's push-in.
 */
export function pushInScale(frame: number, beatFrames: number, family: CanvasFamily): number {
  const t = interpolate(frame, [0, Math.max(1, beatFrames)], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  })
  return Math.min(1 + MOTION.pushInMax, 1 + MOTION.pushInMax * MOTION.parallax[family] * t)
}

interface CanvasCameraProps {
  beatFrames: number
  family: CanvasFamily
  children: React.ReactNode
  style?: React.CSSProperties
  /** True inside a Device screen: the device's own camera already pushes, so the inner beat holds still. */
  disabled?: boolean
}

/** The camera never stops: every canvas layer pushes in over its beat, deeper layers a little sooner. */
export const CanvasCamera: React.FC<CanvasCameraProps> = ({ beatFrames, family, children, style, disabled }) => {
  const frame = useCurrentFrame()
  if (disabled) return <AbsoluteFill style={style}>{children}</AbsoluteFill>
  const scale = pushInScale(frame, beatFrames, family)
  return (
    <AbsoluteFill style={{ transform: `scale(${scale})`, transformOrigin: '50% 50%', ...style }}>
      {children}
    </AbsoluteFill>
  )
}
