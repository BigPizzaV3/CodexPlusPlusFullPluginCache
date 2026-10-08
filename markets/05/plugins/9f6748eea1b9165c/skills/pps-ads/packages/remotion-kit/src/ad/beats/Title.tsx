import React from 'react'
import { AbsoluteFill } from 'remotion'
import { CanvasCamera } from '../../motion/CanvasCamera'
import { MaskReveal } from '../../motion/MaskReveal'
import { PopIn } from '../../motion/PopIn'
import { frames } from '../../motion/timing'
import { BrandTag } from '../BrandTag'
import { bricolage, inter } from '../fonts'
import { ON_ACCENT, useStage } from '../stage'
import type { BeatProps } from '../types'

/**
 * The big typographic card: a kicker, the headline revealed from below with a color block behind the last
 * word, an optional partner lockup. Each word is one unbreakable span, so a line only breaks between words.
 */
export const Title: React.FC<BeatProps> = ({ beat, theme, brand, seconds, compact }) => {
  const { width, height, u } = useStage()
  const words = (beat.text ?? '').split(/\s+/).filter(Boolean)
  const headline = Math.min(width * 0.11, height * 0.13)
  return (
    <AbsoluteFill style={{ background: theme.canvasBg }}>
      <CanvasCamera beatFrames={frames(seconds)} family="type" disabled={compact}>
        <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', padding: '0 6%' }}>
          {beat.kicker ? (
            <PopIn>
              <div
                style={{
                  fontFamily: inter.fontFamily,
                  fontWeight: 600,
                  fontSize: u * 0.03,
                  color: theme.canvasMuted,
                  letterSpacing: '0.14em',
                  textTransform: 'uppercase',
                  marginBottom: u * 0.04,
                  textAlign: 'center',
                }}
              >
                {beat.kicker}
              </div>
            </PopIn>
          ) : null}
          <MaskReveal from="bottom" delaySeconds={0.1} style={{ marginBottom: -headline * 0.2 }}>
            <div
              style={{
                fontFamily: bricolage.fontFamily,
                fontWeight: 800,
                fontSize: headline,
                lineHeight: 1.0,
                color: theme.canvasFg,
                textAlign: 'center',
                letterSpacing: '-0.025em',
                textWrap: 'balance',
                // The reveal clips to this box, and the color block reaches past the last word on the right and
                // below the baseline: pad the box to hold it (the reveal's negative margin gives the height back).
                padding: '0.04em 0.06em 0.2em',
              }}
            >
              {words.map((word, w) => {
                const last = w === words.length - 1
                return (
                  <React.Fragment key={w}>
                    <span
                      style={{
                        display: 'inline-block',
                        whiteSpace: 'nowrap',
                        position: 'relative',
                        padding: last ? '0 0.14em' : 0,
                      }}
                    >
                      {last ? (
                        <span
                          style={{
                            position: 'absolute',
                            // Down past the baseline so a descender (y, g, p) sits on the block, not below it.
                            inset: '0.04em -0.04em -0.14em -0.04em',
                            background: theme.accent,
                            borderRadius: '0.12em',
                            zIndex: 0,
                          }}
                        />
                      ) : null}
                      <span style={{ position: 'relative', zIndex: 1, color: last ? ON_ACCENT : theme.canvasFg }}>
                        {word}
                      </span>
                    </span>
                    {last ? null : ' '}
                  </React.Fragment>
                )
              })}
            </div>
          </MaskReveal>
          {beat.partner ? (
            <PopIn delaySeconds={0.5}>
              <div
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: u * 0.02,
                  marginTop: u * 0.05,
                  fontFamily: inter.fontFamily,
                  fontWeight: 600,
                  fontSize: u * 0.034,
                  color: theme.canvasMuted,
                }}
              >
                <span>{brand.name}</span>
                <span style={{ color: theme.accentInk }}>x</span>
                <span>{beat.partner}</span>
              </div>
            </PopIn>
          ) : null}
        </AbsoluteFill>
      </CanvasCamera>
      {compact ? null : <BrandTag theme={theme} brand={brand} />}
    </AbsoluteFill>
  )
}
