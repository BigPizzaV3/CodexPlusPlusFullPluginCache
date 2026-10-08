import { z } from 'zod'
import { AD_FORMATS, ASPECT_RATIOS, BEAT_TYPES } from '../grammar'
import { frames } from '../motion/timing'

/**
 * What the worker hands the composition: the connector's ad spec with every asset id swapped for a
 * URL (worker/remotion/node/render.mjs does the swap from the request's `assets` map), so the kit
 * renders the same from PPS and from a developer's machine.
 */
const CaptionWord = z.object({ text: z.string(), start: z.number(), end: z.number() })
const CaptionGroup = z.object({ text: z.string(), start: z.number(), end: z.number(), words: z.array(CaptionWord) })

export const AD_COMPOSITION_PROPS = z.object({
  spec: z.object({
    title: z.string(),
    format: z.enum(AD_FORMATS).optional(),
    lengthSeconds: z.union([z.literal(15), z.literal(30), z.literal(60)]),
    aspectRatio: z.enum(ASPECT_RATIOS),
    brand: z.object({
      name: z.string(),
      color: z.string().optional(),
      logoUrl: z.string().optional(),
      canvas: z.enum(['light', 'dark']).optional(),
    }),
    musicUrl: z.string().optional(),
    musicTempo: z.enum(['slow', 'mid', 'fast']).optional(),
    beats: z.array(
      z.object({
        type: z.enum(BEAT_TYPES),
        start: z.number(),
        end: z.number(),
        text: z.string().optional(),
        subtitle: z.string().optional(),
        kicker: z.string().optional(),
        partner: z.string().optional(),
        lines: z.array(z.string()).optional(),
        punchline: z.boolean().optional(),
        clipUrl: z.string().optional(),
        clipUrls: z.array(z.string()).optional(),
        imageUrls: z.array(z.string()).optional(),
        thumbnailUrl: z.string().optional(),
        pickIndex: z.number().int().min(0).optional(),
        frame: z.enum(['phone', 'laptop']).optional(),
        inner: z.enum(['prompt', 'agent', 'results']).optional(),
        captions: z.boolean().optional(),
        captionAccent: z.array(z.string()).optional(),
        captionGroups: z.array(CaptionGroup).optional(),
        voiceoverUrl: z.string().optional(),
        /** The take's own length, filled server-side; the music ducks for exactly this long. */
        voiceoverSeconds: z.number().positive().optional(),
      }),
    ),
  }),
})
export type AdCompositionProps = z.infer<typeof AD_COMPOSITION_PROPS>

export function adDurationInFrames(props: AdCompositionProps): number {
  return frames(props.spec.lengthSeconds)
}
