import React from 'react'
import { AbsoluteFill, useCurrentFrame } from 'remotion'
import { CanvasCamera } from '../../motion/CanvasCamera'
import { Cursor, cursorPose, type CursorPath } from '../../motion/Cursor'
import { PopIn } from '../../motion/PopIn'
import { FPS, frames } from '../../motion/timing'
import { BrandTag } from '../BrandTag'
import { inter } from '../fonts'
import { CENTER_ANCHOR, ON_ACCENT, PressRing, cursorTip, useStage } from '../stage'
import type { BeatProps } from '../types'

const CURSOR_START_SECONDS = 0.5
const CURSOR_TRAVEL_SECONDS = 0.7

/** The approval moment: a sublabel, Decline and Approve, the cursor travels in and presses Approve, a check lands. */
export const Approve: React.FC<BeatProps> = ({ beat, theme, brand, seconds, compact }) => {
  const frame = useCurrentFrame()
  const { width, height, u } = useStage()
  const cursorSize = u * 0.06
  const tip = cursorTip(cursorSize)
  const startFrame = frames(CURSOR_START_SECONDS)
  const pressFrame = Math.min(startFrame + frames(CURSOR_TRAVEL_SECONDS), frames(seconds) - frames(0.5))
  const path: CursorPath = {
    from: { x: -width * 0.55 - tip.x, y: height * 0.35 - tip.y },
    to: { x: -tip.x, y: -tip.y },
    startFrame,
    endFrame: pressFrame,
  }
  const pressed = cursorPose(frame, path).pressed
  const fontSize = u * 0.05
  const pill: React.CSSProperties = {
    fontFamily: inter.fontFamily,
    fontSize,
    borderRadius: 999,
    padding: `${fontSize * 0.6}px ${fontSize * 1.4}px`,
    whiteSpace: 'nowrap',
  }
  const check = fontSize * 1.5
  return (
    <AbsoluteFill style={{ background: theme.canvasBg }}>
      <CanvasCamera beatFrames={frames(seconds)} family="card" disabled={compact}>
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', padding: '0 8%' }}>
          {beat.subtitle ? (
            <PopIn>
              <div
                style={{
                  fontFamily: inter.fontFamily,
                  fontWeight: 600,
                  fontSize: u * 0.044,
                  color: theme.canvasMuted,
                  textAlign: 'center',
                  marginBottom: u * 0.05,
                }}
              >
                {beat.subtitle}
              </div>
            </PopIn>
          ) : null}
          <div style={{ display: 'flex', alignItems: 'center', gap: u * 0.03 }}>
            <PopIn delaySeconds={0.1}>
              <div style={{ ...pill, fontWeight: 600, color: theme.canvasFg, border: `2px solid ${theme.hairline}` }}>
                Decline
              </div>
            </PopIn>
            <div style={{ position: 'relative' }}>
              <PopIn delaySeconds={0.2}>
                <div
                  style={{
                    ...pill,
                    fontWeight: 700,
                    color: ON_ACCENT,
                    background: theme.accent,
                    border: `2px solid ${theme.accent}`,
                    transform: `scale(${pressed ? 0.96 : 1})`,
                  }}
                >
                  {beat.text ?? 'Approve'}
                </div>
              </PopIn>
              <div style={{ position: 'absolute', left: '100%', top: '50%', marginLeft: u * 0.025 }}>
                <PopIn delaySeconds={pressFrame / FPS + 0.12} overshoot style={{ marginTop: -check / 2 }}>
                  <svg width={check} height={check} viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="11" fill={theme.accent} />
                    <path
                      d="M7 12.5l3.2 3.2L17 9"
                      fill="none"
                      stroke={ON_ACCENT}
                      strokeWidth="2.6"
                      strokeLinecap="round"
                    />
                  </svg>
                </PopIn>
              </div>
              <div style={CENTER_ANCHOR}>
                <PressRing pressFrame={pressFrame} size={fontSize * 3} color={theme.accent} />
                <Cursor path={path} size={cursorSize} />
              </div>
            </div>
          </div>
        </AbsoluteFill>
      </CanvasCamera>
      {compact ? null : <BrandTag theme={theme} brand={brand} />}
    </AbsoluteFill>
  )
}
