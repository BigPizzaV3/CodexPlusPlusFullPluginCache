import type { MotionKey, TrailerAudio } from './schema'

export function easing(t: number, ease: MotionKey['ease']): number {
  if (ease === 'in') return t * t * t
  if (ease === 'out') return 1 - (1 - t) ** 3
  if (ease === 'in-out') return t < 0.5 ? 4 * t ** 3 : 1 - (-2 * t + 2) ** 3 / 2
  return t
}

export function poseAt(keys: MotionKey[], frame: number): MotionKey {
  const next = keys.findIndex((key) => key.frame > frame)
  if (next === -1) return keys[keys.length - 1]
  if (next === 0) return keys[0]
  const a = keys[next - 1], b = keys[next]
  const t = easing((frame - a.frame) / (b.frame - a.frame), b.ease)
  const mix = (x: number, y: number) => x + (y - x) * t
  return { ...a, x: mix(a.x, b.x), y: mix(a.y, b.y), scale: mix(a.scale, b.scale),
    rotate: mix(a.rotate, b.rotate), opacity: mix(a.opacity, b.opacity), reveal: mix(a.reveal, b.reveal) }
}

export function audioGainAt(audio: TrailerAudio, frame: number): number {
  const fadeIn = audio.fadeInFrames ? Math.min(1, frame / audio.fadeInFrames) : 1
  const fadeOut = audio.fadeOutFrames ? Math.min(1, (audio.durationFrames - 1 - frame) / audio.fadeOutFrames) : 1
  let envelope = 1
  if (audio.gainKeys.length) {
    const next = audio.gainKeys.findIndex((k) => k.frame > frame)
    if (next === -1) envelope = audio.gainKeys[audio.gainKeys.length - 1].gain
    else if (next === 0) envelope = audio.gainKeys[0].gain
    else {
      const a = audio.gainKeys[next - 1], b = audio.gainKeys[next]
      envelope = a.gain + (b.gain - a.gain) * (frame - a.frame) / (b.frame - a.frame)
    }
  }
  return Math.max(0, audio.volume * fadeIn * fadeOut * envelope)
}
