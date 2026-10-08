import React from 'react'
import { AbsoluteFill, useCurrentFrame } from 'remotion'
import { promptTiming } from '../../grammar'
import { CanvasCamera } from '../../motion/CanvasCamera'
import { Cursor, cursorPose, type CursorPath } from '../../motion/Cursor'
import { PopIn } from '../../motion/PopIn'
import { Typewriter } from '../../motion/Typewriter'
import { frames } from '../../motion/timing'
import { BrandTag } from '../BrandTag'
import { inter } from '../fonts'
import { CENTER_ANCHOR, ON_ACCENT, PressRing, cardStyle, cursorTip, useStage } from '../stage'
import type { BeatProps } from '../types'

const CURSOR_TRAVEL_SECONDS = 0.5

/**
 * A composer card: the prompt types itself in, the send button pops in the moment it finishes, and the
 * cursor travels in from below to press it. The timing is the grammar's `promptTiming`, the same answer the
 * storyboard note prints: a long prompt types faster than the reading pace, so the whole sentence always lands.
 */
export const Prompt: React.FC<BeatProps> = ({ beat, theme, brand, seconds, compact }) => {
  const frame = useCurrentFrame()
  const { width, height, u } = useStage()
  const text = beat.text ?? ''
  const { charsPerSecond, sendAt, pressAt } = promptTiming(seconds, text.length)
  const button = u * 0.11
  const cursorSize = u * 0.06
  const tip = cursorTip(cursorSize)
  const pressFrame = frames(pressAt)
  const path: CursorPath = {
    from: { x: width * 0.08 - tip.x, y: height * 0.3 - tip.y },
    to: { x: -tip.x, y: -tip.y },
    startFrame: pressFrame - frames(CURSOR_TRAVEL_SECONDS),
    endFrame: pressFrame,
  }
  const pressed = cursorPose(frame, path).pressed
  return (
    <AbsoluteFill style={{ background: theme.canvasBg }}>
      <CanvasCamera beatFrames={frames(seconds)} family="card" disabled={compact}>
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
          <PopIn style={{ width: '100%', display: 'flex', justifyContent: 'center' }}>
            <div style={{ ...cardStyle(theme, width, u), fontFamily: inter.fontFamily }}>
              <div
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: u * 0.018,
                  fontWeight: 600,
                  fontSize: u * 0.036,
                  color: theme.canvasFg,
                  marginBottom: u * 0.035,
                }}
              >
                <span
                  style={{
                    width: u * 0.026,
                    height: u * 0.026,
                    borderRadius: 999,
                    background: theme.accent,
                    display: 'inline-block',
                  }}
                />
                <span>{brand.name}</span>
              </div>
              <div
                style={{
                  fontWeight: 400,
                  fontSize: u * 0.056,
                  lineHeight: 1.35,
                  color: theme.canvasFg,
                  minHeight: u * 0.056 * 1.35 * 3,
                }}
              >
                <Typewriter text={text} charsPerSecond={charsPerSecond} cursorColor={theme.accent} />
              </div>
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  marginTop: u * 0.04,
                }}
              >
                <span
                  style={{
                    fontWeight: 600,
                    fontSize: u * 0.03,
                    color: theme.canvasMuted,
                    border: `1px solid ${theme.hairline}`,
                    borderRadius: 999,
                    padding: `${u * 0.012}px ${u * 0.026}px`,
                  }}
                >
                  Assistant
                </span>
                <div style={{ position: 'relative', width: button, height: button }}>
                  <PopIn delaySeconds={sendAt} overshoot>
                    <div
                      style={{
                        width: button,
                        height: button,
                        borderRadius: 999,
                        background: theme.accent,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        transform: `scale(${pressed ? 0.92 : 1})`,
                      }}
                    >
                      <svg width={button * 0.45} height={button * 0.45} viewBox="0 0 24 24">
                        <path
                          d="M12 19V5M5 12l7-7 7 7"
                          fill="none"
                          stroke={ON_ACCENT}
                          strokeWidth="2.6"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        />
                      </svg>
                    </div>
                  </PopIn>
                  <div style={CENTER_ANCHOR}>
                    <PressRing pressFrame={pressFrame} size={button * 1.3} color={theme.accent} />
                    <Cursor path={path} size={cursorSize} />
                  </div>
                </div>
              </div>
            </div>
          </PopIn>
        </AbsoluteFill>
      </CanvasCamera>
      {compact ? null : <BrandTag theme={theme} brand={brand} />}
    </AbsoluteFill>
  )
}
