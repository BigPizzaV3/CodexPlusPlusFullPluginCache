import React from 'react'
import { TrailerComposition } from './trailer/TrailerComposition'
import { TRAILER_PROPS, TRAILER_SPEC } from './trailer/schema'
import { Composition, type CalculateMetadataFunction } from 'remotion'
import { AdComposition } from './ad/AdComposition'
import { AD_COMPOSITION_PROPS, adDurationInFrames, type AdCompositionProps } from './ad/schema'
import { FPS, sizeFor } from './motion/timing'
import fixture15 from './fixtures/ad-15.json'

// Duration and canvas come from the spec, so one composition id serves every length and shape.
const calculateMetadata: CalculateMetadataFunction<AdCompositionProps> = async ({ props }) => ({
  durationInFrames: adDurationInFrames(props),
  ...sizeFor(props.spec.aspectRatio),
  fps: FPS,
})

export const RemotionRoot: React.FC = () => (
  <>
  <Composition
    id="AdComposition"
    component={AdComposition}
    schema={AD_COMPOSITION_PROPS}
    defaultProps={fixture15 as AdCompositionProps}
    calculateMetadata={calculateMetadata}
    durationInFrames={450}
    fps={FPS}
    width={1080}
    height={1920}
  />
  <Composition id="TrailerComposition" component={TrailerComposition} schema={TRAILER_PROPS}
    defaultProps={{ spec: TRAILER_SPEC.parse({ title: 'Trailer', mode: 'product-hype', durationFrames: 150,
      layers: [{ kind: 'text', startFrame: 0, durationFrames: 150, text: 'MAKE IT CINEMATIC', x: 10, y: 40, width: 80 }] }), assets: {} }}
    calculateMetadata={({ props }) => ({ durationInFrames: props.spec.durationFrames, ...sizeFor(props.spec.aspectRatio), fps: FPS })}
    durationInFrames={150} fps={FPS} width={1920} height={1080} />
  </>
)
