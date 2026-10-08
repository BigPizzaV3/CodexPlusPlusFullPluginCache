import React from 'react'
import { AbsoluteFill, useVideoConfig } from 'remotion'
import { Video } from '@remotion/media'
import { SOUND } from '../../grammar'
import { Grain } from '../../motion/Grain'
import { SlideFade } from '../../motion/SlideFade'
import { inter } from '../fonts'
import { clipTrimFrames } from '../audio-plan'
import { BrandTag } from '../BrandTag'
import { Captions } from '../Captions'
import { Grade } from '../Grade'
import type { BeatProps } from '../types'

/** A looping action under a small all-caps CTA, the brand tag bottom-left (the reference end cards). */
export const End: React.FC<BeatProps> = ({ beat, theme, brand, seconds }) => {
  const { width } = useVideoConfig()
  return (
    <AbsoluteFill style={{ background: '#000' }}>
      <Grade theme={theme}>
        {beat.clipUrl ? (
          <Video
            src={beat.clipUrl}
            volume={SOUND.clipVolume}
            loop
            trimBefore={clipTrimFrames(seconds)}
            objectFit="cover"
            style={{ width: '100%', height: '100%' }}
          />
        ) : null}
      </Grade>
      <AbsoluteFill style={{ background: 'linear-gradient(180deg, rgba(0,0,0,0) 55%, rgba(0,0,0,0.55) 100%)' }} />
      <Grain />
      {beat.captionGroups?.length ? (
        <Captions groups={beat.captionGroups} accents={beat.captionAccent} theme={theme} />
      ) : null}
      <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
        <SlideFade from="up" distancePx={24} durationMs={360}>
          <div
            style={{
              fontFamily: inter.fontFamily,
              fontWeight: 600,
              fontSize: width * 0.028,
              letterSpacing: '0.12em',
              color: theme.footageFg,
              textTransform: 'uppercase',
              textAlign: 'center',
              padding: '0 10%',
            }}
          >
            {beat.text}
          </div>
        </SlideFade>
      </AbsoluteFill>
      <BrandTag theme={theme} brand={brand} onFootage />
    </AbsoluteFill>
  )
}
