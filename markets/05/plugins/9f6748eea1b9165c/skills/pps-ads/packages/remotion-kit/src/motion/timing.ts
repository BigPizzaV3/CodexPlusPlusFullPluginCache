import type { AdAspectRatio } from '../grammar'

export const FPS = 30

export function frames(seconds: number): number {
  return Math.round(seconds * FPS)
}

export function sizeFor(aspectRatio: AdAspectRatio): { width: number; height: number } {
  // 9:16 and 16:9 only: a PPS project is never square, so neither is an ad (grammar ASPECT_RATIOS).
  if (aspectRatio === '16:9') return { width: 1920, height: 1080 }
  return { width: 1080, height: 1920 }
}
