import React from 'react'
import { AbsoluteFill } from 'remotion'
import { CanvasCamera } from '../../motion/CanvasCamera'
import { CountUp } from '../../motion/CountUp'
import { MaskReveal } from '../../motion/MaskReveal'
import { PopIn } from '../../motion/PopIn'
import { frames } from '../../motion/timing'
import { BrandTag } from '../BrandTag'
import { bricolage, inter } from '../fonts'
import { useStage } from '../stage'
import type { BeatProps } from '../types'

/** A quote or a number in big type, its source small. `text` may be "line | source"; a number counts up. */
export const Proof: React.FC<BeatProps> = ({ beat, theme, brand, seconds, compact }) => {
  const { u } = useStage()
  const [line, source] = (beat.text ?? '').split('|').map((part) => part.trim())
  return (
    <AbsoluteFill style={{ background: theme.canvasBg }}>
      <CanvasCamera beatFrames={frames(seconds)} family="type" disabled={compact}>
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', padding: '0 10%' }}>
          <MaskReveal from="bottom">
            <div
              style={{
                fontFamily: bricolage.fontFamily,
                fontWeight: 800,
                fontSize: u * 0.11,
                color: theme.accentInk,
                textAlign: 'center',
                lineHeight: 1.05,
                fontVariantNumeric: 'tabular-nums',
              }}
            >
              <CountUp text={line ?? ''} />
            </div>
          </MaskReveal>
          {source ? (
            <PopIn delaySeconds={0.4}>
              <div
                style={{
                  fontFamily: inter.fontFamily,
                  fontWeight: 400,
                  fontSize: u * 0.036,
                  color: theme.canvasMuted,
                  textAlign: 'center',
                  marginTop: u * 0.03,
                }}
              >
                {source}
              </div>
            </PopIn>
          ) : null}
        </AbsoluteFill>
      </CanvasCamera>
      {compact ? null : <BrandTag theme={theme} brand={brand} />}
    </AbsoluteFill>
  )
}
