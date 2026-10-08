import React from 'react'
import { Easing, interpolate, useCurrentFrame } from 'remotion'
import { MOTION } from '../grammar'
import { FPS } from './timing'

export interface CursorPath {
  from: { x: number; y: number }
  to: { x: number; y: number }
  startFrame: number
  endFrame: number
}

export interface CursorPose {
  x: number
  y: number
  scale: number
  pressed: boolean
}

/** Eased travel, then a clickDipMs press (scale 0.9) at arrival. Pure, so the stills can be reasoned about. */
export function cursorPose(frame: number, path: CursorPath): CursorPose {
  const travelEnd = Math.max(path.startFrame + 1, path.endFrame)
  const t = interpolate(frame, [path.startFrame, travelEnd], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.inOut(Easing.cubic),
  })
  const dip = Math.ceil((MOTION.clickDipMs / 1000) * FPS)
  const pressed = frame > path.endFrame && frame <= path.endFrame + dip
  return {
    x: path.from.x + (path.to.x - path.from.x) * t,
    y: path.from.y + (path.to.y - path.from.y) * t,
    scale: pressed ? 0.9 : 1,
    pressed,
  }
}

interface CursorProps {
  path: CursorPath
  size?: number
  color?: string
}

/** The reference ads' cursor: a plain arrow with a soft shadow, positioned in canvas pixels. */
export const Cursor: React.FC<CursorProps> = ({ path, size = 44, color = '#111113' }) => {
  const frame = useCurrentFrame()
  const pose = cursorPose(frame, path)
  if (frame < path.startFrame) return null
  const style: React.CSSProperties = {
    position: 'absolute',
    left: pose.x,
    top: pose.y,
    transform: `scale(${pose.scale})`,
    transformOrigin: '20% 10%',
    filter: 'drop-shadow(0 4px 10px rgba(0,0,0,0.25))',
  }
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" style={style}>
      <path d="M5 3l14 8.5-6.2 1.4L10 20z" fill={color} stroke="#fff" strokeWidth="1.5" strokeLinejoin="round" />
    </svg>
  )
}
