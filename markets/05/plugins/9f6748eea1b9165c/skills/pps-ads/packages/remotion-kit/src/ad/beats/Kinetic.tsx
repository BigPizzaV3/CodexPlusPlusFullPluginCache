import React from 'react'
import { AbsoluteFill } from 'remotion'
import { CanvasCamera } from '../../motion/CanvasCamera'
import { MaskReveal } from '../../motion/MaskReveal'
import { frames } from '../../motion/timing'
import { BrandTag } from '../BrandTag'
import { bricolage } from '../fonts'
import { useStage } from '../stage'
import type { BeatProps } from '../types'

/** One sentence, 3 to 7 words, revealed from the left under a pushing camera; the last word in the brand ink. */
export const Kinetic: React.FC<BeatProps> = ({ beat, theme, brand, seconds, compact }) => {
  const { u } = useStage()
  const words = (beat.text ?? '').split(/\s+/).filter(Boolean)
  return (
    <AbsoluteFill style={{ background: theme.canvasBg }}>
      <CanvasCamera beatFrames={frames(seconds)} family="type" disabled={compact}>
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', padding: '0 10%' }}>
          <MaskReveal from="left" durationMs={360}>
            <div
              style={{
                fontFamily: bricolage.fontFamily,
                fontWeight: 800,
                fontSize: u * 0.1,
                lineHeight: 1.05,
                color: theme.canvasFg,
                textAlign: 'center',
                letterSpacing: '-0.02em',
                textWrap: 'balance',
              }}
            >
              {words.map((word, i) => (
                <span key={i} style={{ color: i === words.length - 1 ? theme.accentInk : theme.canvasFg }}>
                  {word}
                  {i < words.length - 1 ? ' ' : ''}
                </span>
              ))}
            </div>
          </MaskReveal>
        </AbsoluteFill>
      </CanvasCamera>
      {compact ? null : <BrandTag theme={theme} brand={brand} />}
    </AbsoluteFill>
  )
}
