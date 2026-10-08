import React from 'react'
import { AbsoluteFill, useCurrentFrame } from 'remotion'
import { MOTION } from '../grammar'

/** Film grain and a 2% vignette over footage beats. The noise tile shifts every frame so it never reads as a sticker. */
export const Grain: React.FC = () => {
  const frame = useCurrentFrame()
  const shift = (frame * 37) % 97
  const noise =
    "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'>" +
    "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/>" +
    // Raw fractal noise sits near 50% grey, which overlay treats as neutral (invisible). Map its alpha channel
    // to high-contrast opaque grey so the grain actually lifts and darkens the footage.
    "<feColorMatrix values='0 0 0 9 -4 0 0 0 9 -4 0 0 0 9 -4 0 0 0 0 1'/>" +
    "</filter><rect width='160' height='160' filter='url(%23n)' opacity='0.9'/></svg>\")"
  return (
    <>
      <AbsoluteFill
        style={{
          backgroundImage: noise,
          backgroundPosition: `${shift}px ${shift * 2}px`,
          opacity: MOTION.grainOpacity,
          mixBlendMode: 'overlay',
          pointerEvents: 'none',
        }}
      />
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse at center, rgba(0,0,0,0) 60%, rgba(0,0,0,${MOTION.vignette * 10}) 100%)`,
          pointerEvents: 'none',
        }}
      />
    </>
  )
}
