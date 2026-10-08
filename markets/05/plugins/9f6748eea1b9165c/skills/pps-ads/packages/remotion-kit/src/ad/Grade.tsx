import React from 'react'
import { AbsoluteFill } from 'remotion'
import type { AdTheme } from '../theme'

/** A 4% contrast lift and a 3% tint toward the canvas so a warm clip and a cool card read as one ad. */
export const Grade: React.FC<{ theme: AdTheme; children: React.ReactNode }> = ({ theme, children }) => (
  <AbsoluteFill style={{ filter: 'contrast(1.04)' }}>
    {children}
    <AbsoluteFill
      style={{
        background: theme.canvas === 'light' ? theme.accent : theme.canvasBg,
        opacity: 0.03,
        mixBlendMode: 'soft-light',
        pointerEvents: 'none',
      }}
    />
  </AbsoluteFill>
)
