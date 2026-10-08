import React from 'react'
import { Img, useVideoConfig } from 'remotion'
import { inter } from './fonts'
import type { AdTheme } from '../theme'

interface BrandTagProps {
  theme: AdTheme
  brand: { name: string; logoUrl?: string }
  onFootage?: boolean
}

/**
 * The small logo-and-name tag that sits bottom-left on every canvas beat and the end card. It does not pop in:
 * it is a tag that stays, and re-popping at every cut reads as a blink.
 */
export const BrandTag: React.FC<BrandTagProps> = ({ theme, brand, onFootage }) => {
  const { width, height } = useVideoConfig()
  const u = Math.min(width, height)
  const color = onFootage ? theme.footageFg : theme.canvasMuted
  return (
    <div style={{ position: 'absolute', left: u * 0.06, bottom: u * 0.05 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: u * 0.01 }}>
        {brand.logoUrl ? <Img src={brand.logoUrl} style={{ height: u * 0.045, width: 'auto' }} /> : null}
        <span
          style={{
            fontFamily: inter.fontFamily,
            fontWeight: 600,
            fontSize: u * 0.022,
            color,
            letterSpacing: '0.01em',
          }}
        >
          {brand.name}
        </span>
      </div>
    </div>
  )
}
