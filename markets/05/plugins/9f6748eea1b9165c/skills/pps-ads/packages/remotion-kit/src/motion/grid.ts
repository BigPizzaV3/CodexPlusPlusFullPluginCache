import { MOTION, MUSIC_BPM, type MusicTempo } from '../grammar'

export function bpmFor(tempo: MusicTempo | undefined): number {
  return MUSIC_BPM[tempo ?? 'mid']
}

/** An eighth note: half a beat. Canvas entrances land on this grid. */
export function gridSeconds(bpm: number): number {
  return 60 / bpm / 2
}

export function quantizeToGrid(seconds: number, bpm: number): number {
  const grid = gridSeconds(bpm)
  return Math.round(seconds / grid) * grid
}

/**
 * n entrance times. Canvas-beat entrances land on the grid (the first is quantized, so 0 stays 0); the tiles inside
 * a beat then follow at the tile rate (tileStaggerMs), not a whole grid step, which would be 2 to 4 times too slow.
 */
export function staggerOnGrid(count: number, bpm: number): number[] {
  const first = quantizeToGrid(0, bpm)
  const gap = MOTION.tileStaggerMs / 1000
  return Array.from({ length: count }, (_, i) => Number((first + i * gap).toFixed(6)))
}
