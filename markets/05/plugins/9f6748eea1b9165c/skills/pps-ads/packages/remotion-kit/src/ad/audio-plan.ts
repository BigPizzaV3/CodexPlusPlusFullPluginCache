import { clipSecondsFor } from '../grammar'
import { frames } from '../motion/timing'

/** The fields the timing plan reads off a beat; kept import-free of React so the unit tests can load it. */
interface TimedBeat {
  start: number
  end: number
  clipUrl?: string
  voiceoverUrl?: string
  voiceoverSeconds?: number
}

export interface FrameWindow {
  start: number
  end: number
}

/**
 * Where the music ducks under voiceover, in frames. A take starts on its beat but is not cut at the
 * beat's end: it plays for its own length (`voiceoverSeconds`, filled server-side from the take), or,
 * when that length is unknown, to the end of the ad, so the duck never lifts mid-sentence.
 */
export function voiceoverWindows(spec: { lengthSeconds: number; beats: TimedBeat[] }): FrameWindow[] {
  const last = frames(spec.lengthSeconds)
  return spec.beats
    .filter((beat) => beat.voiceoverUrl)
    .map((beat) => {
      const seconds = beat.voiceoverSeconds ?? spec.lengthSeconds - beat.start
      return { start: frames(beat.start), end: Math.min(last, frames(beat.start + seconds)) }
    })
}

/** Where a footage clip plays with its own sound, in frames: the music sits lower there. */
export function footageWindows(spec: { beats: TimedBeat[] }): FrameWindow[] {
  return spec.beats
    .filter((beat) => beat.clipUrl)
    .map((beat) => ({ start: frames(beat.start), end: frames(beat.end) }))
}

/**
 * Frames to skip at the head of a footage clip. A clip is generated at clipSecondsFor(beat) seconds,
 * longer than its beat, and its action peaks at the end, so the beat plays the clip's LAST seconds.
 */
export function clipTrimFrames(beatSeconds: number): number {
  return frames(clipSecondsFor(beatSeconds) - beatSeconds)
}
