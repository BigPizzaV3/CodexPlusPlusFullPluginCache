import type { AdTheme } from '../theme'
import type { AdFormat, BeatType } from '../grammar'

export interface RenderCaptionGroup {
  text: string
  start: number
  end: number
  words: Array<{ text: string; start: number; end: number }>
}

/** The spec's beat, as the composition receives it: ids already swapped for URLs by the worker. */
export interface RenderBeat {
  type: BeatType
  start: number
  end: number
  text?: string
  subtitle?: string
  kicker?: string
  partner?: string
  lines?: string[]
  punchline?: boolean
  clipUrl?: string
  clipUrls?: string[]
  imageUrls?: string[]
  thumbnailUrl?: string
  pickIndex?: number
  frame?: 'phone' | 'laptop'
  inner?: 'prompt' | 'agent' | 'results'
  captions?: boolean
  captionAccent?: string[]
  captionGroups?: RenderCaptionGroup[]
  voiceoverUrl?: string
  voiceoverSeconds?: number
}

export interface BeatProps {
  beat: RenderBeat
  theme: AdTheme
  brand: { name: string; logoUrl?: string }
  seconds: number
  bpm: number
  format: AdFormat
  /** True when the beat renders inside a device frame (Task 7): smaller chrome, no full-bleed effects. */
  compact?: boolean
}
