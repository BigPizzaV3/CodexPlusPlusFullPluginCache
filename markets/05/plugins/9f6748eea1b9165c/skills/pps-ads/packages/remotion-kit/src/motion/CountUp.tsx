import React from 'react'
import { Easing, interpolate, useCurrentFrame } from 'remotion'
import { MOTION } from '../grammar'
import { FPS } from './timing'

export interface CountTarget {
  value: number
  prefix: string
  suffix: string
  grouped: boolean
  /** Digits after the decimal point in the raw number, 0 when none. */
  decimals: number
}

/** "2,400 new visits" -> 2400 + " new visits"; "$1.2M raised" -> $ 1.2 "M raised". No number, no count-up. */
export function parseCountTarget(text: string): CountTarget | null {
  const match = text.match(/^([^\d]*?)(\d[\d,]*(?:\.\d+)?)(.*)$/)
  if (!match) return null
  const [, prefix, raw, suffix] = match
  const dot = raw.indexOf('.')
  return {
    value: Number(raw.replace(/,/g, '')),
    prefix,
    suffix,
    grouped: raw.includes(','),
    decimals: dot === -1 ? 0 : raw.length - dot - 1,
  }
}

/** Whether the number reads as a count: not a rank (#1), a ratio (24/7), a year (2026) or a single digit. */
export function shouldCountUp(target: CountTarget, raw: string): boolean {
  if (target.value < 10) return false
  if (target.prefix.endsWith('#')) return false
  if (target.suffix.startsWith('/')) return false
  if (/^(19|20)\d\d$/.test(raw)) return false
  return true
}

export function countUpValue(
  frame: number,
  target: number,
  fps: number = FPS,
  grouped = true,
  decimals = 0,
): string {
  const end = Math.ceil((MOTION.countUpMs / 1000) * fps)
  const t = interpolate(frame, [0, end], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  })
  const fixed = (target * t).toFixed(decimals)
  if (!grouped) return fixed
  return Number(fixed).toLocaleString('en-US', { minimumFractionDigits: decimals, maximumFractionDigits: decimals })
}

interface CountUpProps {
  text: string
  style?: React.CSSProperties
}

export const CountUp: React.FC<CountUpProps> = ({ text, style }) => {
  const frame = useCurrentFrame()
  const target = parseCountTarget(text)
  const raw = text.match(/\d[\d,]*(?:\.\d+)?/)?.[0] ?? ''
  if (!target || !shouldCountUp(target, raw)) return <span style={style}>{text}</span>
  return (
    <span style={style}>
      {target.prefix}
      {countUpValue(frame, target.value, FPS, target.grouped, target.decimals)}
      {target.suffix}
    </span>
  )
}
