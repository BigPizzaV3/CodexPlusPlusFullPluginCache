import React from 'react'
import { AbsoluteFill, Sequence, useCurrentFrame, useVideoConfig } from 'remotion'
import { MOTION } from '../grammar'
import { PopIn } from '../motion/PopIn'
import { FPS } from '../motion/timing'
import { inter } from './fonts'
import type { AdTheme } from '../theme'

export interface CaptionGroupLike {
  text: string
  start: number
  end: number
}

const HOLD_SECONDS = 0.3

/** The group under the playhead; a group holds HOLD_SECONDS past its end so a pause does not blink the text. */
export function activeCaptionGroup<T extends CaptionGroupLike>(groups: readonly T[], seconds: number): T | undefined {
  for (let i = groups.length - 1; i >= 0; i -= 1) {
    const g = groups[i]
    if (seconds >= g.start && seconds <= g.end + HOLD_SECONDS) return g
  }
  return undefined
}

function normalizeWord(word: string): string {
  return word
    .normalize('NFC')
    .replace(/[’‘]/g, "'")
    .toLowerCase()
    .replace(/[^\p{L}\p{N}']/gu, '')
}

export function splitAccent(text: string, accents: readonly string[] = []): Array<{ word: string; accent: boolean }> {
  const wanted = new Set(accents.map(normalizeWord))
  return text
    .split(/\s+/)
    .filter(Boolean)
    .map((word) => ({ word, accent: wanted.has(normalizeWord(word)) }))
}

interface CaptionsProps {
  groups: readonly CaptionGroupLike[]
  accents?: readonly string[]
  theme: AdTheme
}

/** The references' captions: 2 to 4 bold words low in frame, keywords in the brand color, each page popping in. */
export const Captions: React.FC<CaptionsProps> = ({ groups, accents, theme }) => {
  const frame = useCurrentFrame()
  const { width, height } = useVideoConfig()
  const u = Math.min(width, height)
  const group = activeCaptionGroup(groups, frame / FPS)
  if (!group) return null
  const textStyle: React.CSSProperties = {
    fontFamily: inter.fontFamily,
    fontWeight: 700,
    fontSize: u * 0.075,
    lineHeight: 1.1,
    color: theme.footageFg,
    textAlign: 'center',
    textShadow: '0 2px 10px rgba(0,0,0,0.7), 0 0 2px rgba(0,0,0,0.6)',
    padding: `0 ${u * 0.08}px`,
    textWrap: 'balance',
    letterSpacing: '-0.01em',
  }
  return (
    <AbsoluteFill
      style={{ justifyContent: 'flex-end', alignItems: 'center', paddingBottom: height * 0.18, pointerEvents: 'none' }}
    >
      <Sequence key={group.start} from={Math.round(group.start * FPS)} layout="none">
        <PopIn durationMs={220} fromScale={MOTION.captionScaleFrom} style={{ width: '100%' }}>
          <div style={textStyle}>
            {splitAccent(group.text, accents).map((part, i, parts) => (
              <React.Fragment key={i}>
                <span style={{ color: part.accent ? theme.accent : theme.footageFg }}>{part.word}</span>
                {i < parts.length - 1 ? ' ' : null}
              </React.Fragment>
            ))}
          </div>
        </PopIn>
      </Sequence>
    </AbsoluteFill>
  )
}
