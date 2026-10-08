import React from 'react'
import { interpolate, useCurrentFrame } from 'remotion'
import { MOTION } from '../grammar'
import { FPS } from './timing'

/** String slicing, never per-character opacity (Remotion rule). Cursor blinks at 2 Hz after the text lands. */
export const Typewriter: React.FC<{
  text: string
  charsPerSecond?: number
  style?: React.CSSProperties
  cursorColor: string
}> = ({ text, charsPerSecond = MOTION.typewriterCharsPerSecond, style, cursorColor }) => {
  const frame = useCurrentFrame()
  const typed = Math.min(text.length, Math.floor((frame / FPS) * charsPerSecond))
  const blink = interpolate(frame % 16, [0, 8, 16], [1, 0, 1])
  return (
    <span style={style}>
      {text.slice(0, typed)}
      <span
        style={{
          display: 'inline-block',
          width: '0.08em',
          height: '1em',
          verticalAlign: '-0.12em',
          marginLeft: 2,
          background: cursorColor,
          opacity: blink,
        }}
      />
    </span>
  )
}
