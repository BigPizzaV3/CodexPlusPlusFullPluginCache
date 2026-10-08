import React from 'react'
import { AbsoluteFill, Img, useCurrentFrame } from 'remotion'
import { CanvasCamera } from '../../motion/CanvasCamera'
import { PopIn } from '../../motion/PopIn'
import { gridSeconds, quantizeToGrid } from '../../motion/grid'
import { FPS, frames } from '../../motion/timing'
import { BrandTag } from '../BrandTag'
import { inter } from '../fonts'
import { cardStyle, useStage } from '../stage'
import type { AdTheme } from '../../theme'
import type { BeatProps } from '../types'

const FIRST_STEP_SECONDS = 0.2
const LAST_STEP_BEFORE_END_SECONDS = 0.6
const LAST_CHECK_BEFORE_END_SECONDS = 0.4
const SPIN_SECONDS_PER_TURN = 0.8

/**
 * Step times on the music grid: the first on the grid line nearest 0.2 s, then one every `stretch` grid steps,
 * where `stretch` is the largest whole number that keeps the last step at least 0.6 s before the beat ends
 * (never below 1). Every step lands on the beat and the steps spread across the room the beat has.
 */
export function agentStepTimes(count: number, bpm: number, seconds: number): number[] {
  const first = quantizeToGrid(FIRST_STEP_SECONDS, bpm)
  const grid = gridSeconds(bpm)
  const room = seconds - LAST_STEP_BEFORE_END_SECONDS - first
  const stretch = count > 1 ? Math.max(1, Math.floor(room / ((count - 1) * grid) + 1e-9)) : 1
  return Array.from({ length: count }, (_, i) => Number((first + i * grid * stretch).toFixed(6)))
}

const Spinner: React.FC<{ size: number; theme: AdTheme }> = ({ size, theme }) => {
  const frame = useCurrentFrame()
  const degrees = ((frame / FPS) / SPIN_SECONDS_PER_TURN) * 360
  const r = 9
  const circumference = 2 * Math.PI * r
  return (
    <svg width={size} height={size} viewBox="0 0 24 24">
      <circle cx="12" cy="12" r={r} fill="none" stroke={theme.hairline} strokeWidth="3" />
      <circle
        cx="12"
        cy="12"
        r={r}
        fill="none"
        stroke={theme.accent}
        strokeWidth="3"
        strokeLinecap="round"
        strokeDasharray={`${circumference * 0.28} ${circumference}`}
        transform={`rotate(${degrees} 12 12)`}
      />
    </svg>
  )
}

/** The tick: a filled brand-color circle with a white check, popping in when the step is done. */
const CheckMark: React.FC<{ size: number; color: string }> = ({ size, color }) => (
  <svg width={size} height={size} viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="11" fill={color} />
    <path d="M7 12.5l3.2 3.2L17 9" fill="none" stroke="#ffffff" strokeWidth="2.6" strokeLinecap="round" />
  </svg>
)

/** The assistant at work: each step appears on the grid with a spinner that turns to a check when the next lands. */
export const Agent: React.FC<BeatProps> = ({ beat, theme, brand, seconds, bpm, compact }) => {
  const frame = useCurrentFrame()
  const { width, u } = useStage()
  const lines = beat.lines ?? []
  const times = agentStepTimes(lines.length, bpm, seconds)
  const lastCheck = seconds - LAST_CHECK_BEFORE_END_SECONDS
  const icon = u * 0.066
  return (
    <AbsoluteFill style={{ background: theme.canvasBg }}>
      <CanvasCamera beatFrames={frames(seconds)} family="card" disabled={compact}>
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
          <PopIn style={{ width: '100%', display: 'flex', justifyContent: 'center' }}>
            <div
              style={{
                ...cardStyle(theme, width, u),
                display: 'flex',
                alignItems: 'flex-start',
                gap: u * 0.04,
                fontFamily: inter.fontFamily,
              }}
            >
              <div style={{ flex: 1, minWidth: 0, display: 'grid', gap: u * 0.036 }}>
                {lines.map((line, i) => {
                  const doneAt = i + 1 < times.length ? times[i + 1] : lastCheck
                  const done = frame >= frames(doneAt)
                  return (
                    <PopIn key={i} delaySeconds={times[i]} style={{ transformOrigin: '0% 50%' }}>
                      <div
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          gap: u * 0.028,
                          fontSize: u * 0.05,
                          fontWeight: done ? 600 : 400,
                          color: done ? theme.canvasFg : theme.canvasMuted,
                        }}
                      >
                        <span style={{ width: icon, height: icon, flex: 'none', display: 'inline-flex' }}>
                          {done ? (
                            <PopIn delaySeconds={doneAt} overshoot>
                              <CheckMark size={icon} color={theme.accent} />
                            </PopIn>
                          ) : (
                            <Spinner size={icon} theme={theme} />
                          )}
                        </span>
                        <span>{line}</span>
                      </div>
                    </PopIn>
                  )
                })}
              </div>
              {beat.thumbnailUrl ? (
                <PopIn delaySeconds={times[0] ?? 0} style={{ width: '22%', flex: 'none' }}>
                  <Img
                    src={beat.thumbnailUrl}
                    style={{
                      width: '100%',
                      aspectRatio: '1 / 1',
                      objectFit: 'cover',
                      borderRadius: 16,
                      display: 'block',
                    }}
                  />
                </PopIn>
              ) : null}
            </div>
          </PopIn>
        </AbsoluteFill>
      </CanvasCamera>
      {compact ? null : <BrandTag theme={theme} brand={brand} />}
    </AbsoluteFill>
  )
}
