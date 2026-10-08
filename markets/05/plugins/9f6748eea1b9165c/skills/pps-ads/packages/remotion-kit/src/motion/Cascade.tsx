import React from 'react'
import { SlideFade } from './SlideFade'

/** Children enter one after another, each a SlideFade, staggered by `stepSeconds`. */
export const Cascade: React.FC<{
  children: React.ReactNode[]
  stepSeconds?: number
  from?: 'up' | 'down' | 'left' | 'right'
  /** Per-child delay in seconds (for example from staggerOnGrid); wins over stepSeconds. */
  times?: number[]
}> = ({ children, stepSeconds = 0.18, from = 'up', times }) => (
  <>
    {React.Children.map(children, (child, index) => (
      <SlideFade delaySeconds={times?.[index] ?? index * stepSeconds} from={from}>
        {child}
      </SlideFade>
    ))}
  </>
)
