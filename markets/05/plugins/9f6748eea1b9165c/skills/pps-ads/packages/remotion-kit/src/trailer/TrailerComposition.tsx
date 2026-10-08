import React from 'react'
import { AbsoluteFill, Img, Sequence, useCurrentFrame, useVideoConfig } from 'remotion'
import { Audio, Video } from '@remotion/media'
import { bricolage, inter } from '../ad/fonts'
import { audioGainAt, poseAt } from './motion'
import { type TrailerAudio, type TrailerLayer, type TrailerProps, TRAILER_SPEC, validateTrailer } from './schema'

const Layer: React.FC<{ layer: TrailerLayer; assets: Record<string, string> }> = ({ layer, assets }) => {
  const frame = useCurrentFrame()
  const { width, height } = useVideoConfig()
  const pose = poseAt(layer.keys, frame)
  const style: React.CSSProperties = {
    position: 'absolute', left: `${layer.x}%`, top: `${layer.y}%`, width: `${layer.width}%`, height: `${layer.height}%`,
    transform: `translate(${pose.x * width / 100}px, ${pose.y * height / 100}px) scale(${pose.scale}) rotate(${pose.rotate}deg)`,
    opacity: pose.opacity, overflow: 'hidden', borderRadius: layer.kind === 'ellipse' ? '50%' : layer.radius,
    clipPath: `inset(0 ${(1 - pose.reveal) * 100}% 0 0)`,
    background: layer.background ?? (layer.kind === 'rect' || layer.kind === 'ellipse' ? layer.color : undefined),
    border: layer.borderWidth ? `${layer.borderWidth}px solid ${layer.borderColor}` : undefined,
    boxSizing: 'border-box',
  }
  return <div style={style}>
    {layer.kind === 'text' ? <div style={{
      fontFamily: layer.font === 'display' ? bricolage.fontFamily : layer.font === 'mono' ? 'monospace' : inter.fontFamily,
      fontSize: layer.fontSize * width / 100, fontWeight: Number(layer.weight), color: layer.color,
      textAlign: layer.align, lineHeight: 1.12, whiteSpace: 'pre-wrap', overflowWrap: 'break-word',
    }}>{layer.text}</div> : null}
    {layer.kind === 'cursor' ? <svg viewBox="0 0 32 40" width="100%" height="100%">
      <path d="M3 2 L27 25 L17 25 L22 36 L16 39 L11 28 L3 35 Z" fill={layer.color} stroke="#10131a" strokeWidth="2" />
    </svg> : null}
    {layer.kind === 'image' ? <Img src={assets[layer.imageId!]} style={{ width: '100%', height: '100%', objectFit: layer.fit }} /> : null}
    {layer.kind === 'video' ? <Video src={assets[layer.videoId!]} trimBefore={layer.trimStartFrame}
      volume={layer.volume} style={{ width: '100%', height: '100%' }} objectFit={layer.fit} /> : null}
  </div>
}

const AudioLayer: React.FC<{ audio: TrailerAudio; src: string }> = ({ audio, src }) => {
  const frame = useCurrentFrame()
  return <Audio src={src} trimBefore={audio.trimStartFrame} volume={audioGainAt(audio, frame)} />
}

export const TrailerComposition: React.FC<TrailerProps> = ({ spec: rawSpec, assets }) => {
  const spec = TRAILER_SPEC.parse(rawSpec)
  const errors = validateTrailer(spec)
  if (errors.length) throw new Error(errors.join(' '))
  for (const id of [...spec.layers.flatMap((l) => [l.videoId, l.imageId]), ...spec.audio.map((a) => a.assetId)]) {
    if (id && !assets[id]) throw new Error(`Missing trailer asset: ${id}`)
  }
  return <AbsoluteFill style={{ background: spec.background }}>
    {spec.layers.map((layer, i) => <Sequence key={i} from={layer.startFrame} durationInFrames={layer.durationFrames}>
      <Layer layer={layer} assets={assets} />
    </Sequence>)}
    {spec.audio.map((audio, i) => <Sequence key={`a${i}`} from={audio.startFrame} durationInFrames={audio.durationFrames}>
      <AudioLayer audio={audio} src={assets[audio.assetId]} />
    </Sequence>)}
  </AbsoluteFill>
}
