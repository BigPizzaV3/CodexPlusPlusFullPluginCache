import React from 'react'
import { AbsoluteFill, Easing, interpolate, useCurrentFrame } from 'remotion'
import { CanvasCamera } from '../../motion/CanvasCamera'
import { PopIn } from '../../motion/PopIn'
import { frames } from '../../motion/timing'
import { BrandTag } from '../BrandTag'
import { StageProvider, useStage } from '../stage'
import type { BeatProps, RenderBeat } from '../types'
import { Agent } from './Agent'
import { Prompt } from './Prompt'
import { Results } from './Results'

const BEZEL_COLOR = '#0b0b0d'
const PHONE_RADIUS = 56
const LAPTOP_BEZEL = 24
const TILT_SECONDS = 0.6

const INNER = { prompt: Prompt, agent: Agent, results: Results } as const

/** What the screen shows: the beat's own `inner`, else whatever content the beat carries. */
export function innerFor(beat: RenderBeat): keyof typeof INNER {
  if (beat.inner) return beat.inner
  if (beat.imageUrls?.length || beat.clipUrls?.length) return 'results'
  if (beat.lines?.length) return 'agent'
  return 'prompt'
}

interface Screen {
  width: number
  height: number
  bezel: number
}

/** The screen box on the stage: a 9:16 phone up to 80% of the width, or a 16:9 laptop lid; both fit the height. */
export function screenFor(frame: 'phone' | 'laptop', width: number, height: number): Screen {
  if (frame === 'phone') {
    const bezel = Math.max(12, width * 0.016)
    const screenW = Math.min(width * 0.8 - 2 * bezel, ((height * 0.82 - 2 * bezel) * 9) / 16)
    return { width: screenW, height: (screenW * 16) / 9, bezel }
  }
  const screenW = Math.min(width * 0.8 - 2 * LAPTOP_BEZEL, ((height * 0.68 - 2 * LAPTOP_BEZEL) * 16) / 9)
  return { width: screenW, height: (screenW * 9) / 16, bezel: LAPTOP_BEZEL }
}

/**
 * The interface inside hardware: the inner beat renders at a virtual stage with the screen's shape and is
 * scaled into the screen, so its type and its cursor targets keep their proportions. The device settles
 * from a slight tilt to square over the first 0.6 s.
 */
export const Device: React.FC<BeatProps> = (props) => {
  const { beat, theme, brand, seconds, compact } = props
  const now = useCurrentFrame()
  const { width, height } = useStage()
  const frame = beat.frame ?? (width < height ? 'phone' : 'laptop')
  const screen = screenFor(frame, width, height)
  const virtual = { width, height: (width * screen.height) / screen.width }
  const scale = screen.width / virtual.width
  const Inner = INNER[innerFor(beat)]
  const settle = interpolate(now, [0, frames(TILT_SECONDS)], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  })
  // Once square, no transform at all: a resting 3D context keeps the screen on its own layer, softening its type.
  const tilt = settle >= 1 ? 'none' : `rotateY(${-6 * (1 - settle)}deg) rotateX(${2 * (1 - settle)}deg)`
  const screenRadius = Math.max(6, (frame === 'phone' ? PHONE_RADIUS : 20) - screen.bezel)
  const outerW = screen.width + 2 * screen.bezel
  const outerH = screen.height + 2 * screen.bezel
  const phone = frame === 'phone'
  const outerRadius = phone ? PHONE_RADIUS : 20
  const screenEl = (
    <div
      style={{
        position: 'absolute',
        left: screen.bezel,
        top: screen.bezel,
        width: screen.width,
        height: screen.height,
        borderRadius: screenRadius,
        overflow: 'hidden',
        // overflow alone does not clip a scaled child to the rounded corners in every compositor; the clip-path does.
        clipPath: `inset(0 round ${screenRadius}px)`,
        background: theme.canvasBg,
      }}
    >
      <div
        style={{
          position: 'absolute',
          left: 0,
          top: 0,
          width: virtual.width,
          height: virtual.height,
          transform: `scale(${scale})`,
          transformOrigin: '0 0',
        }}
      >
        <StageProvider size={virtual}>
          <Inner {...props} compact />
        </StageProvider>
      </div>
    </div>
  )
  return (
    <AbsoluteFill style={{ background: theme.canvasBg }}>
      <CanvasCamera beatFrames={frames(seconds)} family="device" disabled={compact}>
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', perspective: '1400px' }}>
          <PopIn>
            <div style={{ transform: tilt, display: 'flex', flexDirection: 'column' }}>
              <div
                style={{
                  position: 'relative',
                  width: outerW,
                  height: outerH,
                  background: BEZEL_COLOR,
                  borderRadius: outerRadius,
                  boxShadow: '0 40px 90px rgba(0,0,0,0.28), 0 10px 24px rgba(0,0,0,0.18)',
                }}
              >
                {screenEl}
                {phone ? (
                  <div
                    style={{
                      position: 'absolute',
                      left: '50%',
                      top: screen.bezel + screen.height * 0.014,
                      width: screen.width * 0.28,
                      height: screen.width * 0.06,
                      marginLeft: -screen.width * 0.14,
                      borderRadius: 999,
                      background: BEZEL_COLOR,
                    }}
                  />
                ) : null}
              </div>
              {phone ? null : (
                <div
                  style={{
                    alignSelf: 'center',
                    width: outerW * 1.14,
                    height: Math.max(14, outerW * 0.022),
                    borderRadius: `0 0 ${outerW * 0.02}px ${outerW * 0.02}px`,
                    background: 'linear-gradient(180deg, #3a3a3f 0%, #1c1c20 100%)',
                    boxShadow: '0 24px 50px rgba(0,0,0,0.25)',
                  }}
                />
              )}
            </div>
          </PopIn>
        </AbsoluteFill>
      </CanvasCamera>
      {compact ? null : <BrandTag theme={theme} brand={brand} />}
    </AbsoluteFill>
  )
}
