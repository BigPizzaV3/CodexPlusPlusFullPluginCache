import React from 'react'
import { AbsoluteFill, useVideoConfig } from 'remotion'
import { Video } from '@remotion/media'
import { SOUND } from '../../grammar'
import { Grain } from '../../motion/Grain'
import { SlideFade } from '../../motion/SlideFade'
import { inter } from '../fonts'
import { clipTrimFrames } from '../audio-plan'
import { Captions } from '../Captions'
import { Grade } from '../Grade'
import type { BeatProps } from '../types'

/** A generated clip under the grade and grain; word-timed captions when the voiceover has them, else a subtitle. */
export const Live: React.FC<BeatProps> = ({ beat, theme, seconds }) => {
  const { width } = useVideoConfig()
  return (
    <AbsoluteFill style={{ background: '#000' }}>
      <Grade theme={theme}>
        {beat.clipUrl ? (
          <Video
            src={beat.clipUrl}
            volume={SOUND.clipVolume}
            trimBefore={clipTrimFrames(seconds)}
            objectFit="cover"
            style={{ width: '100%', height: '100%' }}
          />
        ) : null}
      </Grade>
      <Grain />
      {beat.captionGroups?.length ? (
        <Captions groups={beat.captionGroups} accents={beat.captionAccent} theme={theme} />
      ) : beat.subtitle ? (
        <AbsoluteFill style={{ justifyContent: 'flex-end', alignItems: 'center', paddingBottom: width * 0.12 }}>
          <SlideFade from="up" distancePx={20}>
            <div
              style={{
                fontFamily: inter.fontFamily,
                fontWeight: 600,
                fontSize: width * 0.034,
                color: theme.footageFg,
                textShadow: '0 2px 12px rgba(0,0,0,0.6)',
                textAlign: 'center',
                padding: '0 8%',
              }}
            >
              {beat.subtitle}
            </div>
          </SlideFade>
        </AbsoluteFill>
      ) : null}
    </AbsoluteFill>
  )
}
