import React from 'react'
import { AbsoluteFill, Sequence, interpolate, useVideoConfig } from 'remotion'
import { Audio } from '@remotion/media'
import { SOUND, type BeatType } from '../grammar'
import { themeFromBrand } from '../theme'
import { frames } from '../motion/timing'
import { bpmFor } from '../motion/grid'
import type { AdCompositionProps } from './schema'
import type { BeatProps, RenderBeat } from './types'
import { footageWindows, voiceoverWindows } from './audio-plan'
import { Open } from './beats/Open'
import { Title } from './beats/Title'
import { Lockup } from './beats/Lockup'
import { Kinetic } from './beats/Kinetic'
import { Live } from './beats/Live'
import { Prompt } from './beats/Prompt'
import { Agent } from './beats/Agent'
import { Demo } from './beats/Demo'
import { Results } from './beats/Results'
import { Device } from './beats/Device'
import { Approve } from './beats/Approve'
import { Proof } from './beats/Proof'
import { End } from './beats/End'

const BEAT_COMPONENTS: Record<BeatType, React.FC<BeatProps>> = {
  open: Open,
  title: Title,
  lockup: Lockup,
  kinetic: Kinetic,
  live: Live,
  prompt: Prompt,
  agent: Agent,
  demo: Demo,
  results: Results,
  device: Device,
  approve: Approve,
  proof: Proof,
  end: End,
}

export const AdComposition: React.FC<AdCompositionProps> = ({ spec }) => {
  const { fps, durationInFrames } = useVideoConfig()
  const theme = themeFromBrand({ color: spec.brand.color, canvas: spec.brand.canvas })
  const brand = { name: spec.brand.name, logoUrl: spec.brand.logoUrl }
  const ducked = voiceoverWindows(spec)
  const footage = footageWindows(spec)
  const duck = Math.pow(10, -SOUND.musicDuckDb / 20)
  const underClip = Math.pow(10, -SOUND.musicUnderClipDb / 20)
  const musicVolume = (f: number) => {
    const inVoice = ducked.some((w) => f >= w.start && f <= w.end)
    const inClip = footage.some((w) => f >= w.start && f < w.end)
    const fadeOut = interpolate(
      f,
      [durationInFrames - frames(SOUND.finalFadeMs / 1000), durationInFrames],
      [1, 0],
      { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' },
    )
    return (inVoice ? duck : inClip ? underClip : 1) * fadeOut
  }
  return (
    <AbsoluteFill style={{ background: '#000' }}>
      {spec.beats.map((beat, index) => {
        const Component = BEAT_COMPONENTS[beat.type]
        const from = frames(beat.start)
        const length = frames(beat.end) - from
        return (
          <Sequence key={index} from={from} durationInFrames={length} premountFor={fps}>
            <Component
              beat={beat as RenderBeat}
              theme={theme}
              brand={brand}
              seconds={length / fps}
              bpm={bpmFor(spec.musicTempo)}
              format={spec.format ?? 'promo'}
            />
          </Sequence>
        )
      })}
      {/* A take starts on its beat but runs its own length: no durationInFrames, or a line is cut mid-word. */}
      {spec.beats.map((beat, index) =>
        beat.voiceoverUrl ? (
          <Sequence key={`vo-${index}`} from={frames(beat.start)} premountFor={fps}>
            <Audio src={beat.voiceoverUrl} />
          </Sequence>
        ) : null,
      )}
      {spec.musicUrl ? <Audio src={spec.musicUrl} volume={musicVolume} /> : null}
    </AbsoluteFill>
  )
}
