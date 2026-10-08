import React from 'react'
import { AbsoluteFill, Easing, Img, interpolate, useCurrentFrame } from 'remotion'
import { Video } from '@remotion/media'
import { CanvasCamera } from '../../motion/CanvasCamera'
import { Cursor, type CursorPath } from '../../motion/Cursor'
import { PopIn } from '../../motion/PopIn'
import { staggerOnGrid } from '../../motion/grid'
import { frames } from '../../motion/timing'
import { MOTION } from '../../grammar'
import { BrandTag } from '../BrandTag'
import { PressRing, cursorTip, useStage } from '../stage'
import type { BeatProps } from '../types'

const POP_SECONDS = 0.28
const CURSOR_TRAVEL_SECONDS = 0.6
const PRESS_BEFORE_END_SECONDS = 0.5

export interface TileBox {
  x: number
  y: number
  size: number
}

/**
 * Where each square tile sits on the stage: 2 columns up to 4 tiles, 3 above, 84% of the width with a 2%
 * gap, shrunk to fit 78% of the height on a wide canvas, centered. The cursor aims at these same boxes.
 */
export function tileLayout(count: number, width: number, height: number): TileBox[] {
  const cols = count <= 4 ? 2 : 3
  const rows = Math.max(1, Math.ceil(count / cols))
  const gap = width * 0.02
  const size = Math.min((width * 0.84 - gap * (cols - 1)) / cols, (height * 0.78 - gap * (rows - 1)) / rows)
  const gridW = cols * size + gap * (cols - 1)
  const gridH = rows * size + gap * (rows - 1)
  const left = (width - gridW) / 2
  const top = (height - gridH) / 2
  return Array.from({ length: count }, (_, i) => ({
    x: left + (i % cols) * (size + gap),
    y: top + Math.floor(i / cols) * (size + gap),
    size,
  }))
}

type Tile = { kind: 'image'; url: string } | { kind: 'clip'; url: string }

/** 3 to 6 results land tile by tile on the music grid, then the cursor picks one and it lifts. */
export const Results: React.FC<BeatProps> = ({ beat, theme, brand, seconds, bpm, compact }) => {
  const frame = useCurrentFrame()
  const { width, height, u } = useStage()
  const tiles: Tile[] = [
    ...(beat.imageUrls ?? []).map((url): Tile => ({ kind: 'image', url })),
    ...(beat.clipUrls ?? []).map((url): Tile => ({ kind: 'clip', url })),
  ]
  const boxes = tileLayout(tiles.length, width, height)
  const times = staggerOnGrid(tiles.length, bpm)
  const pick = Math.min(Math.max(0, beat.pickIndex ?? 0), Math.max(0, tiles.length - 1))
  const landed = frames((times[times.length - 1] ?? 0) + POP_SECONDS + 0.1)
  const cursorSize = u * 0.06
  const tip = cursorTip(cursorSize)
  const pressFrame = Math.min(landed + frames(CURSOR_TRAVEL_SECONDS), frames(seconds - PRESS_BEFORE_END_SECONDS))
  const target = boxes[pick]
  const center = target
    ? { x: target.x + target.size / 2, y: target.y + target.size / 2 }
    : { x: width / 2, y: height / 2 }
  const path: CursorPath = {
    from: { x: width * 0.62 - tip.x, y: height - tip.y },
    to: { x: center.x - tip.x, y: center.y - tip.y },
    startFrame: pressFrame - frames(CURSOR_TRAVEL_SECONDS),
    endFrame: pressFrame,
  }
  const after = interpolate(frame, [pressFrame, pressFrame + frames(POP_SECONDS)], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  })
  const radius = Math.max(12, width * 0.018)
  const ring = Math.max(4, u * 0.006)
  return (
    <AbsoluteFill style={{ background: theme.canvasBg }}>
      <CanvasCamera beatFrames={frames(seconds)} family="card" disabled={compact}>
        {tiles.map((tile, i) => {
          const box = boxes[i]
          const picked = i === pick
          const lift = picked ? 1 + (MOTION.overshootMax - 1) * after : 1
          return (
            <div
              key={i}
              style={{
                position: 'absolute',
                left: box.x,
                top: box.y,
                width: box.size,
                height: box.size,
                transform: `scale(${lift})`,
                opacity: picked ? 1 : 1 - 0.15 * after,
                zIndex: picked ? 2 : 1,
              }}
            >
              <PopIn delaySeconds={times[i]} durationMs={POP_SECONDS * 1000} style={{ width: '100%', height: '100%' }}>
                <div
                  style={{
                    width: '100%',
                    height: '100%',
                    borderRadius: radius,
                    overflow: 'hidden',
                    background: theme.surface,
                    border: `1px solid ${theme.hairline}`,
                    boxShadow: picked
                      ? `0 0 0 ${ring * after}px ${theme.accent}, 0 16px 40px rgba(0,0,0,${0.12 + 0.1 * after})`
                      : '0 10px 30px rgba(0,0,0,0.12)',
                    boxSizing: 'border-box',
                  }}
                >
                  {tile.kind === 'image' ? (
                    <Img src={tile.url} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                  ) : (
                    // A tile is a picture of a clip: the ad's sound is the music, voiceover and footage beats.
                    <Video src={tile.url} muted loop objectFit="cover" style={{ width: '100%', height: '100%' }} />
                  )}
                </div>
              </PopIn>
            </div>
          )
        })}
        <div style={{ position: 'absolute', left: center.x, top: center.y, width: 0, height: 0, zIndex: 3 }}>
          <PressRing pressFrame={pressFrame} size={cursorSize * 1.6} color={theme.accent} />
        </div>
        <AbsoluteFill style={{ zIndex: 4, pointerEvents: 'none' }}>
          <Cursor path={path} size={cursorSize} />
        </AbsoluteFill>
      </CanvasCamera>
      {compact ? null : <BrandTag theme={theme} brand={brand} />}
    </AbsoluteFill>
  )
}
