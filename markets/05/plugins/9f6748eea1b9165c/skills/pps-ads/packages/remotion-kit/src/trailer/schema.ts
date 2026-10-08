import { z } from 'zod'

export const TRAILER_FPS = 30
export const TRAILER_COMPOSITION_ID = 'TrailerComposition'
export function createTrailerSchemas(z: typeof import('zod').z) {
  const frame = z.number().int().min(0).max(1800)
  const id = z.string().trim().min(1).max(64)
  const color = z.string().regex(/^#[0-9a-fA-F]{6}$/)
  const MOTION_KEY = z.object({
    frame,
    x: z.number().min(-200).max(200).default(0),
    y: z.number().min(-200).max(200).default(0),
    scale: z.number().min(0.01).max(10).default(1),
    rotate: z.number().min(-720).max(720).default(0),
    opacity: z.number().min(0).max(1).default(1),
    reveal: z.number().min(0).max(1).default(1),
    ease: z.enum(['linear', 'in', 'out', 'in-out']).default('out'),
  }).strict()
  const TRAILER_LAYER = z.object({
    kind: z.enum(['text', 'rect', 'ellipse', 'cursor', 'image', 'video']),
    startFrame: frame,
    durationFrames: frame.min(1),
    // Percent of the composition's width/height, top-left anchored. Order is back to front.
    x: z.number().min(-100).max(100).default(0),
    y: z.number().min(-100).max(100).default(0),
    width: z.number().positive().max(200).default(100),
    height: z.number().positive().max(200).default(100),
    text: z.string().min(1).max(600).optional(),
    color: color.default('#ffffff'),
    background: color.optional(),
    font: z.enum(['display', 'sans', 'mono']).default('sans'),
    fontSize: z.number().min(0.5).max(30).default(5),
    weight: z.enum(['400', '600', '700', '800']).default('700'),
    align: z.enum(['left', 'center', 'right']).default('left'),
    radius: z.number().min(0).max(100).default(0),
    borderWidth: z.number().min(0).max(20).default(0),
    borderColor: color.default('#ffffff'),
    fit: z.enum(['cover', 'contain']).default('cover'),
    imageId: id.optional(),
    videoId: id.optional(),
    trimStartFrame: frame.default(0),
    volume: z.number().min(0).max(1).default(1),
    // Local frames. x/y are offsets in canvas percentages; ease belongs to the destination key.
    keys: z.array(MOTION_KEY).min(1).max(16).default([{ frame: 0, x: 0, y: 0, scale: 1, rotate: 0, opacity: 1, reveal: 1, ease: 'out' }]),
  }).strict()
  const TRAILER_AUDIO = z.object({
    kind: z.enum(['music', 'voiceover', 'scene-audio']),
    assetId: id,
    startFrame: frame,
    durationFrames: frame.min(1),
    trimStartFrame: frame.default(0),
    volume: z.number().min(0).max(1).default(1),
    fadeInFrames: frame.default(0),
    fadeOutFrames: frame.default(12),
    // Explicit local gain envelope for ducks, score drops and impacts. No guessed beat detection.
    gainKeys: z.array(z.object({ frame, gain: z.number().min(0).max(1) }).strict()).max(32).default([]),
  }).strict()
  const TRAILER_SPEC = z.object({
    title: z.string().trim().min(1).max(120),
    mode: z.enum(['cinematic', 'product-hype']),
    durationFrames: frame.min(150),
    aspectRatio: z.enum(['9:16', '16:9']).default('16:9'),
    background: color.default('#080a12'),
    layers: z.array(TRAILER_LAYER).min(1).max(80),
    audio: z.array(TRAILER_AUDIO).max(16).default([]),
  }).strict()
  return { TRAILER_SPEC, TRAILER_LAYER, TRAILER_AUDIO, MOTION_KEY }
}

export const { TRAILER_SPEC, TRAILER_LAYER, TRAILER_AUDIO, MOTION_KEY } = createTrailerSchemas(z)
export type TrailerSpec = z.infer<typeof TRAILER_SPEC>
export type TrailerLayer = z.infer<typeof TRAILER_LAYER>
export type TrailerAudio = z.infer<typeof TRAILER_AUDIO>
export type MotionKey = z.infer<typeof MOTION_KEY>

export function validateTrailer(spec: TrailerSpec): string[] {
  const errors: string[] = []
  for (const [i, layer] of spec.layers.entries()) {
    const label = `Layer ${i + 1}`
    if (layer.startFrame + layer.durationFrames > spec.durationFrames) errors.push(`${label} exceeds the trailer.`)
    if (layer.kind === 'text' && !layer.text) errors.push(`${label} needs text.`)
    if (layer.kind === 'image' && !layer.imageId) errors.push(`${label} needs imageId.`)
    if (layer.kind === 'video' && !layer.videoId) errors.push(`${label} needs videoId.`)
    if (layer.kind !== 'image' && layer.imageId) errors.push(`${label}: imageId only belongs on an image.`)
    if (layer.kind !== 'video' && layer.videoId) errors.push(`${label}: videoId only belongs on a video.`)
    if (layer.keys[0].frame !== 0) errors.push(`${label}: first key must be at local frame 0.`)
    layer.keys.forEach((key, j) => {
      if (key.frame >= layer.durationFrames) errors.push(`${label}: key exceeds its local duration.`)
      if (j > 0 && key.frame <= layer.keys[j - 1].frame) errors.push(`${label}: keys must increase strictly.`)
    })
  }
  for (const [i, audio] of spec.audio.entries()) {
    const label = `Audio ${i + 1}`
    if (audio.startFrame + audio.durationFrames > spec.durationFrames) errors.push(`${label} exceeds the trailer.`)
    if (audio.fadeInFrames + audio.fadeOutFrames > audio.durationFrames) errors.push(`${label}: fades exceed duration.`)
    audio.gainKeys.forEach((key, j) => {
      if (key.frame >= audio.durationFrames) errors.push(`${label}: gain key exceeds duration.`)
      if (j > 0 && key.frame <= audio.gainKeys[j - 1].frame) errors.push(`${label}: gain keys must increase strictly.`)
    })
  }
  const assetIds = new Set([
    ...spec.layers.flatMap((l) => [l.imageId, l.videoId].filter(Boolean)),
    ...spec.audio.map((a) => a.assetId),
  ])
  if (assetIds.size > 80) errors.push('At most 80 distinct media assets may be used.')
  // Bound concurrent decoding independently of total layer count.
  const videos = spec.layers.filter((l) => l.kind === 'video')
  if (videos.some((a) => videos.filter((b) =>
    b.startFrame <= a.startFrame && b.startFrame + b.durationFrames > a.startFrame).length > 4)) {
    errors.push('At most four videos may play at once.')
  }
  return errors
}

export const TRAILER_PROPS = z.object({ spec: TRAILER_SPEC, assets: z.record(z.string()) })
export type TrailerProps = z.infer<typeof TRAILER_PROPS>
